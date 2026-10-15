"""Expand an evaluated case into a read-only agent task manifest.

The host agent performs authorized retrieval; this module makes no external calls.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
from . import engine as E

def build_plan(c):
 r=E.evaluate(c);tasks=[]
 for issue in r['issues']:
  tasks.append({'id':issue['id'],'kind':'scope_or_inventory','priority':0,'next_action':issue['message'],'assignee':'filer_or_preparer','status':'open'})
 for q in r['questions']:
  if q['state']not in ['unanswered','conflict']:continue
  spec=E.QUESTIONS[q['id']]
  tasks.append({'id':q['key'],'kind':'confirm_fact','priority':1,'next_action':q['prompt'],'module':q['module'],'instance_id':q['entity_id'],'entity_label':q['entity_label'],'answer_type':spec['type'],'choices':spec.get('choices'),'opening_condition':spec['when'],'source_refs':spec['sources'],'status':q['state'],'assignee':'filer_or_authorized_evidence_agent','constraint':'Do not convert inference into a confirmed answer without a cited basis; do not infer no from missing documents.'})
 for d in r['evidence']:
  if d['status']in ['verified','alternative_accepted','not_required']:continue
  spec=E.CAT['documents'][d['document_id']];ent=E.entity(c,d['module'],d['entity_id']);owners=[p['label'] for p in c['entities']['PERSON'] if p['id']in ent['owner_ids']]
  terms=[t.replace('{tax_year}',str(c['catalog_year'])).replace('{entity_label}',d['entity_label']).replace('{owner}',' '.join(owners)) for t in spec['search_terms']]
  tasks.append({'id':d['key'],'kind':'evidence','priority':d['priority'],'next_action':'Reverify against changed facts' if d['status']=='stale' else ('Extract and reconcile the located document' if d['status']=='located' else 'Search authorized locations; otherwise ask the filer for this record'),'module':d['module'],'instance_id':d['entity_id'],'entity_label':d['entity_label'],'owner_ids':ent['owner_ids'],'document_title':d['title'],'document_kind':spec['kind'],'required_fields':spec['fields'],'candidate_search_locations':spec['search_locations'],'search_terms':terms,'acceptance':spec['acceptance'],'fallback':spec['alternatives'],'status':d['status'],'fingerprint':d['fingerprint'],'activated_by':d['rules'],'permission':'Candidate search locations are NOT authorization. Check the approved source scope before each access.'})
 for f in r['form_candidates']:
  if f['status']in ['required','not_required']:continue
  tasks.append({'id':f['key'],'kind':'form_applicability','priority':2,'next_action':'Document whether this form is required after reviewing eligibility, exceptions, authority and supporting facts.','form':f['id'],'lane':f['lane'],'assembly_unit':E.CAT['form_aggregation_units'].get(f['id'],'Verify person/entity/return aggregation in applicable instructions.'),'reasons':f['reasons'],'source_refs':f['sources'],'entity_label':f['entity_label'],'fingerprint':f['fingerprint'],'assignee':'qualified_preparer_or_approved_rule_adapter','status':f['status']})
 for kind,key in [('technical_review','reviews'),('cross_topic_route','routes')]:
  for x in r[key]:
   if x['status']=='resolved':continue
   tasks.append({'id':x['key'],'kind':kind,'priority':0 if kind=='technical_review' else 1,'next_action':x['instruction'],'entity_label':x['entity_label'],'destination':x.get('destination'),'assignee':'preparer_or_rules_agent_with_required_review','status':x['status'],'fingerprint':x['fingerprint']})
 tasks.sort(key=lambda t:(t['priority'],t['kind'],t['id']))
 return {'schema_version':'2.0','case_id':c['case_id'],'tax_year':c['catalog_year'],'readiness':r['readiness'],'summary':r['summary'],'permissions':'No external access, communication, filing, payments or elections granted by this manifest.','task_count':len(tasks),'tasks':tasks,'still_waiting_on_upstream':r['summary']['questions_blocked_by_upstream'],'coverage_warning':E.CAT['scope']}
