"""The 5e round structure as a core :class:`~dndsim.core.timeline.Timeline`:
one phase per participant's turn, a legendary-action window inserted after
every OTHER participant's turn, and an optional lair-action window at the
top of the round — all fired purely by walking
:class:`~dndsim.core.timeline.Window` ids and publishing
:class:`~dndsim.core.events.Event`\\ s on the shared
:class:`~dndsim.core.events.EventBus`, never as a simulator special case
(issue #45's "expressed as core Timeline windows" acceptance criterion).

A legendary or lair handler is nothing more than an ordinary
:meth:`~dndsim.core.events.EventBus.subscribe` against the window id this
module names (`legendary_action:<id>`, `lair_action`) — resource-gating a
legendary creature's 3-per-round pool, or a lair's damage, is the
subscriber's own business, exactly like a reaction's own
:mod:`~dndsim.rules.dnd5e_2014.reactions` gating.
"""

from __future__ import annotations

from dndsim.core.events import Event, EventBus
from dndsim.core.timeline import Phase, Timeline, Window

START_OF_TURN = "start_of_turn"
ACTION = "action"
END_OF_TURN = "end_of_turn"
LEGENDARY_ACTION = "legendary_action"
LAIR_ACTION = "lair_action"
END_OF_ROUND = "end_of_round"


def build_round_timeline(
    turn_order: list[str],
    *,
    legendary_ids: frozenset[str] = frozenset(),
    has_lair: bool = False,
) -> Timeline:
    """One round: an optional lair-action window at the top (5e RAW: a lair
    action acts on initiative count 20, losing ties — i.e. before anyone's
    turn), then each participant's own turn phase
    (`start_of_turn:<id>`/`action:<id>`/`end_of_turn:<id>` windows), with a
    legendary-action window for every OTHER legendary participant inserted
    immediately after that turn phase — legendary actions fire "at the end
    of another creature's turn" (5e RAW), never on the legendary creature's
    own turn."""
    phases: list[Phase] = []
    if has_lair:
        phases.append(Phase("lair", (Window(LAIR_ACTION),)))
    for actor_id in turn_order:
        phases.append(
            Phase(
                f"turn:{actor_id}",
                (
                    Window(f"{START_OF_TURN}:{actor_id}"),
                    Window(f"{ACTION}:{actor_id}"),
                    Window(f"{END_OF_TURN}:{actor_id}"),
                ),
            )
        )
        others = [lid for lid in legendary_ids if lid != actor_id]
        if others:
            phases.append(
                Phase(
                    f"legendary_after:{actor_id}",
                    tuple(Window(f"{LEGENDARY_ACTION}:{lid}") for lid in others),
                )
            )
    phases.append(Phase("round_end", (Window(END_OF_ROUND),)))
    return Timeline(tuple(phases))


def run_round(timeline: Timeline, bus: EventBus, *, round_num: int) -> list[str]:
    """Walk every window in `timeline` in order, publishing one `Event` per
    window whose `name` is the window's own id and whose `payload` carries
    `round_num`. A legendary or lair handler subscribed by window id fires
    exactly in its own window and nowhere else — the entire mechanism by
    which "legendary and lair actions fire in their windows" holds, with no
    branch anywhere naming "legendary" or "lair" outside this construction.
    Returns the ordered list of window ids actually published, so a test or
    caller can assert firing order/coverage without inspecting bus
    internals."""
    fired: list[str] = []
    for phase in timeline:
        for window in phase:
            bus.publish(Event(name=window.id, payload={"round": round_num}))
            fired.append(window.id)
    return fired
