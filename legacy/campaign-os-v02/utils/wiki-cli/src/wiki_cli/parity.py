"""wiki-cli lint utilities.

Parity harness completed and signed off (PARITY-SIGNOFF.md, ADR-0045).
The npm lint engine functions have been removed; only wiki-cli lint
invocation remains for use by other tooling.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from wiki_cli.contracts import all_rules

Finding = tuple[str, str, int]
"""(rule_id, rel_path, line)."""

_WIKI_CLI_ROOT = Path(__file__).resolve().parents[2]


def ported_rules() -> set[str]:
    """All registered rule ids."""
    import wiki_cli.rules  # noqa: F401

    return {rule.id for rule in all_rules()}


def run_wiki_lint(path: Path) -> set[Finding]:
    """Shell wiki-cli's `--json` mode and parse its findings."""
    result = subprocess.run(
        ["uv", "run", "wiki", "lint", str(path.resolve()), "--json"],
        cwd=_WIKI_CLI_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        entries = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
    except json.JSONDecodeError as error:
        if result.returncode not in (0, 1):
            raise RuntimeError(
                f"wiki lint failed (exit {result.returncode}) on {path} and printed "
                f"unparseable stdout.\n"
                f"stdout: {result.stdout[:2000]!r}\nstderr: {result.stderr[:2000]!r}"
            ) from error
        return set()

    findings: set[Finding] = set()
    for entry in entries:
        raw_rule_id = entry.get("rule_id") or entry.get("rule")
        raw_rel = entry.get("file") or entry.get("rel") or entry.get("path")
        if raw_rule_id is None or raw_rel is None:
            continue
        findings.add((str(raw_rule_id), str(raw_rel), int(entry.get("line") or 1)))
    return findings


def run_wiki_lint_for_rule(rule_id: str, paths: list[Path]) -> set[Finding]:
    """Collect wiki-cli findings for a specific rule across paths."""
    all_findings: set[Finding] = set()
    for path in paths:
        all_findings |= {f for f in run_wiki_lint(path) if f[0] == rule_id}
    return all_findings
