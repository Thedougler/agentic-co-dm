"""Ported from npm's W89 (`utils/scripts/lint-rules/w89-unsummarized-page.mjs`).

Every `vault/**` page carries a frontmatter `summary:`. The llm-wiki skill's
preview ladder reads it before ever opening the body, so a page without one
forces a full Read on every lookup. No length threshold and no per-type
exemption: a page too short or too machine-derived to state what a reader
learns in one sentence is a page that costs a full Read to find that out.
"""

from __future__ import annotations

from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register


@register
class UnsummarizedPageRule(FileRule):
    """Ported from npm's W89 (`utils/scripts/lint-rules/w89-unsummarized-page.mjs`)."""

    id = "W89"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = 'Add summary: "<one sentence, <=200 chars>" stating what a reader learns here.'
    producer = "wiki"
    pure = True
    version = "2"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus

        if not page.rel_path.startswith("vault/"):
            return

        if page.type is None:
            return  # W1's job

        summary = page.frontmatter.get("summary")
        if summary is not None and str(summary).strip() != "":
            return

        yield self.finding(
            file=page.rel_path,
            line=page.body_start_line,
            message=(
                "No summary: — add summary: \"<one sentence, <=200 chars>\" to the "
                "frontmatter stating what a reader learns here; without it every "
                "lookup costs a full Read"
            ),
        )
