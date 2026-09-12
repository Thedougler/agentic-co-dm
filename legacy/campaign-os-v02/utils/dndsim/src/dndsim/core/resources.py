"""Batched resource pools.

A :class:`ResourcePool` holds one named, spendable quantity per universe in
a batch (a mana pool, an ammo count, a per-encounter charge, a vitality
total — anything a Rules pack meters). The core has no opinion on what any
given pool represents; a Rules pack declares each one and what depleting it
means.
"""

from __future__ import annotations

import numpy as np


class ResourcePool:
    """A per-universe integer quantity bounded to ``[0, max_value]``."""

    def __init__(self, name: str, max_value: np.ndarray) -> None:
        self.name = name
        self.max_value = max_value.copy()
        self.current = max_value.copy()

    @property
    def size(self) -> int:
        return int(self.max_value.shape[0])

    def spend(self, amount: np.ndarray, mask: np.ndarray) -> None:
        """Subtract ``amount`` (shape ``(mask.sum(),)``) from the masked universes, clamped to 0."""
        idx = np.flatnonzero(mask)
        if amount.shape[0] != idx.shape[0]:
            raise ValueError(
                f"amount has {amount.shape[0]} entries but mask selects {idx.shape[0]}"
            )
        np.subtract.at(self.current, idx, amount)
        np.maximum(self.current, 0, out=self.current)

    def restore(self, amount: np.ndarray, mask: np.ndarray) -> None:
        """Add ``amount`` (shape ``(mask.sum(),)``) to masked universes; clamps to ``max_value``."""
        idx = np.flatnonzero(mask)
        if amount.shape[0] != idx.shape[0]:
            raise ValueError(
                f"amount has {amount.shape[0]} entries but mask selects {idx.shape[0]}"
            )
        np.add.at(self.current, idx, amount)
        self.current = np.minimum(self.current, self.max_value)

    def depleted(self) -> np.ndarray:
        """Boolean array: True where ``current`` has reached zero."""
        return self.current <= 0
