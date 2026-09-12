---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "Huge dragon (CR 15) with lightning immunity, breath weapon, spellcasting, and legendary resistance."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Adult Bronze Dragon"
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[central-strait|Central Strait]]"
uid: 8fe05382-1aa0-4b84-9e40-7e932cdbf254
---

# Adult Bronze Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Adult Bronze Dragon"
size: Huge
type: dragon
alignment: "Lawful Good"
ac: 18
hp: 212
hit_dice: "17d12 + 102"
speed: "40 ft., Fly 80 ft., Swim 40 ft."
stats: [25, 10, 23, 16, 15, 20]
saves:
  - dex: 5
  - wis: 7
damage_immunities: "Lightning"
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
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of (A) Repulsion Breath or (B) Spellcasting to cast *Guiding Bolt* (level 2 version)."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +12, reach 10 ft. 16 (2d8 + 7) Slashing damage plus 5 (1d10) Lightning damage."
  - name: "Lightning Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 19, each creature in a 90-foot-long, 5-foot-wide Line. *Failure:* 55 (10d10) Lightning damage. *Success:* Half damage."
  - name: "Repulsion Breath"
    desc: "*Strength Saving Throw*: DC 19, each creature in a 30-foot Cone. *Failure:* The target is pushed up to 60 feet straight away from the dragon and has the Prone condition."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 17, +10 to hit with spell attacks): - **At Will:** *Detect Magic*, *Guiding Bolt*, *Shapechange*, *Speak with Animals*, *Thaumaturgy* - **1e/Day Each:** *Detect Thoughts*, *Water Breathing*"
legendary_actions:
  - name: "Guiding Light"
    desc: "The dragon uses Spellcasting to cast *Guiding Bolt* (level 2 version)."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
  - name: "Thunderclap"
    desc: "*Constitution Saving Throw*: DC 17, each creature in a 20-foot-radius Sphere [Area of Effect]|XPHB|Sphere centered on a point the dragon can see within 90 feet. *Failure:* 10 (3d6) Thunder damage, and the target has the Deafened condition until the end of its next turn."
```
