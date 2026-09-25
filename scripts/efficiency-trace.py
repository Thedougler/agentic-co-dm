#!/usr/bin/env python3
"""Record, report, retain, and promote redacted efficiency traces.

Examples:
  python3 scripts/efficiency-trace.py record --input trace.json
  python3 scripts/efficiency-trace.py report
  python3 scripts/efficiency-trace.py retain --days 30
  python3 scripts/efficiency-trace.py promote --input trace.json --risk low
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import statistics
import sys
from pathlib import Path
from typing import Any, Iterable, NoReturn

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "config" / "efficiency.yaml"
SUPPORTED_SCHEMA = 1
SITTING_CLASSES = {"prep", "wrapup"}
WORK_STATUSES = {"produced", "accepted", "failed", "incomplete"}
MEASUREMENT_STATUSES = {"complete", "measurement-gap"}
DM_ACCEPTANCE = {"not-required", "pending", "accepted", "modified", "rejected"}
RAW_KEYS = {"prompt", "raw_prompt", "raw_content", "campaign_content", "wiki_content", "model_content", "provider_content"}
TRAJECTORY_FIELDS = ("request", "loaded_context", "retrieval", "tools", "failures", "retries", "model_input", "model_output", "final_work")
RETRIEVAL_FIELDS = ("queries", "fetches", "tokens", "useful", "unused")


def error(message: str) -> NoReturn:
    raise ValueError(message)


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        error(f"cannot read JSON input {path}: {exc}")


def _scalar(text: str, key: str) -> str | None:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(f"{key}:"):
            value = stripped.split(":", 1)[1].strip().split(" #", 1)[0].strip()
            return value.strip("\"'")
    return None


def policy() -> dict[str, Any]:
    """Read the policy scalars needed by the CLI without adding a YAML dependency."""
    try:
        text = POLICY_PATH.read_text(encoding="utf-8")
    except OSError as exc:
        error(f"cannot read efficiency policy {POLICY_PATH}: {exc}")
    values = {
        "schema_version": _scalar(text, "schema_version"),
        "policy_version": _scalar(text, "policy_version"),
        "retention_days": _scalar(text, "retention_days"),
        "minimum_pairs": _scalar(text, "minimum_pairs"),
        "minimum_median_reduction": _scalar(text, "minimum_median_reduction"),
        "native_tokenizer_accepted": None,
    }
    in_native = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped == "native_tokenizer_governance:":
            in_native = True
            continue
        if in_native and stripped and not line.startswith((" ", "\t")):
            in_native = False
        if in_native and stripped.startswith("accepted:"):
            values["native_tokenizer_accepted"] = _scalar(stripped, "accepted") == "true"
    if values["schema_version"] != "1" or not values["policy_version"]:
        error("efficiency policy is missing a supported schema_version or policy_version")
    try:
        values["retention_days"] = int(values["retention_days"] or 0)
        values["minimum_pairs"] = int(values["minimum_pairs"] or 0)
        values["minimum_median_reduction"] = float(values["minimum_median_reduction"] or 0)
    except ValueError as exc:
        error(f"efficiency policy has invalid numeric thresholds: {exc}")
    if values["retention_days"] <= 0 or values["minimum_pairs"] <= 0:
        error("efficiency policy thresholds must be positive")
    if values["native_tokenizer_accepted"] is None:
        error("efficiency policy must declare native tokenizer governance acceptance")
    return values


def records_from(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, list):
        raw_records: Any = value
    elif isinstance(value, dict):
        raw_records = value.get("records", [value])
    else:
        error("input must be a JSON object or array of objects")
    if not isinstance(raw_records, list) or not all(isinstance(item, dict) for item in raw_records):
        error("input must be a JSON object or array of objects")
    return [item for item in raw_records]


def walk(value: Any, path: str = "") -> Iterable[tuple[str, Any]]:
    yield path, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, f"{path}.{key}" if path else key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]")


def validate_count(value: Any, label: str) -> None:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        error(f"{label} must be a non-negative integer")


def validate_record(record: dict[str, Any]) -> dict[str, Any]:
    if record.get("record_kind") == "command":
        if record.get("schema_version") != SUPPORTED_SCHEMA:
            error(f"incompatible schema_version {record.get('schema_version')}; supported {SUPPORTED_SCHEMA}")
        if record.get("command") not in {"lint", "lint fix", "query", "health"}:
            error(f"invalid command {record.get('command')}")
        validate_count(record.get("duration_ms"), "duration_ms")
        for key in ("cache_hits", "cache_misses", "vale_skipped"):
            validate_count(record.get(key), key)
        if record.get("exit") not in {0, 1, 2}:
            error(f"invalid exit {record.get('exit')}")
        if not isinstance(record.get("timestamp"), str) or not record["timestamp"].strip():
            error("timestamp must be a non-empty string")
        return record
    required = ("schema_version", "trace_id", "policy_version", "sitting_class", "work_status", "measurement_status", "model_family", "tokenizer_family", "encoding", "trajectory", "retrieval", "source_components", "quality")
    missing = [key for key in required if key not in record]
    if missing:
        error(f"missing required fields: {', '.join(missing)}")
    if record["schema_version"] != SUPPORTED_SCHEMA:
        error(f"incompatible schema_version {record['schema_version']}; supported {SUPPORTED_SCHEMA}")
    for key in ("trace_id", "policy_version", "model_family", "tokenizer_family", "encoding"):
        if not isinstance(record[key], str) or not record[key].strip():
            error(f"{key} must be a non-empty string")
    if record["sitting_class"] not in SITTING_CLASSES:
        error(f"invalid sitting_class {record['sitting_class']}")
    if record["work_status"] not in WORK_STATUSES:
        error(f"invalid work_status {record['work_status']}")
    if record["measurement_status"] not in MEASUREMENT_STATUSES:
        error(f"invalid measurement_status {record['measurement_status']}")
    if record["measurement_status"] == "measurement-gap" and not isinstance(record.get("measurement_gap_reason"), str):
        error("measurement-gap records require measurement_gap_reason")
    if record.get("comparison_sample") is True and record["measurement_status"] != "complete":
        error("measurement-gap cannot be a comparison sample")
    if str(record["tokenizer_family"]).lower().startswith("native") and not policy()["native_tokenizer_accepted"]:
        if record["measurement_status"] != "measurement-gap":
            error("native-tokenizer record requires an explicit governance measurement gap")
    for key, value in walk(record):
        if key.rsplit(".", 1)[-1].split("[", 1)[0].lower() in RAW_KEYS:
            error(f"raw-content field is not allowed: {key}")
    trajectory = record["trajectory"]
    if not isinstance(trajectory, dict):
        error("trajectory must be an object")
    for key in TRAJECTORY_FIELDS:
        if key not in trajectory:
            error(f"trajectory.{key} is required")
        validate_count(trajectory[key], f"trajectory.{key}")
    retrieval = record["retrieval"]
    if not isinstance(retrieval, dict):
        error("retrieval must be an object")
    for key in RETRIEVAL_FIELDS:
        if key not in retrieval:
            error(f"retrieval.{key} is required")
        validate_count(retrieval[key], f"retrieval.{key}")
    for key in ("attempted_collections", "fallbacks"):
        if not isinstance(retrieval.get(key), list) or not all(isinstance(item, str) for item in retrieval[key]):
            error(f"retrieval.{key} must be a list of strings")
    if retrieval["useful"] + retrieval["unused"] > retrieval["fetches"]:
        error("retrieval useful and unused counts exceed fetches")
    known_collections = {"wiki": 0, "shattered-sea": 1, "legacy": 2}
    attempted_known = [known_collections[name] for name in retrieval["attempted_collections"] if name in known_collections]
    if attempted_known != sorted(attempted_known):
        error("retrieval collections must preserve wiki -> shattered-sea -> legacy precedence")
    if retrieval.get("accepted_canon_overridden") is True:
        error("fallback retrieval cannot override accepted canon")
    components = record["source_components"]
    if not isinstance(components, list) or not components:
        error("source_components must be a non-empty list")
    source_total = 0
    owners: set[str] = set()
    for component in components:
        if not isinstance(component, dict) or not isinstance(component.get("owner"), str) or not component["owner"]:
            error("each source component needs an owner")
        if component["owner"] in owners:
            error(f"duplicate primary source owner {component['owner']}")
        owners.add(component["owner"])
        validate_count(component.get("tokens"), f"source_components[{component['owner']}].tokens")
        source_total += component["tokens"]
        if not isinstance(component.get("secondary_provenance", []), list):
            error(f"secondary_provenance for {component['owner']} must be a list")
    tokens = record.get("tokens")
    if tokens is not None:
        if not isinstance(tokens, dict):
            error("tokens must be an object")
        for key, value in tokens.items():
            if key not in {"input", "output", "total", "source_components"}:
                continue
            if key != "source_components":
                validate_count(value, f"tokens.{key}")
        total = tokens.get("total")
        if total is not None and source_total > total:
            error("primary source component tokens exceed total tokens")
    quality = record["quality"]
    if not isinstance(quality, dict):
        error("quality must be an object")
    for key in ("hard_gate_failures", "dm_revisions", "runtime_failures"):
        validate_count(quality.get(key), f"quality.{key}")
    if quality.get("semantic_non_inferior") not in {True, False}:
        error("quality.semantic_non_inferior must be boolean")
    if quality.get("dm_acceptance") not in DM_ACCEPTANCE:
        error(f"invalid quality.dm_acceptance {quality.get('dm_acceptance')}")
    if record["work_status"] == "accepted" and quality["dm_acceptance"] != "accepted":
        error("accepted Work requires explicit DM acceptance")
    if record["work_status"] in {"failed", "incomplete"}:
        if not isinstance(record.get("failure_reason"), str) or not record["failure_reason"].strip():
            error(f"{record['work_status']} Work requires failure_reason")
    return record


def quarantine(record: dict[str, Any], reason: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"quarantined_at": dt.datetime.now(dt.timezone.utc).isoformat(), "reason": reason, "record": record}
    with path.open("a") as stream:
        stream.write(json.dumps(payload, sort_keys=True) + "\n")


def append_records(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as stream:
        for record in records:
            stream.write(json.dumps(record, sort_keys=True) + "\n")


def load_stream(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            value: Any = json.loads(line)
        except json.JSONDecodeError as exc:
            error(f"invalid JSONL at line {line_number}: {exc}")
        if not isinstance(value, dict):
            error(f"JSONL line {line_number} is not an object")
        records.append(value)
    return records


def metric(value: int | float, denominator: int | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {"value": value, "label": "measured"}
    if denominator is not None:
        result["denominator"] = denominator
    return result


def report(records: list[dict[str, Any]]) -> dict[str, Any]:
    valid = [validate_record(record) for record in records if record.get("record_kind") != "command"]
    trajectory_total = sum(sum(record["trajectory"].values()) for record in valid)
    input_total = sum(record["trajectory"]["model_input"] for record in valid)
    output_total = sum(record["trajectory"]["model_output"] for record in valid)
    accepted = sum(record["work_status"] == "accepted" for record in valid)
    comparable = [record for record in valid if record["measurement_status"] == "complete" and record["work_status"] == "accepted"]
    comparison_groups: dict[str, int] = {}
    for record in comparable:
        key = f"{record['sitting_class']}:{record.get('job', 'unspecified')}"
        comparison_groups[key] = comparison_groups.get(key, 0) + 1
    retries = sum(record["trajectory"]["retries"] for record in valid)
    attempts = sum(sum(record["trajectory"].values()) for record in valid)
    hard_failures = sum(record["quality"]["hard_gate_failures"] for record in valid)
    revisions = sum(record["quality"]["dm_revisions"] for record in valid)
    runtime = sum(record["quality"]["runtime_failures"] for record in valid)
    retrieval_queries = sum(record["retrieval"]["queries"] for record in valid)
    retrieval_fetches = sum(record["retrieval"]["fetches"] for record in valid)
    retrieval_tokens = sum(record["retrieval"]["tokens"] for record in valid)
    component_totals: dict[str, int] = {}
    for record in valid:
        for component in record["source_components"]:
            owner = component["owner"]
            component_totals[owner] = component_totals.get(owner, 0) + component["tokens"]
    return {
        "records": len(valid),
        "sitting_classes": sorted({record["sitting_class"] for record in valid}),
        "jobs": sorted({record.get("job", "unspecified") for record in valid}),
        "trajectory_tokens": metric(trajectory_total),
        "input_tokens": metric(input_total),
        "output_tokens": metric(output_total),
        "source_components": {owner: metric(tokens) for owner, tokens in sorted(component_totals.items())},
        "retrieval": {"queries": metric(retrieval_queries), "fetches": metric(retrieval_fetches), "tokens": metric(retrieval_tokens)},
        "retry_amplification": metric(retries / max(1, attempts), len(valid)),
        "hard_gate_failure_rate": metric(hard_failures / max(1, len(valid)), len(valid)),
        "dm_acceptance_rate": metric(accepted / max(1, len(valid)), len(valid)),
        "dm_revision_rate": metric(revisions / max(1, accepted), accepted),
        "runtime_tool_failure_rate": metric(runtime / max(1, len(valid)), len(valid)),
        "useful_retrieval": metric(sum(r["retrieval"]["useful"] for r in valid), retrieval_fetches),
        "unnecessary_retrieval": metric(sum(r["retrieval"]["unused"] for r in valid), retrieval_fetches),
        "work_status_counts": {status: metric(sum(r["work_status"] == status for r in valid), len(valid)) for status in sorted(WORK_STATUSES)},
        "measurement_status_counts": {status: metric(sum(r["measurement_status"] == status for r in valid), len(valid)) for status in sorted(MEASUREMENT_STATUSES)},
        "accepted_work_denominator": len(comparable),
        "same_kind_comparison_groups": comparison_groups,
        "policy": {"policy_version": policy()["policy_version"], "label": "measured"},
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    record = sub.add_parser("record", epilog="Examples: scripts/efficiency-trace.py record --input trace.json")
    record.add_argument("--input", required=True, type=Path)
    record.add_argument("--trace", type=Path, default=ROOT / ".local/efficiency/traces.jsonl")
    record.add_argument("--quarantine", type=Path, default=ROOT / ".local/efficiency/quarantine/rejected.jsonl")
    report_cmd = sub.add_parser("report", epilog="Examples: scripts/efficiency-trace.py report --trace .local/efficiency/traces.jsonl")
    report_cmd.add_argument("--input", type=Path)
    report_cmd.add_argument("--trace", type=Path, default=ROOT / ".local/efficiency/traces.jsonl")
    retain = sub.add_parser("retain", epilog="Examples: scripts/efficiency-trace.py retain --days 30")
    retain.add_argument("--trace", type=Path, default=ROOT / ".local/efficiency/traces.jsonl")
    retain.add_argument("--days", type=int)
    promote = sub.add_parser("promote", epilog="Examples: scripts/efficiency-trace.py promote --input trace.json --risk low")
    promote.add_argument("--input", required=True, type=Path)
    promote.add_argument("--risk", required=True, choices=("low", "moderate", "high"))
    promote.add_argument("--canary", type=float, default=0.0)
    promote.add_argument("--shadow", action="store_true")
    promote.add_argument("--human-review", action="store_true")
    return parser.parse_args()

def main() -> int:
    args = parse_args()
    try:
        if args.command == "record":
            records = records_from(read_json(args.input))
            accepted: list[dict[str, Any]] = []
            failures: list[str] = []
            for record in records:
                try:
                    accepted.append(validate_record(record))
                except ValueError as exc:
                    reason = str(exc)
                    quarantine(record, reason, args.quarantine)
                    failures.append(reason)
            append_records(accepted, args.trace)
            if failures:
                error(f"{len(failures)} record(s) quarantined: {'; '.join(failures)}")
            print(json.dumps({"status": "recorded", "count": len(accepted), "trace": str(args.trace)}))
        elif args.command == "report":
            records = records_from(read_json(args.input)) if args.input else load_stream(args.trace)
            print(json.dumps(report(records), sort_keys=True))
        elif args.command == "retain":
            retention_days = policy()["retention_days"] if args.days is None else args.days
            if retention_days < 0:
                error("retention days must be non-negative")
            cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=retention_days)
            kept: list[dict[str, Any]] = []
            removed = 0
            for record in load_stream(args.trace):
                stamp = record.get("timestamps", {}).get("started_at") or record.get("timestamp")
                try:
                    when = dt.datetime.fromisoformat(str(stamp).replace("Z", "+00:00"))
                except (TypeError, ValueError):
                    kept.append(record)
                    continue
                if when >= cutoff:
                    kept.append(record)
                else:
                    removed += 1
            args.trace.parent.mkdir(parents=True, exist_ok=True)
            args.trace.write_text("".join(json.dumps(record, sort_keys=True) + "\n" for record in kept), encoding="utf-8")
            print(json.dumps({"status": "retained", "removed": removed, "days": retention_days}))
        elif args.command == "promote":
            settings = policy()
            records = [validate_record(record) for record in records_from(read_json(args.input)) if record.get("record_kind") != "command"]
            complete = [
                record
                for record in records
                if record["measurement_status"] == "complete" and record["work_status"] == "accepted"
            ]
            classes = {record["sitting_class"] for record in complete}
            jobs = {record.get("job") for record in complete}
            identities = {(record["model_family"], record["tokenizer_family"], record["encoding"]) for record in complete}
            if len(complete) < settings["minimum_pairs"] or len(classes) != 1 or len(jobs) != 1:
                error(f"promotion requires at least {settings['minimum_pairs']} same-kind accepted complete records")
            if len(identities) != 1:
                error("promotion rejected: model/tokenizer families and encodings are not comparable")
            if any(str(r["tokenizer_family"]).lower().startswith("native") for r in complete) and not settings["native_tokenizer_accepted"]:
                error("promotion blocked: native-tokenizer governance is pending")
            if any(r["quality"]["hard_gate_failures"] for r in complete) or not all(r["quality"]["semantic_non_inferior"] for r in complete):
                error("promotion blocked by hard-gate or semantic regression; rollback required")
            reductions: list[float] = []
            for record in complete:
                baseline = record.get("baseline_trajectory_tokens")
                if baseline is None:
                    error("promotion requires a pinned baseline trajectory for every pair")
                validate_count(baseline, "baseline_trajectory_tokens")
                current = sum(record["trajectory"].values())
                reductions.append((baseline - current) / max(1, baseline))
                baseline_quality = record.get("baseline_quality")
                if isinstance(baseline_quality, dict):
                    for field in ("runtime_failures", "dm_revisions"):
                        if field in baseline_quality:
                            validate_count(baseline_quality[field], f"baseline_quality.{field}")
                            if record["quality"][field] > baseline_quality[field]:
                                error(f"promotion blocked by material {field} regression; rollback required")
            median_reduction = statistics.median(reductions)
            if median_reduction < settings["minimum_median_reduction"]:
                error(f"promotion requires at least a {settings['minimum_median_reduction']:.0%} median trajectory-token reduction")
            if not 0 <= args.canary <= 1:
                error("canary must be a fraction between 0 and 1")
            if args.risk == "low" and args.canary < 0.10:
                error("low-risk promotion requires a 10% canary")
            if args.risk == "moderate" and (not args.shadow or args.canary < 0.10):
                error("moderate-risk promotion requires shadow replay and canary review")
            if args.risk == "high" and not args.human_review:
                error("high-risk promotion requires human review")
            print(json.dumps({"status": "promotable", "risk": args.risk, "pairs": len(complete), "median_reduction": median_reduction, "policy_version": settings["policy_version"]}))
        return 0
    except (ValueError, OSError) as exc:
        print(f"FAIL {args.command}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
