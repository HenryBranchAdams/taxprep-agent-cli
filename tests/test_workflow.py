"""Read-only workflow discovery must preserve the evaluator's unknown states."""
import copy
import json
from pathlib import Path
import unittest

from taxprep import engine as E, workflow as W
from taxprep.errors import AppError
from taxprep.operations import apply_operations, CHECKS


class CatalogGraphTests(unittest.TestCase):
    def test_full_graph_uses_exact_validated_topology(self):
        actual = W.catalog_graph()
        expected = E.validate_catalog()
        self.assertEqual(actual["node_count"], expected["nodes"])
        self.assertEqual(actual["edge_count"], expected["edges"])
        self.assertEqual([(edge["source"], edge["target"]) for edge in actual["edges"]],
                         expected["graph_edges"])
        self.assertEqual({row["id"] for row in actual["nodes"]}, set(expected["topological_order"]))
        self.assertIn("invalidation", actual["scope"])
        self.assertEqual(actual, W.catalog_graph())

    def test_direction_and_depth_bound_the_exact_neighborhood(self):
        node = "DIGITAL.broker_form"
        self.assertEqual([row["id"] for row in W.catalog_graph(node=node, depth=0)["nodes"]], [node])
        actual = W.catalog_graph(node=node, direction="downstream", depth=2)
        self.assertEqual({row["id"] for row in actual["nodes"]},
                         {node, "rule.DIGITAL.broker_form", "evidence.DIGITAL.DIGITAL.doc_broker_form"})
        upstream = W.catalog_graph(node=node, direction="upstream", depth=1)
        self.assertEqual({row["id"] for row in upstream["nodes"]}, {node, "screen.DIGITAL"})
        both = W.catalog_graph(node=node, direction="both", depth=1)
        self.assertEqual(both["node_count"], 3)
        self.assertEqual(both["edge_count"], 3)  # Preserves the screen -> rule edge too.

    def test_module_graph_is_induced_and_rejects_invalid_queries(self):
        graph = W.catalog_graph(module="WAGE")
        node_ids = {row["id"] for row in graph["nodes"]}
        self.assertTrue(all(row["module"] == "WAGE" for row in graph["nodes"]))
        self.assertTrue(all(edge["source"] in node_ids and edge["target"] in node_ids
                            for edge in graph["edges"]))
        for args in ({"module": "UNKNOWN"}, {"module": "WAGE", "node": "WAGE.tips"},
                     {"depth": -1}, {"depth": 11}, {"depth": True}, {"depth": 1.0},
                     {"direction": "sideways"}):
            with self.subTest(args=args), self.assertRaises(AppError) as cm:
                W.catalog_graph(**args)
            self.assertEqual(cm.exception.code, "invalid_arguments")
        with self.assertRaises(AppError) as cm:
            W.catalog_graph(node="DIGITAL.broker")
        self.assertEqual(cm.exception.code, "not_found")
        self.assertEqual(cm.exception.exit_code, 4)

    def test_mermaid_uses_generated_ids_and_escaped_single_line_labels(self):
        graph = {"nodes": [{"id": 'bad]"', "label": 'text\nclick n0 "evil" <script>\\`#', "module": "X", "kind": "question"}],
                 "edges": []}
        rendered = W.render_mermaid(graph)
        self.assertEqual(len(rendered.splitlines()), 2)
        self.assertTrue(rendered.startswith('flowchart TD\n    n0["'))
        self.assertIn("#34;", rendered)
        self.assertIn("#60;script#62;", rendered)
        self.assertIn("#92;#96;#35;", rendered)
        self.assertNotIn("\nclick", rendered)
        actual = W.catalog_graph(node="DIGITAL.broker_form", direction="downstream", depth=2)
        self.assertEqual(W.render_mermaid(actual), W.render_mermaid(actual))
        self.assertIn("n0 --> n2", W.render_mermaid(actual))


class ExplainTests(unittest.TestCase):
    def case(self, module="WAGE"):
        case = E.new_case()
        E.add_entity(case, "PERSON", "Fictional person", eid="p")
        E.set_screen(case, module, True)
        E.add_entity(case, module, "Fictional account", ["p"], eid="a")
        return case

    def test_unknown_tentative_false_and_true_have_distinct_explanations(self):
        for value, status, expected in ((None, "confirmed", None),
                                        (True, "tentative", None),
                                        (True, "conflict", None),
                                        (False, "confirmed", False),
                                        (True, "confirmed", True)):
            with self.subTest(value=value, status=status):
                case = self.case()
                if value is not None:
                    E.set_answer(case, "WAGE", "a", "WAGE.overtime", value, status=status)
                before = copy.deepcopy(case)
                result = W.explain(case, "WAGE/a/WAGE.flsa")
                self.assertIs(result["activation"]["result"], expected)
                parent = next(row for row in result["prerequisites"] if row["id"] == "WAGE.overtime")
                self.assertIs(parent["value"], value if status == "confirmed" else None)
                self.assertEqual(case, before)
                if expected is None:
                    self.assertEqual(result["item"]["state"], "blocked_by_upstream")
                    self.assertIn("unknown", result["reason"])

    def test_repeated_entities_keep_distinct_fact_prerequisites(self):
        case = self.case()
        E.add_entity(case, "WAGE", "Another employer", ["p"], eid="b")
        E.set_answer(case, "WAGE", "a", "WAGE.overtime", True)
        E.set_answer(case, "WAGE", "b", "WAGE.overtime", False)
        for entity_id, expected in (("a", True), ("b", False)):
            result = W.explain(case, "WAGE/" + entity_id + "/WAGE.flsa")
            self.assertIs(result["activation"]["result"], expected)
            parent = next(row for row in result["prerequisites"] if row["id"] == "WAGE.overtime")
            self.assertEqual(parent["key"], "WAGE/" + entity_id + "/WAGE.overtime")

    def test_transitive_prerequisites_preserve_unknown_parent_states(self):
        case = E.new_case()
        E.add_entity(case, "PERSON", "Fictional person", eid="p")
        result = W.explain(case, "PERSON/p/PERSON.refund_only")
        prerequisites = {row["id"]: row for row in result["prerequisites"]}
        self.assertIn("PERSON.role", prerequisites)
        self.assertIn("PERSON.joint_return", prerequisites)
        self.assertEqual(prerequisites["PERSON.role"]["depth"], 1)
        self.assertIsNone(result["activation"]["result"])
        self.assertEqual(prerequisites["PERSON.joint_return"]["state"], "blocked_by_upstream")
        self.assertIsNone(prerequisites["PERSON.joint_return"]["value"])

    def test_issued_digital_statement_explains_requirement_and_source_staleness(self):
        case = self.case("DIGITAL")
        E.set_answer(case, "DIGITAL", "a", "DIGITAL.broker_form", True)
        key = "DIGITAL/a/evidence/DIGITAL.doc_broker_form"
        result = W.explain(case, key)
        self.assertEqual(result["item"]["status"], "missing")
        self.assertEqual(result["rules"][0]["id"], "DIGITAL.broker_form")
        self.assertIs(result["rules"][0]["result"], True)
        self.assertIn("DIGITAL/a/DIGITAL.broker_form", {row["key"] for row in result["prerequisites"]})
        case = apply_operations(case, {"operations": [{"op": "evidence", "key": key,
                                "status": "verified", "fingerprint": result["current_fingerprint"],
                                "checks": {check: True for check in CHECKS},
                                "reference": "fixture://statement", "note": "Fictional reconciliation"}]}, "tester")
        verified = W.explain(case, key)
        self.assertIs(verified["fingerprint_matches"], True)
        case = apply_operations(case, {"operations": [{"op": "source_change", "key": key,
                                "reference": "fixture://corrected", "note": "Fictional correction",
                                "source_version": "v2"}]}, "tester")
        stale = W.explain(case, key)
        self.assertEqual(stale["item"]["status"], "stale")
        self.assertIs(stale["fingerprint_matches"], False)
        self.assertIn("source-changed:", stale["stored_fingerprint"])

    def test_form_review_route_and_inventory_issue_are_supported(self):
        case = json.loads((Path(__file__).resolve().parents[1] / "examples/fictional_case.json").read_text())
        report = E.evaluate(case)
        for section in ("form_candidates", "reviews"):
            result = W.explain(case, report[section][0]["key"])
            self.assertEqual(result["section"], section)
            self.assertTrue(result["rules"])
            self.assertTrue(any(rule["result"] is True for rule in result["rules"]))
        case = self.case()
        E.set_answer(case, "WAGE", "a", "WAGE.foreign", True)
        key = next(row["key"] for row in E.evaluate(case)["routes"])
        self.assertIs(W.explain(case, key)["activation"]["result"], True)
        issue = W.explain(case, "roster/WAGE")
        self.assertEqual(issue["section"], "issues")
        self.assertEqual(issue["inventory"]["entities"][0]["id"], "a")
        self.assertIsNone(W.explain(E.new_case(), "screen/DIGITAL")["module_status"])

    def test_returned_data_is_detached_and_exact_keys_are_required(self):
        case = self.case()
        before = copy.deepcopy(case)
        condition = copy.deepcopy(E.QUESTIONS["WAGE.flsa"]["when"])
        result = W.explain(case, "WAGE/a/WAGE.flsa")
        result["activation"]["condition"]["value"] = "bad"
        result["prerequisites"][0]["value"] = "bad"
        self.assertEqual(E.QUESTIONS["WAGE.flsa"]["when"], condition)
        self.assertEqual(case, before)
        for key in ("WAGE.flsa", "WAGE/missing/WAGE.flsa", "DIGITAL/a/evidence/DIGITAL.doc_broker_form"):
            with self.subTest(key=key), self.assertRaises(AppError) as cm:
                W.explain(case, key)
            self.assertEqual(cm.exception.code, "not_found")
            self.assertEqual(cm.exception.exit_code, 4)


if __name__ == "__main__":
    unittest.main()
