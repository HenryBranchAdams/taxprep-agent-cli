"""Revision comparisons describe workflow changes, not tax conclusions."""
import copy
import json
import unittest

from taxprep import engine as E
from taxprep.changes import compare_cases, compare_snapshots
from taxprep.errors import AppError
from taxprep.operations import CHECKS, apply_operations


class ChangeTests(unittest.TestCase):
    def base(self, module="DIGITAL", ids=("account",)):
        case = E.new_case()
        case["case_id"] = "fictional-change-fixture"
        E.add_entity(case, "PERSON", "Fictional person", eid="p")
        E.set_screen(case, module, True)
        for identity in ids:
            E.add_entity(case, module, "Fictional " + identity, ["p"], eid=identity)
        return case

    def apply(self, case, *operations):
        return apply_operations(case, {"operations": list(operations)}, "fixture-agent")

    def answer(self, key, value, **fields):
        return {"op": "answer", "key": key, "value": value, "source": "fictional intake",
                "reference": "fixture://intake", **fields}

    def verify(self, case, key):
        row = next(item for item in E.evaluate(case)["evidence"] if item["key"] == key)
        return self.apply(case, {"op": "evidence", "key": key, "status": "verified",
                                 "fingerprint": row["fingerprint"],
                                 "checks": {check: True for check in CHECKS},
                                 "reference": "fixture://document-v1", "source_version": "v1",
                                 "note": "Fictional completed checks"})

    def find(self, rows, key):
        return next(row for row in rows if row["key"] == key)

    def test_unknown_true_adds_issued_document_requirement(self):
        before = self.base()
        after = self.apply(before, self.answer("DIGITAL/account/DIGITAL.broker_form", True))
        result = compare_cases(before, after)
        key = "DIGITAL/account/evidence/DIGITAL.doc_broker_form"
        row = self.find(result["tasks"]["added"], key)
        self.assertEqual(row, {"key": key, "kind": "evidence", "before": None,
                               "after": {"state": "missing"}})
        self.assertEqual(result["summary"]["required_evidence_items"]["delta"], 1)
        self.assertEqual(result["counts"]["tasks_reopened"], 0)
        self.assertEqual(result["readiness"], {"before": "OPEN", "after": "OPEN"})

    def test_unknown_false_deactivates_children_without_counting_completion(self):
        before = self.base("WAGE", ("job",))
        after = self.apply(before, self.answer("WAGE/job/WAGE.overtime", False))
        result = compare_cases(before, after)
        child = self.find(result["tasks"]["changed"], "WAGE/job/WAGE.flsa")
        self.assertEqual(child["before"], {"state": "blocked_by_upstream", "visibility": None})
        self.assertEqual(child["after"], {"state": "not_applicable", "visibility": False})
        self.assertFalse(result["tasks"]["reopened"])
        self.assertNotIn("completed", result["tasks"])

    def test_disappearing_requirement_is_removed_not_reopened_or_verified(self):
        before = self.apply(self.base(), self.answer("DIGITAL/account/DIGITAL.broker_form", True))
        after = self.apply(before, self.answer("DIGITAL/account/DIGITAL.broker_form", False))
        result = compare_cases(before, after)
        key = "DIGITAL/account/evidence/DIGITAL.doc_broker_form"
        row = self.find(result["tasks"]["removed"], key)
        self.assertEqual(row["before"], {"state": "missing"})
        self.assertIsNone(row["after"])
        self.assertNotIn(key, [item["key"] for item in result["tasks"]["reopened"]])
        self.assertTrue(any("not evidence" in text for text in result["caveats"]))

    def test_source_change_reopens_verified_evidence_without_changing_answers(self):
        key = "WAGE/job/evidence/W2"
        before = self.verify(self.base("WAGE", ("job",)), key)
        after = self.apply(before, {"op": "source_change", "key": key,
                                    "reference": "fixture://document-v2", "source_version": "v2",
                                    "note": "Fictional corrected source"})
        result = compare_cases(before, after)
        row = self.find(result["tasks"]["reopened"], key)
        self.assertEqual(row["before"]["state"], "verified")
        self.assertEqual(row["after"]["state"], "stale")
        self.assertIn(row, result["tasks"]["changed"])
        self.assertEqual(result["records"]["answers"], [])
        source = self.find(result["records"]["evidence"], key)
        self.assertEqual(source["before"]["value"]["source_version"], "v1")
        self.assertEqual(source["after"]["value"]["source_version"], "v2")
        self.assertEqual(result["summary"]["unverified_evidence_items"]["delta"], 1)

    def test_repeated_entities_keep_distinct_task_and_answer_keys(self):
        before = self.base("WAGE", ("job", "other"))
        before = self.verify(before, "WAGE/job/evidence/W2")
        before = self.verify(before, "WAGE/other/evidence/W2")
        after = self.apply(before, self.answer("WAGE/job/WAGE.tips", True))
        result = compare_cases(before, after)
        self.assertIn("WAGE/job/evidence/W2", [item["key"] for item in result["tasks"]["reopened"]])
        self.assertNotIn("WAGE/other/evidence/W2", [item["key"] for item in result["tasks"]["changed"]])
        self.assertEqual([item["key"] for item in result["records"]["answers"]], ["WAGE/job/WAGE.tips"])

    def test_source_change_reports_every_reopened_review_kind(self):
        case = self.base("WAGE", ("job",))
        case = self.apply(case, self.answer("WAGE/job/WAGE.foreign", True),
                          self.answer("WAGE/job/WAGE.misclassified", True))
        case = self.verify(case, "WAGE/job/evidence/W2")
        report = E.evaluate(case)
        form = next(row for row in report["form_candidates"] if row["key"] == "WAGE/job/form/1040")
        operations = [{"op": "decision", "key": form["key"], "decision": "required",
                       "fingerprint": form["fingerprint"], "reference": "fixture://review",
                       "note": "Fictional applicability review"}]
        for section, kind in (("reviews", "review"), ("routes", "route")):
            operations += [{"op": "resolve", "kind": kind, "key": row["key"],
                            "fingerprint": row["fingerprint"], "reference": "fixture://review",
                            "note": "Fictional review"}
                           for row in report[section] if row["module"] == "WAGE"]
        before = self.apply(case, *operations)
        after = self.apply(before, {"op": "source_change", "key": "WAGE/job/evidence/W2",
                                    "reference": "fixture://document-v2", "source_version": "v2",
                                    "note": "Fictional corrected source"})
        result = compare_cases(before, after)
        self.assertEqual({row["kind"] for row in result["tasks"]["reopened"]},
                         {"evidence", "form_applicability", "technical_review", "cross_topic_route"})
        self.assertEqual(self.find(result["tasks"]["reopened"], form["key"])["after"]["state"], "stale")
        self.assertTrue(result["records"]["reviews"])
        self.assertTrue(result["records"]["route_decisions"])

    def test_household_fact_change_reopens_closures_in_both_instances(self):
        before = self.base("WAGE", ("job", "other"))
        before = self.verify(before, "WAGE/job/evidence/W2")
        before = self.verify(before, "WAGE/other/evidence/W2")
        after = self.apply(before, self.answer("PERSON/p/PERSON.age", 40))
        result = compare_cases(before, after)
        reopened = {row["key"] for row in result["tasks"]["reopened"]}
        self.assertTrue({"WAGE/job/evidence/W2", "WAGE/other/evidence/W2"}.issubset(reopened))

    def test_confirmed_fact_becoming_unknown_reopens_without_inferring_false(self):
        before = self.apply(self.base(), self.answer("DIGITAL/account/DIGITAL.broker_form", True))
        after = self.apply(before, self.answer("DIGITAL/account/DIGITAL.broker_form", None))
        result = compare_cases(before, after)
        row = self.find(result["tasks"]["reopened"], "DIGITAL/account/DIGITAL.broker_form")
        self.assertEqual(row["before"]["state"], "answered")
        self.assertEqual(row["after"]["state"], "unanswered")
        self.assertEqual(result["records"]["answers"][0]["after"]["value"]["value"], None)

    def test_absent_and_explicit_unknown_are_distinct_records(self):
        before = self.base()
        after = copy.deepcopy(before)
        after["entities"]["DIGITAL"][0]["answers"]["DIGITAL.broker_form"] = None
        result = compare_cases(before, after)
        row = self.find(result["records"]["answers"], "DIGITAL/account/DIGITAL.broker_form")
        self.assertEqual(row["before"], {"present": False, "value": None})
        self.assertEqual(row["after"], {"present": True, "value": None})
        self.assertEqual(row["change"], "added")
        self.assertFalse(result["tasks"]["changed"])

    def test_timestamp_noise_is_ignored_but_reference_change_is_recorded(self):
        before = self.apply(self.base(), self.answer("DIGITAL/account/DIGITAL.broker_form", False))
        after = copy.deepcopy(before)
        after["audit"].append({"at": "later", "action": "fixture", "subject": "fixture"})
        after["updated_at"] = "later"
        after["entities"]["DIGITAL"][0]["answers"]["DIGITAL.broker_form"]["at"] = "later"
        self.assertEqual(compare_cases(before, after)["counts"]["record_changes"], 0)
        after["entities"]["DIGITAL"][0]["answers"]["DIGITAL.broker_form"]["reference"] = "fixture://new"
        result = compare_cases(before, after)
        self.assertEqual(result["counts"]["record_changes"], 1)
        self.assertEqual(result["counts"]["tasks_changed"], 0)

    def test_roster_and_entity_metadata_changes_are_separate_from_answers(self):
        before = self.base()
        before = self.apply(before, {"op": "enumerate", "module": "DIGITAL", "complete": True,
                                     "source": "fixture", "reference": "fixture://roster"})
        after = self.apply(before, {"op": "entity_add", "module": "DIGITAL", "id": "new",
                                    "label": "Fictional second exchange", "owner_ids": ["p"]})
        result = compare_cases(before, after)
        self.assertEqual(self.find(result["records"]["entities"], "DIGITAL/new")["change"], "added")
        self.assertEqual(self.find(result["records"]["enumerated"], "DIGITAL")["change"], "removed")
        self.assertEqual(result["records"]["answers"], [])

    def test_noop_is_deterministic_serializable_and_does_not_mutate_inputs(self):
        before = self.base()
        after = self.apply(before, self.answer("DIGITAL/account/DIGITAL.broker_form", True))
        original_before, original_after = copy.deepcopy(before), copy.deepcopy(after)
        result = compare_cases(before, after)
        self.assertEqual(result, compare_cases(before, after))
        json.dumps(result, allow_nan=False)
        self.assertEqual(before, original_before)
        self.assertEqual(after, original_after)
        result["records"]["answers"][0]["after"]["value"]["value"] = False
        self.assertEqual(after, original_after)
        noop = compare_cases(before, before)
        self.assertTrue(all(count == 0 for count in noop["counts"].values()))

    def test_snapshot_revisions_and_reverse_direction(self):
        before = self.base()
        after = self.apply(before, self.answer("DIGITAL/account/DIGITAL.broker_form", True))
        result = compare_snapshots({"revision": 4, "case": after}, {"revision": 2, "case": before})
        self.assertEqual((result["from_revision"], result["to_revision"]), (4, 2))
        self.assertEqual(result["summary"]["required_evidence_items"]["delta"], -1)
        self.assertEqual(result["records"]["answers"][0]["change"], "removed")

    def test_different_cases_are_not_compared(self):
        before = self.base()
        after = copy.deepcopy(before)
        after["case_id"] = "different-case"
        with self.assertRaises(AppError) as error:
            compare_cases(before, after)
        self.assertEqual(error.exception.code, "case_mismatch")


if __name__ == "__main__":
    unittest.main()
