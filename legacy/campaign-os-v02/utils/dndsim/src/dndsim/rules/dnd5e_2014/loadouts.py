"""Loadouts, creature overrides, and scenarios (issue #49) — the
agent-authored judgment layer that lets a DM express a specific fight
without editing a creature's own page, built onto this engine's compiled
representation (:mod:`dndsim.rules.dnd5e_2014.compile`).

Three top-level keys (real content under
``vault/campaigns/shattered-sea/pcs/combat-profile/loadouts/*.loadouts.yaml``):

- **loadouts** — named, per-combatant modifier sets (``applies_to`` a
  combatant's slug or display name).
- **creature_overrides** — modifiers a statblock's prose left unmodeled,
  attached by slug/name, applied unconditionally (not name-selected).
- **scenarios** — a roster (``party``/``enemies``, each a page file plus an
  optional loadout name and a count) bundled with a ``lair:`` list and
  targeting/formation assumptions. A scenario's ``lair:`` list is scenario
  data, never a field on any one combatant — it belongs to the encounter
  the same way ``run_round``'s ``lair_action`` window
  (:mod:`dndsim.rules.dnd5e_2014.encounter_timeline`) fires once per round
  regardless of which side "owns" the lair.

Every modifier — in a ``loadouts[].modifiers``, a ``creature_overrides[].
modifiers``, or nowhere else — validates through
:func:`~dndsim.rules.dnd5e_2014.sim_extension.describe_modifier` against
the exact same :data:`~dndsim.rules.dnd5e_2014.sim_extension.MODIFIER_KINDS`
registry a statblock's own ``sim.abilities`` validates against: one schema,
two authoring surfaces (PRD "Modifier definitions validate against the same
tagged-union vocabulary as page-authored content"). This module raises no
competing modifier-content error — :class:`~dndsim.rules.dnd5e_2014.
sim_extension.SimExtensionError` propagates unchanged from
:func:`~dndsim.rules.dnd5e_2014.sim_extension.describe_modifier` for a bad
modifier, naming the same field the reference would; a scenario-only kind
used on a combatant's own page is rejected by :func:`~dndsim.rules.
dnd5e_2014.sim_extension.parse_sim_block` already (its own ``SCENARIO_ONLY_
KINDS`` check), not duplicated here. :class:`LoadoutError` is reserved for
this module's OWN structure — a missing ``name``, a bad ``schema_version``,
an unknown targeting policy, a malformed lair entry.

**Reserved loadout names** (:func:`resolve_loadout`, README § Loadout file
schema): ``optimal`` (no loadout modifiers — a combatant's own block runs
under the perfect-play auto-policy), ``min`` (the implicit resource floor —
every declared resource pool capped to 0, so a costed reaction stays silent
rather than a bare empty modifier list leaving pools full), ``avg``/``max``
(run bare with a note when unauthored, matching an authored loadout of any
name when one exists).

**Applying** a resolved modifier set to a compiled statblock
(:func:`apply_modifiers`) reuses exactly the same compile step a
statblock's own ``sim.abilities`` goes through
(:func:`~dndsim.rules.dnd5e_2014.primitives.modifier_to_primitive`) —
a loadout modifier and a page-authored ability produce indistinguishable
:class:`~dndsim.rules.dnd5e_2014.primitives.PrimitiveBase` instances, appended
onto :attr:`~dndsim.rules.dnd5e_2014.compile.CompiledStatblock.ability_primitives`.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any, NoReturn

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from dndsim.rules.dnd5e_2014.compile import CompiledStatblock, slugify
from dndsim.rules.dnd5e_2014.dice import DiceExprError, validate_dice_expr
from dndsim.rules.dnd5e_2014.primitives import modifier_to_primitive
from dndsim.rules.dnd5e_2014.sim_extension import (
    EFFECT_TAGS,
    SCENARIO_ONLY_KINDS,
    TARGETING_POLICIES,
    ModifierBase,
    OnFailBlock,
    describe_modifier,
)
from dndsim.rules.dnd5e_2014.yaml_safe import safe_load as _yaml_load

LOADOUT_SCHEMA_VERSION = 1

#: The reserved-behavior triplet (README § Loadout file schema) plus
#: `optimal`, the CLI's own omitted-flag default.
RESERVED_LOADOUT_NAMES: frozenset[str] = frozenset({"optimal", "min", "avg", "max"})


class LoadoutError(ValueError):
    """A loadout/scenario file's own structure failed validation — never a
    modifier's content, which raises :class:`~dndsim.rules.dnd5e_2014.
    sim_extension.SimExtensionError` instead (see module docstring)."""


def fail(source: str, path: str, message: str) -> NoReturn:
    raise LoadoutError(f"loadout: {source} — {path}: {message}")


def _check_dice(expr: str, field_path: str) -> None:
    try:
        validate_dice_expr(expr, field_path)
    except DiceExprError as err:
        raise ValueError(str(err)) from err


# --- parsed shapes -----------------------------------------------------


@dataclass(frozen=True, slots=True)
class Loadout:
    name: str
    applies_to: str
    modifiers: tuple[ModifierBase, ...] = ()


@dataclass(frozen=True, slots=True)
class CreatureOverride:
    applies_to: str
    modifiers: tuple[ModifierBase, ...] = ()


@dataclass(frozen=True, slots=True)
class RosterEntry:
    file: str
    loadout: str | None = None
    count: int = 1


class LairAction(BaseModel):
    """One scenario-level lair action — a save-action-shaped entry fired
    once per round on the enemy side's behalf
    (:data:`~dndsim.rules.dnd5e_2014.encounter_timeline.LAIR_ACTION`),
    cycling, never the same entry two rounds running (README § Lair
    actions). Vault pages keep lair actions in prose; this is where they
    are encoded for simulation.

    ``on_fail``'s dice/effect-tag checks go beyond ``loadout.mjs``, which
    passes a lair's ``on_fail`` through unvalidated — lair actions are not
    part of the closed Modifier vocabulary (no ``kind`` field), so nothing
    in ADR-0007's "validate clause-for-clause against the reference"
    constraint applies here. The checks mirror :class:`~dndsim.rules.
    dnd5e_2014.sim_extension.ActionSim`'s own ``on_fail`` validation instead,
    for the same reason a DM wants a named-field rejection on this content
    too (PRD user story #20).
    """

    model_config = ConfigDict(frozen=True, extra="allow")

    id: str
    dc: float
    save: str
    on_fail: OnFailBlock = Field(default_factory=OnFailBlock)
    half_on_save: bool = False
    targets: dict[str, Any] = Field(default_factory=lambda: {"area": True, "radius": 15})

    @model_validator(mode="after")
    def _check(self) -> LairAction:
        if self.id == "":
            raise ValueError("lair[].id: must be a non-empty string")
        if self.save == "":
            raise ValueError("lair[].save: must be a non-empty string")
        for i, damage in enumerate(self.on_fail.damage):
            _check_dice(damage.dice, f"on_fail.damage[{i}].dice")
        for i, rider in enumerate(self.on_fail.effects):
            if rider.effect.lower() not in EFFECT_TAGS:
                raise ValueError(
                    f'on_fail.effects[{i}]: unknown condition tag "{rider.effect.lower()}"'
                )
        return self


@dataclass(frozen=True, slots=True)
class ScenarioAssumptions:
    surprise: str = "none"
    targeting: dict[str, str] = field(default_factory=dict)
    # `formation` names a FORMATIONS deployment; `start_engaged` is the
    # deprecated boolean alias
    # (`False` -> "skirmish", otherwise "engaged").
    formation: str = "engaged"
    start_engaged: bool = True


@dataclass(frozen=True, slots=True)
class Scenario:
    name: str
    party: tuple[RosterEntry, ...] = ()
    enemies: tuple[RosterEntry, ...] = ()
    lair: tuple[LairAction, ...] = ()
    assumptions: ScenarioAssumptions = field(default_factory=ScenarioAssumptions)


@dataclass(frozen=True, slots=True)
class LoadoutFile:
    source: str
    loadouts: tuple[Loadout, ...] = ()
    creature_overrides: tuple[CreatureOverride, ...] = ()
    scenarios: tuple[Scenario, ...] = ()


# --- parsing -------------------------------------------------------------


def validate_modifier(mod: Any, source: str, path: str) -> ModifierBase:
    """Validate one raw modifier map through the shared
    :func:`~dndsim.rules.dnd5e_2014.sim_extension.describe_modifier`
    vocabulary — the single point where a loadout/override modifier and a
    page-authored ``sim.abilities`` modifier run through identical
    validation."""
    if not isinstance(mod, dict):
        fail(source, path, "modifier must be a map")
    kind = mod.get("kind")
    if not isinstance(kind, str):
        fail(source, path, 'modifier must declare a string "kind"')
    data = {k: v for k, v in mod.items() if k != "kind"}
    return describe_modifier(kind, source, path, **data)


def _parse_loadout(entry: Any, source: str, path: str) -> Loadout:
    if not isinstance(entry, dict):
        fail(source, path, "must be a map")
    name = entry.get("name")
    if not isinstance(name, str) or name == "":
        fail(source, f"{path}.name", "required")
    applies_to = entry.get("applies_to")
    if not isinstance(applies_to, str) or applies_to == "":
        fail(source, f"{path}.applies_to", "required")
    modifiers = tuple(
        validate_modifier(m, source, f"{path}.modifiers[{j}]")
        for j, m in enumerate(entry.get("modifiers") or [])
    )
    return Loadout(name=name, applies_to=applies_to, modifiers=modifiers)


def _parse_creature_override(entry: Any, source: str, path: str) -> CreatureOverride:
    if not isinstance(entry, dict):
        fail(source, path, "must be a map")
    applies_to = entry.get("applies_to")
    if not isinstance(applies_to, str) or applies_to == "":
        fail(source, f"{path}.applies_to", "required")
    modifiers = tuple(
        validate_modifier(m, source, f"{path}.modifiers[{j}]")
        for j, m in enumerate(entry.get("modifiers") or [])
    )
    return CreatureOverride(applies_to=applies_to, modifiers=modifiers)


def _parse_roster_entry(entry: Any, source: str, path: str) -> RosterEntry:
    if not isinstance(entry, dict):
        fail(source, path, "must be a map")
    file_path = entry.get("file")
    if not isinstance(file_path, str) or file_path == "":
        fail(source, f"{path}.file", "required")
    loadout = entry.get("loadout")
    if loadout is not None and not isinstance(loadout, str):
        fail(source, f"{path}.loadout", "must be a string")
    count = entry.get("count", 1)
    if not isinstance(count, int) or isinstance(count, bool) or count < 1:
        fail(source, f"{path}.count", "must be a positive integer")
    return RosterEntry(file=file_path, loadout=loadout, count=count)


def _parse_lair_action(entry: Any, source: str, path: str) -> LairAction:
    if not isinstance(entry, dict):
        fail(source, path, "must be a map")
    try:
        return LairAction.model_validate(entry)
    except ValidationError as err:
        fail(source, path, str(err))


def _parse_scenario(entry: Any, source: str, path: str) -> Scenario:
    if not isinstance(entry, dict):
        fail(source, path, "must be a map")
    name = entry.get("name")
    if not isinstance(name, str) or name == "":
        fail(source, f"{path}.name", "required")
    party = tuple(
        _parse_roster_entry(e, source, f"{path}.party[{j}]")
        for j, e in enumerate(entry.get("party") or [])
    )
    enemies = tuple(
        _parse_roster_entry(e, source, f"{path}.enemies[{j}]")
        for j, e in enumerate(entry.get("enemies") or [])
    )
    lair = tuple(
        _parse_lair_action(e, source, f"{path}.lair[{j}]")
        for j, e in enumerate(entry.get("lair") or [])
    )
    assumptions_raw = entry.get("assumptions") or {}
    targeting = dict(assumptions_raw.get("targeting") or {})
    for side_name, policy in targeting.items():
        if policy not in TARGETING_POLICIES:
            fail(
                source,
                f"{path}.assumptions.targeting.{side_name}",
                f'unknown policy "{policy}"',
            )
    start_engaged = assumptions_raw.get("start_engaged", True) is not False
    formation = assumptions_raw.get("formation") or (
        "skirmish" if assumptions_raw.get("start_engaged") is False else "engaged"
    )
    assumptions = ScenarioAssumptions(
        surprise=assumptions_raw.get("surprise", "none"),
        targeting=targeting,
        formation=formation,
        start_engaged=start_engaged,
    )
    return Scenario(name=name, party=party, enemies=enemies, lair=lair, assumptions=assumptions)


def parse_loadout_file(data: dict[str, Any] | None, source: str) -> LoadoutFile:
    """Validate one already-loaded loadout-file mapping (the pure-parse
    half — separated from :func:`load_loadout_file`'s disk read so tests
    can drive it with an inline dict, matching :func:`~dndsim.rules.
    dnd5e_2014.sim_extension.parse_sim_block`'s own split)."""
    if data is None or not isinstance(data, dict):
        fail(source, "<root>", "file is empty or not a mapping")
    if data.get("schema_version") != LOADOUT_SCHEMA_VERSION:
        fail(source, "schema_version", f"must be {LOADOUT_SCHEMA_VERSION}")
    loadouts = tuple(
        _parse_loadout(e, source, f"loadouts[{i}]")
        for i, e in enumerate(data.get("loadouts") or [])
    )
    creature_overrides = tuple(
        _parse_creature_override(e, source, f"creature_overrides[{i}]")
        for i, e in enumerate(data.get("creature_overrides") or [])
    )
    scenarios = tuple(
        _parse_scenario(e, source, f"scenarios[{i}]")
        for i, e in enumerate(data.get("scenarios") or [])
    )
    return LoadoutFile(
        source=source, loadouts=loadouts, creature_overrides=creature_overrides, scenarios=scenarios
    )


def load_loadout_file(path: str | Path) -> LoadoutFile:
    """Read, YAML-parse, and validate one loadout file from disk."""
    p = Path(path)
    try:
        raw = p.read_text(encoding="utf-8")
    except OSError as err:
        raise LoadoutError(f"loadout: cannot read {p}: {err}") from err
    try:
        data = _yaml_load(raw)
    except yaml.YAMLError as err:
        raise LoadoutError(f"loadout: cannot parse {p}: {err}") from err
    return parse_loadout_file(data, str(p))


def merge_loadout_files(files: Sequence[LoadoutFile]) -> LoadoutFile:
    """Merge several loadout files — later files extend earlier ones,
    matching ``mergeLoadoutFiles``'s append-only semantics (no
    later-wins override; a duplicate name/applies_to pair is simply two
    entries, exactly as the reference behaves)."""
    loadouts: list[Loadout] = []
    creature_overrides: list[CreatureOverride] = []
    scenarios: list[Scenario] = []
    for f in files:
        loadouts.extend(f.loadouts)
        creature_overrides.extend(f.creature_overrides)
        scenarios.extend(f.scenarios)
    sources = ", ".join(f.source for f in files) or "<empty>"
    return LoadoutFile(
        source=sources,
        loadouts=tuple(loadouts),
        creature_overrides=tuple(creature_overrides),
        scenarios=tuple(scenarios),
    )


def find_scenario(merged: LoadoutFile, name: str) -> Scenario:
    for scenario in merged.scenarios:
        if scenario.name == name:
            return scenario
    raise LoadoutError(f'loadout: no scenario named "{name}"')


# --- resolution + application ---------------------------------------------


def _matches(applies_to: str, combatant_id: str, combatant_name: str) -> bool:
    key = applies_to.strip().lower()
    return combatant_id.strip().lower() == key or combatant_name.strip().lower() == key


@dataclass(frozen=True, slots=True)
class ResolvedLoadout:
    name: str
    modifiers: tuple[ModifierBase, ...]
    authored: bool
    note: str | None = None


def _zero_all_pools(resource_ids: Sequence[str]) -> tuple[ModifierBase, ...]:
    """Implicit resource floor for the `min` reserved name: a
    `resource_budget` zeroing every pool the combatant declares. An EMPTY
    modifier list would leave pools full and let a block-declared costed
    reaction (Shield, Cutting Words) still fire, which is not a floor at
    all — matches ``loadout.mjs``'s ``zeroAllPools``."""
    if not resource_ids:
        return ()
    pools = {rid: 0 for rid in resource_ids}
    return (describe_modifier("resource_budget", "<loadout:min>", "pools", pools=pools),)


def resolve_loadout(
    merged: LoadoutFile,
    *,
    combatant_id: str,
    combatant_name: str,
    name: str,
    resource_ids: Sequence[str] = (),
) -> ResolvedLoadout:
    """Resolve the modifier set for one combatant + loadout name (README §
    Loadout file schema's reserved-name behavior; port of ``loadout.mjs``'s
    ``resolveLoadout``).

    An authored loadout of any name (reserved or not) wins if one matches
    both ``name`` and the combatant. Absent one: ``optimal`` runs no
    modifiers, ``min`` defaults to :func:`_zero_all_pools`, ``avg``/``max``
    run bare with a note. Any other unauthored name is an error — there is
    no silent fallback for a typo'd loadout name.
    """
    for loadout in merged.loadouts:
        if loadout.name == name and _matches(loadout.applies_to, combatant_id, combatant_name):
            return ResolvedLoadout(name=name, modifiers=loadout.modifiers, authored=True)
    if name == "optimal":
        return ResolvedLoadout(name=name, modifiers=(), authored=False)
    if name == "min":
        return ResolvedLoadout(name=name, modifiers=_zero_all_pools(resource_ids), authored=False)
    if name in ("avg", "max"):
        return ResolvedLoadout(
            name=name,
            modifiers=(),
            authored=False,
            note=f'no "{name}" loadout authored — optimal auto-policy ran instead',
        )
    raise LoadoutError(f'loadout: no loadout named "{name}" for {combatant_name}')


def apply_modifiers(
    statblock: CompiledStatblock,
    modifiers: Sequence[ModifierBase],
    *,
    tag: str,
    namespace: str = "dnd5e_2014",
) -> CompiledStatblock:
    """Apply ``modifiers`` onto a compiled statblock. Returns a new
    :class:`CompiledStatblock`; the input is never mutated (it is frozen).

    Two application paths, split by :data:`~dndsim.rules.dnd5e_2014.
    sim_extension.SCENARIO_ONLY_KINDS`:

    - An ordinary ability-modifier kind compiles to a Primitive via
      :func:`~dndsim.rules.dnd5e_2014.primitives.modifier_to_primitive` and
      is appended to ``ability_primitives`` — the exact same compile step a
      statblock's own ``sim.abilities`` goes through, so a loadout modifier
      and a page-authored ability are indistinguishable once compiled.
    - ``resource_budget`` (the one scenario-only kind real content actually
      authors) has no Primitive counterpart by design
      (:data:`~dndsim.rules.dnd5e_2014.primitives.ABILITY_PRIMITIVES` never
      registers a scenario-only kind — it isn't a combatant capability, it
      caps one) — its ``pools`` mapping instead overrides each named
      resource's declared ``max``, which is what "a floor" or "a per-fight
      budget" means for a pool the routine spends against.
    - The remaining scenario-only kinds (``setup_round``,
      ``assume_rider_triggers``, ``save_action_priority``) and any
      ``resource_budget`` authored with no ``pools`` mapping (real content:
      ``{resource, spend_per_encounter}``) are not yet consumed by any
      engine mechanism — carried through as a named warning rather than
      silently dropped (PRD: "tell me loudly when it cannot model
      something").
    """
    if not modifiers:
        return statblock
    slug = slugify(statblock.name)

    compilable = [m for m in modifiers if m.kind not in SCENARIO_ONLY_KINDS]  # type: ignore[attr-defined]
    new_primitives = tuple(
        modifier_to_primitive(m, f"{namespace}:primitive/{m.kind}/{slug}-{tag}-{i}")  # type: ignore[attr-defined]
        for i, m in enumerate(compilable)
    )

    resources = statblock.resources
    unmodeled_warnings: list[str] = []
    for m in modifiers:
        if m.kind == "resource_budget":  # type: ignore[attr-defined]
            pools: dict[str, int] = m.pools  # type: ignore[attr-defined]
            if pools:
                resources = tuple(
                    r.model_copy(update={"max": pools[r.id]}) if r.id in pools else r
                    for r in resources
                )
            else:
                unmodeled_warnings.append(
                    f'loadout modifier "resource_budget" ({tag}) carries no "pools" mapping — '
                    "not yet consumed by the engine, carried through unapplied"
                )
        elif m.kind in SCENARIO_ONLY_KINDS:  # type: ignore[attr-defined]
            unmodeled_warnings.append(
                f'loadout modifier "{m.kind}" ({tag}) is a scenario assumption not yet '  # type: ignore[attr-defined]
                "consumed by the engine — carried through unapplied"
            )

    return replace(
        statblock,
        ability_primitives=statblock.ability_primitives + new_primitives,
        resources=resources,
        warnings=statblock.warnings + tuple(unmodeled_warnings),
    )


def apply_creature_overrides(
    statblock: CompiledStatblock,
    merged: LoadoutFile,
    *,
    combatant_id: str,
    combatant_name: str,
) -> CompiledStatblock:
    """Attach every matching creature override's modifiers — unconditional,
    never name-selected (unlike a loadout): a creature override encodes a
    trait the prose left unmodeled, not a scenario choice."""
    out = statblock
    for i, override in enumerate(merged.creature_overrides):
        if _matches(override.applies_to, combatant_id, combatant_name):
            out = apply_modifiers(out, override.modifiers, tag=f"override-{i}")
    return out


def apply_loadout(
    statblock: CompiledStatblock,
    merged: LoadoutFile,
    *,
    combatant_id: str,
    combatant_name: str,
    name: str,
) -> tuple[CompiledStatblock, ResolvedLoadout]:
    """Resolve and apply one loadout name in a single call — the common
    case a scenario roster entry and a CLI ``--loadout`` selection both
    need."""
    resource_ids = tuple(r.id for r in statblock.resources)
    resolved = resolve_loadout(
        merged,
        combatant_id=combatant_id,
        combatant_name=combatant_name,
        name=name,
        resource_ids=resource_ids,
    )
    applied = apply_modifiers(statblock, resolved.modifiers, tag=f"loadout-{name}")
    return applied, resolved


# --- scenario assembly -----------------------------------------------------


@dataclass(frozen=True, slots=True)
class ResolvedCombatant:
    entry: RosterEntry
    statblock: CompiledStatblock
    loadout: ResolvedLoadout


@dataclass(frozen=True, slots=True)
class ResolvedScenario:
    """A scenario reproduced from its name: every roster entry loaded,
    creature-overridden, and loadout-applied, plus the scenario's own
    ``lair`` list carried through untouched — lair actions attach to this,
    the encounter-level result, never to any one
    :class:`ResolvedCombatant`."""

    name: str
    party: tuple[ResolvedCombatant, ...]
    enemies: tuple[ResolvedCombatant, ...]
    lair: tuple[LairAction, ...]
    assumptions: ScenarioAssumptions


def _resolve_roster_entry(
    entry: RosterEntry,
    merged: LoadoutFile,
    *,
    repo_root: Path,
    default_loadout: str,
) -> ResolvedCombatant:
    # Imported here, not at module scope: `dndsim.profile` sits above this
    # rules pack (it composes several rules-pack modules for the `profile`
    # CLI verb), so importing it at module scope would invert ADR-0007's
    # layering for every caller of this module, not only scenario
    # resolution. `load_compiled_statblock` is still the right function to
    # reuse (WHAT EXISTS: "the page->CompiledStatblock loader. Reuse it.") —
    # deferring the import keeps that reuse without the inverted dependency
    # biting an import of `loadouts.py` that never touches scenarios.
    from dndsim.profile import load_compiled_statblock

    page_path = repo_root / entry.file
    markdown = page_path.read_text(encoding="utf-8")
    statblock, _block = load_compiled_statblock(markdown, str(page_path))
    slug = slugify(statblock.name)
    statblock = apply_creature_overrides(
        statblock, merged, combatant_id=slug, combatant_name=statblock.name
    )
    loadout_name = entry.loadout or default_loadout
    statblock, resolved = apply_loadout(
        statblock, merged, combatant_id=slug, combatant_name=statblock.name, name=loadout_name
    )
    return ResolvedCombatant(entry=entry, statblock=statblock, loadout=resolved)


def resolve_scenario(
    scenario: Scenario,
    merged: LoadoutFile,
    *,
    repo_root: Path,
    default_loadout: str = "optimal",
) -> ResolvedScenario:
    """Reproduce ``scenario`` by name: load every roster entry's page,
    apply matching creature overrides, resolve and apply each entry's own
    loadout (or ``default_loadout`` when the entry names none), and carry
    the scenario's ``lair:`` list through unchanged. Deterministic — the
    same scenario resolved twice from the same files produces byte-for-byte
    identical Primitives, which is the concrete sense in which "a named
    scenario reproduces a specific encounter"."""
    party = tuple(
        _resolve_roster_entry(e, merged, repo_root=repo_root, default_loadout=default_loadout)
        for e in scenario.party
    )
    enemies = tuple(
        _resolve_roster_entry(e, merged, repo_root=repo_root, default_loadout=default_loadout)
        for e in scenario.enemies
    )
    return ResolvedScenario(
        name=scenario.name,
        party=party,
        enemies=enemies,
        lair=scenario.lair,
        assumptions=scenario.assumptions,
    )
