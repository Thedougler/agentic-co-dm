"""Exhaustion — the D&D 5e condition whose resolution genuinely differs
between the 2014 and 2024 editions (issue #55: the ADR-0007 payoff made
concrete). The 2014 SRD (5.1) resolves it as a tiered table: a creature's
own exhaustion level unlocks successive penalties as it climbs (disadvantage
on saving throws at level 3+, speed halved at level 2+ and zero at level 5+).
The 2024 SRD (5.2, `vault/srd/rules/exhaustion.md`)
replaces the table with two flat, continuously-scaling penalties: every
D20 Test (an attack roll or a saving throw) is reduced by 2 x level, and
Speed is reduced by 5 ft x level. Both editions agree a creature dies at
level 6.

:class:`ExhaustionRules` is the shared SHAPE (mirroring
:class:`~dndsim.rules.dnd5e_2014.conditions.ConditionDef`'s own
data-not-branch pattern) — one edition's actual numbers are never
duplicated as a second copy of this class, only as a second frozen VALUE
registered under :data:`exhaustion_rules`. This module holds no ruleset
opinion of its own (no default numbers): it is the contract both
`dndsim.rules.dnd5e_2014.exhaustion` and `dndsim.rules.dnd5e_2024.exhaustion`
populate, sitting beside those packages rather than inside either one
(neither edition owns a rule both of them implement) and outside
`dndsim.core` (exhaustion is 5e vocabulary, which core may not know —
ADR-0007).
"""

from __future__ import annotations

from dataclasses import dataclass

from dndsim.core.registry import Registry


@dataclass(frozen=True, slots=True)
class ExhaustionRules:
    """One edition's exhaustion resolution, as data.

    ``d20_penalty_per_level``: flat subtraction from an attack roll or a
    saving throw per exhaustion level (2024's "D20 Test" rule) — 0 in an
    edition that uses disadvantage instead of a flat number.
    ``save_disadvantage_from_level``: the level at/above which every saving
    throw is rolled at disadvantage (2014's tiered table) — ``None`` if
    this edition never does this (2024 uses the flat penalty instead).
    ``speed_penalty_ft_per_level``: flat feet subtracted from speed per
    level (2024) — ``None`` if this edition uses the tiered halved/zero
    steps below instead.
    ``speed_halved_from_level`` / ``speed_zero_from_level``: the levels
    at/above which speed is halved / reduced to 0 (2014's tiered table) —
    ``None`` if this edition uses the flat per-level penalty instead.
    ``death_at_level``: the level at which the creature dies — shared by
    both editions, carried here rather than re-derived at each call site.
    """

    id: str
    d20_penalty_per_level: int = 0
    save_disadvantage_from_level: int | None = None
    speed_penalty_ft_per_level: int | None = None
    speed_halved_from_level: int | None = None
    speed_zero_from_level: int | None = None
    death_at_level: int = 6

    def d20_penalty(self, level: int) -> int:
        """The flat subtraction this level applies to an attack roll or a
        saving throw — 0 for an edition (or a level) that uses disadvantage
        instead of a number, or for a non-exhausted combatant."""
        if level <= 0:
            return 0
        return self.d20_penalty_per_level * level

    def imposes_save_disadvantage(self, level: int) -> bool:
        """Whether this level rolls every saving throw at disadvantage."""
        return self.save_disadvantage_from_level is not None and level >= (
            self.save_disadvantage_from_level
        )

    def effective_speed_ft(self, level: int, base_speed_ft: int) -> int:
        """``base_speed_ft`` after this level's speed penalty — the tiered
        halved-then-zero steps, or the flat per-level reduction, whichever
        this edition defines (never both; a level of 0 always returns
        ``base_speed_ft`` unchanged)."""
        if level <= 0:
            return base_speed_ft
        speed = base_speed_ft
        if self.speed_zero_from_level is not None and level >= self.speed_zero_from_level:
            return 0
        if self.speed_halved_from_level is not None and level >= self.speed_halved_from_level:
            speed = speed // 2
        if self.speed_penalty_ft_per_level is not None:
            speed = max(0, speed - self.speed_penalty_ft_per_level * level)
        return speed

    def is_dead(self, level: int) -> bool:
        return level >= self.death_at_level


#: Keyed by ``"<pack-id>:rules/exhaustion"`` — at most one edition's value
#: is ever registered per process (``dndsim.plugins.load_rules_packs``
#: loads exactly one Rules pack's entry point), but both editions' ids are
#: valid keys here simultaneously, matching how ``policies``/``mechanics``
#: registries hold every registered id regardless of which one a given run
#: selects.
exhaustion_rules: Registry[ExhaustionRules] = Registry("dndsim.rules.exhaustion")
