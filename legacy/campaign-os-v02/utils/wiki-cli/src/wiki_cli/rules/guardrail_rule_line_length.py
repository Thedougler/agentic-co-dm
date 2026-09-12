"""Ported from npm's W109 (`utils/scripts/lint-rules/w109-guardrail-rule-line-length.mjs`).

A guardrail checklist rule grown past the length a model holds in one
glance. `_FORMAT.md` F1:

    F1. Every rule is one line, <=20 words where possible, opening with an
        imperative verb or a trigger clause ... A checklist line over ~30
        words splits into sub-lines under the same ID.

The enforced cap is deliberately looser than F1's ~30-word authoring
target — `GUARDRAIL_RULE_MAX_WORDS` (60 in production) is the drainable-
backlog floor beneath it, tuned in `wiki.toml`, never hard-coded here.

Body words = everything after `- <ID>. `, whitespace-split. Sub-lines (an
indented `  - C16a.` continuation) are measured on their own, which is
exactly the split F1 prescribes.

`MIGRATION-LOG.md` and `PROJECT-NOTES.md` are excluded — F15 names them
project-authored archives never reformatted to these contracts.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_GUARDRAIL_DOC_RE = re.compile(r"(^|/)docs/guardrails/([^/]+)\.md$")
_F15_ARCHIVES = frozenset({"MIGRATION-LOG", "PROJECT-NOTES"})
_RULE_LINE_RE = re.compile(r"^\s*-\s+([A-Z]{1,3}\d+[a-z]?)\.\s+(.*)$")
_FORMAT_DOC = "docs/guardrails/_FORMAT.md"


@register
class GuardrailRuleLineLengthRule(FileRule):
    """Ported from npm's W109 (`utils/scripts/lint-rules/w109-guardrail-rule-line-length.mjs`)."""

    id = "W109"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = (
        'Split the rule into sub-lines under the same ID, or move rationale '
        'below the "--- reference ---" divider.'
    )
    producer = "wiki"
    pure = True
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        match = _GUARDRAIL_DOC_RE.search("/" + page.rel_path)
        if not match:
            return
        if match.group(2) in _F15_ARCHIVES:
            return

        config = load_config()
        max_words = int(config.threshold("GUARDRAIL_RULE_MAX_WORDS"))
        lines = page.raw.split("\n")

        for index, line in enumerate(lines):
            rule_match = _RULE_LINE_RE.match(line)
            if not rule_match:
                continue
            words = len(rule_match.group(2).split())
            if words <= max_words:
                continue
            yield self.finding(
                file=page.rel_path,
                line=index + 1,
                message=(
                    f'{words}-word rule — split into sub-lines under the same ID or move '
                    f'rationale below the "--- reference ---" divider ({_FORMAT_DOC} F1: a '
                    "rule the model holds in one glance stops firing past a paragraph)."
                ),
            )
