"""Ported from npm's W27 (`utils/scripts/lint-rules/w27-empty-tags.mjs`).

A page carries no tag at all — tags drive an LLM-wiki's coarse retrieval/
filtering layer, so an untagged page is invisible to any tag-scoped query.
A `visibility/*` tag is a restriction, not subject matter, and does not
satisfy this rule on its own (matches `docs/tags.md`'s rule that it never
counts toward the tag cap).

Skips: no `type:` (W84's own job), `subtype: ingest-review` (pipeline
scaffolding, not authored content), and any page under the templates root
(a template's own `tags:` is the placeholder an instantiated page fills,
not that page's subject matter).

Not fixable — picking the right tag is a content judgment, not a
mechanical derivation.
"""

from __future__ import annotations

from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_VISIBILITY_PREFIX = "visibility/"
_TEMPLATES_PREFIX = "vault/_templates/"
"""Repo-root-relative form of the default templates root — a template's own
`tags:` is a placeholder an instantiated page fills, not subject matter."""


@register
class EmptyTagsRule(FileRule):
    """Ported from npm's W27 (`utils/scripts/lint-rules/w27-empty-tags.mjs`)."""

    id = "W27"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = "Add the closest-fit real tag from docs/tags.md — no page is exempt from carrying one."
    producer = "wiki"
    pure = True
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus

        if page.type is None:
            return  # W84's job

        if page.rel_path.startswith(_TEMPLATES_PREFIX):
            return

        frontmatter = page.frontmatter
        if frontmatter.get("subtype") == "ingest-review":
            return

        tags_raw = frontmatter.get("tags")
        tags = [item for item in tags_raw if isinstance(item, str)] if isinstance(tags_raw, list) else []
        subject = [tag for tag in tags if not tag.startswith(_VISIBILITY_PREFIX)]
        if subject:
            return

        had = (
            " (a visibility/ tag states restriction, not subject matter)"
            if tags
            else ""
        )
        line = page.frontmatter_lines.get("tags", 2)
        yield self.finding(
            file=page.rel_path,
            line=line,
            message=(
                f"page carries no tag{had} — every page states what it touches; "
                "add the closest fit from docs/tags.md § Domain, plus any § Project "
                "arc it belongs to"
            ),
        )
