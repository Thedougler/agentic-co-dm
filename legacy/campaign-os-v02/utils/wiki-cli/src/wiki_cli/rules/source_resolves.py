"""Ported from npm's W118 (`utils/scripts/lint-rules/w118-source-resolves.mjs`).

A `vault/**` page's `source:` frontmatter, when set, must resolve to a real
file on disk. The ingestion contract (`raw/CLAUDE.md`) is: a file lands in
`inbox/`, is copied verbatim into `raw/<YYYY-MM>/<name>`, then decomposed
into `vault/` pages each stamped `source: "raw/<YYYY-MM>/<name>"` pointing
at the raw file it came from. That frontmatter is the ONLY record of "what
was this page ingested from" — there is no ledger of record — so a
`source:` value that doesn't resolve breaks the pipeline's statelessness.
An empty `source: ""` (the template default for a page never migrated from
a raw/ document) is not a claim and never fires.

Not pure — the finding depends on the real filesystem (`corpus.repo_root`,
the true repo root that `raw/` and `vault/` both sit under), not just this
file's own bytes.
"""

from __future__ import annotations

from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register


@register
class SourceResolvesRule(FileRule):
    """Ported from npm's W118 (`utils/scripts/lint-rules/w118-source-resolves.mjs`)."""

    id = "W118"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = (
        'Fix source: to the real raw/<YYYY-MM>/<name> archive path, or clear it to '
        '"" if this page was never migrated from a raw/ document.'
    )
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        if not page.rel_path.startswith("vault/"):
            return

        source = page.frontmatter.get("source")
        if not isinstance(source, str) or source.strip() == "":
            return

        if (corpus.repo_root / source).exists():
            return

        yield self.finding(
            file=page.rel_path,
            line=page.line_of("source"),
            message=(
                f'source: "{source}" does not resolve to a file on disk — fix the path '
                "to the real raw/<YYYY-MM>/<name> archive file, or clear it to \"\" if "
                "this page was never migrated from a raw/ document"
            ),
        )
