"""TDD for `wiki_cli.baseline` — the lint baseline as a suppression list
(ADR-0062). One test per law:

- the engine syncs a file's per-rule floor DOWN to `min(live, floor)`
  after a sweep, never up and never inventing new entries, and drops the
  floor for a file that has left the corpus
- `over_entries` names every (file, rule) pair above its floor and by how
  far; `check` counts them; `ratchet_token` names the command that lists
  them and marks a scoped verdict as scoped
- `partition` suppresses a pair's first `floor` warnings and shows the
  rest, never touching errors or advisory findings
- `seed`/`promote` write the floor from scratch / from current counts
- `report.render` carries the ratchet state as one header token and the
  suppression total as one trailing line
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import pytest
from typer.testing import CliRunner

from wiki_cli import baseline, cli
from wiki_cli.contracts import Finding, Severity, Tier
from wiki_cli.orchestrator import LintResult, RunStats
from wiki_cli.report import render

_FILE_A = "vault/npcs/barnaby-rook.md"
_FILE_B = "vault/locations/the-open-midchain.md"


@dataclass(frozen=True)
class _StubConfig:
    """Only what the `baseline` commands read off a Config — the sweep
    itself is monkeypatched out, so no vault is needed."""

    repo_root: Path


def _finding(
    rule_id: str,
    *,
    file: str = _FILE_A,
    severity: Severity = Severity.WARNING,
) -> Finding:
    return Finding(
        rule_id=rule_id,
        file=file,
        line=1,
        message=f"{rule_id} fired",
        severity=severity,
        tier=Tier.CONTENT_SHAPE,
        producer="wiki",
    )


def _write_baseline(repo_root: Path, data: dict[str, dict[str, int]]) -> None:
    path = repo_root / baseline.BASELINE_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data), encoding="utf-8")


def test_load_baseline_missing_file_returns_empty_dict(tmp_path: Path) -> None:
    assert baseline.load_baseline(tmp_path) == {}


def test_save_and_load_round_trip_with_sorted_keys(tmp_path: Path) -> None:
    baseline.save_baseline(tmp_path, {"b.md": {"W2": 1}, "a.md": {"W10": 3, "W1": 2}})

    raw = (tmp_path / baseline.BASELINE_PATH).read_text(encoding="utf-8")
    assert list(json.loads(raw)) == ["a.md", "b.md"]
    assert list(json.loads(raw)["a.md"]) == ["W1", "W10"]
    assert baseline.load_baseline(tmp_path) == {"b.md": {"W2": 1}, "a.md": {"W10": 3, "W1": 2}}


def test_auto_sync_down(tmp_path: Path) -> None:
    """After a sweep, a file's per-rule floor becomes min(live, floor) —
    here live (2) is below the seeded floor (5), so the floor drops."""
    _write_baseline(tmp_path, {_FILE_A: {"W25": 5}})

    findings = [_finding("W25"), _finding("W25")]  # 2 live hits
    baseline.auto_sync_down(tmp_path, findings)

    assert baseline.load_baseline(tmp_path) == {_FILE_A: {"W25": 2}}


def test_auto_sync_down_never_raises_the_floor(tmp_path: Path) -> None:
    """Live (5) above the seeded floor (2): auto_sync_down leaves the
    floor untouched — only `seed`/`promote` may raise it."""
    _write_baseline(tmp_path, {_FILE_A: {"W25": 2}})

    findings = [_finding("W25") for _ in range(5)]
    baseline.auto_sync_down(tmp_path, findings)

    assert baseline.load_baseline(tmp_path) == {_FILE_A: {"W25": 2}}


def test_auto_sync_down_drops_a_rule_fixed_to_zero(tmp_path: Path) -> None:
    """Live 0 (the rule no longer fires anywhere): the entry disappears
    entirely rather than sitting at floor 0 forever."""
    _write_baseline(tmp_path, {_FILE_A: {"W25": 3}})

    baseline.auto_sync_down(tmp_path, findings=[])

    assert baseline.load_baseline(tmp_path) == {}


def test_auto_sync_down_never_creates_new_entries(tmp_path: Path) -> None:
    """A rule with live findings but no baseline entry at all is not
    something auto_sync_down may seed — only seed/promote add entries."""
    _write_baseline(tmp_path, {})

    baseline.auto_sync_down(tmp_path, findings=[_finding("W25")])

    assert baseline.load_baseline(tmp_path) == {}


def test_check_exits_1_style_when_over_floor(tmp_path: Path) -> None:
    """check()'s (ok, over_count) is exactly what a `check exits 1` CLI
    command is built from: any live count above its floor -> not ok."""
    _write_baseline(tmp_path, {_FILE_A: {"W25": 1}})

    ok, over = baseline.check(tmp_path, findings=[_finding("W25"), _finding("W25")])

    assert ok is False
    assert over == 1


def test_check_exits_0_when_all_live_counts_at_or_below_floor(tmp_path: Path) -> None:
    _write_baseline(tmp_path, {_FILE_A: {"W25": 3}, _FILE_B: {"W12": 1}})

    ok, over = baseline.check(
        tmp_path, findings=[_finding("W25"), _finding("W25"), _finding("W12", file=_FILE_B)]
    )

    assert ok is True
    assert over == 0


def test_check_missing_floor_entry_is_floor_zero(tmp_path: Path) -> None:
    """A rule with live findings but no baseline entry for that file/rule
    at all is a regression against an implicit floor of 0 — the same
    "no free debt" contract the legacy engine documents."""
    _write_baseline(tmp_path, {})

    ok, over = baseline.check(tmp_path, findings=[_finding("W25")])

    assert ok is False
    assert over == 1


def test_check_ignores_error_severity(tmp_path: Path) -> None:
    """Error severity is a presence gate elsewhere, never baselined, and
    never counts toward the ratchet."""
    _write_baseline(tmp_path, {})

    ok, over = baseline.check(
        tmp_path,
        findings=[_finding("W1", severity=Severity.ERROR)],
    )

    assert ok is True
    assert over == 0


def test_seed_force_writes_the_baseline_from_scratch(tmp_path: Path) -> None:
    """seed() always writes fresh floors from current live counts,
    overwriting whatever was there before — the CLI is what requires
    --force to reach it (never a fixing agent's own call)."""
    _write_baseline(tmp_path, {_FILE_A: {"W25": 99}})

    baseline.seed(tmp_path, findings=[_finding("W12", file=_FILE_B), _finding("W12", file=_FILE_B)])

    assert baseline.load_baseline(tmp_path) == {_FILE_B: {"W12": 2}}


def test_promote_updates_floor_to_current_counts(tmp_path: Path) -> None:
    """promote() raises (or lowers) every floor to match today's live
    counts exactly — a synonym for seed() in practice."""
    _write_baseline(tmp_path, {_FILE_A: {"W25": 1}})

    baseline.promote(tmp_path, findings=[_finding("W25"), _finding("W25"), _finding("W25")])

    assert baseline.load_baseline(tmp_path) == {_FILE_A: {"W25": 3}}


def test_auto_sync_down_drops_a_file_that_left_the_corpus(tmp_path: Path) -> None:
    """A renamed or deleted file reports no live counts, so `min(live,
    floor)` alone would keep its floor forever. Passing the swept corpus
    prunes it — the floor follows reality."""
    _write_baseline(tmp_path, {_FILE_A: {"W25": 3}, _FILE_B: {"W12": 1}})

    baseline.auto_sync_down(
        tmp_path, findings=[_finding("W12", file=_FILE_B)], corpus=[_FILE_B]
    )

    assert baseline.load_baseline(tmp_path) == {_FILE_B: {"W12": 1}}


def test_auto_sync_down_without_a_corpus_keeps_every_file(tmp_path: Path) -> None:
    """No corpus given: only the live-count rule applies, so a file with a
    live count keeps its floor and nothing is pruned for absence."""
    _write_baseline(tmp_path, {_FILE_A: {"W25": 3}})

    baseline.auto_sync_down(tmp_path, findings=[_finding("W25"), _finding("W25")])

    assert baseline.load_baseline(tmp_path) == {_FILE_A: {"W25": 2}}


def test_over_entries_names_each_pair_and_its_delta(tmp_path: Path) -> None:
    """The triage view `wiki drain --over` prints: which file, which
    rule, how far above — sorted worst delta first."""
    _write_baseline(tmp_path, {_FILE_A: {"W25": 1}, _FILE_B: {"W12": 1}})

    entries = baseline.over_entries(
        tmp_path,
        findings=[
            _finding("W25"),
            _finding("W25"),  # +1 over floor 1
            *[_finding("W12", file=_FILE_B) for _ in range(4)],  # +3 over floor 1
        ],
    )

    assert entries == [(_FILE_B, "W12", 3), (_FILE_A, "W25", 1)]


def test_over_entries_only_paths_restricts_to_a_scoped_run(tmp_path: Path) -> None:
    """A scoped run judges only its own targets — a file outside the
    scope never reaches the verdict."""
    _write_baseline(tmp_path, {})

    entries = baseline.over_entries(
        tmp_path,
        findings=[_finding("W25"), _finding("W12", file=_FILE_B)],
        only_paths=[_FILE_A],
    )

    assert entries == [(_FILE_A, "W25", 1)]


def test_partition_suppresses_only_the_baselined_share(tmp_path: Path) -> None:
    """Floor 2, live 3: two findings are old debt and vanish from the
    listing, the third is the actionable queue and is shown."""
    _write_baseline(tmp_path, {_FILE_A: {"W25": 2}})

    shown, suppressed = baseline.partition(
        tmp_path, findings=[_finding("W25"), _finding("W25"), _finding("W25")]
    )

    assert suppressed == 2
    assert len(shown) == 1


def test_partition_never_suppresses_errors(tmp_path: Path) -> None:
    """Errors are a presence gate — a floor entry for that id cannot hide
    them."""
    _write_baseline(tmp_path, {_FILE_A: {"W1": 5}})

    shown, suppressed = baseline.partition(
        tmp_path,
        findings=[_finding("W1", severity=Severity.ERROR)],
    )

    assert suppressed == 0
    assert len(shown) == 1


def test_partition_with_no_baseline_shows_everything(tmp_path: Path) -> None:
    shown, suppressed = baseline.partition(tmp_path, findings=[_finding("W25")])

    assert suppressed == 0
    assert len(shown) == 1


def test_ratchet_token_ok(tmp_path: Path) -> None:
    _write_baseline(tmp_path, {_FILE_A: {"W25": 3}})

    assert baseline.ratchet_token(tmp_path, findings=[_finding("W25")]) == "ratchet OK"


def test_ratchet_token_over_floor_names_the_listing_command(tmp_path: Path) -> None:
    _write_baseline(tmp_path, {_FILE_A: {"W25": 1}, _FILE_B: {"W12": 1}})

    findings = [
        _finding("W25"),
        _finding("W25"),  # W25 over by 1 (file A)
        _finding("W12", file=_FILE_B),
        _finding("W12", file=_FILE_B),  # W12 over by 1 (file B)
    ]

    assert (
        baseline.ratchet_token(tmp_path, findings)
        == "ratchet +2 over floor — run: wiki drain --over"
    )


def test_ratchet_token_marks_a_scoped_verdict(tmp_path: Path) -> None:
    """A scoped run's token is distinguishable from a full sweep's, and
    covers only the targeted files."""
    _write_baseline(tmp_path, {_FILE_A: {"W25": 3}})

    token = baseline.ratchet_token(
        tmp_path,
        findings=[_finding("W25"), _finding("W12", file=_FILE_B)],
        only_paths=[_FILE_A],
        scoped=True,
    )

    assert token == "ratchet OK (scoped)"


def test_render_never_prints_the_ratchet_state() -> None:
    """ADR-0064: the report is an instruction list — the ratchet is a
    maintenance verdict `wiki ratchet` prints, never report vocabulary."""
    for findings in ([], [_finding("W25")]):
        result = LintResult(
            findings=findings,
            stats=RunStats(files=1, rules_run=1, cache_hits=0, seconds=0.3),
        )

        assert "ratchet" not in render(result)


def test_render_summarises_suppressed_findings_on_one_line() -> None:
    """Baselined old debt never lists itself: one trailing line, naming
    the command that does."""
    result = LintResult(
        findings=[_finding("W25")],
        stats=RunStats(files=1, rules_run=1, cache_hits=0, seconds=0.3),
    )

    output = render(result, suppressed=10991)

    assert output.splitlines()[-2] == (
        "SUPPRESSED: 10,991 baselined findings — run: wiki drain --over"
    )


def test_render_clean_run_still_reports_suppressed_findings() -> None:
    result = LintResult(
        findings=[],
        stats=RunStats(files=1, rules_run=0, cache_hits=0, seconds=0.1),
    )

    output = render(result, suppressed=4)

    assert output.splitlines()[0] == "LINT 1 file — clean"
    assert output.splitlines()[1] == "SUPPRESSED: 4 baselined findings — run: wiki drain --over"


def test_render_quiet_compresses_the_suppression_total_to_a_token() -> None:
    result = LintResult(
        findings=[_finding("W25")],
        stats=RunStats(files=1, rules_run=1, cache_hits=0, seconds=0.1),
    )

    output = render(result, quiet=True, suppressed=1234)

    assert output.splitlines() == [output]
    assert output.endswith("· 1,234 suppressed")


def test_render_without_suppression_has_no_suppressed_line() -> None:
    result = LintResult(
        findings=[_finding("W25")],
        stats=RunStats(files=1, rules_run=1, cache_hits=0, seconds=0.1),
    )

    assert "SUPPRESSED" not in render(result)


def test_drain_over_groups_by_rule_chattiest_first(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """`wiki drain --over` is the triage view the `+N over floor` token
    points at: rule, file count, per-file delta."""
    _write_baseline(tmp_path, {})
    findings = [
        _finding("W25"),
        _finding("W25", file=_FILE_B),
        _finding("W12", file=_FILE_B),
    ]
    monkeypatch.setattr(cli, "load_config", lambda: _StubConfig(tmp_path))
    monkeypatch.setattr(cli, "_git_root", lambda _repo_root: tmp_path)
    monkeypatch.setattr(cli, "_full_sweep_findings", lambda _config: findings)

    result = CliRunner().invoke(cli.app, ["drain", "--over"])

    assert result.exit_code == 0
    lines = result.output.splitlines()
    assert lines[0] == "ratchet +3 over floor · 3 findings above floor"
    assert lines[1] == "W25 — 2 file(s), +2"
    assert lines[2:4] == [f"  +1  {_FILE_B}", f"  +1  {_FILE_A}"]
    assert lines[4] == "W12 — 1 file(s), +1"


def test_drain_over_reports_a_clean_ratchet(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _write_baseline(tmp_path, {_FILE_A: {"W25": 1}})
    monkeypatch.setattr(cli, "load_config", lambda: _StubConfig(tmp_path))
    monkeypatch.setattr(cli, "_git_root", lambda _repo_root: tmp_path)
    monkeypatch.setattr(cli, "_full_sweep_findings", lambda _config: [_finding("W25")])

    result = CliRunner().invoke(cli.app, ["drain", "--over"])

    assert result.exit_code == 0
    assert result.output.startswith("ratchet OK — every (file, rule) pair")


def test_scoped_render_has_no_ratchet_trailer(tmp_path: Path) -> None:
    """A scoped run prints no `ratchet OK (scoped)` trailer: the verdict is
    not an action the reading agent takes."""
    del tmp_path
    result = LintResult(
        findings=[_finding("W25")],
        stats=RunStats(files=1, rules_run=1, cache_hits=0, seconds=0.1),
    )

    assert "(scoped)" not in render(result)
