"""W146 — performative pages name the story or world fact they tell.

`type: narration`, `dialogue`, and `handout` carry `goal:` — the lore the
party needs to progress, fewest words. Empty or missing fails.
`.claude/skills/narration/references/goal.md` owns the contract.
"""

from __future__ import annotations

from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_TYPES = frozenset({"narration", "dialogue", "handout"})
_SOURCE = ".claude/skills/narration/references/goal.md"


@register
class PerformativeGoalRule(FileRule):
    """W146 — goal: is present and non-empty on player-facing prose."""

    id = "W146"
    version = "1"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Set goal: to the story or world fact this file tells the party, "
        f"fewest words ({_SOURCE})."
    )
    producer = "wiki"
    pure = True

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        if page.type not in _TYPES:
            return
        if not page.rel_path.startswith("vault/"):
            return
        goal = page.frontmatter.get("goal")
        if isinstance(goal, str) and goal.strip():
            return
        yield self.finding(
            file=page.rel_path,
            line=1,
            message=(
                "missing or empty goal: — name the story or world fact "
                f"the party needs from this file ({_SOURCE})"
            ),
        )
