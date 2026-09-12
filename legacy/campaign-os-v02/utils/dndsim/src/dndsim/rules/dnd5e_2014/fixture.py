"""The hardcoded two-combatant fixture used by ``dndsim sim-combat``.

Loosely modeled on a real Shattered Sea matchup (a duelist vs. a grung
skirmisher) purely as flavor; the numbers exist to give the walking
skeleton something concrete to simulate, not to represent tuned canon
content.
"""

from __future__ import annotations

from dataclasses import dataclass

from dndsim.core.entity import Attribute, Entity
from dndsim.rules.dnd5e_2014.compile import CompiledStatblock


@dataclass(slots=True)
class CombatantSpec:
    """A combatant's fixed stat block plus its damage-dice shape.

    The positional/legendary/concentration fields (issue #59) all default to
    the two-combatant walking skeleton's implicit shape — melee, 30 ft.
    speed, no legendary actions, no lair, not concentrating — so every
    existing fixture and test built before the party-vs-party loop keeps
    working unchanged.
    """

    entity: Entity
    hp_max: int
    damage_dice_count: int
    damage_dice_sides: int
    speed_ft: int = 30
    is_melee: bool = True
    reach_ft: float = 5.0
    range_ft: float | None = None
    range_long_ft: float | None = None
    legendary: bool = False
    has_lair: bool = False
    con_bonus: int = 0
    starts_concentrating: bool = False
    # Issue #60: the real compiled kit `run_combat` executes when present —
    # `compiled_actions`/`routine`/`ability_primitives` — instead of the flat
    # single-attack shape the fields above still carry, since that shape
    # stays what opportunity-attack/legendary-action fallbacks and any
    # combatant with no compiled statblock resolve through unchanged.
    compiled: CompiledStatblock | None = None
    #: Issue #55: this combatant's own Exhaustion level (0 = unaffected).
    #: No page currently authors this (there is no `sim:` fence key for it
    #: yet — a named, separately-scoped follow-up); every existing
    #: statblock therefore compiles to 0 and simulates identically under
    #: either Rules pack. Its edition-specific resolution (attack/save
    #: penalty, speed) is looked up by `combat.py` from the active
    #: `dndsim.rules.exhaustion.exhaustion_rules` entry, never branched on
    #: here.
    exhaustion_level: int = 0

    @property
    def armor_class(self) -> int:
        return int(self.entity.attr("armor_class").value())

    @property
    def attack_bonus(self) -> int:
        return int(self.entity.attr("attack_bonus").value())

    @property
    def damage_bonus(self) -> int:
        return int(self.entity.attr("damage_bonus").value())


def make_combatant(
    *,
    entity_id: str,
    name: str,
    hp_max: int,
    armor_class: int,
    attack_bonus: int,
    damage_bonus: int,
    damage_dice_count: int,
    damage_dice_sides: int,
    speed_ft: int = 30,
    is_melee: bool = True,
    reach_ft: float = 5.0,
    range_ft: float | None = None,
    range_long_ft: float | None = None,
    legendary: bool = False,
    has_lair: bool = False,
    con_bonus: int = 0,
    starts_concentrating: bool = False,
    compiled: CompiledStatblock | None = None,
    exhaustion_level: int = 0,
) -> CombatantSpec:
    entity = Entity(
        id=entity_id,
        name=name,
        attributes={
            "armor_class": Attribute(name="armor_class", base=armor_class),
            "attack_bonus": Attribute(name="attack_bonus", base=attack_bonus),
            "damage_bonus": Attribute(name="damage_bonus", base=damage_bonus),
        },
    )
    return CombatantSpec(
        entity=entity,
        hp_max=hp_max,
        damage_dice_count=damage_dice_count,
        damage_dice_sides=damage_dice_sides,
        speed_ft=speed_ft,
        is_melee=is_melee,
        reach_ft=reach_ft,
        range_ft=range_ft,
        range_long_ft=range_long_ft,
        legendary=legendary,
        has_lair=has_lair,
        con_bonus=con_bonus,
        starts_concentrating=starts_concentrating,
        compiled=compiled,
        exhaustion_level=exhaustion_level,
    )


TWO_COMBATANT_FIXTURE: tuple[CombatantSpec, CombatantSpec] = (
    make_combatant(
        entity_id="dnd5e_2014:combatant/perrin",
        name="Perrin",
        hp_max=38,
        armor_class=17,
        attack_bonus=7,
        damage_bonus=4,
        damage_dice_count=1,
        damage_dice_sides=8,
    ),
    make_combatant(
        entity_id="dnd5e_2014:combatant/grung-skirmisher",
        name="Grung Skirmisher",
        hp_max=36,
        armor_class=15,
        attack_bonus=5,
        damage_bonus=3,
        damage_dice_count=1,
        damage_dice_sides=6,
    ),
)


#: A 3-vs-3 fixture for the party-vs-party loop (issue #59): a melee/melee/
#: ranged party against two ordinary skirmishers plus one legendary,
#: lair-bearing boss — real enough to exercise positioning (the archer
#: kites, the skirmishers close), a concentration break (Ysolde), and both
#: the legendary and lair encounter-timeline windows in one encounter,
#: rather than only unit-testing each mechanism slice in isolation.
PARTY_VS_ENEMIES_FIXTURE: tuple[list[CombatantSpec], list[CombatantSpec]] = (
    [
        make_combatant(
            entity_id="dnd5e_2014:combatant/perrin",
            name="Perrin",
            hp_max=46,
            armor_class=17,
            attack_bonus=7,
            damage_bonus=4,
            damage_dice_count=1,
            damage_dice_sides=8,
        ),
        make_combatant(
            entity_id="dnd5e_2014:combatant/ysolde",
            name="Ysolde",
            hp_max=52,
            armor_class=18,
            attack_bonus=6,
            damage_bonus=4,
            damage_dice_count=1,
            damage_dice_sides=10,
            con_bonus=2,
            starts_concentrating=True,
        ),
        make_combatant(
            entity_id="dnd5e_2014:combatant/rowan",
            name="Rowan",
            hp_max=36,
            armor_class=15,
            attack_bonus=6,
            damage_bonus=3,
            damage_dice_count=1,
            damage_dice_sides=8,
            is_melee=False,
            range_ft=80,
            range_long_ft=320,
        ),
    ],
    [
        make_combatant(
            entity_id="dnd5e_2014:combatant/grung-skirmisher-a",
            name="Grung Skirmisher A",
            hp_max=36,
            armor_class=15,
            attack_bonus=5,
            damage_bonus=3,
            damage_dice_count=1,
            damage_dice_sides=6,
        ),
        make_combatant(
            entity_id="dnd5e_2014:combatant/grung-skirmisher-b",
            name="Grung Skirmisher B",
            hp_max=36,
            armor_class=15,
            attack_bonus=5,
            damage_bonus=3,
            damage_dice_count=1,
            damage_dice_sides=6,
        ),
        make_combatant(
            entity_id="dnd5e_2014:combatant/grung-chief",
            name="Grung Chief",
            hp_max=54,
            armor_class=16,
            attack_bonus=6,
            damage_bonus=3,
            damage_dice_count=1,
            damage_dice_sides=8,
            reach_ft=10,
            legendary=True,
            has_lair=True,
        ),
    ],
)
