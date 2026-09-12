from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

from dndsim import plugins
from dndsim.cli import app
from dndsim.core.universe import UniverseBatch
from dndsim.report import render_combat_report
from dndsim.rules.dnd5e_2014.combat import run_combat
from dndsim.rules.dnd5e_2014.side_spec import resolve_side

runner = CliRunner()

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"


# Every test passes --no-audit-log: sim-combat's audit line is ON by
# default (issue #50 acceptance criteria), but a test run must never write
# into the repo's real utils/dndsim/dndsim-audit.jsonl. Audit-log behavior
# itself is exercised separately below with an explicit tmp_path --audit-log.
NO_AUDIT = ["--no-audit-log"]


def test_sim_combat_prints_markdown_report() -> None:
    result = runner.invoke(app, ["sim-combat", "--seed", "1", "--universes", "500", *NO_AUDIT])
    assert result.exit_code == 0
    assert "# Combat simulation report" in result.stdout
    assert "**Seed**: 1" in result.stdout
    assert "dndsim v" in result.stdout


def test_sim_combat_defaults_to_the_2024_edition() -> None:
    """Issue #55: the default is 2024, not 2014 — this repo's live content
    (exhaustion_level 0 everywhere) simulates identically either way, so
    the default is only observable in the report's own **Edition** line."""
    result = runner.invoke(app, ["sim-combat", "--seed", "1", "--universes", "200", *NO_AUDIT])
    assert result.exit_code == 0
    assert "**Edition**: dnd5e_2024" in result.stdout


def test_sim_combat_accepts_an_explicit_2014_edition() -> None:
    result = runner.invoke(
        app,
        ["sim-combat", "--seed", "1", "--universes", "200", "--edition", "dnd5e_2014", *NO_AUDIT],
    )
    assert result.exit_code == 0
    assert "**Edition**: dnd5e_2014" in result.stdout


def test_sim_combat_rejects_an_unknown_edition() -> None:
    result = runner.invoke(
        app,
        ["sim-combat", "--seed", "1", "--universes", "200", "--edition", "dnd5e_1977", *NO_AUDIT],
    )
    assert result.exit_code == 1
    assert "unknown edition" in result.output


def test_sim_combat_same_seed_is_identical() -> None:
    args = ["sim-combat", "--seed", "42", "--universes", "1000", *NO_AUDIT]
    first = runner.invoke(app, args)
    second = runner.invoke(app, args)
    assert first.stdout == second.stdout


def test_sim_combat_out_option_writes_file(tmp_path) -> None:  # type: ignore[no-untyped-def]
    out_path = tmp_path / "report.md"
    result = runner.invoke(
        app,
        ["sim-combat", "--seed", "1", "--universes", "200", "--out", str(out_path), *NO_AUDIT],
    )
    assert result.exit_code == 0
    assert out_path.exists()
    assert "# Combat simulation report" in out_path.read_text()


def test_sim_combat_no_seed_generates_and_reports_one() -> None:
    result = runner.invoke(app, ["sim-combat", "--universes", "200", *NO_AUDIT])
    assert result.exit_code == 0
    assert "**Seed generated**:" in result.stdout


def test_sim_combat_explicit_seed_does_not_report_generated() -> None:
    result = runner.invoke(app, ["sim-combat", "--seed", "1", "--universes", "200", *NO_AUDIT])
    assert result.exit_code == 0
    assert "**Seed generated**:" not in result.stdout


def test_sim_combat_adaptive_stops_within_floor_and_cap() -> None:
    result = runner.invoke(
        app,
        [
            "sim-combat",
            "--seed",
            "3",
            "--adaptive",
            "--adaptive-chunk",
            "200",
            "--adaptive-floor",
            "200",
            "--adaptive-threshold",
            "0.05",
            "--adaptive-cap",
            "5000",
            *NO_AUDIT,
        ],
    )
    assert result.exit_code == 0
    assert "adaptive" in result.stdout.lower()
    assert "Trials run" in result.stdout
    assert "95% CI" in result.stdout


def test_sim_combat_writes_one_audit_line_by_default(tmp_path) -> None:  # type: ignore[no-untyped-def]
    log_path = tmp_path / "audit.jsonl"
    result = runner.invoke(
        app,
        [
            "sim-combat",
            "--seed",
            "1",
            "--universes",
            "200",
            "--audit-log",
            str(log_path),
        ],
    )
    assert result.exit_code == 0
    assert log_path.exists()
    lines = log_path.read_text().splitlines()
    assert len(lines) == 1
    payload = json.loads(lines[0])
    assert payload["seed"] == 1
    assert payload["engineVersion"]
    assert payload["resultDigest"]


def test_sim_combat_no_audit_log_suppresses_the_line(tmp_path) -> None:  # type: ignore[no-untyped-def]
    log_path = tmp_path / "audit.jsonl"
    result = runner.invoke(
        app,
        [
            "sim-combat",
            "--seed",
            "1",
            "--universes",
            "200",
            "--audit-log",
            str(log_path),
            "--no-audit-log",
        ],
    )
    assert result.exit_code == 0
    assert not log_path.exists()


# --- side-spec grammar (issue #67) --------------------------------------------


def test_sim_combat_bare_literal_paths_run_a_real_matchup() -> None:
    x = FIXTURES_DIR / "dravosi-deckhand-statblock.md"
    y = FIXTURES_DIR / "fixture-grung-elite-warrior.md"
    result = runner.invoke(
        app,
        ["sim-combat", str(x), str(y), "--seed", "1", "--universes", "200", *NO_AUDIT],
    )
    assert result.exit_code == 0, result.stdout
    assert "Dravosi Deckhand" in result.stdout
    assert "Grung Elite Warrior" in result.stdout


def test_sim_combat_count_suffix_repeats_a_combatant() -> None:
    x = FIXTURES_DIR / "dravosi-deckhand-statblock.md"
    y = FIXTURES_DIR / "fixture-grung-elite-warrior.md"
    result = runner.invoke(
        app,
        [
            "sim-combat",
            f"{x}:2",
            str(y),
            "--seed",
            "1",
            "--universes",
            "200",
            *NO_AUDIT,
        ],
    )
    assert result.exit_code == 0, result.stdout
    # Two copies of the same PC side by name — the report's per-PC section
    # lists each combatant once, so the repeated name appears twice.
    assert result.stdout.count("Dravosi Deckhand") >= 2


def test_sim_combat_comma_list_builds_a_heterogeneous_roster() -> None:
    a = FIXTURES_DIR / "dravosi-deckhand-statblock.md"
    b = FIXTURES_DIR / "fixture-otar-the-foul.md"
    y = FIXTURES_DIR / "fixture-grung-elite-warrior.md"
    result = runner.invoke(
        app,
        [
            "sim-combat",
            f"{a},{b}",
            str(y),
            "--seed",
            "1",
            "--universes",
            "200",
            *NO_AUDIT,
        ],
    )
    assert result.exit_code == 0, result.stdout
    assert "Dravosi Deckhand" in result.stdout
    assert "Otar the Foul" in result.stdout


def test_sim_combat_party_keyword_expands_party_glob(tmp_path: Path) -> None:
    party_dir = tmp_path / "party"
    party_dir.mkdir()
    pc_source = FIXTURES_DIR / "dravosi-deckhand-statblock.md"
    (party_dir / "pc1-sheet.md").write_text(pc_source.read_text())
    y = FIXTURES_DIR / "fixture-grung-elite-warrior.md"
    result = runner.invoke(
        app,
        [
            "sim-combat",
            "party",
            str(y),
            "--party-glob",
            str(party_dir / "*-sheet.md"),
            "--seed",
            "1",
            "--universes",
            "200",
            *NO_AUDIT,
        ],
    )
    assert result.exit_code == 0, result.stdout
    assert "Dravosi Deckhand" in result.stdout


def test_sim_combat_party_keyword_no_match_is_a_loud_error(tmp_path: Path) -> None:
    y = FIXTURES_DIR / "fixture-grung-elite-warrior.md"
    result = runner.invoke(
        app,
        [
            "sim-combat",
            "party",
            str(y),
            "--party-glob",
            str(tmp_path / "nothing-matches-*.md"),
            *NO_AUDIT,
        ],
    )
    assert result.exit_code != 0
    assert result.stderr is not None
    assert "matched no files" in result.stderr


def test_sim_combat_unresolvable_slug_names_the_search_and_never_fuzzy_matches() -> None:
    y = FIXTURES_DIR / "fixture-grung-elite-warrior.md"
    result = runner.invoke(
        app,
        ["sim-combat", "zzz-nonexistent-slug-issue67", str(y), *NO_AUDIT],
    )
    assert result.exit_code != 0
    assert result.stderr is not None
    assert 'no file matching "zzz-nonexistent-slug-issue67"' in result.stderr


def test_sim_combat_only_x_given_is_an_error() -> None:
    x = FIXTURES_DIR / "dravosi-deckhand-statblock.md"
    result = runner.invoke(app, ["sim-combat", str(x), *NO_AUDIT])
    assert result.exit_code != 0
    assert result.stderr is not None
    assert "both <X> and <Y>" in result.stderr


def test_sim_combat_no_arguments_still_runs_the_bundled_fixture() -> None:
    # The walking-skeleton fixture stays reachable as the explicit
    # no-argument default (issue #67 acceptance criteria) — this is the
    # same behavior test_sim_combat_prints_markdown_report above already
    # exercises; restated here to anchor it against the side-spec grammar
    # tests below it.
    result = runner.invoke(app, ["sim-combat", "--seed", "1", "--universes", "200", *NO_AUDIT])
    assert result.exit_code == 0
    assert "Perrin" in result.stdout


def test_sim_combat_cli_report_matches_run_combat_api_at_same_seed() -> None:
    """A CLI-driven matchup and the same matchup driven through
    ``run_combat()`` directly must agree bit-for-bit at one seed (issue #67
    acceptance criteria) — the same parity guarantee every other verb
    already has to the Python API, now extended to arbitrary combatants
    instead of only the hardcoded fixture."""
    x = FIXTURES_DIR / "dravosi-deckhand-statblock.md"
    y = FIXTURES_DIR / "fixture-grung-elite-warrior.md"
    seed = 7
    universes = 300

    cli_result = runner.invoke(
        app,
        [
            "sim-combat",
            str(x),
            str(y),
            "--seed",
            str(seed),
            "--universes",
            str(universes),
            *NO_AUDIT,
        ],
    )
    assert cli_result.exit_code == 0, cli_result.stdout

    plugins.load_rules_packs()
    plugins.load_policies()
    party = resolve_side(str(x), role="party")
    enemies = resolve_side(str(y), role="enemy")
    batch = UniverseBatch(size=universes, seed=seed)
    api_result = run_combat(
        list(party.combatants),
        list(enemies.combatants),
        batch,
        round_cap=20,
        policy_id="dndsim:policy/greedy",
    )
    api_report = (
        render_combat_report(api_result)
        + "**Policy**: dndsim:policy/greedy\n"
        + "**Edition**: dnd5e_2024\n"
    )

    assert cli_result.stdout.strip() == api_report.strip()
