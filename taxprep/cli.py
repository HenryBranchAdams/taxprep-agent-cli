"""Noninteractive JSON command protocol. No network access or tax calculations."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile

from . import __version__, engine as E, planner
from .errors import AppError
from .operations import apply_operations, operation_schema
from .store import Store

PROTOCOL = "1.0"
KINDS = ["scope_or_inventory", "confirm_fact", "evidence", "form_applicability",
         "technical_review", "cross_topic_route"]


def dumps(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2) + "\n"


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON object key: " + key)
        result[key] = value
    return result


def load_json(path):
    def invalid_constant(value):
        raise ValueError("Nonfinite JSON number: " + value)
    try:
        text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
        return json.loads(text, object_pairs_hook=_pairs, parse_constant=invalid_constant)
    except (ValueError, UnicodeError) as exc:
        raise AppError("invalid_json", str(exc)) from exc


class Parser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "allow_abbrev": False})

    def error(self, message):
        raise AppError("invalid_arguments", message)


def positive(value):
    value = int(value)
    if value < 1:
        raise argparse.ArgumentTypeError("Must be at least 1")
    return value


def parser():
    p = Parser(prog="taxprep", description="Agent CLI for the 2025 tax intake workflow. JSON output; never prompts.")
    p.add_argument("--db", default="taxprep.sqlite", help="One SQLite database per case (put before subcommand)")
    p.add_argument("--version", action="store_true")
    sub = p.add_subparsers(dest="command")
    new = sub.add_parser("init", help="Initialize a new case; refuses existing paths")
    new.add_argument("--case-id", required=True)
    new.add_argument("--year", type=int, choices=[2025], default=2025)
    new.add_argument("--actor", required=True)
    imp = sub.add_parser("import-case", help="Import workbench case JSON into a NEW database")
    imp.add_argument("--input", required=True, help="JSON file or - for stdin")
    imp.add_argument("--actor", required=True)
    for command, desc in [("status", "Summary and revision"), ("plan", "All open tasks with search and acceptance details"),
                          ("report", "Full evaluated case"), ("check", "Exit 5 when preparation work remains open"),
                          ("doctor", "Validate bundled catalog and runtime")]:
        sub.add_parser(command, help=desc)
    nxt = sub.add_parser("next", help="Bounded, prioritized open work queue")
    nxt.add_argument("--limit", type=positive, default=10)
    nxt.add_argument("--kind", choices=KINDS)
    nxt.add_argument("--module", choices=sorted(E.MOD))
    qs = sub.add_parser("questions", help="Questions with types, choices, and answer state")
    qs.add_argument("--module", choices=sorted(E.MOD))
    qs.add_argument("--include-inactive", action="store_true")
    ins = sub.add_parser("inspect", help="Inspect one exact case task/question key")
    ins.add_argument("key")
    apply = sub.add_parser("apply", help="Validate and atomically commit a JSON operation batch")
    apply.add_argument("--input", required=True, help="JSON file or - for stdin")
    apply.add_argument("--expect", required=True, type=positive, help="Last observed revision")
    apply.add_argument("--request-id", required=True, help="Stable idempotency key for retries")
    apply.add_argument("--actor", required=True)
    apply.add_argument("--dry-run", action="store_true")
    ex = sub.add_parser("export", help="Export workbench-compatible case JSON; refuses overwrite")
    ex.add_argument("--output", required=True, help="New output file or - for raw JSON on stdout")
    ex.add_argument("--revision", type=positive)
    hand = sub.add_parser("handoff", help="Create a new directory with case, reports, queue, and checksums")
    hand.add_argument("--output", required=True)
    hist = sub.add_parser("history", help="Read committed snapshot metadata")
    hist.add_argument("--limit", type=positive, default=100)
    cat = sub.add_parser("catalog", help="Search or inspect the complete reference catalog")
    cat.add_argument("--kind", choices=["modules", "questions", "rules", "documents", "sources", "routes"], default="modules")
    cat.add_argument("--id")
    cat.add_argument("--module", choices=sorted(E.MOD))
    cat.add_argument("--query")
    schema = sub.add_parser("schema", help="Machine-readable input and output contract")
    schema.add_argument("--target", choices=["operations", "protocol"], default="operations")
    return p


def enrich_plan(case):
    plan = planner.build_plan(case)
    for task in plan["tasks"]:
        parts = task["id"].split("/")
        if parts[0] in ("screen", "roster", "enumerate"):
            task["module"] = parts[1]
            task["operation"] = "screen" if parts[0] == "screen" else "enumerate"
            task["specification"] = E.MOD[parts[1]]
        elif parts[0] in E.MOD:
            task.setdefault("module", parts[0])
    return plan


def summary(snapshot):
    result = E.evaluate(snapshot["case"])
    return {"case_id": result["case_id"], "tax_year": result["tax_year"],
            "readiness": result["readiness"], "summary": result["summary"],
            "scope": E.CAT["scope"], "authorization": result["authorization"]}


def secure_write_new(path, text):
    path = Path(path).absolute()
    if path.exists() or path.is_symlink():
        raise AppError("already_exists", "Output already exists; choose a new path.", 3)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Link a fully fsynced temp file into place atomically without replacing a target.
    fd, temp = tempfile.mkstemp(prefix=".taxprep-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        try:
            os.link(temp, path)
        except FileExistsError as exc:
            raise AppError("already_exists", "Output was created by another process.", 3) from exc
    finally:
        os.unlink(temp)
    return str(path)


def handoff(snapshot, destination):
    target = Path(destination).absolute()
    if target.exists() or target.is_symlink():
        raise AppError("already_exists", "Handoff destination exists; choose a new directory.", 3)
    target.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".taxprep-handoff-", dir=target.parent))
    case = snapshot["case"]
    created_target = False
    complete = False
    try:
        report = E.evaluate(case)
        contents = {"case.json": case, "report.json": report, "agent-plan.json": enrich_plan(case)}
        for name, value in contents.items():
            secure_write_new(staging/name, dumps(value))
        E.write_report_md(report, staging/"open-items.md")
        os.chmod(staging/"open-items.md", 0o600)
        files = {p.name: {"sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "bytes": p.stat().st_size}
                 for p in sorted(staging.iterdir())}
        secure_write_new(staging/"manifest.json", dumps({"protocol_version": PROTOCOL, "revision": snapshot["revision"],
                         "case_id": case["case_id"], "created_at": E.now(), "files": files}))
        # mkdir reserves the destination without ever replacing someone else's path.
        target.mkdir(mode=0o700)
        created_target = True
        for item in staging.iterdir():
            os.replace(item, target/item.name)
        complete = True
        return {"directory": str(target), "files": sorted([*files, "manifest.json"]), "readiness": report["readiness"]}
    finally:
        shutil.rmtree(staging)
        if created_target and not complete:
            shutil.rmtree(target)


def protocol_schema():
    return {"protocol_version": PROTOCOL, "json_default": True, "interactive": False,
            "global_options": {"--db": "Database path; place before command"},
            "commands": ["init", "import-case", "status", "next", "plan", "questions", "inspect", "report", "check",
                         "apply", "export", "handoff", "history", "catalog", "schema", "doctor"],
            "success_envelope": {"ok": True, "protocol_version": PROTOCOL, "command": "name", "revision": "integer or null", "data": "object"},
            "error_envelope": {"ok": False, "protocol_version": PROTOCOL, "error": {"code": "stable identifier", "message": "description", "details": "optional"}},
            "streams": {"success": "stdout", "error": "stderr", "help": "stdout text", "export_stdout": "raw case JSON when --output -"},
            "exit_codes": {"0": "Success, including OPEN status", "2": "Invalid arguments, JSON, or data", "3": "Revision, idempotency, catalog, or path conflict",
                           "4": "Missing resource or IO failure", "5": "check found OPEN readiness", "70": "Unexpected internal failure"},
            "mutation": {"command": "apply", "required": ["--expect", "--request-id", "--actor", "--input"],
                         "atomic": True, "retry": "Retry identical payload and actor with the same request ID; reuse with different content is rejected",
                         "dry_run": "Validates proposed case without committing; returned revision remains the current committed revision"},
            "case_schema_version": "2.0", "catalog_year": 2025, "maximum_readiness": "READY_FOR_PREPARER_REVIEW"}


def dispatch(args):
    command = args.command
    if args.version:
        return {"version": __version__}, None, 0
    if command == "schema":
        return operation_schema() if args.target == "operations" else protocol_schema(), None, 0
    if command == "doctor":
        graph = E.validate_catalog()
        return {"version": __version__, "python": sys.version.split()[0], "catalog_year": 2025,
                "modules": len(E.MOD), "questions": len(E.QUESTIONS), "rules": len(E.CAT["rules"]),
                "graph": {k: graph[k] for k in ["valid", "nodes", "edges"]}, "runtime_dependencies": []}, None, 0
    if command == "catalog":
        records = E.CAT[args.kind]
        records = list(records.values()) if isinstance(records, dict) else records
        if args.id:
            records = [x for x in records if x["id"] == args.id]
            if not records:
                raise AppError("not_found", "Catalog ID not found in selected kind.", 4)
        if args.module:
            if args.kind in ("documents", "sources"):
                specs = [r for r in E.CAT["rules"] if r["module"] == args.module]
                ids = {k for r in specs for k in r[args.kind]}
                if args.kind == "sources":
                    ids.update(E.MOD[args.module]["sources"])
                    ids.update(s for q in E.LOCAL[args.module] for s in q["sources"])
                records = [x for x in records if x["id"] in ids]
            else:
                records = [x for x in records if x.get("module", x["id"]) == args.module]
        if args.query:
            records = [x for x in records if args.query.casefold() in json.dumps(x, ensure_ascii=False).casefold()]
        return {"kind": args.kind, "count": len(records), "items": records}, None, 0
    if not command:
        raise AppError("invalid_arguments", "A command is required; run taxprep --help.")
    store = Store(args.db)
    if command in ("init", "import-case"):
        if not args.actor.strip():
            raise AppError("invalid_arguments", "Actor must be nonblank.")
        case = E.new_case() if command == "init" else load_json(args.input)
        if command == "init":
            case["case_id"] = args.case_id
        E.validate_case(case)
        E.evaluate(case)
        snap = store.initialize(case, args.actor)
        return summary(snap), snap["revision"], 0
    if command == "apply":
        payload = load_json(args.input)
        snap = store.mutate(args.expect, args.request_id, args.actor, payload,
                            lambda case: apply_operations(case, payload, args.actor), args.dry_run)
        return {**summary(snap), "replayed": snap["replayed"], "dry_run": snap.get("dry_run", False)}, snap["revision"], 0
    if command == "history":
        return {"snapshots": store.history(args.limit)}, None, 0
    snap = store.read(args.revision if command == "export" else None)
    case, revision = snap["case"], snap["revision"]
    E.validate_case(case)
    if command in ("status", "check"):
        result = summary(snap)
        return result, revision, 5 if command == "check" and result["readiness"] == "OPEN" else 0
    if command == "export":
        if args.output == "-":
            return case, revision, -1
        return {"path": secure_write_new(args.output, dumps(case)), "case_id": case["case_id"]}, revision, 0
    if command == "handoff":
        return handoff(snap, args.output), revision, 0
    if command in ("plan", "next"):
        plan = enrich_plan(case)
        if command == "next":
            tasks = [t for t in plan["tasks"] if (not args.kind or t["kind"] == args.kind)
                     and (not args.module or t.get("module") == args.module)]
            plan = {"case_id": case["case_id"], "readiness": plan["readiness"], "total_open": plan["task_count"],
                    "matching": len(tasks), "returned": min(len(tasks), args.limit), "tasks": tasks[:args.limit],
                    "still_waiting_on_upstream": plan["still_waiting_on_upstream"]}
        return plan, revision, 0
    report = E.evaluate(case)
    if command == "report":
        return report, revision, 0
    if command == "questions":
        items = [{**q, "specification": E.QUESTIONS[q["id"]]} for q in report["questions"]
                 if (not args.module or q["module"] == args.module)
                 and (args.include_inactive or q["visibility"] is True)]
        return {"count": len(items), "items": items}, revision, 0
    if command == "inspect":
        for section in ["questions", "evidence", "form_candidates", "reviews", "routes", "issues"]:
            for item in report[section]:
                if item.get("key", item.get("id")) == args.key:
                    result = {"section": section, **item}
                    if section == "questions":
                        result["specification"] = E.QUESTIONS[item["id"]]
                    elif section == "evidence":
                        result["specification"] = E.CAT["documents"][item["document_id"]]
                    return result, revision, 0
        raise AppError("not_found", "No current task or question matches that exact key.", 4)
    raise AppError("invalid_arguments", "Unknown command.")


def main(argv=None):
    try:
        args = parser().parse_args(argv)
        data, revision, code = dispatch(args)
        if code == -1:
            sys.stdout.write(dumps(data))
            return 0
        sys.stdout.write(dumps({"ok": True, "protocol_version": PROTOCOL, "command": args.command or "version",
                               "revision": revision, "data": data}))
        return code
    except AppError as exc:
        error = exc
    except (ValueError, TypeError, KeyError, StopIteration) as exc:
        error = AppError("invalid_data", str(exc) or "Invalid data")
    except OSError as exc:
        error = AppError("io_error", str(exc), 4)
    except Exception as exc:
        error = AppError("internal_error", "Unexpected failure: " + type(exc).__name__, 70)
    payload = {"code": error.code, "message": error.message}
    if error.details is not None:
        payload["details"] = error.details
    sys.stderr.write(dumps({"ok": False, "protocol_version": PROTOCOL, "error": payload}))
    return error.exit_code
