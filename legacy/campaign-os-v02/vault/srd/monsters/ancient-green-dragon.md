---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
found_at:
- "[[midchain-west|Midchain West]]"
- "[[verdant-teeth|Verdant Teeth]]"
tags: [combat]
summary: "Gargantuan ancient green dragon (CR 22) with poison breath, mind-affecting spells, and amphibious powers."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Ancient Green Dragon"
uid: f023ab14-ff13-4a78-a9c2-1041539d0246
---

# Ancient Green Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Ancient Green Dragon"
size: Gargantuan
type: dragon
alignment: "Lawful Evil"
ac: 21
hp: 402
hit_dice: "23d20 + 161"
speed: "40 ft., Fly 80 ft., Swim 40 ft."
stats: [27, 12, 25, 20, 17, 22]
saves:
  - dex: 8
  - wis: 10
damage_immunities: "Poison"
condition_immunities: "Poisoned"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 27"
languages: "Common, Draconic"
cr: 22
traits:
  - name: "Amphibious"
    desc: "The dragon can breathe air and water."
  - name: "Legendary Resistance (4/Day, or 5/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of Spellcasting to cast *Mind Spike* (level 5 version)."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +15, reach 15 ft. 17 (2d8 + 8) Slashing damage plus 10 (3d6) Poison damage."
  - name: "Poison Breath (Recharge 5-6)"
    desc: "*Constitution Saving Throw*: DC 22, each creature in a 90-foot Cone. *Failure:* 77 (22d6) Poison damage. *Success:* Half damage."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 21): - **At Will:** *Detect Magic*, *Mind Spike* - **1e/Day Each:** *Geas*, *Modify Memory*"
legendary_actions:
  - name: "Mind Invasion"
    desc: "The dragon uses Spellcasting to cast *Mind Spike* (level 5 version)."
  - name: "Noxious Miasma"
    desc: "*Constitution Saving Throw*: DC 21, each creature in a 30-foot-radius Sphere [Area of Effect]|XPHB|Sphere centered on a point the dragon can see within 90 feet. *Failure:* 17 (5d6) Poison damage, and the target takes a -2 penalty to AC until the end of its next turn. *Failure or Success*: The dragon can't take this action again until the start of its next turn."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
```
