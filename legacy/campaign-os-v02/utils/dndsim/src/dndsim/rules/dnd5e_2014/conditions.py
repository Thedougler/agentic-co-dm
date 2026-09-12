"""The 5e condition vocabulary — defined exactly once (issue #43's prefactor,
ADR-0007).

Each condition's mechanical consequences are DATA on one registry
entry, never a code branch: whether it grants or imposes advantage/
disadvantage on an attack roll (as the condition-bearer's own attacker, or
as the target an attacker rolls against), which ability saves it auto-fails,
and whether it prevents the bearer from acting at all. Four later slices
(#45 combat model, #46 death saves, #47 positioning, #49 loadouts) read
this registry; none may define a second copy or extend it in place —
`tests/rules/test_conditions.py::test_condition_vocabulary_has_no_second_copy`
fails the build if one appears.

:data:`CONDITION_TAGS` is derived from the registry (never hand-listed a
second time) and is the UNION of the five copies, in `combatant.mjs`'s
ordering — the one copy that carries the whole vocabulary. `attack-string.
mjs`'s narrower array omits ``incapacitated_prone``; that tag is a `sim:`
fence effect (Hideous Laughter's ``effects: [{effect:
incapacitated_prone}]``), never a word appearing in statblock prose, so
including it leaves :mod:`attack_string`'s prose scan — which iterates this
tuple to decide rider *emission* order — byte-identical to the differential
harness's reference output.

:data:`RIDER_EFFECT_TAGS` is the adjacent, smaller vocabulary of non-
condition roll-state riders (`combatant.mjs`'s own `RIDER_EFFECT_TAGS`) —
kept here, in the same single home, rather than reintroducing a second
scattered copy of *that* list either.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final

from dndsim.core.registry import Registry


@dataclass(frozen=True, slots=True)
class ConditionDef:
    """One condition's full mechanical consequence, as data.

    ``grants_self_advantage`` / ``imposes_self_disadvantage`` govern the
    condition-bearer's OWN attack rolls (``engine.mjs``'s
    ``attackerConditionMods``). ``grants_attacker_advantage[_melee_only]`` /
    ``imposes_attacker_disadvantage`` govern attack rolls made AGAINST the
    bearer (``targetConditionMods``'s switch). ``auto_fail_saves`` names
    the ability keys the bearer auto-fails outright (``resolveSave`` /
    ``saveFailChance``'s duplicated array). ``prevents_acting`` marks the
    incapacitating set a combat model must treat as unable to take a turn.
    """

    tag: str
    grants_self_advantage: bool = False
    imposes_self_disadvantage: bool = False
    grants_attacker_advantage: bool = False
    grants_attacker_advantage_melee_only: bool = False
    imposes_attacker_disadvantage: bool = False
    auto_fail_saves: tuple[str, ...] = ()
    prevents_acting: bool = False


conditions: Registry[ConditionDef] = Registry("dndsim.conditions")


def _define(tag: str, **kwargs: object) -> None:
    conditions.register_value(tag, ConditionDef(tag=tag, **kwargs))  # type: ignore[arg-type]


# Registered in the reference engine's own vocabulary order (combatant.mjs's
# CONDITION_TAGS) — preserved so tuple(conditions) reproduces that exact order.
_define("blinded", imposes_self_disadvantage=True, grants_attacker_advantage=True)
_define("charmed")
_define("deafened")
_define("frightened", imposes_self_disadvantage=True)
_define("grappled")
_define("incapacitated", prevents_acting=True)
# Hideous Laughter's compound Prone+Incapacitated outcome, carried as one tag
# by the reference engine (`simulator.mjs`'s INCAPACITATING, `engine.mjs`'s
# targetConditionMods, `policy.mjs`'s rider weights, `combatant.mjs`'s Set).
_define("incapacitated_prone", prevents_acting=True, grants_attacker_advantage=True)
_define("invisible", grants_self_advantage=True, imposes_attacker_disadvantage=True)
_define(
    "paralyzed",
    prevents_acting=True,
    grants_attacker_advantage=True,
    auto_fail_saves=("str", "dex"),
)
_define(
    "petrified",
    prevents_acting=True,
    grants_attacker_advantage=True,
    auto_fail_saves=("str", "dex"),
)
_define("poisoned", imposes_self_disadvantage=True)
_define("prone", grants_attacker_advantage_melee_only=True)
_define("restrained", imposes_self_disadvantage=True, grants_attacker_advantage=True)
_define(
    "stunned",
    prevents_acting=True,
    grants_attacker_advantage=True,
    auto_fail_saves=("str", "dex"),
)
_define(
    "unconscious",
    prevents_acting=True,
    grants_attacker_advantage=True,
    auto_fail_saves=("str", "dex"),
)

CONDITION_TAGS: Final[tuple[str, ...]] = tuple(conditions)

# combatant.mjs's own RIDER_EFFECT_TAGS — non-condition roll-state riders a
# `sim:` `on_fail`/`post_hit_rider` effect list may also carry.
RIDER_EFFECT_TAGS: Final[tuple[str, ...]] = (
    "disadvantage_next_attack",
    "speed_halved",
    "grants_advantage_next_attack",
    "lit",
)
