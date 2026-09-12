"""The `sim:` extension namespace (issue #43) — the judgment layer a native
Fantasy Statblocks fence can't express (resource pools, ability modifiers,
per-action costs and overrides).

Modeled as pydantic tagged unions discriminated on `kind` (ADR-0007;
Pydantic's own documented performance guidance for closed alternatives). A
malformed value is rejected by the field's own type or a
``@model_validator``, naming the field and what was expected.

**Strictness tracks the reference clause by clause.** ``extra="forbid"``
is set exactly where `sim-extension.mjs` calls ``checkUnknownKeys`` — the
top-level `sim:` map (``TOP_LEVEL_KEYS``), a per-action `sim:` sub-map
(``ACTION_KEYS``), and `sim.position` (its own inline key loop) — so a
typo'd key there is rejected loudly by pydantic naming the offending field
(PRD user story #21). Everywhere the reference validator walks a sub-object
WITHOUT a key check — every ability modifier and its nested
``save``/``cost``/``on_fail``/``on_success``/``damage``/``effects``
sub-maps, `sim.resources[]`, `sim.save_advantage[]`, `sim.spellcasting[]`,
and a per-action ``cost``/``heal``/``on_success`` — the model sets
``extra="allow"`` to match, because real vault content carries keys there
that the reference accepts (`crissdalynn-khinriss-sheet.md`'s
``bonus_attack.id``/``.cost`` and rider ``duration``,
`delmar-fisk-sheet.md`'s rider ``save_ends``, `perrin-black-jaw-sheet.md`'s
spellcasting ``ability_mod``). Value checks are placed where the reference
places them too: the condition-tag and dice checks on ``on_fail`` live in
:class:`ActionSim`, not in the shared :class:`EffectRider`/
:class:`DamageDie` models, because ``validateActionSim`` runs them and
``validateModifier`` does not.

Registration replaces dispatch: :func:`describe_modifier` resolves a `kind`
string through :data:`MODIFIER_KINDS` to its model class — a plain
dict-backed lookup, never a branch — and no edit here is required to add a
new kind (`tests/rules/test_sim_extension.py::
test_new_modifier_kind_needs_no_registry_edit` proves it by registering one
at test scope). `SimBlock.abilities` additionally uses a static pydantic
discriminated :data:`Modifier` union for the closed, shipped vocabulary —
growing that union is normal Rules-pack maintenance (the same way a new
Mechanic ships by editing this Rules pack), not a change to the engine core.

Scenario-only kinds (`resource_budget`, `setup_round`,
`assume_rider_triggers`, `save_action_priority`) encode a scenario
assumption, not a combatant's own capability — legal in a loadout file's
`modifiers:` list, rejected on a statblock's own `sim.abilities` by
:func:`parse_sim_block`, matching `sim-extension.mjs`'s
`SCENARIO_ONLY_KINDS` check.
"""

from __future__ import annotations

from typing import Annotated, Any, Literal, NoReturn

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from dndsim.core.registry import Registry
from dndsim.rules.dnd5e_2014.conditions import CONDITION_TAGS, RIDER_EFFECT_TAGS
from dndsim.rules.dnd5e_2014.dice import DiceExprError, validate_dice_expr

EFFECT_TAGS: frozenset[str] = frozenset(CONDITION_TAGS) | frozenset(RIDER_EFFECT_TAGS)

RECHARGE_KINDS: frozenset[str] = frozenset({"long_rest", "short_rest", "round", "encounter"})
MOVEMENT_BOOST_GRANTS: frozenset[str] = frozenset({"dash", "disengage", "both"})
PERIODIC_EFFECT_TRIGGERS: frozenset[str] = frozenset({"start_of_turn_self", "start_of_turn_others"})
PERIODIC_EFFECT_EFFECTS: frozenset[str] = frozenset({"regen", "damage"})
RETALIATE_TRIGGERS: frozenset[str] = frozenset({"hit_by_melee", "hit_by_any"})
REACTION_KINDS: frozenset[str] = frozenset(
    {"damage_reduction", "damage_reduction_pct", "extra_attack", "ac_bonus", "unmodeled"}
)
REACTION_TRIGGERS: frozenset[str] = frozenset(
    {
        "self_hit",
        "self_or_ally_hit",
        "enemy_hits_adjacent_ally",
        "after_unarmed_strike_in_attack_action",
    }
)
# 2024 PHB Weapon Mastery properties (issue #71) — the SRD-2024 weapon table
# names six more (Sap, Push, Topple, Cleave, Graze, Nick,
# vault/srd/rules/weapons.md), deferred: no
# statblock's prose ever names a mastery property (it is unlocked by a
# player-facing class feature, not stated in monster/attack text), so it is
# authored exclusively as a per-action `sim:` override, same as `kind`/`die`.
WEAPON_MASTERY_KINDS: frozenset[str] = frozenset({"vex", "slow"})
ACTION_COST_KINDS: frozenset[str] = frozenset({"action", "bonus"})
TARGETING_POLICIES: frozenset[str] = frozenset(
    {"focus_fire", "focus_lowest_hp", "focus_highest_dpr", "random", "spread"}
)


class SimExtensionError(ValueError):
    """A `sim:` block or one of its ability modifiers failed validation."""


def fail(source: str, field: str, message: str) -> NoReturn:
    raise SimExtensionError(f"sim: {source} — {field}: {message}")


def _check_dice(expr: str, field: str) -> None:
    try:
        validate_dice_expr(expr, field)
    except DiceExprError as err:
        raise ValueError(str(err)) from err


class ModifierBase(BaseModel):
    """Shared config for every ability-modifier kind: frozen, open schema.

    Open because `loadout.mjs`'s ``validateModifier`` — the sole validator
    the reference runs over `sim.abilities[]` — never calls
    ``checkUnknownKeys``: it checks ``kind`` against the vocabulary and the
    per-kind ``needs`` table, and passes every other key through. Real
    content relies on that (``bonus_attack.id``, ``movement_boost.id``).
    """

    model_config = ConfigDict(frozen=True, extra="allow")

    # Not part of the reference JS vocabulary's `needs` table — every kind
    # accepts an optional free-text `source` for the loadout-authoring
    # convention seen in real content (`{ kind: advantage, source: "ally
    # Faerie Fire" }`).
    source: str | None = None


class ResourceCost(BaseModel):
    # Open: the reference checks `cost.resource`/`cost.spend` only — never
    # the cost map's key set (`sim-extension.mjs:163-170`).
    model_config = ConfigDict(frozen=True, extra="allow")

    resource: str
    spend: float = 1

    @model_validator(mode="after")
    def _check(self) -> ResourceCost:
        if self.resource == "":
            raise ValueError("cost.resource: must be a string")
        if self.spend < 1:
            raise ValueError("cost.spend: must be >= 1")
        return self


class DamageDie(BaseModel):
    """One damage entry. Open, and the dice expression is NOT parsed here:
    the reference parses `on_fail.damage[].dice` in ``validateActionSim``
    only (`sim-extension.mjs:176`), never for a modifier's own on_fail —
    so :class:`ActionSim` owns that check instead."""

    model_config = ConfigDict(frozen=True, extra="allow")

    dice: str
    type: str | None = None


class EffectRider(BaseModel):
    """One condition/rider entry. Open, and the tag is NOT checked here:
    the reference checks `on_fail.effects[].effect` against the tag
    vocabulary in ``validateActionSim`` only (`sim-extension.mjs:177-182`),
    never for a modifier's own on_fail — so :class:`ActionSim` owns that
    check. Real riders carry `duration:`/`save_ends:` alongside `effect:`."""

    model_config = ConfigDict(frozen=True, extra="allow")

    effect: str
    escape_dc: int | None = None
    # A re-save/re-roll rider (issue #63's save_ends interlock) — declared
    # (not left to `extra="allow"`) so combat.py's own consumer
    # (`_rider_save_ends`) is typed. `{save|ability, dc, ...}`, open shape —
    # the reference never key-checks it either.
    save_ends: dict[str, Any] | None = None


class SaveSpec(BaseModel):
    # Open: the reference checks `save.ability` is present and `save.dc` is
    # finite, and nothing else (`loadout.mjs:70-72`).
    model_config = ConfigDict(frozen=True, extra="allow")

    ability: str
    dc: float


class OnFailBlock(BaseModel):
    model_config = ConfigDict(frozen=True, extra="allow")

    damage: list[DamageDie] = Field(default_factory=list)
    effects: list[EffectRider] = Field(default_factory=list)


# --- the 29-entry modifier-kind vocabulary (loadout.mjs's MODIFIER_KINDS) --


class FlatToHitModifier(ModifierBase):
    kind: Literal["flat_to_hit"] = "flat_to_hit"
    value: float


class FlatDamageModifier(ModifierBase):
    kind: Literal["flat_damage"] = "flat_damage"
    value: float


class ExtraDamageModifier(ModifierBase):
    kind: Literal["extra_damage"] = "extra_damage"
    dice: str
    id: str | None = None
    type: str | None = None
    when: str | None = None
    requires: dict[str, Any] | None = None
    cost: ResourceCost | None = None
    once_per_turn: bool = False

    @model_validator(mode="after")
    def _check(self) -> ExtraDamageModifier:
        _check_dice(self.dice, "dice")
        return self


class AdvantageModifier(ModifierBase):
    kind: Literal["advantage"] = "advantage"
    on: str | None = None


class DisadvantageModifier(ModifierBase):
    kind: Literal["disadvantage"] = "disadvantage"
    on: str | None = None


class ImposeDisadvantageOnEnemyModifier(ModifierBase):
    kind: Literal["impose_disadvantage_on_enemy"] = "impose_disadvantage_on_enemy"


class CritRangeModifier(ModifierBase):
    kind: Literal["crit_range"] = "crit_range"
    value: int


class TradeoffModifier(ModifierBase):
    kind: Literal["tradeoff"] = "tradeoff"
    to_hit: float
    damage_bonus: float
    policy: dict[str, Any] | None = None


class ReplaceAttackModifier(ModifierBase):
    kind: Literal["replace_attack"] = "replace_attack"
    use: str


class BonusAttackModifier(ModifierBase):
    # `needs` requires only `attack` (`loadout.mjs:56`), but the consumer
    # reads `m.cost ?? null` (`simulator.mjs:1183`) and real content authors
    # both `cost` and an `id` reference slug. Declared rather than left to
    # ModifierBase's `extra="allow"`: an undeclared key survives validation
    # but carries no type, and a resource cost that silently fails to apply
    # makes the ability free.
    kind: Literal["bonus_attack"] = "bonus_attack"
    attack: str
    id: str | None = None
    cost: ResourceCost | None = None


class BonusAttackOnModifier(ModifierBase):
    kind: Literal["bonus_attack_on"] = "bonus_attack_on"
    trigger: str
    attack: str


class ExtraAttackCountModifier(ModifierBase):
    kind: Literal["extra_attack_count"] = "extra_attack_count"
    value: int | None = None
    count: int | None = None
    rounds: int | None = None

    @model_validator(mode="after")
    def _check(self) -> ExtraAttackCountModifier:
        if self.value is None and self.count is None:
            raise ValueError('extra_attack_count: requires "value" or "count"')
        return self


class RerollAddModifier(ModifierBase):
    kind: Literal["reroll_add"] = "reroll_add"
    die: str
    pool: str
    trigger: str | None = None
    policy: dict[str, Any] | None = None

    @model_validator(mode="after")
    def _check(self) -> RerollAddModifier:
        _check_dice(self.die, "die")
        return self


class RerollTakeBestModifier(ModifierBase):
    kind: Literal["reroll_take_best"] = "reroll_take_best"
    pool: str


class DamageReductionReactionModifier(ModifierBase):
    kind: Literal["damage_reduction_reaction"] = "damage_reduction_reaction"
    dice: str
    trigger: str | None = None
    uses_per_round: int | None = None

    @model_validator(mode="after")
    def _check(self) -> DamageReductionReactionModifier:
        _check_dice(self.dice, "dice")
        return self


class ReactionAcBonusModifier(ModifierBase):
    # `needs` has no entry for this kind, but the consumer reads
    # `s.bonus ?? 5` and `s.cost ?? null` (`simulator.mjs:424-425`) — the
    # default of 5 is Shield's. `spells.py` compiles Shield into one of
    # these, so an undeclared `bonus` means the AC swing is unrepresentable.
    kind: Literal["reaction_ac_bonus"] = "reaction_ac_bonus"
    bonus: float = 5
    cost: ResourceCost | None = None


class TempHpModifier(ModifierBase):
    kind: Literal["temp_hp"] = "temp_hp"
    amount: float
    cost: ResourceCost | None = None


class HealPolicyModifier(ModifierBase):
    kind: Literal["heal_policy"] = "heal_policy"


class ConditionOnHitModifier(ModifierBase):
    kind: Literal["condition_on_hit"] = "condition_on_hit"
    effect: str | None = None
    escape_dc: int | None = None


class SaveActionPriorityModifier(ModifierBase):
    kind: Literal["save_action_priority"] = "save_action_priority"


class SetupRoundModifier(ModifierBase):
    kind: Literal["setup_round"] = "setup_round"


class AssumeRiderTriggersModifier(ModifierBase):
    kind: Literal["assume_rider_triggers"] = "assume_rider_triggers"
    value: float


class LegendaryResistanceLikeModifier(ModifierBase):
    kind: Literal["legendary_resistance_like"] = "legendary_resistance_like"


class ResourceBudgetModifier(ModifierBase):
    # Open and pools-optional: `loadout.mjs`'s `needs` table has no entry for
    # `resource_budget` at all, so the reference never requires `pools` —
    # real content (`crissdalynn-khinriss.loadouts.yaml`) authors a
    # per-encounter spend cap instead (`{resource, spend_per_encounter}`),
    # which `ModifierBase`'s `extra="allow"` already passes through. `pools`
    # stays the shape `loadouts.py`'s implicit `min`-floor construction uses.
    kind: Literal["resource_budget"] = "resource_budget"
    pools: dict[str, int] = Field(default_factory=dict)


class PeriodicEffectModifier(ModifierBase):
    kind: Literal["periodic_effect"] = "periodic_effect"
    trigger: str
    effect: str
    amount: float | None = None
    dice: str | None = None
    damage_type: str | None = None
    suppressed_if_damaged_by: list[str] | None = None

    @model_validator(mode="after")
    def _check(self) -> PeriodicEffectModifier:
        if self.trigger not in PERIODIC_EFFECT_TRIGGERS:
            raise ValueError(
                f"periodic_effect trigger must be one of {sorted(PERIODIC_EFFECT_TRIGGERS)}"
            )
        if self.effect not in PERIODIC_EFFECT_EFFECTS:
            raise ValueError(
                f"periodic_effect effect must be one of {sorted(PERIODIC_EFFECT_EFFECTS)}"
            )
        if self.effect == "regen" and self.amount is None:
            raise ValueError('periodic_effect effect "regen" requires a numeric "amount"')
        if self.effect == "damage" and self.dice is None:
            raise ValueError('periodic_effect effect "damage" requires a "dice" expression')
        if self.dice is not None:
            _check_dice(self.dice, "dice")
        return self


class PostHitRiderModifier(ModifierBase):
    kind: Literal["post_hit_rider"] = "post_hit_rider"
    id: str
    save: SaveSpec
    cost: ResourceCost | None = None
    applies_to: list[str] | None = None
    once_per_turn: bool | None = None
    on_fail: OnFailBlock | None = None
    on_success: OnFailBlock | None = None

    @model_validator(mode="after")
    def _check(self) -> PostHitRiderModifier:
        if self.on_fail is None and self.on_success is None:
            raise ValueError(
                "post_hit_rider needs an on_fail and/or on_success branch — "
                "it models nothing otherwise"
            )
        return self


class TradeDiceForRiderModifier(ModifierBase):
    kind: Literal["trade_dice_for_rider"] = "trade_dice_for_rider"
    id: str
    # A count of dice OR a dice expression naming what is traded away — the
    # reference requires the key's presence and nothing more
    # (`loadout.mjs:62`), and real content spends `1d6` of Sneak Attack
    # (`delmar-fisk-sheet.md`). A bare `int` field rejected that.
    dice_cost: int | str
    save: SaveSpec
    from_: str = Field(alias="from")
    on_fail: OnFailBlock | None = None
    on_success: OnFailBlock | None = None

    model_config = ConfigDict(frozen=True, extra="allow", populate_by_name=True)

    @model_validator(mode="after")
    def _check(self) -> TradeDiceForRiderModifier:
        if self.on_fail is None and self.on_success is None:
            raise ValueError(
                "trade_dice_for_rider needs an on_fail and/or on_success branch — "
                "it models nothing otherwise"
            )
        return self


class RetaliateDamage(BaseModel):
    model_config = ConfigDict(frozen=True, extra="allow")

    dice: str
    type: str | None = None

    @model_validator(mode="after")
    def _check(self) -> RetaliateDamage:
        _check_dice(self.dice, "dice")
        return self


class RetaliateModifier(ModifierBase):
    kind: Literal["retaliate"] = "retaliate"
    trigger: Literal["hit_by_melee", "hit_by_any"]
    damage: RetaliateDamage
    while_: str | None = Field(default=None, alias="while")

    model_config = ConfigDict(frozen=True, extra="allow", populate_by_name=True)


class MovementBoostModifier(ModifierBase):
    kind: Literal["movement_boost"] = "movement_boost"
    grants: Literal["dash", "disengage", "both"]
    cost: ResourceCost | None = None
    id: str | None = None


MODIFIER_CLASSES: tuple[type[ModifierBase], ...] = (
    FlatToHitModifier,
    FlatDamageModifier,
    ExtraDamageModifier,
    AdvantageModifier,
    DisadvantageModifier,
    ImposeDisadvantageOnEnemyModifier,
    CritRangeModifier,
    TradeoffModifier,
    ReplaceAttackModifier,
    BonusAttackModifier,
    BonusAttackOnModifier,
    ExtraAttackCountModifier,
    RerollAddModifier,
    RerollTakeBestModifier,
    DamageReductionReactionModifier,
    ReactionAcBonusModifier,
    TempHpModifier,
    HealPolicyModifier,
    ConditionOnHitModifier,
    SaveActionPriorityModifier,
    SetupRoundModifier,
    AssumeRiderTriggersModifier,
    LegendaryResistanceLikeModifier,
    ResourceBudgetModifier,
    PeriodicEffectModifier,
    PostHitRiderModifier,
    TradeDiceForRiderModifier,
    RetaliateModifier,
    MovementBoostModifier,
)

# Kinds that encode a scenario assumption rather than a combatant's own
# capability — legal in a loadout file's `modifiers:` list only.
SCENARIO_ONLY_KINDS: frozenset[str] = frozenset(
    {"resource_budget", "setup_round", "assume_rider_triggers", "save_action_priority"}
)

Modifier = Annotated[
    FlatToHitModifier
    | FlatDamageModifier
    | ExtraDamageModifier
    | AdvantageModifier
    | DisadvantageModifier
    | ImposeDisadvantageOnEnemyModifier
    | CritRangeModifier
    | TradeoffModifier
    | ReplaceAttackModifier
    | BonusAttackModifier
    | BonusAttackOnModifier
    | ExtraAttackCountModifier
    | RerollAddModifier
    | RerollTakeBestModifier
    | DamageReductionReactionModifier
    | ReactionAcBonusModifier
    | TempHpModifier
    | HealPolicyModifier
    | ConditionOnHitModifier
    | SaveActionPriorityModifier
    | SetupRoundModifier
    | AssumeRiderTriggersModifier
    | LegendaryResistanceLikeModifier
    | ResourceBudgetModifier
    | PeriodicEffectModifier
    | PostHitRiderModifier
    | TradeDiceForRiderModifier
    | RetaliateModifier
    | MovementBoostModifier,
    Field(discriminator="kind"),
]

# Registration replaces dispatch: MODIFIER_KINDS maps every closed-vocabulary
# `kind` string to its model class. A new kind is added by registering it
# here — never by adding a branch anywhere a modifier is consumed.
MODIFIER_KINDS: Registry[type[ModifierBase]] = Registry("dndsim.modifier_kinds")
for _cls in MODIFIER_CLASSES:
    _kind: str = _cls.model_fields["kind"].default
    MODIFIER_KINDS.register_value(f"dnd5e_2014:modifier/{_kind}", _cls)


def describe_modifier(kind: str, page_source: str, field_path: str, **data: Any) -> ModifierBase:
    """Validate one ability-modifier's raw data against its registered kind.

    Resolves ``kind`` through :data:`MODIFIER_KINDS` (a plain dict lookup,
    never a branch) and delegates to that class's own pydantic validation.
    Raises :class:`SimExtensionError` naming ``page_source``/``field_path``
    for an unknown kind or invalid data — mirrors ``validateModifier``'s
    failure shape. Parameters are named apart from ``**data`` because a
    modifier's own schema carries an unrelated ``source`` field (free-text
    attribution, e.g. ``"ally Faerie Fire"``) that would otherwise collide.
    """
    namespaced = f"dnd5e_2014:modifier/{kind}"
    if namespaced not in MODIFIER_KINDS:
        fail(page_source, field_path, f'unknown modifier kind "{kind}"')
    cls = MODIFIER_KINDS.get(namespaced)
    try:
        return cls.model_validate({"kind": kind, **data})
    except ValidationError as err:
        fail(page_source, field_path, str(err))


# --- top-level `sim:` and per-action `sim:` schemas -------------------------

_EDITIONS: frozenset[str] = frozenset({"2014", "2024"})
_ROUTINE_SLOTS: frozenset[str] = frozenset({"action", "bonus", "reaction", "legendary"})


class SaveAdvantageEntry(BaseModel):
    # Open: the reference checks `vs` and `mode` only, never the entry's key
    # set (`sim-extension.mjs:109-114`).
    model_config = ConfigDict(frozen=True, extra="allow")

    vs: str
    mode: Literal["advantage", "disadvantage"] = "advantage"

    @model_validator(mode="after")
    def _check(self) -> SaveAdvantageEntry:
        if self.vs == "":
            raise ValueError("save_advantage[].vs: must be a string")
        return self


class ResourcePoolSpec(BaseModel):
    # Open: the reference checks `id`/`max`/`recharge` only, never the
    # entry's key set (`sim-extension.mjs:116-122`).
    model_config = ConfigDict(frozen=True, extra="allow")

    id: str
    max: float
    recharge: str | None = None

    @model_validator(mode="after")
    def _check(self) -> ResourcePoolSpec:
        if self.id == "":
            raise ValueError("resources[].id: must be a string")
        if self.max < 1:
            raise ValueError(f"resources[{self.id}].max: must be a positive number")
        if self.recharge is not None and self.recharge not in RECHARGE_KINDS:
            raise ValueError(
                f"resources[{self.id}].recharge: must be one of {sorted(RECHARGE_KINDS)}"
            )
        return self


class SpellcastingPool(BaseModel):
    """A caster's independent slot pool.

    Extra keys beyond README's documented shape (``source``,
    ``ability_mod``, etc.) are allowed and passed through — the reference
    validator (`sim-extension.mjs`) never closes this sub-object either,
    and real vault content (`perrin-black-jaw-sheet.md`) relies on that.
    """

    model_config = ConfigDict(frozen=True, extra="allow")

    ability: str
    dc: float
    attack_bonus: float | None = None
    level: float | None = None
    # YAML's unquoted `1: bard_slot_1` parses the key as an int (JS objects
    # coerce it to a string automatically; Python/pydantic don't) — typed
    # `int` to accept the real vault shape rather than requiring authors to
    # quote every slot-level key.
    slots: dict[int, str] | None = None
    known: list[str]

    @model_validator(mode="after")
    def _check(self) -> SpellcastingPool:
        if len(self.known) == 0:
            raise ValueError("spellcasting[].known: must be a non-empty list of spell names")
        if self.slots is not None:
            for lvl in self.slots:
                if not (1 <= lvl <= 9):
                    raise ValueError(f"spellcasting[].slots.{lvl}: slot level must be 1..9")
        return self


class Position(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    start_band: int

    @model_validator(mode="after")
    def _check(self) -> Position:
        if not (0 <= self.start_band <= 3):
            raise ValueError(
                "position.start_band: must be an integer 0..3 (bands back from the contact line)"
            )
        return self


class SimBlock(BaseModel):
    """The top-level `sim:` block on a statblock fence."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    side: Literal["party", "enemy"] = "enemy"
    level: float | None = None
    initiative: float | None = None
    temp_hp: float | None = None
    crit_range: float | None = None
    concentration_save: float | None = None
    # The reference compares `String(sim.edition)`, so an unquoted YAML
    # `edition: 2014` (an int) is accepted there — typed to match.
    edition: str | int | None = None
    save_advantage: list[SaveAdvantageEntry] = Field(default_factory=list)
    resources: list[ResourcePoolSpec] = Field(default_factory=list)
    abilities: list[Modifier] = Field(default_factory=list)
    # The reference requires each of the four KNOWN slots, when present, to
    # be a list, and passes any other key through untouched
    # (`sim-extension.mjs:131-139`) — no unknown-slot rejection.
    routine: dict[str, Any] | None = None
    position: Position | None = None
    spellcasting: list[SpellcastingPool] | None = None

    @model_validator(mode="after")
    def _check(self) -> SimBlock:
        if self.edition is not None and str(self.edition) not in _EDITIONS:
            raise ValueError(f"edition: must be one of {sorted(_EDITIONS)}")
        for i, ability in enumerate(self.abilities):
            if ability.kind in SCENARIO_ONLY_KINDS:
                raise ValueError(
                    f'abilities[{i}]: kind "{ability.kind}" encodes a scenario assumption — it '
                    "belongs in a loadout file, not on the combatant"
                )
        if self.routine is not None:
            for slot in _ROUTINE_SLOTS:
                steps = self.routine.get(slot)
                if steps is not None and not isinstance(steps, list):
                    raise ValueError(f"routine.{slot}: must be a list")
        return self


def parse_sim_block(data: dict[str, Any] | None, source: str) -> SimBlock:
    """Validate one page's top-level `sim:` block, or default it if absent.

    A page with no `sim:` block at all still parses fine (creatures/NPCs
    authored before this extension existed), defaulting to
    ``sim: { side: enemy }`` — README's documented fallback.
    """
    try:
        return SimBlock.model_validate(data or {})
    except ValidationError as err:
        fail(source, "sim", str(err))


class HealSpec(BaseModel):
    # Open: the reference parses `heal.dice` and checks no other key
    # (`sim-extension.mjs:187-189`).
    model_config = ConfigDict(frozen=True, extra="allow")

    dice: str

    @model_validator(mode="after")
    def _check(self) -> HealSpec:
        _check_dice(self.dice, "dice")
        return self


class OnSuccessSpec(BaseModel):
    # Open: the reference checks `on_success.damage_multiplier` and no other
    # key (`sim-extension.mjs:171-174`).
    model_config = ConfigDict(frozen=True, extra="allow")

    # `typing.Literal` cannot hold a float (PEP 586) — validated instead.
    damage_multiplier: float

    @model_validator(mode="after")
    def _check(self) -> OnSuccessSpec:
        if self.damage_multiplier not in (0, 0.5):
            raise ValueError("on_success.damage_multiplier: must be 0 or 0.5")
        return self


class ActionSim(BaseModel):
    """A per-action `sim:` sub-map on an actions/bonus_actions/reactions/
    legendary_actions entry — replaces prose-derived values when present,
    never merges (README § Per-action `sim:`)."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str | None = None
    cost: ResourceCost | None = None
    concentration: bool | None = None
    once_per_turn: bool | None = None
    on_success: OnSuccessSpec | None = None
    on_fail: OnFailBlock | None = None
    on_hit_effects: list[EffectRider] = Field(default_factory=list)
    heal: HealSpec | None = None
    action_cost: Literal["action", "bonus"] | None = None
    # Full `REACTION_KINDS` vocabulary — `damage_reduction_pct` is the
    # fractional reduction Uncanny Dodge and Absorb Elements are authored
    # with (`delmar-fisk-sheet.md`, `catarina-davirelli-sheet.md`).
    kind: (
        Literal["damage_reduction", "damage_reduction_pct", "extra_attack", "ac_bonus", "unmodeled"]
        | None
    ) = None
    die: str | None = None
    attack: str | None = None
    bonus: float | None = None
    trigger: str | None = None
    reach: float | None = None
    range: float | None = None
    fraction: float | None = None
    # A redirect clause is a map in real content (Deflect Attacks' cost +
    # damage + save + range_ft) and the reference type-checks it not at all
    # — it is a known key with no validation (`ACTION_KEYS`).
    redirect: Any = None
    damage_types: list[str] | None = None
    # issue #71: 2024 PHB Weapon Mastery (Vex/Slow only — see
    # WEAPON_MASTERY_KINDS). Never prose-parsed (see that constant's own
    # docstring); an attack's `sim:` block is the sole authoring surface.
    mastery: Literal["vex", "slow"] | None = None

    @model_validator(mode="after")
    def _check(self) -> ActionSim:
        if self.id is not None and self.id == "":
            raise ValueError("id: must be a non-empty string")
        if self.on_fail is not None:
            for i, damage in enumerate(self.on_fail.damage):
                _check_dice(damage.dice, f"on_fail.damage[{i}].dice")
            for i, rider in enumerate(self.on_fail.effects):
                if rider.effect.lower() not in EFFECT_TAGS:
                    raise ValueError(
                        f'on_fail.effects[{i}]: unknown condition tag "{rider.effect.lower()}"'
                    )
        for i, rider in enumerate(self.on_hit_effects):
            if rider.effect == "":
                raise ValueError(f"on_hit_effects[{i}].effect: must be a non-empty string")
        # The reference parses `die` for a `damage_reduction` reaction only
        # (`sim-extension.mjs:197-199`).
        if self.kind == "damage_reduction" and self.die is not None:
            _check_dice(self.die, "die")
        return self


def parse_action_sim(data: dict[str, Any] | None, source: str, field: str) -> ActionSim:
    """Validate one action entry's per-action `sim:` sub-map, or default it if absent."""
    try:
        return ActionSim.model_validate(data or {})
    except ValidationError as err:
        fail(source, field, str(err))
