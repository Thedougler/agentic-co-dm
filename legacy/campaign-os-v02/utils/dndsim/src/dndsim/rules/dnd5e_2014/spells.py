"""The spell-library Importer (issue #48; ADR-0009).

A statblock's ``sim.spellcasting`` pools reference spells **by name**; this
module resolves that name (exact slug -> ``-spell`` disambiguation suffix ->
frontmatter ``aliases:``) against its SRD page
(``vault/srd/spells/<school>/<slug>.md``) and compiles the pool's
``known:`` list into ordinary :data:`~dndsim.rules.dnd5e_2014.attack_string.Action`
+ :class:`~dndsim.rules.dnd5e_2014.sim_extension.ActionSim` pairs (attacks,
saves, heals) or ability :class:`~dndsim.rules.dnd5e_2014.sim_extension.
ModifierBase` instances (self-buffs) — the exact vocabulary
:mod:`dndsim.rules.dnd5e_2014.compile` already compiles for a statblock's
own actions/abilities. ``compile_statblock`` calls
:func:`compile_spellcasting` once per declared pool and merges its output
into that same loop (README's own words: "the simulator and policy know
nothing about spells" — this generalizes the property #43's docstring
already claims for the whole Rules pack).

Declared content this engine has no primitive for (a multi-beam attack, a
save's re-save timing, a slot cost on a modifier kind with no ``cost``
field) degrades explicitly: a warning naming what was lost, never a silent
drop — the same contract ``sim.notes`` already documents by convention on
real vault pages (``hex.md``, ``bless.md``, ...).
"""

from __future__ import annotations

import re
from collections.abc import Callable
from collections.abc import Set as AbstractSet
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, ClassVar, Final, Literal

import yaml
from pydantic import BaseModel, ConfigDict, model_validator

from dndsim.core.importer import Importer, importers
from dndsim.rules.dnd5e_2014.attack_string import (
    Action,
    ActionUsage,
    AttackAction,
    DamageGroup,
    OnFail,
    OnHitEffect,
    SaveAction,
    TargetClause,
    UnmodeledAction,
)
from dndsim.rules.dnd5e_2014.dice import DiceExprError, parse_dice_expr, validate_dice_expr
from dndsim.rules.dnd5e_2014.sim_extension import (
    EFFECT_TAGS,
    MODIFIER_KINDS,
    ActionSim,
    HealSpec,
    ModifierBase,
    ResourceCost,
    SpellcastingPool,
    TempHpModifier,
    describe_modifier,
)

# --- parse seam --------------------------------------------------------------

_ACTION_COSTS: Final[frozenset[str]] = frozenset({"action", "bonus", "reaction"})


class SpellCompileError(ValueError):
    """A spellcasting pool references an undeclared resource, or a spell name resolves to
    nothing."""


def _check_dice(expr: str, field_name: str) -> None:
    try:
        validate_dice_expr(expr, field_name)
    except DiceExprError as err:
        raise ValueError(str(err)) from err


class SpellDamage(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    dice: str
    type: str

    @model_validator(mode="after")
    def _check(self) -> SpellDamage:
        _check_dice(self.dice, "dice")
        return self


class SpellSaveSpec(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    ability: str


class SpellTargets(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    area: bool = False
    count: int | None = None
    radius: int | None = None


class SpellEffect(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    effect: str
    escape_dc: int | None = None
    # A re-save/re-roll rider (issue #63's save_ends interlock) — carried
    # through onto the compiled OnHitEffect/EffectRider, consumed by
    # combat.py's EffectTracker.tick_saves at the bearer's own end-of-turn.
    # `timing`/`also_on_damage` sub-keys ride along but only `end_of_turn`
    # re-saves are modeled; `also_on_damage` (an extra mid-turn re-save on
    # taking damage) is NOT wired (NOT_DONE — see combat.py's tick_saves).
    save_ends: dict[str, Any] | None = None


class SpellHeal(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    dice: str
    add_ability_mod: bool | None = None

    @model_validator(mode="after")
    def _check(self) -> SpellHeal:
        _check_dice(self.dice, "heal.dice")
        return self


class SpellTempHp(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    amount: float


class SpellPerSlotAbove(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    damage_dice: str | None = None
    heal_dice: str | None = None
    attack_count: int | None = None


class SpellScaling(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    per_slot_above: SpellPerSlotAbove | None = None


class CantripOverride(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    attack_count: int | None = None
    damage: list[SpellDamage] | None = None


class SpellSimBlock(BaseModel):
    """A spell's ``sim:`` sub-map — README § Spell library's schema."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str | None = None
    action_cost: str | None = None
    attack_type: Literal["melee_spell", "ranged_spell"] | None = None
    attack_count: int | None = None
    damage: list[SpellDamage] | None = None
    save: SpellSaveSpec | None = None
    half_on_save: bool | None = None
    targets: SpellTargets | None = None
    range: float | None = None
    reach: float | None = None
    concentration: bool | None = None
    effects: list[SpellEffect] | None = None
    heal: SpellHeal | None = None
    temp_hp: SpellTempHp | None = None
    # Both carry their own `kind`/shape matching a sim_extension Modifier
    # directly (real content: `retaliate: { kind: retaliate, ... }`,
    # `modifier: { kind: extra_damage, ... }`) — validated at compile time
    # via describe_modifier, not here, matching how a statblock's own
    # sim.abilities entries are validated.
    retaliate: dict[str, Any] | None = None
    modifier: dict[str, Any] | None = None
    scaling: SpellScaling | None = None
    cantrip_scaling: dict[int, CantripOverride] | None = None
    notes: str | None = None

    @model_validator(mode="after")
    def _check(self) -> SpellSimBlock:
        if self.action_cost is not None and self.action_cost not in _ACTION_COSTS:
            raise ValueError(f"action_cost: must be one of {sorted(_ACTION_COSTS)}")
        modeled = (
            self.attack_type is not None
            or self.save is not None
            or self.heal is not None
            or self.temp_hp is not None
            or self.retaliate is not None
            or self.modifier is not None
        )
        if not modeled:
            raise ValueError(
                "sim: models nothing — needs an attack_type, save, heal, temp_hp, retaliate, "
                "or modifier"
            )
        return self


class SpellContent(BaseModel):
    """Normalized spell content for one SRD page (the parse seam)."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    source: str
    name: str
    level: int
    school: str | None = None
    classes: list[str] | str | None = None
    desc: str | None = None
    sim: SpellSimBlock

    @model_validator(mode="after")
    def _check(self) -> SpellContent:
        if self.name == "":
            raise ValueError("name: required")
        if not (0 <= self.level <= 9):
            raise ValueError("level: must be an integer 0..9")
        return self


_SPELL_FENCE_RE = re.compile(r"```spell\s*\n([\s\S]*?)```")


def parse_spell_page(text: str, source_path: str) -> SpellContent | None:
    """Extract the ``## Simulation Data`` ````spell` YAML block from a spell
    page and parse it into :class:`SpellContent`.  Returns ``None`` when the
    page carries no sim data (e.g. a flavour-only page)."""
    m = _SPELL_FENCE_RE.search(text)
    if m is None:
        return None
    data = yaml.safe_load(m.group(1))
    if not isinstance(data, dict):
        return None
    sim_raw = data.get("sim")
    if sim_raw is None:
        return None
    return SpellContent(
        source=source_path,
        name=data.get("name", ""),
        level=data.get("level", 0),
        school=data.get("school"),
        classes=data.get("classes"),
        desc=data.get("desc"),
        sim=SpellSimBlock.model_validate(sim_raw),
    )


IMPORTER_ID = "dnd5e_2014:importer/spell"


@importers.register(IMPORTER_ID)
class SpellImporter(Importer[SpellContent]):
    """Reads an SRD spell page (ADR-0009's Importer contract)."""

    id: ClassVar[str] = IMPORTER_ID

    def parse(self, text: str, source_path: str) -> SpellContent | None:
        return parse_spell_page(text, source_path)


# --- name resolution: exact slug -> "-spell" suffix -> frontmatter alias ----

# spells.py -> src/dndsim/rules/dnd5e_2014/spells.py; parents[6] is the repo
# root (campaign-os), matching REPO_ROOT's derivation in lint/run.py. Anchored
# to __file__ rather than left cwd-relative — a bare relative string only
# resolved when the process happened to be invoked from repo root.
_REPO_ROOT = Path(__file__).resolve().parents[6]
# One directory per school of magic — the vault has no flat spell directory,
# and `vault/srd/spells` (the path this now names) contains spell files.
SPELL_DIRS: Final[tuple[str, ...]] = tuple(
    str(_REPO_ROOT / "vault" / "srd" / "spells" / school)
    for school in (
        "abjuration",
        "conjuration",
        "divination",
        "enchantment",
        "evocation",
        "illusion",
        "necromancy",
        "transmutation",
    )
)

_SLUG_STRIP_RE = re.compile(r"[^a-z0-9]+")
_APOSTROPHE_RE = re.compile(r"['’]")
_FRONTMATTER_RE = re.compile(r"^---\r?\n([\s\S]*?)\r?\n---", re.MULTILINE)
_ALIASES_RE = re.compile(r"aliases:\s*\[([^\]]*)\]")

_def_cache: dict[str, SpellContent] = {}
_alias_index: dict[str, Path] | None = None


def spell_slugify(name: str) -> str:
    """ "Hunter's Mark" -> "hunters-mark" — apostrophes vanish rather than hyphenate."""
    stripped = _APOSTROPHE_RE.sub("", name.lower())
    return _SLUG_STRIP_RE.sub("-", stripped).strip("-")


def clear_spell_cache() -> None:
    """Test hook: clear the module-level resolution caches."""
    global _alias_index
    _def_cache.clear()
    _alias_index = None


def _build_alias_index(dirs: tuple[str, ...]) -> dict[str, Path]:
    index: dict[str, Path] = {}
    for d in dirs:
        dpath = Path(d)
        if not dpath.is_dir():
            continue
        for f in sorted(dpath.iterdir()):
            if f.suffix != ".md":
                continue
            text = f.read_text(encoding="utf-8")
            fm = _FRONTMATTER_RE.search(text)
            if fm is None:
                continue
            am = _ALIASES_RE.search(fm.group(1))
            if am is None or am.group(1).strip() == "":
                continue
            for alias in am.group(1).split(","):
                clean = alias.strip().strip("'\"")
                if clean != "":
                    index[spell_slugify(clean)] = f
    return index


def load_spell_def(name: str, *, dirs: tuple[str, ...] = SPELL_DIRS) -> SpellContent:
    """Resolve a spell NAME to its page: exact slug -> ``-spell`` disambiguation
    suffix -> frontmatter ``aliases:`` -> a loud error naming near-miss
    candidates. No fuzzy matching."""
    global _alias_index
    slug = spell_slugify(name)
    cached = _def_cache.get(slug)
    if cached is not None:
        return cached

    path: Path | None = None
    for d in dirs:
        dpath = Path(d)
        for candidate in (f"{slug}.md", f"{slug}-spell.md"):
            p = dpath / candidate
            if p.is_file():
                path = p
                break
        if path is not None:
            break

    if path is None:
        if _alias_index is None:
            _alias_index = _build_alias_index(dirs)
        path = _alias_index.get(slug)

    if path is None:
        head = slug.split("-")[0]
        near: list[str] = []
        for d in dirs:
            dpath = Path(d)
            if not dpath.is_dir():
                continue
            near.extend(f.name for f in dpath.iterdir() if f.suffix == ".md" and head in f.name)
        near_text = f"; near matches: {', '.join(sorted(near)[:5])}" if near else ""
        raise SpellCompileError(
            f'spell "{name}" — no page found in {", ".join(dirs)} '
            f"(tried {slug}.md, {slug}-spell.md, aliases){near_text}"
        )

    text = path.read_text(encoding="utf-8")
    content = parse_spell_page(text, str(path))
    if content is None:
        raise SpellCompileError(f'spell "{name}" — {path} not yet modeled (no sim data on page)')
    _def_cache[slug] = content
    return content


# --- compile: SpellcastingPool -> ordinary Action/ActionSim/Modifier -------


@dataclass(frozen=True, slots=True)
class CompiledSpellcasting:
    """One pool's ``known:`` list compiled to what ``compile_statblock``'s
    existing machinery already consumes — no new field on
    :class:`~dndsim.rules.dnd5e_2014.compile.CompiledStatblock`."""

    actions: tuple[Action, ...] = ()
    action_sim: dict[str, ActionSim] = field(default_factory=dict)
    abilities: tuple[ModifierBase, ...] = ()
    warnings: tuple[str, ...] = ()


def _cantrip_overrides(sim: SpellSimBlock, caster_level: float | None) -> CantripOverride | None:
    table = sim.cantrip_scaling
    if not table or caster_level is None:
        return None
    best: CantripOverride | None = None
    for threshold in sorted(table):
        if caster_level >= threshold:
            best = table[threshold]
    return best


def _scale_dice_str(dice: str, per_slot_dice: str, levels_above: int) -> str:
    """Bump only the LEADING ``NdM`` term's count; the rest of the string
    (a trailing ``+5``, ...) is preserved verbatim — port of
    ``spellcasting.mjs``'s ``scaleDamage``."""
    if levels_above == 0:
        return dice
    parsed = parse_dice_expr(dice)
    extra = parse_dice_expr(per_slot_dice)
    if not parsed.dice or not extra.dice:
        return dice
    first, bump = parsed.dice[0], extra.dice[0]
    if bump.sides != first.sides:
        return dice
    bumped = f"{first.count + bump.count * levels_above}d{first.sides}"
    return re.sub(r"^\s*\d*d\d+", bumped, dice.strip())


def _resolve_damage(
    sim: SpellSimBlock, over: CantripOverride | None, levels_above: int
) -> list[SpellDamage] | None:
    base = over.damage if (over is not None and over.damage is not None) else sim.damage
    if base is None:
        return None
    per_slot = sim.scaling.per_slot_above if sim.scaling is not None else None
    if per_slot is None or per_slot.damage_dice is None or levels_above == 0:
        return base
    scaled_first = SpellDamage(
        dice=_scale_dice_str(base[0].dice, per_slot.damage_dice, levels_above), type=base[0].type
    )
    return [scaled_first, *base[1:]]


def _compile_effects(
    effects: list[SpellEffect] | None, spell_name: str, default_dc: float
) -> tuple[list[OnHitEffect], list[str]]:
    """Compile a spell's `effects:` list to riders — issue #63's save_ends
    interlock: a `save_ends` clause now rides through onto the compiled
    rider (`combat.py`'s `_resolve_save_primitive`/`EffectTracker.tick_saves`
    consume it) instead of degrading to a warning. `save_ends.dc`, when the
    fence omits it (real content: `hideous-laughter.md` never authors one),
    defaults to the caster's own spell save DC — port of
    ``spellcasting.mjs``'s own `e.save_ends.dc === undefined ? {...,
    dc: pool.dc} : e` backfill."""
    riders: list[OnHitEffect] = []
    warnings: list[str] = []
    for e in effects or []:
        tag = e.effect.lower()
        if tag not in EFFECT_TAGS:
            warnings.append(
                f'{spell_name}: effect "{tag}" not modeled — no matching condition/rider tag'
            )
            continue
        save_ends = e.save_ends
        if save_ends is not None and save_ends.get("dc") is None:
            save_ends = {**save_ends, "dc": default_dc}
        riders.append(OnHitEffect(effect=tag, escape_dc=e.escape_dc, save_ends=save_ends))
    return riders, warnings


def _compile_targets(targets: SpellTargets | None) -> TargetClause:
    if targets is None or not targets.area:
        return TargetClause(area=False, count=1)
    return TargetClause(area=True, count=None, radius=targets.radius, cone=None)


def _map_action_cost(
    action_cost: str | None, spell_name: str, warnings: list[str]
) -> Literal["action", "bonus"] | None:
    if action_cost in (None, "action", "bonus"):
        return action_cost  # type: ignore[return-value]
    warnings.append(
        f'{spell_name}: action_cost "{action_cost}" has no compiled-action equivalent — '
        "compiled as a standard action"
    )
    return None


def compile_spellcasting(
    pool: SpellcastingPool,
    resource_ids: AbstractSet[str],
    source: str,
    *,
    load: Callable[[str], SpellContent] = load_spell_def,
) -> CompiledSpellcasting:
    """Compile one ``sim.spellcasting[]`` pool's ``known:`` list into ordinary
    Action/ActionSim pairs (attacks, saves, heals) and ability Modifiers
    (self-buffs) — port of ``spellcasting.mjs``'s ``compileSpellcasting``."""
    slots = pool.slots or {}
    for lvl, resource_id in slots.items():
        if resource_id not in resource_ids:
            raise SpellCompileError(
                f'spellcasting: {source} — spellcasting.slots.{lvl}: "{resource_id}" is not a '
                "declared sim.resources id"
            )
    slot_levels = sorted(slots)

    actions: list[Action] = []
    action_sim: dict[str, ActionSim] = {}
    abilities: list[ModifierBase] = []
    warnings: list[str] = []

    for name in pool.known:
        spell = load(name)
        sim = spell.sim
        base_id = sim.id or spell_slugify(spell.name)

        casts: list[tuple[str, str, ResourceCost | None, int]]
        if spell.level == 0:
            casts = [(base_id, spell.name, None, 0)]
        else:
            usable = [lvl for lvl in slot_levels if lvl >= spell.level]
            if not usable:
                warnings.append(
                    f"{spell.name}: no declared slot at level >= {spell.level} — not compiled"
                )
                continue
            per_slot = sim.scaling.per_slot_above if sim.scaling is not None else None
            emit = usable if per_slot is not None else usable[:1]
            multi = len(emit) > 1
            casts = [
                (
                    f"{base_id}-l{lvl}" if multi else base_id,
                    f"{spell.name} (L{lvl})" if multi else spell.name,
                    ResourceCost(resource=slots[lvl], spend=1),
                    lvl - spell.level,
                )
                for lvl in emit
            ]

        for cast_id, action_name, cost, levels_above in casts:
            over = _cantrip_overrides(sim, pool.level) if spell.level == 0 else None
            damage = _resolve_damage(sim, over, levels_above)
            action_cost = _map_action_cost(sim.action_cost, spell.name, warnings)

            if sim.heal is not None:
                heal_dice = sim.heal.dice
                per_slot = sim.scaling.per_slot_above if sim.scaling is not None else None
                if levels_above > 0 and per_slot is not None and per_slot.heal_dice is not None:
                    heal_dice = _scale_dice_str(heal_dice, per_slot.heal_dice, levels_above)
                mod_bonus = ""
                if sim.heal.add_ability_mod:
                    # SpellcastingPool allows extra keys (real vault content's own
                    # ability_mod: N) not part of its declared schema — see its docstring.
                    ability_mod: float | None = getattr(pool, "ability_mod", None)
                    if ability_mod is not None:
                        mod_bonus = f"+{int(ability_mod)}"
                    else:
                        warnings.append(
                            f"{spell.name}: add_ability_mod set but the pool declares no "
                            "ability_mod — compiled without the caster's bonus"
                        )
                actions.append(
                    UnmodeledAction(
                        name=action_name, desc=spell.desc or spell.name, usage=ActionUsage()
                    )
                )
                action_sim[action_name] = ActionSim(
                    id=cast_id,
                    cost=cost,
                    action_cost=action_cost or "action",
                    concentration=sim.concentration,
                    heal=HealSpec(dice=f"{heal_dice}{mod_bonus}"),
                )
            elif sim.attack_type is not None:
                cantrip_beams = over.attack_count if over is not None else None
                beams = (cantrip_beams if cantrip_beams is not None else sim.attack_count) or 1
                per_slot = sim.scaling.per_slot_above if sim.scaling is not None else None
                if levels_above > 0 and per_slot is not None and per_slot.attack_count is not None:
                    beams += per_slot.attack_count * levels_above
                if beams != 1:
                    warnings.append(
                        f"{spell.name}: {beams} beams/attacks not modeled — this engine has no "
                        "multi-beam attack primitive yet; compiled as a single attack"
                    )
                riders, effect_warnings = _compile_effects(sim.effects, spell.name, pool.dc)
                warnings.extend(effect_warnings)
                actions.append(
                    AttackAction(
                        name=action_name,
                        desc=spell.desc or spell.name,
                        usage=ActionUsage(),
                        attack_type=sim.attack_type,
                        to_hit=int(pool.attack_bonus or 0),
                        reach=int(sim.reach) if sim.reach is not None else None,
                        range=int(sim.range) if sim.range is not None else None,
                        damage=[DamageGroup(dice=d.dice, type=d.type) for d in (damage or [])],
                        on_hit_effects=riders,
                    )
                )
                action_sim[action_name] = ActionSim(
                    id=cast_id, cost=cost, action_cost=action_cost, concentration=sim.concentration
                )
            elif sim.save is not None:
                riders, effect_warnings = _compile_effects(sim.effects, spell.name, pool.dc)
                warnings.extend(effect_warnings)
                actions.append(
                    SaveAction(
                        name=action_name,
                        desc=spell.desc or spell.name,
                        usage=ActionUsage(),
                        dc=int(pool.dc),
                        save=str(sim.save.ability)[:3].lower(),
                        targets=_compile_targets(sim.targets),
                        on_fail=OnFail(
                            damage=[DamageGroup(dice=d.dice, type=d.type) for d in (damage or [])],
                            effects=riders,
                        ),
                        half_on_save=bool(sim.half_on_save),
                    )
                )
                action_sim[action_name] = ActionSim(
                    id=cast_id, cost=cost, action_cost=action_cost, concentration=sim.concentration
                )
            elif sim.temp_hp is not None or sim.retaliate is not None or sim.modifier is not None:
                if sim.temp_hp is not None:
                    abilities.append(TempHpModifier(amount=sim.temp_hp.amount, cost=cost))
                if sim.retaliate is not None:
                    retaliate_data = {k: v for k, v in sim.retaliate.items() if k != "kind"}
                    kind = sim.retaliate.get("kind")
                    if kind is None:
                        raise SpellCompileError(
                            f'spell: {source} — {spell.name}.sim.retaliate: "kind" is required'
                        )
                    abilities.append(
                        describe_modifier(
                            kind, source, f"{spell.name}.sim.retaliate", **retaliate_data
                        )
                    )
                if sim.modifier is not None:
                    kind = sim.modifier.get("kind")
                    if kind is None:
                        raise SpellCompileError(
                            f'spell: {source} — {spell.name}.sim.modifier: "kind" is required'
                        )
                    mod_data = {k: v for k, v in sim.modifier.items() if k not in ("kind", "cost")}
                    resolved_cost = sim.modifier.get("cost", cost)
                    namespaced = f"dnd5e_2014:modifier/{kind}"
                    modifier_cls = (
                        MODIFIER_KINDS.get(namespaced) if namespaced in MODIFIER_KINDS else None
                    )
                    if (
                        resolved_cost is not None
                        and modifier_cls is not None
                        and "cost" not in modifier_cls.model_fields
                    ):
                        resource_name = (
                            resolved_cost.resource
                            if isinstance(resolved_cost, ResourceCost)
                            else resolved_cost.get("resource")
                        )
                        warnings.append(
                            f'{spell.name}: cast cost ({resource_name}) not attached — "{kind}" '
                            "carries no cost field, so this modifier compiles free of its slot cost"
                        )
                        resolved_cost = None
                    if resolved_cost is not None:
                        mod_data["cost"] = resolved_cost
                    abilities.append(
                        describe_modifier(kind, source, f"{spell.name}.sim.modifier", **mod_data)
                    )
            if sim.notes:
                warnings.append(f"{spell.name}: {sim.notes}")

    return CompiledSpellcasting(
        actions=tuple(actions),
        action_sim=action_sim,
        abilities=tuple(abilities),
        warnings=tuple(warnings),
    )
