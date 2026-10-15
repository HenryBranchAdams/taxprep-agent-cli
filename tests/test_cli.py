"""Process-level checks of the public agent protocol using only fictional data.

These tests exercise parsing, durable mutation, retries, exports and handoffs;
they do not certify the questionnaire's tax-law coverage or legal conclusions.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
ACTOR = "fictional-test-agent"
PROVENANCE = {
    "source": "fictional test fixture",
    "reference": "fixture://cli-tests/interview",
}


class CliTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="taxprep-cli-test-")
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.db = self.directory / "case.sqlite"

    def run_cli(self, *args, stdin=None, db=None):
        return subprocess.run(
            [sys.executable, "-m", "taxprep", "--db", str(db or self.db), *args],
            cwd=ROOT, input=stdin, capture_output=True, text=True, timeout=20,
        )

    def success(self, *args, stdin=None, db=None, exit_code=0):
        process = self.run_cli(*args, stdin=stdin, db=db)
        self.assertEqual(process.returncode, exit_code, process.stderr)
        self.assertEqual(process.stderr, "")
        result = json.loads(process.stdout)
        self.assertIs(result["ok"], True)
        self.assertEqual(result["protocol_version"], "1.0")
        self.assertIn("revision", result)
        self.assertIn("data", result)
        return result

    def failure(self, *args, stdin=None, db=None, exit_code=2, code=None):
        process = self.run_cli(*args, stdin=stdin, db=db)
        self.assertEqual(process.returncode, exit_code, process.stderr)
        self.assertEqual(process.stdout, "")
        result = json.loads(process.stderr)
        self.assertIs(result["ok"], False)
        self.assertEqual(result["protocol_version"], "1.0")
        self.assertTrue(result["error"]["message"])
        if code is not None:
            self.assertEqual(result["error"]["code"], code)
        return result

    def initialize(self):
        return self.success("init", "--case-id", "fictional-cli-case", "--actor", ACTOR)

    def apply(self, operations, *, expect=1, request_id="fictional-request-1", actor=ACTOR,
              dry_run=False, exit_code=0, error_code=None):
        args = ["apply", "--input", "-", "--expect", str(expect),
                "--request-id", request_id, "--actor", actor]
        if dry_run:
            args.append("--dry-run")
        payload = json.dumps({"operations": operations})
        if error_code is not None or exit_code != 0:
            return self.failure(*args, stdin=payload, exit_code=exit_code, code=error_code)
        return self.success(*args, stdin=payload)

    def export_case(self, *, db=None, revision=None):
        args = ["export", "--output", "-"]
        if revision is not None:
            args.extend(["--revision", str(revision)])
        process = self.run_cli(*args, db=db)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(process.stderr, "")
        case = json.loads(process.stdout)
        self.assertNotIn("ok", case)  # Explicit raw-export exception to the envelope.
        return case

    @staticmethod
    def screen(value=True):
        return {"op": "screen", "module": "WAGE", "value": value, **PROVENANCE}

    @staticmethod
    def intake_batch():
        return [
            CliTests.screen(),
            {"op": "entity_add", "module": "PERSON", "id": "p",
             "label": "Fictional Person"},
            {"op": "answer", "key": "PERSON/p/PERSON.role", "value": "Taxpayer",
             **PROVENANCE},
            {"op": "entity_add", "module": "WAGE", "id": "employer",
             "label": "Fictional Employer", "owner_ids": ["p"]},
            {"op": "answer", "key": "WAGE/employer/WAGE.tips", "value": False,
             **PROVENANCE},
        ]

    def test_discovery_commands_do_not_create_a_database(self):
        doctor = self.success("doctor")
        self.assertIsNone(doctor["revision"])
        self.assertTrue(doctor["data"]["graph"]["valid"])
        self.assertGreater(doctor["data"]["questions"], 0)
        self.assertEqual(doctor["data"]["runtime_dependencies"], [])
        catalog = self.success("catalog", "--kind", "questions", "--module", "WAGE")
        self.assertGreater(catalog["data"]["count"], 0)
        self.assertTrue(all(item["module"] == "WAGE" for item in catalog["data"]["items"]))
        schema = self.success("schema")
        self.assertEqual(schema["data"]["required"], ["operations"])
        protocol = self.success("schema", "--target", "protocol")
        self.assertIs(protocol["data"]["interactive"], False)
        self.assertIn("apply", protocol["data"]["commands"])
        self.assertFalse(self.db.exists())

    def test_missing_database_read_is_structured_and_does_not_create_file(self):
        self.failure("status", exit_code=4, code="not_found")
        self.assertFalse(self.db.exists())

    def test_initialization_and_duplicate_initialization_preserve_case(self):
        initialized = self.initialize()
        self.assertEqual(initialized["revision"], 1)
        self.assertEqual(initialized["data"]["case_id"], "fictional-cli-case")
        original = self.export_case()
        self.failure("init", "--case-id", "replacement", "--actor", ACTOR,
                     exit_code=3, code="already_exists")
        self.assertEqual(self.export_case(), original)

    def test_status_keeps_unknown_answers_and_reports_revision(self):
        self.initialize()
        status = self.success("status")
        self.assertEqual(status["revision"], 1)
        self.assertEqual(status["data"]["readiness"], "OPEN")
        self.assertGreater(status["data"]["summary"]["unanswered_screens"], 0)
        self.assertGreater(status["data"]["summary"]["active_unanswered_questions"], 0)
        case = self.export_case()
        self.assertIsNone(case["screens"]["WAGE"])
        self.assertEqual(case["entities"]["PERSON"], [])

    def test_bad_flags_and_incomplete_commands_are_json_errors(self):
        for args in [("status", "--bogus"), ("next", "--limit", "0"),
                     ("next", "--limit", "not-a-number"), ("next", "--module", "NOT_A_MODULE"),
                     ("apply",), ()]:
            with self.subTest(args=args):
                self.failure(*args, code="invalid_arguments")
        self.assertFalse(self.db.exists())

    def test_malformed_duplicate_key_and_nonfinite_json_are_rejected(self):
        self.initialize()
        original = self.export_case()
        for text in ('{"operations": [', '{"operations": [], "operations": []}',
                     '{"operations": [{"value": NaN}]}'):
            with self.subTest(text=text):
                self.failure("apply", "--input", "-", "--expect", "1",
                             "--request-id", "invalid-json", "--actor", ACTOR,
                             stdin=text, code="invalid_json")
        self.assertEqual(self.export_case(), original)

    def test_atomic_intake_batch_records_actor_and_provenance(self):
        self.initialize()
        applied = self.apply(self.intake_batch())
        self.assertEqual(applied["revision"], 2)
        self.assertFalse(applied["data"]["replayed"])
        case = self.export_case()
        self.assertTrue(case["screens"]["WAGE"]["value"])
        person = case["entities"]["PERSON"][0]
        self.assertEqual(person["id"], "p")
        role = person["answers"]["PERSON.role"]
        self.assertEqual(role["value"], "Taxpayer")
        self.assertEqual(role["actor"], ACTOR)
        self.assertEqual(role["source"], PROVENANCE["source"])
        self.assertEqual(role["reference"], PROVENANCE["reference"])
        self.assertTrue(all(entry["actor"] == ACTOR for entry in case["audit"][-5:]))
        inspected = self.success("inspect", "PERSON/p/PERSON.role")
        self.assertEqual(inspected["data"]["state"], "answered")
        self.assertEqual(inspected["data"]["value"], "Taxpayer")

    def test_retry_returns_original_revision_without_losing_newer_changes(self):
        self.initialize()
        first = self.apply(self.intake_batch())
        original = self.export_case()
        second = self.apply([self.screen(False)], expect=2, request_id="fictional-request-2")
        self.assertEqual(second["revision"], 3)
        retried = self.apply(self.intake_batch(), expect=1)
        self.assertTrue(retried["data"]["replayed"])
        self.assertEqual(retried["revision"], first["revision"])
        self.assertEqual(self.export_case(revision=2), original)
        self.assertEqual(self.success("status")["revision"], 3)
        self.assertFalse(self.export_case()["screens"]["WAGE"]["value"])
        self.assertEqual(len(self.success("history")["data"]["snapshots"]), 3)

    def test_stale_revision_and_reused_request_conflicts_are_structured(self):
        self.initialize()
        self.apply([self.screen()])
        stale = self.apply([self.screen(False)], expect=1, request_id="stale-request",
                           exit_code=3, error_code="revision_conflict")
        self.assertEqual(stale["error"]["details"]["actual_revision"], 2)
        self.apply([self.screen(False)], expect=2, exit_code=3, error_code="request_conflict")
        self.apply([self.screen()], expect=2, actor="another-fictional-agent",
                   exit_code=3, error_code="request_conflict")
        self.assertEqual(self.success("status")["revision"], 2)

    def test_invalid_later_operation_rolls_back_entire_batch_and_request_id(self):
        self.initialize()
        original = self.export_case()
        invalid = [self.screen(), {"op": "answer", "key": "PERSON/missing/PERSON.role",
                                   "value": "Taxpayer", **PROVENANCE}]
        self.apply(invalid, exit_code=2, error_code="INACTIVE_TASK")
        self.assertEqual(self.export_case(), original)
        self.assertEqual(len(self.success("history")["data"]["snapshots"]), 1)
        # A rolled-back request ID is available for a corrected attempt.
        self.assertEqual(self.apply([self.screen()])["revision"], 2)

    def test_dry_run_is_reviewable_without_committing_or_consuming_request_id(self):
        self.initialize()
        original = self.export_case()
        dry = self.apply(self.intake_batch(), dry_run=True)
        self.assertTrue(dry["data"]["dry_run"])
        self.assertEqual(dry["revision"], 1)
        self.assertGreater(dry["data"]["summary"]["answered_questions"], 0)
        self.assertEqual(self.export_case(), original)
        self.assertEqual(len(self.success("history")["data"]["snapshots"]), 1)
        self.assertEqual(self.apply(self.intake_batch())["revision"], 2)

    def test_export_import_roundtrip_preserves_case_and_refuses_overwrites(self):
        self.initialize()
        self.apply(self.intake_batch())
        original = self.export_case()
        destination = self.directory / "export.json"
        exported = self.success("export", "--output", str(destination))
        self.assertEqual(exported["revision"], 2)
        self.assertEqual(json.loads(destination.read_text()), original)
        self.failure("export", "--output", str(destination), exit_code=3, code="already_exists")
        imported_db = self.directory / "imported.sqlite"
        imported = self.success("import-case", "--input", str(destination), "--actor", ACTOR,
                                db=imported_db)
        self.assertEqual(imported["revision"], 1)
        self.assertEqual(self.export_case(db=imported_db), original)
        self.failure("import-case", "--input", str(destination), "--actor", ACTOR,
                     db=imported_db, exit_code=3, code="already_exists")

    def test_bundled_fictional_case_import_keeps_independent_document_tasks(self):
        self.success("import-case", "--input", str(ROOT / "examples" / "fictional_case.json"),
                     "--actor", ACTOR)
        report = self.success("report")["data"]
        evidence = {item["key"]: item for item in report["evidence"]}
        self.assertEqual(evidence["WAGE/northstar/evidence/W2"]["status"], "verified")
        self.assertEqual(evidence["WAGE/harbor/evidence/W2"]["status"], "missing")
        self.assertEqual(evidence["RETIRE/ira/evidence/IRA_HISTORY"]["status"], "missing")

    def test_report_and_planning_commands_cannot_mutate_case(self):
        self.initialize()
        self.apply(self.intake_batch())
        original = self.export_case()
        db_digest = hashlib.sha256(self.db.read_bytes()).hexdigest()
        history = self.success("history")["data"]
        for command in ("report", "plan", "questions", "next", "status"):
            with self.subTest(command=command):
                self.assertEqual(self.success(command)["revision"], 2)
        self.assertEqual(self.export_case(), original)
        self.assertEqual(self.success("history")["data"], history)
        self.assertEqual(hashlib.sha256(self.db.read_bytes()).hexdigest(), db_digest)

    def test_check_open_uses_exit_five_with_success_envelope(self):
        self.initialize()
        result = self.success("check", exit_code=5)
        self.assertEqual(result["command"], "check")
        self.assertEqual(result["revision"], 1)
        self.assertEqual(result["data"]["readiness"], "OPEN")

    def test_handoff_exports_consistent_files_and_verifiable_hashes(self):
        self.initialize()
        self.apply(self.intake_batch())
        destination = self.directory / "handoff"
        result = self.success("handoff", "--output", str(destination))
        expected_files = {"case.json", "report.json", "agent-plan.json", "open-items.md", "manifest.json"}
        self.assertEqual(set(result["data"]["files"]), expected_files)
        self.assertEqual({path.name for path in destination.iterdir()}, expected_files)
        manifest = json.loads((destination / "manifest.json").read_text())
        self.assertEqual(manifest["revision"], 2)
        self.assertEqual(manifest["case_id"], "fictional-cli-case")
        self.assertEqual(set(manifest["files"]), expected_files - {"manifest.json"})
        for name, record in manifest["files"].items():
            data = (destination / name).read_bytes()
            self.assertEqual(record["bytes"], len(data))
            self.assertEqual(record["sha256"], hashlib.sha256(data).hexdigest())
        self.assertEqual(json.loads((destination / "case.json").read_text()), self.export_case())
        self.assertEqual(json.loads((destination / "report.json").read_text())["readiness"], "OPEN")
        self.assertGreater(json.loads((destination / "agent-plan.json").read_text())["task_count"], 0)
        self.assertTrue((destination / "open-items.md").read_text().strip())
        self.failure("handoff", "--output", str(destination), exit_code=3, code="already_exists")

    def test_next_module_and_kind_filters_return_only_matching_bounded_tasks(self):
        self.initialize()
        screened = self.success("next", "--module", "WAGE", "--limit", "1")["data"]
        self.assertEqual(screened["returned"], 1)
        self.assertEqual(screened["tasks"][0]["id"], "screen/WAGE")
        self.apply(self.intake_batch())
        queue = self.success("next", "--module", "WAGE", "--kind", "evidence",
                             "--limit", "2")["data"]
        self.assertGreater(queue["matching"], 0)
        self.assertEqual(queue["returned"], len(queue["tasks"]))
        self.assertLessEqual(queue["returned"], 2)
        self.assertTrue(all(task["module"] == "WAGE" and task["kind"] == "evidence"
                            for task in queue["tasks"]))
        self.assertGreaterEqual(queue["total_open"], queue["matching"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
