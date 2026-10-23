# Workflow diagnostics

These commands explain the bundled 2025 intake workflow and recorded case state. They do not validate tax law, retrieve documents, calculate tax, or establish that a human reviewed a source. All records in the examples below are fictional.

## Start with the runnable example

From a source checkout:

```bash
python3 examples/diagnostics_demo.py --output fictional-diagnostics
```

The destination must be new. Omit `--output` to run in a temporary directory that is removed afterward. The script invokes the public CLI through subprocesses, uses only local fictional records, checks each command, and fails if the expected state transitions do not occur.

| Revision | Recorded change | What the diagnostics demonstrate |
| --- | --- | --- |
| 1 | Initialize a fictional case. | Empty organization state. |
| 2 | Apply the fictional bootstrap. | Supported example person and employer records. |
| 3 | Add a fictional digital-asset platform. | The issuer-statement answer remains unknown. |
| 3, dry run | Propose a confirmed issuer-statement answer. | Preview added work without advancing the revision. |
| 4 | Commit that answer. | The issuer-document requirement activates. |
| 5 | Record stipulated verification of a synthetic statement. | A closure uses the current fingerprint and six explicit checks. |
| 6 | Record a corrected synthetic source. | Evidence becomes stale and requires verification again. |

The verification step is part of the synthetic fixture; the script does not inspect any real document. Most intake work remains unanswered, so the case deliberately ends `OPEN`.

The retained directory contains `case.sqlite`, the Mermaid graph, and JSON command results: the unknown fact explanation, dry-run preview, active requirement explanation, stale evidence explanation, historical verification explanation, activation diff, correction diff, and final status. The database retains the complete fictional revision history.

## Query the reference graph

Use `graph` without a database to discover node IDs and edges. Query a single module for a manageable view:

```bash
python3 -m taxprep graph --module DIGITAL
python3 -m taxprep graph --module DIGITAL --format mermaid --output digital-workflow.mmd
```

For a specific relationship, use an exact node ID and a bounded neighborhood:

```bash
python3 -m taxprep graph --node DIGITAL.broker_form --direction both --depth 2
python3 -m taxprep graph --node DIGITAL.broker_form --direction downstream --depth 2 --format mermaid
```

`--depth 0` returns only the selected node. The maximum is 10. `--direction upstream` follows supporting dependencies; `downstream` follows requirements that may activate; `both` explores both. Module and node filters are mutually exclusive. Without a node filter, depth and direction do not truncate the module or full graph.

JSON output preserves exact IDs, node kinds, modules, labels, and directed edges. Mermaid uses generated internal identifiers so catalog text cannot become diagram syntax. Output files contain raw graph data or Mermaid; stdout returns the usual receipt envelope. Mermaid sent directly to stdout is intentionally raw text.

The issuer-statement path includes these different node kinds:

| Catalog node ID | Meaning |
| --- | --- |
| `screen.DIGITAL` | Whether the topic applies. |
| `DIGITAL.broker_form` | Whether an issuer statement is known to exist. |
| `rule.DIGITAL.broker_form` | The condition that activates issuer-document work. |
| `evidence.DIGITAL.DIGITAL.doc_broker_form` | The reference document requirement. |

This is an activation DAG. It is not a complete map of invalidation. For example, the evaluator conservatively includes every scope screen and global household context in fingerprints, while explicit source-change operations invalidate related stored closures.

## Explain an evaluated task

Catalog nodes describe reusable specifications. Case task keys also include a module and a particular entity instance. Obtain those keys from `next`, `plan`, `questions`, or `report`:

```bash
python3 -m taxprep --db fictional-diagnostics/case.sqlite explain DIGITAL/platform/DIGITAL.broker_form
python3 -m taxprep --db fictional-diagnostics/case.sqlite explain DIGITAL/platform/evidence/DIGITAL.doc_broker_form
```

The result includes the evaluated item, applicable activation rules, predicate results, upstream facts, and available current and stored fingerprints. A null predicate result means unknown. The explanation preserves conflict, unanswered, upstream-blocked, and inactive states instead of treating them as false.

An explanation can inspect a saved revision:

```bash
python3 -m taxprep --db fictional-diagnostics/case.sqlite explain DIGITAL/platform/evidence/DIGITAL.doc_broker_form --revision 5
```

That result describes revision 5, before the synthetic source correction. A historical fingerprint cannot close work in the current case. A key must exist in the selected evaluation; an old stored record that is no longer active is not proof of a current requirement or a completed review.

Fingerprint equality reports matching recorded fact context. It does not prove source authenticity, professional review, or the precise cause of a change. Use revision comparisons and source references to inspect the supporting record.

## Compare revisions and preview a batch

Compare the case before and after the statement answer, then inspect what the source correction reopened:

```bash
python3 -m taxprep --db fictional-diagnostics/case.sqlite diff --from 3 --to 4
python3 -m taxprep --db fictional-diagnostics/case.sqlite diff --from 5
```

Omitting `--to` selects the current committed revision. The result identifies both revision numbers; the envelope revision is the destination. Read it in three parts:

| Field | Interpretation |
| --- | --- |
| `records` | Changes to facts, entity inventories, roster confirmations, source records, and closures. Absent and explicit null values remain distinct. Audit entries and timestamp-only changes are omitted. |
| `tasks` | Added, removed, changed, and reopened evaluated work. Reopened tasks are a subset of changed tasks. |
| `readiness`, `summary`, `counts` | Before/after readiness, evaluated count deltas, and totals for the listed changes. |

A task can disappear because its parent condition becomes inactive. Such a removal is not a successful verification, a resolved issue, or a legal conclusion. Conversely, adding a task records a newly active modeled requirement; it does not determine whether the underlying tax position is correct.

The same comparison appears under `data.impact` when validating a new batch:

```bash
python3 -m taxprep --db case.sqlite apply --input proposed.json --expect 6 --request-id supported-change-1 --actor intake-agent --dry-run
```

The preview uses the current committed case and the validated proposal within the mutation operation. It does not advance the revision or reserve the request ID. Review its changed records, removed requirements, and reopened closures, then commit the identical supported batch using the same observed revision and unused request ID.

If that request ID already committed with the same actor and parsed payload, the CLI replays its original result. A replay has `replayed: true` and omits `impact`; it is not a fresh preview against the latest state. Read `status` or `next` again before preparing more work.

The machine-facing details are in [CLI_CONTRACT.md](CLI_CONTRACT.md). The operating rules in [AGENTS.md](../AGENTS.md) continue to apply to every diagnostic result and mutation.
