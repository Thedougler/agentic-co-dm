---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 16 Lawful Good dragon with cold immunity, paralyzing and cold breaths, versatile spellcasting."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[crown-islands|Crown Islands]]"
statblock: inline
name: "Adult Silver Dragon"
uid: 68c61cc5-d86f-43be-b0ba-2449a422210f
---

# Adult Silver Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Adult Silver Dragon"
size: Huge
type: dragon
alignment: "Lawful Good"
ac: 19
hp: 216
hit_dice: "16d12 + 112"
speed: "40 ft., Fly 80 ft."
stats: [27, 10, 25, 16, 13, 22]
saves:
  - dex: 5
  - wis: 6
damage_immunities: "Cold"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 21"
languages: "Common, Draconic"
cr: 16
traits:
  - name: "Legendary Resistance (3/Day, or 4/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of (A) Paralyzing Breath or (B) Spellcasting to cast *Ice Knife*."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +13, reach 10 ft. 17 (2d8 + 8) Slashing damage plus 4 (1d8) Cold damage."
  - name: "Cold Breath (Recharge 5-6)"
    desc: "*Constitution Saving Throw*: DC 20, each creature in a 60-foot Cone. *Failure:* 54 (12d8) Cold damage. *Success:* Half damage."
  - name: "Paralyzing Breath"
    desc: "*Constitution Saving Throw*: DC 20, each creature in a 60-foot Cone. *First Failure* The target has the Incapacitated condition until the end of its next turn, when it repeats the save. *Second Failure* The target has the Paralyzed condition, and it repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 19, +11 to hit with spell attacks): - **At Will:** *Detect Magic*, *Hold Monster*, *Ice Knife*, *Shapechange* - **1e/Day Each:** *Ice Storm*, *Zone of Truth*"
legendary_actions:
  - name: "Chill"
    desc: "The dragon uses Spellcasting to cast *Hold Monster*. The dragon can't take this action again until the start of its next turn."
  - name: "Cold Gale"
    desc: "*Dexterity Saving Throw*: DC 19, each creature in a 60-foot-long, 10-foot-wide Line. *Failure:* 14 (4d6) Cold damage, and the target is pushed up to 30 feet straight away from the dragon. *Success:* Half damage only. *Failure or Success*: The dragon can't take this action again until the start of its next turn."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
```
