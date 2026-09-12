"""dndsim in-process merge producer (ADR-0010, ADR-0015, ADR-0041).

Merges dndsim's statblock/combatant-block lint rules
(`utils/dndsim/src/dndsim/lint/rules.py`) directly into wiki-cli's report
via an editable path dependency (`[tool.uv.sources]`).

ADR-0015: opt-in via ``WIKI_CLI_DNDSIM=1`` env var or ``wiki lint --dndsim``.
"""

from __future__ import annotations

import os
from pathlib import Path

from dndsim.lint.rules import lint_file as _dndsim_lint_file

from wiki_cli.config import Config
from wiki_cli.contracts import Corpus, Finding, ProducerRuleDoc, Severity, Tier

FAMILY_ID = "dndsim"
VERSION = "1"
PURE = False
"""Uncached. The verdict comes from the editable local `dndsim` package's
own lint rules, whose code changes without its version moving — a cache
key this module can compute would serve a stale verdict after any edit
there. It is also opt-in (`--dndsim`) and cheap, so caching buys little."""

RULE_DOCS: tuple[ProducerRuleDoc, ...] = (
    ProducerRuleDoc(
        id=FAMILY_ID,
        tier=Tier.STRUCTURAL,
        severity=Severity.WARNING,
        fix=(
            "Fix the statblock defect the dndsim rule name at the head of the message reports "
            "(W-statblock-simulatable, W-combatant-block), inside the page's own ```statblock "
            "fence. Clearing `WIKI_CLI_DNDSIM` hides the finding and is not a fix."
        ),
    ),
)

_ENV_FLAG = "WIKI_CLI_DNDSIM"

_TRUTHY = frozenset({"1", "true", "yes", "on"})


def _enabled() -> bool:
    return os.environ.get(_ENV_FLAG, "").strip().lower() in _TRUTHY


def run(config: Config, targets: list[Path], corpus: Corpus) -> list[Finding]:
    """Run dndsim's statblock/combatant-block checks over *targets*.

    Silent unless ``WIKI_CLI_DNDSIM`` is set (see module docstring).
    """
    del config  # dndsim's own lint module owns its scoped-root constants; nothing here reads repo config
    if not targets or not _enabled():
        return []

    repo_root = corpus.repo_root.resolve()
    findings: list[Finding] = []
    for target in targets:
        resolved = target.resolve()
        try:
            rel = str(resolved.relative_to(repo_root))
        except ValueError:
            continue  # outside the repo root — dndsim's scoped-root checks can never match it
        for dndsim_finding in _dndsim_lint_file(resolved, rel):
            severity = Severity.WARNING if dndsim_finding.severity == "warning" else Severity.ERROR
            findings.append(
                Finding(
                    rule_id=FAMILY_ID,
                    file=rel,
                    line=dndsim_finding.line,
                    message=f"{dndsim_finding.rule_name}: {dndsim_finding.message}",
                    severity=severity,
                    tier=Tier.STRUCTURAL,
                    producer=FAMILY_ID,
                    column=dndsim_finding.column,
                    fixable=dndsim_finding.fixable,
                )
            )
    return findings
