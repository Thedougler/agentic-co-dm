from __future__ import annotations

import numpy as np

from dndsim.core.events import Event, EventBus
from dndsim.rules.dnd5e_2014.reactions import make_reaction_pool, register_reaction


def test_reaction_fires_during_another_combatants_action_event() -> None:
    size = 4
    bus = EventBus()
    pool = make_reaction_pool(size)
    fired_masks: list[np.ndarray] = []

    register_reaction(
        bus,
        trigger="action:enemy-1",  # published from inside the ENEMY's own action
        pool=pool,
        eligible=lambda event: np.ones(size, dtype=np.bool_),
        handler=lambda event, mask: fired_masks.append(mask.copy()),
    )

    # simulator publishes this event mid-resolution of enemy-1's attack —
    # the reactor never gets its own dedicated turn/window for it.
    bus.publish(Event(name="action:enemy-1", payload={"round": 1}))

    assert len(fired_masks) == 1
    assert fired_masks[0].all()


def test_reaction_spends_its_resource_pool_and_then_is_exhausted() -> None:
    size = 3
    bus = EventBus()
    pool = make_reaction_pool(size)
    fire_count = [0]

    register_reaction(
        bus,
        trigger="on_hit",
        pool=pool,
        eligible=lambda event: np.ones(size, dtype=np.bool_),
        handler=lambda event, mask: fire_count.__setitem__(0, fire_count[0] + 1),
    )

    assert not pool.depleted().any()
    bus.publish(Event(name="on_hit"))
    assert pool.depleted().all()
    assert fire_count[0] == 1

    # second trigger this "turn": pool is spent, so the handler never runs.
    bus.publish(Event(name="on_hit"))
    assert fire_count[0] == 1

    # refreshed at the reactor's own start_of_turn window (an ordinary
    # ResourcePool.restore, exactly like any other per-turn resource).
    pool.restore(pool.max_value.copy(), np.ones(size, dtype=np.bool_))
    bus.publish(Event(name="on_hit"))
    assert fire_count[0] == 2


def test_reaction_only_fires_in_eligible_universes() -> None:
    size = 4
    bus = EventBus()
    pool = make_reaction_pool(size)
    fired_masks: list[np.ndarray] = []
    eligible_mask = np.array([True, False, True, False])

    register_reaction(
        bus,
        trigger="on_hit",
        pool=pool,
        eligible=lambda event: eligible_mask,
        handler=lambda event, mask: fired_masks.append(mask.copy()),
    )

    bus.publish(Event(name="on_hit"))
    assert fired_masks[0].tolist() == eligible_mask.tolist()
    # only the eligible universes spent their charge
    assert pool.depleted().tolist() == eligible_mask.tolist()
