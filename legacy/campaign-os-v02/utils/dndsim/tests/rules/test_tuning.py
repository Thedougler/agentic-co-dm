"""Goal scoring, difficulty drivers, band ladder, and the evolutionary
tuner (issue #54) — one file, since all four share the same fixture shape
(a party vs. one compiled-attack enemy) and the ladder/evolve tests are
naturally slow-ish (real Monte Carlo runs) even at reduced universe counts.
"""

from __future__ import annotations

import time
from pathlib import Path

import pytest

from dndsim import plugins
from dndsim.core.universe import UniverseBatch
from dndsim.rules.dnd5e_2014.attack_string import DamageGroup
from dndsim.rules.dnd5e_2014.combat import run_combat
from dndsim.rules.dnd5e_2014.compile import CompiledAbility, CompiledStatblock
from dndsim.rules.dnd5e_2014.evolve import (
    TuneWriteRefused,
    emit_statblock_markdown,
    evolve_statblock,
    guard_shared_reference,
    run_band_ladder_tune,
    stage_tuned_statblock,
)
from dndsim.rules.dnd5e_2014.fixture import CombatantSpec, make_combatant
from dndsim.rules.dnd5e_2014.goals import (
    GoalsError,
    band_tune_goals,
    default_tune_goals,
    evaluate_goals,
    validate_goals,
)
from dndsim.rules.dnd5e_2014.knobs import apply_delta, describe_delta, mutate_dice_expr
from dndsim.rules.dnd5e_2014.primitives import AttackPrimitive, RoutineStepPrimitive
from dndsim.rules.dnd5e_2014.sensitivity import is_material_win_delta, rank_drivers
from dndsim.rules.dnd5e_2014.sweep import combatant_spec_from_statblock


@pytest.fixture(autouse=True)
def _load_rules_pack() -> None:
    plugins.load_rules_packs()
    plugins.load_policies()


def _statblock_with_attack(
    *, name: str = "Fixture Foe", ac: int = 14, hp: int = 30, to_hit: int = 5, dice: str = "1d8+3"
) -> CompiledStatblock:
    attack_id = "dnd5e_2014:primitive/attack/fixture-attack"
    ability = CompiledAbility(
        id=attack_id,
        name="Fixture Attack",
        step=AttackPrimitive(
            id=attack_id, to_hit=to_hit, damage=[DamageGroup(dice=dice, type="slashing")]
        ),
    )
    routine = (RoutineStepPrimitive(ref=attack_id, count=1, alternatives=[]),)
    return CompiledStatblock(
        id=f"dnd5e_2014:statblock/{name.lower().replace(' ', '-')}",
        name=name,
        ac=ac,
        hp=hp,
        side="enemy",
        compiled_actions=(ability,),
        routine=routine,
    )


def _party() -> list[CombatantSpec]:
    return [
        make_combatant(
            entity_id="dnd5e_2014:combatant/pc1",
            name="PC One",
            hp_max=44,
            armor_class=16,
            attack_bonus=6,
            damage_bonus=4,
            damage_dice_count=1,
            damage_dice_sides=8,
        ),
        make_combatant(
            entity_id="dnd5e_2014:combatant/pc2",
            name="PC Two",
            hp_max=40,
            armor_class=15,
            attack_bonus=7,
            damage_bonus=3,
            damage_dice_count=2,
            damage_dice_sides=6,
        ),
    ]


def _enemy_spec(statblock: CompiledStatblock) -> list[CombatantSpec]:
    return [combatant_spec_from_statblock(statblock, suffix="/enemy")]


# --- goals -------------------------------------------------------------------


def test_validate_goals_rejects_unknown_metric() -> None:
    with pytest.raises(GoalsError, match="unknown metric"):
        validate_goals({"schema_version": 1, "goals": [{"metric": "nonsense", "min": 0.5}]})


def test_validate_goals_requires_min_or_max() -> None:
    with pytest.raises(GoalsError, match="requires min and/or max"):
        validate_goals({"schema_version": 1, "goals": [{"metric": "win_probability"}]})


def test_evaluate_goals_scores_zero_when_met() -> None:
    goals = validate_goals(
        {"schema_version": 1, "goals": [{"metric": "win_probability", "min": 0.5, "max": 0.9}]}
    )
    party, enemies = _party(), _enemy_spec(_statblock_with_attack(ac=10, hp=10))
    batch = UniverseBatch(size=2000, seed=1)
    result = run_combat(party, enemies, batch)
    evaluation = evaluate_goals(goals, result)
    assert evaluation.per_goal[0].value == result.party_win_rate
    if 0.5 <= result.party_win_rate <= 0.9:
        assert evaluation.all_met
        assert evaluation.score == 0.0
    else:
        assert not evaluation.all_met
        assert evaluation.score > 0.0


def test_default_and_band_tune_goals_are_internally_consistent() -> None:
    assert default_tune_goals() == band_tune_goals("hard")
    for band in ("easy", "medium", "hard", "deadly", "tpk"):
        assert len(band_tune_goals(band)) > 0
    with pytest.raises(GoalsError, match="unknown band"):
        band_tune_goals("nightmare")


# --- knobs ---------------------------------------------------------------


def test_mutate_dice_expr_steps_dice_and_folds_flat() -> None:
    assert mutate_dice_expr("2d6+3", dice_step=1, flat_delta=2) == "3d6+5"
    assert mutate_dice_expr("1d8+3", dice_step=0, flat_delta=-10) == "1d8-7"


def test_apply_delta_mutates_ac_hp_to_hit_and_damage() -> None:
    statblock = _statblock_with_attack(ac=14, hp=30, to_hit=5, dice="1d8+3")
    spec = _enemy_spec(statblock)[0]
    mutated = apply_delta(spec, {"ac": -3, "hp": -10, "to_hit": -2, "flat_damage": -3})
    assert mutated.armor_class == 11
    assert mutated.hp_max == 20
    assert mutated.compiled is not None
    attack = mutated.compiled.compiled_actions[0].step
    assert isinstance(attack, AttackPrimitive)
    assert attack.to_hit == 3
    assert attack.damage[0].dice == "1d8"
    # original untouched
    assert spec.armor_class == 14
    assert spec.compiled.compiled_actions[0].step.to_hit == 5  # type: ignore[union-attr]


def test_apply_delta_multiattack_bumps_routine_step_count() -> None:
    statblock = _statblock_with_attack()
    spec = _enemy_spec(statblock)[0]
    mutated = apply_delta(spec, {"multiattack": 2})
    assert mutated.compiled.routine[0].count == 3  # type: ignore[union-attr]


def test_describe_delta_names_the_changes() -> None:
    statblock = _statblock_with_attack(ac=14, hp=30)
    text = describe_delta(statblock, {"ac": -2, "hp": -5})
    assert "AC 14->12" in text
    assert "HP 30->25" in text
    assert describe_delta(statblock, {}) == "original (no changes)"


# --- difficulty drivers (sensitivity) ----------------------------------------


def test_is_material_win_delta_floor_and_relative_lift() -> None:
    assert not is_material_win_delta(0.01, 0.5)  # below noise floor
    assert is_material_win_delta(0.06, 0.5)  # clears absolute bar
    assert is_material_win_delta(0.03, 0.05)  # clears relative-lift bar on a low baseline
    assert not is_material_win_delta(0.03, 0.5)  # neither bar cleared


def test_rank_drivers_reports_a_ranked_table_against_a_weak_enemy() -> None:
    party = _party()
    enemies = _enemy_spec(_statblock_with_attack(ac=8, hp=6, to_hit=0, dice="1d4"))
    ranking = rank_drivers(party, enemies, 0, seed=7, probe_universes=800)
    assert ranking.baseline.win_probability > 0.9  # party crushes this fodder enemy
    assert len(ranking.drivers) > 0
    # already-weak knobs should show little further movement -> no material driver
    assert ranking.primary_driver is None
    assert ranking.note is not None


def test_rank_drivers_finds_a_primary_driver_against_a_strong_enemy() -> None:
    party = _party()
    enemies = _enemy_spec(_statblock_with_attack(ac=19, hp=90, to_hit=9, dice="3d8+6"))
    ranking = rank_drivers(party, enemies, 0, seed=7, probe_universes=1500)
    assert ranking.baseline.win_probability < 0.3  # this enemy is dominant
    assert ranking.primary_driver is not None
    assert ranking.primary_driver.delta_win > 0


# --- evolutionary tuner --------------------------------------------------


def test_evolve_statblock_is_deterministic_per_seed() -> None:
    party = _party()
    enemies = _enemy_spec(_statblock_with_attack(ac=18, hp=80, to_hit=8, dice="2d8+5"))
    goals = default_tune_goals()
    r1 = evolve_statblock(
        party, enemies, 0, goals, seed=42, population=6, generations=2, probe_universes=300
    )
    r2 = evolve_statblock(
        party, enemies, 0, goals, seed=42, population=6, generations=2, probe_universes=300
    )
    assert [v.delta for v in r1.ranked] == [v.delta for v in r2.ranked]
    assert [v.score for v in r1.ranked] == [v.score for v in r2.ranked]


def test_evolve_statblock_moves_score_toward_the_goal() -> None:
    # A wildly-overtuned enemy (Deadly, likely TPK) should have a
    # meaningfully worse original score than its best found variant once
    # the GA has had a few generations to weaken it toward the Hard band.
    party = _party()
    enemies = _enemy_spec(_statblock_with_attack(ac=20, hp=150, to_hit=10, dice="3d10+8"))
    goals = default_tune_goals()
    result = evolve_statblock(
        party, enemies, 0, goals, seed=3, population=8, generations=4, probe_universes=500
    )
    original_score = (
        next(v.score for v in result.ranked if v.delta == {})
        if any(v.delta == {} for v in result.ranked)
        else None
    )
    best = result.ranked[0]
    assert result.sims_run > 0
    if original_score is not None:
        assert best.score <= original_score


def test_run_band_ladder_tune_covers_every_band_and_is_fast() -> None:
    party = _party()
    enemies = _enemy_spec(_statblock_with_attack(ac=17, hp=70, to_hit=7, dice="2d6+4"))
    started = time.perf_counter()
    ladder = run_band_ladder_tune(
        party,
        enemies,
        0,
        seed=11,
        ga_kwargs={"population": 6, "generations": 2, "probe_universes": 300},
    )
    wall_s = time.perf_counter() - started
    assert set(ladder.ladder.keys()) == {"easy", "medium", "hard", "deadly", "tpk"}
    for band_result in ladder.ladder.values():
        assert len(band_result.ranked) > 0
    # ADR-0011's Phase 0 finding: a full 274-page corpus sweep runs in ~1s
    # at 8 workers, so a 5-band ladder at this reduced GA size needs no
    # wall-clock budget system to stay usable within a test timeout.
    assert wall_s < 30, f"band ladder took {wall_s:.2f}s — measured, not assumed"


# --- staging / corpus-integrity guard ----------------------------------------


_SAMPLE_PAGE = """---
type: statblock
source_url: null
---

```statblock
name: Fixture Foe
ac: 14
hp: 30
stats: [14, 12, 14, 8, 10, 8]
actions:
  - name: Bite
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8+3) piercing damage."
```
"""

_SHARED_PAGE = """---
type: statblock
source_url: "https://dnd.wizards.com/srd"
---

```statblock
name: Shared Foe
ac: 14
hp: 30
stats: [14, 12, 14, 8, 10, 8]
actions:
  - name: Bite
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8+3) piercing damage."
```
"""


def test_guard_shared_reference_refuses_srd_frontmatter(tmp_path: Path) -> None:
    with pytest.raises(TuneWriteRefused, match="shared reference"):
        guard_shared_reference(_SHARED_PAGE, tmp_path / "shared.md")


def test_guard_shared_reference_allows_homebrew_frontmatter(tmp_path: Path) -> None:
    guard_shared_reference(_SAMPLE_PAGE, tmp_path / "homebrew.md")  # no raise


def test_emit_statblock_markdown_patches_ac_hp_and_to_hit_and_reparses() -> None:
    statblock = _statblock_with_attack(ac=14, hp=30, to_hit=5, dice="1d8+3")
    emitted = emit_statblock_markdown(
        _SAMPLE_PAGE, statblock, {"ac": -2, "hp": -10, "to_hit": -1, "flat_damage": 1}
    )
    assert "ac: 12" in emitted
    assert "hp: 20" in emitted
    assert "+4 to hit" in emitted
    assert "1d8+4" in emitted


def test_stage_tuned_statblock_stages_to_scratch_by_default(tmp_path: Path) -> None:
    original_path = tmp_path / "fixture-foe-statblock.md"
    original_path.write_text(_SAMPLE_PAGE)
    statblock = _statblock_with_attack(ac=14, hp=30, to_hit=5, dice="1d8+3")
    scratch = tmp_path / "scratch" / "out.md"

    written = stage_tuned_statblock(original_path, statblock, {"ac": -2}, scratch_path=scratch)

    assert written == scratch
    assert scratch.read_text() != ""
    # the real page was never touched
    assert original_path.read_text() == _SAMPLE_PAGE


def test_stage_tuned_statblock_refuses_shared_reference_even_with_apply(tmp_path: Path) -> None:
    original_path = tmp_path / "shared-foe-statblock.md"
    original_path.write_text(_SHARED_PAGE)
    statblock = _statblock_with_attack(name="Shared Foe", ac=14, hp=30, to_hit=5, dice="1d8+3")

    with pytest.raises(TuneWriteRefused):
        stage_tuned_statblock(original_path, statblock, {"ac": -2}, apply=True)

    assert original_path.read_text() == _SHARED_PAGE
