"""New rule (no npm parity) — wiki-cli read layer plan Task 8.

A page links to the same target more than once from the same section — the
repeat wikilinks add nothing a reader didn't already get from the first one.

Which repeats are meaningful (a table row vs. a stray duplicate) needs
real-vault tuning, same rationale as `backlink_symmetry.py`; a hit is
baselineable debt until that tuning lands.

A `VaultRule` operating on the whole `VaultIndex`, reusing
`query.links.redundant` rather than re-deriving link-detail counts here.
"""

from __future__ import annotations

from collections.abc import Iterable

from wiki_cli.contracts import Corpus, Finding, Severity, Tier, VaultRule, register
from wiki_cli.index import VaultIndex


@register
class RedundantLinkRule(VaultRule):
    """New rule (wiki-cli read layer plan Task 8, no npm parity)."""

    id = "wiki/redundant-link"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = "Keep the first [[wikilink]] to a target within a section; drop or unlink the repeats"
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, corpus: Corpus) -> Iterable[Finding]:
        if not isinstance(corpus, VaultIndex):
            return

        from wiki_cli.query.links import redundant

        for source, section, target, count in redundant(corpus):
            slug = target.rsplit("/", 1)[-1].removesuffix(".md")
            section_label = f'section "{section}"' if section else "before first heading"
            yield self.finding(
                file=source,
                line=1,
                message=(
                    f"[[{slug}]] linked {count}x in {section_label} — same target, same section"
                ),
            )
