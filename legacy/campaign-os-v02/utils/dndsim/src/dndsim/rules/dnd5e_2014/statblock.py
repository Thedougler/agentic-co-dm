"""The native Fantasy Statblocks fence Importer (ADR-0009).

Same required keys, same tolerant normalizers (ability-key case/length,
``ac`` as int or a ``"20 (unarmored)"`` string, semicolon/comma/``and``-
split damage tags with ``nonmagical_*`` expansion, ``cr`` as a fraction or
decimal) throughout. Scope is the native fence keys only — name, ac, hp,
stats, saves, damage tags, cr, speed, senses. SRD attack prose
(``actions``/``traits``/...) and the ``sim:`` extension namespace are later
slices and are not read here.

Validation is loud: a missing required key or an unparseable value raises
:class:`StatblockParseError` naming ``source_path`` and the offending key.
An empty fence (a stub page) returns ``None``, never an error.
"""

from __future__ import annotations

import re
from typing import Any, ClassVar, Final, Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field

from dndsim.core.importer import Importer, importers
from dndsim.rules.dnd5e_2014.yaml_safe import safe_load as _yaml_safe_load

ABILITY_KEYS: Final[tuple[str, str, str, str, str, str]] = (
    "str",
    "dex",
    "con",
    "int",
    "wis",
    "cha",
)

# ```statblock ... ``` — mirrors statblock-parse.mjs's extractStatblockFence
# regex exactly (same anchoring, same tolerance for a trailing \r).
_FENCE_RE = re.compile(r"^```statblock[ \t]*\r?\n(.*?)^```[ \t]*$", re.MULTILINE | re.DOTALL)

# "Cold, Necrotic, ...; Bludgeoning, ... from Nonmagical Attacks" splits on
# comma, semicolon-separated clauses, or the word "and".
_NONMAGICAL_RE = re.compile(r"(.*)\bfrom\s+nonmagical\s+attacks", re.IGNORECASE)
_TAG_SPLIT_RE = re.compile(r",|\band\b", re.IGNORECASE)

_FRACTION_RE = re.compile(r"^\d+/\d+$")
_LEADING_INT_RE = re.compile(r"\d+")
_PARENTHETICAL_RE = re.compile(r"\(([^)]+)\)")

# --- traits (port of statblock-parse.mjs's parseTraits) --------------------
# 2024 SRD often extends the parenthetical ("3/Day, or 4/Day in Lair") —
# match the opening count only, never require the paren to close right
# after "Day"; the base (non-lair) count is the conservative number to take
# (the engine has no in-lair-vs-not state to gate the higher one).
_LEGENDARY_RESISTANCE_RE = re.compile(r"Legendary Resistance\s*\((\d+)\s*/\s*Day", re.IGNORECASE)
_PACK_TACTICS_NAME_RE = re.compile(r"^Pack Tactics$", re.IGNORECASE)
_MAGIC_RESISTANCE_NAME_RE = re.compile(r"^Magic Resistance$", re.IGNORECASE)
_SAVE_ADVANTAGE_DESC_RE = re.compile(r"advantage on\s+(\w+)\s+saving throws", re.IGNORECASE)


class StatblockParseError(ValueError):
    """A required key is missing, or a value the native fence format cannot make sense of."""


class SaveAdvantageTrait(BaseModel):
    """One statblock trait granting advantage on a class of saving throws
    (Magic Resistance, or the generic "advantage on X saving throws" prose).
    ``vs`` is ``"magic"`` for Magic Resistance (this engine treats every
    save it executes as magical — see ``combat.py``'s ``save_advantage``
    docstring) or a normalized ability key for the generic pattern."""

    model_config = ConfigDict(frozen=True)

    vs: str
    mode: Literal["advantage"] = "advantage"


class Defenses(BaseModel):
    """Damage/condition tags this creature resists, is immune to, or is vulnerable to."""

    model_config = ConfigDict(frozen=True)

    resist: list[str] = Field(default_factory=list)
    immune: list[str] = Field(default_factory=list)
    vulnerable: list[str] = Field(default_factory=list)
    condition_immune: list[str] = Field(default_factory=list)


class StatblockContent(BaseModel):
    """Normalized native-fence content for one Fantasy Statblocks page.

    Pre-primitive: this is the parse seam's output, not yet compiled to
    engine Primitives (that compile step, and the rest of the fence's keys,
    are later slices).
    """

    model_config = ConfigDict(frozen=True)

    source: str
    name: str
    size: str | None = None
    creature_type: str | None = None
    ac: int
    ac_note: str | None = None
    hp: int
    hit_dice: str | None = None
    speed: str | None = None
    senses: str | None = None
    abilities: dict[str, int]
    saves: dict[str, int]
    cr: float | None = None
    defenses: Defenses = Field(default_factory=Defenses)
    # Issue #66: parsed ``traits:`` prose (port of ``parseTraits``) — the
    # three named traits (Magic Resistance, Legendary Resistance (N/Day),
    # Pack Tactics) plus the generic "advantage on X saving throws"
    # pattern; anything else lands in ``unmodeled_traits`` plus a warning,
    # never silently dropped. Compiled into engine mechanisms by
    # ``compile.py`` — this class carries only the parsed shape.
    save_advantage: list[SaveAdvantageTrait] = Field(default_factory=list)
    #: Statblock-level conditional-advantage triggers (Pack Tactics ->
    #: ``"ally_adjacent_to_target"``) — applies to every compiled attack
    #: that carries no per-action ``advantage_if`` of its own (attack_string
    #: .py's "target_has:" prose grammar).
    advantage_if: list[str] = Field(default_factory=list)
    #: Uses/day from a matched "Legendary Resistance (N/Day...)" trait, or
    #: 0 when absent. No consumer exists in combat.py yet — see compile.py's
    #: warning for the measured (zero) cost of leaving it unmodeled.
    legendary_resistance: int = 0
    #: Trait names statblock.py's vocabulary does not recognise — an
    #: explicit, named entry (never a silent drop), mirrored by a matching
    #: warning below.
    unmodeled_traits: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


def extract_statblock_fence(markdown: str) -> str | None:
    """Return the fence's inner YAML text, or ``None`` for no fence / an empty one."""
    match = _FENCE_RE.search(markdown)
    if match is None:
        return None
    inner = match.group(1).strip()
    return inner if inner != "" else None


def _normalize_ability_key(key: str) -> str | None:
    candidate = key.strip().lower()[:3]
    return candidate if candidate in ABILITY_KEYS else None


def _normalize_bonus(value: object, source_path: str, field: str) -> int:
    if isinstance(value, bool):
        raise StatblockParseError(
            f'statblock: {source_path} — {field}: unparseable bonus "{value}"'
        )
    if isinstance(value, int | float):
        return int(value)
    try:
        return int(str(value).replace("+", "").strip())
    except ValueError:
        raise StatblockParseError(
            f'statblock: {source_path} — {field}: unparseable bonus value "{value}"'
        ) from None


def _normalize_keyed_list(
    value: object, source_path: str, field: str, key_normalizer: Any
) -> dict[str, int]:
    """``saves`` comes as a list of single-key maps, or one map directly."""
    out: dict[str, int] = {}
    if value is None:
        return out
    entries = value if isinstance(value, list) else [value]
    for entry in entries:
        if not isinstance(entry, dict):
            raise StatblockParseError(
                f"statblock: {source_path} — {field}: expected a mapping entry"
            )
        for raw_key, raw_value in entry.items():
            key = key_normalizer(str(raw_key))
            if key is not None:
                out[key] = _normalize_bonus(raw_value, source_path, field)
    return out


def _normalize_ac(block: dict[str, Any], source_path: str) -> tuple[int, str | None]:
    raw = block["ac"]
    ac_note = block.get("ac_note")
    ac_class = block.get("ac_class")
    if isinstance(raw, int | float) and not isinstance(raw, bool):
        return int(raw), (ac_note if ac_note is not None else ac_class)
    text = str(raw)
    match = _LEADING_INT_RE.search(text)
    if match is None:
        raise StatblockParseError(f'statblock: {source_path} — ac: no numeric AC in "{text}"')
    if ac_note is not None:
        note = ac_note
    elif ac_class is not None:
        note = ac_class
    else:
        paren = _PARENTHETICAL_RE.search(text)
        note = paren.group(1) if paren else None
    return int(match.group(0)), note


def parse_damage_tags(value: object) -> list[str]:
    """ "Cold, Necrotic, Poison; Bludgeoning ... from Nonmagical Attacks" -> tag list.

    Sorted and deduplicated so the differential harness can compare it
    order-independently — the reference engine's tag order follows raw
    split/insertion order, which this normalization intentionally does not
    preserve.
    """
    tags: set[str] = set()
    if value is None or value == "":
        return []
    for part in str(value).split(";"):
        nonmagical = _NONMAGICAL_RE.search(part)
        if nonmagical:
            for piece in _TAG_SPLIT_RE.split(nonmagical.group(1)):
                tag = piece.strip().lower()
                if tag != "":
                    tags.add(f"nonmagical_{tag}")
            continue
        for piece in _TAG_SPLIT_RE.split(part):
            tag = piece.strip().lower()
            if tag != "":
                tags.add(tag)
    return sorted(tags)


def _parse_cr(value: object) -> float | None:
    if isinstance(value, int | float) and not isinstance(value, bool):
        return float(value)
    text = str(value if value is not None else "").strip()
    if _FRACTION_RE.match(text):
        numerator, denominator = (int(part) for part in text.split("/"))
        return numerator / denominator
    try:
        return float(text)
    except ValueError:
        return None


def _parse_traits(
    traits: object, warnings: list[str]
) -> tuple[list[SaveAdvantageTrait], list[str], int, list[str]]:
    """Port of ``statblock-parse.mjs``'s ``parseTraits`` (line 97): matches
    Legendary Resistance (N/Day, ...), Pack Tactics, Magic Resistance, and
    the generic "advantage on X saving throws" prose (ability-worded,
    under 120 chars — the same guard the reference uses to avoid matching a
    long unrelated description that merely mentions saving throws in
    passing). Anything else becomes an explicit unmodeled entry plus a
    warning — never a silent drop, exactly as the reference does and as
    ``attack_string.py`` already does for prose it cannot model.

    ``warnings`` is mutated in place (mirrors the reference's shared
    ``warnings`` array, threaded the same way ``parseActionList`` already
    receives it)."""
    save_advantage: list[SaveAdvantageTrait] = []
    advantage_if: list[str] = []
    legendary_resistance = 0
    unmodeled: list[str] = []
    if not isinstance(traits, list):
        return save_advantage, advantage_if, legendary_resistance, unmodeled
    for raw in traits:
        if not isinstance(raw, dict):
            continue
        name = str(raw.get("name") or "")
        desc = str(raw.get("desc") or "")
        lr = _LEGENDARY_RESISTANCE_RE.search(name)
        if lr:
            legendary_resistance = int(lr.group(1))
            continue
        if _PACK_TACTICS_NAME_RE.fullmatch(name.strip()):
            advantage_if.append("ally_adjacent_to_target")
            continue
        if _MAGIC_RESISTANCE_NAME_RE.fullmatch(name.strip()):
            save_advantage.append(SaveAdvantageTrait(vs="magic"))
            continue
        sav_adv = _SAVE_ADVANTAGE_DESC_RE.search(desc)
        if sav_adv is not None:
            ability = _normalize_ability_key(sav_adv.group(1))
            if ability is not None and len(desc) < 120:
                save_advantage.append(SaveAdvantageTrait(vs=ability))
                continue
        unmodeled.append(name or "(unnamed trait)")
        warnings.append(
            f"unmodeled trait: {name or '(unnamed)'} — supply mechanics via "
            "creature_overrides in a loadout file if it matters"
        )
    return save_advantage, advantage_if, legendary_resistance, unmodeled


def parse_statblock_page(markdown: str, source_path: str = "(unknown)") -> StatblockContent | None:
    """Parse one page's native statblock fence, or ``None`` for a stub page."""
    fence = extract_statblock_fence(markdown)
    if fence is None:
        return None
    try:
        block = _yaml_safe_load(fence)
    except yaml.YAMLError as err:
        raise StatblockParseError(f"statblock: YAML parse failed in {source_path}: {err}") from err
    if not isinstance(block, dict):
        return None

    for required in ("name", "ac", "hp", "stats"):
        if required not in block:
            raise StatblockParseError(f'statblock: {source_path} missing required key "{required}"')

    stats = block["stats"]
    if not isinstance(stats, list) or len(stats) != 6:
        raise StatblockParseError(
            f"statblock: {source_path} stats must be [STR,DEX,CON,INT,WIS,CHA]"
        )

    abilities: dict[str, int] = {}
    for key, score in zip(ABILITY_KEYS, stats, strict=True):
        if not isinstance(score, int | float) or isinstance(score, bool):
            raise StatblockParseError(
                f'statblock: {source_path} — stats: non-numeric score "{score}"'
            )
        abilities[key] = int(score)

    def ability_mod(score: int) -> int:
        return (score - 10) // 2

    saves = _normalize_keyed_list(block.get("saves"), source_path, "saves", _normalize_ability_key)
    for key in ABILITY_KEYS:
        if key not in saves:
            saves[key] = ability_mod(abilities[key])

    ac, ac_note = _normalize_ac(block, source_path)

    hp = block["hp"]
    if not isinstance(hp, int | float) or isinstance(hp, bool):
        raise StatblockParseError(f'statblock: {source_path} — hp: non-numeric value "{hp}"')

    warnings: list[str] = []
    save_advantage, advantage_if, legendary_resistance, unmodeled_traits = _parse_traits(
        block.get("traits"), warnings
    )

    return StatblockContent(
        source=source_path,
        name=str(block["name"]),
        size=block.get("size"),
        creature_type=block.get("type"),
        ac=ac,
        ac_note=ac_note,
        hp=int(hp),
        hit_dice=str(block["hit_dice"]) if block.get("hit_dice") is not None else None,
        speed=str(block["speed"]) if block.get("speed") is not None else None,
        senses=str(block["senses"]) if block.get("senses") is not None else None,
        abilities=abilities,
        saves=saves,
        cr=_parse_cr(block.get("cr")),
        defenses=Defenses(
            resist=parse_damage_tags(block.get("damage_resistances")),
            immune=parse_damage_tags(block.get("damage_immunities")),
            vulnerable=parse_damage_tags(block.get("damage_vulnerabilities")),
            condition_immune=parse_damage_tags(block.get("condition_immunities")),
        ),
        save_advantage=save_advantage,
        advantage_if=advantage_if,
        legendary_resistance=legendary_resistance,
        unmodeled_traits=unmodeled_traits,
        warnings=warnings,
    )


IMPORTER_ID = "dnd5e_2014:importer/statblock"


@importers.register(IMPORTER_ID)
class StatblockImporter(Importer[StatblockContent]):
    """Reads the native Fantasy Statblocks fence (ADR-0009's Importer contract)."""

    id: ClassVar[str] = IMPORTER_ID

    def parse(self, text: str, source_path: str) -> StatblockContent | None:
        return parse_statblock_page(text, source_path)
