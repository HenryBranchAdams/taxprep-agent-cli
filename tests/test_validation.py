"""Import and closure boundaries for cases supplied by an agent or the UI."""
import copy
import json
from pathlib import Path
import unittest

from taxprep import engine as E


class CaseValidationTests(unittest.TestCase):
    def case(self):
        case = E.new_case()
        E.add_entity(case, 'PERSON', 'Example person', eid='p')
        E.set_screen(case, 'WAGE', True)
        E.add_entity(case, 'WAGE', 'Example employer', ['p'], eid='w')
        E.set_answer(case, 'WAGE', 'w', 'WAGE.foreign', True)
        return case

    def closure(self, item, **changes):
        return {
            'status': 'verified',
            'fingerprint': item['fingerprint'],
            'actor': 'Example reviewer',
            'reference': 'fixture://w2/page1',
            'note': 'Matched the source to this task.',
            'checks': dict.fromkeys(
                ['year', 'owner', 'entity', 'complete', 'corrections', 'reconciled'], True
            ),
            **changes,
        }

    def evidence(self, case):
        return next(x for x in E.evaluate(case)['evidence'] if x['key'] == 'WAGE/w/evidence/W2')

    def test_original_example_imports_and_retains_verification(self):
        root = Path(__file__).resolve().parents[1]
        case = json.loads((root / 'examples' / 'fictional_case.json').read_text())
        self.assertTrue(E.validate_case(case))
        item = next(x for x in E.evaluate(case)['evidence'] if x['key'] == 'WAGE/northstar/evidence/W2')
        self.assertEqual(item['status'], 'verified')

    def test_malformed_singleton_is_validation_error(self):
        for value in [None, {}, [], [None], [{}], ['return'], [True]]:
            with self.subTest(value=value):
                case = E.new_case()
                case['entities']['CORE'] = value
                with self.assertRaises(ValueError):
                    E.evaluate(case)

    def test_roster_requires_typed_complete_and_unique_ids(self):
        for record in [None, 'bad', {}, {'complete': 'false', 'entity_ids': ['p']},
                       {'complete': 1, 'entity_ids': ['p']},
                       {'complete': True, 'entity_ids': 'p'},
                       {'complete': True, 'entity_ids': ['p', 'p']},
                       {'complete': True, 'entity_ids': [None]}]:
            with self.subTest(record=record):
                case = self.case()
                case['enumerated']['PERSON'] = record
                with self.assertRaises(ValueError):
                    E.evaluate(case)

    def test_stale_roster_stays_an_open_issue(self):
        case = self.case()
        case['enumerated']['PERSON'] = {'complete': True, 'entity_ids': ['earlier-person']}
        self.assertTrue(E.validate_case(case))
        self.assertIn('roster/PERSON', {x['id'] for x in E.evaluate(case)['issues']})

    def test_unknown_roster_module_is_rejected(self):
        for module in ['MADE_UP', 'CORE']:
            with self.subTest(module=module):
                case = self.case()
                case['enumerated'][module] = {'complete': False, 'entity_ids': []}
                with self.assertRaises(ValueError):
                    E.validate_case(case)

    def test_unresolved_owner_reference_remains_repairable(self):
        case = self.case()
        E.entity(case, 'WAGE', 'w')['owner_ids'] = ['missing-person']
        self.assertTrue(E.validate_case(case))
        self.assertIn('WAGE/w/owner', {x['id'] for x in E.evaluate(case)['issues']})

    def test_unknown_task_keys_are_rejected(self):
        cases = [
            ('evidence', 'UNKNOWN/w/evidence/W2'),
            ('evidence', 'WAGE/unknown/evidence/W2'),
            ('evidence', 'WAGE/w/evidence/MADE_UP'),
            ('evidence', 'WAGE/w/evidence/IRA_HISTORY'),
            ('form_decisions', 'WAGE/w/form/MADE_UP'),
            ('reviews', 'WAGE/w/MADE_UP/review'),
            ('route_decisions', 'WAGE/w/route.MADE_UP'),
        ]
        for collection, key in cases:
            with self.subTest(collection=collection, key=key):
                case = self.case()
                case[collection][key] = {}
                with self.assertRaises(ValueError):
                    E.validate_case(case)

    def test_malformed_evidence_fields_are_rejected(self):
        changes = [
            {'actor': True}, {'reference': 123}, {'note': []}, {'fingerprint': 1},
            {'status': 'done'}, {'checks': None}, {'checks': []},
            {'checks': {'year': 1}}, {'checks': {'invented': True}},
        ]
        for change in changes:
            with self.subTest(change=change):
                case = self.case()
                item = self.evidence(case)
                case['evidence'][item['key']] = self.closure(item, **change)
                with self.assertRaises(ValueError):
                    E.evaluate(case)

    def test_missing_closure_fields_remain_open(self):
        for field in ['actor', 'reference', 'note', 'fingerprint', 'checks']:
            with self.subTest(field=field):
                case = self.case()
                item = self.evidence(case)
                record = self.closure(item)
                del record[field]
                case['evidence'][item['key']] = record
                self.assertTrue(E.validate_case(case))
                self.assertNotIn(self.evidence(case)['status'], ['verified', 'alternative_accepted', 'not_required'])

    def test_whitespace_cannot_close_evidence_form_review_or_route(self):
        for field in ['actor', 'reference', 'note']:
            with self.subTest(field=field):
                case = self.case()
                report = E.evaluate(case)
                evidence = self.evidence(case)
                case['evidence'][evidence['key']] = self.closure(evidence, **{field: ' \t '})
                for collection, report_key in [('form_decisions', 'form_candidates'),
                                                ('reviews', 'reviews'),
                                                ('route_decisions', 'routes')]:
                    item = report[report_key][0]
                    record = self.closure(item, **{field: ' \t '})
                    record.pop('checks')
                    record.pop('status')
                    record.update({'decision': 'required'} if collection == 'form_decisions' else {'status': 'resolved'})
                    case[collection][item['key']] = record
                result = E.evaluate(case)
                self.assertNotEqual(self.evidence(case)['status'], 'verified')
                self.assertNotEqual(result['form_candidates'][0]['status'], 'required')
                self.assertNotEqual(result['reviews'][0]['status'], 'resolved')
                self.assertNotEqual(result['routes'][0]['status'], 'resolved')

    def test_invalid_decision_and_resolution_states_are_rejected(self):
        for collection, report_key, field in [('form_decisions', 'form_candidates', 'decision'),
                                               ('reviews', 'reviews', 'status'),
                                               ('route_decisions', 'routes', 'status')]:
            with self.subTest(collection=collection):
                case = self.case()
                item = E.evaluate(case)[report_key][0]
                case[collection][item['key']] = {field: 'done'}
                with self.assertRaises(ValueError):
                    E.validate_case(case)

    def test_inactive_valid_evidence_is_preserved(self):
        case = self.case()
        item = self.evidence(case)
        case['evidence'][item['key']] = self.closure(item)
        E.set_screen(case, 'WAGE', False)
        self.assertTrue(E.validate_case(case))
        self.assertEqual(E.evaluate(case)['inactive_evidence_preserved'], 1)

    def test_source_change_fingerprint_marker_is_accepted_and_stale(self):
        case = self.case()
        item = self.evidence(case)
        case['evidence'][item['key']] = self.closure(item, fingerprint='source-changed:2026-10-15T00:00:00Z')
        self.assertTrue(E.validate_case(case))
        self.assertEqual(self.evidence(case)['status'], 'stale')

    def test_malformed_answer_metadata_is_rejected(self):
        case = self.case()
        E.entity(case, 'WAGE', 'w')['answers']['WAGE.foreign']['source'] = True
        with self.assertRaises(ValueError):
            E.validate_case(case)

    def test_audit_snapshots_do_not_follow_later_entity_changes(self):
        case = E.new_case()
        E.add_entity(case, 'PERSON', 'Example person', eid='p')
        before = copy.deepcopy(case['audit'][0])
        E.set_answer(case, 'PERSON', 'p', 'PERSON.age', 35)
        self.assertEqual(case['audit'][0], before)

    def test_form_task_ids_can_contain_slashes(self):
        case = self.case()
        E.add_entity(case, 'HOUSEHOLD', 'Household employment', ['p'], eid='h')
        key = 'HOUSEHOLD/h/form/W-2 / W-3'
        case['form_decisions'][key] = {}
        self.assertTrue(E.validate_case(case))


if __name__ == '__main__':
    unittest.main()
