"""W133 — a `type: beat` page must embed a narration sibling.

A beat's spoken opener is what makes it a drop-in unit the DM can
introduce on pacing and table energy. Spoken prose lives in a sibling
`type: narration` file embedded whole-file (`![[<slug>-narration-<role>]]`,
ADR-0056) — never an inline read-aloud callout. A beat with no embed is a
prep note, not a deployable unit.

`vault/_templates/_episodes/_beat_hook.md` (shared spine of the five
`_beat_*.md` templates). Episode 09's pre-ADR-0060 pages are exempt until
that episode's rewrite.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register
from wiki_cli.rules.retired_session_unit import LEGACY_EPISODE_09_PAGES

_NARRATION_EMBED_RE = re.compile(r"^!\[\[[^\]\n]*-narration-[^\]\n]*\]\]", re.MULTILINE)
_SOURCE_DOC = "vault/_templates/_episodes/_beat_hook.md"


@register
class BeatNarrationEmbedRule(FileRule):
    """W133 — beat pages require a whole-file narration-sibling embed."""

    id = "W133"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Embed the beat's spoken opener as a narration sibling: create the "
        "type: narration file beside the beat (writing-player-prose owns its "
        "prose) and add ![[<slug>-narration-open]] below the H1."
    )
    producer = "wiki"
    pure = True
    version = "2"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        rel = page.rel_path
        if not rel.endswith(".md") or not rel.startswith("vault/"):
            return
        if page.type != "beat":
            return
        if rel in LEGACY_EPISODE_09_PAGES:
            return

        if not _NARRATION_EMBED_RE.search(page.raw):
            yield self.finding(
                file=rel,
                line=1,
                message=(
                    "type: beat page has no narration-sibling embed — every beat "
                    "ships its spoken opener as ![[<slug>-narration-<role>]] "
                    f"below the H1 ({_SOURCE_DOC})"
                ),
            )
