"""Advantage/disadvantage: accumulation, collapse, and the d20 mechanics
that consume a resolved mode — plus the condition *consequences* (auto-fail
saves, turn-skipping) that ride on the same registry.

`conditions.py` is the single home for the vocabulary itself (issue #43's
prefactor); this module is the one place in the #45 combat-model slice that
*consumes* it to decide a roll's advantage mode, a save's auto-fail, or
whether a bearer's turn is skipped outright. Every lookup goes through
:data:`dndsim.rules.dnd5e_2014.conditions.conditions` — never a hand-listed
tag set — so `test_condition_vocabulary_has_no_second_copy` stays green as
this module grows.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Literal

import numpy as np

from dndsim.rules.dnd5e_2014.conditions import conditions

if TYPE_CHECKING:
    from dndsim.core.rng import BatchRNG
    from dndsim.core.tags import BatchTags

AdvantageMode = Literal["normal", "advantage", "disadvantage"]


def collapse_advantage(modes: Iterable[AdvantageMode]) -> AdvantageMode:
    """Accumulate any number of advantage/disadvantage *sources* down to one
    5e roll mode (PHB p.173): any advantage source cancels any disadvantage
    source — the pair nets to a straight roll, never to double-advantage or
    double-disadvantage — regardless of how many sources stack on either
    side."""
    has_adv = False
    has_dis = False
    for mode in modes:
        if mode == "advantage":
            has_adv = True
        elif mode == "disadvantage":
            has_dis = True
    if has_adv and has_dis:
        return "normal"
    if has_adv:
        return "advantage"
    if has_dis:
        return "disadvantage"
    return "normal"


def attack_advantage_mode(
    *, attacker_tags: set[str], defender_tags: set[str], is_melee: bool
) -> AdvantageMode:
    """The roll mode for one attack roll, from both combatants' own
    condition tags — the scalar (single-entity) form, for the
    per-decision-instance shape every :class:`~dndsim.core.mechanic.Mechanic`
    already uses."""
    sources: list[AdvantageMode] = []
    for tag in attacker_tags:
        if tag not in conditions:
            continue
        cdef = conditions.get(tag)
        if cdef.grants_self_advantage:
            sources.append("advantage")
        if cdef.imposes_self_disadvantage:
            sources.append("disadvantage")
    for tag in defender_tags:
        if tag not in conditions:
            continue
        cdef = conditions.get(tag)
        melee_riser = is_melee and cdef.grants_attacker_advantage_melee_only
        if cdef.grants_attacker_advantage or melee_riser:
            sources.append("advantage")
        if cdef.imposes_attacker_disadvantage:
            sources.append("disadvantage")
    return collapse_advantage(sources)


def auto_fails_save(tags: set[str], ability: str) -> bool:
    """Whether any tag in `tags` forces an automatic failure of an
    `ability` saving throw (e.g. paralyzed auto-fails STR/DEX) — read off
    each condition's own `auto_fail_saves`, never a hand-listed ability
    set."""
    return any(tag in conditions and ability in conditions.get(tag).auto_fail_saves for tag in tags)


def is_prevented_from_acting(tags: set[str]) -> bool:
    """Whether any tag in `tags` incapacitates the bearer outright, so its
    turn is skipped rather than merely constrained."""
    return any(tag in conditions and conditions.get(tag).prevents_acting for tag in tags)


# --- batched (per-universe) forms, for BatchTags-backed state --------------


def batch_attack_advantage_modes(
    *, attacker_tags: BatchTags, defender_tags: BatchTags, is_melee: np.ndarray, size: int
) -> np.ndarray:
    """The batched analogue of :func:`attack_advantage_mode`: one mode per
    universe, encoded as ``int8`` (``1`` advantage, ``-1`` disadvantage,
    ``0`` normal) so it composes with numpy masks directly. Iterates the
    condition registry's own entries, exactly like the scalar form — never
    a hand-listed tag set."""
    has_adv = np.zeros(size, dtype=np.bool_)
    has_dis = np.zeros(size, dtype=np.bool_)
    for tag, cdef in conditions.items():
        if cdef.grants_self_advantage:
            has_adv |= attacker_tags.has(tag)
        if cdef.imposes_self_disadvantage:
            has_dis |= attacker_tags.has(tag)
        if cdef.grants_attacker_advantage:
            has_adv |= defender_tags.has(tag)
        if cdef.grants_attacker_advantage_melee_only:
            has_adv |= defender_tags.has(tag) & is_melee
        if cdef.imposes_attacker_disadvantage:
            has_dis |= defender_tags.has(tag)
    modes = np.zeros(size, dtype=np.int8)
    modes[has_adv & ~has_dis] = 1
    modes[has_dis & ~has_adv] = -1
    return modes


def batch_auto_fails_save(tags: BatchTags, ability: str, size: int) -> np.ndarray:
    """Per-universe boolean: does the bearer's current tag set auto-fail an
    `ability` save."""
    result = np.zeros(size, dtype=np.bool_)
    for tag, cdef in conditions.items():
        if ability in cdef.auto_fail_saves:
            result |= tags.has(tag)
    return result


def batch_prevented_from_acting(tags: BatchTags, size: int) -> np.ndarray:
    """Per-universe boolean: is the bearer incapacitated (turn skipped)."""
    result = np.zeros(size, dtype=np.bool_)
    for tag, cdef in conditions.items():
        if cdef.prevents_acting:
            result |= tags.has(tag)
    return result


# --- d20 roll mechanics shared by every advantage-aware Mechanic -----------


def roll_d20(rng: BatchRNG, size: int, mode: AdvantageMode) -> np.ndarray:
    """One batch of ``size`` d20 rolls under `mode`: two dice, kept-highest
    for advantage or kept-lowest for disadvantage, one die for normal."""
    if mode == "advantage":
        first, second = rng.integers(1, 21, size=size), rng.integers(1, 21, size=size)
        rolls: np.ndarray = np.maximum(first, second)
        return rolls
    if mode == "disadvantage":
        first, second = rng.integers(1, 21, size=size), rng.integers(1, 21, size=size)
        rolls = np.minimum(first, second)
        return rolls
    return rng.integers(1, 21, size=size)


def d20_face_probabilities(mode: AdvantageMode) -> list[float]:
    """``P(roll == k)`` for ``k`` in ``1..20``, index ``0`` holding ``k=1``.

    Advantage: ``P(k) = (2k-1)/400`` (probability the max of two d20s is
    exactly ``k``). Disadvantage is its mirror: ``P(k) = (41-2k)/400``. Both
    close forms follow directly from order statistics of two uniform dice
    and are the exact (not approximated) distribution — every
    ``expected_value()`` built on this stays a true closed form, not an
    approximation."""
    if mode == "advantage":
        return [(2 * k - 1) / 400.0 for k in range(1, 21)]
    if mode == "disadvantage":
        return [(41 - 2 * k) / 400.0 for k in range(1, 21)]
    return [1 / 20.0] * 20
