"""Strict, atomic, dependency-free operations for an agent-owned case.

The caller supplies an actor identity; this module records, but does not
authenticate, that identity. It performs no filesystem or network operations.
"""
from __future__ import annotations

from copy import deepcopy
import math
import re

from . import engine
from .errors import AppError


CHECKS = ("year", "owner", "entity", "complete", "corrections", "reconciled")
CLOSED = frozenset(("verified", "alternative_accepted", "not_required"))
STATUSES = ("missing", "searching", "located", "verified", "rejected",
            "alternative_accepted", "not_required", "stale")
_SHAPES = {
    "answer": (("op", "key", "value", "source", "reference"), ("status",)),
    "screen": (("op", "module", "value", "source", "reference"), ("status",)),
    "entity_add": (("op", "module", "id", "label"), ("owner_ids",)),
    "entity_update": (("op", "module", "id"), ("label", "owner_ids")),
    "enumerate": (("op", "module", "complete", "source", "reference"), ()),
    "evidence": (("op", "key", "status"), ("reference", "note", "checks",
                 "fingerprint", "source_version", "sha256")),
    "decision": (("op", "key", "decision", "reference", "note", "fingerprint"), ()),
    "resolve": (("op", "kind", "key", "reference", "note", "fingerprint"), ()),
    "search_log": (("op", "key", "source", "query", "outcome", "reference"), ("note",)),
    "source_change": (("op", "key", "reference", "note"), ("source_version", "sha256")),
}


def _error(message, code="INVALID_OPERATION", **details):
    raise AppError(code, message, details=details or None)


def _text(value, field):
    if not isinstance(value, str) or not value.strip():
        _error(f"{field} must be nonblank text", field=field)


def _shape(op):
    if not isinstance(op, dict):
        _error("Each operation must be an object")
    kind = op.get("op")
    if not isinstance(kind, str) or kind not in _SHAPES:
        _error("Unknown operation", operation=kind)
    required, optional = _SHAPES[kind]
    missing = set(required) - set(op)
    extra = set(op) - set(required) - set(optional)
    if missing or extra:
        _error("Operation has missing or unknown fields", operation=kind,
               missing=sorted(missing), unknown=sorted(extra))
    for field, value in op.items():
        if field not in ("value", "complete", "checks", "owner_ids"):
            _text(value, field)
    if "module" in op and op["module"] not in engine.MOD:
        _error("Unknown module", module=op["module"])
    if "id" in op and ("/" in op["id"] or op["id"] != op["id"].strip()):
        _error("Entity ID must not contain / or surrounding whitespace")
    if kind in ("answer", "screen"):
        if op.get("status", "confirmed") not in ("confirmed", "tentative", "conflict"):
            _error("Invalid answer status")
        value = op["value"]
        if value is not None and type(value) not in (str, bool, int, float):
            _error("Answer values must be JSON scalars or null")
        if type(value) in (int, float) and not math.isfinite(value):
            _error("Answer numbers must be finite")
        if kind == "screen" and value is not None and type(value) is not bool:
            _error("Screen value must be true, false, or null")
    if "complete" in op and type(op["complete"]) is not bool:
        _error("complete must be a boolean")
    if "owner_ids" in op:
        owners = op["owner_ids"]
        if (not isinstance(owners, list) or any(not isinstance(p, str) or not p.strip()
                                               or "/" in p for p in owners)):
            _error("owner_ids must be an array of nonblank person IDs")
        if len(set(owners)) != len(owners):
            _error("owner_ids must not contain duplicates")
    if kind == "entity_update" and not ({"label", "owner_ids"} & set(op)):
        _error("entity_update requires label or owner_ids")
    if "checks" in op:
        checks = op["checks"]
        if (not isinstance(checks, dict) or set(checks) - set(CHECKS)
                or any(type(v) is not bool for v in checks.values())):
            _error("checks may contain only the six named boolean verification checks")
    if "sha256" in op and not re.fullmatch(r"[0-9a-fA-F]{64}", op["sha256"]):
        _error("sha256 must contain exactly 64 hexadecimal characters")
    if kind == "evidence":
        if op["status"] not in STATUSES:
            _error("Invalid evidence status")
        needed = set()
        if op["status"] in CLOSED:
            needed.update(("reference", "note", "fingerprint"))
            if op["status"] != "not_required":
                if not all(op.get("checks", {}).get(check) is True for check in CHECKS):
                    _error("Verified or accepted alternative evidence requires all six checks to be true")
        elif op["status"] == "located":
            needed.add("reference")
        elif op["status"] == "rejected":
            needed.add("note")
        if needed - set(op):
            _error("Evidence status requires additional fields", missing=sorted(needed - set(op)))
    if kind == "decision" and op["decision"] not in ("required", "not_required"):
        _error("decision must be required or not_required")
    if kind == "resolve" and op["kind"] not in ("review", "route"):
        _error("Resolution kind must be review or route")
    if kind == "search_log" and op["outcome"] not in ("found", "not_found", "inaccessible"):
        _error("Invalid search outcome")


def _audit(case, action, subject, before, after, actor):
    # A deep copy is essential: later operations must not rewrite earlier history.
    case["audit"].append({"at": engine.now(), "actor": actor, "action": action,
                          "subject": subject, "before": deepcopy(before), "after": deepcopy(after)})


def _put(case, collection, key, record, actor, action):
    old = case[collection].get(key)
    case[collection][key] = deepcopy(record)
    _audit(case, action, key, old, record, actor)


def _task(report, collection, key):
    for task in report[collection]:
        if task["key"] == key:
            return task
    _error("Task key is invalid or inactive", code="INACTIVE_TASK", key=key, kind=collection)


def _current_fingerprint(op, task):
    if op["fingerprint"] != task["fingerprint"]:
        _error("Fingerprint does not match the current task context", code="STALE_FINGERPRINT",
               key=op["key"], expected=task["fingerprint"], supplied=op["fingerprint"])


def _active_module(case, mid, repeatable=False):
    if engine.module_status(case, mid) is not True:
        _error("Module must be confirmed active", code="INACTIVE_MODULE", module=mid)
    if repeatable and not engine.MOD[mid]["repeatable"]:
        _error("Operation requires a repeatable module", module=mid)


def _owners(case, mid, owners):
    if mid == "PERSON" and owners:
        _error("PERSON entities must not have owner_ids")
    people = {p["id"] for p in case["entities"]["PERSON"]}
    invalid = set(owners) - people
    if invalid:
        _error("owner_ids must refer to existing PERSON entities", unknown=sorted(invalid))


def _answer_record(op, actor):
    # Even null facts retain their actual provenance, while remaining unknown.
    return {"value": op["value"], "status": op.get("status", "confirmed"),
            "source": op["source"], "reference": op["reference"], "actor": actor, "at": engine.now()}


def _source_change(case, op, report, actor):
    task = _task(report, "evidence", op["key"])
    stale_marker = "source-changed:" + engine.now()
    rec = deepcopy(case["evidence"].get(op["key"], {}))
    rec.update({k: v for k, v in op.items() if k not in ("op", "key")})
    rec.update(status="stale", fingerprint=stale_marker, actor=actor, at=engine.now())
    _put(case, "evidence", op["key"], rec, actor, "source_change")
    prefix = task["module"] + "/" + task["entity_id"] + "/"
    global_source = task["module"] in ("CORE", "PERSON", "STATUS", "STATE")
    # The base fingerprint deliberately excludes source bytes. Explicitly poison
    # previous review fingerprints so restored facts cannot silently revive them.
    for collection in ("form_decisions", "reviews", "route_decisions"):
        for key, old in list(case[collection].items()):
            if global_source or key.startswith(prefix):
                changed = deepcopy(old)
                changed.update(fingerprint=stale_marker, invalidated_at=engine.now(),
                               invalidated_by=actor, invalidation_source=op["key"])
                _put(case, collection, key, changed, actor, "source_invalidation")


def apply_operations(case, payload, actor):
    """Return a changed deep copy, or raise AppError without changing ``case``.

    Operations are evaluated in order; an earlier confirmed answer may activate
    a later task. Every closure must still be valid at the end of the batch.
    ``actor`` is required separately and cannot be overridden by an operation.
    """
    _text(actor, "actor")
    if not isinstance(payload, dict) or set(payload) != {"operations"}:
        _error("Payload must be an object containing only operations")
    operations = payload["operations"]
    if not isinstance(operations, list) or len(operations) > 500:
        _error("operations must be an array with at most 500 entries")
    for index, op in enumerate(operations):
        try:
            _shape(op)
        except AppError as exc:
            # Keep the public exception object usable by the CLI's JSON wrapper.
            if isinstance(getattr(exc, "details", None), dict):
                exc.details["operation_index"] = index
            raise
    changed = deepcopy(case)
    closures = []
    for index, op in enumerate(operations):
        kind = op["op"]
        try:
            report = engine.evaluate(changed)
            if kind == "answer":
                task = _task(report, "questions", op["key"])
                if task["visibility"] is not True:
                    _error("Question is not currently visible", code="INACTIVE_TASK", key=op["key"])
                engine.validate_answer(engine.QUESTIONS[task["id"]], op["value"])
                ent = engine.entity(changed, task["module"], task["entity_id"])
                old = ent["answers"].get(task["id"])
                rec = _answer_record(op, actor)
                ent["answers"][task["id"]] = rec
                _audit(changed, kind, op["key"], old, rec, actor)
            elif kind == "screen":
                if op["module"] not in changed["screens"]:
                    _error("Mandatory modules have no screen answer", module=op["module"])
                _put(changed, "screens", op["module"], _answer_record(op, actor), actor, kind)
            elif kind in ("entity_add", "entity_update"):
                mid = op["module"]
                _active_module(changed, mid, repeatable=kind == "entity_add")
                items = changed["entities"][mid]
                existing = next((ent for ent in items if ent["id"] == op["id"]), None)
                if kind == "entity_add":
                    if existing is not None:
                        _error("Entity ID already exists", module=mid, id=op["id"])
                    owners = op.get("owner_ids", [])
                    _owners(changed, mid, owners)
                    ent = {"id": op["id"], "label": op["label"].strip(),
                           "owner_ids": deepcopy(owners), "answers": {}}
                    items.append(ent)
                    _audit(changed, kind, mid + "/" + op["id"], None, ent, actor)
                    if mid in changed["enumerated"]:
                        old_seal = changed["enumerated"].pop(mid)
                        _audit(changed, "enumeration_invalidation", mid, old_seal, None, actor)
                else:
                    if existing is None:
                        _error("Entity does not exist", module=mid, id=op["id"])
                    before = deepcopy(existing)
                    if "owner_ids" in op:
                        _owners(changed, mid, op["owner_ids"])
                        existing["owner_ids"] = deepcopy(op["owner_ids"])
                    if "label" in op:
                        existing["label"] = op["label"].strip()
                    _audit(changed, kind, mid + "/" + op["id"], before, existing, actor)
            elif kind == "enumerate":
                mid = op["module"]
                _active_module(changed, mid, repeatable=True)
                ids = sorted(ent["id"] for ent in changed["entities"][mid])
                if op["complete"] and not ids:
                    _error("An empty active roster cannot be declared complete", module=mid)
                rec = {"complete": op["complete"], "entity_ids": ids, "source": op["source"],
                       "reference": op["reference"], "actor": actor, "at": engine.now()}
                _put(changed, "enumerated", mid, rec, actor, kind)
            elif kind == "evidence":
                task = _task(report, "evidence", op["key"])
                previous = changed["evidence"].get(op["key"], {})
                for field in ("source_version", "sha256"):
                    if field in op and field in previous:
                        left, right = op[field], previous[field]
                        if field == "sha256":
                            left, right = left.lower(), right.lower()
                        if left != right:
                            _error("Use source_change before replacing a recorded source version or hash",
                                   code="SOURCE_CHANGE_REQUIRED", key=op["key"], field=field)
                if op["status"] in CLOSED:
                    _current_fingerprint(op, task)
                    closures.append(("evidence", op["key"], op["status"]))
                rec = {k: deepcopy(v) for k, v in op.items() if k not in ("op", "key")}
                for field in ("source_version", "sha256"):
                    if field not in rec and field in previous:
                        rec[field] = previous[field]
                rec.update(actor=actor, at=engine.now())
                _put(changed, "evidence", op["key"], rec, actor, kind)
            elif kind in ("decision", "resolve"):
                collection = ("form_candidates" if kind == "decision" else
                              "reviews" if op["kind"] == "review" else "routes")
                task = _task(report, collection, op["key"])
                _current_fingerprint(op, task)
                rec = {k: op[k] for k in ("fingerprint", "reference", "note")}
                rec.update(actor=actor, at=engine.now())
                if kind == "decision":
                    rec["decision"] = op["decision"]
                    storage = "form_decisions"
                    expected = op["decision"]
                else:
                    rec["status"] = "resolved"
                    storage = "reviews" if op["kind"] == "review" else "route_decisions"
                    expected = "resolved"
                _put(changed, storage, op["key"], rec, actor, kind)
                closures.append((collection, op["key"], expected))
            elif kind == "search_log":
                active = {task["key"] for collection in ("evidence", "form_candidates", "reviews", "routes")
                          for task in report[collection]}
                active.update(q["key"] for q in report["questions"] if q["visibility"] is True)
                active.update(issue["id"] for issue in report["issues"])
                if op["key"] not in active:
                    _error("Search task key is invalid or inactive", code="INACTIVE_TASK", key=op["key"])
                rec = {k: op[k] for k in op if k != "op"}
                rec.update(actor=actor, at=engine.now())
                logs = changed.setdefault("search_log", [])
                if not isinstance(logs, list):
                    _error("Existing case search_log must be an array", code="INVALID_CASE")
                logs.append(rec)
                _audit(changed, kind, op["key"], None, rec, actor)
            elif kind == "source_change":
                _source_change(changed, op, report, actor)
        except AppError as exc:
            if isinstance(getattr(exc, "details", None), dict):
                exc.details["operation_index"] = index
            raise
        except (ValueError, KeyError, StopIteration, TypeError, OverflowError) as exc:
            _error(str(exc) or "Invalid operation", operation_index=index, operation=kind)
    try:
        final = engine.evaluate(changed)
    except (ValueError, KeyError, StopIteration, TypeError) as exc:
        _error(str(exc), code="INVALID_CASE")
    for collection, key, expected in closures:
        current = next((row for row in final[collection] if row["key"] == key), None)
        if current is None or current["status"] != expected:
            _error("A later operation invalidated a closure in this batch; split fact changes and reviews",
                   code="INVALIDATED_CLOSURE", key=key, expected=expected,
                   actual=current["status"] if current else "inactive")
    return changed


def operation_schema():
    """Describe the mutation payload; runtime also enforces active case context."""
    text = {"type": "string", "minLength": 1, "pattern": r"\S"}
    identity = {"type": "string", "pattern": r"^[^/\s](?:[^/]*[^/\s])?$"}
    props = {name: deepcopy(text) for name in ("key", "label", "source", "reference", "note",
                                               "fingerprint", "source_version", "query")}
    props.update(module={"enum": sorted(engine.MOD)}, id=identity,
                 owner_ids={"type": "array", "items": identity, "uniqueItems": True},
                 value={"type": ["string", "number", "boolean", "null"]},
                 complete={"type": "boolean"},
                 checks={"type": "object", "properties": {c: {"type": "boolean"} for c in CHECKS},
                         "additionalProperties": False},
                 sha256={"type": "string", "pattern": "^[0-9a-fA-F]{64}$"},
                 kind={"enum": ["review", "route"]},
                 decision={"enum": ["required", "not_required"]},
                 outcome={"enum": ["found", "not_found", "inaccessible"]})
    variants = []
    for kind, (required, optional) in _SHAPES.items():
        properties = {k: deepcopy(props[k]) for k in (*required, *optional) if k not in ("op", "status")}
        properties["op"] = {"const": kind}
        if "status" in (*required, *optional):
            properties["status"] = {"enum": list(STATUSES) if kind == "evidence" else
                                     ["confirmed", "tentative", "conflict"]}
        variant = {"type": "object", "properties": properties,
                   "required": list(required), "additionalProperties": False}
        if kind == "screen":
            properties["value"] = {"type": ["boolean", "null"]}
        if kind == "entity_update":
            variant["anyOf"] = [{"required": ["label"]}, {"required": ["owner_ids"]}]
        if kind == "evidence":
            variant["allOf"] = [
                {"if": {"properties": {"status": {"enum": sorted(CLOSED)}}},
                 "then": {"required": ["reference", "note", "fingerprint"]}},
                {"if": {"properties": {"status": {"enum": ["verified", "alternative_accepted"]}}},
                 "then": {"required": ["checks"], "properties": {"checks": {
                     "required": list(CHECKS), "properties": {c: {"const": True} for c in CHECKS}}}}},
                {"if": {"properties": {"status": {"const": "located"}}},
                 "then": {"required": ["reference"]}},
                {"if": {"properties": {"status": {"const": "rejected"}}},
                 "then": {"required": ["note"]}},
            ]
        variants.append(variant)
    return {"$schema": "https://json-schema.org/draft/2020-12/schema", "title": "Taxprep operation batch",
            "description": "Atomic sequential operations. Actor is supplied separately. Task keys must be active; "
                           "answers must match catalog types. Closures require the current evaluator fingerprint "
                           "and must remain valid after the entire batch. Changed recorded source hashes or versions "
                           "require source_change before evidence updates; omitted hashes/versions are preserved. "
                           "No operation authorizes external action.",
            "type": "object", "properties": {"operations": {"type": "array", "maxItems": 500,
                                                              "items": {"oneOf": variants}}},
            "required": ["operations"], "additionalProperties": False}
