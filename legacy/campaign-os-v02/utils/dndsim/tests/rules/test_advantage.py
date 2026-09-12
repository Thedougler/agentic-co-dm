from __future__ import annotations

import numpy as np

from dndsim.core.rng import BatchRNG
from dndsim.core.tags import BatchTags
from dndsim.rules.dnd5e_2014.advantage import (
    attack_advantage_mode,
    auto_fails_save,
    batch_attack_advantage_modes,
    batch_auto_fails_save,
    batch_prevented_from_acting,
    collapse_advantage,
    d20_face_probabilities,
    is_prevented_from_acting,
    roll_d20,
)


def test_collapse_advantage_only_source_wins() -> None:
    assert collapse_advantage(["advantage"]) == "advantage"
    assert collapse_advantage(["disadvantage"]) == "disadvantage"
    assert collapse_advantage([]) == "normal"


def test_collapse_advantage_multiple_same_side_do_not_stack() -> None:
    assert collapse_advantage(["advantage", "advantage", "advantage"]) == "advantage"
    assert collapse_advantage(["disadvantage", "disadvantage"]) == "disadvantage"


def test_collapse_advantage_and_disadvantage_cancel_to_normal() -> None:
    assert collapse_advantage(["advantage", "disadvantage"]) == "normal"
    assert collapse_advantage(["advantage", "advantage", "disadvantage"]) == "normal"


def test_attack_advantage_mode_reads_grants_and_imposes_from_registry() -> None:
    # invisible attacker: grants_self_advantage
    assert (
        attack_advantage_mode(attacker_tags={"invisible"}, defender_tags=set(), is_melee=True)
        == "advantage"
    )
    # prone defender vs. melee attacker: grants_attacker_advantage_melee_only
    assert (
        attack_advantage_mode(attacker_tags=set(), defender_tags={"prone"}, is_melee=True)
        == "advantage"
    )
    # prone defender vs. ranged attacker: melee-only flag does not apply
    assert (
        attack_advantage_mode(attacker_tags=set(), defender_tags={"prone"}, is_melee=False)
        == "normal"
    )
    # blinded attacker: imposes_self_disadvantage
    assert (
        attack_advantage_mode(attacker_tags={"blinded"}, defender_tags=set(), is_melee=True)
        == "disadvantage"
    )
    # paralyzed defender: grants_attacker_advantage (unconditional)
    assert (
        attack_advantage_mode(attacker_tags=set(), defender_tags={"paralyzed"}, is_melee=False)
        == "advantage"
    )


def test_attack_advantage_mode_accumulates_and_collapses_across_both_combatants() -> None:
    # attacker blinded (self-disadvantage) + defender invisible (imposes
    # attacker disadvantage) + defender prone melee (attacker advantage):
    # dis + dis + adv -> collapses to disadvantage, not normal.
    mode = attack_advantage_mode(
        attacker_tags={"blinded"}, defender_tags={"invisible"}, is_melee=True
    )
    assert mode == "disadvantage"


def test_auto_fails_save_matches_registered_conditions() -> None:
    assert auto_fails_save({"paralyzed"}, "str") is True
    assert auto_fails_save({"paralyzed"}, "wis") is False
    assert auto_fails_save({"charmed"}, "str") is False
    assert auto_fails_save(set(), "str") is False


def test_is_prevented_from_acting_matches_registered_conditions() -> None:
    assert is_prevented_from_acting({"stunned"}) is True
    assert is_prevented_from_acting({"charmed"}) is False
    assert is_prevented_from_acting(set()) is False


def test_batch_attack_advantage_modes_matches_scalar_form() -> None:
    size = 6
    attacker_tags = BatchTags(size)
    defender_tags = BatchTags(size)
    # universe 0: attacker invisible -> advantage
    attacker_tags.add("invisible", np.array([True, False, False, False, False, False]))
    # universe 1: defender prone, melee -> advantage
    defender_tags.add("prone", np.array([False, True, False, False, False, False]))
    # universe 2: attacker blinded -> disadvantage
    attacker_tags.add("blinded", np.array([False, False, True, False, False, False]))
    # universe 3: attacker blinded + defender invisible -> both disadvantage, still disadvantage
    attacker_tags.add("blinded", np.array([False, False, False, True, False, False]))
    defender_tags.add("invisible", np.array([False, False, False, True, False, False]))
    # universe 4: attacker invisible (adv) + attacker blinded (dis) -> cancels to normal
    attacker_tags.add("invisible", np.array([False, False, False, False, True, False]))
    attacker_tags.add("blinded", np.array([False, False, False, False, True, False]))
    # universe 5: nothing -> normal
    is_melee = np.ones(size, dtype=np.bool_)

    modes = batch_attack_advantage_modes(
        attacker_tags=attacker_tags, defender_tags=defender_tags, is_melee=is_melee, size=size
    )
    assert modes.tolist() == [1, 1, -1, -1, 0, 0]


def test_batch_auto_fails_save_and_prevented_from_acting() -> None:
    size = 3
    tags = BatchTags(size)
    tags.add("stunned", np.array([True, False, False]))
    tags.add("charmed", np.array([False, True, False]))

    auto_fail = batch_auto_fails_save(tags, "dex", size)
    assert auto_fail.tolist() == [True, False, False]

    prevented = batch_prevented_from_acting(tags, size)
    assert prevented.tolist() == [True, False, False]


def test_roll_d20_advantage_and_disadvantage_bounds() -> None:
    rng = BatchRNG(seed=1)
    normal = roll_d20(rng, 5000, "normal")
    adv = roll_d20(rng, 5000, "advantage")
    dis = roll_d20(rng, 5000, "disadvantage")
    assert normal.min() >= 1 and normal.max() <= 20
    assert adv.mean() > normal.mean() > dis.mean()


def test_d20_face_probabilities_sum_to_one_and_favor_correct_side() -> None:
    for mode in ("normal", "advantage", "disadvantage"):
        probs = d20_face_probabilities(mode)
        assert len(probs) == 20
        assert abs(sum(probs) - 1.0) < 1e-9
    adv = d20_face_probabilities("advantage")
    dis = d20_face_probabilities("disadvantage")
    # advantage weights high faces more than disadvantage does
    assert adv[19] > dis[19]
    assert dis[0] > adv[0]
