"""W138 — a `type: item` page is missing the `unique:` frontmatter key.

`unique:` drives the item graph's opt-in flag (pages.unique DB column,
ADR — feat(db) 6342681). Every item page must carry it explicitly; the
safe default is `false`. The rule fires only on absence — `unique: false`
and `unique: true` both satisfy it.

Fixable: insert `unique: false` after the `attunement:` line in
frontmatter (the natural position in `vault/_templates/_srd/_item.md`).
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.contracts import (
    Autofix,
    Corpus,
    FileRule,
    Finding,
    Page,
    Severity,
    Tier,
    register,
)
from wiki_cli.markdown import parse_page

_TOP_LEVEL_KEY_RE = re.compile(r"^([A-Za-z0-9_-]+):")

_UNIQUE_LINE = "unique: false"


def _insert_unique(text: str) -> str:
    """`unique: false` written into a `type: item` page's frontmatter.

    Placed right after `attunement:` — the position
    `vault/_templates/_srd/_item.md` gives it — or immediately before the
    closing `---` on a page that carries no `attunement:` key. A page that
    already declares `unique:` (either value) is left alone, which is what
    makes the second pass a no-op.
    """
    page = parse_page("in-memory.md", text)
    if page.type != "item" or "unique" in page.frontmatter or page.body_start_line <= 1:
        return text

    lines = text.split("\n")
    closing_fence_index = page.body_start_line - 2
    insert_at = closing_fence_index
    for index in range(1, closing_fence_index):
        match = _TOP_LEVEL_KEY_RE.match(lines[index])
        if match and match.group(1) == "attunement":
            insert_at = index + 1
            break

    return "\n".join([*lines[:insert_at], _UNIQUE_LINE, *lines[insert_at:]])


@register
class ItemUniqueMissingRule(FileRule):
    """W138 — `type: item` page missing the `unique:` frontmatter key."""

    id = "W138"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = 'Insert `unique: false` after the `attunement:` line in frontmatter.'
    producer = "wiki"
    pure = True
    fixable = True
    version = "1"
    autofix = Autofix(scope="frontmatter", apply=_insert_unique)

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus

        if page.type != "item":
            return

        if "unique" in page.frontmatter:
            return

        yield self.finding(
            file=page.rel_path,
            line=page.line_of("attunement"),
            message=(
                'item page is missing the `unique:` key — '
                "add `unique: false` (or `true` for a one-of-a-kind item)"
            ),
        )
