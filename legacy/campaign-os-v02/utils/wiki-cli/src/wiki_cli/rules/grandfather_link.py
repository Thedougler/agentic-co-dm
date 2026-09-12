"""Ported from npm's W119 (`utils/scripts/lint-rules/w119-grandfather-link.mjs`).

A page's structural slots connect it to its own `parent:`, never to an
ancestor further up the containment chain. An island whose parent is
[[midchain-north]] carrying `| Region | [[midchain]] |` names its
grandparent and leaves its parent unlinked, so the chain reads one rung
short everywhere it matters.

Prose is exempt by design: a sentence that genuinely names an ancestor is
the unlinked-entity mention W25 demands a link for. Only label slots — a
containment row of an At-a-Glance table, or a cell/bullet that is a link
with nothing around it — are checked. A slot that already links the
immediate parent alongside the ancestor is an address, not a skip, and
stays silent. The one autofixable shape (`fixable=True` on the finding) is
a table cell whose entire content is the ancestor link (plus an optional
article); the autofix retargets exactly those cells and leaves every other
hit to report. Resolving the chain needs the corpus, which the repair
reads from `autofix.current_context()` — without one it changes nothing.

LEGACY-BUG: the legacy module reads `parent:`, but ADR-0040's `within:`
rename retired `parent:` across every real template and page (zero
`vault/campaigns/**` pages carry `parent:` any more) — the npm engine's
W119 is currently a dead check against the real vault. This port stays
bug-compatible with the frozen npm engine (reads `parent:`, matching
ADR-0042's parity contract) rather than switching to `within:`; both sides
find 0 live matches today. Task 32's cutover pass should retarget this to
`within:` once the npm engine retires.

Not pure — walking the containment chain needs the corpus.
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from typing import ClassVar

from wiki_cli.autofix import current_context
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

_SCOPED_ROOTS = ("vault/", "pcs/")
_EXCLUDED_PREFIXES = (
    "vault/_",
    "sys/",
    "vault/stories/",
    "vault/ideas/",
    "vault/campaigns/shattered-sea/pcs/combat-profile/",
    "vault/campaigns/shattered-sea/pcs/character-sheets/",
)
_WIKILINK_RE = re.compile(r"\[\[([^\]]+?)\]\]")
_BULLET_RE = re.compile(r"^[-*]\s")
_BULLET_STRIP_RE = re.compile(r"^[-*]\s+")
_LEADING_LABEL_RE = re.compile(r"^\s*[A-Za-z][A-Za-z ]{0,24}:\s*")
_NON_ALNUM_RE = re.compile(r"[^A-Za-z0-9\s]")
_SOLE_LINK_CELL_RE = re.compile(r"^\s*(the\s+)?\[\[[^\]]*\]\][\s.,]*$", re.IGNORECASE)


def _slug_of(target: str) -> str:
    """`path/to/page\\|Display` (table-escaped or not) -> `page`, lowercased."""
    unescaped = target.replace("\\|", "|")
    link_target = unescaped.split("|", 1)[0]
    return link_target.split("#", 1)[0].strip().rsplit("/", 1)[-1].lower()


def _alias_of(target: str) -> str | None:
    """`page|Display` -> `Display`, or None when the link carries no alias."""
    unescaped = target.replace("\\|", "|")
    pipe = unescaped.find("|")
    return None if pipe == -1 else unescaped[pipe + 1 :].strip()


def _strip_brackets(field: str) -> str:
    return field.removeprefix("[[").removesuffix("]]")


def _ancestors_above(parent_slug: str, corpus: Corpus) -> set[str]:
    """Every ancestor ABOVE `parent_slug` in the containment chain. Cycle-guarded."""
    above: set[str] = set()
    seen = {parent_slug}
    current = corpus.resolve(parent_slug)
    while current is not None:
        parent_field = current.frontmatter.get("parent")
        if not isinstance(parent_field, str) or "[[" not in parent_field:
            break
        next_slug = _slug_of(_strip_brackets(parent_field))
        if next_slug in seen:
            break
        seen.add(next_slug)
        above.add(next_slug)
        current = corpus.resolve(next_slug)
    return above


def _split_cells(line: str) -> list[tuple[str, int]]:
    """Cells of a table row with their 0-based offsets into the line. Splits on
    unescaped `|` only — a wikilink's own alias pipe is written `\\|` inside a
    table and is not a cell boundary."""
    cells: list[tuple[str, int]] = []
    start: int | None = None
    for i, char in enumerate(line):
        if char != "|" or (i > 0 and line[i - 1] == "\\"):
            continue
        if start is not None:
            cells.append((line[start:i], start))
        start = i + 1
    return cells


def _residual_word_count(text: str) -> int:
    """Words left once wikilinks, a leading `Label:`, and punctuation are gone."""
    bare = _WIKILINK_RE.sub(" ", text)
    bare = _LEADING_LABEL_RE.sub(" ", bare, count=1)
    bare = _NON_ALNUM_RE.sub(" ", bare)
    return len([word for word in bare.split() if word])


def _retarget_grandparent_links(text: str) -> str:
    """Each sole-link label cell repointed from the grandparent to the parent.

    Reuses `check` itself rather than re-deriving the chain, so the repair
    lands on exactly the hits the rule calls fixable and nowhere else. The
    rewritten cell then links the parent, which is what `check`'s own
    "an address names the whole chain" branch reads as satisfied on a
    second pass.
    """
    context = current_context()
    if context is None or context.corpus is None:
        return text

    page = parse_page(context.rel_path, text)
    fixes = [
        finding
        for finding in GrandfatherLinkRule().check(page, context.corpus)
        if finding.fixable
    ]
    if not fixes:
        return text

    parent_field = page.frontmatter.get("parent")
    if not isinstance(parent_field, str) or "[[" not in parent_field:
        return text
    parent_raw = _strip_brackets(parent_field)
    parent_slug = _slug_of(parent_raw)
    parent_display = _alias_of(parent_raw) or parent_slug
    parent_link = (
        f"[[{parent_slug}]]"
        if parent_display == parent_slug
        else f"[[{parent_slug}\\|{parent_display}]]"
    )

    lines = text.split("\n")
    for finding in sorted(fixes, key=lambda f: (f.line, f.column), reverse=True):
        index = finding.line - 1
        if index < 0 or index >= len(lines):
            continue
        start = finding.column - 1
        match = _WIKILINK_RE.match(lines[index], start)
        if match is None:
            continue
        lines[index] = lines[index][:start] + parent_link + lines[index][match.end() :]
    return "\n".join(lines)


@register
class GrandfatherLinkRule(FileRule):
    """Ported from npm's W119 (`w119-grandfather-link.mjs`)."""

    id = "W119"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.ERROR
    fix: ClassVar[str] = (
        "Retarget the label slot to [[<parent-slug>]] — this page's own parent:, "
        "never an ancestor further up the chain."
    )
    producer = "wiki"
    fixable: ClassVar[bool] = True
    pure = False
    version = "1"
    autofix: ClassVar[Autofix | None] = Autofix(
        scope="syntax", apply=_retarget_grandparent_links
    )

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        rel = page.rel_path
        if not rel.endswith(".md"):
            return
        if not any(rel.startswith(root) for root in _SCOPED_ROOTS):
            return
        if rel.startswith(_EXCLUDED_PREFIXES):
            return
        if page.type == "table":
            return

        parent_field = page.frontmatter.get("parent")
        if not isinstance(parent_field, str) or "[[" not in parent_field:
            return
        parent_raw = _strip_brackets(parent_field)
        parent_slug = _slug_of(parent_raw)

        ancestors = _ancestors_above(parent_slug, corpus)
        if not ancestors:
            return

        config = load_config()
        containment_labels = {
            label.strip().lower()
            for label in config.threshold("CONTAINMENT_ROW_LABELS").split(",")
            if label.strip()
        }
        max_residual_words = int(config.threshold("LABEL_SLOT_MAX_RESIDUAL_WORDS"))

        parent_display = _alias_of(parent_raw) or parent_slug
        parent_link = (
            f"[[{parent_slug}]]"
            if parent_display == parent_slug
            else f"[[{parent_slug}\\|{parent_display}]]"
        )
        parent_link_display = parent_link.replace("\\|", "|")

        lines = page.raw.split("\n")
        for i, line in enumerate(lines):
            trimmed = line.strip()
            links = list(_WIKILINK_RE.finditer(line))
            if not links:
                continue

            hits = [m for m in links if _slug_of(m.group(1)) in ancestors]
            if not hits:
                continue
            # An address names the whole chain — the parent is linked right
            # there alongside the ancestor, so nothing is skipped.
            if any(_slug_of(m.group(1)) == parent_slug for m in links):
                continue

            is_table_row = trimmed.startswith("|")
            is_bullet = bool(_BULLET_RE.match(trimmed))
            if not is_table_row and not is_bullet:
                continue
            if (
                is_bullet
                and _residual_word_count(_BULLET_STRIP_RE.sub("", trimmed)) > max_residual_words
            ):
                continue

            cells = _split_cells(line) if is_table_row else []
            label_cell = cells[0][0].strip().lower() if cells else ""
            is_containment_row = label_cell in containment_labels

            for match in hits:
                cell = next(
                    (
                        c
                        for c in cells
                        if match.start() >= c[1] and match.start() < c[1] + len(c[0])
                    ),
                    None,
                )
                # A descriptive cell (a "Locations Within" Detail column) is prose
                # that happens to sit in a table — only label-shaped cells count.
                if (
                    is_table_row
                    and not is_containment_row
                    and (cell is None or _residual_word_count(cell[0]) > max_residual_words)
                ):
                    continue

                sole_link_cell = (
                    cell is not None
                    and len(list(_WIKILINK_RE.finditer(cell[0]))) == 1
                    and bool(_SOLE_LINK_CELL_RE.match(cell[0]))
                )

                yield self.finding(
                    file=rel,
                    line=i + 1,
                    column=match.start() + 1,
                    message=(
                        f'"{match.group(0)}" is this page\'s grandparent, not its parent — '
                        "this slot links the page one rung above where it belongs. Link its "
                        f"parent {parent_link_display} here instead. An ancestor link belongs "
                        "only where prose naturally names it."
                    ),
                    fixable=sole_link_cell,
                )
