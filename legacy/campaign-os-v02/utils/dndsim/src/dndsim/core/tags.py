"""Batched, per-universe tag membership.

A :class:`BatchTags` tracks which universes currently have which named tag
set — the batched analogue of :attr:`dndsim.core.entity.Entity.tags`, for
state that can turn on and off per universe as a simulation runs (a Rules
pack's own status vocabulary, whatever it names). The core never interprets
a tag name.
"""

from __future__ import annotations

import numpy as np


class BatchTags:
    """Boolean tag membership, one array of shape ``(size,)`` per tag name."""

    def __init__(self, size: int) -> None:
        self._size = size
        self._tags: dict[str, np.ndarray] = {}

    def add(self, tag: str, mask: np.ndarray) -> None:
        arr = self._tags.setdefault(tag, np.zeros(self._size, dtype=np.bool_))
        arr[mask] = True

    def remove(self, tag: str, mask: np.ndarray) -> None:
        arr = self._tags.setdefault(tag, np.zeros(self._size, dtype=np.bool_))
        arr[mask] = False

    def has(self, tag: str) -> np.ndarray:
        return self._tags.get(tag, np.zeros(self._size, dtype=np.bool_))
