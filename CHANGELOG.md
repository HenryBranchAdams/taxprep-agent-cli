# Changelog

## 0.2.0 — Workflow diagnostics

- Query the reference activation DAG with `graph`, including bounded node neighborhoods, module views, JSON, and Mermaid exports.
- Explain evaluated questions, evidence, decisions, reviews, routes, and inventory issues with `explain`; inspect saved snapshots with `--revision`.
- Compare saved revisions with `diff`, separating record changes from activated, removed, changed, and reopened work.
- Review proposed changes in `apply --dry-run` under `data.impact`. Idempotent replays retain their earlier result and omit a fresh preview.
- Add a runnable fictional example and CI checks for Python 3.10, 3.12, and 3.13.

The protocol remains 1.0. Existing case databases, operation payloads, catalog bytes, and maximum readiness are unchanged. Graph arrows describe activation and do not enumerate all conservative invalidation dependencies. Diagnostics organize preparation work; they do not calculate tax, validate tax law, or authorize filing or external actions.

## 0.1.1

- Add an explicit evidence requirement for an issued digital-asset tax statement.

## 0.1.0

- Package the source workflow as a noninteractive Python CLI with strict JSON operations, transactional SQLite snapshots, idempotent requests, and preparer handoff exports.
