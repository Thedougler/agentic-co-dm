"""The 2014 SRD (5.1) exhaustion table — a tiered ladder, not a flat
number: disadvantage on saving throws unlocks at level 3, speed halves at
level 2 and zeroes at level 5. Registered under :data:`RULES_ID` into the
shared :data:`~dndsim.rules.exhaustion.exhaustion_rules` registry; the
2024 pack's own numbers (`dndsim.rules.dnd5e_2024.exhaustion`) are a
different VALUE under a different id, never a second copy of the shape
this module fills in.

Attack-roll disadvantage (this table's own level-3 clause also covers
attack rolls) is NOT wired into an actual attack roll this pass: no single
call site in ``combat.py`` assembles condition-driven attack advantage
uniformly (several reaction/opportunity-attack paths already pass a bare
``"normal"`` literal — see e.g. ``_register_extra_attack_reaction``), so
retrofitting one condition's disadvantage there risks a much larger,
differently-scoped change than this issue's slice. Saving throws (a
single, uniform call site — :func:`~dndsim.rules.dnd5e_2014.combat.
_save_advantage_mode`) and speed (a single call site —
``actor.pos.start_turn``) are wired; hit-point-maximum halving (level 4)
is not, since it needs ``hp_max``/``ResourcePool`` plumbing outside this
slice's scope. Each is a named, narrow follow-up, not a silently dropped
requirement.
"""

from __future__ import annotations

from dndsim.rules.exhaustion import ExhaustionRules, exhaustion_rules

RULES_ID = "dnd5e_2014:rules/exhaustion"

exhaustion_rules.register_value(
    RULES_ID,
    ExhaustionRules(
        id=RULES_ID,
        d20_penalty_per_level=0,
        save_disadvantage_from_level=3,
        speed_halved_from_level=2,
        speed_zero_from_level=5,
        death_at_level=6,
    ),
)
