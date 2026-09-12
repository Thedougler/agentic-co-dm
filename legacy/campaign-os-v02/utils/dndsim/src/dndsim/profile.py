"""``profile`` mode (issue #51): one character's own statistical picture with
no specific opponent — exact closed-form hit chance across an AC ladder, a
sampled damage-per-round distribution, exact closed-form chance to be hit,
and effective-hit-points arithmetic. Built on this engine's own
compiled-Primitive representation
(:func:`~dndsim.rules.dnd5e_2014.compile.compile_statblock`).

Closed-form figures (hit tables, be-hit table, survivability) are exact —
no sampling; only the damage-per-round table is Monte Carlo, because a
routine's total damage has no closed form once multiple attacks and crit
variance combine.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import yaml

from dndsim.core.rng import BatchRNG, substream_seed
from dndsim.rules.dnd5e_2014.attack_string import (
    Action,
    DamageGroup,
    legendary_actions_per_round,
    parse_action_category,
    parse_name_usage,
)
from dndsim.rules.dnd5e_2014.compile import CompiledStatblock, build_routine, compile_statblock
from dndsim.rules.dnd5e_2014.dice import parse_dice_expr
from dndsim.rules.dnd5e_2014.primitives import AttackPrimitive, RoutineStepPrimitive
from dndsim.rules.dnd5e_2014.statblock import (
    StatblockParseError,
    extract_statblock_fence,
    parse_statblock_page,
)
from dndsim.rules.dnd5e_2014.yaml_safe import safe_load as _yaml_safe_load

_ROUTINE_ACTION_CATEGORIES: tuple[str, ...] = (
    "actions",
    "bonus_actions",
    "reactions",
    "legendary_actions",
)


class ProfileError(ValueError):
    """A page has no ```statblock fence, or its fence has no attack Primitive
    a routine can be built from."""


def load_compiled_statblock(markdown: str, source: str) -> tuple[CompiledStatblock, dict[str, Any]]:
    """Parse one page's ```statblock fence and every action category, and
    compile the result — the same assembly ``tests/rules/test_compile.py``
    and ``scripts/differential_harness.py`` already hand-build inline, given
    a single reusable home now that a CLI verb needs it too. Returns the
    compiled statblock plus the raw fence mapping (the mapping is kept for
    call-site compatibility; routine resolution reads only
    ``CompiledStatblock.routine`` — see :func:`~dndsim.rules.dnd5e_2014.
    compile.compile_statblock`)."""
    content = parse_statblock_page(markdown, source)
    if content is None:
        raise ProfileError(f"{source}: no ```statblock fence (or an empty one)")
    fence = extract_statblock_fence(markdown)
    assert fence is not None  # content is not None => fence matched above
    try:
        block = _yaml_safe_load(fence)
    except yaml.YAMLError as err:
        raise StatblockParseError(f"statblock: YAML parse failed in {source}: {err}") from err
    if not isinstance(block, dict):
        raise ProfileError(f"{source}: statblock fence did not parse to a mapping")

    all_actions: list[Action] = []
    action_sim_data: dict[str, dict[str, object] | None] = {}
    # Issue #60: which raw fence category each action came from — the
    # action/bonus/reaction/legendary split is otherwise lost once every
    # category's actions flatten into one `all_actions` list below, and
    # `compile_statblock` needs it to default a bonus-action-slot ability's
    # `action_cost` when no per-action `sim.action_cost` overrides it.
    action_categories: dict[str, str] = {}
    for category in _ROUTINE_ACTION_CATEGORIES:
        parsed, _warnings = parse_action_category(block.get(category), category)
        all_actions.extend(parsed)
        for action in parsed:
            action_categories[action.name] = category
        for raw in block.get(category) or []:
            if isinstance(raw, dict) and raw.get("sim") is not None:
                name, _usage = parse_name_usage(raw.get("name") or "")
                action_sim_data[name] = raw["sim"]

    legendary_per_round = legendary_actions_per_round(block.get("legendary_actions"))

    compiled = compile_statblock(
        content,
        actions=all_actions,
        action_sim_data=action_sim_data,
        sim_data=block.get("sim"),
        routine=build_routine(block),
        action_categories=action_categories,
        legendary_actions_per_round=legendary_per_round,
    )
    return compiled, block


def hit_chance(
    to_hit: int, ac: int, *, mode: str = "straight", crit_range: int = 20
) -> tuple[float, float]:
    """Exact ``(p_hit, p_crit)`` for one attack roll — ``p_hit`` includes
    crits. Closed-form, no sampling; port of ``lib/closed-form.mjs``'s
    ``hitChance``. ``mode`` is one of ``"straight"``/``"advantage"``/
    ``"disadvantage"``; nat 1 always misses, nat >= ``crit_range`` always
    hits and crits."""
    crit_faces = 21 - crit_range
    p_crit_single = crit_faces / 20
    needed = ac - to_hit
    lowest_hitting_face = min(max(needed, 2), crit_range)
    p_hit_single = (21 - lowest_hitting_face) / 20

    if mode == "advantage":
        return 1 - (1 - p_hit_single) ** 2, 1 - (1 - p_crit_single) ** 2
    if mode == "disadvantage":
        return p_hit_single**2, p_crit_single**2
    return p_hit_single, p_crit_single


@dataclass(frozen=True, slots=True)
class HitTableRow:
    ac: int
    p_hit: float
    p_crit: float


@dataclass(frozen=True, slots=True)
class HitTable:
    id: str
    name: str
    to_hit: int
    rows: tuple[HitTableRow, ...]


def hit_tables(
    statblock: CompiledStatblock, ac_sweep: list[int], *, mode: str = "straight"
) -> list[HitTable]:
    """Closed-form hit table for every attack action the statblock declares
    (whether or not it's in the sampled routine) — a PC wants to see every
    weapon's math, not only the one currently in rotation."""
    tables: list[HitTable] = []
    for ability in statblock.compiled_actions:
        if not isinstance(ability.step, AttackPrimitive):
            continue
        rows = []
        for ac in ac_sweep:
            p_hit, p_crit = hit_chance(ability.step.to_hit, ac, mode=mode)
            rows.append(HitTableRow(ac=ac, p_hit=p_hit, p_crit=p_crit))
        tables.append(
            HitTable(id=ability.id, name=ability.name, to_hit=ability.step.to_hit, rows=tuple(rows))
        )
    return tables


@dataclass(frozen=True, slots=True)
class BeHitRow:
    bonus: int
    p_hit: float
    p_crit: float


def be_hit_table(ac: int, attack_bonus_sweep: list[int]) -> list[BeHitRow]:
    """Closed-form chance an incoming attack at each bonus hits this
    character — the PC's own AC read as a defender's, port of
    ``lib/pc-profile.mjs``'s ``beHitTable``."""
    return [
        BeHitRow(bonus=bonus, p_hit=(p := hit_chance(bonus, ac))[0], p_crit=p[1])
        for bonus in attack_bonus_sweep
    ]


@dataclass(frozen=True, slots=True)
class SurvivabilityColumn:
    damage_per_hit: int
    expected_attacks: float


@dataclass(frozen=True, slots=True)
class SurvivabilityRow:
    bonus: int
    columns: tuple[SurvivabilityColumn, ...]


def hits_survivable(
    hp_max: int,
    ac: int,
    attack_bonus_sweep: list[int],
    damage_per_hit: tuple[int, ...] = (5, 10, 15, 20),
) -> list[SurvivabilityRow]:
    """Expected incoming attacks survived at each attack-bonus x
    damage-per-hit combination — pure arithmetic, no monster table baked
    in. A crit adds ~50% extra on the crit share (the dice half of a
    typical dice+mod split, doubled) — a stated approximation, matching
    ``lib/pc-profile.mjs``'s own documented one. This is the closed-form
    "effective hit points" figure: how many hits of a given size this
    character can expect to take before dropping."""
    rows: list[SurvivabilityRow] = []
    for bonus in attack_bonus_sweep:
        p_hit, p_crit = hit_chance(bonus, ac)
        columns = []
        for dmg in damage_per_hit:
            denom = p_hit * dmg + p_crit * dmg * 0.5
            expected = hp_max / denom if denom > 0 else float("inf")
            columns.append(SurvivabilityColumn(damage_per_hit=dmg, expected_attacks=expected))
        rows.append(SurvivabilityRow(bonus=bonus, columns=tuple(columns)))
    return rows


@dataclass(frozen=True, slots=True)
class DprSummary:
    mean: float
    stddev: float
    min: float
    max: float
    p5: float
    p25: float
    p50: float
    p75: float
    p95: float


def _summarize(samples: np.ndarray) -> DprSummary:
    return DprSummary(
        mean=float(samples.mean()),
        stddev=float(samples.std()),
        min=float(samples.min()),
        max=float(samples.max()),
        p5=float(np.percentile(samples, 5)),
        p25=float(np.percentile(samples, 25)),
        p50=float(np.percentile(samples, 50)),
        p75=float(np.percentile(samples, 75)),
        p95=float(np.percentile(samples, 95)),
    )


def _roll_attack_damage(
    rng: BatchRNG, iterations: int, to_hit: int, ac: int, damage: list[DamageGroup]
) -> np.ndarray:
    """One attack roll (straight, no advantage) plus its damage, sampled
    ``iterations`` times at once. A natural 20 always hits and doubles
    every damage group's dice (not its flat modifier); a natural 1 always
    misses — matching ``AttackDamageMechanic.resolve``'s single-damage-group
    case, generalized here to a multi-group action (e.g. a weapon attack
    plus a fire rider)."""
    d20 = rng.integers(1, 21, size=iterations)
    crit = d20 == 20
    fumble = d20 == 1
    hit = (~fumble) & (crit | (d20 + to_hit >= ac))

    total = np.zeros(iterations, dtype=np.float64)
    for group in damage:
        parsed = parse_dice_expr(group.dice)
        group_total = np.full(iterations, float(parsed.flat), dtype=np.float64)
        for term in parsed.dice:
            rolls = rng.integers(1, term.sides + 1, size=(term.count, iterations)).sum(axis=0)
            group_total += term.sign * rolls
            crit_rolls = rng.integers(1, term.sides + 1, size=(term.count, iterations)).sum(axis=0)
            group_total += np.where(crit, term.sign * crit_rolls, 0.0)
        total += group_total
    return np.where(hit, total, 0.0)


@dataclass(frozen=True, slots=True)
class DprRow:
    ac: int
    summary: DprSummary


def dpr_distribution(
    statblock: CompiledStatblock,
    routine: list[RoutineStepPrimitive],
    ac_sweep: list[int],
    *,
    iterations: int,
    seed: int,
) -> tuple[list[DprRow], list[str]]:
    """Monte Carlo damage-per-round distribution vs. each AC in the sweep,
    resolving every attack step of ``routine`` against a passive,
    infinite-HP dummy. Returns ``(rows, skipped_routine_steps)`` — a
    routine step referencing a non-attack ability (a heal, a reaction) has
    no opponent state to resolve against in profile mode and is skipped,
    named, rather than silently dropped."""
    action_by_id = {ability.id: ability for ability in statblock.compiled_actions}
    attack_steps: list[tuple[AttackPrimitive, int]] = []
    skipped: list[str] = []
    for step in routine:
        ability = action_by_id.get(step.ref)
        if ability is None:
            continue
        if isinstance(ability.step, AttackPrimitive):
            attack_steps.append((ability.step, step.count))
        else:
            skipped.append(ability.name)

    rows: list[DprRow] = []
    for ac_index, ac in enumerate(ac_sweep):
        rng = BatchRNG(substream_seed(seed, ac_index))
        total = np.zeros(iterations, dtype=np.float64)
        for attack, count in attack_steps:
            for _ in range(count):
                total += _roll_attack_damage(rng, iterations, attack.to_hit, ac, attack.damage)
        rows.append(DprRow(ac=ac, summary=_summarize(total)))
    return rows, skipped


@dataclass(frozen=True, slots=True)
class PcProfile:
    name: str
    id: str
    ac: int
    hp_max: int
    hit_tables: tuple[HitTable, ...]
    dpr: tuple[DprRow, ...]
    skipped_routine_steps: tuple[str, ...]
    be_hit: tuple[BeHitRow, ...]
    survivability: tuple[SurvivabilityRow, ...]
    warnings: tuple[str, ...]


def build_pc_profile(
    statblock: CompiledStatblock,
    block: dict[str, Any],
    *,
    ac_sweep: list[int],
    attack_bonus_sweep: list[int],
    iterations: int,
    seed: int,
) -> PcProfile:
    """Assemble the full profile result for one compiled statblock.

    ``block`` (the raw fence mapping) is accepted for call-site compatibility
    with :func:`load_compiled_statblock`'s return shape but no longer read
    here: routine resolution now reads only ``statblock.routine``, which
    ``compile_statblock`` already merges from a parsed Multiattack or an
    authored ``sim.routine`` block (issue #59) — the raw-fence re-read this
    function used to fall back to is gone.
    """
    # Priority: 1) statblock.routine (Multiattack or sim.routine, merged by
    # compile_statblock). 2) one use of every attack action, so a statblock
    # with neither still profiles something instead of an all-zero DPR table.
    routine = list(statblock.routine) or [
        RoutineStepPrimitive(ref=ability.id, count=1)
        for ability in statblock.compiled_actions
        if isinstance(ability.step, AttackPrimitive)
    ]
    dpr_rows, skipped = dpr_distribution(
        statblock, routine, ac_sweep, iterations=iterations, seed=seed
    )

    warnings = list(statblock.warnings)
    if not routine:
        warnings.append(
            "no routine could be resolved (no Multiattack, no sim.routine.action, "
            "no attack actions) — the damage-per-round distribution is all zero"
        )

    return PcProfile(
        name=statblock.name,
        id=statblock.id,
        ac=statblock.ac,
        hp_max=statblock.hp,
        hit_tables=tuple(hit_tables(statblock, ac_sweep)),
        dpr=tuple(dpr_rows),
        skipped_routine_steps=tuple(skipped),
        be_hit=tuple(be_hit_table(statblock.ac, attack_bonus_sweep)),
        survivability=tuple(hits_survivable(statblock.hp, statblock.ac, attack_bonus_sweep)),
        warnings=tuple(warnings),
    )
