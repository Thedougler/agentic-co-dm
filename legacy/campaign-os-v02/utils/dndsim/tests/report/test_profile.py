"""``dndsim.profile`` — pc-profile mode (issue #51)."""

from __future__ import annotations

from pathlib import Path

import pytest

from dndsim.profile import (
    ProfileError,
    build_pc_profile,
    hit_chance,
    load_compiled_statblock,
)
from dndsim.rules.dnd5e_2014.statblock import StatblockParseError

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"

# A minimal party-side PC sheet with no Multiattack, using the real
# `sim.routine.action` slot (README's documented shape — mirrors
# perrin-black-jaw-sheet.md's `sim: { routine: { action: [longsword] } }`)
# so compile_statblock's sim.routine wiring (issue #59) is exercised by a
# fixture rather than only against a live vault page.
PC_FIXTURE = """\
```statblock
name: Fixture Duelist
ac: 16
hp: 30
stats: [14, 16, 12, 10, 10, 10]
actions:
  - name: "Rapier"
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft. Hit: 7 (1d8 + 3) piercing damage."
    sim: { id: rapier }
sim:
  side: party
  routine:
    action: [rapier]
```
"""

NO_ATTACK_FIXTURE = """\
```statblock
name: Fixture Healer
ac: 12
hp: 20
stats: [10, 10, 10, 10, 14, 10]
```
"""


def test_hit_chance_matches_the_golden_math() -> None:
    # +7 vs AC 15 = 0.65 — same golden figure the reference engine's own
    # test suite pins (report.mjs's own doc comment references this exact
    # case).
    p_hit, _p_crit = hit_chance(7, 15)
    assert p_hit == pytest.approx(0.65)


def test_hit_chance_nat_1_always_misses_nat_20_always_hits() -> None:
    # AC so far out of reach that only a natural 20 can hit — pHit collapses
    # to exactly the crit chance (1/20).
    p_hit, p_crit = hit_chance(-10, 100)
    assert p_hit == pytest.approx(0.05)
    assert p_crit == pytest.approx(0.05)


def test_load_compiled_statblock_no_fence_raises_profile_error() -> None:
    with pytest.raises(ProfileError):
        load_compiled_statblock("# No fence here\n", "(test)")


def test_load_compiled_statblock_bad_yaml_raises_statblock_parse_error() -> None:
    with pytest.raises(StatblockParseError):
        load_compiled_statblock("```statblock\nname: [unterminated\n```\n", "(test)")


def test_build_pc_profile_from_multiattack_fixture() -> None:
    text = (FIXTURES_DIR / "fixture-otar-the-foul.md").read_text()
    statblock, block = load_compiled_statblock(text, "fixture-otar-the-foul.md")
    profile = build_pc_profile(
        statblock,
        block,
        ac_sweep=[10, 15, 20],
        attack_bonus_sweep=[4, 8],
        iterations=500,
        seed=1,
    )
    assert profile.name == "Otar the Foul"
    assert profile.ac == 17
    assert profile.hp_max == 241
    # Bite, Claw, Tongue Lash all parse as attack actions.
    names = {t.name for t in profile.hit_tables}
    assert {"Bite", "Claw", "Tongue Lash"} <= names
    # The routine (Bite + Claw + Tongue Lash, per Multiattack's desc) drove
    # a non-zero DPR at every swept AC.
    assert all(row.summary.mean > 0 for row in profile.dpr)
    assert not profile.skipped_routine_steps


def test_build_pc_profile_uses_sim_routine_fallback_when_no_multiattack() -> None:
    statblock, block = load_compiled_statblock(PC_FIXTURE, "(pc fixture)")
    # No Multiattack on this sheet — compile_statblock wires the authored
    # sim.routine.action slot into CompiledStatblock.routine directly
    # (issue #59), so profile.py no longer needs its own raw-fence fallback.
    assert [step.ref for step in statblock.routine] == [
        next(a.id for a in statblock.compiled_actions if a.name == "Rapier")
    ]
    profile = build_pc_profile(
        statblock,
        block,
        ac_sweep=[12, 16],
        attack_bonus_sweep=[3],
        iterations=300,
        seed=2,
    )
    assert all(row.summary.mean > 0 for row in profile.dpr)


def test_build_pc_profile_no_attacks_reports_zero_dpr_with_a_warning() -> None:
    statblock, block = load_compiled_statblock(NO_ATTACK_FIXTURE, "(no-attack fixture)")
    profile = build_pc_profile(
        statblock,
        block,
        ac_sweep=[12],
        attack_bonus_sweep=[3],
        iterations=100,
        seed=3,
    )
    assert profile.hit_tables == ()
    assert all(row.summary.mean == 0 for row in profile.dpr)
    assert any("no routine could be resolved" in w for w in profile.warnings)


def test_dpr_distribution_is_deterministic_for_a_given_seed() -> None:
    text = (FIXTURES_DIR / "fixture-otar-the-foul.md").read_text()
    statblock, block = load_compiled_statblock(text, "fixture-otar-the-foul.md")
    first = build_pc_profile(
        statblock, block, ac_sweep=[15], attack_bonus_sweep=[5], iterations=200, seed=9
    )
    second = build_pc_profile(
        statblock, block, ac_sweep=[15], attack_bonus_sweep=[5], iterations=200, seed=9
    )
    assert first.dpr[0].summary.mean == second.dpr[0].summary.mean
    assert first.dpr[0].summary.p95 == second.dpr[0].summary.p95
