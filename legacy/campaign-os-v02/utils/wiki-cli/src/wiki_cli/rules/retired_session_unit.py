"""W143 — passage, moment, fork, sequence, and dm-screen are retired types;
do not instantiate new ones.

ADR-0061: beats absorb moments, decisions/forks, and sequences; the
dm-screen legacy route is deleted. A crossing is a Route; a playable
dramatic unit is a `type: beat` page instantiated from
`vault/_templates/_episodes/_beat_*.md`. Episodes 001-008 are played
history and frozen — every page under those directories is exempt.
Episode 09's pre-ADR-0061 leftover pages stay readable until that
episode's rewrite (LEGACY_EPISODE_09_PAGES, also honored by W132/W133).
Any other page of a retired type, or named like one, under
vault/episodes/ fails.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_SOURCE = "docs/adr/0061-beats-absorb-moments-forks-and-sequences.md"
_RETIRED_TYPES = frozenset({"passage", "moment", "fork", "sequence", "dm-screen"})
_RETIRED_BASENAME_PREFIXES = ("passage-", "moment-", "fork-", "sequence-")
_FROZEN_EPISODE_RE = re.compile(r"^vault/episodes/(00[1-8])/")
LEGACY_EPISODE_09_PAGES = frozenset(
    {
        "vault/episodes/009/beat-01-crown-cutter.md",
        "vault/episodes/009/beat-02-empty-docks.md",
        "vault/episodes/009/beat-03-waveservant-wreckage.md",
        "vault/episodes/009/beat-04-smoke-on-the-coast.md",
        "vault/episodes/009/beat-05-the-shadow.md",
        "vault/episodes/009/beat-06-strange-pennant.md",
        "vault/episodes/009/beat-07-something-below.md",
        "vault/episodes/009/beat-08-the-chemical-story.md",
        "vault/episodes/009/beat-09-the-depot.md",
        "vault/episodes/009/beat-10-the-squall.md",
        "vault/episodes/009/beat-11-velvet-terms.md",
        "vault/episodes/009/beat-12-storm-debris.md",
        "vault/episodes/009/passage-01-crossing-to-fathomrush.md",
        "vault/episodes/009/passage-02-three-days-west.md",
        "vault/episodes/009/passage-03-four-days-south.md",
        "vault/episodes/009/passage-04-seven-days-southwest.md",
        "vault/episodes/009/passage-05-four-days-east.md",
        "vault/episodes/009/fork-01-the-heading-choice.md",
        "vault/episodes/009/fork-02-the-burning-yard.md",
        "vault/episodes/009/moment-02-la-vasca-departure.md",
        "vault/episodes/009/moment-03-the-heading-choice.md",
        "vault/episodes/009/moment-05-high-eyrie-approach.md",
        "vault/episodes/009/moment-07-timber-yard-fire.md",
        "vault/episodes/009/moment-08-sparhold-arrival.md",
        "vault/episodes/009/moment-10-the-brigantine.md",
        "vault/episodes/009/moment-11-the-dead-lady-finds-them.md",
        "vault/episodes/009/moment-13-the-shelfworks.md",
        "vault/episodes/009/moment-14-vestra-water.md",
        "vault/episodes/009/moment-15-the-green-cut-trail.md",
        "vault/episodes/009/moment-16-the-kailani-smack.md",
        "vault/episodes/009/sequence-01-cold-open-aruhe.md",
    }
)


@register
class RetiredSessionUnitRule(FileRule):
    """W143 — new pages of a retired session-unit type fail."""

    id = "W143"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Put a crossing on a type: route page instead of this page. A playable "
        "dramatic unit is a type: beat page instantiated from "
        "vault/_templates/_episodes/_beat_*.md."
    )
    producer = "wiki"
    pure = True
    version = "3"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        rel = page.rel_path
        if not rel.startswith("vault/episodes/") or not rel.endswith(".md"):
            return
        if _FROZEN_EPISODE_RE.match(rel):
            return
        if rel in LEGACY_EPISODE_09_PAGES:
            return
        basename = rel.rsplit("/", 1)[-1]
        retired_name = basename.startswith(_RETIRED_BASENAME_PREFIXES) or basename == "dm-screen.md"
        if page.type not in _RETIRED_TYPES and not retired_name:
            return
        yield self.finding(
            file=rel,
            line=1,
            message=(
                f"type: {page.type} is not a session unit — do not instantiate "
                "a passage, moment, fork, sequence, or dm-screen page; use a "
                f"Route, a Situation, or a type: beat page ({_SOURCE})"
            ),
        )
