"""The 2024 SRD (5.2) exhaustion rule
(`vault/srd/rules/exhaustion.md`) — two flat,
continuously-scaling penalties in place of 2014's tiered table: every D20
Test (an attack roll or a saving throw) is reduced by 2 x level, and Speed
is reduced by 5 ft x level. Registered under :data:`RULES_ID` into the
shared :data:`~dndsim.rules.exhaustion.exhaustion_rules` registry — the
2014 pack's own numbers (`dndsim.rules.dnd5e_2014.exhaustion`) are a
different VALUE under a different id, never a second copy of the shape.

The D20 Test penalty is wired onto attack rolls and saving throws (the two
d20 tests this engine actually resolves); an ability check has no
Primitive/Mechanic in this engine at all, so 2024's own "ability checks
count too" clause is not modeled — a real, named gap, not a silent one.
"""

from __future__ import annotations

from dndsim.rules.exhaustion import ExhaustionRules, exhaustion_rules

RULES_ID = "dnd5e_2024:rules/exhaustion"

exhaustion_rules.register_value(
    RULES_ID,
    ExhaustionRules(
        id=RULES_ID,
        d20_penalty_per_level=2,
        save_disadvantage_from_level=None,
        speed_penalty_ft_per_level=5,
        death_at_level=6,
    ),
)
