"""Read-only catalog topology and explanations from the existing case evaluator.

The graph describes activation, not every dependency used for invalidation.
No answer, evidence record, or review is changed by these functions.
"""
from __future__ import annotations

from collections import defaultdict, deque
from copy import deepcopy

from . import engine as E
from .errors import AppError


GRAPH_SCOPE = (
    "Illustrative activation dependencies from the bundled 2025 catalog. "
    "Edges do not describe every invalidation dependency or establish tax applicability. "
    "Global scope and household facts can invalidate closures beyond this graph."
)
EXPLAIN_SCOPE = (
    "Explanation of the current evaluator state, not tax advice or authority to act. "
    "Unknown, tentative, and conflicting facts remain unknown. Fingerprints include "
    "all topic screens, CORE/PERSON/STATUS/STATE context, and the local instance; "
    "explicit source changes can also invalidate prior closures. A fingerprint "
    "mismatch alone does not identify which earlier fact or source changed."
)


def _catalog_nodes():
    nodes = {}

    def add(nid, kind, module, label):
        nodes[nid] = {"id": nid, "kind": kind, "module": module, "label": label}

    for m in E.CAT["modules"]:
        add("screen." + m["id"], "screen", m["id"], m["title"])
    for q in E.CAT["questions"]:
        add(q["id"], "question", q["module"], q["prompt"])
    for r in E.CAT["rules"]:
        add("rule." + r["id"], "rule", r["module"], r["title"])
        for did in r["documents"]:
            add("evidence." + r["module"] + "." + did, "evidence", r["module"],
                E.CAT["documents"][did]["title"])
        for form in r["forms"]:
            add("form." + r["module"] + "." + form["id"], "form", r["module"],
                form["id"])
    for route in E.CAT["routes"]:
        add("task." + route["id"], "route", route["module"], route["instruction"])
    return nodes


def catalog_graph(module=None, node=None, direction="both", depth=2):
    """Return an induced module graph or a bounded node neighborhood.

    Depth counts traversed edges. Direction affects traversal from the selected
    node; all edges between selected nodes are then preserved in their original
    direction. Full-catalog and module queries do not use the depth parameter.
    """
    if module is not None and node is not None:
        raise AppError("invalid_arguments", "Choose either a module or a node neighborhood.")
    if module is not None and module not in E.MOD:
        raise AppError("invalid_arguments", "Unknown graph module.")
    if direction not in ("upstream", "downstream", "both"):
        raise AppError("invalid_arguments", "Graph direction must be upstream, downstream, or both.")
    if type(depth) is not int or not 0 <= depth <= 10:
        raise AppError("invalid_arguments", "Graph depth must be an integer from 0 to 10.")
    graph = E.validate_catalog()
    nodes = _catalog_nodes()
    edges = graph["graph_edges"]
    selected = set(nodes)
    if module is not None:
        selected = {nid for nid, row in nodes.items() if row["module"] == module}
    elif node is not None:
        if node not in nodes:
            raise AppError("not_found", "No catalog graph node matches that exact ID.", 4,
                           details={"node": node})
        adjacency = defaultdict(set)
        for source, target in edges:
            if direction in ("downstream", "both"):
                adjacency[source].add(target)
            if direction in ("upstream", "both"):
                adjacency[target].add(source)
        selected = {node}
        pending = deque([(node, 0)])
        while pending:
            current, distance = pending.popleft()
            if distance >= depth:
                continue
            for neighbor in sorted(adjacency[current] - selected):
                selected.add(neighbor)
                pending.append((neighbor, distance + 1))
    chosen_edges = [{"source": a, "target": b} for a, b in edges
                    if a in selected and b in selected]
    return {"nodes": [nodes[nid] for nid in sorted(selected)], "edges": chosen_edges,
            "node_count": len(selected), "edge_count": len(chosen_edges),
            "catalog_counts": {"nodes": graph["nodes"], "edges": graph["edges"]},
            "filters": {"module": module, "node": node, "direction": direction,
                        "depth": depth if node is not None else None},
            "scope": GRAPH_SCOPE}


def _mermaid_label(text):
    # Numerical entities preserve text inside Mermaid's quoted labels. Encode
    # delimiters before adding entities; no HTML labels or executable directives.
    text = " ".join(str(text).split())
    entities = {"#": "#35;", '"': "#34;", "&": "#38;", "<": "#60;",
                ">": "#62;", "\\": "#92;", "`": "#96;"}
    return "".join(entities.get(char, char) for char in text)


def render_mermaid(graph):
    """Render stable generated identifiers; catalog text appears only in labels."""
    nodes = sorted(graph["nodes"], key=lambda row: row["id"])
    identifiers = {row["id"]: "n" + str(index) for index, row in enumerate(nodes)}
    lines = ["flowchart TD"]
    for row in nodes:
        label = row["id"] + ": " + row["label"]
        lines.append('    ' + identifiers[row["id"]] + '["' + _mermaid_label(label) + '"]')
    for edge in sorted(graph["edges"], key=lambda edge: (edge["source"], edge["target"])):
        lines.append("    " + identifiers[edge["source"]] + " --> " + identifiers[edge["target"]])
    return "\n".join(lines) + "\n"


def _fact(case, module, entity_id, ref):
    normalized = ref.removeprefix("$")
    if normalized.startswith("screen."):
        mid = normalized.split(".", 1)[1]
        value = E.module_status(case, mid)
        return {"id": normalized, "key": "screen/" + mid, "module": mid,
                "state": "mandatory" if E.MOD[mid]["screen"] is None else
                         ("unknown" if value is None else "confirmed"),
                "visibility": True, "value": value, "record": case["screens"].get(mid)}
    q = E.QUESTIONS[normalized]
    mid = q["module"]
    instance = E.entity(case, mid, entity_id) if mid == module else case["entities"][mid][0]
    row = E.inspect_instance(case, mid, instance)["questions_by_id"][normalized]
    return {"id": normalized, "key": mid + "/" + instance["id"] + "/" + normalized,
            "module": mid, "state": row["state"], "visibility": row["visibility"],
            "value": row["value"], "record": row["record"]}


def _prerequisites(case, module, entity_id, conditions):
    seeds = {"screen." + module}
    for condition in conditions:
        seeds.update(ref.removeprefix("$") for ref in E.refs(condition))
    pending = deque((ref, 1) for ref in sorted(seeds))
    seen = set()
    rows = []
    while pending:
        ref, depth = pending.popleft()
        if ref in seen:
            continue
        seen.add(ref)
        rows.append({**_fact(case, module, entity_id, ref), "depth": depth})
        if ref in E.QUESTIONS:
            for upstream in sorted(E.refs(E.QUESTIONS[ref]["when"])):
                pending.append((upstream.removeprefix("$"), depth + 1))
    return sorted(rows, key=lambda row: (row["depth"], row["key"]))


def _reason(section, item):
    state = item.get("state", item.get("status", "open"))
    if section == "issues":
        return item["message"]
    if section == "questions":
        return {"blocked_by_upstream": "The opening condition depends on unknown upstream facts.",
                "not_applicable": "The opening condition is false; this question is inactive.",
                "answered": "A confirmed, known answer satisfies this visible question.",
                "conflict": "The stored answer is conflicting and remains open.",
                "unanswered": "No confirmed, known answer satisfies this visible question."
                }[state]
    if state == "stale":
        return "The stored closure does not satisfy the current context or source version; review it again."
    if state in ("verified", "alternative_accepted", "not_required", "required", "resolved"):
        return "The stored record satisfies this requirement in the current evaluated context."
    if state == "located":
        return "A source is located, but the required verification has not been completed."
    return "An activated requirement remains open; inspect its record and supporting facts."


def explain(case, key):
    """Explain one exact currently evaluated key, including inactive questions.

    Entire inactive modules are absent from the evaluated case, as they are from
    ``inspect``. Historical explanations are obtained by supplying that snapshot.
    """
    report = E.evaluate(case)
    section = None
    item = None
    for collection in ("questions", "evidence", "form_candidates", "reviews", "routes", "issues"):
        item = next((row for row in report[collection]
                     if row.get("key", row.get("id")) == key), None)
        if item is not None:
            section = collection
            break
    if item is None:
        raise AppError("not_found", "No current task or question matches that exact key.", 4,
                       details={"key": key})
    result = {"key": key, "section": section, "item": deepcopy(item),
              "reason": _reason(section, item), "scope": EXPLAIN_SCOPE,
              "rules": [], "prerequisites": [], "current_fingerprint": item.get("fingerprint"),
              "stored_fingerprint": (item.get("record") or {}).get("fingerprint"),
              "fingerprint_matches": None, "module_status": None}
    module, entity_id = item.get("module"), item.get("entity_id")
    if section == "issues":
        parts = key.split("/")
        module = parts[1] if parts[0] in ("screen", "roster", "enumerate") else parts[0]
        if module in E.MOD:
            result["module_status"] = E.module_status(case, module)
            result["inventory"] = {"module": module,
                                   "entities": [{k: deepcopy(x[k]) for k in ("id", "label", "owner_ids")}
                                                for x in case["entities"][module]],
                                   "enumeration": deepcopy(case["enumerated"].get(module))}
        return result
    result["module_status"] = E.module_status(case, module)
    context = E.inspect_instance(case, module, E.entity(case, module, entity_id))
    conditions = []
    if section == "questions":
        condition = E.QUESTIONS[item["id"]]["when"]
        result["activation"] = {"condition": deepcopy(condition), "result": item["visibility"]}
        conditions.append(condition)
    elif section == "routes":
        route = next(route for route in E.CAT["routes"]
                     if module + "/" + entity_id + "/" + route["id"] == key)
        result["activation"] = {"condition": deepcopy(route["when"]), "result": context["eval"](route["when"])}
        conditions.append(route["when"])
    else:
        for rule in E.CAT["rules"]:
            if rule["module"] != module:
                continue
            relevant = ((section == "evidence" and item["document_id"] in rule["documents"]) or
                        (section == "form_candidates" and
                         any(form["id"] == item["id"] for form in rule["forms"])) or
                        (section == "reviews" and item["rule"] == rule["id"]))
            if relevant:
                conditions.append(rule["when"])
                result["rules"].append({"id": rule["id"], "title": rule["title"],
                                        "condition": deepcopy(rule["when"]),
                                        "result": context["eval"](rule["when"]),
                                        "facts": sorted(E.refs(rule["when"]))})
    result["prerequisites"] = deepcopy(_prerequisites(case, module, entity_id, conditions))
    if result["current_fingerprint"] is not None and result["stored_fingerprint"] is not None:
        result["fingerprint_matches"] = result["current_fingerprint"] == result["stored_fingerprint"]
    return result
