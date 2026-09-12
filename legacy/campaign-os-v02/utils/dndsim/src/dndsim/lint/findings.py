"""One finding + the markdownlint-obsidian-shaped JSON payload it serializes
to (ADR-0010).

``markdownlint-obsidian --output-formatter json`` emits
``[{filePath, errors: [{ruleCode, ruleName, severity, line, column, message,
fixable}]}]`` — one entry per requested file, ``errors: []`` for a clean
file. :func:`build_payload` reproduces that shape exactly (same key names,
same per-file-always-present convention) so
``utils/scripts/lib/lint-findings.mjs`` can concatenate this array with
markdownlint's own and let its existing byFile-accumulation loop merge the
two producers' findings under one rel path — no new merge logic needed on
the JS side beyond the concatenation itself.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True, slots=True)
class Finding:
    """One rule violation on one file.

    ``rule_code``/``rule_name`` preserve the exact identifiers the retired
    markdownlint-obsidian custom rules used (their ``names: [slug, W-code]``
    tuple) — a committed ratchet floor keyed on either string carries over
    untouched (docs/adr/0010).
    """

    rule_code: str
    rule_name: str
    severity: str
    line: int
    column: int
    message: str
    fixable: bool = False

    def to_json(self) -> dict[str, Any]:
        return {
            "ruleCode": self.rule_code,
            "ruleName": self.rule_name,
            "severity": self.severity,
            "line": self.line,
            "column": self.column,
            "message": self.message,
            "fixable": self.fixable,
        }


def build_payload(files_findings: list[tuple[Path, list[Finding]]]) -> list[dict[str, Any]]:
    """One payload entry per file, in the order given — ``errors: []`` for a
    clean file, matching markdownlint-obsidian's own shape exactly."""
    return [
        {
            "filePath": str(path.resolve()),
            "errors": [finding.to_json() for finding in findings],
        }
        for path, findings in files_findings
    ]
