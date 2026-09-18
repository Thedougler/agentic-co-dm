"""Build approval-gated repair plans from lint findings."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

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
            action = finding.get("repair_action") or finding.get("action")
            if action not in ALLOWED_ACTIONS:
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
