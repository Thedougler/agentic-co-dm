"""Ported from npm's W120 (`utils/scripts/lint-rules/w120-section-count-outlier.mjs`
+ `w120-section-count-outlier.test.mjs`).

A page's H2 section count is a neighbour-relative outlier vs same-`type`
siblings: the mechanical backstop for the ONE-FACT-ONE-PAGE contract
(`vault/refs/qc-wiki-page.md`) — a page carrying far more sections than its
type normally does is probably several atomic entities/topics wedged onto
one page and should split. A heuristic that fires on a legitimately large
hub/reference page is baselined as debt rather than fixed.

Below `ATOMICITY_MIN_SIBLINGS` same-type siblings the measure is too thin
to trust and this rule stays silent — unlike W12, there is no fallback
ceiling (copies w120's own documented shape, not `pageLengthNeighbors.mjs`'s).
Both the target page and its siblings are measured from the *whole file's*
raw text (frontmatter included) — matching the legacy module exactly, and
unlike W12 there is no asymmetry here since w120 measures both sides the
same way (`countH2Sections(parsed.raw)` for the target, `countH2Sections
(file.raw)` for every sibling via `corpusStats.mjs`'s `computeGroupStats`).
"""

from __future__ import annotations

import math
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register
from wiki_cli.corpus_stats import count_h2_sections, outlier_limit

_TEMPLATES_PREFIX = "vault/_templates/"

_EXEMPT_PREFIXES = (
    "vault/dashboards/",  # hub pages, many sections by design
    "vault/refs/table-",  # one section per rollable table, by design
    "vault/stories/",
    "vault/ideas/",
    "vault/campaigns/shattered-sea/pcs/combat-profile/",
    "vault/campaigns/shattered-sea/pcs/character-sheets/",
)
_EXEMPT_EXACT = "vault/campaigns/shattered-sea/dm-voice-script.md"

_DERIVED_DATA_TYPES = frozenset(
    {"pc-sheet", "pc-stats", "pc-spells", "pc-combat-profile", "party-combat-profile"}
)

# Single-slot cache scoped to the most recently seen corpus — same fix,
# same rationale as `page_length.py`'s `_prose_line_cache`: an N-page
# same-`type:` group otherwise paid N*(N-1) calls to `count_h2_sections`
# instead of N. `page.raw` is fixed for the run, so this is exactly
# `count_h2_sections(sibling.raw.splitlines())`, computed once per page
# instead of once per group member.
_h2_section_cache: tuple[Corpus, dict[str, float]] | None = None


def _h2_section_counts(corpus: Corpus) -> dict[str, float]:
    global _h2_section_cache
    if _h2_section_cache is not None and _h2_section_cache[0] is corpus:
        return _h2_section_cache[1]
    counts = {p.rel_path: float(count_h2_sections(p.raw.splitlines())) for p in corpus.pages()}
    _h2_section_cache = (corpus, counts)
    return counts


@register
class SectionCountOutlierRule(FileRule):
    """Ported from npm's W120 (`utils/scripts/lint-rules/w120-section-count-outlier.mjs`)."""

    id = "W120"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = "Break this into smaller atomic pages, one per distinct entity/topic, linked from here."
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        if not page.rel_path.startswith("vault/"):
            return
        if page.rel_path.startswith(_TEMPLATES_PREFIX):
            return
        if page.rel_path.startswith(_EXEMPT_PREFIXES) or page.rel_path == _EXEMPT_EXACT:
            return
        if "transcript" in page.rel_path.lower():
            return

        page_type = page.type
        if page_type is None:
            return  # W84's own job
        if page_type in _DERIVED_DATA_TYPES:
            return

        config = load_config()
        headroom_pct = float(config.threshold("ATOMICITY_SECTION_HEADROOM_PCT"))
        min_siblings = int(config.threshold("ATOMICITY_MIN_SIBLINGS"))
        section_floor = float(config.threshold("ATOMICITY_SECTION_FLOOR"))

        siblings = [
            sibling for sibling in corpus.by_type(page_type) if sibling.rel_path != page.rel_path
        ]
        section_counts = _h2_section_counts(corpus)
        sibling_values = [section_counts[sibling.rel_path] for sibling in siblings]

        resolved = outlier_limit(
            sibling_values,
            headroom_pct=headroom_pct,
            min_sample=min_siblings,
            fallback_max=None,
            floor=section_floor,
        )
        if resolved is None:
            return  # too few same-type siblings to trust a median — stay silent

        section_count = count_h2_sections(page.raw.splitlines())
        if section_count <= resolved.limit:
            return

        assert resolved.sibling_median is not None
        yield self.finding(
            file=page.rel_path,
            line=page.body_start_line,
            message=(
                f"Page carries {section_count} H2 sections; {page_type}-page siblings run "
                f"median {resolved.sibling_median:g}, limit {math.ceil(resolved.limit)} — "
                "probable ONE-FACT-ONE-PAGE violation: break this into smaller atomic pages, "
                "one per distinct entity/topic, linked from here (vault/refs/qc-wiki-page.md)"
            ),
        )
