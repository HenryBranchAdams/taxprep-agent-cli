"""Mutation boundary tests; these do not certify legal or tax conclusions."""
import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from taxprep import engine as E
from taxprep.errors import AppError
from taxprep.operations import CHECKS, apply_operations, operation_schema


class OperationTests(unittest.TestCase):
    def apply(self, case, *ops, actor="test-agent"):
        return apply_operations(case, {"operations": list(ops)}, actor)

    def answer(self, key, value, **kw):
        return {"op": "answer", "key": key, "value": value, "source": "fictional intake",
                "reference": "fixture://intake/1", **kw}

    def screen(self, mid, value, **kw):
        return {"op": "screen", "module": mid, "value": value, "source": "fictional intake",
                "reference": "fixture://intake/1", **kw}

    def base(self):
        return self.apply(E.new_case(),
                          {"op": "entity_add", "module": "PERSON", "id": "p", "label": "Person"},
                          self.screen("WAGE", True),
                          {"op": "entity_add", "module": "WAGE", "id": "job", "label": "Employer",
                           "owner_ids": ["p"]})

    def evidence(self, case, key="WAGE/job/evidence/W2", status="verified", **kw):
        row = next(x for x in E.evaluate(case)["evidence"] if x["key"] == key)
        return {"op": "evidence", "key": key, "status": status,
                "fingerprint": row["fingerprint"], "reference": "fixture://w2/page1",
                "note": "Fictional reconciliation", "checks": {k: True for k in CHECKS}, **kw}

    def decision(self, case, key="WAGE/job/form/1040", **kw):
        row = next(x for x in E.evaluate(case)["form_candidates"] if x["key"] == key)
        return {"op": "decision", "key": key, "decision": "required", "fingerprint": row["fingerprint"],
                "reference": "fixture://review", "note": "Fictional decision", **kw}

    def state(self, case, collection, key):
        return next(x["status"] for x in E.evaluate(case)[collection] if x["key"] == key)

    def test_atomic_success_and_audit_snapshots(self):
        c = E.new_case()
        before = copy.deepcopy(c)
        updated = self.apply(c,
                            {"op": "entity_add", "module": "PERSON", "id": "p", "label": "P"},
                            self.answer("PERSON/p/PERSON.age", 30),
                            self.answer("PERSON/p/PERSON.age", 31))
        self.assertEqual(c, before)
        self.assertEqual(updated["entities"]["PERSON"][0]["answers"]["PERSON.age"]["value"], 31)
        self.assertEqual(updated["audit"][0]["after"]["answers"], {})
        self.assertEqual(updated["audit"][1]["after"]["value"], 30)
        self.assertTrue(all(a["actor"] == "test-agent" for a in updated["audit"]))

    def test_failure_rolls_back_entire_batch(self):
        c = self.base()
        before = copy.deepcopy(c)
        with self.assertRaises(AppError):
            self.apply(c, self.answer("WAGE/job/WAGE.tips", True),
                       self.answer("WAGE/job/UNKNOWN", False))
        self.assertEqual(c, before)

    def test_strict_payload_and_actor(self):
        invalid = [{}, [], {"operations": [], "actor": "fake"}, {"operations": {}},
                   {"operations": [{"op": "delete"}]}, {"operations": [None]},
                   {"operations": [{"op": "screen", "module": "WAGE", "value": True,
                                    "source": "source", "reference": "ref", "force": True}]},
                   {"operations": [{}] * 501}]
        for payload in invalid:
            with self.subTest(payload=str(payload)[:100]), self.assertRaises(AppError):
                apply_operations(E.new_case(), payload, "test-agent")
        with self.assertRaises(AppError):
            apply_operations(E.new_case(), {"operations": []}, "  ")

    def test_unknown_and_tentative_do_not_close_facts(self):
        c = self.base()
        for value, status in [(None, "confirmed"), (False, "tentative"), (False, "conflict")]:
            with self.subTest(value=value, status=status):
                changed = self.apply(c, self.answer("WAGE/job/WAGE.tips", value, status=status))
                row = next(q for q in E.evaluate(changed)["questions"] if q["key"] == "WAGE/job/WAGE.tips")
                self.assertNotEqual(row["state"], "answered")
                self.assertEqual(row["record"]["source"], "fictional intake")
        changed = self.apply(c, self.screen("WAGE", None))
        self.assertIsNone(E.module_status(changed, "WAGE"))
        self.assertEqual(changed["screens"]["WAGE"]["reference"], "fixture://intake/1")

    def test_provenance_is_required_and_not_fabricated(self):
        c = self.base()
        for field in ("source", "reference"):
            op = self.answer("WAGE/job/WAGE.tips", False)
            del op[field]
            with self.assertRaises(AppError):
                self.apply(c, op)
        c = self.apply(c, self.screen("WAGE", True, source="connector:drive", reference="file:42"))
        self.assertEqual(c["screens"]["WAGE"]["source"], "connector:drive")

    def test_question_visibility_and_catalog_value_validation(self):
        c = self.base()
        for op in (self.answer("WAGE/job/WAGE.flsa", True),
                   self.answer("WAGE/job/WAGE.tips", "false"),
                   self.answer("WAGE/job/WAGE.tips", []),
                   self.answer("PERSON/p/PERSON.age", float("nan")),
                   self.screen("WAGE", 1)):
            with self.subTest(op=op), self.assertRaises(AppError):
                self.apply(c, op)
        c = self.apply(c, self.answer("WAGE/job/WAGE.overtime", True),
                       self.answer("WAGE/job/WAGE.flsa", True))
        c = self.apply(c, self.answer("WAGE/job/WAGE.overtime", False))
        with self.assertRaises(AppError):
            self.apply(c, self.answer("WAGE/job/WAGE.flsa", False))

    def test_entity_scope_ownership_and_updates(self):
        c = self.base()
        bad = [
            {"op": "entity_add", "module": "INVEST", "id": "a", "label": "A"},
            {"op": "entity_add", "module": "WAGE", "id": "job", "label": "Duplicate"},
            {"op": "entity_add", "module": "WAGE", "id": "bad/id", "label": "Bad"},
            {"op": "entity_add", "module": "PERSON", "id": "q", "label": "Q", "owner_ids": ["p"]},
            {"op": "entity_add", "module": "WAGE", "id": "x", "label": "X", "owner_ids": ["missing"]},
            {"op": "entity_update", "module": "WAGE", "id": "job"},
            {"op": "entity_update", "module": "WAGE", "id": "job", "owner_ids": ["p", "p"]},
            {"op": "entity_update", "module": "WAGE", "id": "absent", "label": "X"},
        ]
        for op in bad:
            with self.subTest(op=op), self.assertRaises(AppError):
                self.apply(c, op)
        changed = self.apply(c, {"op": "entity_update", "module": "WAGE", "id": "job", "label": "Renamed"})
        self.assertEqual(changed["entities"]["WAGE"][0]["label"], "Renamed")

    def test_enumeration_and_invalidation_are_audited(self):
        c = self.base()
        op = {"op": "enumerate", "module": "WAGE", "complete": True,
              "source": "filer", "reference": "intake://roster"}
        c = self.apply(c, op)
        self.assertEqual(c["enumerated"]["WAGE"]["source"], "filer")
        c = self.apply(c, {"op": "entity_add", "module": "WAGE", "id": "two", "label": "Second"})
        self.assertNotIn("WAGE", c["enumerated"])
        self.assertEqual(c["audit"][-1]["action"], "enumeration_invalidation")
        self.assertEqual(c["audit"][-1]["before"]["entity_ids"], ["job"])
        for invalid in ({**op, "complete": 1}, {**op, "module": "INVEST"},
                        {**op, "module": "CORE"}):
            with self.assertRaises(AppError):
                self.apply(c, invalid)
        with self.assertRaises(AppError):
            self.apply(E.new_case(), {**op, "module": "PERSON"})

    def test_evidence_closure_is_strict_and_fingerprint_bound(self):
        c = self.base()
        valid = self.evidence(c)
        invalid = [{**valid, "fingerprint": "old"}, {**valid, "note": " "},
                   {**valid, "checks": {k: 1 for k in CHECKS}},
                   {**valid, "checks": {**valid["checks"], "extra": True}},
                   {**valid, "status": "done"}, {**valid, "actor": "forged"},
                   {**valid, "sha256": "abc"}, {**valid, "key": "WAGE/other/evidence/W2"}]
        invalid.append({k: v for k, v in valid.items() if k != "fingerprint"})
        for op in invalid:
            with self.subTest(op=op), self.assertRaises(AppError):
                self.apply(c, op)
        for status in ("verified", "alternative_accepted", "not_required"):
            op = {**valid, "status": status}
            if status == "not_required":
                op.pop("checks")
            result = self.apply(c, op)
            self.assertEqual(self.state(result, "evidence", valid["key"]), status)

    def test_located_and_rejected_have_minimum_documentation(self):
        c = self.base()
        for status in ("located", "rejected"):
            with self.assertRaises(AppError):
                self.apply(c, {"op": "evidence", "key": "WAGE/job/evidence/W2", "status": status})
        for status in ("missing", "searching", "stale"):
            result = self.apply(c, {"op": "evidence", "key": "WAGE/job/evidence/W2", "status": status})
            self.assertEqual(self.state(result, "evidence", "WAGE/job/evidence/W2"), status)

    def test_batch_cannot_leave_a_claimed_closure_stale_or_inactive(self):
        c = self.base()
        for later in (self.answer("WAGE/job/WAGE.tips", True), self.screen("WAGE", False)):
            with self.subTest(later=later), self.assertRaises(AppError) as ctx:
                self.apply(c, self.evidence(c), later)
            self.assertEqual(ctx.exception.code, "INVALIDATED_CLOSURE")
        with self.assertRaises(AppError):
            self.apply(c, self.decision(c), self.answer("PERSON/p/PERSON.age", 40))

    def test_form_and_route_decisions_use_current_exact_key(self):
        c = self.base()
        c = self.apply(c, self.decision(c))
        self.assertEqual(self.state(c, "form_candidates", "WAGE/job/form/1040"), "required")
        with self.assertRaises(AppError):
            self.apply(c, self.decision(c, fingerprint="stale"))
        c = self.apply(c, self.answer("WAGE/job/WAGE.foreign", True))
        route = next(x for x in E.evaluate(c)["routes"] if x["module"] == "WAGE")
        op = {"op": "resolve", "kind": "route", "key": route["key"], "fingerprint": route["fingerprint"],
              "reference": "fixture://foreign-track", "note": "Downstream instance linked"}
        c = self.apply(c, op)
        self.assertEqual(self.state(c, "routes", route["key"]), "resolved")
        with self.assertRaises(AppError):
            self.apply(c, {**op, "kind": "review"})

    def test_search_records_do_not_satisfy_evidence_or_questions(self):
        c = self.base()
        op = {"op": "search_log", "key": "WAGE/job/evidence/W2", "source": "Drive",
              "query": "2025 employer W2", "outcome": "not_found", "reference": "search://actual-run"}
        c = self.apply(c, op)
        self.assertEqual(c["search_log"][0]["outcome"], "not_found")
        self.assertEqual(self.state(c, "evidence", op["key"]), "missing")
        self.assertEqual(c["audit"][-1]["actor"], "test-agent")
        for bad in ({**op, "outcome": "absent"}, {**op, "key": "fake/task"}):
            with self.assertRaises(AppError):
                self.apply(c, bad)

    def test_source_change_invalidates_reviews_and_preserves_history(self):
        c = self.base()
        c = self.apply(c, self.answer("WAGE/job/WAGE.foreign", True),
                       self.answer("WAGE/job/WAGE.misclassified", True))
        r = E.evaluate(c)
        ops = [self.evidence(c), self.decision(c)]
        relevant = [("review", row) for row in r["reviews"] if row["module"] == "WAGE"]
        relevant += [("route", row) for row in r["routes"] if row["module"] == "WAGE"]
        self.assertTrue(any(kind == "review" for kind, _ in relevant))
        self.assertTrue(any(kind == "route" for kind, _ in relevant))
        ops += [{"op": "resolve", "kind": kind, "key": row["key"], "fingerprint": row["fingerprint"],
                 "reference": "fixture://review", "note": "Fictional review"} for kind, row in relevant]
        c = self.apply(c, *ops)
        before = copy.deepcopy(c)
        op = {"op": "source_change", "key": "WAGE/job/evidence/W2", "reference": "fixture://w2/corrected",
              "note": "Corrected W2 arrived", "source_version": "corrected-1", "sha256": "a" * 64}
        c = self.apply(c, op)
        self.assertEqual(self.state(c, "evidence", op["key"]), "stale")
        self.assertEqual(self.state(c, "form_candidates", "WAGE/job/form/1040"), "stale")
        for kind, row in relevant:
            self.assertNotEqual(self.state(c, "reviews" if kind == "review" else "routes", row["key"]), "resolved")
        self.assertEqual(c["audit"][:len(before["audit"])], before["audit"])
        self.assertTrue(all(a["actor"] == "test-agent" for a in c["audit"]))
        c = self.apply(c, self.evidence(c), self.decision(c))
        self.assertEqual(self.state(c, "form_candidates", "WAGE/job/form/1040"), "required")

    def test_schema_is_json_serializable_and_matches_all_operations(self):
        schema = json.loads(json.dumps(operation_schema()))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(schema["additionalProperties"])
        variants = schema["properties"]["operations"]["items"]["oneOf"]
        self.assertEqual(len(variants), 10)
        self.assertTrue(all(v["additionalProperties"] is False for v in variants))

    def test_source_identity_cannot_bypass_invalidation_and_survives_status_updates(self):
        c = self.base()
        c = self.apply(c, self.evidence(c, sha256="a" * 64, source_version="v1"), self.decision(c))
        for kw in ({"sha256": "b" * 64}, {"source_version": "v2"}):
            with self.subTest(kw=kw), self.assertRaises(AppError) as ctx:
                self.apply(c, self.evidence(c, **kw))
            self.assertEqual(ctx.exception.code, "SOURCE_CHANGE_REQUIRED")
        c = self.apply(c, self.evidence(c, sha256="A" * 64))
        self.assertEqual(c["evidence"]["WAGE/job/evidence/W2"]["source_version"], "v1")
        change = {"op": "source_change", "key": "WAGE/job/evidence/W2", "reference": "fixture://v2",
                  "note": "Corrected source", "source_version": "v2", "sha256": "b" * 64}
        c = self.apply(c, change, self.evidence(c, reference="fixture://v2"))
        self.assertEqual(self.state(c, "evidence", change["key"]), "verified")
        self.assertEqual(c["evidence"][change["key"]]["sha256"], "b" * 64)
        self.assertEqual(c["evidence"][change["key"]]["source_version"], "v2")
        self.assertEqual(self.state(c, "form_candidates", "WAGE/job/form/1040"), "stale")

    def test_source_change_does_not_reopen_an_unrelated_instance(self):
        c = self.base()
        c = self.apply(c, {"op": "entity_add", "module": "WAGE", "id": "two", "label": "Second", "owner_ids": ["p"]})
        c = self.apply(c, self.evidence(c), self.decision(c),
                       self.evidence(c, key="WAGE/two/evidence/W2"), self.decision(c, key="WAGE/two/form/1040"))
        c = self.apply(c, {"op": "source_change", "key": "WAGE/job/evidence/W2", "reference": "fixture://v2",
                          "note": "Corrected source"})
        self.assertEqual(self.state(c, "form_candidates", "WAGE/two/form/1040"), "required")
        self.assertEqual(self.state(c, "evidence", "WAGE/two/evidence/W2"), "verified")

    def test_closure_followed_by_source_change_fails_final_batch_check(self):
        c = self.base()
        with self.assertRaises(AppError) as ctx:
            self.apply(c, self.evidence(c), {"op": "source_change", "key": "WAGE/job/evidence/W2",
                                           "reference": "fixture://v2", "note": "Source replaced"})
        self.assertEqual(ctx.exception.code, "INVALIDATED_CLOSURE")


if __name__ == "__main__":
    unittest.main()
