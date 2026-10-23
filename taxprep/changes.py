"""Read-only comparisons of saved or proposed case revisions.

Record changes explain what was entered; evaluated task changes explain what the
current engine requires. These are separate views: a disappearing requirement is
not proof that work was completed, and a source correction can reopen work even
when no recorded answer changes.
"""
from __future__ import annotations

import copy

from . import engine as E
from .errors import AppError


_TIMESTAMPS = {"at", "created_at", "updated_at", "invalidated_at"}
_COLLECTIONS = ("screens", "enumerated", "entities", "answers", "evidence",
                "form_decisions", "reviews", "route_decisions", "search_log")
_CLOSED = {
    "confirm_fact": {"answered"},
    "evidence": {"verified", "alternative_accepted", "not_required"},
    "form_applicability": {"required", "not_required"},
    "technical_review": {"resolved"},
    "cross_topic_route": {"resolved"},
    "scope_or_inventory": set(),
}


def _record(value):
    """Remove record metadata timestamps without rewriting user-supplied values."""
    if not isinstance(value, dict):
        return copy.deepcopy(value)
    return {key: copy.deepcopy(item) for key, item in value.items()
            if key not in _TIMESTAMPS}


def _records(case):
    result = {name: {} for name in _COLLECTIONS}
    for name in ("screens", "enumerated", "evidence", "form_decisions",
                 "reviews", "route_decisions"):
        result[name] = {key: _record(value) for key, value in case[name].items()}
    for module, entities in case["entities"].items():
        for entity in entities:
            prefix = module + "/" + entity["id"]
            result["entities"][prefix] = _record({key: value for key, value in entity.items()
                                                   if key != "answers"})
            for question, value in entity["answers"].items():
                result["answers"][prefix + "/" + question] = _record(value)
    # Search records are append-only through the mutation interface. Position
    # preserves duplicate searches instead of collapsing equal-looking entries.
    for position, value in enumerate(case.get("search_log", [])):
        result["search_log"][str(position)] = _record(value)
    return result


def _record_changes(before, after):
    changes = []
    for key in sorted(before.keys() | after.keys()):
        present_before, present_after = key in before, key in after
        if present_before and present_after and before[key] == after[key]:
            continue
        changes.append({
            "key": key,
            "change": "added" if not present_before else ("removed" if not present_after else "changed"),
            "before": {"present": present_before, "value": before.get(key)},
            "after": {"present": present_after, "value": after.get(key)},
        })
    return changes


def _tasks(report):
    result = {}
    for section, kind in (("questions", "confirm_fact"), ("evidence", "evidence"),
                          ("form_candidates", "form_applicability"),
                          ("reviews", "technical_review"), ("routes", "cross_topic_route"),
                          ("issues", "scope_or_inventory")):
        for item in report[section]:
            key = item.get("key", item.get("id"))
            state = {"state": item.get("state", item.get("status", "open"))}
            if section == "questions":
                state["visibility"] = item["visibility"]
            result[key] = {"kind": kind, "state": state}
    return result


def _task_changes(before, after):
    changes = {name: [] for name in ("added", "removed", "changed", "reopened")}
    for key in sorted(before.keys() | after.keys()):
        previous, current = before.get(key), after.get(key)
        if previous == current:
            continue
        row = {"key": key, "kind": (current or previous)["kind"],
               "before": copy.deepcopy(previous["state"]) if previous else None,
               "after": copy.deepcopy(current["state"]) if current else None}
        group = "added" if previous is None else ("removed" if current is None else "changed")
        changes[group].append(row)
        if previous and current:
            closed = _CLOSED[row["kind"]]
            if previous["state"]["state"] in closed and current["state"]["state"] not in closed:
                # An answered fact becoming inapplicable is deactivation, not
                # reopened fact work. It remains visible in the changed list.
                if row["kind"] != "confirm_fact" or current["state"]["visibility"] is not False:
                    changes["reopened"].append(copy.deepcopy(row))
    return changes


def compare_cases(before: dict, after: dict) -> dict:
    """Compare two valid snapshots without mutating them or interpreting tax law.

    Direction is explicit: callers may compare an older case to a newer one or
    reverse that order. The returned before/after values follow that direction.
    Full case records can contain sensitive data; callers choose where to send
    this output just as they do for ``report`` and ``export``.
    """
    first, second = E.evaluate(before), E.evaluate(after)
    if before["case_id"] != after["case_id"]:
        raise AppError("case_mismatch", "Only revisions of the same case can be compared.")
    before_records, after_records = _records(before), _records(after)
    records = {name: _record_changes(before_records[name], after_records[name])
               for name in _COLLECTIONS}
    tasks = _task_changes(_tasks(first), _tasks(second))
    return {
        "case_id": before["case_id"],
        "readiness": {"before": first["readiness"], "after": second["readiness"]},
        "summary": {key: {"before": first["summary"][key], "after": second["summary"][key],
                          "delta": second["summary"][key] - first["summary"][key]}
                    for key in sorted(first["summary"])},
        "records": records,
        "tasks": tasks,
        "counts": {"record_changes": sum(len(items) for items in records.values()),
                   **{"tasks_" + name: len(items) for name, items in tasks.items()}},
        "caveats": [
            "Removed or deactivated tasks are not evidence of completed work.",
            "Reopened tasks are a subset of changed tasks that were closed and now require work.",
            "Audit entries and timestamp-only record changes are omitted; source and review changes are retained.",
            "This comparison uses the bundled evaluator, not independent tax advice or a complete causal explanation.",
        ],
    }


def compare_snapshots(before: dict, after: dict) -> dict:
    """Compare Store snapshots and attach the exact requested revisions."""
    return {"from_revision": before["revision"], "to_revision": after["revision"],
            **compare_cases(before["case"], after["case"])}
