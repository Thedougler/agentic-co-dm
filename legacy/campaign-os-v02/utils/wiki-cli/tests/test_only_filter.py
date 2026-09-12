"""TDD for `wiki lint --only`: execution-gating (not display-only, unlike
`--rule`/`--producer`, ADR-0023) so an agent can run a single rule or
producer against the whole repo without paying for every other producer.
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

from typer.testing import CliRunner

from wiki_cli.cli import _resolve_only, app
from wiki_cli.contracts import Finding, Severity, Tier
from wiki_cli.orchestrator import LintResult, RunStats

runner = CliRunner()


def _lint_result(findings: list[Finding], *, per_producer_seconds: dict[str, float]) -> LintResult:
    return LintResult(
        findings=findings,
        stats=RunStats(
            files=1,
            rules_run=1,
            cache_hits=0,
            seconds=0.2,
            per_producer_seconds=per_producer_seconds,
        ),
    )


# --- _resolve_only ---


def test_resolve_only_rule_id_maps_to_its_producer() -> None:
    producers, rule_filter = _resolve_only(["W25"])
    assert producers == ["wiki"]
    assert rule_filter == ["W25"]


def test_resolve_only_producer_name_has_no_rule_filter() -> None:
    producers, rule_filter = _resolve_only(["wiki"])
    assert producers == ["wiki"]
    assert rule_filter is None


def test_resolve_only_merges_and_dedupes_producers_across_rule_ids() -> None:
    # W25 and W5 are both native rules — same "wiki" producer — so the
    # producers list dedupes to one entry while the rule filter keeps both.
    producers, rule_filter = _resolve_only(["W25", "W5"])
    assert producers == ["wiki"]
    assert rule_filter == ["W25", "W5"]


def test_resolve_only_mixes_rule_id_and_producer_name() -> None:
    producers, rule_filter = _resolve_only(["W25", "W86"])
    assert producers == ["wiki", "W86"]
    assert rule_filter == ["W25"]


# --- CLI wiring ---


def test_only_gates_execution_to_the_resolved_producer(tmp_path: Path) -> None:
    target = tmp_path / "page.md"
    target.write_text("---\ntype: npc\n---\nbody\n")
    finding = Finding(
        rule_id="W5",
        file=str(target),
        line=1,
        message="x",
        severity=Severity.WARNING,
        tier=Tier.STRUCTURAL,
        producer="wiki",
    )
    with patch("wiki_cli.cli.run_lint") as mock_run_lint:
        mock_run_lint.return_value = _lint_result([finding], per_producer_seconds={"wiki": 0.1})
        result = runner.invoke(app, ["lint", str(target), "--only", "W5", "--quiet"])

    assert result.exit_code in (0, 1)
    _, kwargs = mock_run_lint.call_args
    assert kwargs["producers"] == ["wiki"]


def test_lint_with_no_paths_is_a_usage_error_naming_sweep(tmp_path: Path) -> None:
    """ADR-0064: `lint` is the scoped edit loop, `sweep` is the corpus —
    a bare `lint` never silently sweeps."""
    del tmp_path
    with patch("wiki_cli.cli.run_lint") as mock_run_lint:
        result = runner.invoke(app, ["lint", "--quiet"])

    assert result.exit_code == 2
    assert "usage: wiki lint <paths> — full corpus is: wiki sweep" in result.output
    mock_run_lint.assert_not_called()


def test_sweep_runs_unscoped_over_every_producer(tmp_path: Path) -> None:
    del tmp_path
    with patch("wiki_cli.cli.run_lint") as mock_run_lint:
        mock_run_lint.return_value = _lint_result([], per_producer_seconds={})
        runner.invoke(app, ["sweep", "--quiet"])

    _, kwargs = mock_run_lint.call_args
    assert kwargs["scoped"] is False
    assert "producers" not in kwargs


def test_a_run_with_paths_is_scoped(tmp_path: Path) -> None:
    target = tmp_path / "page.md"
    target.write_text("---\ntype: npc\n---\nbody\n")
    with patch("wiki_cli.cli.run_lint") as mock_run_lint:
        mock_run_lint.return_value = _lint_result([], per_producer_seconds={})
        runner.invoke(app, ["lint", str(target), "--quiet"])

    _, kwargs = mock_run_lint.call_args
    assert kwargs["scoped"] is True


def test_only_prints_per_producer_timing_footer(tmp_path: Path) -> None:
    target = tmp_path / "page.md"
    target.write_text("---\ntype: npc\n---\nbody\n")
    finding = Finding(
        rule_id="W5",
        file=str(target),
        line=1,
        message="x",
        severity=Severity.WARNING,
        tier=Tier.STRUCTURAL,
        producer="wiki",
    )
    with patch("wiki_cli.cli.run_lint") as mock_run_lint:
        mock_run_lint.return_value = _lint_result([finding], per_producer_seconds={"wiki": 0.4})
        result = runner.invoke(app, ["lint", str(target), "--only", "W5", "--quiet"])

    assert "wiki: 0.4s  (1 findings)" in result.output


def _slow_result() -> LintResult:
    """A run whose wall time would have blown the old 5s scoped budget."""
    return LintResult(
        findings=[],
        stats=RunStats(
            files=1,
            rules_run=1,
            cache_hits=0,
            seconds=99.0,
            per_producer_seconds={"W86": 98.0},
        ),
    )


def test_lint_never_proposes_a_rerun(tmp_path: Path) -> None:
    """A lint report is read by an agent mid-edit. Neither a budget line
    nor a GATED line may appear there, however long the run took — both
    name work the agent must not go and do."""
    target = tmp_path / "page.md"
    target.write_text("---\ntype: npc\n---\nbody\n")
    with patch("wiki_cli.cli.run_lint") as mock_run_lint:
        mock_run_lint.return_value = _slow_result()
        result = runner.invoke(app, ["lint", str(target), "--quiet"])

    assert "PERF OVER BUDGET" not in result.output
    assert "GATED" not in result.output
    assert "--slow" not in result.output
