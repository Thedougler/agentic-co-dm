"""Adaptive stopping over a chunked run of trials (issue #50).

Ends a run once the success-rate confidence interval has tightened past a
threshold, within a floor (minimum trials considered before stopping) and a
cap (maximum trials regardless of convergence) — so a stable answer doesn't
keep consuming trials past the point it stopped changing.

Chunks are consumed in strict index order (0, 1, 2, ...) and each chunk's
stop decision depends only on the outcomes accumulated so far, never on
wall clock or worker count. That is what makes running this same adaptive
run's *chunks* sequential by construction (a chunk can't be scheduled until
the previous one's cumulative count is known) while still letting
independent *cells* — separate adaptive runs, e.g. different matchups in a
sweep — execute in parallel via :mod:`dndsim.core.threaded` with no change
to any one cell's own result.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from dndsim.core.stats import ConfidenceInterval, wilson_interval


@dataclass(frozen=True, slots=True)
class AdaptiveConfig:
    """The four stopping knobs. All four belong on any report/audit line
    that cites a figure produced under adaptive stopping — they are
    determinism inputs, not implementation details.
    """

    chunk: int = 500
    floor: int = 500
    threshold: float = 0.02
    cap: int = 10_000

    def __post_init__(self) -> None:
        if self.chunk < 1:
            raise ValueError(f"chunk must be >= 1, got {self.chunk}")
        if self.floor < 1:
            raise ValueError(f"floor must be >= 1, got {self.floor}")
        if self.cap < self.floor:
            raise ValueError(f"cap ({self.cap}) must be >= floor ({self.floor})")
        if not 0.0 < self.threshold < 1.0:
            raise ValueError(f"threshold must be in (0, 1), got {self.threshold}")


@dataclass(frozen=True, slots=True)
class AdaptiveResult:
    """The outcome of one :func:`run_adaptive` call."""

    successes: int
    trials: int
    interval: ConfidenceInterval
    stopped_early: bool
    config: AdaptiveConfig


def run_adaptive(
    run_chunk: Callable[[int, int], int],
    config: AdaptiveConfig | None = None,
) -> AdaptiveResult:
    """Run chunks of up to ``config.chunk`` trials until the interval converges.

    ``run_chunk(start, size)`` runs ``size`` more trials — the cumulative
    trial count is ``start`` before the call — and returns how many of them
    succeeded. It must derive its own randomness solely from ``(start,
    size)``, never from the stopping decision itself: that is what makes
    stopping at trial count ``n`` bit-identical to a fixed-iteration call
    truncated at the same ``n``.
    """
    if config is None:
        config = AdaptiveConfig()
    successes = 0
    trials = 0
    interval = wilson_interval(0, 0)
    stopped_early = False
    while trials < config.cap:
        size = min(config.chunk, config.cap - trials)
        successes += run_chunk(trials, size)
        trials += size
        interval = wilson_interval(successes, trials)
        half_width = interval.half_width
        if trials >= config.floor and half_width is not None and half_width <= config.threshold:
            stopped_early = trials < config.cap
            break
    return AdaptiveResult(
        successes=successes,
        trials=trials,
        interval=interval,
        stopped_early=stopped_early,
        config=config,
    )
