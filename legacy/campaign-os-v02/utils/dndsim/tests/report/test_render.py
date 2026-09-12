"""``dndsim.report`` — markdown rendering (issue #51 report parity)."""

from __future__ import annotations

from pathlib import Path

from dndsim.profile import build_pc_profile, load_compiled_statblock
from dndsim.report import render_combat_report, render_pc_profile_report
from dndsim.rules.dnd5e_2014.combat import CombatResult

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"


def _result(**overrides: object) -> CombatResult:
    base: dict[str, object] = {
        "universes": 1000,
        "seed": 1,
        "rounds_cap": 20,
        "party_name": "Perrin",
        "enemy_name": "Grung Skirmisher",
        "party_win_rate": 0.7,
        "enemy_win_rate": 0.25,
        "draw_rate": 0.05,
        "mean_rounds": 4.2,
        "median_rounds": 4.0,
        "p95_rounds": 9.0,
        "any_down_probability": 0.1,
        "at_least_k_down": (0.1,),
        "tpk_probability": 0.25,
        "mean_party_hp_loss": 0.3,
        "pc_outcomes": (),
        "combatant_outputs": (),
    }
    base.update(overrides)
    return CombatResult(**base)  # type: ignore[arg-type]


def test_render_combat_report_carries_every_documented_section() -> None:
    report = render_combat_report(_result())
    for heading in (
        "# Combat simulation report",
        "## Outcome distribution",
        "## Party outcomes",
        "## Per-PC",
        "## Per-combatant output",
        "## Positional figures",
        "## Effective Difficulty Rating",
        "## Data gaps in this run",
    ):
        assert heading in report, heading


def test_render_combat_report_computes_wilson_ci_and_tpk() -> None:
    report = render_combat_report(_result(party_win_rate=0.7, enemy_win_rate=0.25, universes=1000))
    assert "95% CI" in report
    assert "MC stderr" in report
    assert "P(TPK): **25.0%**" in report


def test_render_combat_report_warns_about_gaps() -> None:
    report = render_combat_report(_result(pc_outcomes=(), combatant_outputs=()))
    assert "WARN" in report
    assert "Per-PC" in report


def test_render_combat_report_deadly_band_when_win_rate_is_low() -> None:
    report = render_combat_report(_result(party_win_rate=0.4, enemy_win_rate=0.55, draw_rate=0.05))
    assert "Effective Difficulty Rating: **Deadly**" in report
    assert "Fired rule: P(win) < 0.75" in report


def test_render_pc_profile_report_carries_every_documented_section() -> None:
    text = (FIXTURES_DIR / "fixture-otar-the-foul.md").read_text()
    statblock, block = load_compiled_statblock(text, "fixture-otar-the-foul.md")
    profile = build_pc_profile(
        statblock, block, ac_sweep=[10, 15], attack_bonus_sweep=[4, 8], iterations=200, seed=1
    )
    report = render_pc_profile_report(profile, seed=1, iterations=200)
    for heading in (
        "# Combat profile — Otar the Foul",
        "## Hit chance vs AC (closed-form, exact)",
        "## Damage per round vs AC (Monte Carlo, routine)",
        "## Chance to be hit vs incoming attack bonus (closed-form)",
        "## Effective hit points",
    ):
        assert heading in report, heading
