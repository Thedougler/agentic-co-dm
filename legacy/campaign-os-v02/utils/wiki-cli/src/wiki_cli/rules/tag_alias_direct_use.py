"""W113 — a page tag that is a listed alias (`docs/tags.md` § Aliases)
rather than its canonical form. Ported from `utils/scripts/lint-rules/
w113-tag-alias-direct-use.mjs`.

Detected regardless of the page's own `status:` — an alias use is still
worth a finding on a `canon`/`retired` page — but `fixable` is gated off
for those two locked statuses, so a mechanical alias -> canonical rewrite
is never silently applied to canon content (`vault/.claude/skills/
tag-taxonomy/SKILL.md`'s canon-page gate, enforced here at the mechanism
level, not just by convention).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from wiki_cli.config import load_config
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
from wiki_cli.tags import Taxonomy, default_taxonomy_path, page_tags

if TYPE_CHECKING:
    from collections.abc import Iterable
    from pathlib import Path

_LOCKED_STATUSES: frozenset[str] = frozenset({"canon", "retired"})


def _canonicalise_tags(text: str) -> str:
    """Every alias tag replaced by its canonical form, in place.

    Each `PageTag` carries the exact line and column of its own value, so
    the rewrite touches those characters and nothing else — quoting,
    ordering, and the inline-vs-block shape all survive. Applied
    bottom-up so an earlier replacement never shifts a later column. A
    `canon`/`retired` page is skipped for the same reason `check` withholds
    `fixable` there: locked content is never rewritten mechanically. A
    canonical tag is never itself an alias, so a second pass changes
    nothing.
    """
    try:
        taxonomy_path = default_taxonomy_path(load_config())
    except (OSError, ValueError):
        return text
    taxonomy = Taxonomy.load(taxonomy_path)

    page = parse_page("in-memory.md", text)
    if page.frontmatter.get("status") in _LOCKED_STATUSES:
        return text

    replacements = [tag for tag in page_tags(page) if taxonomy.is_alias(tag.value)]
    if not replacements:
        return text

    lines = text.split("\n")
    for tag in sorted(replacements, key=lambda t: (t.line, t.column), reverse=True):
        index = tag.line - 1
        if index < 0 or index >= len(lines):
            continue
        start = tag.column - 1
        end = start + len(tag.value)
        if lines[index][start:end] != tag.value:
            continue
        lines[index] = lines[index][:start] + taxonomy.canonical(tag.value) + lines[index][end:]
    return "\n".join(lines)


@register
class TagAliasDirectUseRule(FileRule):
    """Ported from npm's W113 (`w113-tag-alias-direct-use.mjs`)."""

    id = "W113"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = "Replace the alias tag with its canonical form — docs/tags.md § Aliases lists the target."
    producer = "wiki"
    fixable = True
    pure = False
    """Depends on docs/tags.md's alias map, not just this page's own bytes."""
    version = "1"
    autofix = Autofix(scope="frontmatter", apply=_canonicalise_tags)

    def __init__(self, taxonomy_path: Path | None = None) -> None:
        self._taxonomy_path_override = taxonomy_path

    def _resolve_taxonomy_path(self) -> Path:
        if self._taxonomy_path_override is not None:
            return self._taxonomy_path_override
        return default_taxonomy_path(load_config())

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        status = page.frontmatter.get("status")
        fixable = status not in _LOCKED_STATUSES

        taxonomy = Taxonomy.load(self._resolve_taxonomy_path())
        for tag in page_tags(page):
            if not taxonomy.is_alias(tag.value):
                continue
            canonical = taxonomy.canonical(tag.value)
            yield self.finding(
                file=page.rel_path,
                line=tag.line,
                column=tag.column,
                message=(
                    f'tag "{tag.value}" is an alias, not canonical (docs/tags.md § '
                    f'Aliases) — replace with "{canonical}"'
                ),
                fixable=fixable,
            )
