"""Compact health snapshot shaping for the agent-facing wiki CLI.

The command layer owns reading the vault and tracker files.  This module only
normalises the dictionaries it is given into the bounded result shapes in the
health contract.
"""
from __future__ import annotations

import copy
import math
import re
import json

from collections import Counter
from collections.abc import Iterable, Mapping, Sequence
from pathlib import Path, PurePosixPath
from typing import Any, TypeAlias

JsonObject: TypeAlias = dict[str, Any]
TrackerInput: TypeAlias = Mapping[str, Any] | Sequence[Mapping[str, Any]] | None

__all__ = ["build_trends", "build_focus", "build_health_snapshot", "build_context_load", "build_core_files"]

_DRIVE_PATH = re.compile(r"^[A-Za-z]:(?:/|\\)")


def _number(value: Any, default: int | float = 0) -> int | float:
    """Return finite numeric values while treating malformed tracker data as zero."""
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        return default
    return value


def _int(value: Any, default: int = 0) -> int:
    raw = _number(value, default)
    try:
        return int(raw)
    except (TypeError, ValueError, OverflowError):
        return default


def _float(value: Any, default: float = 0.0) -> float:
    raw = _number(value, default)
    try:
        return float(raw)
    except (TypeError, ValueError, OverflowError):
        return default


def _metric(value: Any, default: int | float = 0) -> int | float:
    if isinstance(value, Mapping):
        return _metric(value.get("value", default), default)
    return _number(value, default)


def _clone(value: Any) -> Any:
    """Copy caller-owned dictionaries so shaping never mutates tracker results."""
    return copy.deepcopy(value)


def _rows(value: Any, keys: Sequence[str] = ()) -> list[Mapping[str, Any]]:
    """Extract record rows from a list, a records wrapper, or one record."""
    if value is None:
        return []
    if isinstance(value, Mapping):
        for key in keys:
            candidate = value.get(key)
            if isinstance(candidate, Sequence) and not isinstance(candidate, (str, bytes, bytearray)):
                return [row for row in candidate if isinstance(row, Mapping)]
        return [value]
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [row for row in value if isinstance(row, Mapping)]
    if isinstance(value, Iterable) and not isinstance(value, (str, bytes, bytearray)):
        items = list(value)
        if isinstance(value, (set, frozenset)):
            items.sort(key=repr)
        return [row for row in items if isinstance(row, Mapping)]
    return []


def _summary_mapping(value: Any, keys: Sequence[str]) -> Mapping[str, Any] | None:
    if not isinstance(value, Mapping) or not any(key in value for key in keys):
        return None
    # A wrapper containing rows is not itself an aggregate.
    if any(
        isinstance(value.get(key), Sequence) and not isinstance(value.get(key), (str, bytes, bytearray))
        for key in ("records", "sittings", "entries", "errors", "traces", "items")
    ):
        return None
    return value


def _skill_names(value: Any) -> list[str]:
    if isinstance(value, Mapping):
        if "name" in value:
            value = value.get("name")
        else:
            value = value.keys()
    if isinstance(value, str):
        values: Iterable[Any] = (value,)
    elif isinstance(value, Iterable) and not isinstance(value, (bytes, bytearray)):
        values = value
    else:
        return []
    result: list[str] = []
    for item in values:
        if isinstance(item, Mapping):
            item = item.get("name")
        if isinstance(item, str) and item.strip():
            result.append(item.strip())
    return result


def _sitting_trends(sittings: TrackerInput) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    summary = _summary_mapping(sittings, ("count", "by_kind", "skills"))
    if summary is not None and "count" in summary:
        raw_by_kind = summary.get("by_kind")
        by_kind: Mapping[str, Any] = raw_by_kind if isinstance(raw_by_kind, Mapping) else {}
        sitting = {
            "count": _int(summary.get("count")),
            "by_kind": {kind: _int(by_kind.get(kind)) for kind in ("prep", "wrapup")},
        }
        skills: list[dict[str, Any]] = []
        raw_skills = summary.get("skills")
        if isinstance(raw_skills, Sequence) and not isinstance(raw_skills, (str, bytes, bytearray)):
            for row in raw_skills:
                if not isinstance(row, Mapping) or not isinstance(row.get("name"), str):
                    continue
                name = row["name"].strip()
                if name:
                    skills.append({"name": name, "sittings": _int(row.get("sittings"))})
        skills.sort(key=lambda row: (-row["sittings"], row["name"]))
        return sitting, skills[:5]

    rows = _rows(sittings, ("records", "sittings", "items"))
    by_kind = {kind: 0 for kind in ("prep", "wrapup")}
    skill_counts: Counter[str] = Counter()
    for row in rows:
        kind = row.get("kind", row.get("sitting_class"))
        if isinstance(kind, str) and kind.casefold() in by_kind:
            by_kind[kind.casefold()] += 1
        skill_counts.update(set(_skill_names(row.get("skills_loaded", row.get("skills")))))
    skills = [
        {"name": name, "sittings": count}
        for name, count in sorted(skill_counts.items(), key=lambda pair: (-pair[1], pair[0]))[:5]
    ]
    return {"count": len(rows), "by_kind": by_kind}, skills


def _cause_rows(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        return []
    result: list[dict[str, Any]] = []
    for row in value:
        if not isinstance(row, Mapping) or not isinstance(row.get("cause"), str):
            continue
        cause = row["cause"].strip()
        if cause:
            result.append({"cause": cause, "count": _int(row.get("count"))})
    result.sort(key=lambda row: (-row["count"], row["cause"]))
    return result[:3]


def _error_entries(value: Any, *, limit: int = 5) -> list[dict[str, Any]]:
    """Expose small open-ledger records without dumping the ledger."""
    rows = _rows(value, ("records", "errors", "entries", "items"))
    entries: list[dict[str, Any]] = []
    for row in rows:
        status = row.get("status", "open")  # errors.md entries carry no status: every entry is open
        if not isinstance(status, str) or status.casefold() != "open":
            continue
        entry: dict[str, Any] = {"status": "open"}
        for key in ("id", "cause"):
            if isinstance(row.get(key), str) and row[key].strip():
                entry[key] = row[key].strip()
        path = _error_path(row)
        if path:
            entry["path"] = path
        elif isinstance(row.get("sitting"), str) and row["sitting"].strip():
            entry["sitting"] = row["sitting"].strip()
        entries.append(entry)
    return entries if len(entries) <= limit else []


def _with_error_entries(result: dict[str, Any], source: Any) -> dict[str, Any]:
    entries = _error_entries(source)
    if entries:
        result["entries"] = entries
    elif _rows(source, ("records", "errors", "entries", "items")) == []:
        result["entries"] = []
    return result


def _error_trends(errors: TrackerInput) -> dict[str, Any]:
    summary = _summary_mapping(errors, ("open_count", "causes"))
    if summary is not None and "open_count" in summary:
        result = {"open_count": _int(summary.get("open_count")), "causes": _cause_rows(summary.get("causes"))}
        return _with_error_entries(result, summary.get("entries"))

    rows = _rows(errors, ("records", "errors", "entries", "items"))
    causes: Counter[str] = Counter()
    open_count = 0
    for row in rows:
        status = row.get("status", "open")  # errors.md entries carry no status: every entry is open
        if not isinstance(status, str) or status.casefold() != "open":
            continue
        open_count += 1
        cause = row.get("cause")
        if isinstance(cause, str) and cause.strip():
            causes[cause.strip()] += 1
    result = {
        "open_count": open_count,
        "causes": [
            {"cause": cause, "count": count}
            for cause, count in sorted(causes.items(), key=lambda pair: (-pair[1], pair[0]))[:3]
        ],
    }
    return _with_error_entries(result, rows)


def _trajectory_tokens(row: Mapping[str, Any]) -> int:
    direct = row.get("trajectory_tokens")
    if direct is not None:
        return _int(_metric(direct))
    trajectory = row.get("trajectory")
    if not isinstance(trajectory, Mapping):
        return 0
    return sum(_int(_metric(value)) for value in trajectory.values())


def _retrieval_queries(row: Mapping[str, Any]) -> int:
    direct = row.get("retrieval_queries")
    if direct is not None:
        return _int(_metric(direct))
    retrieval = row.get("retrieval")
    if isinstance(retrieval, Mapping):
        return _int(_metric(retrieval.get("queries")))
    return 0


def _efficiency_trends(efficiency: TrackerInput) -> dict[str, Any]:
    summary = _summary_mapping(
        efficiency,
        ("records", "trajectory_tokens", "retrieval_queries", "hard_gate_failure_rate", "dm_acceptance_rate"),
    )
    if summary is not None and "records" in summary and not isinstance(summary.get("records"), Sequence):
        raw_retrieval = summary.get("retrieval")
        retrieval: Mapping[str, Any] = raw_retrieval if isinstance(raw_retrieval, Mapping) else {}
        return {
            "records": _int(summary.get("records")),
            "trajectory_tokens": _int(_metric(summary.get("trajectory_tokens"))),
            "retrieval_queries": _int(_metric(summary.get("retrieval_queries", retrieval.get("queries")))),
            "hard_gate_failure_rate": _float(_metric(summary.get("hard_gate_failure_rate"))),
            "dm_acceptance_rate": _float(_metric(summary.get("dm_acceptance_rate"))),
        }

    rows = _rows(efficiency, ("records", "traces", "items"))
    trajectory_total = sum(_trajectory_tokens(row) for row in rows)
    retrieval_total = sum(_retrieval_queries(row) for row in rows)
    hard_failures = 0
    accepted = 0
    direct_hard_rates: list[float] = []
    direct_acceptance_rates: list[float] = []
    for row in rows:
        raw_quality = row.get("quality")
        quality: Mapping[str, Any] = raw_quality if isinstance(raw_quality, Mapping) else {}
        hard_value = quality.get("hard_gate_failures", row.get("hard_gate_failures"))
        if hard_value is None and row.get("hard_gate_failure_rate") is not None:
            direct_hard_rates.append(_float(_metric(row.get("hard_gate_failure_rate"))))
        else:
            hard_failures += _int(_metric(hard_value))
        status = row.get("work_status")
        if isinstance(status, str):
            accepted += status.casefold() == "accepted"
        elif row.get("dm_acceptance_rate") is not None:
            direct_acceptance_rates.append(_float(_metric(row.get("dm_acceptance_rate"))))
        else:
            acceptance = row.get("dm_acceptance")
            if isinstance(acceptance, str) and acceptance.casefold() == "accepted":
                accepted += 1
    record_count = len(rows)
    hard_rate = (
        hard_failures / record_count
        if record_count
        else (sum(direct_hard_rates) / len(direct_hard_rates) if direct_hard_rates else 0.0)
    )
    acceptance_rate = (
        accepted / record_count
        if record_count
        else (sum(direct_acceptance_rates) / len(direct_acceptance_rates) if direct_acceptance_rates else 0.0)
    )
    return {
        "records": record_count,
        "trajectory_tokens": trajectory_total,
        "retrieval_queries": retrieval_total,
        "hard_gate_failure_rate": hard_rate,
        "dm_acceptance_rate": acceptance_rate,
    }


def _efficiency_detail(efficiency: TrackerInput) -> tuple[list[Mapping[str, Any]], list[Mapping[str, Any]]]:
    """Return command and sitting rows, excluding aggregate report summaries."""
    if isinstance(efficiency, Mapping):
        if isinstance(efficiency.get("records"), int):
            return [], []
        rows = _rows(efficiency, ("records", "traces", "items"))
    else:
        rows = _rows(efficiency, ("records", "traces", "items"))
    commands: list[Mapping[str, Any]] = []
    sittings: list[Mapping[str, Any]] = []
    known_commands = {"lint", "query", "health"}
    for row in rows:
        command = row.get("command")
        if row.get("record_kind") == "command" or (
            command in known_commands and "sitting_class" not in row
        ):
            commands.append(row)
        elif row.get("record_kind") == "sitting" or "sitting_class" in row or "kind" in row:
            sittings.append(row)
    return commands, sittings


def build_trends(sittings: TrackerInput, errors: TrackerInput, efficiency: TrackerInput) -> dict[str, Any]:
    """Aggregate retained sitting, error, and efficiency tracker records."""
    sitting, skills = _sitting_trends(sittings)
    commands, efficiency_sittings = _efficiency_detail(efficiency)
    command_groups: dict[str, list[int]] = {}
    for row in commands:
        command = row.get("command")
        if isinstance(command, str) and command:
            command_groups.setdefault(command, []).append(_int(row.get("duration_ms")))
    slowest = [
        {"command": command, "duration_ms": max(durations), "n": len(durations)}
        for command, durations in command_groups.items()
    ]
    slowest.sort(key=lambda row: row["duration_ms"], reverse=True)
    token_groups: dict[tuple[str, str], int] = {}
    for row in efficiency_sittings:
        sitting_class = row.get("sitting_class", row.get("kind", "unspecified"))
        job = row.get("job", "unspecified")
        key = (str(sitting_class), str(job))
        token_groups[key] = token_groups.get(key, 0) + _trajectory_tokens(row)
    token_heaviest = [
        {"sitting_class": sitting_class, "job": job, "tokens": tokens}
        for (sitting_class, job), tokens in token_groups.items()
    ]
    token_heaviest.sort(key=lambda row: row["tokens"], reverse=True)
    return {
        "sittings": sitting,
        "skills": skills,
        "errors": _error_trends(errors),
        "efficiency": _efficiency_trends(
            efficiency if isinstance(efficiency, Mapping) and isinstance(efficiency.get("records"), int) else efficiency_sittings
        ),
        "slowest_commands": slowest[:3],
        "token_heaviest": token_heaviest[:3],
    }


def _relative_path(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    text = value.strip().replace("\\", "/")
    if not text or text.startswith(("/", "~")) or _DRIVE_PATH.match(text) or "\x00" in text:
        return None
    path = PurePosixPath(text)
    if not path.parts or path.parts == (".",) or ".." in path.parts:
        return None
    return path.as_posix()


def _plan_items(value: Any, keys: Sequence[str] = ("plans", "items", "entries", "prefixes", "layout", "layouts")) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, Mapping):
        for key in keys:
            candidate = value.get(key)
            if isinstance(candidate, Sequence) and not isinstance(candidate, (str, bytes, bytearray)):
                return list(candidate)
        if any(key in value for key in ("src", "path", "prefix", "layout_prefix", "remorph_prefix")):
            return [value]
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, Sequence) and not isinstance(value, (bytes, bytearray)):
        return list(value)
    return []


def _reason(value: Any, fallback: str) -> str:
    return value.strip() if isinstance(value, str) and value.strip() else fallback


def _lint_reason(lint: Mapping[str, Any], page: str) -> str:
    next_item = lint.get("next")
    if isinstance(next_item, Mapping) and next_item.get("path") == page:
        findings = next_item.get("findings")
        if isinstance(findings, (int, float)) and not isinstance(findings, bool):
            return f"{_int(findings)} lint findings on this page"
        action = next_item.get("action")
        if isinstance(action, str) and action.strip():
            return action.strip()
    for key in ("next_reason", "reason"):
        if isinstance(lint.get(key), str) and lint[key].strip():
            return lint[key].strip()
    backlog = lint.get("backlog")
    if isinstance(backlog, Sequence) and not isinstance(backlog, (str, bytes, bytearray)):
        for row in backlog:
            if not isinstance(row, Mapping):
                continue
            if row.get("page", row.get("path")) != page:
                continue
            findings = row.get("findings", row.get("rules"))
            if isinstance(findings, (int, float)) and not isinstance(findings, bool):
                return f"{_int(findings)} lint findings on this page"
            if isinstance(findings, str) and findings.strip():
                return findings.strip()
            if isinstance(findings, Sequence) and not isinstance(findings, (str, bytes, bytearray)):
                for finding in findings:
                    rule = finding.get("rule") if isinstance(finding, Mapping) else finding
                    if isinstance(rule, str) and rule.strip():
                        return rule.strip()
    counts = lint.get("counts")
    if isinstance(counts, Mapping):
        rules = sorted(str(rule) for rule, count in counts.items() if _int(count) > 0)
        if rules:
            return f"{rules[0]} lint findings"
    return "lint findings"


def _focus_action(source: str, path: str, reason: str) -> str:
    if source == "lint":
        return f"Repair {reason} in {path}, then rerun wiki health."
    if source == "tracker":
        return f"Resolve the open error for {path}, then rerun wiki health."
    return f"Apply the {source} plan for {path}, then rerun wiki health."


def _error_path(row: Any) -> str | None:
    if not isinstance(row, Mapping):
        return None
    for key in ("path", "file", "page", "source"):
        path = _relative_path(row.get(key))
        if path and not path.startswith("external:"):
            return path
    sitting = row.get("sitting")
    if isinstance(sitting, Mapping):
        for key in ("path", "file", "page"):
            path = _relative_path(sitting.get(key))
            if path:
                return path
        return None
    if isinstance(sitting, str) and ("/" in sitting or sitting.casefold().endswith(".md")):
        return _relative_path(sitting)
    return None


def build_focus(
    lint: Mapping[str, Any] | None,
    remorph: Any = None,
    layout: Any = None,
    open_errors: TrackerInput = None,
    cap: int = 5,
) -> list[dict[str, str]]:
    """Choose bounded, existing paths in lint/remorph/layout/tracker order."""
    limit = max(0, _int(cap, 5))
    if limit == 0:
        return []
    items: list[dict[str, str]] = []
    seen: set[str] = set()

    def add(path: Any, reason: Any, source: str, fallback: str) -> None:
        if len(items) >= limit:
            return
        relative = _relative_path(path)
        if relative is None or relative in seen:
            return
        seen.add(relative)
        objective = _reason(reason, fallback)
        items.append({
            "path": relative,
            "reason": objective,
            "source": source,
            "action": _focus_action(source, relative, objective),
        })

    if isinstance(lint, Mapping):
        add(lint.get("next_page"), _lint_reason(lint, str(lint.get("next_page", ""))), "lint", "lint findings")

    plans = _plan_items(remorph)
    for plan in plans:
        if not isinstance(plan, Mapping):
            add(plan, None, "remorph", "remorph plan")
            continue
        add(plan.get("src"), plan.get("reason"), "remorph", "remorph plan")
        nested: list[Any] = []
        for key in (
            "prefixes",
            "layout_prefixes",
            "remorph_prefixes",
            "layout",
            "layouts",
        ):
            if key in plan:
                nested.extend(_plan_items(plan.get(key), ("items", "entries", "prefixes", "plans")))
        for prefix in nested:
            if isinstance(prefix, Mapping):
                add(
                    prefix.get("prefix", prefix.get("path", prefix.get("layout_prefix", prefix.get("remorph_prefix")))),
                    prefix.get("reason", plan.get("reason")),
                    "layout",
                    "layout plan",
                )
            else:
                add(prefix, plan.get("reason"), "layout", "layout plan")

    for item in _plan_items(layout):
        if isinstance(item, Mapping):
            add(
                item.get("prefix", item.get("path", item.get("layout_prefix"))),
                item.get("reason"),
                "layout",
                "layout plan",
            )
        else:
            add(item, None, "layout", "layout plan")

    return items
def _compact_lint(lint: Any) -> dict[str, Any]:
    if not isinstance(lint, Mapping):
        return {}
    result = {
        key: _clone(value)
        for key, value in lint.items()
        if key not in {"findings", "findings_by_file", "files"}
    }
    raw_counts = lint.get("counts")
    counts = raw_counts if isinstance(raw_counts, Mapping) else {}
    finding_total = _int(lint.get("finding_total")) or sum(_int(value) for value in counts.values())
    raw_affected = lint.get("affected_pages")
    if isinstance(raw_affected, (int, float)) and not isinstance(raw_affected, bool):
        affected_pages = max(0, int(raw_affected))
    else:
        backlog = lint.get("backlog")
        affected_pages = (
            len(backlog)
            if isinstance(backlog, Sequence) and not isinstance(backlog, (str, bytes, bytearray))
            else len({
                target
                for values in (lint.get("unique"),)
                if isinstance(values, Mapping)
                for targets in values.values()
                if isinstance(targets, Sequence) and not isinstance(targets, (str, bytes, bytearray))
                for target in targets
            })
        )
    blocking = [
        {"rule": str(rule), "findings": _int(count)}
        for rule, count in sorted(counts.items(), key=lambda item: str(item[0]))
        if _int(count) > 0
    ]
    hard_fail = bool(lint.get("hard_fail"))
    result.update({
        "finding_total": finding_total,
        "affected_pages": affected_pages,
        "blocking": blocking if hard_fail else [],
        "meaning": (
            f"{finding_total:,} blocking lint findings remain across {affected_pages:,} pages."
            if hard_fail
            else "No blocking lint findings remain."
        ),
        "action": (
            "Repair the blocking findings, then rerun wiki health."
            if hard_fail
            else "No blocking lint repair is required."
        ),
    })
    return result




def _layer_object(value: Any, fields: Sequence[str]) -> dict[str, Any]:
    source: Mapping[str, Any] = value if isinstance(value, Mapping) else {}
    raw_metric = source.get("metric")
    metric: Mapping[str, Any] = raw_metric if isinstance(raw_metric, Mapping) else source
    result: dict[str, Any] = {}
    for field in fields:
        if field in metric:
            result[field] = _clone(metric[field])
        elif field == "conflict_count" and isinstance(source.get("conflicts"), Sequence):
            result[field] = len(source["conflicts"])
        elif field == "ok":
            result[field] = False
        else:
            result[field] = 0
    return result


def _status(status: Any, lint: Mapping[str, Any]) -> str:
    result = status if isinstance(status, str) and status else "clean"
    lint_status = lint.get("status")
    if result == "clean" and lint_status in {"findings", "error"}:
        return lint_status
    return result


def _repo_relative(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.name


def _token_row(root: Path, path: Path, encoding: str) -> dict[str, Any] | None:
    if not path.is_file():
        return None
    from tools.token_count import count_file

    counted = count_file(path, encoding=encoding)
    return {"path": _repo_relative(root, path), "tokens": int(counted["tokens"])}


def _previous_first_turn(traces: TrackerInput) -> int | None:
    rows = traces if isinstance(traces, Sequence) and not isinstance(traces, (str, bytes, bytearray)) else ()
    for row in reversed(list(rows)):
        if not isinstance(row, Mapping):
            continue
        if row.get("record_kind") != "command" or row.get("command") != "health":
            continue
        value = row.get("first_turn_tokens")
        if value is None:
            continue
        try:
            return int(value)
        except (TypeError, ValueError):
            continue
    return None


def _eval_coverage(skill_dir: Path) -> dict[str, Any]:
    path = skill_dir / "evals" / "evals.json"
    empty = {"evals": 0, "criteria": 0, "coverage": "without"}
    if not path.is_file():
        return empty
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return empty
    cases = payload.get("evals") if isinstance(payload, Mapping) else payload
    if not isinstance(cases, list):
        return empty
    evals = 0
    criteria = 0
    for case in cases:
        if not isinstance(case, Mapping):
            continue
        evals += 1
        rows = case.get("assertions") or case.get("expectations") or ()
        if not isinstance(rows, list):
            continue
        for row in rows:
            if isinstance(row, str) and row.strip():
                criteria += 1
            elif isinstance(row, Mapping) and str(row.get("text") or "").strip():
                criteria += 1
    return {
        "evals": evals,
        "criteria": criteria,
        "coverage": "with" if evals and criteria else "without",
    }


INDEX_LINE = re.compile(r"\[\[[^\]]+\]\]\s+[—–-]")
LOG_LINE = re.compile(r"\[20\d{2}-\d{2}-\d{2}[T ]")
HEADING = re.compile(r"^##\s+(.+)$", re.M)
H1 = re.compile(r"^#\s+", re.M)
CORE_FILES = (
    ("index.md", "master index of every page"),
    ("hot.md", "500-word semantic snapshot"),
    ("log.md", "chronological activity log"),
    ("AGENTS.md", "owner conventions"),
)


def _core_body(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4 :]
    return text


def build_core_files(vault: str | Path) -> dict[str, Any]:
    """Flag oversized, bloated, duplicate, redundant, and overlapping llm-wiki core files."""
    root = Path(vault)
    files: list[dict[str, Any]] = []
    issues: list[dict[str, str]] = []
    headings: dict[str, str] = {}
    for name, job in CORE_FILES:
        path = root / name
        row = {"path": name, "job": job, "exists": path.is_file(), "bytes": 0, "words": 0, "index_lines": 0, "log_lines": 0}
        if path.is_file():
            raw = path.read_text(encoding="utf-8")
            body = _core_body(raw)
            words = [part for part in body.split() if part]
            index_lines = len(INDEX_LINE.findall(body))
            log_lines = len(LOG_LINE.findall(body))
            row.update({
                "bytes": path.stat().st_size,
                "words": len(words),
                "index_lines": index_lines,
                "log_lines": log_lines,
            })
            if len(H1.findall(body)) > 1:
                issues.append({"path": name, "kind": "bloated", "reason": f"{name} has multiple H1 headings"})
            if name == "hot.md" and len(words) > 500:
                issues.append({"path": name, "kind": "oversized", "reason": f"hot.md is {len(words)} words; snapshot job is 500"})
            if name == "AGENTS.md" and row["bytes"] > 24 * 1024:
                issues.append({"path": name, "kind": "oversized", "reason": f"AGENTS.md is {row['bytes']} bytes; conventions belong behind a pointer past 24KB"})
            if name == "hot.md" and index_lines > 8:
                issues.append({"path": name, "kind": "cohesion", "reason": "hot.md is doing the index.md listing job"})
            if name == "hot.md" and log_lines > 3:
                issues.append({"path": name, "kind": "cohesion", "reason": "hot.md is doing the log.md activity-log job"})
            if name == "index.md" and log_lines > 5:
                issues.append({"path": name, "kind": "cohesion", "reason": "index.md is doing the log.md activity-log job"})
            if name == "log.md" and index_lines > 20 and log_lines == 0:
                issues.append({"path": name, "kind": "cohesion", "reason": "log.md is doing the index.md listing job"})
            if name == "AGENTS.md" and (index_lines > 8 or log_lines > 3):
                issues.append({"path": name, "kind": "cohesion", "reason": "AGENTS.md is duplicating index.md or log.md"})
            for heading in HEADING.findall(body):
                key = heading.strip().casefold()
                if key in headings and headings[key] != name:
                    issues.append({
                        "path": name,
                        "kind": "duplication",
                        "reason": f"{name} and {headings[key]} share heading {heading.strip()}",
                    })
                else:
                    headings[key] = name
        files.append(row)
    act = [
        f"Repair {item['path']} ({item['kind']}): {item['reason']}. Done: index.md lists pages, log.md is the activity log, hot.md is a 500-word snapshot, AGENTS.md is conventions only."
        for item in issues
    ]
    return {"files": files, "issues": issues, "act": act}


def build_context_load(
    *,
    root: Path,
    vault: Path,
    traces: TrackerInput = None,
    encoding: str | None = None,
) -> dict[str, Any]:
    """Tiktoken first-turn files, ranked skills, and imperative act steps."""
    from tools.token_count import resolve_encoding

    enc = resolve_encoding(encoding)
    seen: set[str] = set()
    files: list[dict[str, Any]] = []
    for path in (
        root / ".omp" / "AGENTS.md",
        root / "AGENTS.md",
        vault / "AGENTS.md",
        vault / "hot.md",
    ):
        row = _token_row(root, path, enc)
        if row is None or row["path"] in seen:
            continue
        seen.add(str(row["path"]))
        files.append(row)
    files.sort(key=lambda item: (-int(item["tokens"]), str(item["path"])))
    first_total = sum(int(item["tokens"]) for item in files)

    skills: list[dict[str, Any]] = []
    with_evals = 0
    without_evals = 0
    for skill in sorted((root / ".agents" / "skills").glob("*/SKILL.md")):
        row = _token_row(root, skill, enc)
        if row is None:
            continue
        coverage = _eval_coverage(skill.parent)
        if coverage["coverage"] == "with":
            with_evals += 1
        else:
            without_evals += 1
        skills.append({
            "name": skill.parent.name,
            "path": row["path"],
            "tokens": row["tokens"],
            "evals": coverage["evals"],
            "criteria": coverage["criteria"],
            "coverage": coverage["coverage"],
        })
    skills.sort(key=lambda item: (-int(item["tokens"]), str(item["name"])))

    previous = _previous_first_turn(traces)
    delta = None if previous is None else first_total - previous
    if previous is None:
        trend = "new"
    elif delta and delta > 0:
        trend = "up"
    elif delta and delta < 0:
        trend = "down"
    else:
        trend = "flat"

    act: list[str] = []
    if files:
        heaviest = files[0]
        act.append(
            f"Disclose {heaviest['path']} ({heaviest['tokens']} tokens) behind a pointer when that file is reference. Done: first-turn files are steps only."
        )
    if skills:
        heaviest_skill = skills[0]
        act.append(
            f"Load {heaviest_skill['name']} ({heaviest_skill['tokens']} tokens, {heaviest_skill['coverage']} eval criteria) only when this job matches that skill. Done: SKILL.md stayed behind its description unless the job matched."
        )
        missing = next((item for item in skills if item["coverage"] == "without"), None)
        if missing:
            act.append(
                f"Add eval criteria for {missing['name']} ({missing['tokens']} tokens, evals={missing['evals']}, criteria={missing['criteria']}). Done: evals.json has assertions or expectations."
            )
    if trend == "up" and delta:
        act.append(
            f"First-turn grew by {delta} tokens since last wiki health. Disclose the grown file. Done: first-turn delta is 0 or down."
        )

    return {
        "encoding": enc,
        "first_turn": {"total_tokens": first_total, "files": files},
        "skills": skills[:15],
        "skills_total": len(skills),
        "eval_coverage": {"with": with_evals, "without": without_evals},
        "efficiency": {
            "first_turn_tokens": first_total,
            "previous_first_turn_tokens": previous,
            "delta_tokens": delta,
            "trend": trend,
        },
        "act": act,
    }


def build_health_snapshot(
    *,
    status: str,
    pages: int,
    bytes: int,
    tokens: int | None,
    lint: Mapping[str, Any],
    waste: Mapping[str, Any] | None,
    staging: Mapping[str, Any] | None,
    remorph: Mapping[str, Any] | None,
    policy: Mapping[str, Any] | None,
    trends: Mapping[str, Any] | None,
    focus: Sequence[Mapping[str, Any]] | None = None,
    context: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Assemble the compact path-scoped health snapshot."""
    compact_lint = _compact_lint(lint)
    focus_rows = [
        {
            "path": str(item["path"]),
            "reason": str(item["reason"]),
            "source": str(item["source"]),
            "action": str(item.get("action") or _focus_action(str(item["source"]), str(item["path"]), str(item["reason"]))),
        }
        for item in (focus or ())
        if isinstance(item, Mapping) and {"path", "reason", "source"}.issubset(item)
    ][:5]
    snapshot: dict[str, Any] = {
        "status": _status(status, compact_lint),
        "pages": _int(pages),
        "bytes": _int(bytes),
        "tokens": None if tokens is None else _int(tokens),
        "lint": compact_lint,
        "waste": _layer_object(waste, ("hits", "hard_hits")),
        "staging": _layer_object(staging, ("leftover_count",)),
        "remorph": _layer_object(remorph, ("plan_count", "skip_count", "error_count")),
        "policy": _layer_object(policy, ("ok", "conflict_count")),
        "trends": _clone(trends) if isinstance(trends, Mapping) else build_trends(None, None, None),
        "focus": focus_rows,
        "next": _clone(focus_rows[0]) if focus_rows else None,
        "context": _clone(context) if isinstance(context, Mapping) else {
            "encoding": "cl100k_base",
            "first_turn": {"total_tokens": 0, "files": []},
            "skills": [],
            "skills_total": 0,
            "efficiency": {
                "first_turn_tokens": 0,
                "previous_first_turn_tokens": None,
                "delta_tokens": None,
                "trend": "new",
            },
            "act": [],
        },
    }
    if isinstance(lint.get("identity"), Mapping):
        snapshot["identity"] = _clone(lint["identity"])
    return snapshot
