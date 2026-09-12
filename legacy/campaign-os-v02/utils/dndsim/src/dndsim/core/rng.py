"""A single seeded, batched random source shared across a simulation run.

``dndsim`` determinism (ADR-0011, issue #39 acceptance criteria) rests on
one rule: a :class:`BatchRNG` wraps exactly one ``numpy.random.Generator``
per run, and every draw pulls from it in the same call order for a given
code path. Identical seed + identical call sequence => identical output.
Mechanics draw batched values (one per universe, or one per masked slice)
rather than looping per-universe draws, which is what makes the lockstep
batching in ADR-0011 pay off.

Issue #50 layers seeding on top of that single-generator rule so
reproducibility survives running independent cells in parallel (ADR-0012):

- A **run seed** — the top-level seed a caller supplies or, via
  :func:`random_seed`, one generated and reported when they don't.
- A **substream seed**, :func:`substream_seed`, derived from the run seed
  and a cell's position. Two cells with different positions never collide,
  no matter what order threads happen to finish them in.
- A **cell seed**, :func:`cell_seed`, derived from the run seed and a
  stable string key naming the cell's own identity (not its position) —
  what lets one cell of a larger run be re-run alone, by key, and
  reproduce exactly.

Algorithm shape: double splitmix32 mixing, FNV-1a for the string key.
"""

from __future__ import annotations

import secrets

import numpy as np

_MASK32 = 0xFFFFFFFF


def _splitmix32(state: int) -> int:
    """One splitmix32 mixing step: a 32-bit state to a well-mixed 32-bit value."""
    z = (state + 0x9E3779B9) & _MASK32
    z = ((z ^ (z >> 16)) * 0x21F0AAAD) & _MASK32
    z = ((z ^ (z >> 15)) * 0x735A2D97) & _MASK32
    return (z ^ (z >> 15)) & _MASK32


def _fnv1a32(text: str) -> int:
    """FNV-1a 32-bit hash of a UTF-8 string — deterministic, no external dependency."""
    h = 0x811C9DC5
    for byte in text.encode("utf-8"):
        h ^= byte
        h = (h * 0x01000193) & _MASK32
    return h


def random_seed() -> int:
    """A fresh unsigned 32-bit seed for a run that supplied none.

    Cryptographically sourced (``secrets``) so concurrent invocations never
    collide; the caller is responsible for reporting the value it draws so
    the run can be repeated later.
    """
    return secrets.randbelow(0x100000000)


def substream_seed(seed: int, index: int) -> int:
    """An independent seed for the ``index``-th cell of a run seeded ``seed``.

    Deterministic in ``(seed, index)`` alone — never in execution order —
    which is what keeps a threaded run's output identical to the serial
    run's regardless of how many workers process the cells or in what
    order they complete (ADR-0012).
    """
    return _splitmix32(_splitmix32(seed & _MASK32) ^ _splitmix32(index & _MASK32))


def cell_seed(seed: int, key: str) -> int:
    """The stable seed for the cell identified by ``key`` under run ``seed``.

    Same ``seed`` + same ``key`` always derive the same value, regardless
    of the cell's position in any particular run — what lets one cell of a
    larger sweep be re-run alone, addressed only by its own identity, and
    reproduce exactly the number it produced inside the full run.
    """
    return _splitmix32(_splitmix32(seed & _MASK32) ^ _fnv1a32(key))


class BatchRNG:
    """Thin wrapper around ``numpy.random.Generator`` for batched draws."""

    def __init__(self, seed: int) -> None:
        self.seed = seed
        self._generator = np.random.default_rng(seed)

    def integers(self, low: int, high: int, size: int | tuple[int, ...]) -> np.ndarray:
        """Uniform integers in ``[low, high)``, inclusive-low/exclusive-high."""
        return self._generator.integers(low, high, size=size)

    def uniform(self, size: int | tuple[int, ...]) -> np.ndarray:
        """Uniform floats in ``[0, 1)``."""
        return self._generator.uniform(size=size)
