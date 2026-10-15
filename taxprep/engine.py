"""Deterministic conditional intake evaluator, not a tax-computation engine.

Use the public ``taxprep`` CLI for transactional writes and reports.
"""
from __future__ import annotations
import argparse, json, math, copy
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict, deque
from importlib import resources
from typing import Any
ROOT=Path(__file__).resolve().parent
CAT=json.loads(resources.files('taxprep').joinpath('catalog.json').read_text(encoding='utf-8'))
MOD={m['id']:m for m in CAT['modules']}; QUESTIONS={q['id']:q for q in CAT['questions']}
LOCAL=defaultdict(list)
for q in CAT['questions']:LOCAL[q['module']].append(q)
INACTIVE=object()

def now():return datetime.now(timezone.utc).isoformat()
def canonical(x):return json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':'))
def digest(x):
    # UTF-8 FNV-1a fingerprint for local invalidation, NOT for cryptographic integrity.
    h=2166136261
    for b in canonical(x).encode('utf-8'):h=((h^b)*16777619)&0xffffffff
    return f'{h:08x}'
def answer_record(value,*,status='confirmed',source='user',reference='explicit questionnaire answer'):
    if status not in ['confirmed','tentative','conflict']:raise ValueError('Invalid answer status')
    return {'value':value,'status':status,'source':source,'reference':reference,'at':now()}
def known(rec):
    return rec.get('value') if isinstance(rec,dict) and rec.get('status')=='confirmed' else None

def new_case():
    c={'schema_version':'2.0','catalog_year':2025,'case_id':'new-case','created_at':now(),'screens':{},'entities':{},'enumerated':{},'evidence':{},'reviews':{},'form_decisions':{},'route_decisions':{},'audit':[]}
    for m in CAT['modules']:
        id=m['id'];c['entities'][id]=[]
        if m['screen']:c['screens'][id]=None
        if not m['repeatable']:c['entities'][id]=[{'id':'return','label':'Return','owner_ids':[],'answers':{}}]
    return c

def entity(c,m,e):
    return next(x for x in c['entities'].get(m,[]) if x['id']==e)
def audit(c,action,subject,old,new):
    c['audit'].append({'at':now(),'action':action,'subject':subject,'before':copy.deepcopy(old),'after':copy.deepcopy(new)})
def set_screen(c,m,value,status='confirmed'):
    if MOD[m]['screen'] is None:raise ValueError('Mandatory module has no screening answer')
    if value is not None and type(value) is not bool:raise ValueError('Screen must be boolean or unknown')
    old=c['screens'].get(m);v=None if value is None else answer_record(value,status=status)
    c['screens'][m]=v;audit(c,'screen',m,old,v)
def add_entity(c,m,label,owner_ids=None,eid=None):
    if not MOD[m]['repeatable']:raise ValueError('Not repeatable')
    if not label.strip():raise ValueError('Entity label required')
    items=c['entities'].setdefault(m,[])
    eid=eid or ('e'+str(max([int(x['id'][1:]) for x in items if x['id'].startswith('e') and x['id'][1:].isdigit()]+[0])+1))
    if any(x['id']==eid for x in items):raise ValueError('Duplicate entity ID')
    obj={'id':eid,'label':label.strip(),'owner_ids':list(owner_ids or []),'answers':{}}
    items.append(obj);c['enumerated'].pop(m,None);audit(c,'add_entity',m+'/'+eid,None,obj.copy());return obj

def validate_answer(q,value):
    if value is None:return
    t=q['type']
    if t=='boolean' and type(value) is not bool:raise ValueError('Expected true or false')
    if t=='number' and (type(value) not in (int,float) or (type(value) is float and not math.isfinite(value))):raise ValueError('Expected finite number')
    if t in ['text','date','enum'] and (not isinstance(value,str) or not value.strip()):raise ValueError('Expected nonblank text')
    if t=='date':datetime.strptime(value,'%Y-%m-%d')
    if t=='enum' and value not in q['choices']:raise ValueError('Invalid choice')

def set_answer(c,m,e,qid,value,status='confirmed',source='user',reference='explicit questionnaire answer'):
    q=QUESTIONS[qid]
    if q['module']!=m:raise ValueError('Question/entity scope mismatch')
    validate_answer(q,value);x=entity(c,m,e)
    old=x['answers'].get(qid);rec=None if value is None else answer_record(value,status=status,source=source,reference=reference)
    x['answers'][qid]=rec;audit(c,'answer',m+'/'+e+'/'+qid,old,rec)

def mark_enumerated(c,m,complete=True):
    if not MOD[m]['repeatable']:raise ValueError('Not repeatable')
    n=len(c['entities'].get(m,[]))
    if complete and not n:raise ValueError('Cannot confirm an empty active roster')
    c['enumerated'][m]={'complete':complete,'entity_ids':sorted(x['id'] for x in c['entities'][m]),'at':now(),'source':'user'}
    audit(c,'enumeration',m,None,c['enumerated'][m])

def refs(cond):
    if isinstance(cond,bool):return set()
    out={cond['fact']} if 'fact'in cond else set()
    for x in cond.get('args',[]):out|=refs(x)
    if 'arg'in cond:out|=refs(cond['arg'])
    return out

def tri(cond,fetch):
    if isinstance(cond,bool):return cond
    op=cond['op']
    if op in ['all','any']:
        vs=[tri(a,fetch) for a in cond['args']]
        if op=='all':return False if False in vs else (None if None in vs else True)
        return True if True in vs else (None if None in vs else False)
    if op=='not':
        v=tri(cond['arg'],fetch);return None if v is None else not v
    v=fetch(cond['fact'])
    if v is INACTIVE:return False
    if v is None:return None # unanswered is not false, even for ne or answered
    if op=='answered':return True
    rhs=cond.get('value')
    if op=='eq':return type(v)==type(rhs) and v==rhs if isinstance(v,bool) or isinstance(rhs,bool) else v==rhs
    if op=='ne':return v!=rhs
    if op=='in':return v in rhs
    if type(v) not in [int,float] or type(rhs) not in [int,float]:raise ValueError('Numeric predicate requires numbers')
    return {'gt':lambda:v>rhs,'ge':lambda:v>=rhs,'lt':lambda:v<rhs,'le':lambda:v<=rhs}[op]()

def module_status(c,m):return True if MOD[m]['screen'] is None else known(c['screens'].get(m))
def fingerprint(c,m,e):
    # Conservative invalidation: global scope/household changes invalidate all units;
    # local answers invalidate only their unit. Audit timestamps do not alter it.
    def slim(ent):return {'id':ent['id'],'owner_ids':ent.get('owner_ids',[]),'answers':{k:{'value':r.get('value'),'status':r.get('status')} if isinstance(r,dict) else None for k,r in ent.get('answers',{}).items()}}
    context={'year':c.get('catalog_year'),'scope':{k:known(v) for k,v in c['screens'].items()},'global':{k:[slim(z) for z in c['entities'].get(k,[])] for k in ['CORE','PERSON','STATUS','STATE']},'local':slim(entity(c,m,e))}
    return digest(context)

def inspect_instance(c,m,x):
    cache={};vis={};visiting=set()
    def value(ref):
        if ref.startswith('$screen.'):
            z=module_status(c,ref.split('.',1)[1]);return z
        ref=ref.removeprefix('$')
        q=QUESTIONS.get(ref)
        if q is None:raise ValueError('Unknown fact '+ref)
        if q['module']!=m:
            candidates=c['entities'].get(q['module'],[])
            if MOD[q['module']]['repeatable']:raise ValueError('Cross-instance fact requires an explicit aggregate; raw reference forbidden')
            if not candidates:return None
            other=inspect_instance(c,q['module'],candidates[0]);z=other['questions_by_id'][ref]
            return INACTIVE if z['visibility'] is False else (z['value'] if z['visibility'] is True else None)
        if ref in cache:return cache[ref]
        if ref in visiting:raise ValueError('Cycle in questions')
        visiting.add(ref)
        visible=tri(q['when'],value);vis[ref]=visible
        rec=x['answers'].get(ref);v=known(rec)
        cache[ref]=INACTIVE if visible is False else (v if visible is True else None)
        visiting.remove(ref);return cache[ref]
    rows=[]
    for q in LOCAL[m]:
        v=value(q['id']);rec=x['answers'].get(q['id']);visibility=vis[q['id']]
        state='not_applicable' if visibility is False else ('blocked_by_upstream' if visibility is None else ('answered' if v is not None else ('conflict' if isinstance(rec,dict) and rec.get('status')=='conflict' else 'unanswered')))
        rows.append({'id':q['id'],'visibility':visibility,'state':state,'value':None if v is INACTIVE else v,'record':rec,'prompt':q['prompt']})
    return {'questions':rows,'questions_by_id':{q['id']:q for q in rows},'eval':lambda cond:tri(cond,value)}

def nonblank(value):
    return isinstance(value,str) and bool(value.strip())

def valid_resolution(rec,sig):
    return bool(rec and rec.get('status')=='resolved' and rec.get('fingerprint')==sig and all(nonblank(rec.get(k)) for k in ['note','reference','actor']))
def support_status(rec,sig):
    if not rec:return 'missing'
    status=rec.get('status','missing')
    if status in ['verified','alternative_accepted','not_required']:
        if rec.get('fingerprint')!=sig:return 'stale'
        if not all(nonblank(rec.get(k)) for k in ['reference','note','actor']):return 'located' if nonblank(rec.get('reference')) else 'missing'
        if status!='not_required' and not all(rec.get('checks',{}).get(k) is True for k in ['year','owner','entity','complete','corrections','reconciled']):return 'located'
    return status

def evaluate(c):
    validate_case(c)
    out={'case_id':c['case_id'],'tax_year':c['catalog_year'],'readiness':'OPEN','screens':[],'modules':[],'questions':[],'evidence':[],'form_candidates':[],'reviews':[],'routes':[],'issues':[],'inactive_evidence_preserved':0,'authorization':'Preparation organization only; no filing, contact, payment or election authorization.'}
    all_required=set();fmap={}
    people={x['id'] for x in c['entities'].get('PERSON',[])}
    if c['catalog_year']!=2025:out['issues'].append({'id':'YEAR','message':'Unsupported catalog year; load a verified tax-year pack.'})
    core=c['entities'].get('CORE',[{'answers':{}}])[0]['answers']
    actual_year=known(core.get('CORE.year'))
    if actual_year is not None and actual_year!=2025:out['issues'].append({'id':'ACTUAL_YEAR','message':'The answered tax year is not 2025. Rule-version block cannot be waived.'})
    if known(core.get('CORE.person_type')) is False:out['issues'].append({'id':'NONINDIVIDUAL','message':'This is not an individual return; load the correct scope.'})
    for cx in c['entities'].get('CLOSE',[]):
        for qid,rec in cx['answers'].items():
            if QUESTIONS[qid]['type']=='boolean' and known(rec) is False:out['issues'].append({'id':'final/'+qid,'message':'Completeness check is not satisfied: '+QUESTIONS[qid]['prompt']})
    for m in CAT['modules']:
        mid=m['id'];ms=module_status(c,mid);entities=c['entities'].get(mid,[])
        out['screens'].append({'module':mid,'value':ms,'mandatory':m['screen'] is None})
        if ms is None:
            out['issues'].append({'id':'screen/'+mid,'message':'Confirm whether this category applies: '+m['title']});continue
        if ms is False:
            out['modules'].append({'id':mid,'state':'not_applicable','entities':len(entities)});continue
        if m['repeatable']:
            sealed=c['enumerated'].get(mid,{})
            if not entities:out['issues'].append({'id':'enumerate/'+mid,'message':'Identify at least one '+m['unit']+' for '+m['title']})
            if not sealed.get('complete') or sealed.get('entity_ids')!=sorted(x['id'] for x in entities):out['issues'].append({'id':'roster/'+mid,'message':'Confirm all '+m['unit']+' instances have been identified.'})
        out['modules'].append({'id':mid,'state':'active','entities':len(entities)})
        for x in entities:
            prefix=mid+'/'+x['id'];sig=fingerprint(c,mid,x['id']);ctx=inspect_instance(c,mid,x)
            if m['repeatable'] and mid!='PERSON' and (not x.get('owner_ids') or any(p not in people for p in x.get('owner_ids',[]))):
                out['issues'].append({'id':prefix+'/owner','message':'Assign valid person IDs to '+x['label']})
            for row in ctx['questions']:
                out['questions'].append({**row,'key':prefix+'/'+row['id'],'module':mid,'entity_id':x['id'],'entity_label':x['label']})
            for r in (r for r in CAT['rules'] if r['module']==mid):
                rv=ctx['eval'](r['when'])
                if rv is not True:continue # unresolved predicates are visible through unresolved question nodes
                rid=prefix+'/'+r['id']
                for did in r['documents']:
                    key=prefix+'/evidence/'+did;all_required.add(key)
                    existing=next((d for d in out['evidence'] if d['key']==key),None)
                    if existing:
                        existing['rules'].append(r['id']);continue
                    rec=c['evidence'].get(key);out['evidence'].append({'key':key,'module':mid,'entity_id':x['id'],'entity_label':x['label'],'document_id':did,'title':CAT['documents'][did]['title'],'status':support_status(rec,sig),'record':rec,'fingerprint':sig,'rules':[r['id']],'priority':r['priority']})
                for f in r['forms']:
                    key=prefix+'/form/'+f['id'];rec=c['form_decisions'].get(key)
                    status='candidate'
                    if rec:
                        if rec.get('fingerprint')!=sig:status='stale'
                        elif rec.get('decision') in ['required','not_required'] and all(nonblank(rec.get(k)) for k in ['actor','note','reference']):status=rec['decision']
                    if key not in fmap:fmap[key]={'key':key,'module':mid,'entity_id':x['id'],'entity_label':x['label'],'id':f['id'],'lane':f['lane'],'status':status,'reasons':[],'sources':[],'record':rec,'fingerprint':sig}
                    fmap[key]['reasons'].append(r['title']);fmap[key]['sources']+=r['sources']
                if r['review']:
                    key=rid+'/review';rec=c['reviews'].get(key)
                    state='resolved' if valid_resolution(rec,sig) else ('stale' if rec and rec.get('status')=='resolved' else 'open')
                    out['reviews'].append({'key':key,'module':mid,'entity_id':x['id'],'entity_label':x['label'],'rule':r['id'],'title':r['title'],'instruction':r['review'],'status':state,'fingerprint':sig,'record':rec})
            for r in (r for r in CAT['routes'] if r['module']==mid):
                if ctx['eval'](r['when']) is not True:continue
                key=prefix+'/'+r['id'];rec=c['route_decisions'].get(key)
                out['routes'].append({'key':key,'module':mid,'entity_id':x['id'],'entity_label':x['label'],'destination':r['destination'],'instruction':r['instruction'],'status':'resolved' if valid_resolution(rec,sig) else 'open','record':rec,'fingerprint':sig})
    out['form_candidates']=list(fmap.values())
    for f in out['form_candidates']:f['sources']=sorted(set(f['sources']))
    out['inactive_evidence_preserved']=len(set(c['evidence'])-all_required)
    out['summary']={'unanswered_screens':sum(s['value'] is None for s in out['screens']),
        'active_unanswered_questions':sum(q['state'] in ['unanswered','conflict'] for q in out['questions']),
        'questions_blocked_by_upstream':sum(q['state']=='blocked_by_upstream' for q in out['questions']),
        'answered_questions':sum(q['state']=='answered' for q in out['questions']),
        'required_evidence_items':len(out['evidence']),
        'unverified_evidence_items':sum(d['status'] not in ['verified','alternative_accepted','not_required'] for d in out['evidence']),
        'form_candidates':len(fmap),'form_decisions_open':sum(f['status'] in ['candidate','stale'] for f in fmap.values()),
        'reviews_open':sum(r['status']!='resolved' for r in out['reviews']),
        'routes_open':sum(r['status']!='resolved' for r in out['routes']),'scope_and_inventory_issues':len(out['issues'])}
    blocking=['unanswered_screens','active_unanswered_questions','questions_blocked_by_upstream','unverified_evidence_items','form_decisions_open','reviews_open','routes_open','scope_and_inventory_issues']
    out['readiness']='READY_FOR_PREPARER_REVIEW' if all(out['summary'][k]==0 for k in blocking) else 'OPEN'
    return out

def validate_catalog():
    nodes=set();edges=[]
    for m in CAT['modules']:nodes.add('screen.'+m['id'])
    if len(QUESTIONS)!=len(CAT['questions']):raise ValueError('Duplicate question IDs')
    for q in CAT['questions']:
        nodes.add(q['id']);edges.append(('screen.'+q['module'],q['id']))
        for ref in refs(q['when']):
            ref=ref.removeprefix('$')
            if ref not in QUESTIONS:raise ValueError('Invalid question reference '+ref)
            if QUESTIONS[ref]['module']!=q['module'] and MOD[QUESTIONS[ref]['module']]['repeatable']:raise ValueError('Unscoped cross-entity reference')
            edges.append((ref,q['id']))
    seen=set()
    for r in CAT['rules']:
        nid='rule.'+r['id']
        if nid in seen:raise ValueError('Duplicate rule ID')
        seen.add(nid);nodes.add(nid);edges.append(('screen.'+r['module'],nid))
        for ref in refs(r['when']):
            ref=ref.removeprefix('$')
            if ref not in QUESTIONS:raise ValueError('Invalid rule fact '+ref)
            edges.append((ref,nid))
        for did in r['documents']:
            if did not in CAT['documents']:raise ValueError('Missing document '+did)
            dn='evidence.'+r['module']+'.'+did;nodes.add(dn);edges.append((nid,dn))
        for f in r['forms']:
            fn='form.'+r['module']+'.'+f['id'];nodes.add(fn);edges.append((nid,fn))
        for s in r['sources']:
            if s not in CAT['sources']:raise ValueError('Missing authority')
    # Cross-module routes are downstream tasks, NOT backward edges modifying screens.
    for r in CAT['routes']:
        n='task.'+r['id'];nodes.add(n)
        for ref in refs(r['when']):edges.append((ref,n))
        if r['destination']not in MOD:raise ValueError('Bad route target')
    indeg={n:0 for n in nodes};adj=defaultdict(list)
    for a,b in set(edges):indeg[b]+=1;adj[a].append(b)
    dq=deque(sorted(n for n,d in indeg.items() if d==0));order=[]
    while dq:
        a=dq.popleft();order.append(a)
        for b in sorted(adj[a]):
            indeg[b]-=1
            if indeg[b]==0:dq.append(b)
    if len(order)!=len(nodes):raise ValueError('Cycle detected')
    return {'valid':True,'nodes':len(nodes),'edges':len(set(edges)),'topological_order':order,'graph_edges':sorted(set(edges))}

def validate_case(c):
    """Validate imported structure without mistaking incomplete work for closure.

    Missing review fields remain open. Supplied fields must have the expected
    types, and task keys must identify a real catalog task for a known instance.
    Valid but stale roster seals and unresolved owner references remain report
    issues so a saved case can be inspected and repaired.
    """
    def text_fields(record, fields, context):
        for field in fields:
            if field in record and not isinstance(record[field],str):
                raise ValueError(f'{context}.{field} must be a string')

    def answer(rec, context):
        if rec is None:return
        if not isinstance(rec,dict) or rec.get('status') not in ['confirmed','tentative','conflict']:
            raise ValueError('Invalid answer record: '+context)
        text_fields(rec,['source','reference','at'],context)

    def identity(value):
        return nonblank(value) and '/' not in value

    required=['schema_version','catalog_year','case_id','screens','entities','enumerated','evidence','reviews','form_decisions','route_decisions','audit']
    if not isinstance(c,dict) or any(k not in c for k in required):
        raise ValueError('Invalid case: missing required fields')
    for key in ['screens','entities','enumerated','evidence','reviews','form_decisions','route_decisions']:
        if not isinstance(c[key],dict):raise ValueError('Expected object: '+key)
    if c['schema_version']!='2.0':raise ValueError('Unsupported case schema version')
    if type(c['catalog_year']) is not int:raise ValueError('Invalid catalog year')
    if not nonblank(c['case_id']):raise ValueError('Case ID required')
    text_fields(c,['created_at','updated_at'],'case')
    if not isinstance(c['audit'],list):raise ValueError('Audit must be an array')
    for record in c['audit']:
        if not isinstance(record,dict):raise ValueError('Audit entries must be objects')
        text_fields(record,['at','action','subject'],'audit')

    expected_screens={m['id'] for m in CAT['modules'] if m['screen']}
    if set(c['screens'])!=expected_screens:raise ValueError('Screen inventory does not match this catalog')
    for mid,rec in c['screens'].items():
        answer(rec,'screen/'+mid)
        if rec is not None and rec.get('value') is not None and type(rec.get('value')) is not bool:
            raise ValueError('Screen answers must be boolean or unknown records')

    if set(c['entities'])!=set(MOD):raise ValueError('Every catalog module must be present in the case')
    for mid,items in c['entities'].items():
        if not isinstance(items,list):raise ValueError('Entity inventory must be an array: '+mid)
        ids=set()
        for x in items:
            if not isinstance(x,dict) or any(k not in x for k in ['id','label','answers','owner_ids']):
                raise ValueError('Invalid entity: '+mid)
            if not identity(x['id']) or not nonblank(x['label']) or not isinstance(x['answers'],dict):
                raise ValueError('Invalid entity identity or answers: '+mid)
            owners=x['owner_ids']
            if not isinstance(owners,list) or any(not identity(p) for p in owners) or len(set(owners))!=len(owners):
                raise ValueError('Invalid entity ownership fields: '+mid)
            if x['id'] in ids:raise ValueError('Duplicate entity IDs: '+mid)
            ids.add(x['id'])
            for qid,rec in x['answers'].items():
                if qid not in QUESTIONS or QUESTIONS[qid]['module']!=mid:raise ValueError('Wrong question scope')
                answer(rec,qid)
                if rec is not None:validate_answer(QUESTIONS[qid],rec.get('value'))
        if not MOD[mid]['repeatable'] and (len(items)!=1 or items[0]['id']!='return'):
            raise ValueError('Singleton module requires return entity: '+mid)

    for mid,record in c['enumerated'].items():
        if mid not in MOD or not MOD[mid]['repeatable']:
            raise ValueError('Unknown or nonrepeatable roster: '+str(mid))
        if not isinstance(record,dict) or type(record.get('complete')) is not bool:
            raise ValueError('Roster complete must be a boolean: '+mid)
        ids=record.get('entity_ids')
        if not isinstance(ids,list) or any(not identity(eid) for eid in ids) or len(set(ids))!=len(ids):
            raise ValueError('Roster entity_ids must be unique entity ID strings: '+mid)
        text_fields(record,['source','reference','at'],'enumerated/'+mid)

    possible={key:set() for key in ['evidence','reviews','form_decisions','route_decisions']}
    for mid,items in c['entities'].items():
        rules=[r for r in CAT['rules'] if r['module']==mid]
        routes=[r for r in CAT['routes'] if r['module']==mid]
        for x in items:
            prefix=mid+'/'+x['id']
            for rule in rules:
                possible['evidence'].update(prefix+'/evidence/'+did for did in rule['documents'])
                possible['form_decisions'].update(prefix+'/form/'+f['id'] for f in rule['forms'])
                if rule['review']:possible['reviews'].add(prefix+'/'+rule['id']+'/review')
            possible['route_decisions'].update(prefix+'/'+route['id'] for route in routes)
    evidence_states=['missing','searching','located','verified','rejected','alternative_accepted','not_required','stale']
    checks=['year','owner','entity','complete','corrections','reconciled']
    for collection,keys in possible.items():
        for key,record in c[collection].items():
            if key not in keys:raise ValueError('Unknown '+collection+' task key: '+str(key))
            if not isinstance(record,dict):raise ValueError('Task records must be objects: '+key)
            text_fields(record,['fingerprint','actor','reference','note','at','source_version','sha256'],key)
            if collection=='evidence':
                if 'status' in record and record['status'] not in evidence_states:
                    raise ValueError('Invalid evidence status: '+key)
                if 'checks' in record:
                    values=record['checks']
                    if not isinstance(values,dict) or any(k not in checks or type(v) is not bool for k,v in values.items()):
                        raise ValueError('Evidence checks must be named booleans: '+key)
            elif collection=='form_decisions':
                if 'decision' in record and record['decision'] not in ['candidate','required','not_required','stale']:
                    raise ValueError('Invalid form decision: '+key)
            elif 'status' in record and record['status'] not in ['open','resolved','stale']:
                raise ValueError('Invalid resolution status: '+key)
    return True

def write_report_md(report,path):
    s=report['summary'];lines=['# Tax preparation open-items report','',f"Case: {report['case_id']} | Tax year: {report['tax_year']} | Status: {report['readiness']}",'','This is an organization report, not a filed return or a tax calculation.','', '## Summary','']
    lines += [f'- {k.replace("_"," ")}: {v}'for k,v in s.items()]
    lines+=['','## Scope and entity inventory','']+[f"- {i['message']}"for i in report['issues']]
    lines+=['','## Questions needing a confirmed answer','']+[f"- [{q['module']} / {q['entity_label']}] {q['prompt']} ({q['state']})"for q in report['questions'] if q['state'] in ['unanswered','conflict']]
    lines+=['','## Evidence still open','']+[f"- [{d['entity_label']}] {d['title']} — {d['status']} (`{d['key']}`)"for d in report['evidence'] if d['status']not in ['verified','alternative_accepted','not_required']]
    lines+=['','## Form applicability decisions','']+[f"- {f['id']} / {f['entity_label']} — {f['status']}; {f['lane']}"for f in report['form_candidates']]
    lines+=['','## Reviews and linked tracks','']+[f"- [{r['entity_label']}] {r.get('instruction')} — {r['status']}"for r in report['reviews']+report['routes'] if r['status']!='resolved']
    Path(path).write_text('\n'.join(lines)+'\n')

