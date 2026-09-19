"""Deterministic human-readable renderers for the wiki CLI."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any


def _value(data: Mapping[str, Any], key: str, default: Any = "") -> Any:
    value = data.get(key, default)
    return default if value is None else value


def render_lint(result: Mapping[str, Any]) -> str:
    """Render a lint worklist without exposing its machine representation."""
    counts = _value(result, "counts", {})
    cache = _value(result, "cache", {})
    lines = [
        "Lint: " + str(_value(result, "status", "unknown")),
        "Counts: " + (" ".join(f"{k}={counts[k]}" for k in sorted(counts)) or "none"),
        f"Hard fail: {bool(_value(result, 'hard_fail', False))}",
        f"Next page: {_value(result, 'next_page', None) or 'none'}",
        "Cache: " + " ".join(f"{k}={cache[k]}" for k in ("hits", "misses", "vale_skipped") if k in cache),
    ]
    findings = _value(result, "findings", ())
    if findings:
        lines.append("")
        for finding in findings:
            file = str(_value(finding, "file", ""))
            line = _value(finding, "line", "")
            rule = str(_value(finding, "rule", ""))
            message = str(_value(finding, "message", ""))
            lines.append(f"{file}:{line}  {rule}  {message}")
    return "\n".join(lines)


def render_query(result: Mapping[str, Any]) -> str:
    """Render query hits, one compact record per line."""
    hits = _value(result, "hits", ())
    return "\n".join(
        f"{_value(hit, 'path', '')}  {_value(hit, 'title', '')}  {_value(hit, 'id', '')}" for hit in hits
    )


def render_health(result: Mapping[str, Any]) -> str:
    """Render the short health scoreboard and ordered focus queue."""
    lint = _value(result, "lint", {})
    lines = [
        "Health: " + str(_value(result, "status", "unknown")),
        "Metrics: " + " ".join(
            f"{key}={_value(result, key, 'n/a')}" for key in ("pages", "bytes", "tokens")
        ) + f" lint_hard={sum(_value(lint, 'counts', {}).get(k, 0) for k in ('hard', 'HARD', 'error', 'ERROR'))}",
    ]
    for section, label in (("waste", "waste"), ("staging", "staging"), ("remorph", "remorph"), ("policy", "policy")):
        values = _value(result, section, {})
        if values:
            lines.append(label + ": " + " ".join(f"{k}={values[k]}" for k in sorted(values)))
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
