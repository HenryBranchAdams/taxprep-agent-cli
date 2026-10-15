"""Persistence guarantees that agents rely on when interrupted or concurrent."""

from concurrent.futures import ThreadPoolExecutor
import os
from pathlib import Path
import sqlite3
import stat
import tempfile
import threading
import unittest
from unittest.mock import patch

from taxprep.errors import AppError
from taxprep.store import Store, _catalog_sha256


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "household.sqlite3"
        self.store = Store(self.path)
        self.case = {"case_id": "household", "audit": [], "facts": {"count": 0}}

    @staticmethod
    def increment(case):
        case["facts"]["count"] += 1
        case["audit"].append("increment")
        return case

    def initialize(self):
        return self.store.initialize(self.case, "test-agent")

    def mutate(self, revision=1, request="request-1", payload=None, **kwargs):
        return self.store.mutate(revision, request, "test-agent",
                                 payload or {"operation": "increment"},
                                 self.increment, **kwargs)

    def assert_error(self, code, operation, exit_code=None):
        with self.assertRaises(AppError) as caught:
            operation()
        self.assertEqual(caught.exception.code, code)
        if exit_code is not None:
            self.assertEqual(caught.exception.exit_code, exit_code)
        return caught.exception

    def test_private_creation_and_round_trip_without_shared_objects(self):
        initialized = self.initialize()
        self.assertEqual(initialized, {"revision": 1, "case": self.case, "replayed": False})
        self.case["facts"]["count"] = 900
        initialized["case"]["facts"]["count"] = 901
        self.assertEqual(self.store.read()["case"]["facts"]["count"], 0)
        if os.name == "posix":
            self.assertEqual(stat.S_IMODE(self.path.stat().st_mode), 0o600)

    def test_existing_file_is_never_overwritten(self):
        for content in (b"unrelated valuable file", b""):
            self.path.write_bytes(content)
            self.assert_error("already_exists", self.initialize, 3)
            self.assertEqual(self.path.read_bytes(), content)
            self.path.unlink()
        self.initialize()
        original = self.path.read_bytes()
        self.assert_error("already_exists", self.initialize, 3)
        self.assertEqual(self.path.read_bytes(), original)

    def test_missing_reads_and_mutations_do_not_create_database(self):
        for action in (self.store.read, self.store.history, self.mutate):
            self.assert_error("not_found", action, 4)
            self.assertFalse(self.path.exists())

    def test_full_snapshots_and_history_remain_available(self):
        self.initialize()
        second = self.mutate()
        third = self.mutate(2, "request-2")
        self.assertEqual([second["revision"], third["revision"]], [2, 3])
        self.assertEqual(self.store.read(1)["case"]["facts"]["count"], 0)
        self.assertEqual(self.store.read(2)["case"]["facts"]["count"], 1)
        self.assertEqual(self.store.read()["case"]["facts"]["count"], 2)
        history = self.store.history(limit=2)
        self.assertEqual([entry["revision"] for entry in history], [3, 2])
        self.assertEqual([entry["parent_revision"] for entry in history], [2, 1])
        self.assertTrue(all(entry["actor"] == "test-agent" for entry in history))
        self.assertTrue(all("case" not in entry and "payload" not in entry for entry in history))
        self.assert_error("not_found", lambda: self.store.read(99), 4)

    def test_retry_returns_original_snapshot_even_after_another_commit(self):
        self.initialize()
        committed = self.mutate(payload={"a": 1, "b": 2})
        self.mutate(2, "request-2")
        def must_not_run(case):
            self.fail("A replay must not run its callback again")
        replay = self.store.mutate(1, "request-1", "test-agent", {"b": 2, "a": 1}, must_not_run)
        self.assertTrue(replay["replayed"])
        self.assertEqual(replay["revision"], 2)
        self.assertEqual(replay["case"], committed["case"])
        self.assertEqual(self.store.read()["revision"], 3)
        self.assertEqual(len(self.store.history()), 3)

    def test_request_key_rejects_changed_actor_or_payload(self):
        self.initialize()
        self.mutate()
        self.assert_error("request_conflict", lambda: self.store.mutate(
            2, "request-1", "different-agent", {"operation": "increment"}, self.increment), 3)
        self.assert_error("request_conflict", lambda: self.mutate(
            2, "request-1", {"operation": "something-else"}), 3)
        self.assertEqual(self.store.read()["revision"], 2)

    def test_stale_revision_rejects_before_callback(self):
        self.initialize()
        self.mutate()
        def must_not_run(case):
            self.fail("A stale writer must not run its callback")
        error = self.assert_error("revision_conflict", lambda: self.store.mutate(
            1, "request-2", "test-agent", {}, must_not_run), 3)
        self.assertEqual(error.details, {"expected_revision": 1, "actual_revision": 2})
        self.assertEqual(len(self.store.history()), 2)

    def test_callback_failure_rolls_back_and_does_not_consume_request_key(self):
        self.initialize()
        def failure(case):
            case["facts"]["count"] = 100
            raise RuntimeError("simulated interrupted batch")
        with self.assertRaisesRegex(RuntimeError, "interrupted batch"):
            self.store.mutate(1, "request-1", "test-agent", {}, failure)
        self.assertEqual(self.store.read(), {"revision": 1, "case": self.case})
        self.assertEqual(len(self.store.history()), 1)
        self.assertEqual(self.mutate()["revision"], 2)

    def test_unserializable_callback_result_is_not_committed(self):
        self.initialize()
        def failure(case):
            case["facts"]["count"] = float("nan")
            return case
        with self.assertRaises(ValueError):
            self.store.mutate(1, "request-1", "test-agent", {}, failure)
        self.assertEqual(self.store.read()["case"], self.case)
        self.assertEqual(self.mutate()["revision"], 2)

    def test_dry_run_returns_proposal_without_committing_or_reserving_key(self):
        self.initialize()
        result = self.mutate(dry_run=True)
        self.assertEqual(result["revision"], 1)
        self.assertEqual(result["case"]["facts"]["count"], 1)
        self.assertTrue(result["dry_run"])
        self.assertFalse(result["replayed"])
        self.assertEqual(self.store.read()["case"], self.case)
        self.assertEqual(len(self.store.history()), 1)
        # Reusing a dry-run key with changed payload remains a new operation.
        applied = self.mutate(payload={"operation": "changed-after-preview"})
        self.assertEqual(applied["revision"], 2)
        self.assertFalse(applied["replayed"])

    def test_catalog_change_blocks_all_case_access_without_mutation(self):
        self.initialize()
        original = self.path.read_bytes()
        with patch("taxprep.store._catalog_sha256", return_value="0" * 64):
            for action in (self.store.read, self.store.history, self.mutate):
                self.assert_error("catalog_mismatch", action, 3)
        self.assertEqual(self.path.read_bytes(), original)
        self.assertEqual(self.store.read()["revision"], 1)

    def test_catalog_hash_pins_raw_bytes(self):
        resources = Path(self.temp.name) / "resources"
        resources.mkdir()
        catalog = resources / "catalog.json"
        with patch("taxprep.store.files", return_value=resources):
            catalog.write_bytes(b'{"year":2025}')
            first = _catalog_sha256()
            catalog.write_bytes(b'{ "year": 2025 }\n')
            self.assertNotEqual(_catalog_sha256(), first)

    def test_modified_snapshot_is_detected(self):
        self.initialize()
        with sqlite3.connect(self.path) as connection:
            connection.execute("UPDATE revisions SET case_json = ? WHERE revision = 1", ('{"case_id":"changed"}',))
        self.assert_error("invalid_database", self.store.read)
        self.assert_error("invalid_database", self.mutate)

    def test_unrelated_database_or_non_database_rejected(self):
        self.path.write_text("not a sqlite database")
        self.assert_error("invalid_database", self.store.read)
        self.path.unlink()
        with sqlite3.connect(self.path) as connection:
            connection.execute("CREATE TABLE unrelated (important TEXT)")
            connection.execute("INSERT INTO unrelated VALUES ('preserve')")
        self.assert_error("invalid_database", self.store.read)
        self.assert_error("invalid_database", self.mutate)
        with sqlite3.connect(self.path) as connection:
            self.assertEqual(connection.execute("SELECT important FROM unrelated").fetchone()[0], "preserve")

    def test_busy_writer_returns_retryable_typed_error(self):
        self.initialize()
        lock = sqlite3.connect(self.path, isolation_level=None)
        self.addCleanup(lock.close)
        lock.execute("BEGIN IMMEDIATE")
        try:
            with patch("taxprep.store.BUSY_TIMEOUT_SECONDS", 0.01):
                error = self.assert_error("io_error", self.mutate, 4)
            self.assertEqual(error.details["reason"], "database_busy")
            self.assertTrue(error.details["retryable"])
        finally:
            lock.rollback()
        self.assertEqual(self.mutate()["revision"], 2)

    def test_two_writers_cannot_silently_overwrite_each_other(self):
        self.initialize()
        ready = threading.Barrier(2)
        def writer(request):
            ready.wait(timeout=5)
            try:
                return Store(self.path).mutate(1, request, "test-agent", {}, self.increment)["revision"]
            except AppError as error:
                return error.code
        with ThreadPoolExecutor(max_workers=2) as pool:
            outcomes = list(pool.map(writer, ["writer-a", "writer-b"]))
        self.assertCountEqual(outcomes, [2, "revision_conflict"])
        self.assertEqual(self.store.read()["case"]["facts"]["count"], 1)
        self.assertEqual(len(self.store.history()), 2)

    def test_failed_initialization_does_not_leave_partial_database(self):
        with patch("taxprep.store.sqlite3.connect", side_effect=sqlite3.OperationalError("database is locked")):
            self.assert_error("io_error", self.initialize, 4)
        self.assertFalse(self.path.exists())
        self.assertEqual(self.initialize()["revision"], 1)

    @unittest.skipUnless(os.name == "posix", "POSIX permissions")
    def test_existing_database_permissions_are_restricted(self):
        self.initialize()
        self.path.chmod(0o666)
        self.store.read()
        self.assertEqual(stat.S_IMODE(self.path.stat().st_mode), 0o600)

    @unittest.skipUnless(hasattr(os, "symlink"), "symlink support")
    def test_symlink_does_not_redirect_case_writes(self):
        target = Path(self.temp.name) / "valuable.txt"
        target.write_text("preserve")
        self.path.symlink_to(target)
        self.assert_error("already_exists", self.initialize, 3)
        self.assert_error("invalid_database", self.store.read)
        self.assert_error("invalid_database", self.mutate)
        self.assertEqual(target.read_text(), "preserve")


if __name__ == "__main__":
    unittest.main()
