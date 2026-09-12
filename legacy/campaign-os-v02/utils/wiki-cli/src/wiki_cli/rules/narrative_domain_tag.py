"""W111 — a narrative page (`type:` in `_NARRATIVE_TAG_TYPES`) whose tags
carry no Domain-group tag (`docs/tags.md` § Domain) states a structural
group at best, never a tone. Ported from `utils/scripts/lint-rules/
w111-narrative-domain-tag.mjs`.

Strips `visibility/*` before checking, resolving each remaining tag
through `docs/tags.md`'s alias map so an aliased Domain tag (e.g.
`boss-fight` -> `combat`) still counts. Skips: empty tag set (W27's job,
not yet ported — Task 8), absent `type:` (W84's job), and `subtype:
ingest-review` (pipeline scaffolding, not authored content). Not fixable
— picking the right Domain tag is a content judgment, not a mechanical
derivation.

`_NARRATIVE_TAG_TYPES` mirrors the legacy module's `DEFAULT_
NARRATIVE_TAG_TYPES` verbatim. The legacy module reads it via
`readOptionalConstant(vaultRoot, "NARRATIVE_TAG_TYPES", DEFAULT)` — an
override key absent from both `utils/scripts/lint-rules/config/
thresholds.json` and this package's `wiki.toml` `[thresholds]` table, so
the legacy default is what always actually runs; hardcoding it here
matches real behaviour exactly, not just the fallback path.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register
from wiki_cli.tags import Taxonomy, default_taxonomy_path, page_tags

if TYPE_CHECKING:
    from collections.abc import Iterable
    from pathlib import Path

_NARRATIVE_TAG_TYPES: frozenset[str] = frozenset(
    {
        "npc",
        "location",
        "faction",
        "quest",
        "lore",
        "ship",
        "session",
        "encounter",
        "campaign",
        "season",
        "rule",
        "pc",
        "creature",
        "event",
        "puzzle",
        "handout",
    }
)
_VISIBILITY_PREFIX = "visibility/"
_INGEST_REVIEW_SUBTYPE = "ingest-review"


@register
class NarrativeDomainTagRule(FileRule):
    """Ported from npm's W111 (`w111-narrative-domain-tag.mjs`)."""

    id = "W111"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = (
        'Add the closest Domain tag from docs/tags.md (e.g. "combat", "intrigue") to '
        "tags:, keeping every existing tag."
    )
    producer = "wiki"
    pure = False
    """Depends on docs/tags.md's Domain group, not just this page's own bytes."""
    version = "1"

    def __init__(self, taxonomy_path: Path | None = None) -> None:
        self._taxonomy_path_override = taxonomy_path

    def _resolve_taxonomy_path(self) -> Path:
        if self._taxonomy_path_override is not None:
            return self._taxonomy_path_override
        return default_taxonomy_path(load_config())

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        if page.frontmatter.get("subtype") == _INGEST_REVIEW_SUBTYPE:
            return
        page_type = page.type
        if page_type is None or page_type not in _NARRATIVE_TAG_TYPES:
            return

        tags = page_tags(page)
        if not tags:
            return  # W27's job (empty tags), not W111's

        remainder = [tag for tag in tags if not tag.value.startswith(_VISIBILITY_PREFIX)]
        if not remainder:
            return

        taxonomy = Taxonomy.load(self._resolve_taxonomy_path())
        domain_group = taxonomy.groups().get("Domain", frozenset())
        has_domain_tag = any(taxonomy.canonical(tag.value) in domain_group for tag in remainder)
        if has_domain_tag:
            return

        domain_list = ", ".join(sorted(domain_group))
        yield self.finding(
            file=page.rel_path,
            line=page.line_of("tags"),
            message=(
                "tags carry no Domain tag — a narrative page states its tone, not just "
                "its structural group; add the closest fit from docs/tags.md § Domain "
                f"({domain_list}) keeping existing tags"
            ),
        )
