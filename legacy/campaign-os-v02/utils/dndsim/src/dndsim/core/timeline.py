"""A generic timeline of phases and windows.

A :class:`Timeline` is an ordered sequence of :class:`Phase` objects; each
phase is an ordered sequence of :class:`Window` ids — named hook points a
Rules pack's :class:`~dndsim.core.events.EventBus` handlers subscribe to.
The core assigns no meaning to a phase or window name: "round" and "action"
are Rules-pack vocabulary, not core vocabulary.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Window:
    """One named hook point within a phase."""

    id: str


@dataclass(frozen=True, slots=True)
class Phase:
    """An ordered group of windows."""

    id: str
    windows: tuple[Window, ...] = field(default_factory=tuple)

    def __iter__(self) -> Iterator[Window]:
        return iter(self.windows)


@dataclass(frozen=True, slots=True)
class Timeline:
    """An ordered sequence of phases, walked once per repetition."""

    phases: tuple[Phase, ...] = field(default_factory=tuple)

    def __iter__(self) -> Iterator[Phase]:
        return iter(self.phases)
