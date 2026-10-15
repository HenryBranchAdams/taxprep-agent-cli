"""Behavioral tests only: these do not certify tax-law accuracy or completeness."""
import copy,json,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from taxprep import engine as E
class EngineTests(unittest.TestCase):
 def base(self,mid=None):
  c=E.new_case();E.add_entity(c,'PERSON','Fictional Person',eid='p');E.mark_enumerated(c,'PERSON')
  if mid:
   E.set_screen(c,mid,True);E.add_entity(c,mid,'Fictional '+mid,['p'],eid='one');E.mark_enumerated(c,mid)
  return c
 def put(self,c,m,q,v,e='one',**kw):E.set_answer(c,m,e,m+'.'+q,v,**kw)
 def forms(self,c,m):return {r['id'] for r in E.evaluate(c)['form_candidates'] if r['module']==m}
 def docs(self,c,m):return {r['document_id'] for r in E.evaluate(c)['evidence'] if r['module']==m}
 def verification(self,c,key):
  d=next(x for x in E.evaluate(c)['evidence'] if x['key']==key)
  c['evidence'][key]={'status':'verified','fingerprint':d['fingerprint'],'reference':'fixture://record/page1','actor':'Fixture reviewer','note':'Verified fixture','checks':{k:True for k in ['year','owner','entity','complete','corrections','reconciled']}}
 def state(self,c,key):return next(x['status'] for x in E.evaluate(c)['evidence'] if x['key']==key)
 def test_graph_is_acyclic(self):self.assertTrue(E.validate_catalog()['valid'])
 def test_catalog_exact_shape(self):self.assertEqual(len(E.CAT['questions']),466);self.assertEqual(len(E.CAT['modules']),35)
 def test_every_question_has_authority(self):self.assertTrue(all(q['sources'] for q in E.CAT['questions']))
 def test_every_rule_doc_reference_exists(self):self.assertTrue(all(d in E.CAT['documents'] for r in E.CAT['rules'] for d in r['documents']))
 def test_unknown_eq_is_unknown(self):self.assertIsNone(E.tri({'op':'eq','fact':'x','value':True},lambda _:None))
 def test_unknown_ne_is_unknown(self):self.assertIsNone(E.tri({'op':'ne','fact':'x','value':True},lambda _:None))
 def test_and_false_dominates_unknown(self):self.assertFalse(E.tri({'op':'all','args':[False,{'op':'eq','fact':'x','value':True}]},lambda _:None))
 def test_or_true_dominates_unknown(self):self.assertTrue(E.tri({'op':'any','args':[True,{'op':'eq','fact':'x','value':True}]},lambda _:None))
 def test_unknown_screen_not_no(self):r=E.evaluate(E.new_case());self.assertEqual(r['summary']['unanswered_screens'],26);self.assertEqual(r['readiness'],'OPEN')
 def test_true_screen_reveals_instance_work(self):c=self.base('WAGE');self.assertIn('W2',self.docs(c,'WAGE'))
 def test_parent_false_hides_stale_yes_child(self):
  c=self.base('WAGE');self.put(c,'WAGE','overtime',True);self.put(c,'WAGE','flsa',True);self.put(c,'WAGE','overtime_detail',True);self.put(c,'WAGE','overtime',False)
  q=E.inspect_instance(c,'WAGE',c['entities']['WAGE'][0])['questions_by_id']['WAGE.flsa'];self.assertEqual(q['state'],'not_applicable')
 def test_unknown_parent_blocks_children(self):
  c=self.base('WAGE');q=E.inspect_instance(c,'WAGE',c['entities']['WAGE'][0])['questions_by_id']['WAGE.flsa'];self.assertEqual(q['state'],'blocked_by_upstream')
 def test_two_employers_independent(self):
  c=self.base('WAGE');E.add_entity(c,'WAGE','Employer two',['p'],eid='two');self.verification(c,'WAGE/one/evidence/W2');self.assertEqual(self.state(c,'WAGE/one/evidence/W2'),'verified');self.assertEqual(self.state(c,'WAGE/two/evidence/W2'),'missing')
 def test_conversion_requires_basis_and_dec31(self):
  c=self.base('RETIRE');self.put(c,'RETIRE','conversion',True);self.put(c,'RETIRE','nondeductible',False);self.assertTrue({'IRA_HISTORY','IRA_DEC31'}<=self.docs(c,'RETIRE'));self.assertIn('8606',self.forms(c,'RETIRE'))
 def test_roth_contribution_not_schedule1(self):
  c=self.base('RETIRE');self.put(c,'RETIRE','type','Roth IRA');self.put(c,'RETIRE','contribution',True);self.assertNotIn('Schedule 1',self.forms(c,'RETIRE'))
 def test_rmd_alone_no_5329(self):
  c=self.base('RETIRE');self.put(c,'RETIRE','rmd',True);self.put(c,'RETIRE','rmd_shortfall',False);self.assertNotIn('5329',self.forms(c,'RETIRE'))
 def test_hsa_idle_no_8889(self):
  c=self.base('HSA');self.put(c,'HSA','type','HSA')
  for q in ['contribution','distribution','lastmonth','carry_issue','excess']:self.put(c,'HSA',q,False)
  self.assertNotIn('8889',self.forms(c,'HSA'))
 def test_hsa_distribution_requires_support(self):c=self.base('HSA');self.put(c,'HSA','type','HSA');self.put(c,'HSA','distribution',True);self.assertIn('8889',self.forms(c,'HSA'));self.assertIn('HSA_MED',self.docs(c,'HSA'))
 def test_crypto_transfer_only_not_8949(self):
  c=self.base('DIGITAL');self.put(c,'DIGITAL','transfer',True);self.put(c,'DIGITAL','fee_crypto',False);self.put(c,'DIGITAL','disposal',False);self.assertNotIn('8949',self.forms(c,'DIGITAL'))
 def test_crypto_fee_disposition_8949(self):
  c=self.base('DIGITAL');self.put(c,'DIGITAL','transfer',True);self.put(c,'DIGITAL','fee_crypto',True);self.assertIn('8949',self.forms(c,'DIGITAL'))
 def test_corporation_is_not_schedule_c(self):
  c=self.base('BUSINESS');self.put(c,'BUSINESS','structure','S corporation');self.put(c,'BUSINESS','expenses',True);self.put(c,'BUSINESS','inventory',True);self.assertNotIn('Schedule C',self.forms(c,'BUSINESS'));self.assertIn('1120-S',self.forms(c,'BUSINESS'))
 def test_separate_lane_for_entity(self):
  c=self.base('BUSINESS');self.put(c,'BUSINESS','structure','C corporation');f=next(f for f in E.evaluate(c)['form_candidates'] if f['id']=='1120');self.assertEqual(f['lane'],'separate_obligation_or_procedure')
 def test_enumeration_invalidated_by_new_entity(self):
  c=self.base('WAGE');E.add_entity(c,'WAGE','New employer',['p']);self.assertIn('roster/WAGE',{i['id'] for i in E.evaluate(c)['issues']})
 def test_owner_unknown_blocks(self):
  c=self.base('WAGE');c['entities']['WAGE'][0]['owner_ids']=['nonexistent'];self.assertIn('WAGE/one/owner',{i['id'] for i in E.evaluate(c)['issues']})
 def test_verified_requires_reviewer(self):
  c=self.base('WAGE');k='WAGE/one/evidence/W2';self.verification(c,k);del c['evidence'][k]['actor'];self.assertEqual(self.state(c,k),'located')
 def test_verified_requires_all_checks(self):
  c=self.base('WAGE');k='WAGE/one/evidence/W2';self.verification(c,k);c['evidence'][k]['checks']['complete']=False;self.assertEqual(self.state(c,k),'located')
 def test_fact_change_stales_support(self):
  c=self.base('WAGE');k='WAGE/one/evidence/W2';self.verification(c,k);self.put(c,'WAGE','tips',True);self.assertEqual(self.state(c,k),'stale')
 def test_other_instance_change_does_not_stale(self):
  c=self.base('WAGE');E.add_entity(c,'WAGE','Other employer',['p'],eid='two');k='WAGE/one/evidence/W2';self.verification(c,k);self.put(c,'WAGE','tips',True,e='two');self.assertEqual(self.state(c,k),'verified')
 def test_global_household_change_stales(self):
  c=self.base('WAGE');k='WAGE/one/evidence/W2';self.verification(c,k);self.put(c,'PERSON','age',60,e='p');self.assertEqual(self.state(c,k),'stale')
 def test_inactive_support_is_preserved(self):
  c=self.base('WAGE');k='WAGE/one/evidence/W2';self.verification(c,k);E.set_screen(c,'WAGE',False);self.assertEqual(E.evaluate(c)['inactive_evidence_preserved'],1);self.assertIn(k,c['evidence'])
 def test_year_mismatch_hard_block(self):
  c=self.base();self.put(c,'CORE','year',2026,e='return');self.assertIn('ACTUAL_YEAR',{i['id'] for i in E.evaluate(c)['issues']})
 def test_negative_final_check_blocks(self):
  c=self.base();self.put(c,'CLOSE','all_people',False,e='return');self.assertIn('final/CLOSE.all_people',{i['id'] for i in E.evaluate(c)['issues']})
 def test_tentative_is_not_confirmed(self):
  c=self.base('WAGE');self.put(c,'WAGE','tips',True,status='tentative');q=E.inspect_instance(c,'WAGE',c['entities']['WAGE'][0])['questions_by_id']['WAGE.tips'];self.assertEqual(q['state'],'unanswered')
 def test_conflict_is_open(self):
  c=self.base('WAGE');self.put(c,'WAGE','tips',True,status='conflict');q=E.inspect_instance(c,'WAGE',c['entities']['WAGE'][0])['questions_by_id']['WAGE.tips'];self.assertEqual(q['state'],'conflict')
 def test_invalid_enum_rejected(self):
  with self.assertRaises(ValueError):self.put(self.base('RETIRE'),'RETIRE','type','Invented account')
 def test_wrong_question_scope_rejected(self):
  c=self.base('WAGE');c['entities']['WAGE'][0]['answers']['RETIRE.type']=E.answer_record('Roth IRA')
  with self.assertRaises(ValueError):E.validate_case(c)
 def test_invalid_screen_rejected(self):
  c=self.base();c['screens']['WAGE']=E.answer_record('Yes')
  with self.assertRaises(ValueError):E.validate_case(c)
 def test_form_not_automatically_required(self):
  c=self.base('RETIRE');self.put(c,'RETIRE','conversion',True);self.assertEqual(next(f['status'] for f in E.evaluate(c)['form_candidates'] if f['id']=='8606'),'candidate')
 def test_route_cannot_be_cleared_by_no(self):
  c=self.base('WAGE');self.put(c,'WAGE','foreign',True);E.set_screen(c,'FOREIGN',False);self.assertEqual(next(r['status'] for r in E.evaluate(c)['routes'] if r['destination']=='FOREIGN'),'open')
 def test_explicit_audit(self):
  c=self.base('WAGE');n=len(c['audit']);self.put(c,'WAGE','tips',True);self.assertEqual(len(c['audit']),n+1)
 def test_demo_independent_missing_documents(self):
  c=json.loads((Path(__file__).resolve().parents[1]/'examples/fictional_case.json').read_text());r=E.evaluate(c);states={d['key']:d['status'] for d in r['evidence']};self.assertEqual(states['WAGE/northstar/evidence/W2'],'verified');self.assertEqual(states['WAGE/harbor/evidence/W2'],'missing');self.assertEqual(states['RETIRE/ira/evidence/IRA_HISTORY'],'missing')
 def test_other_selection_requires_extension_review(self):
  c=self.base('RETIRE');self.put(c,'RETIRE','type','Other');r=E.evaluate(c);self.assertTrue(any(x['rule']=='RETIRE.unmodeled_type' and x['status']=='open' for x in r['reviews']))
 def test_agent_plan_includes_search_and_acceptance(self):
  from taxprep import planner as agent_plan
  c=self.base('WAGE');plan=agent_plan.build_plan(c);t=next(x for x in plan['tasks'] if x['id']=='WAGE/one/evidence/W2');self.assertTrue(t['search_terms']);self.assertTrue(t['required_fields']);self.assertTrue(t['acceptance']);self.assertIn('NOT authorization',t['permission'])
if __name__=='__main__':unittest.main(verbosity=2)
