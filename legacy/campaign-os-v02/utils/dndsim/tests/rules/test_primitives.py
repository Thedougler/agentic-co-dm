"""The compiled 5e Primitive vocabulary (issue #43)."""

from __future__ import annotations

from dndsim.core.primitive import primitives as primitive_registry
from dndsim.rules.dnd5e_2014.primitives import (
    ABILITY_PRIMITIVES,
    AttackPrimitive,
    AutodamagePrimitive,
    PrimitiveBase,
    SavePrimitive,
    modifier_to_primitive,
)
from dndsim.rules.dnd5e_2014.sim_extension import (
    MODIFIER_CLASSES,
    SCENARIO_ONLY_KINDS,
    describe_modifier,
)


def test_every_ability_primitive_is_registered_in_the_core_registry() -> None:
    for kind in ABILITY_PRIMITIVES:
        assert f"dnd5e_2014:primitive/{kind}" in primitive_registry


def test_action_derived_primitives_are_registered() -> None:
    for kind in ("attack", "autodamage", "save", "heal", "reaction"):
        assert f"dnd5e_2014:primitive/{kind}" in primitive_registry


def test_scenario_only_modifier_kinds_have_no_ability_primitive() -> None:
    assert SCENARIO_ONLY_KINDS.isdisjoint(ABILITY_PRIMITIVES)


def test_primitive_vocabulary_matches_the_non_scenario_modifier_kinds() -> None:
    non_scenario_kinds = {
        cls.model_fields["kind"].default
        for cls in MODIFIER_CLASSES
        if cls.model_fields["kind"].default not in SCENARIO_ONLY_KINDS
    }
    assert set(ABILITY_PRIMITIVES) == non_scenario_kinds


def test_every_primitive_instance_carries_a_namespaced_id() -> None:
    m = describe_modifier("advantage", "x.md", "p", source="ally Faerie Fire")
    prim = modifier_to_primitive(m, "dnd5e_2014:primitive/advantage::x/0")
    assert isinstance(prim, PrimitiveBase)
    assert prim.id.startswith("dnd5e_2014:primitive/")


def test_extra_damage_modifier_local_id_becomes_ref_not_identity() -> None:
    m = describe_modifier(
        "extra_damage",
        "x.md",
        "p",
        dice="1d6",
        type="necrotic",
        id="hex",
        cost={"resource": "pact_slot_1", "spend": 1},
    )
    prim = modifier_to_primitive(m, "dnd5e_2014:primitive/extra_damage::otar/hex-0")
    assert prim.id == "dnd5e_2014:primitive/extra_damage::otar/hex-0"
    assert prim.ref == "hex"  # type: ignore[attr-defined]


def test_attack_primitive_shape() -> None:
    from dndsim.rules.dnd5e_2014.attack_string import DamageGroup

    p = AttackPrimitive(id="x", to_hit=8, damage=[DamageGroup(dice="1d8+5", type="slashing")])
    assert p.kind == "attack"


def test_autodamage_and_save_primitive_shapes() -> None:
    from dndsim.rules.dnd5e_2014.attack_string import DamageGroup, TargetClause

    ad = AutodamagePrimitive(
        id="x",
        damage=[DamageGroup(dice="4d12", type="bludgeoning")],
        targets=TargetClause(area=False, count=1),
    )
    assert ad.kind == "autodamage"

    sv = SavePrimitive(id="y", dc=16, save="dex", targets=TargetClause(area=True, radius=20))
    assert sv.kind == "save"
