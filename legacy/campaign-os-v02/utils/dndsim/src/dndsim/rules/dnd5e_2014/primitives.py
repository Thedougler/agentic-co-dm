"""The compiled 5e Primitive vocabulary (issue #43) — what the engine
executes and the planner values, per ADR-0008.

Authored content (a parsed :data:`~dndsim.rules.dnd5e_2014.attack_string.Action`
or a `sim:` :data:`~dndsim.rules.dnd5e_2014.sim_extension.Modifier`) compiles
down to instances of the classes here; nothing this Rules pack executes may
be shaped any other way (`dndsim.rules.dnd5e_2014.compile`). Every instance
carries a namespaced ``id`` — the compiled analogue of a Modifier's optional
authoring-time ``id`` — because the core "never sees an unnamespaced ID"
(ADR-0007/CONTEXT.md § Primitive).

Two families:

- Action-derived: :class:`AttackPrimitive`, :class:`AutodamagePrimitive`,
  :class:`SavePrimitive` — one per non-multiattack, non-unmodeled
  :class:`~dndsim.rules.dnd5e_2014.attack_string.Action` kind. Multiattack
  is not its own Primitive; it becomes :class:`RoutineStep` composition on
  :class:`~dndsim.rules.dnd5e_2014.compile.CompiledStatblock`, matching
  where the parser already keeps a Multiattack's routine (a
  whole-statblock concern, never a single action's own shape).
- Ability-derived: one Primitive class per non-scenario-only
  `sim:abilities[]` Modifier kind, generated mechanically from that kind's
  own Modifier class via :func:`_primitive_for` rather than hand-duplicated
  — a Primitive IS that Modifier's shape plus a mandatory ``id``, which is
  the concrete sense in which "content composes Primitives; content never
  introduces one" (CONTEXT.md): the Primitive vocabulary's shape is
  entirely determined by the already-closed Modifier vocabulary.

Every Primitive class is registered into :data:`dndsim.core.primitive.primitives`
under a namespaced kind id (``dnd5e_2014:primitive/<kind>``) — the registry
resolved by :func:`~dndsim.rules.dnd5e_2014.compile.instantiate_primitive`,
never a switch. Adding a new ability kind means adding one Modifier class in
`sim_extension.py`; this module then defines its Primitive automatically.
"""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, create_model

from dndsim.core.primitive import Primitive, primitives
from dndsim.rules.dnd5e_2014.attack_string import DamageGroup, OnHitEffect, TargetClause
from dndsim.rules.dnd5e_2014.sim_extension import (
    MODIFIER_CLASSES,
    SCENARIO_ONLY_KINDS,
    ModifierBase,
    OnFailBlock,
    ResourceCost,
    SaveSpec,
)


class PrimitiveBase(BaseModel, Primitive):
    """Every compiled Primitive carries a namespaced, stable instance id."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str


# --- action-derived primitives ----------------------------------------------


class AttackPrimitive(PrimitiveBase):
    kind: Literal["attack"] = "attack"
    to_hit: int
    damage: list[DamageGroup]
    on_hit_effects: list[OnHitEffect] = Field(default_factory=list)
    on_hit_save: SaveSpec | None = None
    advantage_if: str | None = None
    # This attack's own physical reach/range profile (issue #63 cause D) —
    # defaults match CombatantSpec's own flat-profile defaults so a
    # hand-built (non-compiled) AttackPrimitive behaves exactly like the
    # legacy melee-reach-5 shape every existing fixture/test assumes.
    # Populated from the parsed action's own attack_type/reach/range in
    # compile.py, never derived from the actor's flat CombatantSpec, so a
    # routine that picks a different alternative than the flat profile
    # implies (the Grung's Shortbow over its Dagger) is judged by the
    # weapon actually fired.
    is_melee: bool = True
    reach_ft: float | None = 5.0
    range_ft: float | None = None
    range_long_ft: float | None = None
    # A costed authored ability's own resource spend (issue #63: the same
    # gap that made SavePrimitive's missing `cost` let an authored
    # save-or-suck ability cast for free every turn) — `None` for an
    # ordinary weapon attack, which spends nothing.
    cost: ResourceCost | None = None
    # issue #71: 2024 PHB Weapon Mastery (Vex/Slow only — see
    # sim_extension.WEAPON_MASTERY_KINDS). `None` for a weapon with no
    # authored mastery property, or one whose property isn't modeled.
    mastery: Literal["vex", "slow"] | None = None


class AutodamagePrimitive(PrimitiveBase):
    kind: Literal["autodamage"] = "autodamage"
    damage: list[DamageGroup]
    targets: TargetClause
    requires_target_condition: str | None = None
    attached_save: SaveSpec | None = None
    cost: ResourceCost | None = None


class SavePrimitive(PrimitiveBase):
    kind: Literal["save"] = "save"
    dc: int
    save: str
    targets: TargetClause
    on_fail: OnFailBlock = Field(default_factory=OnFailBlock)
    half_on_save: bool = False
    # issue #63: without this, an authored save-or-suck ability casts for
    # free, unlimited times — its own compiled `cost` (a bard/pact slot)
    # was compiled onto nothing at all before this, since only
    # HealPrimitive/ReactionPrimitive carried one.
    cost: ResourceCost | None = None


class HealPrimitive(PrimitiveBase):
    """A per-action `sim.heal` override (README: "routes this entry to the
    heals list instead of actions") — compiled regardless of what the
    action's own `desc` prose parsed as, since heal prose ("Perrin touches a
    creature, restoring...") never matches the attack/save/autodamage
    grammar."""

    kind: Literal["heal"] = "heal"
    dice: str
    cost: ResourceCost | None = None


class ReactionPrimitive(PrimitiveBase):
    """A per-action `sim.kind` reaction mechanic (README's `damage_reduction`
    \\| `damage_reduction_pct` \\| `extra_attack` \\| `ac_bonus` \\|
    `unmodeled` vocabulary) — compiled when the action's own prose carries no
    attack/save/autodamage grammar (Cutting Words, Pack Tactics Strike,
    Uncanny Dodge) but its `sim:` block still declares a reaction mechanic."""

    kind: Literal["reaction"] = "reaction"
    reaction_kind: Literal[
        "damage_reduction", "damage_reduction_pct", "extra_attack", "ac_bonus", "unmodeled"
    ]
    die: str | None = None
    attack: str | None = None
    bonus: float | None = None
    #: `damage_reduction_pct`'s share of the incoming damage that survives —
    #: Uncanny Dodge's "halve the attack's damage" authors `fraction: 0.5`
    #: (`delmar-fisk-sheet.md`), Absorb Elements the same
    #: (`catarina-davirelli-sheet.md`). Unused by every other
    #: `reaction_kind`; RAW rounds the halved total down (PHB-2024 p.131).
    fraction: float | None = None
    #: The damage types this reaction may be taken against (Absorb Elements'
    #: acid/cold/fire/lightning/thunder, `catarina-davirelli-sheet.md`).
    #: ``None`` — the authored default, and every reaction that declares no
    #: filter (Cutting Words, Uncanny Dodge) — accepts any damage type.
    damage_types: tuple[str, ...] | None = None
    trigger: str | None = None
    cost: ResourceCost | None = None


primitives.register_value("dnd5e_2014:primitive/attack", AttackPrimitive)
primitives.register_value("dnd5e_2014:primitive/autodamage", AutodamagePrimitive)
primitives.register_value("dnd5e_2014:primitive/save", SavePrimitive)
primitives.register_value("dnd5e_2014:primitive/heal", HealPrimitive)
primitives.register_value("dnd5e_2014:primitive/reaction", ReactionPrimitive)


class RoutineStepPrimitive(BaseModel):
    """One step of a compiled Multiattack routine (never a standalone
    Primitive itself — a whole-statblock composition of other Primitives'
    ids, matching where the parser already keeps a Multiattack routine)."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    ref: str
    count: int
    alternatives: list[str] = Field(default_factory=list)


# --- ability-derived primitives, mechanically generated from Modifier ------


def _primitive_for(modifier_cls: type[ModifierBase]) -> type[PrimitiveBase]:
    """Build ``<X>Primitive`` from ``<X>Modifier``: same fields, plus a
    mandatory ``id``. A Primitive's shape is never independently authored —
    it is the Modifier's own closed shape, with the identity every compiled
    instance must carry.

    A handful of Modifier kinds (``extra_damage``, ``post_hit_rider``,
    ``trade_dice_for_rider``) already declare their own local ``id`` — an
    authoring-time reference slug (``{ kind: extra_damage, id: hex, ... }``),
    not an identity. That field is carried onto the Primitive renamed to
    ``ref`` so it never collides with :class:`PrimitiveBase`'s own ``id``,
    the compiled instance's namespaced identity.
    """
    name = f"{modifier_cls.__name__.removesuffix('Modifier')}Primitive"
    field_defs: dict[str, Any] = {}
    for field_name, field_info in modifier_cls.model_fields.items():
        if field_name == "id":
            field_defs["ref"] = (field_info.annotation, None)
            continue
        field_defs[field_name] = (field_info.annotation, field_info)
    return create_model(name, __base__=(PrimitiveBase,), **field_defs)


_ABILITY_MODIFIER_CLASSES: tuple[type[ModifierBase], ...] = tuple(
    cls for cls in MODIFIER_CLASSES if cls.model_fields["kind"].default not in SCENARIO_ONLY_KINDS
)

ABILITY_PRIMITIVES: dict[str, type[PrimitiveBase]] = {}
for _mod_cls in _ABILITY_MODIFIER_CLASSES:
    _kind: str = _mod_cls.model_fields["kind"].default
    _prim_cls = _primitive_for(_mod_cls)
    ABILITY_PRIMITIVES[_kind] = _prim_cls
    primitives.register_value(f"dnd5e_2014:primitive/{_kind}", _prim_cls)


def modifier_to_primitive(modifier: ModifierBase, primitive_id: str) -> PrimitiveBase:
    """Compile one validated ability :class:`Modifier` instance into its
    Primitive counterpart, resolved through :data:`ABILITY_PRIMITIVES` —
    a dict lookup, never a branch over ``modifier.kind``."""
    # `ModifierBase` itself declares no `kind` — each subclass narrows it to
    # its own single-member Literal (kept that way rather than a shared
    # `str` field on the base, which pyright's pydantic-unaware variance
    # check rejects for a mutable attribute overridden to a narrower type).
    kind: str = modifier.kind  # type: ignore[attr-defined]
    prim_cls = ABILITY_PRIMITIVES[kind]
    data: dict[str, Any] = modifier.model_dump(by_alias=True)

    # `id` is keyed off the dumped data, not the declared field set.
    # `ModifierBase` allows extras (the reference never key-checks a
    # modifier), so an authored `id` can arrive as a pydantic extra, which
    # `model_fields` does not report — reading the field set instead let it
    # through into `**data` and collided with the identity below.
    local_id = data.pop("id", None)
    if local_id is not None:
        data["ref"] = local_id

    # A key the Primitive cannot hold would otherwise surface as an opaque
    # pydantic `extra_forbidden`, or silently vanish if the vocabulary were
    # opened up. Name it and the kind instead: either the Modifier should
    # declare the field, or the content is wrong.
    accepted: set[str] = set()
    for field_name, field_info in prim_cls.model_fields.items():
        accepted.add(field_name)
        if field_info.alias is not None:
            accepted.add(field_info.alias)
    unknown = sorted(set(data) - accepted)
    if unknown:
        raise ValueError(
            f"{kind}: cannot compile to {prim_cls.__name__} — "
            f"no field for authored key(s) {unknown}. Declare them on the "
            f"Modifier class in sim_extension.py, or fix the content."
        )
    return prim_cls(id=primitive_id, **data)
