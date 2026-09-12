---
type: monster
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 22 Gargantuan Lawful Good amphibious dragon with Lightning Breath and Repulsion Breath."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[central-strait|Central Strait]]"
statblock: inline
name: "Ancient Bronze Dragon"
uid: 89aa769c-ad3f-40d3-ac60-8b02868f06fb
---

# Ancient Bronze Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Ancient Bronze Dragon"
size: Gargantuan
type: dragon
alignment: "Lawful Good"
ac: 22
hp: 444
hit_dice: "24d20 + 192"
speed: "40 ft., Fly 80 ft., Swim 40 ft."
stats: [29, 10, 27, 18, 17, 25]
saves:
  - dex: 7
  - wis: 10
damage_immunities: "Lightning"
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
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of (A) Repulsion Breath or (B) Spellcasting to cast *Guiding Bolt* (level 2 version)."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +16, reach 15 ft. 18 (2d8 + 9) Slashing damage plus 9 (2d8) Lightning damage."
  - name: "Lightning Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 23, each creature in a 120-foot-long, 10-foot-wide Line. *Failure:* 82 (15d10) Lightning damage. *Success:* Half damage."
  - name: "Repulsion Breath"
    desc: "*Strength Saving Throw*: DC 23, each creature in a 30-foot Cone. *Failure:* The target is pushed up to 60 feet straight away from the dragon and has the Prone condition."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 22, +14 to hit with spell attacks): - **At Will:** *Detect Magic*, *Guiding Bolt*, *Shapechange*, *Speak with Animals*, *Thaumaturgy* - **1e/Day Each:** *Detect Thoughts*, *Control Water*, *Scrying*, *Water Breathing*"
legendary_actions:
  - name: "Guiding Light"
    desc: "The dragon uses Spellcasting to cast *Guiding Bolt* (level 2 version)."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
  - name: "Thunderclap"
    desc: "*Constitution Saving Throw*: DC 22, each creature in a 20-foot-radius Sphere [Area of Effect]|XPHB|Sphere centered on a point the dragon can see within 120 feet. *Failure:* 13 (3d8) Thunder damage, and the target has the Deafened condition until the end of its next turn."
```
