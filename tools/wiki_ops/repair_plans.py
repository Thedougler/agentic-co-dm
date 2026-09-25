"""Build approval plans and execute only registered safe lint fixers."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Callable, Iterable
from .mutations import MutationOp, apply_mutation, section_hash
from .transactions import Transaction, qmd_hook_runner


def _action_name(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        name = value.get("kind") or value.get("action") or value.get("name")
        return name if isinstance(name, str) else None
    return None


ALLOWED_ACTIONS = frozenset({"delete_redirect_stub", "repair_links", "replace_index_entry", "update_manifest_identity"})


def snapshot(vault: str | Path, files: list[str] | None = None) -> str:
    root = Path(vault).resolve()
    selected = files or sorted(path.relative_to(root).as_posix() for path in root.rglob("*.md") if path.is_file())
    digest = hashlib.sha256()
    for relative in selected:
        path = root / relative
        digest.update(relative.encode())
        if path.is_file():
            digest.update(path.read_bytes())
    return "sha256:" + digest.hexdigest()


def build_plan(vault: str | Path, findings: dict[str, Any], *, scope: dict[str, Any] | None = None) -> dict[str, Any]:
    actions: list[dict[str, Any]] = []
    groups = (findings.get("findings", findings) or {}).values() if isinstance(findings, dict) else []
    for group in groups:
        for finding in group:
            if not isinstance(finding, dict) or finding.get("repair_class") != "deterministic_repair":
                continue
            action = _action_name(finding.get("repair_action") or finding.get("action"))
            if not action or action not in ALLOWED_ACTIONS:
                continue
            target = finding.get("file") or finding.get("page")
            if not target:
                continue
            actions.append({"action": action, "target": str(target), "expected": finding.get("target")})
    actions.sort(key=lambda item: (item["target"], item["action"]))
    files = sorted({item["target"] for item in actions})
    return {
        "version": 1,
        "vault": str(Path(vault).resolve()),
        "scope": scope or {},
        "snapshot": snapshot(vault, files),
        "actions": actions,
        "requires_approval": True,
        "approved": False,
        "human_only": 0,
    }


def plan_json(plan: dict[str, Any]) -> str:
    return json.dumps(plan, sort_keys=True, separators=(",", ":"))


def _scope_paths(scope: dict[str, Any] | None) -> set[str]:
    values = (scope or {}).get("paths", ())
    return {str(value).replace("\\", "/") for value in values if value}


def _in_scope(target: str, scope: set[str]) -> bool:
    if not scope:
        return True
    return target in scope


def _record_skip(finding: dict[str, Any], reason: str) -> dict[str, str]:
    return {
        "rule": str(finding.get("rule") or "unknown"),
        "action": str(_action_name(finding.get("repair_action") or finding.get("action")) or ""),
        "target": str(finding.get("file") or finding.get("page") or ""),
        "reason": reason,
    }


def _delete_redirect_op(vault: Path, finding: dict[str, Any]) -> tuple[MutationOp | None, str | None]:
    target = str(finding.get("file") or finding.get("page") or "").replace("\\", "/")
    if not target:
        return None, "missing_target"
    path = vault / target
    if not path.is_file():
        return None, "target_missing"
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return None, "target_unreadable"
    if "redirects_to:" not in text:
        return None, "redirect_precondition_failed"
    return MutationOp("delete_file", target, selector={"content_hash": section_hash(text)}), None


def _escape_table_pipe_op(vault: Path, finding: dict[str, Any]) -> tuple[MutationOp | None, str | None]:
    target = str(finding.get("file") or finding.get("page") or "").replace("\\", "/")
    path = vault / target
    if not target or not path.is_file():
        return None, "target_missing"
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return None, "target_unreadable"
    return MutationOp("escape_table_wikilink_pipes", target, selector={"content_hash": section_hash(text)}), None


def _rename_page_op(vault: Path, finding: dict[str, Any]) -> tuple[MutationOp | None, str | None]:
    """noncanonical_basename: rename to the lowercase kebab basename lint computed, rewriting backlinks."""
    action = finding.get("repair_action") if isinstance(finding.get("repair_action"), dict) else {}
    source, target = str(action.get("from") or ""), str(action.get("to") or "")
    path = vault / source
    if not source or not target or not path.is_file():
        return None, "target_missing"
    if (vault / target).exists() and not (vault / target).samefile(path):
        return None, "target_exists"
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return None, "target_unreadable"
    return MutationOp("rename_page", source, selector={"content_hash": section_hash(text)},
                      payload={"new_target": target, "rewrite_backlinks": True}), None


_FIXERS: dict[str, Callable[[Path, dict[str, Any]], tuple[MutationOp | None, str | None]]] = {
    "delete_redirect_stub": _delete_redirect_op,
    "escape_table_wikilink_pipe": _escape_table_pipe_op,
    "rename_page": _rename_page_op,
}
_APPLIED_RULE = {
    "delete_file": ("TMPL_redirect_stub", "delete_redirect_stub"),
    "escape_table_wikilink_pipes": ("table_wikilink_unescaped_pipe", "escape_table_wikilink_pipe"),
    "rename_page": ("noncanonical_basename", "rename_page"),
}


def build_safe_fix_plan(
    vault: str | Path,
    findings: Iterable[dict[str, Any]],
    *,
    scope: dict[str, Any] | None = None,
) -> tuple[list[MutationOp], list[dict[str, str]]]:
    """Turn eligible findings into scope-safe, hash-preconditioned operations."""
    root = Path(vault).resolve()
    selected = _scope_paths(scope)
    operations: list[MutationOp] = []
    skipped: list[dict[str, str]] = []
    for finding in findings:
        if not isinstance(finding, dict) or finding.get("repair_class") != "deterministic_repair":
            continue
        action = _action_name(finding.get("repair_action") or finding.get("action"))
        target = str(finding.get("file") or finding.get("page") or "").replace("\\", "/")
        if not action or action not in _FIXERS:
            skipped.append(_record_skip(finding, "unsupported"))
            continue
        if not _in_scope(target, selected):
            skipped.append(_record_skip(finding, "outside_scope"))
            continue
        operation, reason = _FIXERS[action](root, finding)
        if operation is None:
            skipped.append(_record_skip(finding, reason or "precondition_failed"))
        elif operation not in operations:
            operations.append(operation)
    return operations, skipped


def apply_safe_fix_plan(vault: str | Path, operations: list[MutationOp]) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    """Apply single-file repairs as one atomic batch, then each rename on its own (a rename spans backlinks)."""
    renames = [operation for operation in operations if operation.kind == "rename_page"]
    applied, skipped = _apply_batch(vault, [operation for operation in operations if operation.kind != "rename_page"])
    for operation in renames:
        result = apply_mutation(vault, operation)
        if result.get("accepted") and result.get("changed"):
            applied.append({"rule": "noncanonical_basename", "action": "rename_page", "target": operation.target,
                            "status": "applied", "changed_files": list(result.get("changed_files") or [])})
        elif not result.get("accepted"):
            skipped.append({"target": operation.target, "reason": str(result.get("error") or "mutation_failed")})
    refresh = qmd_hook_runner(Path(vault).resolve()) if applied else None
    if refresh is not None:  # changed pages are searchable again before the repair phase reads them
        refresh()
    return applied, skipped


def _apply_batch(vault: str | Path, operations: list[MutationOp]) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    if not operations:
        return [], []
    transaction = Transaction(vault)
    for operation in operations:
        transaction.add(operation)
    validation = transaction.validate()
    if not validation.valid:
        return [], [{"target": operation.target, "reason": "atomic_precondition_failed"} for operation in operations]
    result = transaction.commit()
    if result.get("status") not in {"committed", "finalized"}:
        reason = str(result.get("error") or "mutation_failed")
        return [], [{"target": operation.target, "reason": reason} for operation in operations]
    changed_files = sorted({str(path) for path in result.get("files_changed", [])})
    return [
        {
            "rule": _APPLIED_RULE[operation.kind][0],
            "action": _APPLIED_RULE[operation.kind][1],
            "target": operation.target,
            "status": "applied",
            "changed_files": [operation.target] if operation.target in changed_files else changed_files,
        }
        for operation in operations
    ], []
