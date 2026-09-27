"""Compact lint worklist aggregation for the public wiki CLI."""
from __future__ import annotations

from collections.abc import Iterable, Mapping
from pathlib import Path, PurePosixPath
from typing import Any
from tools.wiki_ops.cli import repo_root
from tools.wiki_ops.owner_skills import owner_skill, strip_template_ref, template_ref
from tools.wiki_ops.pretty import _issue_message
from tools.wiki_ops.scope import _frontmatter
from tools.wiki_ops.template_contracts import template_for


# Structural lint's hard rules. Callers may pass a narrower/current set.
DEFAULT_HARD_KEYS = frozenset(
    {
        "broken_links",
        "missing_frontmatter",
        "bad_type",
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

_FINDING_EXTRAS = (
    "evidence", "action", "owner", "code", "source",
    "repair_class", "repair_action", "repair_target", "target", "reason", "missing",
)


def attach_finding_text(finding: Mapping[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    """Set message and copy optional repair/evidence keys onto a public finding."""
    message = finding.get("message") or finding.get("reason") or finding.get("issue") or finding.get("text") or ""
    result["message"] = str(message)
    if not result["message"].strip():
        result["message"] = _issue_message(finding) or str(result.get("rule") or "")
    for key in _FINDING_EXTRAS:
        value = finding.get(key)
        if value not in (None, ""):
            if key == "repair_target" and isinstance(value, str):
                value = strip_template_ref(value)
            result[key] = value
    return result



def is_moc_page(relative: str) -> bool:
    """Generated Map of Content pages are regenerated, not agent-repaired."""
    name = Path(relative).name
    return name == "_index.md" or name.endswith("-index.md")


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
    result = {
        "rule": name,
        "file": _path(file_name, vault),
        "line": _line(finding.get("line", 1)),
        "severity": str(severity),
    }
    return attach_finding_text(finding, result)


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


def _next_action(path: str, findings: list[dict[str, Any]]) -> str:
    if any(item.get("repair_class") == "deterministic_repair" for item in findings):
        return f"wiki lint fix {path}, then wiki lint {path}"
    return f"wiki lint {path}"


def _page_fields(vault: str | Path | None, page: str) -> dict[str, str]:
    if vault is None or not page:
        return {}
    path = Path(vault) / page
    try:
        return _frontmatter(path.read_text(encoding="utf-8"))
    except OSError:
        return {}


def _file_group(page: str, findings: list[dict[str, Any]], vault: str | Path | None) -> dict[str, Any]:
    entry: dict[str, Any] = {"file": page, "findings": findings}
    fields = _page_fields(vault, page)
    page_type = (fields.get("type") or "").strip()
    kind = (fields.get("kind") or "").strip()
    if page_type:
        entry["type"] = page_type
    skill = owner_skill(page_type, kind)
    if skill:
        entry["skill"] = skill
    chosen = None
    if page_type:
        if vault is not None:
            chosen = template_for(vault, page_type, kind)
        if chosen is None:
            chosen = template_for(repo_root(), page_type, kind)
    if chosen is not None:
        entry["template"] = template_ref(chosen.name)
    return entry


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
            for key in _FINDING_EXTRAS:
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
        if not is_moc_page(page)
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
                "action": _next_action(next_item["page"], grouped.get(next_item["page"], [])),
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
            "files": [_file_group(page, grouped[page], vault) for page in ordered_files],
            "findings": [item for page in ordered_files for item in grouped[page]],
        })
    return result


# A descriptive alias keeps integrations readable without a second implementation.
aggregate_worklist = build_worklist

__all__ = [
    "DEFAULT_HARD_KEYS",
    "aggregate_worklist",
    "attach_finding_text",
    "build_worklist",
    "is_moc_page",
    "normalize_finding",
]

