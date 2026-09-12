"""Range-band positional model (issue #47) — one signed integer band per
combatant, batched per :class:`~dndsim.core.universe.UniverseBatch` universe
(ADR-0011), never a grid. Every per-combatant quantity that can diverge
across a Monte-Carlo batch (band, movement remaining, tallies) is a
``(size,)`` numpy array rather than a scalar field on one object.

The battlefield is a line of :data:`BAND_FT`-ft bands. Party combatants
deploy at negative positions, enemies at positive ones (:data:`FORMATIONS`);
same band = contact (:data:`CONTACT_FT`), otherwise separation is
``BAND_FT`` per band of difference. Same-side allies have no relative
position — an AoE never catches allies, a named non-goal, not an accident.

Opportunity attacks ride the existing reaction machinery
(:mod:`dndsim.rules.dnd5e_2014.reactions`) rather than new machinery, per
issue #45's note: :func:`apply_move` publishes one
:class:`~dndsim.core.events.Event` per band a mover leaves, and
:func:`register_opportunity_attack` is an ordinary
:func:`~dndsim.rules.dnd5e_2014.reactions.register_reaction` subscription
against that event, gated by the reactor's own reaction
:class:`~dndsim.core.resources.ResourcePool` exactly like any other
reaction.

Every positional constant and predicate lives here; nothing else in this
Rules pack may hardcode a distance (mirrors the reference file's own
top-of-file claim).
"""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Literal

import numpy as np

from dndsim.core.events import Event, EventBus
from dndsim.core.resources import ResourcePool
from dndsim.rules.dnd5e_2014.reactions import ReactionBinding, ReactionHandler, register_reaction

Side = Literal["party", "enemy"]

BAND_FT = 30
CONTACT_FT = 5
MAX_POS = 3

_SPEED_FT_RE = re.compile(r"(\d+)\s*ft", re.IGNORECASE)

#: Deployment ``(party_band, enemy_band)`` — party spawns at ``-party_band``,
#: enemy at ``+enemy_band``. ``engaged`` (both 0, everyone in contact)
#: reproduces the pre-band engine's behavior and is the default.
FORMATIONS: dict[str, tuple[int, int]] = {
    "engaged": (0, 0),
    "skirmish": (1, 1),
    "ranged": (2, 1),
}


def deployment_band(side: Side, formation: str, *, start_band: int | None = None) -> int:
    """One combatant's signed starting band.

    ``start_band`` (an authored ``sim.position.start_band``, 0..3) overrides
    the side's formation band when present — README § Range bands: "A
    combatant's own `sim.position: { start_band: 0..3 }` overrides its
    side's formation band." The sign still follows ``side``: party bands are
    negative, enemy bands positive.
    """
    if formation not in FORMATIONS:
        raise ValueError(f"unknown formation {formation!r} — expected one of {sorted(FORMATIONS)}")
    party_band, enemy_band = FORMATIONS[formation]
    band = start_band if start_band is not None else (party_band if side == "party" else enemy_band)
    return -band if side == "party" else band


def deployment_positions(
    side: Side, formation: str, size: int, *, start_band: int | None = None
) -> np.ndarray:
    """A ``(size,)`` array of one combatant's starting band, identical across
    every universe (deployment is not itself randomized)."""
    return np.full(size, deployment_band(side, formation, start_band=start_band), dtype=np.int64)


def separation_ft(pos_a: np.ndarray, pos_b: np.ndarray) -> np.ndarray:
    """Feet between two combatants, per universe: contact (``CONTACT_FT``)
    in the same band, else ``BAND_FT`` per band of difference."""
    bands = np.abs(pos_a - pos_b)
    return np.where(bands == 0, CONTACT_FT, bands * BAND_FT)


def parse_speed_ft(speed: str | None) -> int | None:
    """Parse a statblock ``speed`` string (``"30 ft."``, ``"35 ft., fly 45
    ft."``) into walking-or-flying feet — a flier uses its fly speed.
    Returns ``None`` when nothing parses (caller defaults to 30, RAW
    humanoid walk)."""
    if speed is None:
        return None
    numbers = [int(m.group(1)) for m in _SPEED_FT_RE.finditer(speed)]
    if not numbers:
        return None
    return max(numbers)


def bands_per_turn(
    speed_ft: int,
    *,
    grappled: np.ndarray,
    restrained: np.ndarray,
    prone: np.ndarray,
    speed_halved: np.ndarray,
    speed_reduced_10: np.ndarray | None = None,
) -> np.ndarray:
    """Whole bands this combatant may move on its turn, per universe. Any
    positive speed moves at least one band (a 25-ft dwarf still crosses the
    field); grappled/restrained/prone zero it (RAW speed 0; standing from
    prone costs the band at 30 ft). ``speed_reduced_10`` (issue #71: Weapon
    Mastery's Slow property, a flat -10 ft never exceeded even by multiple
    hits) is applied first, floored at 0; ``speed_halved`` then halves
    whatever remains — 5e's general modifier-ordering rule, flat before
    multiplicative. ``speed_reduced_10=None`` (every pre-existing call site)
    reproduces the prior formula exactly."""
    base = (
        np.where(speed_reduced_10, max(speed_ft - 10, 0), speed_ft)
        if speed_reduced_10 is not None
        else np.full(speed_halved.shape, speed_ft, dtype=np.int64)
    )
    effective = np.where(speed_halved, base // 2, base)
    bands = np.where(effective <= 0, 0, np.maximum(1, effective // BAND_FT))
    zeroed = grappled | restrained | prone
    return np.where(zeroed, 0, bands).astype(np.int64)


def required_move_bands(
    *,
    pos_actor: np.ndarray,
    pos_target: np.ndarray,
    melee: bool,
    reach_ft: float | None,
    range_ft: float | None,
) -> np.ndarray:
    """Bands of movement needed, per universe, before an action is usable
    against a target — 0 when already usable. A ranged action whose prose
    declared no range is unlimited (compat hatch for unmigrated pages),
    matching the reference's ``range === undefined`` branch."""
    diff = np.abs(pos_actor - pos_target)
    if melee:
        reach = reach_ft if reach_ft is not None else CONTACT_FT
        reach_bands = int(reach // BAND_FT) if reach >= BAND_FT else 0
        needed: np.ndarray = np.maximum(0, diff - reach_bands)
        return needed
    if range_ft is None:
        return np.zeros_like(diff)
    range_bands = int(range_ft // BAND_FT)
    needed = np.maximum(0, diff - range_bands)
    return needed


def range_check(
    *,
    pos_actor: np.ndarray,
    pos_target: np.ndarray,
    melee: bool,
    reach_ft: float | None,
    range_ft: float | None,
    range_long_ft: float | None,
    hostile_adjacent: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Is an action usable from the current separation, and at what
    disadvantage, per universe? ``hostile_adjacent`` = a living opponent
    shares the actor's band (RAW: ranged attacks within 5 ft of a hostile
    are at disadvantage, both eras). Long range (``range < sep <=
    range_long``) is disadvantage too. Returns ``(usable, disadvantage)`` —
    ``disadvantage`` counts stacking sources (0/1/2), collapsed to one mode
    by :func:`~dndsim.rules.dnd5e_2014.advantage.collapse_advantage`."""
    sep = separation_ft(pos_actor, pos_target)
    size = sep.shape[0]
    if melee:
        reach = reach_ft if reach_ft is not None else CONTACT_FT
        return sep <= reach, np.zeros(size, dtype=np.int64)
    disadvantage = hostile_adjacent.astype(np.int64)
    if range_ft is None:
        return np.ones(size, dtype=np.bool_), disadvantage
    usable = sep <= range_ft
    if range_long_ft is not None:
        long_band = (sep > range_ft) & (sep <= range_long_ft)
        usable = usable | long_band
        disadvantage = disadvantage + long_band.astype(np.int64)
    return usable, disadvantage


def hostile_adjacent_mask(
    actor_pos: np.ndarray, opponent_positions: list[np.ndarray], opponent_alive: list[np.ndarray]
) -> np.ndarray:
    """A living opponent shares the actor's band, per universe — RAW
    ranged-attack disadvantage within 5 ft of a hostile."""
    out = np.zeros(actor_pos.shape[0], dtype=np.bool_)
    for pos, alive in zip(opponent_positions, opponent_alive, strict=True):
        out |= alive & (pos == actor_pos)
    return out


def nearest_living_band(
    actor_pos: np.ndarray, target_positions: list[np.ndarray], target_alive: list[np.ndarray]
) -> tuple[np.ndarray, np.ndarray]:
    """The nearest living opponent's band, per universe, for closing when
    nothing is reachable this turn — the "spend the movement closing on the
    nearest opponent so the fight still converges" behavior. Ties break
    toward the first target in ``target_positions``' declared order.
    Returns ``(nearest_band, has_any_living)``; a universe with
    ``has_any_living`` false has no valid ``nearest_band`` and the caller
    must not act on it."""
    size = actor_pos.shape[0]
    best_pos = np.zeros(size, dtype=np.int64)
    best_dist = np.full(size, np.iinfo(np.int64).max, dtype=np.int64)
    has_any = np.zeros(size, dtype=np.bool_)
    for pos, alive in zip(target_positions, target_alive, strict=True):
        dist = np.abs(pos - actor_pos)
        better = alive & (dist < best_dist)
        best_pos = np.where(better, pos, best_pos)
        best_dist = np.where(better, dist, best_dist)
        has_any = has_any | alive
    return best_pos, has_any


def kite_destination(side: Side, actor_pos: np.ndarray) -> np.ndarray:
    """One band away from the actor's opposing line — the "ranged attacker
    sharing a band with a living melee threat withdraws one band" behavior.
    Party withdraws toward more-negative bands, enemy toward more-positive,
    clamped to ``MAX_POS``."""
    step = -1 if side == "party" else 1
    clipped: np.ndarray = np.clip(actor_pos + step, -MAX_POS, MAX_POS)
    return clipped


def step_toward(pos: np.ndarray, dest: np.ndarray) -> np.ndarray:
    """One band step from ``pos`` toward ``dest`` per universe (unchanged
    where already equal)."""
    stepped: np.ndarray = pos + np.sign(dest - pos)
    return stepped


# --- opportunity attacks: an ordinary reaction, not new machinery ----------


def leave_band_event(mover_id: str) -> str:
    """The trigger name :func:`apply_move` publishes each band a mover
    leaves — one reactor may :func:`register_opportunity_attack` against
    it per mover it threatens."""
    return f"position:leaves_band:{mover_id}"


def publish_band_departure(
    bus: EventBus, mover_id: str, *, round_num: int, mask: np.ndarray, from_pos: np.ndarray
) -> None:
    """Publish one band-departure event for the universes in ``mask``,
    naming the band each was leaving (``from_pos``) — the payload a
    registered opportunity-attack reaction reads via ``eligible``."""
    bus.publish(
        Event(
            name=leave_band_event(mover_id),
            payload={"round": round_num, "mask": mask, "from_pos": from_pos},
        )
    )


def register_opportunity_attack(
    bus: EventBus,
    *,
    mover_id: str,
    pool: ResourcePool,
    reactor_pos: np.ndarray,
    reactor_alive: np.ndarray,
    reactor_melee_capable: np.ndarray,
    reactor_incapacitated: np.ndarray,
    handler: ReactionHandler,
) -> ReactionBinding:
    """Subscribe one reactor's opportunity attack against ``mover_id``'s
    departures, gated by the reactor's own reaction pool
    (:func:`~dndsim.rules.dnd5e_2014.reactions.make_reaction_pool`) — an
    ordinary :func:`~dndsim.rules.dnd5e_2014.reactions.register_reaction`
    call, per issue #45's note that an opportunity attack needs no new
    machinery. Eligible exactly in the universes that are (a) actually
    leaving this band (``mask``), (b) the reactor is alive, melee-capable,
    and not incapacitated in, and (c) the reactor currently shares the
    mover's departing band (``reactor_pos == from_pos``)."""

    def eligible(event: Event) -> np.ndarray:
        payload = event.payload
        mask: np.ndarray = payload["mask"]
        from_pos: np.ndarray = payload["from_pos"]
        eligible_mask: np.ndarray = (
            mask
            & reactor_alive
            & reactor_melee_capable
            & ~reactor_incapacitated
            & (reactor_pos == from_pos)
        )
        return eligible_mask

    return register_reaction(
        bus, trigger=leave_band_event(mover_id), pool=pool, eligible=eligible, handler=handler
    )


def apply_move(
    bus: EventBus,
    *,
    mover_id: str,
    pos: np.ndarray,
    dest: np.ndarray,
    budget: np.ndarray,
    round_num: int,
    disengaged: np.ndarray | None = None,
    alive: Callable[[], np.ndarray] | None = None,
) -> None:
    """Move ``pos`` toward ``dest`` one band at a time, up to ``budget``
    bands, mutating both ``pos`` and ``budget`` in place. Before each band a
    universe leaves, publishes :func:`leave_band_event` so every registered
    :func:`register_opportunity_attack` reactor gets a chance to fire —
    unless that universe disengaged this turn (``disengaged``). ``alive`` is
    an optional zero-argument getter re-checked after each departure event
    (an opportunity attack may drop the mover mid-move, matching the
    reference's "stops early if an OA drops the mover"); universes it
    reports as dead stop moving immediately, without spending further
    budget."""
    size = pos.shape[0]
    disengaged_mask = disengaged if disengaged is not None else np.zeros(size, dtype=np.bool_)
    alive_fn = alive if alive is not None else (lambda: np.ones(size, dtype=np.bool_))
    while True:
        active = (pos != dest) & (budget > 0) & alive_fn()
        if not bool(active.any()):
            return
        provoking = active & ~disengaged_mask
        if bool(provoking.any()):
            publish_band_departure(
                bus, mover_id, round_num=round_num, mask=provoking, from_pos=pos.copy()
            )
        active = active & alive_fn()
        step = np.sign(dest - pos)
        pos[:] = np.where(active, pos + step, pos)
        budget[:] = np.where(active, budget - 1, budget)


# --- AoE capacity: a shape's stated size caps how many it catches ----------


def aoe_capacity(*, radius_ft: int | None = None, cone_ft: int | None = None) -> int | None:
    """How many creatures an AoE of this parsed shape can catch in one band,
    keyed on the radius/cone size the prose actually stated. ``None`` for a
    shapeless area — the caller falls back to the half-the-side
    abstraction (:func:`aoe_targets`)."""
    ft = radius_ft if radius_ft is not None else cone_ft
    if ft is None:
        return None
    if ft >= 30:
        return 10
    if ft >= 20:
        return 6
    if ft >= 15:
        return 4
    if ft >= 10:
        return 2
    return 1


def aoe_targets(
    *,
    positions: dict[str, np.ndarray],
    alive: dict[str, np.ndarray],
    capacity: int | None,
    size: int,
    radius_ft: int = 0,
) -> dict[str, np.ndarray]:
    """Per universe, which of ``positions``' target ids an area action
    actually catches: the reachable band with the most living opponents, up
    to ``capacity``, spilling into an adjacent band only when ``radius_ft``
    is 20+ (a Fireball reaches two bands; a 15-ft cone does not). A
    shapeless area (``capacity is None``) keeps the pre-band abstraction:
    half the living opponents, rounded up, taken in ``positions``'
    declared order.

    Ties for "densest band" break toward the lowest band number — a
    deliberate, documented divergence from the reference engine's Map-
    insertion-order tiebreak (this engine is not required to reproduce that
    arbitrary a choice bit-for-bit; ADR-0007/0011 make no ordering
    guarantee about insertion order across a batched, vectorized band
    count).

    Returns ``{target_id: (size,) bool array}`` — ``True`` where that
    target is caught in that universe.
    """
    ids = list(positions)
    if not ids:
        return {}

    if capacity is None:
        alive_count = np.zeros(size, dtype=np.int64)
        for i in ids:
            alive_count += alive[i].astype(np.int64)
        half = np.ceil(alive_count / 2).astype(np.int64)
        caught: dict[str, np.ndarray] = {}
        running = np.zeros(size, dtype=np.int64)
        for i in ids:
            take = alive[i] & (running < half)
            caught[i] = take
            running = running + take.astype(np.int64)
        return caught

    band_values = list(range(-MAX_POS, MAX_POS + 1))
    counts = np.zeros((len(band_values), size), dtype=np.int64)
    for i in ids:
        pos_i = positions[i]
        alive_i = alive[i]
        for b_idx, band in enumerate(band_values):
            counts[b_idx] += alive_i & (pos_i == band)
    best_idx = np.argmax(counts, axis=0)
    best_band = np.asarray(band_values, dtype=np.int64)[best_idx]

    caught = {i: np.zeros(size, dtype=np.bool_) for i in ids}
    remaining = np.full(size, capacity, dtype=np.int64)
    for i in ids:
        take = alive[i] & (positions[i] == best_band) & (remaining > 0)
        caught[i] = take
        remaining = remaining - take.astype(np.int64)
    if radius_ft >= 20:
        for i in ids:
            spill = alive[i] & (np.abs(positions[i] - best_band) == 1) & (remaining > 0)
            caught[i] = caught[i] | spill
            remaining = remaining - spill.astype(np.int64)
    return caught


# --- reported positional figures --------------------------------------------


@dataclass(slots=True)
class PositionTally:
    """Per-universe counts of the positional figures the reference engine
    reports (``turnsNoTargetMean``/``opportunityAttacksMean``) — one
    instance per combatant, mirroring
    :class:`~dndsim.rules.dnd5e_2014.reactions.ResourcePool`'s per-universe
    shape rather than a scalar counter."""

    turns_no_target: np.ndarray
    opportunity_attacks: np.ndarray

    @classmethod
    def zeros(cls, size: int) -> PositionTally:
        return cls(
            turns_no_target=np.zeros(size, dtype=np.int64),
            opportunity_attacks=np.zeros(size, dtype=np.int64),
        )

    def record_turn_no_target(self, mask: np.ndarray) -> None:
        """A combatant spent its turn closing rather than acting, in every
        universe in ``mask`` — never silently: this is the counter that
        proves it happened rather than dropping the turn on the floor."""
        self.turns_no_target += mask.astype(np.int64)

    def record_opportunity_attack(self, mask: np.ndarray) -> None:
        self.opportunity_attacks += mask.astype(np.int64)

    def mean_turns_no_target(self) -> float:
        return float(self.turns_no_target.mean())

    def mean_opportunity_attacks(self) -> float:
        return float(self.opportunity_attacks.mean())


@dataclass(slots=True)
class PositionState:
    """One combatant's batched positional state across a
    :class:`~dndsim.core.universe.UniverseBatch`: current band, this turn's
    remaining movement budget, and its running positional tally. Bundled
    together because every caller that moves a combatant needs all three in
    lockstep — ``pos``/``budget`` mutate together inside :func:`apply_move`,
    and ``tally`` records the outcome of the same decision."""

    pos: np.ndarray
    budget: np.ndarray
    tally: PositionTally = field(default_factory=lambda: PositionTally.zeros(0))

    @classmethod
    def deploy(
        cls, side: Side, formation: str, size: int, *, start_band: int | None = None
    ) -> PositionState:
        return cls(
            pos=deployment_positions(side, formation, size, start_band=start_band),
            budget=np.zeros(size, dtype=np.int64),
            tally=PositionTally.zeros(size),
        )

    def start_turn(
        self,
        speed_ft: int,
        *,
        grappled: np.ndarray,
        restrained: np.ndarray,
        prone: np.ndarray,
        speed_halved: np.ndarray,
        speed_reduced_10: np.ndarray | None = None,
    ) -> None:
        """Refresh this turn's movement budget via :func:`bands_per_turn` —
        this module owns no condition vocabulary of its own (the caller
        supplies each mask from :mod:`dndsim.rules.dnd5e_2014.conditions`'s
        batched forms, or issue #71's own Weapon Mastery tag)."""
        self.budget = bands_per_turn(
            speed_ft,
            grappled=grappled,
            restrained=restrained,
            prone=prone,
            speed_halved=speed_halved,
            speed_reduced_10=speed_reduced_10,
        )
