#!/usr/bin/env python3
"""Run the public hybrid SDD fixture matrix with isolated telemetry paths."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

FEATURE = Path(__file__).resolve().parent
ROOT = FEATURE.parents[2]
CHECKER = ROOT / "scripts" / "hybrid-sdd-check.py"
TRACE = ROOT / "scripts" / "efficiency-trace.py"
ROUTES = FEATURE / "routes"
EVIDENCE = FEATURE / "evidence"
TELEMETRY = FEATURE / "telemetry"
PRESET = ROOT / ".specify" / "presets" / "creative-llm-wiki"


def run(command: list[str], *, expect: int = 0) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != expect:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"unexpected exit {result.returncode} for {' '.join(command)}: {detail}")
    return result


def fixture_records(path: Path) -> list[dict[str, object]]:
    value = json.loads(path.read_text())
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        return value.get("records", [value])
    raise RuntimeError(f"invalid fixture container {path}")


def check_hybrid() -> None:
    run([sys.executable, str(CHECKER), "classify", "--fixtures", str(ROUTES)])
    for path in (EVIDENCE / "agency.json", EVIDENCE / "reusable-system.json", EVIDENCE / "agency-failures.json"):
        run([sys.executable, str(CHECKER), "agency", "--fixtures", str(path)])
    for path in (EVIDENCE / "ownership.json", EVIDENCE / "canon-boundary.json", EVIDENCE / "maintenance-boundary.json"):
        run([sys.executable, str(CHECKER), "canon", "--fixtures", str(path)])
    for path in (EVIDENCE / "topology.json", EVIDENCE / "parallel-ownership.json"):
        run([sys.executable, str(CHECKER), "topology", "--fixtures", str(path)])
    run([sys.executable, str(CHECKER), "plan", "--fixtures", str(EVIDENCE / "engineering-plan.json")])
    run([sys.executable, str(CHECKER), "verify", "--fixtures", str(EVIDENCE / "verification.json")])
    run([sys.executable, str(CHECKER), "preset", "--package", str(PRESET)])


def check_telemetry() -> None:
    with tempfile.TemporaryDirectory(prefix="hybrid-sdd-traces-") as directory:
        temp = Path(directory)
        trace = temp / "traces.jsonl"
        quarantine = temp / "quarantine.jsonl"
        def record(record: dict[str, object], expected: int = 0) -> None:
            source = temp / f"{record.get('trace_id', 'record')}.json"
            source.write_text(json.dumps(record))
            run([sys.executable, str(TRACE), "record", "--input", str(source), "--trace", str(trace), "--quarantine", str(quarantine)], expect=expected)
        record(fixture_records(TELEMETRY / "complete.json")[0])
        for record_data in fixture_records(TELEMETRY / "edge-cases.json"):
            record(record_data)
        for record_data in fixture_records(TELEMETRY / "schema-evolution.json"):
            record(record_data, expected=1 if record_data.get("expected_error") else 0)
        report = run([sys.executable, str(TRACE), "report", "--trace", str(trace)])
        report_data = json.loads(report.stdout)
        if "accepted_work_denominator" not in report_data or "trajectory_tokens" not in report_data:
            raise RuntimeError("telemetry report omitted required metric vector")
        for name in ("trajectory_tokens", "input_tokens", "output_tokens", "retry_amplification", "hard_gate_failure_rate", "dm_acceptance_rate", "dm_revision_rate", "runtime_tool_failure_rate", "useful_retrieval", "unnecessary_retrieval"):
            if report_data[name].get("label") not in {"measured", "estimated", "inferred"}:
                raise RuntimeError(f"telemetry metric {name} is unlabeled")
        run([sys.executable, str(TRACE), "promote", "--input", str(TELEMETRY / "paired.json"), "--risk", "low", "--canary", "0.10"])
        retention = temp / "retention.jsonl"
        retention.write_text("\n".join(json.dumps(record) for record in fixture_records(TELEMETRY / "retention.json")) + "\n")
        run([sys.executable, str(TRACE), "retain", "--trace", str(retention), "--days", "90"])
        if len(retention.read_text().splitlines()) != 1:
            raise RuntimeError("retention operation did not remove expired record")
        if not quarantine.is_file() or len(quarantine.read_text().splitlines()) < 2:
            raise RuntimeError("incompatible telemetry was not quarantined")


def main() -> int:
    try:
        check_hybrid()
        check_telemetry()
    except (OSError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("PASS: hybrid SDD route, evidence, telemetry, preset, promotion, retention, and compatibility fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
