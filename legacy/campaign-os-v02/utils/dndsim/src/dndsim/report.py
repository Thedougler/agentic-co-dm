"""Markdown report rendering.

Every report names the engine version and the seed that produced it (issue
#39 acceptance criteria) so a figure quoted anywhere is reproducible.

Every documented section (issue #51) is rendered under its own heading,
using whatever this engine's own ``CombatResult``/``PcProfile`` already
carry. Since issue #59 generalized
``run_combat`` (``rules/dnd5e_2014/combat.py``) into the real party-vs-party
loop, ``CombatResult`` carries per-PC, per-combatant, positional, and
P(≥k down)/rounds-percentile detail for any ordinary run — the sections
below render that data directly. A hand-built ``CombatResult`` with empty
``pc_outcomes``/``combatant_outputs`` tuples (a unit test, or a future run
mode that genuinely can't compute them) still renders an explicit "not
available this run" line rather than an empty table, and collects every
such gap into one warnings block — the engine's own documented behavior for
unmodeled content (issue #51 acceptance criteria: "Unmodeled-content
warnings appear in the report").
"""

from __future__ import annotations

from dndsim import __version__
from dndsim.difficulty import DifficultyInputs, rate_difficulty
from dndsim.profile import PcProfile
from dndsim.rules.dnd5e_2014.combat import CombatResult


def _pct(p: float) -> str:
    return f"{p * 100:.1f}%"


def _num(v: float, digits: int = 2) -> str:
    return f"{v:.{digits}f}"


def _mc_stderr(p: float, n: int) -> float | None:
    """Standard error of a sampled proportion — ``None`` for an empty run."""
    if n <= 0:
        return None
    return float((p * (1 - p) / n) ** 0.5)


def render_combat_report(result: CombatResult, *, policy: str | None = None) -> str:
    """Full encounter report — outcome distribution, stalemate rate,
    rounds, party outcomes, per-PC/per-combatant/positional sections, and
    the Effective Difficulty Rating with the rule that selected it. Any
    section whose source data is empty on ``result`` renders an explicit
    "not available this run" line instead, collected into one warnings
    block (see module docstring).
    """
    from dndsim.core.stats import wilson_interval

    party_successes = round(result.party_win_rate * result.universes)
    win_ci = wilson_interval(party_successes, result.universes)
    stderr = _mc_stderr(result.party_win_rate, result.universes)

    difficulty = rate_difficulty(
        DifficultyInputs(
            win_probability=result.party_win_rate,
            any_down_probability=result.any_down_probability,
            tpk_probability=result.tpk_probability,
            mean_party_hp_loss=result.mean_party_hp_loss,
        )
    )

    gaps: list[str] = []

    lines = [
        "# Combat simulation report",
        "",
        f"- **Engine**: dndsim v{__version__}",
        f"- **Seed**: {result.seed}",
        f"- **Universes**: {result.universes:,}",
        f"- **Round cap**: {result.rounds_cap}",
        "",
        f"## {result.party_name} vs. {result.enemy_name}",
        "",
        "## Outcome distribution",
        "",
        f"- {result.party_name} wins: **{_pct(result.party_win_rate)}**"
        + (
            f" (95% CI {_pct(win_ci.lo)}–{_pct(win_ci.hi)}, MC stderr ±{_pct(stderr)})"
            if win_ci.lo is not None and win_ci.hi is not None and stderr is not None
            else ""
        ),
        f"- {result.enemy_name} wins: **{_pct(result.enemy_win_rate)}**",
        f"- Stalemate rate (round cap hit, counted as a loss): {_pct(result.draw_rate)}",
        f"- Rounds: mean {_num(result.mean_rounds)} "
        f"(median {_num(result.median_rounds)}, p95 {_num(result.p95_rounds)})",
        "",
        "## Party outcomes",
        "",
        f"- P(TPK): **{_pct(result.tpk_probability)}**",
        f"- P(≥1 down): **{_pct(result.any_down_probability)}**",
    ]
    if len(result.at_least_k_down) > 1:
        at_least = ", ".join(
            f"≥{k} down: {_pct(p)}" for k, p in enumerate(result.at_least_k_down, start=1)
        )
        lines.append(f"- {at_least}")
    lines.append("")

    lines.append("## Per-PC")
    lines.append("")
    if result.pc_outcomes:
        lines.append("| PC | HP remaining (p5/p50/p95) | P(down) |")
        lines.append("|---|---|---|")
        for pc in result.pc_outcomes:
            lines.append(
                f"| {pc.name} | {_pct(pc.hp_remaining_pct_p5)}/{_pct(pc.hp_remaining_pct_p50)}/"
                f"{_pct(pc.hp_remaining_pct_p95)} | {_pct(pc.down_probability)} |"
            )
    else:
        lines.append("Not available this run (see Data gaps below).")
        gaps.append("Per-PC HP-remaining percentiles — this result carries no pc_outcomes.")
    lines.append("")

    lines.append("## Per-combatant output")
    lines.append("")
    if result.combatant_outputs:
        lines.append(
            "| Combatant | Side | Mean damage dealt | Mean reactions spent | Mean conc. breaks |"
        )
        lines.append("|---|---|---|---|---|")
        for c in result.combatant_outputs:
            lines.append(
                f"| {c.name} | {c.side} | {_num(c.mean_damage_dealt)} | "
                f"{_num(c.mean_reactions_spent)} | {_num(c.mean_concentration_breaks)} |"
            )
    else:
        lines.append("Not available this run (see Data gaps below).")
        gaps.append(
            "Per-combatant damage dealt / resources spent / concentration breaks — this result "
            "carries no combatant_outputs."
        )
    lines.append("")

    lines.append("## Positional figures")
    lines.append("")
    if result.combatant_outputs:
        lines.append("| Combatant | Mean turns w/o target | Mean opportunity attacks |")
        lines.append("|---|---|---|")
        for c in result.combatant_outputs:
            no_target = _num(c.mean_turns_no_target)
            oa = _num(c.mean_opportunity_attacks)
            lines.append(f"| {c.name} | {no_target} | {oa} |")
    else:
        lines.append("Not available this run (see Data gaps below).")
        gaps.append(
            "Positional figures (mean turns without a reachable target, mean opportunity "
            "attacks) — this result carries no combatant_outputs."
        )
    lines.append("")

    lines.append(f"## Effective Difficulty Rating: **{difficulty.band}**")
    lines.append("")
    lines.append(f"Fired rule: {difficulty.rule}.")
    lines.append("")

    if gaps:
        lines.append("## Data gaps in this run")
        lines.append("")
        lines.extend(f"WARN {gap}" for gap in gaps)
        lines.append("")
    if policy is not None:
        lines.append(f"**Policy**: {policy}")
        lines.append("")
    return "\n".join(lines)


def render_pc_profile_report(
    profile: PcProfile,
    *,
    seed: int,
    iterations: int,
    loadout_name: str = "min (routine only, no resources)",
) -> str:
    """``profile`` verb report: closed-form hit tables, a sampled DPR
    distribution, closed-form chance-to-be-hit, and effective hit points
    (expected attacks survived).
    """
    lines = [
        f"# Combat profile — {profile.name}",
        "",
        f"dndsim v{__version__} | seed {seed} | {iterations} iterations/AC | "
        f"loadout: {loadout_name}",
        f"AC {profile.ac} | HP {profile.hp_max}",
        "",
        "## Hit chance vs AC (closed-form, exact)",
        "",
    ]
    for table in profile.hit_tables:
        lines.append(f"### {table.name} (+{table.to_hit} to hit)")
        lines.append("")
        lines.append(f"| Target AC | {' | '.join(str(r.ac) for r in table.rows)} |")
        lines.append(f"|---|{'|'.join('---' for _ in table.rows)}|")
        lines.append(f"| Hit % (incl. crit) | {' | '.join(_pct(r.p_hit) for r in table.rows)} |")
        lines.append(f"| Crit % | {' | '.join(_pct(r.p_crit) for r in table.rows)} |")
        lines.append("")
    if not profile.hit_tables:
        lines.append("_No attack actions to report._")
        lines.append("")

    lines.append("## Damage per round vs AC (Monte Carlo, routine)")
    lines.append("")
    lines.append("| AC | mean | stddev | min | p5 | p50 | p95 | max |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for row in profile.dpr:
        s = row.summary
        lines.append(
            f"| {row.ac} | {_num(s.mean)} | {_num(s.stddev)} | {_num(s.min, 0)} | {_num(s.p5, 0)} "
            f"| {_num(s.p50, 0)} | {_num(s.p95, 0)} | {_num(s.max, 0)} |"
        )
    if profile.skipped_routine_steps:
        lines.append("")
        lines.append(
            "Skipped non-attack routine steps (no opponent to resolve against in profile mode): "
            + ", ".join(profile.skipped_routine_steps)
            + "."
        )
    lines.append("")

    lines.append("## Chance to be hit vs incoming attack bonus (closed-form)")
    lines.append("")
    lines.append(f"| Attack bonus | {' | '.join(f'+{r.bonus}' for r in profile.be_hit)} |")
    lines.append(f"|---|{'|'.join('---' for _ in profile.be_hit)}|")
    lines.append(f"| Hit % | {' | '.join(_pct(r.p_hit) for r in profile.be_hit)} |")
    lines.append("")

    lines.append("## Effective hit points (expected attacks survived; crit ≈ +50% dice share)")
    lines.append("")
    dmg_cols = (
        [c.damage_per_hit for c in profile.survivability[0].columns]
        if profile.survivability
        else []
    )
    lines.append(f"| Attack bonus | {' | '.join(f'{d} dmg/hit' for d in dmg_cols)} |")
    lines.append(f"|---|{'|'.join('---' for _ in dmg_cols)}|")
    for surv_row in profile.survivability:
        lines.append(
            f"| +{surv_row.bonus} | "
            f"{' | '.join(_num(c.expected_attacks, 1) for c in surv_row.columns)} |"
        )
    lines.append("")

    if profile.warnings:
        lines.append("## Warnings")
        lines.append("")
        lines.extend(f"WARN {w}" for w in profile.warnings)
        lines.append("")

    return "\n".join(lines)
