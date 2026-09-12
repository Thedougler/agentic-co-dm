"""2014 + 2024 SRD attack grammar and Multiattack (issues #41, #42).

Every ``desc`` below is verbatim from a live vault page.
"""

from __future__ import annotations

from dndsim.rules.dnd5e_2014.attack_string import (
    AttackAction,
    AutodamageAction,
    SaveAction,
    UnmodeledAction,
    legendary_actions_per_round,
    parse_action,
    parse_action_category,
    parse_multiattack,
    parse_name_usage,
)


def test_sawek_bite_attack_conditional_advantage_vs_grappled() -> None:
    a = parse_action(
        "Bite",
        "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 18 (3d8 + 5) "
        "piercing damage. The Sawek has advantage on this attack roll if the target "
        "is Grappled.",
    )
    assert isinstance(a, AttackAction)
    assert a.attack_type == "melee_weapon"
    assert a.to_hit == 8
    assert a.reach == 10
    assert [d.model_dump() for d in a.damage] == [{"dice": "3d8+5", "type": "piercing"}]
    assert a.advantage_if == "target_has:grappled"


def test_sawek_tentacle_grapple_escape_dc_and_restrained_riders() -> None:
    a = parse_action(
        "Tentacle",
        "Melee Weapon Attack: +8 to hit, reach 20 ft., one target. Hit: 12 (2d6 + 5) "
        "bludgeoning damage. The target is Grappled (escape DC 16) and Restrained "
        "until the grapple ends. The Sawek can maintain up to two grapples "
        "simultaneously.",
    )
    assert isinstance(a, AttackAction)
    assert [e.model_dump() for e in a.on_hit_effects] == [
        {"effect": "grappled", "escape_dc": 16, "save_ends": None},
        {"effect": "restrained", "escape_dc": None, "save_ends": None},
    ]


def test_sawek_crush_autodamage_requiring_grappled_attached_save_hyphen_recharge() -> None:
    a = parse_action(
        "Crush (Recharge 5-6)",
        "One Grappled creature takes 28 (4d12) bludgeoning damage and must succeed "
        "on a DC 16 Constitution saving throw or be Incapacitated until the end of "
        "its next turn.",
    )
    assert isinstance(a, AutodamageAction)
    assert a.name == "Crush"
    assert a.usage.recharge == (5, 6)
    assert [d.model_dump() for d in a.damage] == [{"dice": "4d12", "type": "bludgeoning"}]
    assert a.requires_target_condition == "grappled"
    assert a.attached_save is not None
    assert a.attached_save.dc == 16
    assert a.attached_save.save == "con"
    assert [e.model_dump() for e in a.attached_save.effects] == [
        {"effect": "incapacitated", "escape_dc": None, "save_ends": None}
    ]


def test_grung_dagger_melee_or_ranged_plus_2d4_poison_second_damage_group() -> None:
    a = parse_action(
        "Dagger",
        "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., "
        "one target. Hit: 5 (1d4 + 3) piercing damage plus 5 (2d4) poison damage.",
    )
    assert isinstance(a, AttackAction)
    assert a.to_hit == 5
    assert [d.model_dump() for d in a.damage] == [
        {"dice": "1d4+3", "type": "piercing"},
        {"dice": "2d4", "type": "poison"},
    ]


def test_grung_mesmerizing_chirr_dc12_wis_area_save_stunned_recharge6() -> None:
    a = parse_action(
        "Mesmerizing Chirr (Recharge 6)",
        "The grung makes a chirring noise to which grung are immune. Each humanoid "
        "or beast within 15 feet of the grung that can hear it must succeed on a "
        "DC 12 Wisdom saving throw or be stunned until the end of the grung's "
        "next turn.",
    )
    assert isinstance(a, SaveAction)
    assert a.dc == 12
    assert a.save == "wis"
    assert a.usage.recharge == (6, 6)
    assert a.targets.model_dump() == {"area": True, "count": None, "radius": 15, "cone": None}
    assert [e.model_dump() for e in a.on_fail.effects] == [
        {"effect": "stunned", "escape_dc": None, "save_ends": None}
    ]


def test_vashu_still_water_strike_conditional_poison_damage_on_poisoned_target() -> None:
    a = parse_action(
        "Still-Water Strike",
        "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) "
        "bludgeoning damage. If the target is poisoned, it also takes 9 (2d8) "
        "poison damage.",
    )
    assert isinstance(a, AttackAction)
    assert [d.model_dump() for d in a.damage] == [{"dice": "2d8+5", "type": "bludgeoning"}]
    assert [c.model_dump() for c in a.conditional_damage] == [
        {"condition": "poisoned", "dice": "2d8", "type": "poison"}
    ]


def test_vashu_pressure_point_costs2_actions_en_dash_recharge_stun_on_fail() -> None:
    a = parse_action(
        "Pressure Point (Costs 2 Actions, Recharge 5–6)",
        "Vashu strikes a nerve cluster on one creature she can perceive within 5 "
        "feet. The target must make a DC 16 Constitution saving throw. On a "
        "failure, it is stunned until the end of Vashu's next turn. On a success, "
        "its speed is halved and it is poisoned until the end of its next turn.",
    )
    assert a.name == "Pressure Point"
    assert a.usage.legendary_cost == 2
    assert a.usage.recharge == (5, 6)
    assert isinstance(a, SaveAction)
    assert a.dc == 16
    assert any(e.effect == "stunned" for e in a.on_fail.effects)


def test_vashu_still_water_deflection_unmodeled_never_guessed() -> None:
    a = parse_action(
        "Still-Water Deflection",
        "When Vashu or an ally within 10 feet of her is hit by a ranged attack "
        "Vashu can perceive, she reduces the damage to that target by 15 (2d10 + 4). "
        "If this reduces the damage taken by Vashu herself to 0, she can redirect "
        "the missile at a creature she can perceive within 30 feet: +8 to hit, 12 "
        "(2d10 + 1) damage of the triggering attack's type.",
    )
    assert isinstance(a, UnmodeledAction)


def test_otar_chaos_pulse_half_on_save_aoe_damage_plus_prone() -> None:
    a = parse_action(
        "Chaos Pulse (Recharge 5-6)",
        "Otar slams both fists into the ground. Each creature within 20 feet must "
        "make a DC 17 Dexterity saving throw. On a failure, a creature takes 33 "
        "(6d10) force damage and is knocked prone. On a success, a creature takes "
        "half damage and isn't knocked prone. Rubble and debris in the area become "
        "difficult terrain.",
    )
    assert isinstance(a, SaveAction)
    assert a.dc == 17
    assert a.save == "dex"
    assert [d.model_dump() for d in a.on_fail.damage] == [{"dice": "6d10", "type": "force"}]
    assert any(e.effect == "prone" for e in a.on_fail.effects)
    assert a.targets.model_dump() == {"area": True, "count": None, "radius": 20, "cone": None}


def test_ozzeth_venom_lash_parenthetical_attack_qualifier_tongue_tolerated() -> None:
    a = parse_action(
        "Venom Lash",
        "Melee Weapon Attack (tongue): +6 to hit, reach 10 ft., one target. Hit: 5 "
        "(1d4 + 3) piercing damage, and the target must succeed on a DC 14 "
        "Constitution saving throw or take 7 (2d6) poison damage. Ozzeth can pull "
        "a target of Medium size or smaller 5 feet toward him on a hit.",
    )
    assert isinstance(a, AttackAction)
    assert a.to_hit == 6
    assert a.on_hit_save is not None
    assert a.on_hit_save.dc == 14
    assert a.on_hit_save.save == "con"


def test_hierarch_blood_sacrifice_save_gated_damage_no_attack_roll_unmodeled() -> None:
    a = parse_action(
        "Blood Sacrifice",
        "One bloodline creature must succeed on a DC 19 Constitution saving throw "
        "or take 3d10 Necrotic damage. The Hierarch regains HP equal to the damage "
        "dealt and regains one expended spell slot or Metamagic use.",
    )
    # "3d10 Necrotic damage" carries no "N (dice)" average — the SRD grammar this
    # parser reads requires the parenthesized form; degraded here to a save action
    # with no parsed damage -> unmodeled, never guessed.
    assert isinstance(a, UnmodeledAction)


def test_name_usage_3_per_day() -> None:
    name, usage = parse_name_usage("Slippery Grip (3/Day)")
    assert name == "Slippery Grip"
    assert usage.per_day == 3


def test_homunculus_bite_bare_flat_damage_2014_grammar_no_parentheses() -> None:
    a = parse_action(
        "Bite", "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 piercing damage."
    )
    assert isinstance(a, AttackAction)
    assert a.to_hit == 2
    assert [d.model_dump() for d in a.damage] == [{"dice": "1", "type": "piercing"}]


def test_regression_parenthesized_dice_still_parsed() -> None:
    a = parse_action(
        "Claw",
        "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) "
        "slashing damage.",
    )
    assert isinstance(a, AttackAction)
    assert [d.model_dump() for d in a.damage] == [{"dice": "1d6+2", "type": "slashing"}]


def test_mixed_bare_flat_and_parenthesized_damage_same_desc_in_order() -> None:
    a = parse_action(
        "Combined Strike",
        "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing "
        "damage plus 5 (1d8 + 2) slashing damage.",
    )
    assert isinstance(a, AttackAction)
    assert [d.model_dump() for d in a.damage] == [
        {"dice": "1", "type": "piercing"},
        {"dice": "1d8+2", "type": "slashing"},
    ]


def test_homunculus_bite_bare_flat_damage_2024_grammar_no_parentheses() -> None:
    a = parse_action("Bite", "Melee Attack Roll: +2, reach 5 ft. 1 Piercing damage.")
    assert isinstance(a, AttackAction)
    assert a.to_hit == 2
    assert [d.model_dump() for d in a.damage] == [{"dice": "1", "type": "piercing"}]


def test_multiattack_one_bite_two_tentacle() -> None:
    r = parse_multiattack(
        "The Sawek makes one Bite attack and two Tentacle attacks.",
        ["Bite", "Tentacle", "Crush"],
    )
    assert r is not None
    assert [s.model_dump() for s in r] == [
        {"ref": "Bite", "count": 1, "alternatives": []},
        {"ref": "Tentacle", "count": 2, "alternatives": []},
    ]


def test_multiattack_three_still_water_strike_attacks() -> None:
    r = parse_multiattack(
        "Vashu makes three Still-Water Strike attacks.",
        ["Still-Water Strike", "Tongue Lash"],
    )
    assert r is not None
    assert [s.model_dump() for s in r] == [
        {"ref": "Still-Water Strike", "count": 3, "alternatives": []}
    ]


def test_multiattack_colon_list_three_attacks() -> None:
    r = parse_multiattack(
        "Otar makes three attacks: one Bite, one Claw, and one Tongue Lash. It can "
        "replace the Tongue Lash with a second Claw attack.",
        ["Bite", "Claw", "Tongue Lash", "Chaos Pulse"],
    )
    assert r is not None
    assert [s.model_dump() for s in r] == [
        {"ref": "Bite", "count": 1, "alternatives": []},
        {"ref": "Claw", "count": 1, "alternatives": []},
        {"ref": "Tongue Lash", "count": 1, "alternatives": []},
    ]


def test_multiattack_two_attacks_with_its_dagger_or_shortbow() -> None:
    r = parse_multiattack(
        "The grung makes two attacks with its dagger or shortbow.",
        ["Dagger", "Shortbow", "Mesmerizing Chirr"],
    )
    assert r is not None
    assert [s.model_dump() for s in r] == [
        {"ref": "Dagger", "count": 2, "alternatives": ["Shortbow"]}
    ]


def test_multiattack_unmatched_phrasing_partial_match_never_a_guess() -> None:
    r = parse_multiattack(
        "Ozzeth casts one cantrip and makes one Venom Lash attack.",
        ["Venom Lash", "Poison Spray (Cantrip)"],
    )
    assert r is not None
    assert [s.model_dump() for s in r] == [{"ref": "Venom Lash", "count": 1, "alternatives": []}]


# 2024-grammar save-action coverage: _save_clause_2024 + _labeled_clauses_2024
# + the 2024 condition-rider regex. Every desc below is verbatim from a real
# committed vault/srd/monsters/*.md page.


def test_adult_black_dragon_acid_breath_2024_labeled_failure_success() -> None:
    # vault/srd/monsters/adult-black-dragon.md, action
    # "Acid Breath (Recharge 5-6)".
    a = parse_action(
        "Acid Breath (Recharge 5-6)",
        "*Dexterity Saving Throw*: DC 18, each creature in a 60-foot-long, "
        "5-foot-wide Line. *Failure:* 54 (12d8) Acid damage. *Success:* Half "
        "damage.",
    )
    assert isinstance(a, SaveAction)
    assert a.dc == 18
    assert a.save == "dex"
    assert [d.model_dump() for d in a.on_fail.damage] == [{"dice": "12d8", "type": "acid"}]
    assert a.half_on_save is True


def test_adult_black_dragon_cloud_of_insects_failure_or_success_bounds_failure() -> None:
    # vault/srd/monsters/adult-black-dragon.md, legendary action
    # "Cloud of Insects".
    a = parse_action(
        "Cloud of Insects",
        "*Dexterity Saving Throw*: DC 17, one creature the dragon can see within "
        "120 feet. *Failure:* 22 (4d10) Poison damage, and the target has "
        "Disadvantage on saving throws to maintain Concentration until the end "
        "of its next turn. *Failure or Success*: The dragon can't take this "
        "action again until the start of its next turn.",
    )
    assert isinstance(a, SaveAction)
    assert a.dc == 17
    assert a.save == "dex"
    assert [d.model_dump() for d in a.on_fail.damage] == [{"dice": "4d10", "type": "poison"}]
    # Only the combined "*Failure or Success*" label is present (no
    # standalone "*Success:*"), so half_on_save must stay false rather than
    # false-matching.
    assert a.half_on_save is False


def test_chuul_pincer_2024_single_condition_rider_grappled_escape_dc() -> None:
    # vault/srd/monsters/chuul.md, action "Pincer".
    a = parse_action(
        "Pincer",
        "*Melee Attack Roll:* +6, reach 10 ft. 9 (1d10 + 4) Bludgeoning damage. "
        "If the target is a Large or smaller creature, it has the Grappled "
        "condition (escape DC 14) from one of two pincers.",
    )
    assert isinstance(a, AttackAction)
    assert [e.model_dump() for e in a.on_hit_effects] == [
        {"effect": "grappled", "escape_dc": 14, "save_ends": None}
    ]


def test_purple_worm_bite_two_condition_riders_both_extracted() -> None:
    # vault/srd/monsters/purple-worm.md, action "Bite" (desc verbatim).
    a = parse_action(
        "Bite",
        "*Melee Attack Roll:* +14, reach 10 ft. 22 (3d8 + 9) Piercing damage. If "
        "the target is a Large or smaller creature, it has the Grappled "
        "condition (escape DC 19), and it has the Restrained condition until "
        "the grapple ends.",
    )
    assert isinstance(a, AttackAction)
    assert [d.model_dump() for d in a.damage] == [{"dice": "3d8+9", "type": "piercing"}]
    assert [e.model_dump() for e in a.on_hit_effects] == [
        {"effect": "grappled", "escape_dc": 19, "save_ends": None},
        {"effect": "restrained", "escape_dc": None, "save_ends": None},
    ]


def test_kraken_tentacle_damage_plus_two_riders_from_one_of_ten_tentacles() -> None:
    # vault/srd/monsters/kraken.md, action "Tentacle" (desc verbatim).
    a = parse_action(
        "Tentacle",
        "*Melee Attack Roll:* +17, reach 30 ft. 24 (4d6 + 10) Bludgeoning damage. "
        "The target has the Grappled condition (escape DC 20) from one of ten "
        "tentacles, and it has the Restrained condition until the grapple "
        "ends.",
    )
    assert isinstance(a, AttackAction)
    assert [d.model_dump() for d in a.damage] == [{"dice": "4d6+10", "type": "bludgeoning"}]
    assert [e.model_dump() for e in a.on_hit_effects] == [
        {"effect": "grappled", "escape_dc": 20, "save_ends": None},
        {"effect": "restrained", "escape_dc": None, "save_ends": None},
    ]


def test_chain_devil_chain_and_roc_talons_from_one_of_two_from_both_phrasing() -> None:
    # vault/srd/monsters/chain-devil.md action "Chain" and
    # vault/srd/monsters/roc.md action "Talons" (descs verbatim) — the same
    # two-rider shape with a different intervening clause each.
    chain = parse_action(
        "Chain",
        "*Melee Attack Roll:* +7, reach 10 ft. 11 (2d6 + 4) Slashing damage. If "
        "the target is a Large or smaller creature, it has the Grappled "
        "condition (escape DC 14) from one of two chains, and it has the "
        "Restrained condition until the grapple ends.",
    )
    assert isinstance(chain, AttackAction)
    assert [e.model_dump() for e in chain.on_hit_effects] == [
        {"effect": "grappled", "escape_dc": 14, "save_ends": None},
        {"effect": "restrained", "escape_dc": None, "save_ends": None},
    ]
    talons = parse_action(
        "Talons",
        "*Melee Attack Roll:* +13, reach 5 ft. 23 (4d6 + 9) Slashing damage. If "
        "the target is a Huge or smaller creature, it has the Grappled "
        "condition (escape DC 19) from both talons, and it has the "
        "Restrained condition until the grapple ends.",
    )
    assert isinstance(talons, AttackAction)
    assert [e.model_dump() for e in talons.on_hit_effects] == [
        {"effect": "grappled", "escape_dc": 19, "save_ends": None},
        {"effect": "restrained", "escape_dc": None, "save_ends": None},
    ]


def test_tarrasque_bite_and_tail_rider_in_next_sentence_and_no_escape_dc() -> None:
    # vault/srd/monsters/tarrasque.md actions "Bite" and "Tail" (descs
    # verbatim). Bite: the second rider lives in the NEXT sentence. Tail: a
    # rider with no escape DC at all.
    bite = parse_action(
        "Bite",
        "*Melee Attack Roll:* +19, reach 15 ft. 36 (4d12 + 10) Piercing damage, "
        "and the target has the Grappled condition (escape DC 20). Until the "
        "grapple ends, the target has the Restrained condition and can't "
        "teleport.",
    )
    assert isinstance(bite, AttackAction)
    assert [e.model_dump() for e in bite.on_hit_effects] == [
        {"effect": "grappled", "escape_dc": 20, "save_ends": None},
        {"effect": "restrained", "escape_dc": None, "save_ends": None},
    ]
    tail = parse_action(
        "Tail",
        "*Melee Attack Roll:* +19, reach 30 ft. 23 (3d8 + 10) Bludgeoning "
        "damage. If the target is a Huge or smaller creature, it has the "
        "Prone condition.",
    )
    assert isinstance(tail, AttackAction)
    assert [d.model_dump() for d in tail.damage] == [{"dice": "3d8+10", "type": "bludgeoning"}]
    assert [e.model_dump() for e in tail.on_hit_effects] == [
        {"effect": "prone", "escape_dc": None, "save_ends": None}
    ]


def test_roper_tentacle_2024_condition_rider_only_action_no_direct_damage() -> None:
    # vault/srd/monsters/roper.md, action "Tentacle" (desc verbatim) — a real
    # grapple-only attack with no "N (dice) type damage" clause at all.
    a = parse_action(
        "Tentacle",
        "*Melee Attack Roll:* +7, reach 60 ft. The target has the Grappled "
        "condition (escape DC 14) from one of six tentacles, and the target "
        "has the Poisoned condition until the grapple ends. The tentacle can "
        "be damaged, freeing a creature it has Grappled when destroyed (AC "
        "20, HP 10, Immunity to Poison and Psychic damage). Damaging the "
        "tentacle deals no damage to the roper, and a destroyed tentacle "
        "regrows at the start of the roper's next turn.",
    )
    assert isinstance(a, AttackAction)
    assert a.to_hit == 7
    assert a.reach == 60
    assert [d.model_dump() for d in a.damage] == []
    assert [e.model_dump() for e in a.on_hit_effects] == [
        {"effect": "grappled", "escape_dc": 14, "save_ends": None},
        {"effect": "poisoned", "escape_dc": None, "save_ends": None},
    ]


def test_invisible_stalker_vortex_2024_save_not_preempted_by_autodamage_phrase() -> None:
    # vault/srd/monsters/invisible-stalker.md, action "Vortex" (desc
    # verbatim). A real 2024-grammar save action whose failure text
    # incidentally matches the autodamage regex.
    a = parse_action(
        "Vortex",
        "*Constitution Saving Throw*: DC 14, one Large or smaller creature in "
        "the stalker's space. *Failure:* 7 (1d8 + 3) Thunder damage, and the "
        "target has the Grappled condition (escape DC 13). Until the grapple "
        "ends, the target can't cast spells with a Verbal component and takes "
        "7 (2d6) Thunder damage at the start of each of the stalker's turns.",
    )
    assert isinstance(a, SaveAction)
    assert a.dc == 14
    assert a.save == "con"
    assert [d.model_dump() for d in a.on_fail.damage] == [{"dice": "1d8+3", "type": "thunder"}]
    assert [e.model_dump() for e in a.on_fail.effects] == [
        {"effect": "grappled", "escape_dc": None, "save_ends": None}
    ]
    assert a.half_on_save is False


def test_storm_giant_lightning_strike_plural_blinded_and_deafened_conditions() -> None:
    # vault/srd/monsters/storm-giant.md, action "Lightning Strike" (desc
    # verbatim) — the plural-compound rider shape.
    a = parse_action(
        "Lightning Strike",
        "*Ranged Attack Roll:* +14, range 500 ft. 22 (2d12 + 9) Lightning "
        "damage, and the target has the Blinded and Deafened conditions "
        "until the start of the giant's next turn.",
    )
    assert isinstance(a, AttackAction)
    assert [e.model_dump() for e in a.on_hit_effects] == [
        {"effect": "blinded", "escape_dc": None, "save_ends": None},
        {"effect": "deafened", "escape_dc": None, "save_ends": None},
    ]


def test_otyugh_tentacle_downstream_whenever_maintenance_save_not_attached() -> None:
    # vault/srd/monsters/otyugh.md, action "Tentacle" (desc verbatim). The
    # DC 15 CON save is a long-rest maintenance check introduced by a
    # "Whenever ..." sentence — not an on-hit gate.
    a = parse_action(
        "Tentacle",
        "*Melee Attack Roll:* +6, reach 5 ft. 12 (2d8 + 3) Piercing damage, and "
        "the target has the Poisoned condition. Whenever the Poisoned target "
        "finishes a Long Rest, it is subjected to the following effect. "
        "*Constitution Saving Throw*: DC 15. *Failure:* The target's Hit "
        "Point maximum decreases by 5 (1d10) and doesn't return to normal "
        "until the Poisoned condition ends on the target. *Success:* The "
        "Poisoned condition ends.",
    )
    assert isinstance(a, AttackAction)
    assert [e.model_dump() for e in a.on_hit_effects] == [
        {"effect": "poisoned", "escape_dc": None, "save_ends": None}
    ]
    assert a.on_hit_save is None


def test_both_grammars_coexist_on_one_page_auto_detected_never_merged() -> None:
    # No live corpus page mixes both grammar eras across its own actions
    # (measured: 234 pages are 2024-only, 37 are 2014-only, 0 use both) —
    # a constructed fixture, per issue #42's acceptance criterion, standing
    # in for a page with one action of each era in its own actions list.
    # Auto-detection reads each action's desc independently; nothing here
    # merges the two grammars into one pattern.
    actions, warnings = parse_action_category(
        [
            {
                "name": "Bite",
                "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. "
                "Hit: 18 (3d8 + 5) piercing damage.",
            },
            {
                "name": "Claw",
                "desc": "*Melee Attack Roll:* +6, reach 10 ft. 9 (1d10 + 4) Bludgeoning damage.",
            },
        ],
        "actions",
    )
    assert warnings == []
    bite, claw = actions
    assert isinstance(bite, AttackAction)
    assert bite.to_hit == 8
    assert [d.model_dump() for d in bite.damage] == [{"dice": "3d8+5", "type": "piercing"}]
    assert isinstance(claw, AttackAction)
    assert claw.to_hit == 6
    assert [d.model_dump() for d in claw.damage] == [{"dice": "1d10+4", "type": "bludgeoning"}]


# --- legendary_actions_per_round ----------------------------------------------


def test_legendary_actions_per_round_reads_singular_preamble() -> None:
    entries = [
        {
            "name": "",
            "desc": (
                "Otar can take 1 legendary action, choosing from the "
                "options below, only at the end of another creature's "
                "turn. Otar regains its spent legendary action at the "
                "start of its turn."
            ),
        },
        {"name": "Lash", "desc": "Otar makes one Tongue Lash attack."},
    ]
    assert legendary_actions_per_round(entries) == 1


def test_legendary_actions_per_round_reads_plural_preamble() -> None:
    entries = [
        {
            "name": "",
            "desc": (
                "Otar can take 3 legendary actions, choosing from the "
                "options below, only at the end of another creature's "
                "turn. Otar regains its spent legendary actions at the "
                "start of its turn."
            ),
        },
    ]
    assert legendary_actions_per_round(entries) == 3


def test_legendary_actions_per_round_defaults_to_three_with_no_preamble_count() -> None:
    entries = [{"name": "Lash", "desc": "Otar makes one Tongue Lash attack."}]
    assert legendary_actions_per_round(entries) == 3


def test_legendary_actions_per_round_is_zero_with_no_legendary_actions() -> None:
    assert legendary_actions_per_round(None) == 0
    assert legendary_actions_per_round([]) == 0
