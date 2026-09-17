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
            rule_id = check.removeprefix("CoDM.").split(".")[-1]
            try:
                rule = registry.get(rule_id)
            except KeyError:
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
            findings.append(Finding(
                rule_id=rule.id,
                result="fail",
                severity=(severity_overrides or {}).get(rule.id, rule.severity),
                location=location,
                evidence=str(alert.get("Message") or alert.get("Match") or rule.message),
                reason=rule.message,
                repair_target=rule.repair,
                evaluator="vale",
            ))
    return findings


def run_vale(files: list[Path], registry: Registry, *, root: Path | None = None,
             severity_overrides: dict[str, str] | None = None,
             executable: str = "vale") -> tuple[list[Finding], list[str]]:
    root = root or ROOT
    if not files:
        return [], []
    binary = shutil.which(executable)
    if not binary:
        return [], [f"Vale is not installed; skipped {len(files)} file(s)"]
    command = [binary, "--output=JSON", f"--config={root / '.vale.ini'}",
               *[_relative_file(p, root) for p in files]]
    env = os.environ.copy()
    proc = subprocess.run(command, cwd=root, capture_output=True, text=True, env=env)
    warnings = [proc.stderr.strip()] if proc.stderr.strip() else []
    if proc.returncode not in (0, 1):
        warnings.append(f"Vale exited {proc.returncode}")
    if not proc.stdout.strip():
        return [], warnings
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        warnings.append(f"Vale returned invalid JSON: {exc}")
        return [], warnings
    return map_vale_output(payload, registry, root=root, severity_overrides=severity_overrides), warnings
