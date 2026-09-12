"""The 5e condition vocabulary (issue #43's prefactor) — defined once."""

from __future__ import annotations

import re
from pathlib import Path

from dndsim.rules.dnd5e_2014 import conditions as conditions_module
from dndsim.rules.dnd5e_2014.attack_string import CONDITION_TAGS as ATTACK_STRING_CONDITION_TAGS
from dndsim.rules.dnd5e_2014.conditions import CONDITION_TAGS, RIDER_EFFECT_TAGS, conditions

RULES_DIR = Path(conditions_module.__file__).parent

# The union of the reference engine's five copies, in combatant.mjs's order
# — the one copy carrying the whole vocabulary. attack-string.mjs's narrower
# array omits `incapacitated_prone`, which is a `sim:` fence effect (Hideous
# Laughter) rather than a word appearing in statblock prose.
EXPECTED_TAGS = (
    "blinded",
    "charmed",
    "deafened",
    "frightened",
    "grappled",
    "incapacitated",
    "incapacitated_prone",
    "invisible",
    "paralyzed",
    "petrified",
    "poisoned",
    "prone",
    "restrained",
    "stunned",
    "unconscious",
)


def test_condition_tags_match_reference_vocabulary_and_order() -> None:
    assert CONDITION_TAGS == EXPECTED_TAGS


def test_attack_string_reuses_the_single_definition_by_import() -> None:
    # Identity, not just equality: attack_string.py must import this tuple,
    # never redeclare it.
    assert ATTACK_STRING_CONDITION_TAGS is CONDITION_TAGS


def test_every_condition_is_registered_exactly_once() -> None:
    assert len(conditions) == len(EXPECTED_TAGS)
    for tag in EXPECTED_TAGS:
        assert tag in conditions


def test_auto_fail_physical_saves_match_reference_engine() -> None:
    auto_fail = {tag for tag in conditions if conditions.get(tag).auto_fail_saves}
    assert auto_fail == {"stunned", "paralyzed", "unconscious", "petrified"}
    for tag in auto_fail:
        assert conditions.get(tag).auto_fail_saves == ("str", "dex")


def test_prevents_acting_matches_reference_engine() -> None:
    incapacitating = {tag for tag in conditions if conditions.get(tag).prevents_acting}
    assert incapacitating == {
        "incapacitated",
        "incapacitated_prone",
        "stunned",
        "paralyzed",
        "unconscious",
        "petrified",
    }


def test_invisible_grants_self_advantage_and_imposes_attacker_disadvantage() -> None:
    invisible = conditions.get("invisible")
    assert invisible.grants_self_advantage is True
    assert invisible.imposes_attacker_disadvantage is True


def test_prone_grants_attacker_advantage_melee_only() -> None:
    prone = conditions.get("prone")
    assert prone.grants_attacker_advantage_melee_only is True
    assert prone.grants_attacker_advantage is False


def test_rider_effect_tags_defined_once_alongside_conditions() -> None:
    assert RIDER_EFFECT_TAGS == (
        "disadvantage_next_attack",
        "speed_halved",
        "grants_advantage_next_attack",
        "lit",
    )


# --- the single-copy guard --------------------------------------------------

# A hand-written condition-vocabulary literal: 3+ of the 15 canonical tags
# appearing as adjacent quoted string literals (a Python list/tuple/set of
# condition names) — the shape every one of the reference engine's five
# copies took. `conditions.py` itself is exempt: it's the single home.
_TAG_ALT = "|".join(EXPECTED_TAGS)
_LITERAL_TAG_RUN_RE = re.compile(
    rf'(?:["\'](?:{_TAG_ALT})["\']\s*,\s*){{2,}}["\'](?:{_TAG_ALT})["\']'
)


def test_condition_vocabulary_has_no_second_copy() -> None:
    offenders: list[str] = []
    for path in sorted(RULES_DIR.rglob("*.py")):
        if path.name == "conditions.py":
            continue
        text = path.read_text()
        if _LITERAL_TAG_RUN_RE.search(text):
            offenders.append(str(path))
    assert offenders == [], f"a second hand-written condition-tag list appeared in: {offenders}"
