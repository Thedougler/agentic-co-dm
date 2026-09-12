---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[central-strait|Central Strait]]"
tags: [combat]
summary: "Gargantuan ancient silver dragon (CR 23) with cold breath, paralyzing effects, and diverse arcane spellcasting abilities."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Ancient Silver Dragon"
uid: 48fd1e59-b5aa-44b7-b9c5-aa284f364a6a
---

# Ancient Silver Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Ancient Silver Dragon"
size: Gargantuan
type: dragon
alignment: "Lawful Good"
ac: 22
hp: 468
hit_dice: "24d20 + 216"
speed: "40 ft., Fly 80 ft."
stats: [30, 10, 29, 18, 15, 26]
saves:
  - dex: 7
  - wis: 9
damage_immunities: "Cold"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 26"
languages: "Common, Draconic"
cr: 23
traits:
  - name: "Legendary Resistance (4/Day, or 5/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of (A) Paralyzing Breath or (B) Spellcasting to cast *Ice Knife* (level 2 version)."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +17, reach 15 ft. 19 (2d8 + 10) Slashing damage plus 9 (2d8) Cold damage."
  - name: "Cold Breath (Recharge 5-6)"
    desc: "*Constitution Saving Throw*: DC 24, each creature in a 90-foot Cone. *Failure:* 67 (15d8) Cold damage. *Success:* Half damage."
  - name: "Paralyzing Breath"
    desc: "*Constitution Saving Throw*: DC 24, each creature in a 90-foot Cone. *First Failure* The target has the Incapacitated condition until the end of its next turn, when it repeats the save. *Second Failure* The target has the Paralyzed condition, and it repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 23, +15 to hit with spell attacks): - **At Will:** *Detect Magic*, *Hold Monster*, *Ice Knife*, *Shapechange* - **1e/Day Each:** *Control Weather*, *Ice Storm*, *Teleport*, *Zone of Truth*"
legendary_actions:
  - name: "Chill"
    desc: "The dragon uses Spellcasting to cast *Hold Monster*. The dragon can't take this action again until the start of its next turn."
  - name: "Cold Gale"
    desc: "*Dexterity Saving Throw*: DC 23, each creature in a 60-foot-long, 10-foot-wide Line. *Failure:* 14 (4d6) Cold damage, and the target is pushed up to 30 feet straight away from the dragon. *Success:* Half damage only. *Failure or Success*: The dragon can't take this action again until the start of its next turn."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
```
