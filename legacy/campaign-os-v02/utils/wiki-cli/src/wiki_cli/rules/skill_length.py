"""Ported from npm's W72 (`utils/scripts/lint-rules/w72-skill-length.mjs`).

A `.claude/skills/<name>/SKILL.md` over `SKILL_MAX_LINES` (`wiki.toml`'s
`[thresholds]` table, default 200) holds more than `.claude/rules/skills.md`
allows inline: frontmatter, the contract line, a short orientation, the
workflow skeleton every invocation needs, and a pointer table to
`references/*.md` — heavy format specs, long checklists, worked examples,
and rationale live in `references/`, because every inline line bills every
invocation. No skill is exempt — an outside-tool reference bills the same
context as a pipeline-native skill.

Line count is measured off the file's raw bytes (frontmatter included), not
`page.body` — matches the legacy module's own `skillSourceLines` helper,
which reads the file directly because the JS engine's `parsed.raw`/
`parsed.lines` come back short on a file with frontmatter.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_SKILL_PATH_RE = re.compile(r"(^|/)\.claude/skills/[^/]+/SKILL\.md$")


def _skill_source_lines(raw: str) -> list[str]:
    """The whole file's lines, frontmatter included. A trailing newline
    yields one empty final element, dropped as not a real line."""
    lines = raw.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    return lines


@register
class SkillLengthRule(FileRule):
    """Ported from npm's W72 (`utils/scripts/lint-rules/w72-skill-length.mjs`)."""

    id = "W72"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = (
        "Move heavy format specs, long checklists, worked examples, and "
        "rationale into references/<topic>.md in this skill's own "
        "directory and replace them with a pointer table row."
    )
    producer = "wiki"
    pure = True
    """Reads wiki.toml's SKILL_MAX_LINES threshold too; captured by
    Config.fingerprint (the cache key), same reasoning as other threshold-
    driven pure rules in this package."""
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        if not _SKILL_PATH_RE.search("/" + page.rel_path):
            return

        max_lines = int(load_config().threshold("SKILL_MAX_LINES"))
        lines = _skill_source_lines(page.raw)
        count = len(lines)
        if count <= max_lines:
            return

        yield self.finding(
            file=page.rel_path,
            line=max_lines + 1,
            message=(
                f"SKILL.md is {count} lines (cap {max_lines}) — move heavy format "
                "specs, long checklists, worked examples, and rationale into "
                "references/<topic>.md in this skill's own directory and replace "
                "them with a pointer table row; every inline line bills every "
                "invocation (cap: wiki.toml [thresholds] SKILL_MAX_LINES)"
            ),
        )
