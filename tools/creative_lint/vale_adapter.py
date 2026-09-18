"""Invoke Vale and map its JSON output to the finding contract."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any

from .finding import Finding
from .registry import Registry

ROOT = Path(__file__).resolve().parents[2]


def _relative_file(value: str | Path, root: Path) -> str:
    path = Path(value)
    if path.is_absolute():
        try:
            return path.resolve().relative_to(root.resolve()).as_posix()
        except ValueError:
            return path.as_posix()
    return path.as_posix()


def map_vale_output(payload: dict[str, Any], registry: Registry, *, root: Path | None = None,
                    severity_overrides: dict[str, str] | None = None) -> list[Finding]:
    root = root or ROOT
    findings: list[Finding] = []
    for filename, alerts in (payload or {}).items():
        if not isinstance(alerts, list):
            continue
        for alert in alerts:
            if not isinstance(alert, dict):
                continue
            check = str(alert.get("Check", ""))
            if not check:
                continue
            is_custom = not check.startswith("CoDM.")
            lookup_id = check.removeprefix("CoDM.").split(".")[-1]
            try:
                rule = registry.get(lookup_id)
            except KeyError:
                rule = None
            if rule is None and not is_custom:
                continue
            span = alert.get("Span") or []
            location: dict[str, Any] = {
                "file": _relative_file(filename, root),
                "line": max(1, int(alert.get("Line", 1) or 1)),
            }
            if len(span) >= 1:
                location["col"] = max(1, int(span[0]))
            if len(span) >= 2:
                location["end_col"] = max(1, int(span[1]))
            if alert.get("Match") is not None:
                location["text"] = str(alert["Match"])
            message = str(alert.get("Message") or alert.get("Match") or (rule.message if rule else check))
            action_kind = "delete_section" if check.casefold().startswith("deprecated.") else "replace_section"
            findings.append(Finding(
                rule_id=f"VALE_{check}" if is_custom else lookup_id,
                result="fail",
                severity=(severity_overrides or {}).get(lookup_id, "REPAIR" if is_custom else rule.severity),
                location=location,
                evidence=message,
                reason=rule.message if rule else message,
                repair_target=rule.repair if rule else message,
                evaluator="vale",
                repair_class="deterministic_repair" if is_custom else getattr(rule, "repair_class", "diagnostic"),
                repair_action=(
                    {"kind": action_kind, "target": location["file"], "selector": {"line": location["line"]}}
                    if is_custom else None
                ),
            ))
    return findings


def _resolve_vale(root: Path, executable: str) -> str | None:
    requested = Path(executable)
    if requested.is_absolute() or requested.parent != Path("."):
        return str(requested) if requested.is_file() and os.access(requested, os.X_OK) else None
    project_binary = root / ".venv" / "bin" / executable
    return str(project_binary) if project_binary.is_file() and os.access(project_binary, os.X_OK) else None


def _runtime_failure(files: list[Path], root: Path, reason: str) -> Finding:
    filename = _relative_file(files[0], root) if files else ""
    return Finding(
        rule_id="VALE_RUNTIME",
        result="fail",
        severity="BLOCK",
        location={"file": filename, "line": 1},
        evidence=reason,
        reason=reason,
        evaluator="vale",
    )


def run_vale(files: list[Path], registry: Registry, *, root: Path | None = None,
             vault: Path | None = None, severity_overrides: dict[str, str] | None = None,
             executable: str = "vale") -> tuple[list[Finding], list[str]]:
    root = (root or ROOT).resolve()
    if not files:
        return [], []
    warnings: list[str] = []
    try:
        from .vale_vocab import refresh_vocab
        refresh_vocab(root, (vault or root / "wiki").resolve())
    except (OSError, ValueError) as exc:
        reason = f"Vale proper-noun vocabulary refresh failed: {exc}"
        return [_runtime_failure(files, root, reason)], [reason]
    binary = _resolve_vale(root, executable)
    if not binary:
        reason = f"Project-local Vale is not installed at {root / '.venv' / 'bin' / executable}; run uv sync"
        return [_runtime_failure(files, root, reason)], [reason]
    command = [
        binary, "--output=JSON",
        f"--config={root / '.vale.ini'}",
        *[_relative_file(p, root) for p in files],
    ]
    proc = subprocess.run(command, cwd=root, capture_output=True, text=True, env=os.environ.copy())
    if proc.stderr.strip():
        warnings.append(proc.stderr.strip())
    if proc.returncode not in (0, 1):
        reason = f"Vale exited {proc.returncode}"
        warnings.append(reason)
        return [_runtime_failure(files, root, reason)], warnings
    if not proc.stdout.strip():
        reason = "Vale returned no JSON output"
        warnings.append(reason)
        return [_runtime_failure(files, root, reason)], warnings
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        reason = f"Vale returned invalid JSON: {exc}"
        warnings.append(reason)
        return [_runtime_failure(files, root, reason)], warnings
    if not isinstance(payload, dict):
        reason = "Vale returned a non-object JSON payload"
        warnings.append(reason)
        return [_runtime_failure(files, root, reason)], warnings
    return map_vale_output(payload, registry, root=root, severity_overrides=severity_overrides), warnings
