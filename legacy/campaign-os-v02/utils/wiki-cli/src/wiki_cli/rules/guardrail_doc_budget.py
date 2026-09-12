"""Ported from npm's W105 (`utils/scripts/lint-rules/w105-guardrail-doc-budget.mjs`).

A `docs/guardrails/*.md` doc exceeds `_FORMAT.md` F11's word or line cap:

    F11. ... Caps: ~120 lines AND ~1,100 words; a doc that must grow past
         either splits by trigger.

A guardrail doc is read cold at the moment its routing row fires — every
word past the cap is billed to the turn that can least afford it, which is
why F11 makes the fix a SPLIT (a new doc + its own routing row), never a
trim.

Body-word method (mirrors the legacy header exactly): drop line 1 when it
is an HTML comment (the kit-version comment), drop every fenced code block
(fence lines included, CommonMark-correct via `corpus_stats.fenced_line_flags`
— reused here rather than re-implemented, same shared helper `page_length.py`
draws on for prose-line counting), then whitespace-split every remaining
line's words.

Scope: every `docs/guardrails/*.md`, `_FORMAT.md` included. `MIGRATION-LOG.md`
and `PROJECT-NOTES.md` are excluded — F15 names them project-authored
archives whose transported content is never reformatted to these contracts.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register
from wiki_cli.corpus_stats import fenced_line_flags

_GUARDRAIL_DOC_RE = re.compile(r"(^|/)docs/guardrails/([^/]+)\.md$")
_F15_ARCHIVES = frozenset({"MIGRATION-LOG", "PROJECT-NOTES"})
_FORMAT_DOC = "docs/guardrails/_FORMAT.md"


def _body_words(lines: list[str]) -> int:
    start = 1 if lines and lines[0].strip().startswith("<!--") else 0
    fenced = fenced_line_flags(lines)
    words = 0
    for index in range(start, len(lines)):
        if fenced[index]:
            continue
        words += len(lines[index].split())
    return words


@register
class GuardrailDocBudgetRule(FileRule):
    """Ported from npm's W105 (`utils/scripts/lint-rules/w105-guardrail-doc-budget.mjs`)."""

    id = "W105"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = (
        "Split the doc by trigger: move a distinct-trigger section into its own "
        "doc and add its routing row to CLAUDE.md."
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
        max_lines = int(config.threshold("GUARDRAIL_DOC_MAX_LINES"))
        max_words = int(config.threshold("GUARDRAIL_DOC_MAX_WORDS"))

        lines = page.raw.split("\n")
        words = _body_words(lines)
        line_count = len(lines)
        if words <= max_words and line_count <= max_lines:
            return

        file_name = page.rel_path.rsplit("/", 1)[-1]
        yield self.finding(
            file=page.rel_path,
            line=1,
            message=(
                f"{file_name} is {words} words / {line_count} lines against "
                f"{_FORMAT_DOC} F11's ~{max_words}/~{max_lines} caps — split by trigger: "
                "move reference sections serving a distinct trigger into their own doc "
                "and add its routing row to CLAUDE.md (kit edit: hand-edit + version bump "
                "+ MIGRATION-LOG entry, F15). Words are body words: line-1 version comment "
                "and fenced code blocks excluded."
            ),
        )
