"""Ported from npm's W116 (`utils/scripts/lint-rules/w116-embed-heading-resolves.mjs`).

A `![[page#Heading]]` transclusion whose heading does not exist on the
target page renders as a broken embed in Obsidian, exactly where the
runner expected operative content mid-play (docs/adr/0025).

The legacy module resolves the target page two ways: a slash-bearing
target is joined directly onto the repo root, a bare target goes through
the vault-wide name index. `corpus.resolve()` already covers both shapes —
every real citation in this vault is either a bare slug/alias/title or the
`vault/...`-prefixed full-path convention `corpus.resolve()` matches via
its exact-rel-path branch — so this port resolves through `corpus.resolve()`
alone rather than duplicating a second filesystem-join path.

Block refs (`#^block`) and non-md embeds (images/audio) are out of scope;
an unresolvable target page is W85/W18's finding, not this one's.

Not pure — the finding depends on the target page's headings, not just
this file's own bytes.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_SCOPED_PREFIX = "vault/"
_EMBED_RE = re.compile(r"!\[\[([^\]|#]+)#([^\]|]+)(?:\|[^\]]*)?\]\]")
_HEADING_LINE_RE = re.compile(r"^#{1,6}\s+(.*)$")


def _headings_of(target_page: Page) -> list[str]:
    """Every heading on `target_page`'s body (frontmatter already excluded
    by `Page.body`), lowercased for case-insensitive comparison."""
    return [
        match.group(1).strip().lower()
        for _, line in target_page.body_lines()
        if (match := _HEADING_LINE_RE.match(line))
    ]


@register
class EmbedHeadingResolvesRule(FileRule):
    """Ported from npm's W116 (`utils/scripts/lint-rules/w116-embed-heading-resolves.mjs`)."""

    id = "W116"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = "Repoint the embed's #Heading to one of the target page's real headings."
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        rel = page.rel_path
        if not rel.startswith(_SCOPED_PREFIX) or not rel.endswith(".md"):
            return

        lines = page.raw.split("\n")
        for idx, line in enumerate(lines):
            for match in _EMBED_RE.finditer(line):
                target = match.group(1).strip()
                heading = match.group(2).strip()
                if heading.startswith("^"):
                    continue  # block ref, not a heading
                if re.search(r"\.[a-zA-Z0-9]{2,4}$", target) and not target.endswith(".md"):
                    continue  # asset embed

                target_page = corpus.resolve(target)
                if target_page is None:
                    continue  # unresolvable page is another rule's finding

                if heading.lower() in _headings_of(target_page):
                    continue

                yield self.finding(
                    file=rel,
                    line=idx + 1,
                    message=(
                        f'embed references "#{heading}" but {target_page.rel_path} carries '
                        "no such heading — repoint it to one of that page's real headings "
                        "(a mismatched embed renders broken at the table)"
                    ),
                )
