"""PERF budgets + `wiki bench` (Task 26 of the wiki-lint migration plan,
ADR-0041).

Two independent contracts share this module:

1. `wiki bench` compares each timed sweep against a budget from
   `wiki.toml`'s `[bench]` section — deliberately HALF the legacy JS
   engine's 30s/150s (`utils/scripts/lint-report.mjs`), so a regression the
   old engine tolerated now fails loud. `perf_over_budget_line` names the
   slowest producer so a fixing agent can reproduce and isolate it, rather
   than re-running the whole sweep. `wiki lint` itself never prints it: a
   lint report is read by an agent mid-edit, and a line proposing an
   hour-long re-run is work it must not be handed.
2. `wiki bench` (`run_bench`) times one cold sweep (findings cache cleared)
   and one warm sweep over the whole vault, appends both to
   `.claude/.wiki-bench.jsonl` (gitignored, one JSON object per invocation),
   and flags a >25% regression on the cold time vs the previous entry — the
   same contract as the legacy `npm run lint:bench`
   (`utils/scripts/lint-bench.mjs`) this replaces.
"""

from __future__ import annotations

import json
import tomllib
from pathlib import Path
from typing import TYPE_CHECKING

from wiki_cli.orchestrator import run_lint

if TYPE_CHECKING:
    from wiki_cli.config import Config
    from wiki_cli.orchestrator import LintResult, RunStats

DEFAULT_SCOPED_BUDGET_S = 5.0
DEFAULT_SWEEP_BUDGET_S = 60.0

WIKI_BENCH_PATH = Path(".claude/.wiki-bench.jsonl")
"""Repo-root-relative path to the bench history, mirroring `baseline.
BASELINE_PATH`'s convention."""

_REGRESSION_THRESHOLD = 0.25

_CACHE_SIDECAR_SUFFIXES = ("-wal", "-shm")
"""Same WAL sidecar suffixes `db.py`'s own corruption-recovery path clears."""


def load_budgets(repo_root: Path) -> tuple[float, float]:
    """`(scoped_budget_s, sweep_budget_s)` from `<repo_root>/wiki.toml`'s
    `[bench]` section, defaulting to 5.0/60.0 when the file, the section, or
    either key is absent."""
    config_path = repo_root / "wiki.toml"
    if not config_path.is_file():
        return DEFAULT_SCOPED_BUDGET_S, DEFAULT_SWEEP_BUDGET_S

    data = tomllib.loads(config_path.read_text(encoding="utf-8"))
    bench_table = data.get("bench", {})
    if not isinstance(bench_table, dict):
        return DEFAULT_SCOPED_BUDGET_S, DEFAULT_SWEEP_BUDGET_S

    scoped = bench_table.get("scoped_budget_s", DEFAULT_SCOPED_BUDGET_S)
    sweep = bench_table.get("sweep_budget_s", DEFAULT_SWEEP_BUDGET_S)
    return float(scoped), float(sweep)


_ATTRIBUTABLE_SHARE = 0.5
"""How much of an over-budget run's wall time the slowest producer must
account for before the line names it. Below this the run's cost is the
corpus build and the rule loop, which no `--only <producer>` reproduction
can isolate — naming the biggest of several small producers there sends a
fixing agent to profile something that was never the cost."""


def perf_over_budget_line(stats: RunStats, budget_s: float) -> str | None:
    """One trailing report line naming what actually cost the time, or
    `None` when `stats.seconds` is within `budget_s`.

    Names the slowest producer, with its `--only` reproduction, when that
    producer accounts for at least `_ATTRIBUTABLE_SHARE` of the run. When
    no producer does — including when `per_producer_seconds` is empty — the
    line reports the unattributed remainder instead, since that is where
    the fix has to happen."""
    if stats.seconds <= budget_s:
        return None

    if stats.per_producer_seconds:
        producer, elapsed = max(stats.per_producer_seconds.items(), key=lambda item: item[1])
        if elapsed >= stats.seconds * _ATTRIBUTABLE_SHARE:
            return (
                f"PERF OVER BUDGET: {producer} {elapsed:.1f}s — "
                f"reproduce: wiki lint --only {producer} <target>"
            )
        unattributed = stats.seconds - sum(stats.per_producer_seconds.values())
        return (
            f"PERF OVER BUDGET: {stats.seconds:.1f}s total, {unattributed:.1f}s outside every "
            f"producer (slowest was {producer} at {elapsed:.1f}s) — the cost is corpus build "
            f"over {stats.files} target(s), not one producer"
        )

    return (
        f"PERF OVER BUDGET: {stats.seconds:.1f}s total, no producer ran — "
        f"the cost is corpus build over {stats.files} target(s)"
    )


def is_scoped(targets_count: int, vault_page_count: int) -> bool:
    """True when a run's targets are a strict subset of the vault — the
    scoped budget applies; a full-vault sweep (`targets_count ==
    vault_page_count`) gets the sweep budget instead."""
    return targets_count < vault_page_count


def _full_vault_targets(vault_root: Path) -> list[Path]:
    resolved_root = vault_root.resolve()
    return sorted(
        p
        for p in resolved_root.rglob("*.md")
        if p.resolve().relative_to(resolved_root).parts[:1] != ("_templates",)
    )


def _clear_cache(cache_path: Path) -> None:
    cache_path.unlink(missing_ok=True)
    for suffix in _CACHE_SIDECAR_SUFFIXES:
        Path(f"{cache_path}{suffix}").unlink(missing_ok=True)


def _stats_dict(result: LintResult, budget_s: float) -> dict:
    entry = {
        "seconds": result.stats.seconds,
        "cache_hits": result.stats.cache_hits,
        "per_producer_seconds": dict(result.stats.per_producer_seconds),
        "findings": len(result.findings),
    }
    over_budget = perf_over_budget_line(result.stats, budget_s)
    if over_budget:
        entry["perf_over_budget"] = over_budget
    return entry


def run_bench(
    config: Config, vault_root: Path, *, producers: list[str] | None = None
) -> list[dict]:
    """One cold sweep (findings cache cleared first) + one warm sweep over
    every page under `vault_root`. Returns `[cold, warm]`, each a dict with
    `seconds`, `cache_hits`, `per_producer_seconds`, and `findings`.

    `producers` restricts which producers run (`orchestrator.run_lint`'s
    own param) — tests pass `producers=["wiki"]` to stay isolated from
    external tools; the real `wiki bench` command omits it to time every
    registered producer. Each dict carries a `perf_over_budget` line when
    that sweep ran past the `[bench]` sweep budget."""
    targets = _full_vault_targets(vault_root)
    _, sweep_budget_s = load_budgets(config.repo_root)

    # `no_fix`: a benchmark measures the corpus, it never edits it — and a
    # cold sweep that repaired files would hand the warm sweep different
    # bytes, so the pair would no longer be the same workload twice.
    _clear_cache(config.cache_path)
    cold = run_lint(config, targets, producers=producers, no_fix=True)
    warm = run_lint(config, targets, producers=producers, no_fix=True)

    return [_stats_dict(cold, sweep_budget_s), _stats_dict(warm, sweep_budget_s)]


def append_jsonl(repo_root: Path, entries: list[dict]) -> None:
    """Append each entry as one JSON line to `<repo_root>/.claude/.wiki-bench.jsonl`,
    creating `.claude/` if needed."""
    path = repo_root / WIKI_BENCH_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for entry in entries:
            handle.write(json.dumps(entry) + "\n")


def last_entry(repo_root: Path) -> dict | None:
    """The most recently appended bench entry, or `None` when the log
    doesn't exist yet — read before `append_jsonl` writes the new one, so
    `check_regression` has something to compare against."""
    path = repo_root / WIKI_BENCH_PATH
    if not path.is_file():
        return None
    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line]
    if not lines:
        return None
    return json.loads(lines[-1])


def check_regression(current: dict, previous: dict | None) -> str | None:
    """A warning when `current["seconds"]` is more than 25% worse than
    `previous["seconds"]`; `None` when there's no previous entry, no prior
    timing to compare, or the regression is within threshold."""
    if previous is None:
        return None
    prev_seconds = previous.get("seconds")
    curr_seconds = current.get("seconds")
    if not prev_seconds or curr_seconds is None:
        return None

    delta = (curr_seconds - prev_seconds) / prev_seconds
    if delta <= _REGRESSION_THRESHOLD:
        return None

    return (
        f"REGRESSION: cold sweep is {delta * 100:.0f}% slower than the previous "
        f"benchmark ({prev_seconds:.1f}s -> {curr_seconds:.1f}s) — find the producer "
        "that grew before trusting new lint changes."
    )
