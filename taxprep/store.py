"""Transactional, revisioned storage for one local preparation case.

Snapshots are deliberately complete rather than patches. Request identifiers make
an interrupted agent's retry safe; optimistic revisions keep two agents from
silently replacing each other's work. This is a local, unencrypted SQLite file,
not an authenticated or tamper-proof audit service.
"""

from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
from importlib.resources import files
import json
import os
from pathlib import Path
import sqlite3
import stat
from typing import Callable

from .errors import AppError


SCHEMA_VERSION = "1"
BUSY_TIMEOUT_SECONDS = 2.0


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def _json(value: object) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False)


def _sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _catalog_sha256() -> str:
    """Pin exact catalog bytes, including changes invisible to JSON parsing."""
    try:
        return hashlib.sha256(files("taxprep").joinpath("catalog.json").read_bytes()).hexdigest()
    except OSError as exc:
        raise AppError("io_error", "Cannot read the packaged question catalog.",
                       exit_code=4) from exc


def _require_text(value: str, name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a nonempty string")


def _case_json(case: dict) -> str:
    if not isinstance(case, dict):
        raise ValueError("Case must be a JSON object")
    return _json(case)


def _database_error(exc: sqlite3.Error) -> AppError:
    code = getattr(exc, "sqlite_errorcode", None)
    # Extended SQLite error codes carry the primary code in their low byte.
    primary = code & 255 if isinstance(code, int) else None
    # Python 3.10 lacks the exception error-code attributes/constants added in
    # 3.11. Primary SQLite result codes are stable; text fallback handles busy.
    if primary in (5, 6) or any(
        word in str(exc).lower() for word in ("locked", "busy")
    ):
        return AppError(
            "io_error", "Case database is busy. Retry the same request after the other writer finishes.",
            exit_code=4, details={"reason": "database_busy", "retryable": True})
    if primary in (14, 10, 8, 13, 3):  # CANTOPEN, IOERR, READONLY, FULL, PERM
        return AppError("io_error", "Cannot access or durably write the case database.",
                        exit_code=4, details={"reason": "sqlite_io_error"})
    return AppError("invalid_database", "The file is not a valid taxprep case database.")


class Store:
    """A fresh connection is used for each operation; instances hold no locks."""

    def __init__(self, path: str | os.PathLike[str]):
        self.path = Path(path).expanduser().absolute()

    def _protect(self) -> None:
        try:
            info = self.path.lstat()
            if not stat.S_ISREG(info.st_mode):
                raise AppError("invalid_database", "Case database must be a regular file, not a link or directory.")
            if os.name == "posix":
                self.path.chmod(0o600)
                # Existing SQLite sidecars can contain case data as well.
                for suffix in ("-journal", "-wal", "-shm"):
                    sidecar = Path(str(self.path) + suffix)
                    try:
                        info = sidecar.lstat()
                    except FileNotFoundError:
                        continue
                    if not stat.S_ISREG(info.st_mode):
                        raise AppError("invalid_database", "Case database sidecar must be a regular file.")
                    try:
                        sidecar.chmod(0o600)
                    except FileNotFoundError:
                        # A concurrent writer can remove its rollback journal
                        # after lstat but before chmod.
                        continue
        except FileNotFoundError as exc:
            raise AppError("not_found", "Case database does not exist. Initialize or import a case first.",
                           exit_code=4) from exc
        except OSError as exc:
            raise AppError("io_error", "Cannot secure or access the case database.",
                           exit_code=4) from exc

    @contextmanager
    def _connection(self, write: bool = False):
        self._protect()
        connection = None
        try:
            # URI mode prevents an absent/misspelled database from being created.
            connection = sqlite3.connect(
                self.path.as_uri() + ("?mode=rw" if write else "?mode=ro"),
                uri=True, timeout=BUSY_TIMEOUT_SECONDS, isolation_level=None)
            connection.row_factory = sqlite3.Row
            connection.execute("PRAGMA foreign_keys = ON")
            if write:
                connection.execute("PRAGMA synchronous = FULL")
                connection.execute("PRAGMA fullfsync = ON")
            connection.execute("BEGIN IMMEDIATE" if write else "BEGIN")
            yield connection
        except sqlite3.Error as exc:
            raise _database_error(exc) from exc
        finally:
            if connection is not None:
                try:
                    if connection.in_transaction:
                        try:
                            connection.rollback()
                        except sqlite3.Error:
                            # Closing also rolls back. Do not hide the original
                            # callback/database error if rollback itself fails.
                            pass
                finally:
                    connection.close()

    @staticmethod
    def _check_metadata(connection: sqlite3.Connection) -> None:
        metadata = dict(connection.execute("SELECT key, value FROM metadata"))
        if metadata.get("application") != "taxprep" or metadata.get("schema_version") != SCHEMA_VERSION:
            raise AppError("invalid_database", "Unsupported or uninitialized taxprep database.")
        actual = _catalog_sha256()
        stored = metadata.get("catalog_sha256")
        if not stored:
            raise AppError("invalid_database", "Case database has no catalog fingerprint.")
        if stored != actual:
            raise AppError("catalog_mismatch", "Case was created with a different question catalog. Use its matching catalog before editing or evaluating it.",
                           exit_code=3,
                           details={"database_catalog_sha256": stored, "current_catalog_sha256": actual})

    @staticmethod
    def _snapshot(row: sqlite3.Row | None) -> dict:
        if row is None:
            raise AppError("not_found", "The requested case revision does not exist.", exit_code=4)
        serialized = row["case_json"]
        if not isinstance(serialized, str) or _sha256(serialized) != row["case_sha256"]:
            raise AppError("invalid_database", "Case snapshot checksum does not match its saved contents.")
        try:
            case = json.loads(serialized)
        except (ValueError, TypeError) as exc:
            raise AppError("invalid_database", "Case snapshot contains invalid JSON.") from exc
        if not isinstance(case, dict):
            raise AppError("invalid_database", "Case snapshot must contain a JSON object.")
        return {"revision": row["revision"], "case": case}

    def initialize(self, case: dict, actor: str) -> dict:
        """Create a private database. Never replace any existing file."""
        _require_text(actor, "actor")
        serialized = _case_json(case)
        catalog_digest = _catalog_sha256()
        created = False
        committed = False
        try:
            self.path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
            fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            os.close(fd)
            created = True
            with self._connection(write=True) as connection:
                # Do not use executescript: it implicitly commits transactions.
                connection.execute("CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
                connection.execute("""CREATE TABLE revisions (
                    revision INTEGER PRIMARY KEY CHECK (revision > 0),
                    parent_revision INTEGER REFERENCES revisions(revision),
                    case_json TEXT NOT NULL,
                    case_sha256 TEXT NOT NULL,
                    actor TEXT NOT NULL,
                    request_id TEXT UNIQUE,
                    payload_sha256 TEXT,
                    created_at TEXT NOT NULL
                )""")
                connection.executemany("INSERT INTO metadata (key, value) VALUES (?, ?)", [
                    ("application", "taxprep"), ("schema_version", SCHEMA_VERSION),
                    ("catalog_sha256", catalog_digest), ("created_at", _now())])
                connection.execute(
                    """INSERT INTO revisions (revision, parent_revision, case_json, case_sha256,
                       actor, request_id, payload_sha256, created_at)
                       VALUES (1, NULL, ?, ?, ?, NULL, NULL, ?)""",
                    (serialized, _sha256(serialized), actor, _now()))
                connection.commit()
                committed = True
            # SQLite synchronizes the database; sync its new directory entry too.
            if os.name == "posix":
                directory = os.open(self.path.parent, os.O_RDONLY)
                try:
                    os.fsync(directory)
                finally:
                    os.close(directory)
            return {"revision": 1, "case": json.loads(serialized), "replayed": False}
        except FileExistsError as exc:
            raise AppError("already_exists", "A file already exists at the case path. Open it or choose a new path; initialization never overwrites a file.",
                           exit_code=3) from exc
        except OSError as exc:
            raise AppError("io_error", "Cannot create or durably save the case database.", exit_code=4) from exc
        finally:
            # A failed initialization must not leave a misleading empty database.
            # Only remove the file created by this invocation, never preexisting data.
            if created and not committed:
                try:
                    self.path.unlink()
                except OSError:
                    pass

    def read(self, revision: int | None = None) -> dict:
        if revision is not None and (type(revision) is not int or revision < 1):
            raise ValueError("revision must be a positive integer")
        with self._connection() as connection:
            self._check_metadata(connection)
            if revision is None:
                row = connection.execute("SELECT * FROM revisions ORDER BY revision DESC LIMIT 1").fetchone()
            else:
                row = connection.execute("SELECT * FROM revisions WHERE revision = ?", (revision,)).fetchone()
            return self._snapshot(row)

    def mutate(self, expected_revision: int, request_id: str, actor: str,
               payload: dict, transform: Callable[[dict], dict],
               dry_run: bool = False) -> dict:
        """Apply one atomic change, or return the result of its exact prior retry.

        A dry run returns the proposed case and the unchanged committed revision.
        Callback exceptions roll back the whole transaction, including idempotency.
        """
        if type(expected_revision) is not int or expected_revision < 1:
            raise ValueError("expected_revision must be a positive integer")
        _require_text(request_id, "request_id")
        _require_text(actor, "actor")
        if not isinstance(payload, dict):
            raise ValueError("payload must be a JSON object")
        digest = _sha256(_json({"actor": actor, "payload": payload}))
        with self._connection(write=True) as connection:
            self._check_metadata(connection)
            previous = connection.execute("SELECT * FROM revisions WHERE request_id = ?", (request_id,)).fetchone()
            if previous is not None:
                if previous["payload_sha256"] != digest or previous["actor"] != actor:
                    raise AppError("request_conflict", "Request ID was already used with a different actor or payload. Use a new request ID for a new operation.",
                                   exit_code=3, details={"request_id": request_id})
                return {**self._snapshot(previous), "replayed": True, "dry_run": bool(dry_run)}
            current = self._snapshot(connection.execute("SELECT * FROM revisions ORDER BY revision DESC LIMIT 1").fetchone())
            if current["revision"] != expected_revision:
                raise AppError("revision_conflict", "Case changed since it was read. Read the current revision before preparing another mutation.",
                               exit_code=3, details={"expected_revision": expected_revision,
                                                    "actual_revision": current["revision"]})
            proposed = transform(current["case"])
            serialized = _case_json(proposed)
            if dry_run:
                return {"revision": current["revision"], "case": json.loads(serialized),
                        "replayed": False, "dry_run": True}
            next_revision = current["revision"] + 1
            connection.execute(
                """INSERT INTO revisions (revision, parent_revision, case_json, case_sha256,
                   actor, request_id, payload_sha256, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (next_revision, current["revision"], serialized, _sha256(serialized),
                 actor, request_id, digest, _now()))
            connection.commit()
            return {"revision": next_revision, "case": json.loads(serialized),
                    "replayed": False, "dry_run": False}

    def history(self, limit: int = 100) -> list[dict]:
        """Newest-first revision metadata without exposing whole case snapshots."""
        if type(limit) is not int or limit < 1:
            raise ValueError("limit must be a positive integer")
        with self._connection() as connection:
            self._check_metadata(connection)
            rows = connection.execute(
                """SELECT revision, parent_revision, actor, request_id, payload_sha256,
                   case_sha256, created_at FROM revisions ORDER BY revision DESC LIMIT ?""", (limit,))
            return [dict(row) for row in rows]
