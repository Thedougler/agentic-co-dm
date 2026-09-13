---
type: pc
subtype: character-sheet
summary: "Transcribed D&D Beyond character sheet for Catarina Da'Virelli, Artificer 5 (Artillerist)."
pc: "catarina-davirelli"
alias: "cd"
pc_level: 5
class_levels: "Artificer 5 (Artillerist)"
last_synced: "2026-07-25"
tags: [arcane]
uid: 4e66b437-2b9c-4227-b967-3743b8f41ee5
---

From D&D Beyond (exported by player: nickdavenock). PDF: `_assets/character-sheets/catarina-davirelli-character-sheet.pdf`.

`[verify]` Flintlock Pistol to-hit (+3) doesn't match DEX mod (+2) + skill bonus (+3) = +5 if she's proficient with firearms. Sheet shows +3 as printed, transcribed as-is, not corrected.

## What lives here, and what does not

The Human-readable transcription lives in `vault/campaigns/shattered-sea/pcs/`, one governed page per
facet, each instantiated from its own Template:

| Facet | Page | Template |
|---|---|---|
| Ability scores, saves, skills, speeds, proficiencies | `vault/campaigns/shattered-sea/pcs/stats/catarina-davirelli-stats.md` | `_templates/pc-stats.md` |
| Traits, features, actions, bonus actions, reactions, feats | `vault/campaigns/shattered-sea/pcs/abilities/catarina-davirelli-abilities.md` | `_templates/pc-abilities.md` |
| Spellcasting, cantrips, known/prepared, slots | `vault/campaigns/shattered-sea/pcs/spells/catarina-davirelli-spells.md` | `_templates/pc-spells.md` |
| Attunement, carried gear, caches, currency | `vault/campaigns/shattered-sea/pcs/inventory/catarina-davirelli-inventory.md` | `_templates/pc-inventory.md` |
| AC, max HP, class levels, total level | `vault/campaigns/shattered-sea/pcs/catarina-davirelli.md` frontmatter | `_templates/pc.md` |

## Combatant Block

```statblock
layout: Basic 5e Layout
name: Catarina Da'Virelli
size: Medium
type: humanoid
alignment: neutral good
ac: 16
hp: 38
hit_dice: "5d8"
speed: "30 ft."
stats: [13, 14, 15, 20, 12, 10]
saves: { str: 1, dex: 2, con: 5, int: 8, wis: 1, cha: 0 }
actions:
  # Fire Bolt/Shocking Grasp removed as hand-coded actions — the sheet's
  # printed 2d10/2d8 dice already match each cantrip's own SRD page at
  # level 5 (cantrip_scaling), so both now come from sim.spellcasting.known
  # below instead of being re-encoded here (sheet and page agree, no
  # divergence to preserve).
  - name: "Flintlock Pistol"
    # [verify] sheet prints +3 to-hit; doesn't match DEX+prof (+5) if
    # proficient with firearms — transcribed as printed, not corrected.
    desc: "Ranged Weapon Attack: +3 to hit, range 30/90 ft., one target. Hit: 8 (1d10 + 3) piercing damage."
    sim: { id: flintlock_pistol }
bonus_actions:
  # [srd vault/srd/classes/subclasses/artificer-artillerist.md]
  # Eldritch Cannon — Flamethrower/Force Ballista, exact page dice/DC.
  # Both draw on the same 1/long-rest eldritch_cannon resource, so this
  # models only a SINGLE activation per long rest — an approximation of
  # the summon (the real cannon persists once created and can be
  # activated again every turn for free; this sim has no
  # summon-as-persistent-object primitive, so the whole lifecycle is
  # compressed into one paid use). Protector's temp HP and the cannon's
  # own AC 18/HP (5 × artificer level) statblock are not modeled at all.
  - name: "Eldritch Cannon — Flamethrower"
    desc: "*Dexterity Saving Throw*: DC 17, each creature in a 15-foot Cone. *Failure:* 9 (2d8) Fire damage. *Success:* Half damage."
    sim: { id: eldritch_cannon_flamethrower, cost: { resource: eldritch_cannon, spend: 1 } }
  - name: "Eldritch Cannon — Force Ballista"
    # 5-ft push on a hit not modeled (no forced-movement primitive).
    desc: "Ranged Spell Attack: +9 to hit, range 120 ft., one target. Hit: 9 (2d8) force damage."
    sim: { id: eldritch_cannon_force_ballista, cost: { resource: eldritch_cannon, spend: 1 } }
reactions:
  # [sheet+srd vault/srd/spells/abjuration/absorb-elements.md] Resistance to
  # the triggering damage type, modeled as a flat 50% reduction. The
  # retaliatory 1d6 rider on her next melee hit isn't modeled (no
  # next-turn damage-boost primitive tied to a reaction).
  - name: "Absorb Elements"
    desc: "When Catarina takes acid, cold, fire, lightning, or thunder damage, she can take a Reaction to gain Resistance to that damage type until the start of her next turn."
    sim: { id: absorb_elements, kind: damage_reduction_pct, fraction: 0.5,
           damage_types: [acid, cold, fire, lightning, thunder], trigger: self_hit,
           cost: { resource: slot_1, spend: 1 } }
  # Shield removed as a hand-coded reaction — now compiled from
  # sim.spellcasting.known below (its reaction_ac_bonus modifier is
  # checked automatically, same as every other Shield-casting PC sheet).
sim:
  side: party
  level: 5
  initiative: 7 # DEX +2 + Alert +5, folded per sheet
  concentration_save: 5 # plain CON save, no War Caster per sheet note
  resources:
    - { id: slot_1, max: 4, recharge: long_rest }
    - { id: slot_2, max: 2, recharge: long_rest }
    - { id: eldritch_cannon, max: 1, recharge: long_rest }
  spellcasting:
    # DC/attack_bonus are the sheet's printed values (already include the
    # All-Purpose Tool +1). Dice come from each spell's own SRD page
    # [sheet+srd] — checked this turn, every one confirmed on her prepared
    # list (Identity/Spellcasting sections above). Cure Wounds, Detect
    # Magic, and the rest of her long utility list stay out of known: —
    # candidates checked this pass were exactly the ones with a
    # damage/save line on the sheet (Fire Bolt, Shocking Grasp, Scorching
    # Ray, Shatter, Thunderwave, Faerie Fire, Web, Grease, False Life,
    # Aid, Blur, Magic Weapon, Catapult, Shield).
    - { ability: int, dc: 17, attack_bonus: 9, level: 5, ability_mod: 5,
        slots: { 1: slot_1, 2: slot_2 },
        known: ["Fire Bolt", "Shocking Grasp", "Scorching Ray", "Shatter",
                "Thunderwave", "Faerie Fire", "Web", "Grease", "False Life",
                "Aid", "Blur", "Magic Weapon", "Catapult", "Shield"] }
  routine:
    action: [fire_bolt, flintlock_pistol]
    bonus: []
```
