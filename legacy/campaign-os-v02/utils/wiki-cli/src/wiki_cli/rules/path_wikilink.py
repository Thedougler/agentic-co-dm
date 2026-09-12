"""W128 — path-qualified wikilink target.

A wikilink like ``[[path/to/slug|Display]]`` contains a directory path in
the target slot. Obsidian resolves by basename so the link works today, but
any tooling that treats the path literally — and the vault organiser's
file-move step — will break it. Slug-only format ``[[slug|Display]]``
survives moves.

Run ``wiki slug-scrub`` to rewrite every path-based wikilink in the vault.
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from pathlib import Path

from wiki_cli.autofix import current_context
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

# Captures the target slot (before any `#` or `|`) from both plain and embed wikilinks.
_WIKILINK_RE = re.compile(r"!?\[\[([^\]|#\n]+)(?:[^\]]*)\]\]")

PATH_WIKILINK_SCRUB_RE = re.compile(
    r"(!?\[\[)"                 # group 1: [[ or ![[
    r"([^\]|#\n]+/[^\]|#\n]*)"  # group 2: target with at least one /
    r"([^\]]*?)"                # group 3: #heading and/or |display (lazy)
    r"(\]\])"                   # group 4: ]]
)
"""The whole-vault rewrite ``wiki slug-scrub`` performs, one link at a
time. Requiring a `/` in the target slot is what keeps an already-bare
slug — and its extension, if the slug legitimately carries a dot —
untouched, which is also why a second pass changes nothing."""


def scrub_paths(text: str) -> tuple[str, int]:
    """(text with every path-qualified wikilink target reduced to its bare
    slug, number of links rewritten). Shared by this rule's autofix and by
    ``wiki slug-scrub``, so both rewrite links the same way."""
    return PATH_WIKILINK_SCRUB_RE.subn(
        lambda match: (
            f"{match.group(1)}{Path(match.group(2).strip()).stem}"
            f"{match.group(3)}{match.group(4)}"
        ),
        text,
    )


def _scrub_vault_paths(text: str) -> str:
    """This rule's autofix — `scrub_paths`, scoped to `vault/` the same way
    `check` is. Outside the vault a directory-shaped target is a real
    relative path, not a slug that lost its folder."""
    context = current_context()
    if context is None or not context.rel_path.startswith("vault/"):
        return text
    return scrub_paths(text)[0]


@register
class PathWikilinkRule(FileRule):
    """Wikilink target is path-qualified — use ``[[slug]]`` instead."""

    id = "W128"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Replace the path-qualified target with the bare slug "
        "(filename without its directory). "
        "Run ``wiki slug-scrub`` to rewrite the whole vault in one pass."
    )
    producer = "wiki"
    pure = True
    fixable = True
    version = "1"
    autofix = Autofix(scope="syntax", apply=_scrub_vault_paths)

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        if not page.rel_path.startswith("vault/"):
            return
        for line_no, text in page.body_lines():
            for match in _WIKILINK_RE.finditer(text):
                target = match.group(1).strip()
                if "/" not in target:
                    continue
                slug = Path(target).stem
                col = text.index(match.group(0)) + 1
                yield self.finding(
                    file=page.rel_path,
                    line=line_no,
                    message=(
                        f'wikilink target "{target}" is path-qualified — '
                        f'use the bare slug "[[{slug}]]" instead '
                        "(path-based links break when the target file moves)"
                    ),
                    column=col,
                )
