"""TDD for `wiki_cli.bench` (Task 26 of the wiki-lint migration plan,
ADR-0041): PERF budgets on every `wiki lint` run, plus `wiki bench`'s
cold+warm sweep history (`.claude/.wiki-bench.jsonl`), same contract as
the legacy `npm run lint:bench` (`utils/scripts/lint-bench.mjs`) this
replaces.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from wiki_cli import bench
from wiki_cli.config import Config
from wiki_cli.orchestrator import RunStats

FIXTURES = Path(__file__).parent / "fixtures" / "orchestrator"


def _config(root: Path) -> Config:
    return Config(
        repo_root=root,
        vault_root=root / "vault",
        templates_root=root / "vault" / "_templates",
        cache_path=root / "cache.sqlite3",
        scoped_roots=("vault",),
        report_cap=50,
        fingerprint="test-fingerprint",
        _thresholds={},
    )


@pytest.fixture
def vault(tmp_path: Path) -> Path:
    dest = tmp_path / "vault" / "orchestrator"
    dest.mkdir(parents=True)
    shutil.copytree(FIXTURES, dest, dirs_exist_ok=True)
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    return tmp_path


# --- load_budgets ---


def test_load_budgets_defaults_when_no_wiki_toml(tmp_path: Path) -> None:
    assert bench.load_budgets(tmp_path) == (5.0, 60.0)


def test_load_budgets_reads_bench_section(tmp_path: Path) -> None:
    (tmp_path / "wiki.toml").write_text(
        "[bench]\nscoped_budget_s = 10\nsweep_budget_s = 120\n", encoding="utf-8"
    )
    assert bench.load_budgets(tmp_path) == (10.0, 120.0)


def test_load_budgets_defaults_when_no_bench_section(tmp_path: Path) -> None:
    (tmp_path / "wiki.toml").write_text('[vault]\nroot = "vault"\n', encoding="utf-8")
    assert bench.load_budgets(tmp_path) == (5.0, 60.0)


# --- perf_over_budget_line ---


def test_budget_line_on_overrun() -> None:
    stats = RunStats(
        files=10,
        rules_run=20,
        cache_hits=0,
        seconds=12.3,
        per_producer_seconds={"wiki": 2.1, "W87": 9.8},
    )
    line = bench.perf_over_budget_line(stats, 5.0)
    assert line is not None
    assert line.startswith("PERF OVER BUDGET: W87 9.8s")
    assert "reproduce: wiki lint --only W87" in line


def test_no_budget_line_under_budget() -> None:
    stats = RunStats(
        files=10,
        rules_run=20,
        cache_hits=0,
        seconds=2.0,
        per_producer_seconds={"wiki": 1.0, "W87": 1.0},
    )
    assert bench.perf_over_budget_line(stats, 5.0) is None


def test_budget_line_reports_unattributed_time_when_no_producer_dominates() -> None:
    """A 6s run whose producers total 0.6s is a corpus-build cost — naming
    the biggest of them sends a fixing agent to profile the wrong thing."""
    stats = RunStats(
        files=1,
        rules_run=20,
        cache_hits=0,
        seconds=6.1,
        per_producer_seconds={"wiki": 0.5, "W91": 0.1},
    )
    line = bench.perf_over_budget_line(stats, 5.0)
    assert line is not None
    assert "6.1s total" in line
    assert "5.5s outside every producer" in line
    assert "--only" not in line


def test_budget_line_falls_back_when_no_producer_timing() -> None:
    stats = RunStats(files=1, rules_run=1, cache_hits=0, seconds=8.0)
    line = bench.perf_over_budget_line(stats, 5.0)
    assert line is not None
    assert "PERF OVER BUDGET:" in line
    assert "8.0s" in line


# --- is_scoped ---


def test_is_scoped_true_when_targets_below_vault_count() -> None:
    assert bench.is_scoped(1, 200) is True


def test_is_scoped_false_on_full_sweep() -> None:
    assert bench.is_scoped(200, 200) is False


# --- append_jsonl ---


def test_bench_jsonl_append(tmp_path: Path) -> None:
    bench.append_jsonl(tmp_path, [{"date": "2026-08-09", "cold": {"seconds": 1.0}}])
    bench.append_jsonl(tmp_path, [{"date": "2026-08-10", "cold": {"seconds": 2.0}}])

    path = tmp_path / bench.WIKI_BENCH_PATH
    lines = path.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 2
    assert json.loads(lines[0])["date"] == "2026-08-09"
    assert json.loads(lines[1])["cold"]["seconds"] == 2.0


def test_last_entry_reads_the_final_jsonl_line(tmp_path: Path) -> None:
    assert bench.last_entry(tmp_path) is None
    bench.append_jsonl(tmp_path, [{"date": "2026-08-09"}])
    bench.append_jsonl(tmp_path, [{"date": "2026-08-10"}])
    assert bench.last_entry(tmp_path) == {"date": "2026-08-10"}


# --- check_regression ---


def test_regression_flag() -> None:
    current = {"seconds": 13.0}
    previous = {"seconds": 10.0}
    warning = bench.check_regression(current, previous)
    assert warning is not None
    assert "REGRESSION" in warning
    assert "30%" in warning


def test_regression_not_flagged_under_threshold() -> None:
    current = {"seconds": 11.0}
    previous = {"seconds": 10.0}
    assert bench.check_regression(current, previous) is None


def test_regression_none_when_no_previous_entry() -> None:
    assert bench.check_regression({"seconds": 100.0}, None) is None


# --- run_bench ---


def test_run_bench_cold_then_warm(vault: Path) -> None:
    config = _config(vault)
    vault_root = vault / "vault"

    entries = bench.run_bench(config, vault_root, producers=["wiki"])

    assert len(entries) == 2
    cold, warm = entries
    assert cold["cache_hits"] == 0
    assert warm["cache_hits"] > 0
    assert "seconds" in cold and "seconds" in warm
    assert "per_producer_seconds" in cold
