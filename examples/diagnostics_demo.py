"""Exercise workflow diagnostics with fictional records and no external access.

Run from a source checkout with Python 3.10+. Use --output NEW_DIRECTORY to
retain the sample database and command results; otherwise temporary files are
removed after the run. No example record represents the user's tax facts.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
ACTOR = "fictional-diagnostics-agent"
FACT_KEY = "DIGITAL/platform/DIGITAL.broker_form"
EVIDENCE_KEY = "DIGITAL/platform/evidence/DIGITAL.doc_broker_form"
PROVENANCE = {
    "source": "fictional demonstration",
    "reference": "fixture://diagnostics/issuer-statement",
}


def run_demo(directory: Path) -> dict:
    """Run public CLI commands; fail if any command or expected state fails."""
    db = directory / "case.sqlite"

    def command(name, *arguments, payload=None, save=None):
        process = subprocess.run(
            [sys.executable, "-m", "taxprep", "--db", str(db), name, *arguments],
            cwd=ROOT, input=None if payload is None else json.dumps(payload),
            capture_output=True, text=True, timeout=30,
        )
        if process.returncode != 0:
            raise RuntimeError(f"{name} failed ({process.returncode}): {process.stderr.strip()}")
        result = json.loads(process.stdout)
        if not result.get("ok"):
            raise RuntimeError(f"{name} did not return a success envelope")
        if save:
            with (directory / save).open("x", encoding="utf-8") as stream:
                stream.write(process.stdout)
        return result

    def apply(operations, revision, request_id, dry_run=False, save=None):
        arguments = ["--input", "-", "--expect", str(revision),
                     "--request-id", request_id, "--actor", ACTOR]
        if dry_run:
            arguments.append("--dry-run")
        return command("apply", *arguments, payload={"operations": operations}, save=save)

    command("init", "--case-id", "fictional-diagnostics-2025", "--actor", ACTOR)
    bootstrap = json.loads((ROOT / "examples/bootstrap.json").read_text(encoding="utf-8"))
    apply(bootstrap["operations"], 1, "fictional-bootstrap")
    apply([
        {"op": "screen", "module": "DIGITAL", "value": True, **PROVENANCE},
        {"op": "entity_add", "module": "DIGITAL", "id": "platform",
         "label": "Fictional digital-asset platform", "owner_ids": ["taxpayer"]},
        {"op": "enumerate", "module": "DIGITAL", "complete": True, **PROVENANCE},
    ], 2, "fictional-platform")
    command("graph", "--node", "DIGITAL.broker_form", "--direction", "both",
            "--depth", "2", save="graph.json")
    command("graph", "--node", "DIGITAL.broker_form", "--direction", "both",
            "--depth", "2", "--format", "mermaid", "--output", str(directory / "workflow.mmd"))
    command("explain", FACT_KEY, save="unknown-fact.json")

    observed = [{"op": "answer", "key": FACT_KEY, "value": True, **PROVENANCE}]
    preview = apply(observed, 3, "fictional-statement-observed", dry_run=True, save="preview.json")
    if preview["revision"] != 3 or "impact" not in preview["data"]:
        raise RuntimeError("Dry run did not return an impact at the unchanged revision")
    if command("status")["revision"] != 3:
        raise RuntimeError("Dry run unexpectedly changed the database revision")
    apply(observed, 3, "fictional-statement-observed")
    command("explain", EVIDENCE_KEY, save="required-evidence.json")
    current = command("inspect", EVIDENCE_KEY)["data"]
    apply([{
        "op": "evidence", "key": EVIDENCE_KEY, "status": "verified",
        "reference": "fixture://diagnostics/issuer-statement/v1",
        "note": "All six checks are stipulated by this synthetic fixture; no real document was reviewed.",
        "checks": {key: True for key in ["year", "owner", "entity", "complete", "corrections", "reconciled"]},
        "fingerprint": current["fingerprint"], "source_version": "fictional-v1",
    }], 4, "fictional-verification")
    apply([{
        "op": "source_change", "key": EVIDENCE_KEY,
        "reference": "fixture://diagnostics/issuer-statement/v2",
        "note": "The synthetic corrected statement replaces v1 and needs fresh verification.",
        "source_version": "fictional-v2",
    }], 5, "fictional-source-correction")
    command("explain", EVIDENCE_KEY, save="stale-evidence.json")
    command("explain", EVIDENCE_KEY, "--revision", "5", save="historical-verification.json")
    command("diff", "--from", "3", "--to", "4", save="activation-diff.json")
    command("diff", "--from", "5", save="correction-diff.json")
    final = command("status", save="status.json")
    if command("inspect", EVIDENCE_KEY)["data"]["status"] != "stale":
        raise RuntimeError("Corrected evidence was not reopened for verification")
    if final["revision"] != 6 or final["data"]["readiness"] != "OPEN":
        raise RuntimeError("The intentionally incomplete fictional case must remain OPEN at revision 6")
    return {
        "fictional": True, "case_id": final["data"]["case_id"],
        "revision": final["revision"], "readiness": final["data"]["readiness"],
        "demonstrated": ["bounded graph", "unknown fact", "dry-run impact", "activated evidence",
                         "source correction", "historical explanation", "revision diff"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="New directory for the fictional database and results")
    args = parser.parse_args()
    try:
        if args.output:
            directory = args.output.expanduser().absolute()
            directory.mkdir(parents=True, exist_ok=False)
            result = run_demo(directory)
            result["directory"] = str(directory)
        else:
            with tempfile.TemporaryDirectory(prefix="taxprep-fictional-demo-") as temporary:
                result = run_demo(Path(temporary))
            result["files_retained"] = False
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, RuntimeError, ValueError, subprocess.TimeoutExpired) as exc:
        print(f"Fictional diagnostics demo failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
