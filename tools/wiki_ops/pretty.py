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


def _issue_rows(result: Mapping[str, Any]):
    """Yield (file, line, rule, message, finding) from a lint result."""
    groups = _value(result, "files", ())
    if groups:
        for group in groups:
            if not isinstance(group, Mapping):
                continue
            group_file = str(_value(group, "file", ""))
            for finding in _value(group, "findings", ()):
                if isinstance(finding, Mapping):
                    yield from _rows_for_finding(finding, str(_value(finding, "rule", "")), group_file)
        return
    findings = _value(result, "findings", {})
    if isinstance(findings, Mapping) and findings:
        for rule, items in findings.items():
            for finding in _flatten_finding_items(items):
                yield from _rows_for_finding(finding, str(rule), "")
        return
    by_file = _value(result, "findings_by_file", {})
    if isinstance(by_file, Mapping):
        for filename, items in by_file.items():
            for finding in items if isinstance(items, (list, tuple)) else ():
                if isinstance(finding, Mapping):
                    yield from _rows_for_finding(
                        finding, str(_value(finding, "rule", "")), str(filename),
                    )


_LOCATION_KEYS = {"file", "page", "path", "line", "lines", "rule"}
_META_KEYS = {"severity", "level", "repair_class", "repair_action", "repair_target", "message", "reason"}


def _fmt_value(value: Any) -> str:
    if isinstance(value, list) and all(not isinstance(item, (dict, list)) for item in value):
        return ",".join(str(item) for item in value)
    return str(value)


def _issue_message(finding: Mapping[str, Any]) -> str:
    parts: list[str] = []
    primary = _value(finding, "message", "") or _value(finding, "reason", "") or _value(finding, "target", "")
    if primary:
        parts.append(str(primary))
    pages = finding.get("pages")
    skip_pages = isinstance(pages, list) and pages and isinstance(pages[0], str)
    for key, value in finding.items():
        if key in _LOCATION_KEYS or key in _META_KEYS:
            continue
        if key == "target" and primary:
            continue
        if key == "pages" and skip_pages:
            continue
        if value in (None, "", [], {}):
            continue
        parts.append(f"{key}={_fmt_value(value)}")
    return " ".join(parts)


def _rows_for_finding(finding: Mapping[str, Any], rule: str, default_file: str):
    name = str(_value(finding, "rule", rule) or rule)
    message = _issue_message(finding)
    pages = finding.get("pages")
    lines = finding.get("lines")
    if isinstance(pages, list) and pages and isinstance(pages[0], str):
        line_list = lines if isinstance(lines, list) else []
        for index, page in enumerate(pages):
            line = line_list[index] if index < len(line_list) else _value(finding, "line", 1)
            yield str(page), line, name, message, finding
        return
    file = str(_value(finding, "file", "") or _value(finding, "page", "") or default_file)
    line = _value(finding, "line", 1)
    yield file, line, name, message, finding


def _flatten_finding_items(value: Any) -> list[Mapping[str, Any]]:
    if isinstance(value, Mapping):
        if any(key in value for key in ("line", "page", "file", "rule", "message", "target", "reason", "pages", "lines")):
            return [value]
        rows: list[Mapping[str, Any]] = []
        for child in value.values():
            rows.extend(_flatten_finding_items(child))
        return rows
    if isinstance(value, (list, tuple)):
        rows = []
        for item in value:
            if isinstance(item, Mapping):
                rows.extend(_flatten_finding_items(item))
            else:
                rows.append({"message": str(item)})
        return rows
    return [{"message": str(value)}] if value not in (None, "") else []


def _fix_hint(finding: Mapping[str, Any], file: str) -> str:
    repair_class = str(_value(finding, "repair_class", ""))
    action = finding.get("repair_action") if isinstance(finding, Mapping) else None
    if repair_class == "deterministic_repair" or (isinstance(action, Mapping) and action.get("kind")):
        return f"wiki lint fix {file}" if file else "wiki lint fix"
    target = _value(finding, "repair_target", "")
    if target:
        return str(target)
    return ""



def render_lint_issues(result: Mapping[str, Any]) -> str:
    """Agent-default lint stdout: file:line: rule: message, plus a fix hint."""
    rows = list(_issue_rows(result))
    if not rows:
        return "clean"
    lines = []
    for file, line, rule, message, finding in rows:
        text = f"{file}:{line}: {rule}: {message}".rstrip(": ")
        hint = _fix_hint(finding, file)
        if hint:
            text += f"\n  fix: {hint}"
        lines.append(text)
    nxt = _value(result, "next", None)
    if isinstance(nxt, Mapping) and nxt.get("path"):
        lines.append(f"next: {nxt['path']}")
    return "\n".join(lines)


def render_lint_fix(result: Mapping[str, Any]) -> str:
    """Default lint-fix stdout: remaining issues, or a dry-run plan."""
    status = str(result.get("status") or "")
    if status == "planned":
        lines = [
            f"planned: {op.get('kind', '')} {op.get('target', '')}".rstrip()
            for op in result.get("planned") or []
            if isinstance(op, Mapping)
        ] or ["already_done"]
        nxt = result.get("next")
        if isinstance(nxt, Mapping) and nxt.get("path"):
            lines.append(f"next: {nxt['path']}")
        return "\n".join(lines)
    remaining = result.get("remaining")
    if isinstance(remaining, Mapping):
        return render_lint_issues(remaining)
    lines = [status or "already_done"]
    nxt = result.get("next")
    if isinstance(nxt, Mapping) and nxt.get("path"):
        lines.append(f"next: {nxt['path']}")
    return "\n".join(lines)






def render_query(result: Mapping[str, Any]) -> str:
    """Render query hits, one compact record per line."""
    hits = _value(result, "hits", ())
    return "\n".join(
        f"{_value(hit, 'path', '')}  {_value(hit, 'title', '')}  {_value(hit, 'id', '')}" for hit in hits
    )


def render_health(result: Mapping[str, Any]) -> str:
    """Default health stdout: finding counts and a copy-pasteable next command."""
    lint = _value(result, "lint", {})
    if not isinstance(lint, Mapping):
        lint = {}
    total = _value(lint, "finding_total", _value(result, "finding_total", 0))
    pages = _value(lint, "affected_pages", _value(result, "affected_pages", 0))
    nxt = _value(result, "next", None)
    if not total and not (isinstance(nxt, Mapping) and nxt.get("path")):
        return "clean"
    lines = [f"{total} findings on {pages} pages"]
    waste = _value(result, "waste", {})
    if isinstance(waste, Mapping) and _value(waste, "hits", 0):
        lines.append(f"waste hits={_value(waste, 'hits', 0)} hard_hits={_value(waste, 'hard_hits', 0)}")
    staging = _value(result, "staging", {})
    if isinstance(staging, Mapping) and _value(staging, "leftover_count", 0):
        lines.append(f"staging leftover_count={_value(staging, 'leftover_count', 0)}")
    remorph = _value(result, "remorph", {})
    if isinstance(remorph, Mapping) and _value(remorph, "plan_count", 0):
        lines.append(
            f"remorph plan_count={_value(remorph, 'plan_count', 0)} "
            f"error_count={_value(remorph, 'error_count', 0)}"
        )
    if isinstance(nxt, Mapping) and nxt.get("path"):
        lines.append(f"next: {nxt['path']}")
        action = nxt.get("action")
        if action:
            lines.append(f"  {action}")
    return "\n".join(lines)





def render_usage_error(message: str) -> str:
    """Return the single stderr-ready line used for pretty usage failures."""
    return f"error: {message}".replace("\n", " ")


render_lint_pretty = render_lint
render_query_pretty = render_query
render_health_pretty = render_health
