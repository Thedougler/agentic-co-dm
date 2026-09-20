"""Compact lint worklist aggregation for the public wiki CLI."""
from __future__ import annotations

from collections.abc import Iterable, Mapping
from pathlib import Path, PurePosixPath
from typing import Any

# Structural lint's hard rules. Callers may pass a narrower/current set.
DEFAULT_HARD_KEYS = frozenset(
    {
        "broken_links",
        "missing_frontmatter",
        "bad_type",
        "bad_lifecycle",
        "typed_relationships",
        "pc_identity_mismatch",
        "misplaced_entity",
        "spaced_basename",
        "noncanonical_basename",
        "aruhe_prefix_basename",
        "illegal_basename",
        "duplicate_stems",
        "duplicate_slugs",
        "redirect_stubs",
        "template_conformance",
    }
)


def _path(value: Any, vault: str | Path | None = None) -> str:
    """Return a stable vault-relative spelling without resolving owners."""
    text = str(value or "").replace("\\", "/")
    if not text:
        return ""
    if vault and Path(text).is_absolute():
        try:
            text = Path(text).resolve().relative_to(Path(vault).expanduser().resolve()).as_posix()
        except ValueError:
            pass
    if text.startswith("./"):
        text = text[2:]
    if not text.startswith("/"):
        text = PurePosixPath(text).as_posix()
    return text


def _line(value: Any) -> int:
    try:
        number = int(value)
    except (TypeError, ValueError):
        return 1
    return max(1, number)


def normalize_finding(
    finding: Mapping[str, Any],
    *,
    rule: str | None = None,
    vault: str | Path | None = None,
) -> dict[str, Any]:
    """Normalize one checker record to the public flat finding shape."""
    name = str(finding.get("rule") or rule or "")
    file_name = finding.get("file", finding.get("page", finding.get("path", "")))
    severity = finding.get("severity")
    if severity is None:
        severity = "error" if name in DEFAULT_HARD_KEYS else "warn"
    message = finding.get("message")
    if message is None:
        message = finding.get("reason", finding.get("issue", ""))
    result = {
        "rule": name,
        "file": _path(file_name, vault),
        "line": _line(finding.get("line", 1)),
        "severity": str(severity),
        "message": str(message),
    }
    for key in (
        "evidence", "action", "owner", "code", "source",
        "repair_class", "repair_action", "repair_target", "target", "reason",
    ):
        value = finding.get(key)
        if value not in (None, ""):
            result[key] = value
    return result


def _is_record(value: Mapping[str, Any]) -> bool:
    return any(key in value for key in ("rule", "file", "page", "path", "line", "message", "target"))


def _records(value: Any, *, rule: str | None = None, vault: str | Path | None = None) -> Iterable[dict[str, Any]]:
    if isinstance(value, Mapping):
        if _is_record(value):
            normalized = normalize_finding(value, rule=rule, vault=vault)
            for key in ("target", "value", "token", "id"):
                if value.get(key) not in (None, ""):
                    normalized["_target"] = str(value[key])
                    break
            yield normalized
            return
        # A lint result may be passed directly; its nested findings are the input.
        if set(value) & {"findings", "findings_by_file"} and not rule:
            for key in ("findings", "findings_by_file"):
                if key in value:
                    yield from _records(value[key], vault=vault)
            return
        if not rule and set(value) <= {"status", "counts", "hard_fail", "cache", "scope", "files_checked"}:
            return
        for name, child in value.items():
            yield from _records(child, rule=str(name) if rule is None else rule, vault=vault)
        return
    if isinstance(value, (str, Path)):
        yield normalize_finding({"page": value}, rule=rule, vault=vault)
        return
    if isinstance(value, Iterable) and not isinstance(value, (bytes, bytearray)):
        for child in value:
            yield from _records(child, rule=rule, vault=vault)


def _target(finding: Mapping[str, Any]) -> str:
    if finding.get("_target") not in (None, ""):
        return str(finding["_target"])
    return str(finding.get("file") or "")


def _bytes_by_page(page_bytes: Mapping[Any, Any] | None, vault: str | Path | None) -> dict[str, int]:
    result: dict[str, int] = {}
    for page, value in (page_bytes or {}).items():
        try:
            size = max(0, int(value))
        except (TypeError, ValueError):
            size = 0
        result[_path(page, vault)] = size
    return result


def _scope(scope: Mapping[str, Any] | Iterable[Any] | None, vault: str | Path | None) -> dict[str, list[str]]:
    if isinstance(scope, Mapping):
        values = scope.get("paths", [])
    else:
        values = scope or []
    if isinstance(values, (str, Path)):
        values = [values]
    return {"paths": sorted({_path(value, vault) for value in values if _path(value, vault)})}


def _cache(cache: Mapping[str, Any] | None) -> dict[str, int]:
    cache = cache or {}
    return {
        key: max(0, int(cache.get(key, 0) or 0))
        for key in ("hits", "misses", "vale_skipped")
    }


def build_worklist(
    findings: Any,
    *,
    files_checked: int = 0,
    scope: Mapping[str, Any] | Iterable[Any] | None = None,
    cache: Mapping[str, Any] | None = None,
    hard_keys: Iterable[str] | None = None,
    include_findings: bool = False,
    full: bool = True,
    vault: str | Path | None = None,
    page_bytes: Mapping[Any, Any] | None = None,
    file_order: Iterable[str] | None = None,
) -> dict[str, Any]:
    """Build the complete lint worklist with aggregate and file findings."""
    flat = list(_records(findings, vault=vault))
    counts: dict[str, int] = {}
    targets: dict[str, set[str]] = {}
    pages: dict[str, int] = {}
    grouped: dict[str, list[dict[str, Any]]] = {}
    first_seen: list[str] = []
    for item in flat:
        rule = item["rule"]
        if not rule:
            continue
        counts[rule] = counts.get(rule, 0) + 1
        targets.setdefault(rule, set()).add(_target(item))
        page = item["file"]
        if page:
            pages[page] = pages.get(page, 0) + 1
            if page not in grouped:
                grouped[page] = []
                first_seen.append(page)
            grouped_item = {
                key: item[key]
                for key in ("rule", "file", "line", "severity", "message")
                if key in item
            }
            for key in (
                "evidence", "action", "owner", "code", "source",
                "repair_class", "repair_action", "repair_target", "target", "reason",
            ):
                if key in item:
                    grouped_item[key] = item[key]
            grouped[page].append(grouped_item)

    counts = {key: counts[key] for key in sorted(counts) if counts[key]}
    unique = {
        key: sorted(target for target in targets.get(key, set()) if target)
        for key in counts
    }
    sizes = _bytes_by_page(page_bytes, vault)
    backlog = [
        {"page": page, "findings": number, "bytes": sizes.get(page, 0)}
        for page, number in pages.items()
    ]
    backlog.sort(key=lambda item: (item["bytes"], item["page"]))
    next_item = backlog[0] if backlog else None
    hard = set(hard_keys) if hard_keys is not None else DEFAULT_HARD_KEYS
    order = list(file_order) if file_order is not None else []
    ordered_files: list[str] = []
    for page in order + first_seen:
        page = _path(page, vault)
        if page in grouped and page not in ordered_files:
            ordered_files.append(page)

    result: dict[str, Any] = {
        "status": "findings" if counts else "clean",
        "counts": counts,
        "hard_fail": any(rule in hard for rule in counts),
        "finding_total": sum(counts.values()),
        "affected_pages": len(pages),
        "next_page": next_item["page"] if next_item else None,
        "next": (
            {
                "path": next_item["page"],
                "findings": next_item["findings"],
                "bytes": next_item["bytes"],
                "action": (
                    f"Run wiki lint fix {next_item['page']}, rerun the affected scope, "
                    f"then use wiki lint {next_item['page']} for remaining findings."
                ),
            }
            if next_item
            else None
        ),
        "cache": _cache(cache),
        "files_checked": max(0, int(files_checked or 0)),
        "scope": _scope(scope, vault),
    }
    if include_findings or full:
        result.update({
            "unique": unique,
            "backlog": backlog,
            "files": [{"file": page, "findings": grouped[page]} for page in ordered_files],
        })
    return result


# A descriptive alias keeps integrations readable without a second implementation.
aggregate_worklist = build_worklist

__all__ = [
    "DEFAULT_HARD_KEYS",
    "aggregate_worklist",
    "build_worklist",
    "normalize_finding",
]
