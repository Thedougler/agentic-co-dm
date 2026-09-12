"""The lockstep Monte-Carlo batch (ADR-0011).

A :class:`UniverseBatch` is the unit of parallelism: ``size`` independent
Monte-Carlo samples ("universes") advanced together, one event dispatch at a
time, with divergent decisions bucketed and resolved on masked slices. The
core provides the batch container and the bucketing helper; what a universe
*contains* (resource pools, tags, entities) is assembled by a Rules pack.
"""

from __future__ import annotations

import numpy as np

from dndsim.core.rng import BatchRNG


class UniverseBatch:
    """``size`` parallel universes sharing one seeded RNG stream."""

    def __init__(self, size: int, seed: int) -> None:
        if size < 1:
            raise ValueError(f"UniverseBatch size must be >= 1, got {size}")
        self.size = size
        self.seed = seed
        self.rng = BatchRNG(seed)
        self.active = np.ones(size, dtype=np.bool_)


def bucket_by_choice(codes: np.ndarray) -> list[tuple[int, np.ndarray]]:
    """Group a per-universe choice-code array into ``(code, mask)`` buckets.

    ``codes`` holds one integer choice per universe; a code of ``-1`` means
    "no choice made this dispatch" (e.g. the actor is inactive) and is
    excluded from the returned buckets. This is the vectorized-argmax ->
    bucket -> masked-resolve shape from ADR-0011's Phase 0 spike.
    """
    present = np.unique(codes[codes >= 0])
    return [(int(code), codes == code) for code in present]
