from __future__ import annotations

import numpy as np

from dndsim.core.events import Event, EventBus
from dndsim.core.resources import ResourcePool
from dndsim.rules.dnd5e_2014.position import (
    BAND_FT,
    CONTACT_FT,
    FORMATIONS,
    MAX_POS,
    PositionState,
    PositionTally,
    aoe_capacity,
    aoe_targets,
    apply_move,
    bands_per_turn,
    deployment_band,
    deployment_positions,
    hostile_adjacent_mask,
    kite_destination,
    leave_band_event,
    nearest_living_band,
    parse_speed_ft,
    range_check,
    register_opportunity_attack,
    required_move_bands,
    separation_ft,
    step_toward,
)
from dndsim.rules.dnd5e_2014.reactions import make_reaction_pool

# --- formations / deployment -------------------------------------------------


def test_engaged_formation_is_everyone_in_contact() -> None:
    assert FORMATIONS["engaged"] == (0, 0)
    party = deployment_band("party", "engaged")
    enemy = deployment_band("enemy", "engaged")
    assert party == 0
    assert enemy == 0


def test_skirmish_and_ranged_formations_open_separation() -> None:
    assert deployment_band("party", "skirmish") == -1
    assert deployment_band("enemy", "skirmish") == 1
    assert deployment_band("party", "ranged") == -2
    assert deployment_band("enemy", "ranged") == 1


def test_start_band_override_replaces_formation_band_but_keeps_side_sign() -> None:
    assert deployment_band("party", "ranged", start_band=0) == 0
    assert deployment_band("enemy", "engaged", start_band=3) == 3
    assert deployment_band("party", "engaged", start_band=3) == -3


def test_deployment_positions_is_uniform_across_the_batch() -> None:
    pos = deployment_positions("party", "skirmish", size=5)
    assert pos.tolist() == [-1, -1, -1, -1, -1]


# --- separation / movement ---------------------------------------------------


def test_separation_ft_is_contact_in_same_band_else_30ft_per_band() -> None:
    a = np.array([0, 0, -1, 2])
    b = np.array([0, 2, 1, -1])
    assert separation_ft(a, b).tolist() == [CONTACT_FT, 2 * BAND_FT, 2 * BAND_FT, 3 * BAND_FT]


def test_parse_speed_ft_takes_the_max_of_every_ft_number_and_defaults_none() -> None:
    assert parse_speed_ft("30 ft.") == 30
    assert parse_speed_ft("35 ft., fly 45 ft.") == 45
    assert parse_speed_ft(None) is None
    assert parse_speed_ft("unknown") is None


def test_bands_per_turn_is_at_least_one_for_any_positive_speed() -> None:
    size = 3
    none_mask = np.zeros(size, dtype=np.bool_)
    bands = bands_per_turn(
        25, grappled=none_mask, restrained=none_mask, prone=none_mask, speed_halved=none_mask
    )
    assert bands.tolist() == [1, 1, 1]


def test_bands_per_turn_zeroed_by_grappled_restrained_or_prone() -> None:
    size = 3
    grappled = np.array([True, False, False])
    restrained = np.array([False, True, False])
    prone = np.array([False, False, True])
    none_mask = np.zeros(size, dtype=np.bool_)
    bands = bands_per_turn(
        30, grappled=grappled, restrained=restrained, prone=prone, speed_halved=none_mask
    )
    assert bands.tolist() == [0, 0, 0]


def test_speed_halved_halves_before_the_band_floor() -> None:
    size = 1
    none_mask = np.zeros(size, dtype=np.bool_)
    halved = np.ones(size, dtype=np.bool_)
    # 60 ft halved to 30 -> still 1 band; 90 ft halved to 45 -> still 1 band
    bands_60 = bands_per_turn(
        60, grappled=none_mask, restrained=none_mask, prone=none_mask, speed_halved=halved
    )
    bands_90 = bands_per_turn(
        90, grappled=none_mask, restrained=none_mask, prone=none_mask, speed_halved=halved
    )
    assert bands_60.tolist() == [1]
    assert bands_90.tolist() == [1]


def test_speed_reduced_10_zeroes_a_low_base_speed_before_the_band_floor() -> None:
    # issue #71: Weapon Mastery's Slow property — a flat -10 ft, not a
    # halving. 10 ft base speed (a Sprite-scale creature) reduced by 10
    # zeroes it; the same 10 ft with the tag absent still floors to 1 band
    # (bands_per_turn's own "any positive speed moves at least one band"
    # rule) — the SAME base speed must diverge only on the flag.
    size = 1
    none_mask = np.zeros(size, dtype=np.bool_)
    reduced = np.ones(size, dtype=np.bool_)
    bands_reduced = bands_per_turn(
        10,
        grappled=none_mask,
        restrained=none_mask,
        prone=none_mask,
        speed_halved=none_mask,
        speed_reduced_10=reduced,
    )
    bands_unreduced = bands_per_turn(
        10, grappled=none_mask, restrained=none_mask, prone=none_mask, speed_halved=none_mask
    )
    assert bands_reduced.tolist() == [0]
    assert bands_unreduced.tolist() == [1]


def test_speed_reduced_10_is_a_flat_subtraction_applied_before_halving() -> None:
    # 5e's general modifier-ordering rule: flat reductions apply before a
    # halving. At 20 ft base speed with both active, (20 - 10) // 2 = 5 ->
    # still 1 band (any positive speed floors to at least one); halving
    # first would give 20 // 2 - 10 = 0 -> zero bands. The two orders
    # disagree at this speed, so this proves which order actually ran.
    size = 1
    both = np.ones(size, dtype=np.bool_)
    bands = bands_per_turn(
        20,
        grappled=np.zeros(size, dtype=np.bool_),
        restrained=np.zeros(size, dtype=np.bool_),
        prone=np.zeros(size, dtype=np.bool_),
        speed_halved=both,
        speed_reduced_10=both,
    )
    assert bands.tolist() == [1]


def test_speed_reduced_10_absent_matches_prior_behavior_exactly() -> None:
    # Backward compatibility: every existing call site that never passes
    # speed_reduced_10 keeps its exact prior numbers.
    size = 2
    none_mask = np.zeros(size, dtype=np.bool_)
    bands = bands_per_turn(
        30, grappled=none_mask, restrained=none_mask, prone=none_mask, speed_halved=none_mask
    )
    assert bands.tolist() == [1, 1]


def test_step_toward_moves_one_band_and_stops_when_equal() -> None:
    pos = np.array([0, 2, -2])
    dest = np.array([3, 2, 0])
    assert step_toward(pos, dest).tolist() == [1, 2, -1]


# --- reach/range gating -------------------------------------------------------


def test_required_move_bands_is_zero_when_already_in_reach() -> None:
    actor = np.array([0])
    target = np.array([0])
    needed = required_move_bands(
        pos_actor=actor, pos_target=target, melee=True, reach_ft=5, range_ft=None
    )
    assert needed.tolist() == [0]


def test_required_move_bands_counts_bands_beyond_melee_reach() -> None:
    actor = np.array([0])
    target = np.array([2])
    needed = required_move_bands(
        pos_actor=actor, pos_target=target, melee=True, reach_ft=5, range_ft=None
    )
    assert needed.tolist() == [2]


def test_required_move_bands_undeclared_range_is_unlimited() -> None:
    actor = np.array([0])
    target = np.array([3])
    needed = required_move_bands(
        pos_actor=actor, pos_target=target, melee=False, reach_ft=None, range_ft=None
    )
    assert needed.tolist() == [0]


def test_range_check_melee_usable_within_reach_no_disadvantage() -> None:
    actor = np.array([0, 0])
    target = np.array([0, 1])
    usable, dis = range_check(
        pos_actor=actor,
        pos_target=target,
        melee=True,
        reach_ft=5,
        range_ft=None,
        range_long_ft=None,
        hostile_adjacent=np.zeros(2, dtype=np.bool_),
    )
    assert usable.tolist() == [True, False]
    assert dis.tolist() == [0, 0]


def test_range_check_ranged_hostile_adjacent_imposes_disadvantage() -> None:
    actor = np.array([0])
    target = np.array([2])
    usable, dis = range_check(
        pos_actor=actor,
        pos_target=target,
        melee=False,
        reach_ft=None,
        range_ft=90,
        range_long_ft=None,
        hostile_adjacent=np.array([True]),
    )
    assert usable.tolist() == [True]
    assert dis.tolist() == [1]


def test_range_check_long_range_adds_disadvantage_and_stays_usable() -> None:
    actor = np.array([0])
    target = np.array([3])  # 90 ft
    usable, dis = range_check(
        pos_actor=actor,
        pos_target=target,
        melee=False,
        reach_ft=None,
        range_ft=60,
        range_long_ft=90,
        hostile_adjacent=np.zeros(1, dtype=np.bool_),
    )
    assert usable.tolist() == [True]
    assert dis.tolist() == [1]


def test_range_check_beyond_long_range_is_unusable() -> None:
    actor = np.array([0])
    target = np.array([3])  # 90 ft
    usable, _dis = range_check(
        pos_actor=actor,
        pos_target=target,
        melee=False,
        reach_ft=None,
        range_ft=30,
        range_long_ft=60,
        hostile_adjacent=np.zeros(1, dtype=np.bool_),
    )
    assert usable.tolist() == [False]


def test_hostile_adjacent_mask_true_only_when_a_living_opponent_shares_the_band() -> None:
    actor = np.array([0, 1])
    opp_pos = [np.array([0, 2])]
    opp_alive = [np.array([True, True])]
    mask = hostile_adjacent_mask(actor, opp_pos, opp_alive)
    assert mask.tolist() == [True, False]


# --- closing on no reachable target / kiting ---------------------------------


def test_nearest_living_band_picks_the_closest_living_target_per_universe() -> None:
    actor = np.array([0, 0])
    targets = [np.array([3, 3]), np.array([1, 1])]
    alive = [np.array([True, False]), np.array([True, True])]
    nearest, has_any = nearest_living_band(actor, targets, alive)
    # universe 0: both alive, target 2 (band 1) is closer than target 1 (band 3)
    # universe 1: only target 2 alive -> band 1
    assert nearest.tolist() == [1, 1]
    assert has_any.tolist() == [True, True]


def test_nearest_living_band_reports_no_living_target() -> None:
    actor = np.array([0])
    targets = [np.array([2])]
    alive = [np.array([False])]
    _nearest, has_any = nearest_living_band(actor, targets, alive)
    assert has_any.tolist() == [False]


def test_a_combatant_with_no_reachable_target_closes_instead_of_wasting_the_turn() -> None:
    """Acceptance criterion: closing, not a silently wasted turn."""
    actor_pos = np.array([0])
    targets = [np.array([3])]
    alive = [np.array([True])]
    nearest, has_any = nearest_living_band(actor_pos, targets, alive)
    assert bool(has_any[0])
    tally = PositionTally.zeros(1)
    tally.record_turn_no_target(has_any)
    budget = np.array([2])
    bus = EventBus()
    apply_move(bus, mover_id="actor", pos=actor_pos, dest=nearest, budget=budget, round_num=1)
    assert actor_pos.tolist() == [2]  # closed as far as its 2-band budget allowed
    assert tally.turns_no_target.tolist() == [1]


def test_kite_destination_steps_one_band_away_from_the_opposing_line_and_clamps() -> None:
    assert kite_destination("party", np.array([0])).tolist() == [-1]
    assert kite_destination("enemy", np.array([0])).tolist() == [1]
    assert kite_destination("enemy", np.array([MAX_POS])).tolist() == [MAX_POS]
    assert kite_destination("party", np.array([-MAX_POS])).tolist() == [-MAX_POS]


# --- opportunity attacks: ride the reaction machinery -------------------------


def test_opportunity_attack_fires_on_provoking_movement() -> None:
    """Acceptance criterion: OAs trigger on the movement that provokes them."""
    size = 1
    bus = EventBus()
    pool = make_reaction_pool(size)
    fired: list[np.ndarray] = []

    register_opportunity_attack(
        bus,
        mover_id="mover",
        pool=pool,
        reactor_pos=np.array([0]),
        reactor_alive=np.array([True]),
        reactor_melee_capable=np.array([True]),
        reactor_incapacitated=np.zeros(size, dtype=np.bool_),
        handler=lambda event, mask: fired.append(mask.copy()),
    )

    pos = np.array([0])
    budget = np.array([2])
    apply_move(bus, mover_id="mover", pos=pos, dest=np.array([2]), budget=budget, round_num=1)

    assert len(fired) == 1  # only the first band-step shares a band with the reactor
    assert fired[0].tolist() == [True]
    assert pos.tolist() == [2]
    assert pool.depleted().tolist() == [True]


def test_opportunity_attack_never_fires_when_the_mover_disengaged() -> None:
    size = 1
    bus = EventBus()
    pool = make_reaction_pool(size)
    fired: list[np.ndarray] = []

    register_opportunity_attack(
        bus,
        mover_id="mover",
        pool=pool,
        reactor_pos=np.array([0]),
        reactor_alive=np.array([True]),
        reactor_melee_capable=np.array([True]),
        reactor_incapacitated=np.zeros(size, dtype=np.bool_),
        handler=lambda event, mask: fired.append(mask.copy()),
    )

    pos = np.array([0])
    budget = np.array([2])
    apply_move(
        bus,
        mover_id="mover",
        pos=pos,
        dest=np.array([2]),
        budget=budget,
        round_num=1,
        disengaged=np.array([True]),
    )

    assert fired == []
    assert not pool.depleted().any()


def test_opportunity_attack_never_fires_for_a_non_melee_or_incapacitated_reactor() -> None:
    size = 1
    bus = EventBus()
    pool = make_reaction_pool(size)
    fired: list[np.ndarray] = []
    register_opportunity_attack(
        bus,
        mover_id="mover",
        pool=pool,
        reactor_pos=np.array([0]),
        reactor_alive=np.array([True]),
        reactor_melee_capable=np.array([False]),  # e.g. a ranged-only reactor
        reactor_incapacitated=np.zeros(size, dtype=np.bool_),
        handler=lambda event, mask: fired.append(mask.copy()),
    )
    pos = np.array([0])
    apply_move(
        bus, mover_id="mover", pos=pos, dest=np.array([1]), budget=np.array([1]), round_num=1
    )
    assert fired == []


def test_opportunity_attack_reaction_pool_gates_a_second_departure_this_round() -> None:
    """A reactor with only one reaction can't OA twice — same pool budget as
    every other reaction (Shield, damage-reduction), per reactions.py."""
    size = 1
    bus = EventBus()
    pool = make_reaction_pool(size)
    fired: list[np.ndarray] = []

    def register_for(mover_id: str) -> None:
        register_opportunity_attack(
            bus,
            mover_id=mover_id,
            pool=pool,
            reactor_pos=np.array([0]),
            reactor_alive=np.array([True]),
            reactor_melee_capable=np.array([True]),
            reactor_incapacitated=np.zeros(size, dtype=np.bool_),
            handler=lambda event, mask: fired.append(mask.copy()),
        )

    # two different movers both leave the reactor's band this round.
    register_for("mover-a")
    register_for("mover-b")

    apply_move(
        bus,
        mover_id="mover-a",
        pos=np.array([0]),
        dest=np.array([1]),
        budget=np.array([1]),
        round_num=1,
    )
    apply_move(
        bus,
        mover_id="mover-b",
        pos=np.array([0]),
        dest=np.array([1]),
        budget=np.array([1]),
        round_num=1,
    )

    assert len(fired) == 1
    assert pool.depleted().tolist() == [True]


def test_apply_move_stops_early_when_alive_reports_the_mover_down() -> None:
    bus = EventBus()
    dead_after_first_step = [False]

    def alive() -> np.ndarray:
        return np.array([not dead_after_first_step[0]])

    bus.subscribe(
        leave_band_event("mover"), lambda event: dead_after_first_step.__setitem__(0, True)
    )

    pos = np.array([0])
    budget = np.array([3])
    apply_move(
        bus, mover_id="mover", pos=pos, dest=np.array([3]), budget=budget, round_num=1, alive=alive
    )
    assert pos.tolist() == [0]  # dropped before completing even the first step


# --- AoE capacity respects formation -----------------------------------------


def test_aoe_capacity_scales_with_stated_radius() -> None:
    assert aoe_capacity(radius_ft=5) == 1
    assert aoe_capacity(radius_ft=10) == 2
    assert aoe_capacity(radius_ft=15) == 4
    assert aoe_capacity(radius_ft=20) == 6
    assert aoe_capacity(radius_ft=30) == 10
    assert aoe_capacity(cone_ft=15) == 4
    assert aoe_capacity() is None


def test_aoe_capacity_caps_a_clustered_formation_below_its_full_group_size() -> None:
    """Acceptance criterion: capacity differs by formation (clustered vs spread)."""
    size = 1
    # engaged: everyone in band 0 (clustered)
    clustered = {
        "e1": np.array([0]),
        "e2": np.array([0]),
        "e3": np.array([0]),
    }
    alive = {k: np.ones(size, dtype=np.bool_) for k in clustered}
    capacity = aoe_capacity(radius_ft=10)  # a 10-ft burst catches 2
    caught = aoe_targets(positions=clustered, alive=alive, capacity=capacity, size=size)
    assert sum(bool(caught[k][0]) for k in clustered) == 2


def test_aoe_capacity_catches_fewer_when_the_formation_is_spread_across_bands() -> None:
    """Same burst, same three targets, spread one-per-band (ranged/skirmish
    formation shape) -> the densest single band has only one target."""
    size = 1
    spread = {
        "e1": np.array([0]),
        "e2": np.array([1]),
        "e3": np.array([2]),
    }
    alive = {k: np.ones(size, dtype=np.bool_) for k in spread}
    capacity = aoe_capacity(radius_ft=10)
    caught = aoe_targets(positions=spread, alive=alive, capacity=capacity, size=size)
    assert sum(bool(caught[k][0]) for k in spread) == 1


def test_aoe_targets_spills_into_adjacent_band_only_at_20ft_plus() -> None:
    size = 1
    positions = {"a": np.array([0]), "b": np.array([1])}
    alive = {k: np.ones(size, dtype=np.bool_) for k in positions}
    capacity = aoe_capacity(radius_ft=20)
    caught_20 = aoe_targets(
        positions=positions, alive=alive, capacity=capacity, size=size, radius_ft=20
    )
    assert bool(caught_20["a"][0]) and bool(caught_20["b"][0])

    capacity_15 = aoe_capacity(radius_ft=15)
    caught_15 = aoe_targets(
        positions=positions, alive=alive, capacity=capacity_15, size=size, radius_ft=15
    )
    assert bool(caught_15["a"][0]) and not bool(caught_15["b"][0])


def test_aoe_targets_dead_targets_are_never_caught() -> None:
    size = 1
    positions = {"a": np.array([0]), "b": np.array([0])}
    alive = {"a": np.array([True]), "b": np.array([False])}
    caught = aoe_targets(positions=positions, alive=alive, capacity=10, size=size)
    assert bool(caught["a"][0])
    assert not bool(caught["b"][0])


def test_aoe_targets_shapeless_area_catches_half_the_living_rounded_up() -> None:
    size = 1
    positions = {"a": np.array([0]), "b": np.array([0]), "c": np.array([0])}
    alive = {k: np.ones(size, dtype=np.bool_) for k in positions}
    caught = aoe_targets(positions=positions, alive=alive, capacity=None, size=size)
    assert sum(bool(caught[k][0]) for k in positions) == 2  # ceil(3/2)


def test_aoe_targets_empty_positions_returns_empty() -> None:
    assert aoe_targets(positions={}, alive={}, capacity=5, size=1) == {}


# --- reported positional figures ---------------------------------------------


def test_position_tally_reports_the_positional_figures_the_old_engine_reported() -> None:
    """Acceptance criterion: positional figures appear in reported results —
    mean turns without a reachable target, mean opportunity attacks."""
    tally = PositionTally.zeros(4)
    tally.record_turn_no_target(np.array([True, False, True, False]))
    tally.record_opportunity_attack(np.array([True, True, False, False]))
    assert tally.mean_turns_no_target() == 0.5
    assert tally.mean_opportunity_attacks() == 0.5


def test_position_state_deploy_and_start_turn_round_trip() -> None:
    size = 3
    state = PositionState.deploy("enemy", "skirmish", size)
    assert state.pos.tolist() == [1, 1, 1]
    assert state.budget.tolist() == [0, 0, 0]

    none_mask = np.zeros(size, dtype=np.bool_)
    state.start_turn(
        30, grappled=none_mask, restrained=none_mask, prone=none_mask, speed_halved=none_mask
    )
    assert state.budget.tolist() == [1, 1, 1]


# --- registration plumbing ----------------------------------------------------


def test_leave_band_event_is_namespaced_per_mover() -> None:
    assert leave_band_event("goblin-1") == "position:leaves_band:goblin-1"
    assert leave_band_event("goblin-1") != leave_band_event("goblin-2")


def test_apply_move_with_no_reactors_still_moves_and_publishes_nothing_fatal() -> None:
    bus = EventBus()
    # no subscribers registered at all — publish must be a no-op, not an error
    pos = np.array([0])
    apply_move(
        bus, mover_id="lonely", pos=pos, dest=np.array([2]), budget=np.array([5]), round_num=1
    )
    assert pos.tolist() == [2]


def test_apply_move_respects_budget_even_with_no_reactors() -> None:
    pos = np.array([0])
    bus = EventBus()
    apply_move(bus, mover_id="m", pos=pos, dest=np.array([3]), budget=np.array([1]), round_num=1)
    assert pos.tolist() == [1]


def test_event_bus_publish_is_a_plain_dispatch_used_by_apply_move() -> None:
    # smoke test that Event/EventBus import path used above actually works
    bus = EventBus()
    seen: list[str] = []
    bus.subscribe("x", lambda e: seen.append(e.name))
    bus.publish(Event(name="x"))
    assert seen == ["x"]


def test_resource_pool_import_path_used_by_reaction_pool_tests_works() -> None:
    pool = ResourcePool("reaction", np.ones(2, dtype=np.float64))
    assert not pool.depleted().any()
