"""A `tier: core` page with no (or empty) `aliases:` frontmatter, ported
from `utils/scripts/lint-rules/w100-core-page-aliases.mjs` (rule id
`W100`): `llm-wiki-query` resolves a core page first, by whatever name a
query actually uses, and today only the page's exact slug and H1 reach it.

`type: ship` is excluded: its own `tier:` field is a 1|2|3 hull rating (the
ship guide's contract), not the retrieval tier this rule is about — the
two fields share a name by coincidence, not by schema.

Not fixable — the aliases a page is actually called by is a content
judgment, never derivable from the page itself.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_TEMPLATES_PREFIX = "vault/_templates/"


def _has_alias_values(frontmatter: Mapping[str, object]) -> bool:
    if "aliases" not in frontmatter:
        return False
    value = frontmatter.get("aliases")
    if value is None:
        return False
    if isinstance(value, list):
        return len(value) > 0
    if isinstance(value, str):
        return value.strip() != ""
    return True


@register
class CorePageAliasesRule(FileRule):
    """Ported from npm's W100 (`utils/scripts/lint-rules/w100-core-page-aliases.mjs`)."""

    id = "W100"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = "Add the names this page is actually called by to aliases: [...]."
    producer = "wiki"
    pure = True
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        rel = page.rel_path
        if not rel.endswith(".md") or rel.startswith(_TEMPLATES_PREFIX):
            return

        frontmatter = page.frontmatter
        if frontmatter.get("tier") != "core":
            return
        if frontmatter.get("type") == "ship":
            return
        if _has_alias_values(frontmatter):
            return

        yield self.finding(
            file=rel,
            line=page.line_of("tier"),
            message=(
                "tier: core with no aliases — add the names this page is actually "
                "called by to aliases: [...]; a core page is what llm-wiki-query "
                "resolves first, and today only its exact slug and H1 reach it"
            ),
        )
