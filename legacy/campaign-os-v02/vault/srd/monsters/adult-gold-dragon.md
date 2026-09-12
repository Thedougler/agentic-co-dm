---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 17 Lawful Good dragon with fire immunity, legendary resistance, and versatile spellcasting."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Adult Gold Dragon"
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[tail|Tail]]"
uid: 03492b4d-2075-42f9-8b49-ba9736191bce
---

# Adult Gold Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Adult Gold Dragon"
size: Huge
type: dragon
alignment: "Lawful Good"
ac: 19
hp: 243
hit_dice: "18d12 + 126"
speed: "40 ft., Fly 80 ft., Swim 40 ft."
stats: [27, 14, 25, 16, 15, 24]
saves:
  - dex: 8
  - wis: 8
damage_immunities: "Fire"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 24"
languages: "Common, Draconic"
cr: 17
traits:
  - name: "Amphibious"
    desc: "The dragon can breathe air and water."
  - name: "Legendary Resistance (3/Day, or 4/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of (A) Spellcasting to cast *Guiding Bolt* (level 2 version) or (B) Weakening Breath."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +14, reach 10 ft. 17 (2d8 + 8) Slashing damage plus 4 (1d8) Fire damage."
  - name: "Fire Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 21, each creature in a 60-foot Cone. *Failure:* 66 (12d10) Fire damage. *Success:* Half damage."
  - name: "Weakening Breath"
    desc: "*Strength Saving Throw*: DC 21, each creature that isn't currently affected by this breath in a 60-foot Cone. *Failure:* The target has Disadvantage on Strength-based D20 Test and subtracts 3 (1d6) from its damage rolls. It repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 21, +13 to hit with spell attacks): - **At Will:** *Detect Magic*, *Guiding Bolt*, *Shapechange* - **1e/Day Each:** *Flame Strike*, *Zone of Truth*"
legendary_actions:
  - name: "Banish"
    desc: "*Charisma Saving Throw*: DC 21, one creature the dragon can see within 120 feet. *Failure:* 10 (3d6) Force damage, and the target has the Incapacitated condition and is transported to a harmless demiplane until the start of the dragon's next turn, at which point it reappears in an unoccupied space of the dragon's choice within 120 feet of the dragon. *Failure or Success*: The dragon can't take this action again until the start of its next turn."
  - name: "Guiding Light"
    desc: "The dragon uses Spellcasting to cast *Guiding Bolt* (level 2 version)."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
```
