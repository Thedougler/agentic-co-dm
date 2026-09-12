"""Ported from npm's W62
(`utils/scripts/lint-rules/w62-inline-statblock-drift.mjs`).

A wikilink to an entity's own canonical stat-block page (`type: monster`,
`npc`, or `pc`) is immediately followed by a parenthetical restating that
entity's mechanical values (CR/AC/HP/to-hit/damage dice/save DC). The
numbers live on the entity's own page and this copy WILL drift the moment
only one side is corrected.

Exemptions ported verbatim: the canonical monster source trees themselves
(`vault/srd/monsters/`, `vault/campaigns/shattered-sea/monsters/`), PC
character-sheet exports (sim-derived, intentionally restate), and any
`*-combat-profile.md` (dndsim's own derived output).

Not pure — resolving the link target's `type:` requires the corpus.
"""

from __future__ import annotations

import re
from collections.abc import Iterator

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_SCOPED_ROOT = "vault/"
_CANONICAL_STAT_TYPES = frozenset({"monster", "npc", "pc"})

_EXEMPT_ROOTS = ("vault/srd/monsters/", "vault/campaigns/shattered-sea/monsters/")
_PCS_CHARACTER_SHEETS_ROOT = "vault/campaigns/shattered-sea/pcs/character-sheets/"

_DAMAGE_TYPES = (
    "piercing|slashing|bludgeoning|fire|cold|lightning|thunder|acid|poison|"
    "psychic|necrotic|radiant|force"
)
_ABILITY_ABBR = "STR|DEX|CON|INT|WIS|CHA"

_STAT_PATTERNS = (
    re.compile(r"\bCR\s*\d+(?:/\d+)?\b"),
    re.compile(r"\bAC\s*\d+\b"),
    re.compile(r"\bHP\s*\d+\b"),
    re.compile(r"[+-]\d+\s+to hit\b", re.IGNORECASE),
    re.compile(rf"\d+d\d+(?:\s*[+-]\s*\d+)?\s+(?:{_DAMAGE_TYPES})\b", re.IGNORECASE),
    re.compile(rf"\bDC\s*\d+\s+(?:{_ABILITY_ABBR})\b"),
)

# [[target|display]] immediately (within a short same-line gap — every real
# example in this vault is a single space) followed by a parenthetical.
_LINK_THEN_PAREN = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\][^(\n]{0,12}\(([^)]{1,300})\)")


@register
class InlineStatblockDriftRule(FileRule):
    """Ported from npm's W62
    (`utils/scripts/lint-rules/w62-inline-statblock-drift.mjs`)."""

    id = "W62"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.ERROR
    fix = (
        "Replace the parenthetical with a plain wikilink — the target page's own "
        "statblock/frontmatter is canonical; if this instance is a genuine one-off "
        "variant, name that explicitly instead of restating the base stat block."
    )
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterator[Finding]:
        rel = page.rel_path
        if not rel.startswith(_SCOPED_ROOT):
            return
        if any(rel.startswith(root) for root in _EXEMPT_ROOTS):
            return
        if rel.startswith(_PCS_CHARACTER_SHEETS_ROOT):
            return
        if rel.endswith("-combat-profile.md"):
            return

        self_slug = page.slug
        lines = page.body.split("\n")
        in_code_fence = False

        for offset, line in enumerate(lines):
            file_line = page.body_start_line + offset
            trimmed = line.strip()

            if trimmed.startswith("```"):
                in_code_fence = not in_code_fence
                continue
            if in_code_fence:
                continue

            for match in _LINK_THEN_PAREN.finditer(line):
                paren_text = match.group(3)
                if not any(pattern.search(paren_text) for pattern in _STAT_PATTERNS):
                    continue

                target = match.group(1).split("/")[-1].strip()
                resolved = corpus.resolve(target)
                if resolved is None:
                    continue
                if resolved.slug == self_slug:
                    continue
                if resolved.type not in _CANONICAL_STAT_TYPES:
                    continue

                display = (match.group(2) or target).strip()
                yield self.finding(
                    file=rel,
                    line=file_line,
                    column=match.start() + 1,
                    message=(
                        f'"{display}" ({resolved.rel_path}) stat block quoted inline '
                        f"({paren_text.strip()}) — that page (or its "
                        "![[<slug>-statblock]] embed) is the canonical source and this "
                        "copy WILL drift. Replace with a plain wikilink."
                    ),
                )
