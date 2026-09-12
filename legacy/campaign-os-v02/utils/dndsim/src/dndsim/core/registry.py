"""A generic plugin registry, backed by ``importlib.metadata`` entry points.

One :class:`Registry` instance exists per pluggable component group
(Rules packs, Mechanics, Policies, Importers — the groups named in
docs/CONTEXT.md's Combat simulation vocabulary). Components register either
in-tree, via the :meth:`Registry.register` decorator, or out-of-tree, by
declaring an ``importlib.metadata`` entry point in the group's name and
calling :meth:`Registry.load_entry_points` once at startup. The registry
holds no opinion about what it stores — it is keyed by a plain string id.
"""

from __future__ import annotations

import logging
from collections.abc import Callable, Iterator
from importlib.metadata import entry_points
from typing import cast

logger = logging.getLogger(__name__)


class DuplicateRegistrationError(ValueError):
    """Raised when two components register the same id in one registry."""


class Registry[T]:
    """Maps a stable string id (``namespace:type/slug``) to a component."""

    def __init__(self, group: str) -> None:
        self.group = group
        self._items: dict[str, T] = {}

    def register[C](self, component_id: str) -> Callable[[C], C]:
        """Decorator: register ``component`` under ``component_id``.

        Generic in the decorated component's own type, not the registry's,
        so that decorating a class returns that exact class. Without this,
        stacking ``@registry.register(...)`` above ``@dataclass`` erases the
        synthesized ``__init__`` and every construction call becomes a type
        error. ``C`` cannot be bound to ``T`` — a TypeVar bound may not
        itself be generic — so the element type is asserted at the storage
        site instead; :meth:`register_value` keeps the strict signature.
        """

        def decorator(component: C) -> C:
            if component_id in self._items:
                raise DuplicateRegistrationError(
                    f"{component_id!r} is already registered in group {self.group!r}"
                )
            self._items[component_id] = cast("T", component)
            return component

        return decorator

    def register_value(self, component_id: str, component: T) -> None:
        """Non-decorator registration for when the value already exists."""
        if component_id in self._items:
            raise DuplicateRegistrationError(
                f"{component_id!r} is already registered in group {self.group!r}"
            )
        self._items[component_id] = component

    def load_entry_points(self) -> None:
        """Import and invoke every entry point declared in this registry's group.

        Each entry point's callable is expected to perform its own
        registration (typically by calling back into this registry) as a
        side effect of being loaded.
        """
        for ep in entry_points(group=self.group):
            loader = ep.load()
            logger.debug("dndsim: loading entry point %s -> %s", ep.name, ep.value)
            loader()

    def get(self, component_id: str) -> T:
        try:
            return self._items[component_id]
        except KeyError:
            raise KeyError(f"{component_id!r} is not registered in group {self.group!r}") from None

    def __contains__(self, component_id: str) -> bool:
        return component_id in self._items

    def __iter__(self) -> Iterator[str]:
        return iter(self._items)

    def items(self) -> Iterator[tuple[str, T]]:
        return iter(self._items.items())

    def values(self) -> Iterator[T]:
        return iter(self._items.values())

    def __len__(self) -> int:
        return len(self._items)
