from __future__ import annotations

from collections.abc import Callable

import numpy as np
import pytest

from dndsim.core.adaptive import AdaptiveConfig, run_adaptive


def _fixed_rate_chunk(rate: float, rng: np.random.Generator) -> Callable[[int, int], int]:
    def _run_chunk(start: int, size: int) -> int:
        draws = rng.uniform(size=size)
        return int((draws < rate).sum())

    return _run_chunk


def test_stops_early_once_interval_converges() -> None:
    rng = np.random.default_rng(1)
    config = AdaptiveConfig(chunk=200, floor=200, threshold=0.05, cap=20_000)
    result = run_adaptive(_fixed_rate_chunk(0.5, rng), config)
    assert result.stopped_early
    assert result.trials < config.cap
    assert result.interval.half_width is not None
    assert result.interval.half_width <= config.threshold


def test_respects_floor_even_if_converged_earlier() -> None:
    # A single trial can look "converged" by chance; floor forbids stopping
    # before it, no matter what the running interval says.
    rng = np.random.default_rng(2)
    config = AdaptiveConfig(chunk=50, floor=500, threshold=0.5, cap=20_000)
    result = run_adaptive(_fixed_rate_chunk(0.5, rng), config)
    assert result.trials >= config.floor


def test_respects_cap_when_never_converging() -> None:
    rng = np.random.default_rng(3)
    # threshold impossible to reach (0) forces the run to the cap.
    config = AdaptiveConfig(chunk=100, floor=100, threshold=1e-9, cap=1_000)
    result = run_adaptive(_fixed_rate_chunk(0.5, rng), config)
    assert result.trials == config.cap
    assert not result.stopped_early


def test_stopping_at_n_matches_fixed_iteration_truncated_at_n() -> None:
    # The determinism guarantee: run_chunk depends only on (start, size),
    # never on the stopping decision, so a run that stops at trial n is
    # identical to a fixed run of exactly n trials built the same way.
    seed = 99

    def run_chunk(start: int, size: int) -> int:
        rng = np.random.default_rng(seed + start)
        return int((rng.uniform(size=size) < 0.5).sum())

    config = AdaptiveConfig(chunk=300, floor=300, threshold=0.03, cap=5_000)
    adaptive_result = run_adaptive(run_chunk, config)

    # Reproduce the same trial count as one fixed-size call built from the
    # same chunk sequence.
    n = adaptive_result.trials
    total = 0
    covered = 0
    while covered < n:
        size = min(config.chunk, n - covered)
        total += run_chunk(covered, size)
        covered += size
    assert total == adaptive_result.successes


def test_invalid_config_raises() -> None:
    with pytest.raises(ValueError):
        AdaptiveConfig(chunk=0)
    with pytest.raises(ValueError):
        AdaptiveConfig(floor=0)
    with pytest.raises(ValueError):
        AdaptiveConfig(cap=10, floor=20)
    with pytest.raises(ValueError):
        AdaptiveConfig(threshold=0.0)
    with pytest.raises(ValueError):
        AdaptiveConfig(threshold=1.0)
