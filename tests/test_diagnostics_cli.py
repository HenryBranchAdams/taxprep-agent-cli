"""Public process contract for workflow diagnostics, using fictional facts only."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
ACTOR = "fictional-diagnostics-agent"
SOURCE = {"source": "fictional interview", "reference": "fixture://diagnostics/interview"}
YEAR_KEY = "CORE/return/CORE.year"


class DiagnosticsCliTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="taxprep-diagnostics-")
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.db = self.directory / "case.sqlite"

    def run_cli(self, *args, stdin=None, executable=None):
        invocation = [sys.executable, str(executable)] if executable else [sys.executable, "-m", "taxprep"]
        return subprocess.run(
            [*invocation, "--db", str(self.db), *args], cwd=self.directory if executable else ROOT,
            input=stdin, capture_output=True, text=True, timeout=30,
        )

    def success(self, *args, stdin=None, executable=None):
        process = self.run_cli(*args, stdin=stdin, executable=executable)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(process.stderr, "")
        result = json.loads(process.stdout)
        self.assertIs(result["ok"], True)
        self.assertEqual(result["protocol_version"], "1.0")
        return result

    def failure(self, *args, code, exit_code=2):
        process = self.run_cli(*args)
        self.assertEqual(process.returncode, exit_code, process.stderr)
        self.assertEqual(process.stdout, "")
        result = json.loads(process.stderr)
        self.assertIs(result["ok"], False)
        self.assertEqual(result["error"]["code"], code)
        return result

    def initialize(self):
        return self.success("init", "--case-id", "fictional-diagnostics", "--actor", ACTOR)

    def apply(self, operations, *, expect=1, request_id="batch-1", dry_run=False):
        args = ["apply", "--input", "-", "--expect", str(expect),
                "--request-id", request_id, "--actor", ACTOR]
        if dry_run:
            args.append("--dry-run")
        return self.success(*args, stdin=json.dumps({"operations": operations}))

    @staticmethod
    def year_answer(value=2025):
        return {"op": "answer", "key": YEAR_KEY, "value": value, **SOURCE}

    @staticmethod
    def digital_intake():
        return [
            {"op": "entity_add", "module": "PERSON", "id": "person", "label": "Fictional Person"},
            {"op": "screen", "module": "DIGITAL", "value": True, **SOURCE},
            {"op": "entity_add", "module": "DIGITAL", "id": "exchange",
             "label": "Fictional Exchange", "owner_ids": ["person"]},
            {"op": "answer", "key": "DIGITAL/exchange/DIGITAL.broker_form", "value": True, **SOURCE},
        ]

    def test_graph_is_catalog_discovery_without_a_database(self):
        result = self.success("graph", "--node", "DIGITAL.broker_form", "--depth", "0")
        self.assertIsNone(result["revision"])
        graph = result["data"]
        self.assertEqual([node["id"] for node in graph["nodes"]], ["DIGITAL.broker_form"])
        self.assertEqual(graph["edges"], [])
        self.assertEqual(graph["node_count"], 1)
        expanded = self.success("graph", "--node", "DIGITAL.broker_form",
                                "--direction", "downstream", "--depth", "1")["data"]
        ids = {node["id"] for node in expanded["nodes"]}
        self.assertIn("rule.DIGITAL.broker_form", ids)
        self.assertNotIn("screen.DIGITAL", ids)
        self.assertTrue(all(edge["source"] in ids and edge["target"] in ids
                            for edge in expanded["edges"]))
        self.assertFalse(self.db.exists())
        commands = self.success("schema", "--target", "protocol")["data"]["commands"]
        self.assertTrue({"graph", "explain", "diff"}.issubset(commands))

    def test_graph_rejects_bad_queries_with_machine_errors(self):
        for arguments in (("--depth", "-1"), ("--depth", "11"), ("--depth", "two"),
                          ("--direction", "sideways"), ("--module", "NONEXISTENT"),
                          ("--module", "DIGITAL", "--node", "DIGITAL.broker_form")):
            with self.subTest(arguments=arguments):
                self.failure("graph", *arguments, code="invalid_arguments")
        self.failure("graph", "--node", "NOT.A.NODE", code="not_found", exit_code=4)
        self.assertFalse(self.db.exists())

    def test_mermaid_stdout_and_files_are_explicit_and_never_overwrite(self):
        arguments = ("graph", "--node", "DIGITAL.broker_form", "--format", "mermaid")
        raw = self.run_cli(*arguments)
        self.assertEqual(raw.returncode, 0, raw.stderr)
        self.assertEqual(raw.stderr, "")
        self.assertTrue(raw.stdout.startswith("flowchart TD\n"), raw.stdout)
        self.assertNotIn('"ok":', raw.stdout)
        destination = self.directory / "issuer-workflow.mmd"
        result = self.success(*arguments, "--output", str(destination))
        self.assertIsNone(result["revision"])
        self.assertEqual(destination.read_text(encoding="utf-8"), raw.stdout)
        original = destination.read_bytes()
        self.failure(*arguments, "--output", str(destination), code="already_exists", exit_code=3)
        self.assertEqual(destination.read_bytes(), original)
        json_path = self.directory / "issuer-workflow.json"
        self.success("graph", "--module", "DIGITAL", "--output", str(json_path))
        saved = json.loads(json_path.read_text(encoding="utf-8"))
        self.assertTrue(saved["nodes"])
        self.assertTrue(all(node["module"] == "DIGITAL" for node in saved["nodes"]))
        self.assertFalse(self.db.exists())

    def test_explain_can_inspect_an_earlier_revision(self):
        self.initialize()
        self.apply([self.year_answer()])
        before = self.success("explain", YEAR_KEY, "--revision", "1")
        after = self.success("explain", YEAR_KEY)
        self.assertEqual(before["revision"], 1)
        self.assertEqual(before["data"]["item"]["state"], "unanswered")
        self.assertEqual(after["revision"], 2)
        self.assertEqual(after["data"]["item"]["state"], "answered")
        self.assertEqual(after["data"]["item"]["value"], 2025)
        self.failure("explain", "CORE/return/NOT_A_QUESTION", code="not_found", exit_code=4)
        self.failure("explain", YEAR_KEY, "--revision", "999", code="not_found", exit_code=4)

    def test_diff_supports_default_current_same_and_reverse_comparisons(self):
        self.initialize()
        self.apply([self.year_answer()])
        forward = self.success("diff", "--from", "1")
        self.assertEqual(forward["revision"], 2)
        data = forward["data"]
        self.assertEqual((data["from_revision"], data["to_revision"]), (1, 2))
        self.assertTrue(any(item["key"] == YEAR_KEY for item in data["records"]["answers"]))
        self.assertGreater(data["counts"]["record_changes"], 0)
        self.assertEqual(data["summary"]["answered_questions"]["delta"], 1)
        reverse = self.success("diff", "--from", "2", "--to", "1")["data"]
        self.assertEqual(reverse["summary"]["answered_questions"]["delta"], -1)
        same = self.success("diff", "--from", "2", "--to", "2")["data"]
        self.assertTrue(all(value == 0 for value in same["counts"].values()))
        self.failure("diff", "--from", "999", code="not_found", exit_code=4)
        self.failure("diff", "--from", "0", code="invalid_arguments")

    def test_dry_run_previews_activation_and_retry_does_not_claim_fresh_impact(self):
        self.initialize()
        payload = self.digital_intake()
        dry = self.apply(payload, dry_run=True)
        self.assertEqual(dry["revision"], 1)
        self.assertTrue(dry["data"]["dry_run"])
        impact = dry["data"]["impact"]
        evidence_key = "DIGITAL/exchange/evidence/DIGITAL.doc_broker_form"
        self.assertTrue(any(task["key"] == evidence_key for task in impact["tasks"]["added"]))
        self.assertEqual(self.success("status")["revision"], 1)
        self.assertEqual(len(self.success("history")["data"]["snapshots"]), 1)
        self.apply(payload)
        committed = self.success("diff", "--from", "1", "--to", "2")["data"]
        self.assertEqual(committed["tasks"], impact["tasks"])
        self.assertEqual(committed["counts"], impact["counts"])
        self.apply([self.year_answer()], expect=2, request_id="batch-2")
        replayed = self.apply(payload, dry_run=True)
        self.assertTrue(replayed["data"]["replayed"])
        self.assertEqual(replayed["revision"], 2)
        self.assertNotIn("impact", replayed["data"])
        self.assertEqual(self.success("status")["revision"], 3)

    def test_diagnostics_preserve_database_bytes_and_revision_history(self):
        self.initialize()
        self.apply([self.year_answer()])
        original_digest = hashlib.sha256(self.db.read_bytes()).hexdigest()
        original_history = self.success("history")["data"]
        self.success("graph", "--module", "CORE")
        self.success("explain", YEAR_KEY)
        self.success("explain", YEAR_KEY, "--revision", "1")
        self.success("diff", "--from", "1", "--to", "2")
        self.assertEqual(self.success("history")["data"], original_history)
        self.assertEqual(hashlib.sha256(self.db.read_bytes()).hexdigest(), original_digest)

    def test_built_zipapp_has_the_same_diagnostics_without_installed_package(self):
        build_directory = self.directory / "standalone-build"
        build_directory.mkdir()
        shutil.copyfile(ROOT / "build_release.py", build_directory / "build_release.py")
        shutil.copytree(ROOT / "taxprep", build_directory / "taxprep",
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        built = subprocess.run([sys.executable, "build_release.py"], cwd=build_directory,
                               capture_output=True, text=True, timeout=30)
        self.assertEqual(built.returncode, 0, built.stderr)
        executable = build_directory / "taxprep.pyz"
        self.assertTrue(executable.is_file())
        arguments = ("graph", "--node", "DIGITAL.broker_form", "--direction", "downstream", "--depth", "2")
        self.assertEqual(self.success(*arguments), self.success(*arguments, executable=executable))
        self.initialize()
        self.apply([self.year_answer()])
        self.assertEqual(self.success("explain", YEAR_KEY),
                         self.success("explain", YEAR_KEY, executable=executable))
        self.assertEqual(self.success("diff", "--from", "1"),
                         self.success("diff", "--from", "1", executable=executable))


if __name__ == "__main__":
    unittest.main(verbosity=2)
