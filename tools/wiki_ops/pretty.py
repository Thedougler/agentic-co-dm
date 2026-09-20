"""Deterministic human-readable renderers for the wiki CLI."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any


def _value(data: Mapping[str, Any], key: str, default: Any = "") -> Any:
    value = data.get(key, default)
    return default if value is None else value


def render_lint(result: Mapping[str, Any]) -> str:
    """Render complete lint and lint-fix results."""
    if "applied" in result:
        applied = _value(result, "applied", ())
        skipped = _value(result, "skipped", ())
        changed = _value(result, "changed_files", ())
        remaining = _value(result, "remaining", {})
        lines = [
            "Lint fix: " + str(_value(result, "status", "unknown")),
            f"Applied: {len(applied)}",
            f"Skipped: {len(skipped)}",
            f"Remaining: {_value(remaining, 'finding_total', 0)}",
            "Changed files: " + (", ".join(str(path) for path in changed) or "none"),
        ]
        lines.extend(_render_findings(remaining))
        return "\n".join(lines)
    counts = _value(result, "counts", {})
    cache = _value(result, "cache", {})
    ledger = _value(result, "ledger", {})
    next_item = _value(result, "next", {}) or {}
    lines = [
        "Lint: " + str(_value(result, "status", "unknown")),
        "Counts: " + (" ".join(f"{k}={counts[k]}" for k in sorted(counts)) or "none"),
        f"Findings: {_value(result, 'finding_total', 0)} on {_value(result, 'affected_pages', 0)} pages",
        f"Next page: {_value(result, 'next_page', None) or 'none'}",
        "Next action: " + str(_value(next_item, "action", "none") or "none"),
        "Cache: " + " ".join(
            f"{key}={_value(cache, key, 0)}" for key in ("hits", "misses", "vale_skipped")
        ),
    ]
    if int(_value(ledger, "open", 0) or 0):
        ids = _value(ledger, "ids", ())
        lines.append("Ledger: " + (" ".join(str(item) for item in ids) or str(_value(ledger, "open"))))
    lines.extend(_render_findings(result))
    return "\n".join(lines)


def _render_findings(result: Mapping[str, Any]) -> list[str]:
    groups = _value(result, "files", ())
    if not groups:
        groups = ({"file": _value(finding, "file", ""), "findings": (finding,)} for finding in _value(result, "findings", ()))
    findings = []
    for group in groups:
        group_file = str(_value(group, "file", ""))
        for finding in _value(group, "findings", ()):
            file = str(_value(finding, "file", group_file))
            line = _value(finding, "line", "")
            rule = str(_value(finding, "rule", ""))
            message = str(_value(finding, "message", ""))
            findings.append(f"{file}:{line}  {rule}  {message}")
    return ["", *findings] if findings else []


def render_query(result: Mapping[str, Any]) -> str:
    """Render query hits, one compact record per line."""
    hits = _value(result, "hits", ())
    return "\n".join(
        f"{_value(hit, 'path', '')}  {_value(hit, 'title', '')}  {_value(hit, 'id', '')}" for hit in hits
    )


def render_health(result: Mapping[str, Any]) -> str:
    """Render the short health scoreboard, context act, and ordered focus queue."""
    lint = _value(result, "lint", {})
    lint_counts = _value(lint, "counts", {})
    hard = sum(v for k, v in lint_counts.items() if str(k).lower() in {"hard", "error"})
    if not hard:
        hard_value = _value(lint, "hard_fail", 0)
        hard = sum(hard_value.values()) if isinstance(hard_value, Mapping) else int(hard_value or 0)
    trends = _value(result, "trends", {})
    slowest = _value(trends, "slowest_commands", ())
    heaviest = _value(trends, "token_heaviest", ())
    context = _value(result, "context", {})
    first_turn = _value(context, "first_turn", {})
    lines = [
        "Health: " + str(_value(result, "status", "unknown")),
        "Metrics: " + " ".join(
            f"{key}={_value(result, key, 'n/a')}" for key in ("pages", "bytes", "tokens")
        ) + f" lint_hard={hard}",
        f"First-turn: {_value(first_turn, 'total_tokens', 0)} tokens",
        f"Slowest: {slowest[0] if slowest else 'none'}",
        f"Token-heaviest: {heaviest[0] if heaviest else 'none'}",
    ]
    for row in _value(first_turn, "files", ()):
        lines.append(f"  {_value(row, 'path', '')}  {_value(row, 'tokens', 0)}")
    skills = _value(context, "skills", ())
    coverage = _value(context, "eval_coverage", {})
    if skills:
        lines.append(
            "Skills: "
            f"with={_value(coverage, 'with', 0)} without={_value(coverage, 'without', 0)}"
        )
        lines.extend(
            f"  {_value(row, 'name', '')}  {_value(row, 'tokens', 0)}  {_value(row, 'coverage', '')}  evals={_value(row, 'evals', 0)}  criteria={_value(row, 'criteria', 0)}"
            for row in skills[:10]
        )
    act = _value(context, "act", ())
    if act:
        lines.append("Act:")
        lines.extend(f"- {step}" for step in act)
    nxt = _value(result, "next", None)
    lines.append("Next: " + (str(_value(nxt, "path", "")) if isinstance(nxt, Mapping) else (str(nxt) if nxt else "none")))
    focus = _value(result, "focus", ())
    if focus:
        lines.append("Focus:")
        lines.extend(f"{_value(item, 'path', '')}  {_value(item, 'source', '')}  {_value(item, 'reason', '')}" for item in focus)
    return "\n".join(lines)




def render_usage_error(message: str) -> str:
    """Return the single stderr-ready line used for pretty usage failures."""
    return f"error: {message}".replace("\n", " ")


render_lint_pretty = render_lint
render_query_pretty = render_query
render_health_pretty = render_health
