"""Human and machine output helpers for creative lint CLI."""
from __future__ import annotations

from .engine import LintResult


def render_human(result: LintResult, *, command: str = "task") -> str:
    label = f"wiki-lint {command}"
    if result.bundle:
        label += f" {result.bundle}"
    lines = [f"{label}: {result.files_checked} files, {result.rules_evaluated} rules → {result.status}", ""]
    for finding in result.findings:
        if finding.result != "fail":
            continue
        location = finding.location
        target = str(location.get("file", ""))
        if location.get("line"):
            target += f":{location['line']}"
        lines.append(f"{finding.severity:<7} {finding.rule_id:<12} {target}  {finding.reason}")
        if location.get("text"):
            lines.append(f"         \"{location['text']}\"")
        lines.append(f"         Evidence: {finding.evidence}")
        if finding.repair_target:
            lines.append(f"         Repair: {finding.repair_target}")
        if finding.waiver:
            lines.append(f"         Waived: {finding.waiver.get('reason', '')}")
    summary = " ".join(f"{key}={result.summary.get(key, 0)}" for key in ("BLOCK", "REPAIR", "REVIEW", "WARN", "INFO"))
    lines.extend(["", f"Summary: {summary}"])
    if result.warnings:
        lines.append("Warnings: " + "; ".join(result.warnings))
    return "\n".join(lines)
