"""New rule: wiki/anchor-missing — typed spatial frontmatter key with no value.

A page that declares `location:` or `within:` with an absent or empty value
has an incomplete typed edge: the spatial anchor is declared but unresolvable.
This prevents the vault organiser from placing the page in a cluster."""

from __future__ import annotations

from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_SPATIAL_KEYS = ("location", "within")


@register
class AnchorMissingRule(FileRule):
    """Structural warning: a spatial frontmatter key exists but has no value."""

    id = "wiki/anchor-missing"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = "Supply a non-empty [[wikilink]] value for the location: or within: key"
    producer = "wiki"
    pure = True
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        for key in _SPATIAL_KEYS:
            if key not in page.frontmatter:
                continue
            raw = page.frontmatter.get(key)
            if raw is None or (isinstance(raw, str) and not raw.strip()):
                yield self.finding(
                    file=page.rel_path,
                    line=page.line_of(key),
                    message=(
                        f"{key}: key is present but has no target — "
                        "supply a [[wikilink]] to the anchor page"
                    ),
                )
