"""Compile-to-Primitives (issue #43): authored content's only executable form.

ADR-0008: a Policy that maximizes expected value cannot value an ability
that does not state its own worth, so the planner must only ever meet
Primitives it can already value. :func:`compile_statblock` generalizes the
one subsystem the old engine already got right — its spell subsystem
compiles ` ```spell ` fences down to ordinary actions, and its own README
records that the simulator and policy "know nothing about spells." Here,
every authored ability (`sim:abilities[]` Modifiers) and every parsed
action (Attack/Save/Autodamage) compiles down to the same closed Primitive
vocabulary (`dndsim.rules.dnd5e_2014.primitives`) before a combat model
(issue #45) ever runs one.

``routine`` — parsed by
:func:`~dndsim.rules.dnd5e_2014.attack_string.parse_multiattack` but
attached to nothing (issues #41/#42's open thread: `statblock.py`'s
:class:`~dndsim.rules.dnd5e_2014.statblock.StatblockContent` carries no
``routine`` field; `scripts/differential_harness.py` assembles it ad hoc)
— finds its home here: :attr:`CompiledStatblock.routine`.

Dispatch is registry-based throughout, matching `sim_extension.py`'s
:data:`~dndsim.rules.dnd5e_2014.sim_extension.MODIFIER_KINDS`: an
:data:`Action`'s ``kind`` resolves through :data:`ACTION_KIND_COMPILERS` to
its compiler function, never a branch, so
`tests/rules/test_compile.py::test_new_action_kind_needs_no_compiler_edit`
can register a dummy compiler at test scope and drive it through
:func:`compile_action` unchanged.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from dndsim.core.registry import Registry
from dndsim.rules.dnd5e_2014.attack_string import (
    Action,
    AttackAction,
    AutodamageAction,
    OnHitEffect,
    RoutineStep,
    SaveAction,
    _is_legendary_preamble,
    parse_action,
    parse_multiattack,
)
from dndsim.rules.dnd5e_2014.primitives import (
    AttackPrimitive,
    AutodamagePrimitive,
    HealPrimitive,
    PrimitiveBase,
    ReactionPrimitive,
    RoutineStepPrimitive,
    SavePrimitive,
    modifier_to_primitive,
)
from dndsim.rules.dnd5e_2014.sim_extension import (
    ActionSim,
    AdvantageModifier,
    DamageDie,
    EffectRider,
    LegendaryResistanceLikeModifier,
    OnFailBlock,
    Position,
    SaveSpec,
    SimBlock,
    parse_action_sim,
    parse_sim_block,
)
from dndsim.rules.dnd5e_2014.spells import compile_spellcasting
from dndsim.rules.dnd5e_2014.statblock import Defenses, StatblockContent

_SLUG_RE = re.compile(r"[^a-z0-9]+")


class CompileError(ValueError):
    """Authored content could not be compiled to Primitives."""


def slugify(name: str) -> str:
    return _SLUG_RE.sub("-", name.lower()).strip("-") or "action"


def _save_bonuses(content: StatblockContent) -> dict[str, int]:
    """One saving-throw bonus per ability key: a bare ability-score modifier
    (``(score - 10) // 2``) for every ability the fence declares, overridden
    by the fence's own ``saves:`` entry (proficiency already folded in)
    where one is authored."""
    bonuses = {ability: (score - 10) // 2 for ability, score in content.abilities.items()}
    bonuses.update(content.saves)
    return bonuses


@dataclass(frozen=True, slots=True)
class CompiledAbility:
    """One action's compiled behavior: its own namespaced id (the routine's
    reference target) plus the Primitive step that resolves it."""

    id: str
    name: str
    step: PrimitiveBase
    action_cost: str | None = None
    concentration: bool = False
    once_per_turn: bool = False
    # Issue (this task): a legendary action's own per-use cost against its
    # creature's per-round pool (Bile Spray "Costs 2 Actions" vs. Lash/
    # Thrash's implicit 1) — parsed onto the action's own name by
    # `attack_string.parse_name_usage` into `ActionUsage.legendary_cost`
    # long before this task, but never read anywhere until now. Meaningless
    # for a non-legendary ability (`action_cost != "legendary"`), which
    # never touches a legendary pool at all.
    legendary_cost: int = 1


@dataclass(frozen=True, slots=True)
class CompiledStatblock:
    """A whole statblock's compiled form — what a combat model (#45) executes.

    ``ability_primitives`` holds the standing, always-available capabilities
    from ``sim.abilities`` (Hex, GWM, regen auras...); ``compiled_actions``
    holds the per-action Primitives compiled from parsed
    actions/bonus_actions/reactions/legendary_actions; ``routine`` is the
    Multiattack ordering, referencing ``compiled_actions`` by id.
    """

    id: str
    name: str
    ac: int
    hp: int
    side: str
    resources: tuple[Any, ...] = ()
    ability_primitives: tuple[PrimitiveBase, ...] = ()
    compiled_actions: tuple[CompiledAbility, ...] = ()
    routine: tuple[RoutineStepPrimitive, ...] = ()
    warnings: tuple[str, ...] = ()
    # Issue #60: a compiled SavePrimitive/AutodamagePrimitive's attached save
    # needs the target's own saving-throw bonus, which the fence's ``saves:``
    # override (proficiency-included) or a bare ability-score modifier
    # supplies — see :func:`_save_bonuses`. Never authored directly; always
    # derived from :class:`~dndsim.rules.dnd5e_2014.statblock.StatblockContent`.
    save_bonuses: dict[str, int] = field(default_factory=dict)
    # An authored ``sim.position.start_band`` (issue #47's positional model),
    # carried through unchanged for whatever assembles the encounter to read
    # — this module compiles content, it never itself deploys a combatant.
    position: Position | None = None
    # Issue #61: the fence's own resist/immune/vulnerable/condition_immune
    # tags (statblock.py's Defenses, produced since #40 but never carried
    # onto this class until now), read by the damage-applying Mechanics so
    # a target's declared resistance/immunity/vulnerability actually mitigates
    # incoming damage instead of every type landing at full value.
    defenses: Defenses = field(default_factory=Defenses)
    # Raw ability scores (str/dex/con/int/wis/cha) straight from the fence's
    # own ``stats:`` list — ``StatblockContent.abilities``, produced since
    # the statblock Importer but never carried onto this class until now.
    # ``save_bonuses`` already derives a bare modifier per ability
    # (``_save_bonuses``), but that dict is overwritten by the fence's own
    # proficient ``saves:`` entry where one exists, so it is the wrong
    # source for a mechanic that needs the RAW ability MODIFIER specifically
    # (rolled initiative's Dex tiebreak: PHB p.189, "the DM decides
    # ties... a good rule is to use each combatant's Dexterity score, with
    # higher Dexterity going first" — a save bonus, proficient or not, is
    # not that number).
    abilities: dict[str, int] = field(default_factory=dict)
    # Issue (this task): how many legendary actions this creature takes
    # per round — 0 for a non-legendary creature. Sourced from the
    # statblock's own ``legendary_actions`` preamble prose
    # (``attack_string.legendary_actions_per_round``), never a flat
    # default; ``combat.py``'s legendary-pool sizing and handler both key
    # off this instead of an engine-wide constant.
    legendary_actions_per_round: int = 0


# --- registry-dispatched Action -> Primitive compilers ----------------------

ActionCompiler = Callable[[Action, ActionSim, str], PrimitiveBase]
ACTION_KIND_COMPILERS: Registry[ActionCompiler] = Registry("dndsim.compile.action_kinds")


def _compile_attack(action: Action, action_sim: ActionSim, primitive_id: str) -> PrimitiveBase:
    assert isinstance(action, AttackAction)
    on_hit_save = (
        SaveSpec(ability=action.on_hit_save.save, dc=action.on_hit_save.dc)
        if action.on_hit_save is not None
        else None
    )
    # sim_extension's EffectRider and attack_string's OnHitEffect share the
    # same {effect, escape_dc} shape by construction, but are distinct
    # pydantic classes — converted explicitly rather than passed cross-type.
    on_hit_effects = [
        OnHitEffect(effect=e.effect, escape_dc=e.escape_dc) for e in action_sim.on_hit_effects
    ] or list(action.on_hit_effects)
    return AttackPrimitive(
        id=primitive_id,
        to_hit=action.to_hit,
        damage=list(action.damage),
        on_hit_effects=on_hit_effects,
        on_hit_save=on_hit_save,
        advantage_if=action.advantage_if,
        # issue #63 cause D: this attack's own physical profile, not the
        # actor's flat CombatantSpec — attack_type is "melee_*"/"ranged_*"
        # (attack_string.py), so startswith("melee") is is_melee the same
        # way scripts/parity_matchups.py's own combatant_from_page derives
        # it for the flat profile.
        is_melee=action.attack_type.startswith("melee"),
        reach_ft=float(action.reach) if action.reach is not None else 5.0,
        range_ft=float(action.range) if action.range is not None else None,
        range_long_ft=float(action.range_long) if action.range_long is not None else None,
        # issue #63: a costed attack spell's own resource spend — was
        # compiled onto nothing before this (only Heal/Reaction carried a
        # cost), so it never gated the planner or the combat loop.
        cost=action_sim.cost,
        # issue #71: 2024 PHB Weapon Mastery — per-action `sim:` override
        # only (see ActionSim.mastery's own docstring for why).
        mastery=action_sim.mastery,
    )


def _compile_autodamage(action: Action, action_sim: ActionSim, primitive_id: str) -> PrimitiveBase:
    assert isinstance(action, AutodamageAction)
    attached_save = (
        SaveSpec(ability=action.attached_save.save, dc=action.attached_save.dc)
        if action.attached_save is not None
        else None
    )
    return AutodamagePrimitive(
        id=primitive_id,
        damage=list(action.damage),
        targets=action.targets,
        requires_target_condition=action.requires_target_condition,
        attached_save=attached_save,
        cost=action_sim.cost,
    )


def _compile_save(action: Action, action_sim: ActionSim, primitive_id: str) -> PrimitiveBase:
    assert isinstance(action, SaveAction)
    on_fail = action_sim.on_fail
    if on_fail is None:
        on_fail = OnFailBlock(
            damage=[DamageDie(dice=d.dice, type=d.type) for d in action.on_fail.damage],
            effects=[
                # `save_ends` is not a declared EffectRider field — it rides
                # through as a pydantic `extra="allow"` key (issue #63's
                # save_ends interlock), exactly like a directly sim.abilities-
                # authored on_fail already carries it.
                EffectRider(effect=e.effect, escape_dc=e.escape_dc, save_ends=e.save_ends)
                for e in action.on_fail.effects
            ],
        )
    half_on_save = (
        action_sim.on_success.damage_multiplier == 0.5
        if action_sim.on_success is not None
        else action.half_on_save
    )
    return SavePrimitive(
        id=primitive_id,
        dc=action.dc,
        save=action.save,
        targets=action.targets,
        on_fail=on_fail,
        half_on_save=half_on_save,
        # issue #63: Hideous Laughter's own bard-1 slot cost — dropped
        # silently before this (SavePrimitive carried no cost field at all),
        # which let a save-or-suck spell cast for free, unlimited times.
        cost=action_sim.cost,
    )


ACTION_KIND_COMPILERS.register_value("attack", _compile_attack)
ACTION_KIND_COMPILERS.register_value("autodamage", _compile_autodamage)
ACTION_KIND_COMPILERS.register_value("save", _compile_save)

# Multiattack contributes only to CompiledStatblock.routine, never its own
# Primitive (attack_string.py's own docs: a whole-statblock concern).
# Unmodeled carries no engine-executable shape by definition.
_UNCOMPILABLE_ACTION_KINDS: frozenset[str] = frozenset({"multiattack", "unmodeled"})


def compile_action(
    namespace: str,
    statblock_slug: str,
    index: int,
    action: Action,
    action_sim: ActionSim,
    *,
    default_action_cost: str | None = None,
) -> CompiledAbility | None:
    """Compile one parsed :data:`Action` into a :class:`CompiledAbility`.

    A per-action `sim.heal` or `sim.kind` override takes priority over the
    parsed action grammar — README: `heal` "routes this entry to the heals
    list instead of actions", and a reaction mechanic's own `sim.kind` is
    how Cutting Words / Pack Tactics Strike compile even though their prose
    ("touches a creature, restoring...", "he expends a Bardic Inspiration
    die...") matches no attack/save/autodamage grammar at all. Absent
    either override, returns ``None`` for a Multiattack or Unmodeled action
    — neither compiles to a standalone Primitive (see module docstring).
    Dispatches on ``action.kind`` through :data:`ACTION_KIND_COMPILERS` — a
    registry lookup, never a branch.
    """
    action_slug = slugify(action.name)
    ability_id = action_sim.id or f"{namespace}:ability/{statblock_slug}/{action_slug}"

    step: PrimitiveBase
    if action_sim.heal is not None:
        primitive_id = f"{namespace}:primitive/heal/{statblock_slug}-{action_slug}-{index}"
        step = HealPrimitive(id=primitive_id, dice=action_sim.heal.dice, cost=action_sim.cost)
    elif action_sim.kind is not None and action.kind in _UNCOMPILABLE_ACTION_KINDS:
        primitive_id = f"{namespace}:primitive/reaction/{statblock_slug}-{action_slug}-{index}"
        step = ReactionPrimitive(
            id=primitive_id,
            reaction_kind=action_sim.kind,
            die=action_sim.die,
            attack=action_sim.attack,
            bonus=action_sim.bonus,
            fraction=action_sim.fraction,
            damage_types=(
                tuple(t.lower() for t in action_sim.damage_types)
                if action_sim.damage_types is not None
                else None
            ),
            trigger=action_sim.trigger,
            cost=action_sim.cost,
        )
    elif action.kind in _UNCOMPILABLE_ACTION_KINDS:
        return None
    else:
        primitive_id = f"{namespace}:primitive/{action.kind}/{statblock_slug}-{action_slug}-{index}"
        compiler = ACTION_KIND_COMPILERS.get(action.kind)
        step = compiler(action, action_sim, primitive_id)

    # `action.usage` is a declared field on every real `Action` variant
    # (default `ActionUsage()`, never absent) — `getattr` only guards
    # `test_new_action_kind_needs_no_compiler_edit`'s bare duck-typed
    # `DummyAction`, which carries no `usage` at all.
    usage = getattr(action, "usage", None)
    return CompiledAbility(
        id=ability_id,
        name=action.name,
        step=step,
        action_cost=action_sim.action_cost or default_action_cost,
        concentration=bool(action_sim.concentration),
        once_per_turn=bool(action_sim.once_per_turn),
        legendary_cost=(usage.legendary_cost if usage is not None else None) or 1,
    )


def build_routine(block: dict[str, Any]) -> list[RoutineStep] | None:
    """Find the Multiattack action's routine from a statblock fence's raw
    ``actions``/``bonus_actions`` categories (port of
    `scripts/differential_harness.py`'s `_build_routine` — the same
    unfiltered-category walk :func:`~dndsim.rules.dnd5e_2014.attack_string.
    parse_action_category` can't do, since it drops a Multiattack entry from
    its own ``"actions"`` return). ``None`` for no Multiattack action, or
    phrasing :func:`parse_multiattack` can't read.
    """

    def parsed_names_and_multiattack(category: str) -> tuple[list[str], str | None]:
        names: list[str] = []
        multi_desc: str | None = None
        for raw in block.get(category) or []:
            if not isinstance(raw, dict) or _is_legendary_preamble(category, raw):
                continue
            action = parse_action(raw.get("name"), raw.get("desc"))
            names.append(action.name)
            if action.kind == "multiattack":
                multi_desc = action.desc
        return names, multi_desc

    main_names, multi_desc = parsed_names_and_multiattack("actions")
    bonus_names, _ = parsed_names_and_multiattack("bonus_actions")
    if multi_desc is None:
        return None
    return parse_multiattack(multi_desc, main_names + bonus_names)


def compile_statblock(
    content: StatblockContent,
    *,
    actions: list[Action],
    action_sim_data: dict[str, dict[str, Any] | None] | None = None,
    sim_data: dict[str, Any] | None = None,
    routine: list[RoutineStep] | None = None,
    namespace: str = "dnd5e_2014",
    action_categories: dict[str, str] | None = None,
    legendary_actions_per_round: int = 0,
) -> CompiledStatblock:
    """Compile one statblock's parsed content into its executable
    :class:`CompiledStatblock`.

    ``action_sim_data`` maps each action's (usage-stripped) name to its raw
    per-action `sim:` sub-map (``None``/absent defaults it). ``sim_data`` is
    the page's raw top-level `sim:` block (``None`` defaults to
    ``sim: { side: enemy }``, matching README's documented fallback for
    pages authored before this extension existed). ``action_categories``
    maps each action's name to the raw fence category it was parsed from
    (``"actions"``/``"bonus_actions"``/``"reactions"``/``"legendary_actions"``)
    — issue #60's own default for :class:`CompiledAbility.action_cost` when
    no per-action `sim.action_cost` overrides it, so a bonus-action-slot
    ability (Perrin's Healing Word) is recognized as one even though real
    content rarely authors `action_cost` explicitly. ``legendary_actions_per_round``
    is this statblock's own declared count (0 for a non-legendary creature),
    carried straight onto :attr:`CompiledStatblock.legendary_actions_per_round`
    — the caller (:func:`~dndsim.profile.load_compiled_statblock`) extracts
    it via :func:`~dndsim.rules.dnd5e_2014.attack_string.legendary_actions_per_round`
    from the raw fence's own ``legendary_actions`` preamble; this function
    never re-derives it from ``actions``.
    """
    slug = slugify(content.name)
    action_categories = action_categories or {}
    _DEFAULT_ACTION_COST_BY_CATEGORY: dict[str, str | None] = {
        "actions": "action",
        "bonus_actions": "bonus",
        "reactions": None,
        "legendary_actions": "legendary",
    }
    action_sim_data = action_sim_data or {}
    sim_block: SimBlock = parse_sim_block(sim_data, content.source)

    # A caster's sim.spellcasting pools (parsed by parse_sim_block above,
    # unused before issue #48) compile down to the exact same Action +
    # ActionSim pairs and ability Modifiers a statblock's own
    # actions/sim.abilities already produce — merged into the loops below
    # rather than carried on a separate CompiledStatblock field (ADR-0009:
    # "the simulator and policy know nothing about spells").
    all_actions = list(actions)
    spell_action_sim: dict[str, ActionSim] = {}
    spell_abilities: list[Any] = []
    spell_warnings: list[str] = []
    if sim_block.spellcasting:
        resource_ids = {r.id for r in sim_block.resources}
        for pool in sim_block.spellcasting:
            compiled_pool = compile_spellcasting(pool, resource_ids, content.source)
            all_actions.extend(compiled_pool.actions)
            spell_action_sim.update(compiled_pool.action_sim)
            spell_abilities.extend(compiled_pool.abilities)
            spell_warnings.extend(compiled_pool.warnings)

    # Issue #66: statblock.py's parsed ``traits`` (Magic Resistance, Pack
    # Tactics, Legendary Resistance, the generic save-advantage pattern)
    # compile into the same ability-Modifier vocabulary sim.abilities
    # already uses, rather than a bespoke code path — Magic Resistance
    # becomes a no-cost `{kind: advantage, on: save}` Modifier, which
    # `combat.py`'s existing `_activate_ability_primitives` pass (10956e68)
    # already sets `_CombatantState.save_advantage` from every round, no
    # page-authored `sim:` block required.
    trait_warnings: list[str] = []
    trait_primitives = [
        modifier_to_primitive(
            AdvantageModifier(on="save"),
            f"{namespace}:primitive/advantage/{slug}-trait-save-advantage-{i}",
        )
        for i in range(len(content.save_advantage))
    ]
    if content.legendary_resistance > 0:
        # No consumer exists yet (combat.py's `_activate_ability_primitives`
        # NOT_DONE note: `legendary_resistance_like` compiles but is not
        # executed by that pass) — compiled and named unwired, per issue
        # #66, rather than silently dropped. Measured cost: zero, since the
        # compiled Primitive is never read at resolution time.
        trait_primitives.append(
            modifier_to_primitive(
                LegendaryResistanceLikeModifier(),
                f"{namespace}:primitive/legendary_resistance_like/{slug}-trait",
            )
        )
        trait_warnings.append(
            f"legendary resistance ({content.legendary_resistance}/day) parsed but not "
            "modeled — compiles to legendary_resistance_like, which combat.py's ability-"
            "primitive activation pass does not execute; no consumer exists yet"
        )

    ability_primitives = tuple(
        modifier_to_primitive(ability, f"{namespace}:primitive/{ability.kind}/{slug}-{i}")
        for i, ability in enumerate((*sim_block.abilities, *spell_abilities))
    ) + tuple(trait_primitives)

    compiled_actions: list[CompiledAbility] = []
    unmodeled_warnings: list[str] = []
    for index, action in enumerate(all_actions):
        action_sim = spell_action_sim.get(action.name) or parse_action_sim(
            action_sim_data.get(action.name), content.source, f"actions[{index}].sim"
        )
        default_cost = _DEFAULT_ACTION_COST_BY_CATEGORY.get(action_categories.get(action.name, ""))
        compiled = compile_action(
            namespace, slug, index, action, action_sim, default_action_cost=default_cost
        )
        if compiled is not None:
            compiled_actions.append(compiled)
        elif action.kind == "unmodeled" and action_sim.kind is None:
            # Debug-mode surfacing (compile_action's own docstring: an
            # Unmodeled action with no sim.kind override compiles to
            # nothing at all — silently, previously untraced). Recorded
            # here rather than inside compile_action so a Multiattack
            # action's own, expected, silent drop (it becomes the routine
            # instead — see this function's `routine` handling below) never
            # gets flagged alongside it.
            unmodeled_warnings.append(
                f'"{action.name}" parsed as unmodeled prose (no attack/save/autodamage '
                "grammar matched, no sim.kind override) — dropped, never executes"
            )

    if content.advantage_if:
        # Issue #66: a statblock-level trait trigger (Pack Tactics ->
        # "ally_adjacent_to_target") applies to every compiled attack that
        # carries no per-action advantage_if of its own (attack_string.py's
        # "target_has:" prose grammar takes priority when both are
        # present — never overwritten). Only one trigger literal exists
        # today; a future second one would need a real precedence rule,
        # not silent last-wins.
        trait_trigger = content.advantage_if[0]
        compiled_actions = [
            (
                CompiledAbility(
                    id=c.id,
                    name=c.name,
                    step=c.step.model_copy(update={"advantage_if": trait_trigger}),
                    action_cost=c.action_cost,
                    concentration=c.concentration,
                    once_per_turn=c.once_per_turn,
                )
                if isinstance(c.step, AttackPrimitive) and c.step.advantage_if is None
                else c
            )
            for c in compiled_actions
        ]

    routine_by_ref: dict[str, str] = {}
    for c in compiled_actions:
        # A routine step may reference an action by its prose name or by an
        # authored `sim.id` — accept either, matching README's "id: stable
        # ref for routine/reactions".
        routine_by_ref[c.name] = c.id
        routine_by_ref[c.id] = c.id

    compiled_routine: list[RoutineStepPrimitive] = []
    for step in routine or []:
        ref = routine_by_ref.get(step.ref, step.ref)
        compiled_routine.append(
            RoutineStepPrimitive(
                ref=ref,
                count=step.count,
                alternatives=[routine_by_ref.get(a, a) for a in step.alternatives],
            )
        )

    # A parsed Multiattack routine takes priority (it already resolved
    # above). Absent one, an authored `sim.routine.<slot>` block (issue
    # #59's fix — previously parsed by parse_sim_block but wired nowhere,
    # so profile.py had to work around it by reading the raw fence itself)
    # feeds the same CompiledAbility ids, in `action`/`bonus`/`reaction`
    # slot order. `legendary` is deliberately excluded: legendary actions
    # are driven by the encounter timeline's own window, never a routine.
    if not compiled_routine and sim_block.routine is not None:
        for slot in ("action", "bonus", "reaction"):
            for ref in sim_block.routine.get(slot) or []:
                if not isinstance(ref, str):
                    continue
                resolved_ref = routine_by_ref.get(ref, ref)
                compiled_routine.append(
                    RoutineStepPrimitive(ref=resolved_ref, count=1, alternatives=[])
                )

    return CompiledStatblock(
        id=f"{namespace}:statblock/{slug}",
        name=content.name,
        ac=content.ac,
        hp=content.hp,
        side=sim_block.side,
        resources=tuple(sim_block.resources),
        ability_primitives=ability_primitives,
        compiled_actions=tuple(compiled_actions),
        routine=tuple(compiled_routine),
        warnings=tuple(content.warnings)
        + tuple(spell_warnings)
        + tuple(trait_warnings)
        + tuple(unmodeled_warnings),
        position=sim_block.position,
        save_bonuses=_save_bonuses(content),
        defenses=content.defenses,
        legendary_actions_per_round=legendary_actions_per_round,
        abilities=dict(content.abilities),
    )
