"""Invoke Vale and map its JSON output to the finding contract."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any


from .finding import Finding
from .registry import Registry

ROOT = Path(__file__).resolve().parents[2]
TIMING: dict[str, int] = {}
VALE_BATCH_SIZE = 100
VALE_MAX_WORKERS = 8
VALE_TIMEOUT_SECONDS = 60



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
            default_severity = "REPAIR" if is_custom else rule.severity if rule else "BLOCK"
            findings.append(Finding(
                rule_id=f"VALE_{check}" if is_custom else lookup_id,
                result="fail",
                severity=(severity_overrides or {}).get(lookup_id, default_severity),
                location=location,
                evidence=message,
                reason=rule.message if rule else message,
                repair_target=rule.repair if rule else message,
                evaluator="vale",
                # Repo-local styles (e.g. Deprecated.*) need an agent's call under wiki-lint:
                # removing or relocating the content has more than one correct output.
                repair_class="human_repair" if is_custom else getattr(rule, "repair_class", "diagnostic"),
                repair_action=None,
            ))
    return findings


def _resolve_vale(root: Path, executable: str) -> str | None:
    requested = Path(executable)
    if requested.is_absolute() or requested.parent != Path("."):
        return str(requested) if requested.is_file() and os.access(requested, os.X_OK) else None
    project_binary = root / ".venv" / "bin" / executable
    if project_binary.is_file() and os.access(project_binary, os.X_OK):
        return str(project_binary)
    return shutil.which(executable)


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



def _vale_json(
    binary: str, root: Path, files: list[Path], style: str | None
) -> tuple[subprocess.CompletedProcess[str], int]:
    command = [binary, "--output=JSON", f"--config={root / '.vale.ini'}"]
    if style:
        command.append(f'--filter=.Name matches "{style}.+"')
    command.extend(_relative_file(path, root) for path in files)
    started = time.monotonic()
    try:
        proc = subprocess.run(
            command,
            cwd=root,
            capture_output=True,
            text=True,
            env=os.environ.copy(),
            timeout=VALE_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode() if isinstance(exc.stdout, bytes) else exc.stdout or ""
        proc = subprocess.CompletedProcess(
            command,
            124,
            stdout,
            f"Vale timed out after {VALE_TIMEOUT_SECONDS}s",
        )
    except OSError as exc:
        proc = subprocess.CompletedProcess(command, 126, "", f"Vale could not run: {exc}")
    return proc, int((time.monotonic() - started) * 1000)


def run_vale(files: list[Path], registry: Registry, *, root: Path | None = None,
             vault: Path | None = None, severity_overrides: dict[str, str] | None = None,
             executable: str = "vale") -> tuple[list[Finding], list[str]]:
    global TIMING
    TIMING = {}
    root = (root or ROOT).resolve()
    if not files:
        return [], []
    if not (root / ".vale.ini").is_file():
        return [], []
    warnings: list[str] = []
    try:
        from .vale_vocab import refresh_vocab
        started = time.monotonic()
        refresh_vocab(root, (vault or root / "wiki").resolve())
        TIMING["tools/creative_lint/vale_vocab.py"] = int((time.monotonic() - started) * 1000)
    except (OSError, ValueError) as exc:
        reason = f"Vale proper-noun vocabulary refresh failed: {exc}"
        return [_runtime_failure(files, root, reason)], [reason]
    binary = _resolve_vale(root, executable)
    if not binary:
        reason = f"Vale is not installed at {root / '.venv' / 'bin' / executable} or on PATH"
        return [_runtime_failure(files, root, reason)], [reason]
    payloads: list[dict[str, Any]] = []
    runtime_failures: list[Finding] = []
    batches = [
        files[start:start + VALE_BATCH_SIZE]
        for start in range(0, len(files), VALE_BATCH_SIZE)
    ]
    started = time.monotonic()
    if len(batches) == 1:
        results = [_vale_json(binary, root, batches[0], None)]
    else:
        with ThreadPoolExecutor(max_workers=min(VALE_MAX_WORKERS, len(batches))) as pool:
            results = list(pool.map(lambda batch: _vale_json(binary, root, batch, None), batches))
    TIMING["vale"] = int((time.monotonic() - started) * 1000)

    merged: dict[str, list[Any]] = {}
    for batch, (proc, _) in zip(batches, results):
        if proc.stderr.strip():
            warnings.append(proc.stderr.strip())
        if proc.returncode not in (0, 1):
            reason = f"Vale exited {proc.returncode}"
            warnings.append(reason)
            runtime_failures.append(_runtime_failure(batch, root, reason))
            continue
        if not proc.stdout.strip():
            continue
        try:
            payload = json.loads(proc.stdout)
        except json.JSONDecodeError as exc:
            reason = f"Vale returned invalid JSON: {exc}"
            warnings.append(reason)
            runtime_failures.append(_runtime_failure(batch, root, reason))
            continue
        if isinstance(payload, dict):
            payloads.append(payload)

    for payload in payloads:
        for filename, alerts in payload.items():
            if isinstance(alerts, list):
                merged.setdefault(str(filename), []).extend(alerts)
    return runtime_failures + map_vale_output(
        merged, registry, root=root, severity_overrides=severity_overrides
    ), warnings

