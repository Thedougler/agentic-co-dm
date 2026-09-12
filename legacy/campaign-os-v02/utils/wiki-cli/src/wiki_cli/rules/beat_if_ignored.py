"""W132 — a `type: beat` page must have a non-empty `if_ignored:` value.

`if_ignored:` is the single highest-leverage sandbox field for a beat: it
makes the world feel alive when the party skips the beat, and distinguishes
skippable beats from unplayable ones
(`.claude/skills/composing-beats/references/audits.md` § Gravity audit).
An empty value means the DM has no answer for what happens when the table
moves on — a sandbox gap, not a draft-in-progress.

`vault/_templates/_episodes/_beat_hook.md` § frontmatter (shared spine of
the five `_beat_*.md` templates). Episode 09's pre-ADR-0060 pages are
exempt until that episode's rewrite.
"""

from __future__ import annotations

from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register
from wiki_cli.rules.retired_session_unit import LEGACY_EPISODE_09_PAGES

_SOURCE_DOC = "vault/_templates/_episodes/_beat_hook.md § frontmatter"


@register
class BeatIfIgnoredRule(FileRule):
    """W132 — beat pages require a non-empty `if_ignored:` frontmatter value."""

    id = "W132"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        'Add a concrete, showable consequence to "if_ignored:" — what the DM can '
        "narrate or the players can stumble across if the party skips this beat "
        "(.claude/skills/composing-beats/references/audits.md § Gravity audit)."
    )
    producer = "wiki"
    pure = True
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        rel = page.rel_path
        if not rel.endswith(".md") or not rel.startswith("vault/"):
            return
        if page.type != "beat":
            return
        if rel in LEGACY_EPISODE_09_PAGES:
            return

        value = page.frontmatter.get("if_ignored")
        if not value or (isinstance(value, str) and not value.strip()):
            yield self.finding(
                file=rel,
                line=1,
                message=(
                    "type: beat page has no if_ignored: value — every beat must answer "
                    "what happens if the party skips it; write a concrete, showable "
                    f"consequence the DM can narrate ({_SOURCE_DOC})"
                ),
            )
