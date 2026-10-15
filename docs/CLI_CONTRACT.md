# CLI contract, version 1.0

Invocation: `taxprep [--db PATH] COMMAND [OPTIONS]`. The equivalent standalone invocation is `python3 taxprep.pyz`; source execution is `python3 -m taxprep`. Python 3.10+ is required. `--db` defaults to `taxprep.sqlite` and must appear before the subcommand. Arguments are never abbreviated and the CLI never prompts.

## Commands

| Command | Required or useful options | Result |
| --- | --- | --- |
| `doctor` | None | Runtime version, catalog counts, and graph validation; no database required. |
| `init` | `--case-id ID --actor LABEL`; `--year 2025` | Creates a new database at revision 1. Refuses an existing path. |
| `import-case` | `--input FILE --actor LABEL` | Validates workbench case JSON and creates a new database at revision 1. Use `--input -` for stdin. |
| `status` | None | Case ID, year, readiness, counts, and revision. |
| `next` | `--limit N` (default 10), `--kind KIND`, `--module ID` | Bounded prioritized tasks, filters, and upstream dependencies. |
| `plan` | None | Full open task queue, search suggestions, and acceptance criteria. |
| `questions` | `--module ID`, `--include-inactive` | Questions, answer state, and catalog specifications. Defaults to currently visible questions. |
| `inspect` | Exact task/question key as positional argument | Current evaluated item and relevant question or document specification. |
| `report` | None | Full evaluated case, including evidence, forms, reviews, routes, and issues. |
| `check` | None | Same summary as `status`; exits 5 while readiness is `OPEN`. |
| `apply` | `--input FILE --expect N --request-id ID --actor LABEL`; `--dry-run` | Atomic operation batch. Use `--input -` for stdin. |
| `export` | `--output FILE`; optional `--revision N` | Exports current or selected earlier case JSON without replacing an existing file. `--output -` emits raw case JSON. |
| `handoff` | `--output NEW_DIRECTORY` | Writes `case.json`, `report.json`, `agent-plan.json`, `open-items.md`, and `manifest.json`. |
| `history` | `--limit N` (default 100) | Newest-first snapshot metadata, actor labels, request IDs, and checksums. |
| `catalog` | `--kind KIND`, `--id ID`, `--module ID`, `--query TEXT` | Searches the complete bundled reference catalog; no database required. |
| `schema` | `--target operations` (default) or `--target protocol` | Mutation JSON Schema or protocol description; no database required. |

`--help` prints text help. `--version` returns the normal JSON envelope. Catalog kinds are `modules`, `questions`, `rules`, `documents`, `sources`, and `routes`. Task kinds are `scope_or_inventory`, `confirm_fact`, `evidence`, `form_applicability`, `technical_review`, and `cross_topic_route`. Inspect exact task/question keys returned by the current evaluation; do not derive keys from display labels.

## Streams and exit codes

Successful commands emit a single JSON object to stdout:

```json
{
  "ok": true,
  "protocol_version": "1.0",
  "command": "status",
  "revision": 2,
  "data": {}
}
```

The revision is null for commands without a single evaluated snapshot, such as `schema` and `history`. Errors emit a single JSON object to stderr and no success object:

```json
{
  "ok": false,
  "protocol_version": "1.0",
  "error": {
    "code": "revision_conflict",
    "message": "Case changed since it was read. Read the current revision before preparing another mutation.",
    "details": {"expected_revision": 1, "actual_revision": 2}
  }
}
```

`details` is optional. Consume `error.code` rather than matching message wording. Help is plain text. `export --output -` intentionally emits raw case JSON instead of an envelope.

| Exit | Meaning |
| --- | --- |
| 0 | Command succeeded. `status` and other reads can succeed while readiness is `OPEN`. |
| 2 | Invalid arguments, JSON, case data, or operation. |
| 3 | Revision, idempotency, catalog, or existing-path conflict. |
| 4 | Missing resource or I/O failure; inspect error details for a retryable database lock. |
| 5 | `check` succeeded but found `OPEN` readiness. Its result is an `ok: true` object on stdout. |
| 70 | Unexpected internal failure. |

## Mutation payload

The input is one object with exactly one field, `operations`, containing at most 500 operation objects. Unknown fields, duplicate JSON keys, nonfinite numbers, invalid values, and inactive task keys are rejected. JSON Schema describes structural requirements; runtime evaluation additionally enforces visibility, types, ownership, and current task context.

```json
{
  "operations": [
    {
      "op": "answer",
      "key": "CORE/return/CORE.year",
      "value": 2025,
      "source": "fixture",
      "reference": "Illustrative intake; replace with actual supported provenance"
    }
  ]
}
```

The actor is supplied once on the command line, not in operations. Text fields must be nonblank. IDs cannot contain `/` or surrounding whitespace. Answers use scalar JSON values or null and must match the catalog's question type and allowed choices.

| Operation | Required fields beyond `op` | Optional fields and conditions |
| --- | --- | --- |
| `answer` | `key`, `value`, `source`, `reference` | `status`: `confirmed` (default), `tentative`, or `conflict`. Question must currently be visible. |
| `screen` | `module`, `value`, `source`, `reference` | Same answer statuses. Value is true, false, or null. Mandatory modules have no screen. |
| `entity_add` | `module`, `id`, `label` | `owner_ids`. Module must be active and repeatable; IDs must be unique within it. Owners must be existing PERSON IDs. PERSON entities cannot have owners. |
| `entity_update` | `module`, `id` | At least one of `label` or `owner_ids`. Module must be active. |
| `enumerate` | `module`, `complete`, `source`, `reference` | `complete` is boolean. An active empty roster cannot be declared complete. Adding an entity invalidates its roster confirmation. |
| `evidence` | `key`, `status` | `reference`, `note`, `checks`, `fingerprint`, `source_version`, `sha256`, according to status below. |
| `decision` | `key`, `decision`, `reference`, `note`, `fingerprint` | Decision is `required` or `not_required` for a current form candidate. |
| `resolve` | `kind`, `key`, `reference`, `note`, `fingerprint` | Kind is `review` or `route`. |
| `search_log` | `key`, `source`, `query`, `outcome`, `reference` | `note`. Outcome is `found`, `not_found`, or `inaccessible`; key must identify current work. |
| `source_change` | `key`, `reference`, `note` | `source_version`, `sha256`. Key must identify a current evidence task. |

Evidence statuses are `missing`, `searching`, `located`, `verified`, `rejected`, `alternative_accepted`, `not_required`, and `stale`.

- `located` requires a reference; `rejected` requires a note.
- `verified`, `alternative_accepted`, and `not_required` require a reference, note, and the exact current fingerprint.
- `verified` and `alternative_accepted` additionally require `checks` with `year`, `owner`, `entity`, `complete`, `corrections`, and `reconciled` all true.
- Optional `sha256` must be 64 hexadecimal characters. It records the supplied digest; the CLI does not read or verify the referenced source file itself.

`source_change` marks the evidence stale and invalidates stored form decisions, technical reviews, and routes for the same instance. A source change in CORE, PERSON, STATUS, or STATE invalidates those stored decisions across the case. It does not discover source changes or mark other evidence files automatically; register every affected evidence task explicitly.

## Transactions, revisions, and retries

Operations execute sequentially against a working case, so an earlier screen or answer can activate a later operation. All operations must be valid, and all closures made in a batch must still be valid at its end. Otherwise the entire batch rolls back. A later change that invalidates an earlier closure is rejected as `INVALIDATED_CLOSURE`; split fact changes and review closures into separate batches.

`--expect` must match the current committed revision. A successful new batch adds one full snapshot and advances the revision by one. `--dry-run` evaluates the proposed case but commits nothing; its returned summary describes the proposal while its revision remains the current committed revision. A dry run does not reserve its request ID.

For a retry, supply the same request ID, actor, and parsed JSON payload. The CLI matches canonicalized JSON, so object-key order and whitespace do not change identity. A matching committed request returns its original snapshot with `replayed: true` before checking the expected revision. Reusing that ID for different content or actor produces `request_conflict`. Replayed results can be older than the latest case; re-read before further work. A dry run using an already committed request ID also replays that committed result.

The database pins the exact bundled catalog bytes. Snapshot checksums detect mismatched stored JSON; neither checksums nor caller-supplied actor labels provide authentication or tamper-proof storage. On POSIX, database files and existing sidecars receive owner-only permissions. Database contents and exported files are unencrypted.

## Fingerprints and handoff

Task fingerprints capture the evaluator's relevant fact context. Copy them from the current evaluated task for every closure; do not calculate, alter, or reuse them across instances. Fact changes can make earlier decisions stale. The underlying fingerprint is content-based, so restoring the same facts can revive earlier decisions unless a source change explicitly invalidated them. Source bytes are not part of the automatic fingerprint; record `source_change` when a document changes without a fact change.

The handoff manifest includes the revision, case ID, creation time, and SHA-256/byte counts for its four content files. It is an organization snapshot, not an export of SQLite revision history. Preserve the database for complete snapshot/request history. Export and handoff refuse existing destinations.

The highest readiness is `READY_FOR_PREPARER_REVIEW`: the modeled organization gates are satisfied. The reference catalog covers 2025 U.S. federal individual intake. This protocol does not compute tax, validate all legal obligations, submit returns, make payments, or authorize external actions.
