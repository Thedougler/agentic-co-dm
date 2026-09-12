---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 15 Lawful Evil dragon with poison immunity, mind-themed spellcasting, and poison breath."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Adult Green Dragon"
found_at:
- "[[midchain-west|Midchain West]]"
- "[[verdant-teeth|Verdant Teeth]]"
uid: c6d956f2-8f5a-47a7-a877-bbca36506609
---

# Adult Green Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Adult Green Dragon"
size: Huge
type: dragon
alignment: "Lawful Evil"
ac: 19
hp: 207
hit_dice: "18d12 + 90"
speed: "40 ft., Fly 80 ft., Swim 40 ft."
stats: [23, 12, 21, 18, 15, 18]
saves:
  - dex: 6
  - wis: 7
damage_immunities: "Poison"
condition_immunities: "Poisoned"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 22"
languages: "Common, Draconic"
cr: 15
traits:
  - name: "Amphibious"
    desc: "The dragon can breathe air and water."
  - name: "Legendary Resistance (3/Day, or 4/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of Spellcasting to cast *Mind Spike* (level 3 version)."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +11, reach 10 ft. 15 (2d8 + 6) Slashing damage plus 7 (2d6) Poison damage."
  - name: "Poison Breath (Recharge 5-6)"
    desc: "*Constitution Saving Throw*: DC 18, each creature in a 60-foot Cone. *Failure:* 56 (16d6) Poison damage. *Success:* Half damage."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 17): - **At Will:** *Detect Magic*, *Mind Spike* - **1/Day Each:** *Geas*"
legendary_actions:
  - name: "Mind Invasion"
    desc: "The dragon uses Spellcasting to cast *Mind Spike* (level 3 version)."
  - name: "Noxious Miasma"
    desc: "*Constitution Saving Throw*: DC 17, each creature in a 20-foot-radius Sphere [Area of Effect]|XPHB|Sphere centered on a point the dragon can see within 90 feet. *Failure:* 7 (2d6) Poison damage, and the target takes a -2 penalty to AC until the end of its next turn. *Failure or Success*: The dragon can't take this action again until the start of its next turn."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
```
