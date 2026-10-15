"""Regression exposed by the real FTX/Coinbase case."""
import unittest
from taxprep import engine as E

class BrokerFormTests(unittest.TestCase):
    def case(self):
        case=E.new_case()
        E.add_entity(case,'PERSON','Fixture',eid='p')
        E.set_screen(case,'DIGITAL',True)
        E.add_entity(case,'DIGITAL','Fixture exchange',['p'],eid='account')
        return case

    def test_issued_notice_creates_specific_missing_form_task(self):
        case=self.case()
        E.set_answer(case,'DIGITAL','account','DIGITAL.broker_form',True)
        report=E.evaluate(case)
        key='DIGITAL/account/evidence/DIGITAL.doc_broker_form'
        row=next(x for x in report['evidence'] if x['key']==key)
        self.assertEqual(row['status'],'missing')
        self.assertEqual(row['priority'],0)
        self.assertFalse(any(f['module']=='DIGITAL' for f in report['form_candidates']))

    def test_false_or_unknown_does_not_invent_an_issued_form(self):
        for value in (None,False):
            case=self.case()
            if value is not None:E.set_answer(case,'DIGITAL','account','DIGITAL.broker_form',value)
            self.assertFalse(any(x['document_id']=='DIGITAL.doc_broker_form' for x in E.evaluate(case)['evidence']))
