"""Exhaustion (issue #55): the shared contract plus each edition's own
numbers — the ADR-0007 payoff made concrete on one real mechanic."""

from __future__ import annotations

from dndsim import plugins
from dndsim.rules.dnd5e_2014.exhaustion import RULES_ID as RULES_ID_2014
from dndsim.rules.dnd5e_2024.exhaustion import RULES_ID as RULES_ID_2024
from dndsim.rules.exhaustion import ExhaustionRules, exhaustion_rules

plugins.load_rules_packs()


def test_both_editions_are_registered_under_distinct_ids() -> None:
    assert RULES_ID_2014 == "dnd5e_2014:rules/exhaustion"
    assert RULES_ID_2024 == "dnd5e_2024:rules/exhaustion"
    assert RULES_ID_2014 in exhaustion_rules
    assert RULES_ID_2024 in exhaustion_rules
    assert exhaustion_rules.get(RULES_ID_2014) is not exhaustion_rules.get(RULES_ID_2024)


def test_2014_uses_the_tiered_table_not_a_flat_penalty() -> None:
    rules = exhaustion_rules.get(RULES_ID_2014)
    assert rules.d20_penalty(3) == 0
    assert rules.imposes_save_disadvantage(2) is False
    assert rules.imposes_save_disadvantage(3) is True
    assert rules.imposes_save_disadvantage(6) is True


def test_2014_speed_halves_at_2_and_zeroes_at_5() -> None:
    rules = exhaustion_rules.get(RULES_ID_2014)
    assert rules.effective_speed_ft(0, 30) == 30
    assert rules.effective_speed_ft(1, 30) == 30
    assert rules.effective_speed_ft(2, 30) == 15
    assert rules.effective_speed_ft(4, 30) == 15
    assert rules.effective_speed_ft(5, 30) == 0
    assert rules.effective_speed_ft(6, 30) == 0


def test_2024_uses_a_flat_penalty_never_disadvantage() -> None:
    rules = exhaustion_rules.get(RULES_ID_2024)
    assert rules.d20_penalty(0) == 0
    assert rules.d20_penalty(1) == 2
    assert rules.d20_penalty(3) == 6
    assert rules.imposes_save_disadvantage(6) is False


def test_2024_speed_drops_5ft_per_level() -> None:
    rules = exhaustion_rules.get(RULES_ID_2024)
    assert rules.effective_speed_ft(0, 30) == 30
    assert rules.effective_speed_ft(1, 30) == 25
    assert rules.effective_speed_ft(3, 30) == 15
    assert rules.effective_speed_ft(6, 30) == 0  # floored at 0, never negative


def test_both_editions_die_at_level_6() -> None:
    for rules_id in (RULES_ID_2014, RULES_ID_2024):
        rules = exhaustion_rules.get(rules_id)
        assert rules.is_dead(5) is False
        assert rules.is_dead(6) is True


def test_a_non_exhausted_combatant_is_unaffected_by_either_edition() -> None:
    for rules_id in (RULES_ID_2014, RULES_ID_2024):
        rules = exhaustion_rules.get(rules_id)
        assert rules.d20_penalty(0) == 0
        assert rules.imposes_save_disadvantage(0) is False
        assert rules.effective_speed_ft(0, 30) == 30


def test_exhaustion_rules_is_a_frozen_dataclass_never_a_mechanic() -> None:
    """Data on a registry entry, mirroring ConditionDef — never a
    `dndsim.core.mechanic.Mechanic` subclass, since it carries no
    stochastic resolve()/expected_value() of its own (ADR-0008 governs
    genuinely probabilistic primitives; this is deterministic per-level
    data, exactly like ConditionDef)."""
    rules = ExhaustionRules(id="test:rules/exhaustion")
    try:
        rules.death_at_level = 1  # type: ignore[misc]
    except AttributeError:
        pass
    else:
        raise AssertionError("ExhaustionRules must be frozen")
