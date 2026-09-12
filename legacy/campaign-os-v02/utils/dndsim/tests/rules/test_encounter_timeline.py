from __future__ import annotations

import numpy as np

from dndsim.core.events import Event, EventBus
from dndsim.core.resources import ResourcePool
from dndsim.rules.dnd5e_2014.encounter_timeline import build_round_timeline, run_round


def test_round_timeline_orders_turns_and_appends_round_end() -> None:
    timeline = build_round_timeline(["pc-1", "boss"])
    bus = EventBus()
    fired = run_round(timeline, bus, round_num=1)

    assert fired == [
        "start_of_turn:pc-1",
        "action:pc-1",
        "end_of_turn:pc-1",
        "start_of_turn:boss",
        "action:boss",
        "end_of_turn:boss",
        "end_of_round",
    ]


def test_lair_action_window_fires_before_any_turn() -> None:
    timeline = build_round_timeline(["pc-1", "boss"], has_lair=True)
    bus = EventBus()
    fired = run_round(timeline, bus, round_num=1)

    assert fired[0] == "lair_action"
    assert fired.index("lair_action") < fired.index("start_of_turn:pc-1")


def test_legendary_action_window_fires_after_other_combatants_turns_only() -> None:
    timeline = build_round_timeline(["pc-1", "pc-2", "boss"], legendary_ids=frozenset({"boss"}))
    bus = EventBus()
    fired = run_round(timeline, bus, round_num=1)

    # legendary window for "boss" appears after EACH other combatant's turn...
    assert "legendary_action:boss" in fired
    assert fired.count("legendary_action:boss") == 2
    idx_pc1_end = fired.index("end_of_turn:pc-1")
    idx_pc2_end = fired.index("end_of_turn:pc-2")
    legendary_indices = [i for i, w in enumerate(fired) if w == "legendary_action:boss"]
    assert legendary_indices[0] == idx_pc1_end + 1
    assert legendary_indices[1] == idx_pc2_end + 1
    # ...but never after the boss's own turn.
    assert "legendary_action:boss" not in fired[fired.index("action:boss") :]


def test_legendary_and_lair_windows_actually_fire_and_spend_resources() -> None:
    """End-to-end demonstration: a legendary creature's 3-per-round pool is
    spent exactly at its legendary windows, and a lair effect fires exactly
    once at the top of the round — both driven purely by subscribing to
    the window ids this module publishes, no simulator special case."""
    size = 10
    legendary_pool = ResourcePool("legendary", np.full(size, 3.0))
    lair_fires = [0]
    legendary_fires = [0]

    bus = EventBus()

    def on_legendary(event: Event) -> None:
        mask = ~legendary_pool.depleted()
        legendary_pool.spend(np.ones(int(mask.sum())), mask)
        legendary_fires[0] += 1

    def on_lair(event: Event) -> None:
        lair_fires[0] += 1

    bus.subscribe("legendary_action:boss", on_legendary)
    bus.subscribe("lair_action", on_lair)

    timeline = build_round_timeline(
        ["pc-1", "pc-2", "boss"], legendary_ids=frozenset({"boss"}), has_lair=True
    )
    run_round(timeline, bus, round_num=1)

    assert lair_fires[0] == 1
    assert legendary_fires[0] == 2  # once after pc-1's turn, once after pc-2's turn
    assert legendary_pool.current.tolist() == [1.0] * size  # 3 - 2 spent = 1 left


def test_event_payload_carries_round_number() -> None:
    timeline = build_round_timeline(["pc-1"])
    bus = EventBus()
    seen_rounds: list[int] = []
    bus.subscribe("action:pc-1", lambda event: seen_rounds.append(event.payload["round"]))
    run_round(timeline, bus, round_num=5)
    assert seen_rounds == [5]
