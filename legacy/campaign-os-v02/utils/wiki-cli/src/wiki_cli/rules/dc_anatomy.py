"""Ported from npm's W70 (`utils/scripts/lint-rules/w70-dc-anatomy-outside-check.mjs`).

A DC sitting in a table cell or a `[!mechanic]` callout body must carry the
same anatomy a `[!check]` callout carries by convention — an ability/skill
the DC targets, and a stated failure consequence — because a DC with
neither is unusable at the table
(vault/campaigns/.claude/skills/callouts/references/{check,mechanic}.md).
An attack roll is never labeled DC either (5e SRD core mechanics: DC
targets ability checks/saves, AC targets attack rolls).

Scope: `vault/` only, same DM-working-material exemptions as W23/W69
(stories, ideas, PC combat-profile/character-sheet dumps carry no page
schema) plus vendored SRD reference material (spells, items, five migrated
equipment rule pages, the classes/subclasses tree) and any
`vault/srd/rules/` page whose frontmatter marks it `status: srd` — a
`[!mechanic]` on verbatim SRD text frequently states no consequence, and
inventing one there would put authored rules text onto vendored source
(vault/CLAUDE.md rule 2).

Detection only — the fix (add the missing column/ability/consequence, move
a genuine roll into its own `[!check]`, or reword "DC" to "AC") is a
content-authorship judgment call.

The legacy module's own callout structure comes from an external markdown
parser (`parsed.callouts`); this port has no such parser available, so it
walks blockquote lines (`> [!type] Title` opener, contiguous `>`-prefixed
continuation lines as the body) itself — equivalent for the
`[!mechanic]`/`[!check]` shapes this rule cares about.
"""

from __future__ import annotations

import re
from collections.abc import Callable, Iterable
from dataclasses import dataclass

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

SCOPED_ROOTS = ("vault/",)
DOC_ROOTS = (
    "vault/srd/spells/",
    "vault/srd/items/",
    "vault/srd/rules/equipment.md",
    "vault/srd/rules/adventuring-gear.md",
    "vault/srd/rules/mounts-vehicles.md",
    "vault/srd/rules/tools.md",
    "vault/srd/rules/weapons.md",
    "vault/srd/classes/",
)
EXEMPT_PATTERNS = (
    re.compile(r"^vault/stories/"),
    re.compile(r"^vault/ideas/"),
    re.compile(r"^vault/campaigns/shattered-sea/pcs/combat-profile/"),
    re.compile(r"^vault/campaigns/shattered-sea/pcs/character-sheets/"),
)
EXEMPT_FILE_PATTERNS = (re.compile(r"(^|/)dm-voice-script\.md$"),)

DC_PATTERN = re.compile(r"\bDC\s?\d+\b", re.IGNORECASE)
AC_PAREN_PATTERN = re.compile(r"\bDC\s?\d+\s*\([^)]*\bAC\b[^)]*\)", re.IGNORECASE)

ABILITY_SKILL_TERMS = (
    "Strength", "STR", "Dexterity", "DEX", "Constitution", "CON",
    "Intelligence", "INT", "Wisdom", "WIS", "Charisma", "CHA",
    "Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception",
    "History", "Insight", "Intimidation", "Investigation", "Medicine",
    "Nature", "Perception", "Performance", "Persuasion", "Religion",
    "Sleight of Hand", "Stealth", "Survival",
)
ABILITY_SKILL_PATTERN = re.compile(
    r"\b(" + "|".join(re.escape(term) for term in ABILITY_SKILL_TERMS) + r")\b",
    re.IGNORECASE,
)

CONSEQUENCE_COLUMN_PATTERN = re.compile(
    r"\b(effect|consequence|result|outcome|failure|miss)\b", re.IGNORECASE
)
# A stated outcome word anywhere in the line/body — deliberately not anchored
# to "or" immediately after the DC: this vault writes the consequence both
# ways ("DC 13 CON save or poisoned" and "Grappled (escape DC 13)",
# trigger-first). Presence of any status/effect term is the signal; word
# order isn't.
CONSEQUENCE_TERM_PATTERN = re.compile(
    r"\bfail(?:s|ed|ure|ing)?\b|\bunless\b|\b(poison(?:ed|s)?|damage|prone|restrain(?:ed|s)?|"
    r"grappl(?:e|ed|es)?|blind(?:ed|s)?|charm(?:ed|s)?|frighten(?:ed|s)?|stun(?:ned|s)?|"
    r"paraly[sz]ed?|push(?:ed|es)?|knock(?:ed|s)?|fall(?:s|en)?|cannot|can.t|unable|lose[s]?|"
    r"drop(?:ped|s)?|drag(?:ged|s)?|shove[ds]?|silenc(?:ed|es)?|infect(?:ed|ion|s)?|"
    r"diseas(?:e|ed)?|escape|petrif(?:y|ied|ies)|exhaust(?:ion|ed)?|incapacitat(?:e|ed|es)|"
    r"curs(?:e|ed)|transform(?:ed|s)?|blast|burn(?:s|ed)?|collapse[ds]?|trap(?:s|ped)?)\b",
    re.IGNORECASE,
)

_TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
_SEPARATOR_ROW_RE = re.compile(r"^\s*\|(\s*:?-+:?\s*\|)+\s*$")
_FENCE_LINE_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
_CLOSING_FENCE_RE = re.compile(r"^\s*(`+|~+)\s*$")
_CALLOUT_OPEN_RE = re.compile(r"^>\s?\[!(\w+)\]\s*(.*)$")
_CALLOUT_CONT_RE = re.compile(r"^>\s?(.*)$")
_DC_COL_RE = re.compile(r"^\**dc\**$", re.IGNORECASE)
_ABILITY_COL_RE = re.compile(r"\b(skill|ability|save)\b", re.IGNORECASE)
_PLACEHOLDER_RE = re.compile(r"^[-—–]+$")
_H2_RE = re.compile(r"^##\s+(.+)$")
_AT_A_GLANCE_RE = re.compile(r"^At a Glance\b", re.IGNORECASE)
_DASH_SPLIT_RE = re.compile(r"\s—\s")


def _fenced_flags(lines: list[str]) -> list[bool]:
    """Same CommonMark-correct fenced-code tracker as the legacy
    `lib/fences.mjs` — a fence closes only on a same-character marker of
    at least the same run length."""
    flags = [False] * len(lines)
    open_fence: tuple[str, int] | None = None
    for i, line in enumerate(lines):
        if open_fence is None:
            match = _FENCE_LINE_RE.match(line)
            if match:
                open_fence = (match.group(1)[0], len(match.group(1)))
                flags[i] = True
            continue
        flags[i] = True
        close = _CLOSING_FENCE_RE.match(line)
        if close and close.group(1)[0] == open_fence[0] and len(close.group(1)) >= open_fence[1]:
            open_fence = None
    return flags


def _is_table_row(line: str) -> bool:
    return bool(_TABLE_ROW_RE.match(line))


def _is_separator_row(line: str) -> bool:
    return bool(_SEPARATOR_ROW_RE.match(line))


def _split_row(line: str) -> list[str]:
    stripped = line.strip()
    stripped = stripped.removeprefix("|")
    stripped = stripped.removesuffix("|")
    return [cell.strip() for cell in stripped.split("|")]


def _scan_tables(
    lines: list[str],
    line_for_index: Callable[[int], int],
    on_row: Callable[[list[str], list[str], str, int], None],
) -> None:
    """Every table block (header + separator + data rows) in `lines`,
    calling `on_row(header, cells, raw_row_text, file_line)` once per data
    row."""
    i = 0
    n = len(lines)
    while i < n:
        if _is_table_row(lines[i]) and i + 1 < n and _is_separator_row(lines[i + 1]):
            header = _split_row(lines[i])
            j = i + 2
            while j < n and _is_table_row(lines[j]):
                on_row(header, _split_row(lines[j]), lines[j], line_for_index(j))
                j += 1
            i = j
        else:
            i += 1


def _cell(cells: list[str], idx: int) -> str:
    return cells[idx] if 0 <= idx < len(cells) else ""


def _check_table_row(
    header: list[str], cells: list[str], raw: str, on_violation: Callable[[str], None]
) -> None:
    dc_col_idx = next((i for i, h in enumerate(header) if _DC_COL_RE.match(h.strip())), -1)
    row_has_dc = (
        bool(re.search(r"\d", _cell(cells, dc_col_idx)))
        if dc_col_idx >= 0
        else bool(DC_PATTERN.search(raw))
    )
    if not row_has_dc:
        return

    ability_col_idx = next((i for i, h in enumerate(header) if _ABILITY_COL_RE.search(h)), -1)
    consequence_col_idx = next(
        (i for i, h in enumerate(header) if CONSEQUENCE_COLUMN_PATTERN.search(h)), -1
    )

    dc_cell_text = _cell(cells, dc_col_idx)
    ability_ok = (
        bool(ABILITY_SKILL_PATTERN.search(dc_cell_text))
        or _cell(cells, ability_col_idx).strip() != ""
        or bool(ABILITY_SKILL_PATTERN.search(raw))
    )

    consequence_cell = _cell(cells, consequence_col_idx).strip()
    consequence_ok = (
        consequence_col_idx >= 0 and not (consequence_cell == "" or _PLACEHOLDER_RE.match(consequence_cell))
    ) or bool(CONSEQUENCE_TERM_PATTERN.search(raw))

    if not ability_ok and not consequence_ok:
        on_violation(
            "DC table row carries no ability/skill and no failure consequence — add a "
            'Skill/Ability column (or fold it into the DC cell, "DC 12 Investigation") and '
            "an Effect/Consequence column, or move this row's roll to its own [!check] "
            "(vault/campaigns/.claude/skills/callouts/references/check.md)"
        )
    elif not ability_ok:
        on_violation(
            "DC table row carries no ability/skill — state which ability, save, or skill the "
            'DC targets (a Skill/Ability column, or "DC 12 Investigation" in the cell) '
            "(vault/campaigns/.claude/skills/callouts/references/check.md)"
        )
    elif not consequence_ok:
        on_violation(
            "DC table row states no failure consequence — add an Effect/Consequence column, "
            "or state what a miss does (vault/campaigns/.claude/skills/callouts/references/check.md)"
        )


@dataclass(frozen=True, slots=True)
class _Callout:
    type: str
    title: str
    body_lines: list[str]
    position_line: int
    """1-indexed file line of the callout's opening `> [!type]` line."""


def _find_callouts(lines: list[str]) -> list[_Callout]:
    callouts: list[_Callout] = []
    i = 0
    n = len(lines)
    while i < n:
        match = _CALLOUT_OPEN_RE.match(lines[i])
        if match:
            position_line = i + 1
            body_lines: list[str] = []
            j = i + 1
            while j < n:
                cont = _CALLOUT_CONT_RE.match(lines[j])
                if not cont:
                    break
                body_lines.append(cont.group(1))
                j += 1
            callouts.append(
                _Callout(
                    type=match.group(1).lower(),
                    title=match.group(2).strip(),
                    body_lines=body_lines,
                    position_line=position_line,
                )
            )
            i = j
        else:
            i += 1
    return callouts


@register
class DcAnatomyOutsideCheckRule(FileRule):
    """Ported from npm's W70 (`w70-dc-anatomy-outside-check.mjs`)."""

    id = "W70"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = (
        "Add the missing ability/skill and failure-consequence anatomy a [!check] "
        "would carry (or move the roll into its own [!check]); state an attack "
        'roll\'s target as "AC", never "DC".'
    )
    producer = "wiki"
    pure = True
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        rel = page.rel_path
        if not rel.endswith(".md"):
            return
        if any(rel.startswith(root) for root in DOC_ROOTS):
            return
        if not any(rel.startswith(root) for root in SCOPED_ROOTS):
            return
        if rel.startswith("vault/srd/rules/") and page.frontmatter.get("status") == "srd":
            return
        if any(pattern.search(rel) for pattern in EXEMPT_PATTERNS):
            return
        if any(pattern.search("/" + rel) for pattern in EXEMPT_FILE_PATTERNS):
            return

        lines = page.raw.split("\n")
        fenced = _fenced_flags(lines)
        findings: list[Finding] = []

        # 1. Top-level tables (outside any callout). Mask frontmatter, fenced
        # code, every blockquote line, and the run-guide's "At a Glance"
        # compression section — its DCs are index copies of the real
        # [!check]/[!mechanic] anatomy living in the scene files.
        masked = list(lines)
        frontmatter_closed = not masked or masked[0].strip() != "---"
        in_at_a_glance = False
        for i in range(len(masked)):
            if not frontmatter_closed:
                if i > 0 and masked[i].strip() == "---":
                    frontmatter_closed = True
                masked[i] = ""
                continue
            h2 = _H2_RE.match(masked[i])
            if h2:
                in_at_a_glance = bool(_AT_A_GLANCE_RE.match(h2.group(1).strip()))
            if in_at_a_glance:
                masked[i] = ""
                continue
            if fenced[i] or re.match(r"^\s*>", masked[i]):
                masked[i] = ""

        def _emit(message: str, line_number: int) -> None:
            findings.append(self.finding(file=rel, line=line_number, message=message))

        _scan_tables(
            masked,
            lambda idx: idx + 1,
            lambda header, cells, raw, line_number: _check_table_row(
                header, cells, raw, lambda message: _emit(message, line_number)
            ),
        )

        # 2. Callouts: [!mechanic] tables/prose get the same anatomy check;
        # [!check] callouts get the AC-as-DC check (title says "Attack Roll"
        # but the body still calls the target number a DC).
        for callout in _find_callouts(lines):
            if callout.type == "mechanic":
                has_table = any(_is_table_row(line) for line in callout.body_lines)
                if has_table:
                    _scan_tables(
                        callout.body_lines,
                        lambda idx, _c=callout: _c.position_line + 1 + idx,
                        lambda header, cells, raw, line_number: _check_table_row(
                            header, cells, raw, lambda message: _emit(message, line_number)
                        ),
                    )
                else:
                    full_text = " ".join(callout.body_lines)
                    if DC_PATTERN.search(full_text):
                        ability_ok = bool(ABILITY_SKILL_PATTERN.search(full_text))
                        consequence_ok = bool(CONSEQUENCE_TERM_PATTERN.search(full_text))
                        if not ability_ok or not consequence_ok:
                            missing = (
                                "no ability/skill and no failure consequence"
                                if not ability_ok and not consequence_ok
                                else "no ability/skill"
                                if not ability_ok
                                else "no failure consequence"
                            )
                            _emit(
                                f"[!mechanic] states a bare DC with {missing} — state the "
                                "ability/skill the DC targets and what a failed roll does, or "
                                "move a genuine roll-gated branch to its own [!check] "
                                "(vault/campaigns/.claude/skills/callouts/references/mechanic.md)",
                                callout.position_line,
                            )

            if callout.type == "check":
                title = callout.title
                skill_segment = _DASH_SPLIT_RE.split(title)[0] if title else title
                body_text = " ".join(callout.body_lines)
                if (
                    re.search(r"\battack\b", skill_segment, re.IGNORECASE)
                    and DC_PATTERN.search(body_text)
                    and not AC_PAREN_PATTERN.search(body_text)
                ):
                    _emit(
                        f'[!check] "{title}" describes an attack roll\'s target as "DC" — '
                        "attack rolls target Armor Class, never a DC; state it as \"AC <n>\" "
                        "(5e SRD core mechanics; vault/campaigns/.claude/skills/callouts/"
                        "references/check.md)",
                        callout.position_line,
                    )

        # 3. The AC-as-DC parenthetical tell, anywhere on the page (prose, a
        # table cell, or inside any callout body) — precise and low-noise
        # enough to check independent of callout scoping.
        frontmatter_closed2 = not lines or lines[0].strip() != "---"
        for i, text in enumerate(lines):
            if not frontmatter_closed2:
                if i > 0 and text.strip() == "---":
                    frontmatter_closed2 = True
                continue
            if fenced[i]:
                continue
            match = AC_PAREN_PATTERN.search(text)
            if match:
                _emit(
                    f'"{match.group(0)}" describes an attack roll\'s target as "DC" — attack '
                    'rolls target Armor Class, never a DC; state it as "AC <n>" (5e SRD core '
                    "mechanics; vault/campaigns/.claude/skills/callouts/references/check.md)",
                    i + 1,
                )

        yield from findings
