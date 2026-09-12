"""A minimal publish/subscribe event bus.

Handlers are registered against a plain string event name (a
:class:`~dndsim.core.timeline.Window` id, typically) and invoked in
registration order. The bus carries no opinion about what an event *means*
— a Rules pack defines its own event names and payload shapes.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

Handler = Callable[["Event"], None]


@dataclass(slots=True)
class Event:
    """One dispatched occurrence.

    ``payload`` is opaque to the bus — handlers agree on its shape out of
    band, by event name.
    """

    name: str
    payload: Any = None


class EventBus:
    """Registers handlers by event name and dispatches events to them."""

    def __init__(self, trace: Handler | None = None) -> None:
        self._handlers: dict[str, list[Handler]] = defaultdict(list)
        self._trace = trace

    def subscribe(self, name: str, handler: Handler) -> None:
        self._handlers[name].append(handler)

    def unsubscribe(self, name: str, handler: Handler) -> None:
        self._handlers[name].remove(handler)

    def publish(self, event: Event) -> None:
        if self._trace is not None:
            self._trace(event)
        for handler in list(self._handlers.get(event.name, ())):
            handler(event)

    def handler_count(self, name: str) -> int:
        return len(self._handlers.get(name, ()))
