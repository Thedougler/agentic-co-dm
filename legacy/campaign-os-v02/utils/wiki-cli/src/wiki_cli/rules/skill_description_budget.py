"""Ported from npm's W79 (`utils/scripts/lint-rules/w79-skill-description-budget.mjs`).

A SKILL.md frontmatter `description:` mechanizes writing-for-agents's
"Writing the description" contract (`~/.claude/skills/writing-for-agents/
SKILL.md`, § Context pointers): "Every word increases context load, so a
description earns even harder pruning than the body" — a model-invoked
description is paid by every turn the window is open, not once. Two
thresholds on the same field, one rule:

- `SKILL_DESCRIPTION_WORD_BUDGET` (default 80): a soft craft budget — past
  it the description is doing more than "state what the skill is, list the
  branches that must trigger it" and needs pruning.
- `SKILL_DESCRIPTION_MAX_CHARS` (default 1536): the API's own hard
  truncation point for a skill description — text past it is silently
  dropped by the runtime, not merely verbose to a human reader, so a branch
  worded past this line never fires at all. The hard-truncation finding
  subsumes the soft word-budget one when both would fire.

Distinct from `SKILL_FRONTMATTER_MAX_CHARS` (the frontmatter-schema gate),
which caps the WHOLE frontmatter block (name + description + other keys
combined) — this rule caps the description field alone against the API's
own per-field truncation limit, a different number for a different reason.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_SKILL_PATH_RE = re.compile(r"(^|/)\.claude/skills/[^/]+/SKILL\.md$")
_AUTHORING_DOC = "`~/.claude/skills/writing-for-agents/SKILL.md` (§ Context pointers)"


@register
class SkillDescriptionBudgetRule(FileRule):
    """Ported from npm's W79 (`w79-skill-description-budget.mjs`)."""

    id = "W79"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = (
        "Prune the description to triggers only: collapse synonym "
        "branches into one, cut identity already stated in the body, "
        "keep only genuinely distinct branches."
    )
    producer = "wiki"
    pure = True
    """Reads wiki.toml's SKILL_DESCRIPTION_WORD_BUDGET/MAX_CHARS thresholds
    too; captured by Config.fingerprint (the cache key)."""
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        if not _SKILL_PATH_RE.search("/" + page.rel_path):
            return

        description = page.frontmatter.get("description")
        if not isinstance(description, str) or description.strip() == "":
            return  # frontmatter schema already flags a missing description

        config = load_config()
        word_budget = int(config.threshold("SKILL_DESCRIPTION_WORD_BUDGET"))
        max_chars = int(config.threshold("SKILL_DESCRIPTION_MAX_CHARS"))

        word_count = len([w for w in re.split(r"\s+", description.strip()) if w])
        char_count = len(description)
        line = page.line_of("description")

        if char_count > max_chars:
            yield self.finding(
                file=page.rel_path,
                line=line,
                message=(
                    f"description is {char_count} characters (API truncates skill "
                    f"descriptions past {max_chars}) — text beyond that point is "
                    "silently dropped at runtime, so any trigger phrase worded past "
                    "it never fires; cut the description under the cap now, per "
                    f"{_AUTHORING_DOC} (cap: wiki.toml [thresholds] "
                    "SKILL_DESCRIPTION_MAX_CHARS)"
                ),
            )
            return  # the hard truncation finding subsumes the soft word-budget one

        if word_count > word_budget:
            yield self.finding(
                file=page.rel_path,
                line=line,
                message=(
                    f"description is {word_count} words (budget ~{word_budget}) — "
                    "prune it to triggers only: collapse synonym branches into one, "
                    "cut identity already stated in the body, keep only genuinely "
                    f"distinct branches, per {_AUTHORING_DOC} (budget: wiki.toml "
                    "[thresholds] SKILL_DESCRIPTION_WORD_BUDGET)"
                ),
            )
