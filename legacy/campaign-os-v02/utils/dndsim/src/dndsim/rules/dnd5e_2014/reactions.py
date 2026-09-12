"""Reactions: fired via the core :class:`~dndsim.core.events.EventBus` from
inside another combatant's own action window, gated by a resource pool
exactly like any other spendable.

Most 5e reactions are 1-per-turn, refreshed at the start of the reactor's
*own* turn (PHB p.190) — not at the start of every round, and not shared
across combatants. A standard :class:`~dndsim.core.resources.ResourcePool`
already models that precisely: :func:`make_reaction_pool` builds one, and
restoring it to its max at the reactor's own `start_of_turn` window is the
same mechanism any other per-turn resource uses (see
:mod:`dndsim.rules.dnd5e_2014.encounter_timeline`). This module adds no
reaction-specific bookkeeping beyond that pool.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

import numpy as np

from dndsim.core.events import Event, EventBus
from dndsim.core.resources import ResourcePool

REACTION_POOL_NAME = "reaction"

ReactionHandler = Callable[[Event, np.ndarray], None]
EligibilityCheck = Callable[[Event], np.ndarray]


def make_reaction_pool(size: int) -> ResourcePool:
    """A standard 1-per-turn reaction pool for a batch of `size` universes."""
    return ResourcePool(REACTION_POOL_NAME, np.ones(size, dtype=np.float64))


@dataclass(slots=True)
class ReactionBinding:
    """One reactor's subscription to one trigger window, gated by its own
    reaction pool. Constructed by :func:`register_reaction`; not meant to
    be built directly."""

    trigger: str
    pool: ResourcePool
    handler: ReactionHandler
    eligible: EligibilityCheck

    def _on_event(self, event: Event) -> None:
        mask = self.eligible(event) & ~self.pool.depleted()
        if not bool(mask.any()):
            return
        self.pool.spend(np.ones(int(mask.sum()), dtype=np.float64), mask)
        self.handler(event, mask)


def register_reaction(
    bus: EventBus,
    *,
    trigger: str,
    pool: ResourcePool,
    eligible: EligibilityCheck,
    handler: ReactionHandler,
) -> ReactionBinding:
    """Subscribe one reaction to `trigger` on `bus`. On every publish to
    `trigger` (typically from inside another combatant's own action
    resolution — an `action:<id>` window firing mid-turn, never a reaction-
    specific dispatch path), the reaction fires in exactly the universes
    where both `eligible(event)` holds AND the reactor's own pool still has
    a charge, spending that charge before running `handler`. This is what
    makes "a reaction triggered inside another combatant's action" a plain
    :class:`~dndsim.core.events.EventBus` subscription rather than a
    simulator special case."""
    binding = ReactionBinding(trigger=trigger, pool=pool, handler=handler, eligible=eligible)
    bus.subscribe(trigger, binding._on_event)
    return binding
