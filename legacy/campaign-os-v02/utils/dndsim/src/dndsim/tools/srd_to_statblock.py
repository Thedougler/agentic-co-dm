"""Deterministic converter: vault/**'s plain bullet+table stat
block -> a ```statblock fence (dndsim's native fence, ADR-0009), so the SRD
corpus becomes sim-parseable. Verbatim structural extraction only: copies
existing prose into ``desc`` fields, never rewords, never invents a number.
Frontmatter is preserved byte-for-byte (provenance intact); only the body's
stat-block section is replaced.

Scope: name/size/type/alignment/ac/hp/speed/stats/saves/damage-tags/senses/
languages/cr plus the five action sections (Traits, Actions, Bonus Actions,
Reactions, Legendary Actions).
Attack-string parsing and the ``sim:`` extension namespace are a later
slice — this tool only extracts and re-renders the source prose, it does
not interpret it.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

ABILITY_ORDER: tuple[str, ...] = ("STR", "DEX", "CON", "INT", "WIS", "CHA")
ABILITY_KEY: dict[str, str] = {
    "STR": "str",
    "DEX": "dex",
    "CON": "con",
    "INT": "int",
    "WIS": "wis",
    "CHA": "cha",
}
SECTION_HEADINGS: dict[str, str] = {
    "Traits": "traits",
    "Actions": "actions",
    "Bonus Actions": "bonus_actions",
    "Reactions": "reactions",
    "Legendary Actions": "legendary_actions",
}

_FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
_BULLET_RE = re.compile(r"^-\s*\*\*(.+?)\*\*\s*:?\s*(.*)$")
_TYPE_RE = re.compile(r"^(\w+)\s+([\w\s]+?)(?:\s*\(([^)]+)\))?,\s*(.+)$")
_AC_RE = re.compile(r"^(\d+)\s*(?:\(([^)]+)\))?")
_HP_RE = re.compile(r"^(\d+)\s*(?:\(([^)]+)\))?")
_CR_RE = re.compile(r"^([\d/]+)")
_STAT_TABLE_HEADER = "|STAT|SCORE|MOD|SAVE|"
_HEADING_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)
_ACTION_ENTRY_RE = re.compile(r"\*\*\*(.+?)\.\*\*\*")
_NAME_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
_WIKILINK_RE = re.compile(r"\[\[(?:[^\]]*\|)?([^\]]*)\]\]")


class SrdToStatblockError(ValueError):
    """A source page does not match the SRD bullet+table shape this tool converts."""


def _fail(source: str, message: str) -> None:
    raise SrdToStatblockError(f"srd-to-statblock: {source} — {message}")


@dataclass(frozen=True)
class ActionEntry:
    name: str
    desc: str


@dataclass(frozen=True)
class ParsedMonster:
    source: str
    frontmatter: str
    name: str
    size: str | None
    creature_type: str | None
    alignment: str | None
    ac: int
    ac_note: str | None
    hp: int
    hit_dice: str | None
    speed: str | None
    stats: list[int]
    saves: list[dict[str, int]]
    senses: str | None
    languages: str | None
    cr: str | None
    damage_resistances: str | None
    damage_vulnerabilities: str | None
    damage_immunities: str | None
    condition_immunities: str | None
    traits: list[ActionEntry] = field(default_factory=list)
    actions: list[ActionEntry] = field(default_factory=list)
    bonus_actions: list[ActionEntry] = field(default_factory=list)
    reactions: list[ActionEntry] = field(default_factory=list)
    legendary_actions: list[ActionEntry] = field(default_factory=list)


def split_frontmatter(markdown: str, source: str) -> tuple[str, str]:
    """Split the page into (frontmatter, body). Frontmatter kept verbatim."""
    m = _FRONTMATTER_RE.match(markdown)
    if m is None:
        _fail(source, "no frontmatter block found")
    assert m is not None  # _fail always raises
    return m.group(0), markdown[m.end() :]


def parse_bullet_line(line: str) -> tuple[str, str] | None:
    """ "- **Label:** value" or "- **Label**: value" or "- **Label** value" -> (label, value)."""
    m = _BULLET_RE.match(line.strip())
    if m is None:
        return None
    label = _WIKILINK_RE.sub(r"\1", m.group(1))
    return label.rstrip(":").strip().lower(), m.group(2).strip()


def parse_type_line(value: str, source: str) -> tuple[str, str, str]:
    # "Huge Dragon (Chromatic), Chaotic Evil" / "Large Ooze, Unaligned"
    m = _TYPE_RE.match(value)
    if m is None:
        _fail(source, f'unparseable Type line: "{value}"')
    assert m is not None
    return m.group(1), m.group(2).strip().lower(), m.group(4).strip()


def parse_ac_line(value: str) -> tuple[int, str | None]:
    m = _AC_RE.match(value)
    assert m is not None
    return int(m.group(1)), m.group(2)


def parse_hp_line(value: str) -> tuple[int, str | None]:
    m = _HP_RE.match(value)
    assert m is not None
    return int(m.group(1)), m.group(2)


def parse_cr_line(value: str) -> str:
    m = _CR_RE.match(value.strip())
    return m.group(1) if m else value.strip()


def split_damage_condition(value: str) -> tuple[str | None, str | None]:
    """damage/condition split on the SRD's "damage types; conditions" convention."""
    parts = [p.strip() for p in value.split(";") if p.strip() != ""]
    damage = parts[0] if len(parts) > 0 else None
    condition = parts[1] if len(parts) > 1 else None
    return damage, condition


def parse_stat_table(
    lines: list[str], cursor: int, source: str
) -> tuple[list[int], list[dict[str, int]], int]:
    # lines[cursor] is the |STAT|SCORE|MOD|SAVE| header; +1 is the --- separator.
    stats: list[int] = []
    saves: list[dict[str, int]] = []
    i = cursor + 2
    for ability in ABILITY_ORDER:
        if i >= len(lines):
            _fail(source, f"stat table truncated before {ability}")
        row = lines[i]
        cells = [c.strip() for c in row.split("|") if c.strip() != ""]
        if not cells or cells[0] != ability:
            _fail(
                source,
                f'stat table row {i} expected {ability}, got "{cells[0] if cells else ""}"',
            )
        score = int(cells[1])
        mod = int(cells[2].replace("+", ""))
        save = int(cells[3].replace("+", ""))
        stats.append(score)
        if save != mod:
            saves.append({ABILITY_KEY[ability]: save})
        i += 1
    return stats, saves, i


def parse_action_section(text: str) -> list[ActionEntry]:
    """Parse one `## Heading` section's `***Name.*** desc...` entries, verbatim."""
    entries: list[ActionEntry] = []
    matches = list(_ACTION_ENTRY_RE.finditer(text))
    for i, m in enumerate(matches):
        name = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        desc = re.sub(r"\s+", " ", text[start:end].strip())
        if name == "" or desc == "":
            continue
        entries.append(ActionEntry(name=name, desc=desc))
    return entries


def yaml_quote(value: object) -> str:
    escaped = str(value).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def render_action_entry(entry: ActionEntry, indent: str = "  ") -> str:
    lines = [f"{indent}- name: {yaml_quote(entry.name)}"]
    lines.append(f"{indent}  desc: {yaml_quote(entry.desc)}")
    return "\n".join(lines)


def parse_srd_monster_page(markdown: str, source: str) -> ParsedMonster:
    """Parse a full SRD monster page body into the fields the statblock fence needs."""
    frontmatter, body = split_frontmatter(markdown, source)
    name_match = _NAME_RE.search(body)
    if name_match is None:
        _fail(source, 'no "# Name" heading found')
    assert name_match is not None
    name = name_match.group(1).strip()

    lines = re.split(r"\r?\n", body)
    bullet_fields: dict[str, str] = {}
    stat_table_idx = -1

    for i, line in enumerate(lines):
        if line.strip().startswith(_STAT_TABLE_HEADER):
            stat_table_idx = i
            continue
        if re.match(r"^##\s+", line):
            break
        bullet = parse_bullet_line(line)
        if bullet is not None:
            bullet_fields[bullet[0]] = bullet[1]

    if stat_table_idx == -1:
        _fail(source, "no |STAT|SCORE|MOD|SAVE| table found")
    stats, saves, _next_index = parse_stat_table(lines, stat_table_idx, source)

    if "type" not in bullet_fields:
        _fail(source, "no **Type:** bullet found")
    if "armor class" not in bullet_fields:
        _fail(source, "no **Armor Class:** bullet found")
    if "hit points" not in bullet_fields:
        _fail(source, "no **Hit Points:** bullet found")

    size, creature_type, alignment = parse_type_line(bullet_fields["type"], source)
    ac, ac_note = parse_ac_line(bullet_fields["armor class"])
    hp, hit_dice = parse_hp_line(bullet_fields["hit points"])
    speed = bullet_fields.get("speed")
    senses = bullet_fields.get("senses")
    languages = bullet_fields.get("languages")
    cr = parse_cr_line(bullet_fields["cr"]) if "cr" in bullet_fields else None

    resist = (
        split_damage_condition(bullet_fields["resistances"])
        if "resistances" in bullet_fields
        else None
    )
    vulnerable = (
        split_damage_condition(bullet_fields["vulnerabilities"])
        if "vulnerabilities" in bullet_fields
        else None
    )
    immune = (
        split_damage_condition(bullet_fields["immunities"])
        if "immunities" in bullet_fields
        else None
    )

    # Section bodies, keyed by native fence key. The reference (srd-to-statblock.mjs)
    # slices `body` by a line-count index, not a char offset — since a line-count is
    # always <= the true char offset of the first "##" heading for real prose, that
    # slice is a harmless superset of the heading section; searching the whole `body`
    # here is behaviorally identical (no "##" heading appears before the first match,
    # so headingRe finds the same matches either way).
    heading_matches = list(_HEADING_RE.finditer(body))
    sections: dict[str, list[ActionEntry]] = {}
    for i, hm in enumerate(heading_matches):
        title = hm.group(1).strip()
        key = SECTION_HEADINGS.get(title)
        if key is None:
            continue  # e.g. a stray "## Lair Actions" variant — left for a follow-up pass
        start = hm.end()
        end = heading_matches[i + 1].start() if i + 1 < len(heading_matches) else len(body)
        sections[key] = parse_action_section(body[start:end])

    condition_clauses = (
        resist[1] if resist else None,
        vulnerable[1] if vulnerable else None,
        immune[1] if immune else None,
    )
    condition_immunities = ", ".join(c for c in condition_clauses if c) or None

    return ParsedMonster(
        source=source,
        frontmatter=frontmatter,
        name=name,
        size=size,
        creature_type=creature_type,
        alignment=alignment,
        ac=ac,
        ac_note=ac_note,
        hp=hp,
        hit_dice=hit_dice,
        speed=speed,
        stats=stats,
        saves=saves,
        senses=senses,
        languages=languages,
        cr=cr,
        damage_resistances=resist[0] if resist else None,
        damage_vulnerabilities=vulnerable[0] if vulnerable else None,
        damage_immunities=immune[0] if immune else None,
        condition_immunities=condition_immunities,
        traits=sections.get("traits", []),
        actions=sections.get("actions", []),
        bonus_actions=sections.get("bonus_actions", []),
        reactions=sections.get("reactions", []),
        legendary_actions=sections.get("legendary_actions", []),
    )


def render_statblock_page(parsed: ParsedMonster) -> str:
    """Render the parsed fields as a full page: frontmatter (verbatim) + `# Name`
    + `## Stats & Combat` fence."""
    yaml_lines: list[str] = []
    yaml_lines.append("layout: Basic 5e Layout")
    yaml_lines.append(f"name: {yaml_quote(parsed.name)}")
    if parsed.size:
        yaml_lines.append(f"size: {parsed.size}")
    if parsed.creature_type:
        yaml_lines.append(f"type: {parsed.creature_type}")
    if parsed.alignment:
        yaml_lines.append(f"alignment: {yaml_quote(parsed.alignment)}")
    ac_suffix = f"\nac_note: {yaml_quote(parsed.ac_note)}" if parsed.ac_note else ""
    yaml_lines.append(f"ac: {parsed.ac}{ac_suffix}")
    yaml_lines.append(f"hp: {parsed.hp}")
    if parsed.hit_dice:
        yaml_lines.append(f"hit_dice: {yaml_quote(parsed.hit_dice)}")
    if parsed.speed:
        yaml_lines.append(f"speed: {yaml_quote(parsed.speed)}")
    yaml_lines.append(f"stats: [{', '.join(str(s) for s in parsed.stats)}]")
    if len(parsed.saves) > 0:
        yaml_lines.append("saves:")
        for s in parsed.saves:
            k, v = next(iter(s.items()))
            yaml_lines.append(f"  - {k}: {v}")
    if parsed.damage_resistances:
        yaml_lines.append(f"damage_resistances: {yaml_quote(parsed.damage_resistances)}")
    if parsed.damage_vulnerabilities:
        yaml_lines.append(f"damage_vulnerabilities: {yaml_quote(parsed.damage_vulnerabilities)}")
    if parsed.damage_immunities:
        yaml_lines.append(f"damage_immunities: {yaml_quote(parsed.damage_immunities)}")
    if parsed.condition_immunities:
        yaml_lines.append(f"condition_immunities: {yaml_quote(parsed.condition_immunities)}")
    if parsed.senses:
        yaml_lines.append(f"senses: {yaml_quote(parsed.senses)}")
    if parsed.languages:
        yaml_lines.append(f"languages: {yaml_quote(parsed.languages)}")
    if parsed.cr:
        cr_value = yaml_quote(parsed.cr) if re.match(r"^\d+/\d+$", parsed.cr) else parsed.cr
        yaml_lines.append(f"cr: {cr_value}")

    if len(parsed.traits) > 0:
        yaml_lines.append("traits:")
        for t in parsed.traits:
            yaml_lines.append(render_action_entry(t))
    if len(parsed.actions) > 0:
        yaml_lines.append("actions:")
        for a in parsed.actions:
            yaml_lines.append(render_action_entry(a))
    if len(parsed.bonus_actions) > 0:
        yaml_lines.append("bonus_actions:")
        for a in parsed.bonus_actions:
            yaml_lines.append(render_action_entry(a))
    if len(parsed.reactions) > 0:
        yaml_lines.append("reactions:")
        for a in parsed.reactions:
            yaml_lines.append(render_action_entry(a))
    if len(parsed.legendary_actions) > 0:
        yaml_lines.append("legendary_actions:")
        for a in parsed.legendary_actions:
            yaml_lines.append(render_action_entry(a))

    fence = "\n".join(["```statblock", *yaml_lines, "```"])
    return f"{parsed.frontmatter}\n# {parsed.name}\n\n## Stats & Combat\n\n{fence}\n"


def convert_file(path: str | Path, *, write: bool = False) -> str:
    p = Path(path)
    markdown = p.read_text(encoding="utf-8")
    parsed = parse_srd_monster_page(markdown, str(path))
    rendered = render_statblock_page(parsed)
    if write:
        p.write_text(rendered, encoding="utf-8")
    return rendered
