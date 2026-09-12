---
type: monster
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 21 Gargantuan Chaotic Evil dragon with Acid Breath, Rend attacks, and spellcasting."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[doldrums|Doldrums]]"
- "[[the-drowned-maw|The Drowned Maw]]"
statblock: inline
name: "Ancient Black Dragon"
uid: 3220260c-5e0f-4988-8b52-d96a55dbe774
---

# Ancient Black Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Ancient Black Dragon"
size: Gargantuan
type: dragon
alignment: "Chaotic Evil"
ac: 22
hp: 367
hit_dice: "21d20 + 147"
speed: "40 ft., Fly 80 ft., Swim 40 ft."
stats: [27, 14, 25, 16, 15, 22]
saves:
  - dex: 9
  - wis: 9
damage_immunities: "Acid"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 26"
languages: "Common, Draconic"
cr: 21
traits:
  - name: "Amphibious"
    desc: "The dragon can breathe air and water."
  - name: "Legendary Resistance (4/Day, or 5/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of Spellcasting to cast *Acid Arrow* (level 4 version)."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +15, reach 15 ft. 17 (2d8 + 8) Slashing damage plus 9 (2d8) Acid damage."
  - name: "Acid Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 22, each creature in a 90-foot-long, 10-foot-wide Line. *Failure:* 67 (15d8) Acid damage. *Success:* Half damage."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 21, +13 to hit with spell attacks): - **At Will:** *Detect Magic*, *Fear*, *Acid Arrow* - **1e/Day Each:** *Create Undead*, *Speak with Dead*, *Vitriolic Sphere*"
legendary_actions:
  - name: "Cloud of Insects"
    desc: "*Dexterity Saving Throw*: DC 21, one creature the dragon can see within 120 feet. *Failure:* 33 (6d10) Poison damage, and the target has Disadvantage on saving throws to maintain Concentration until the end of its next turn. *Failure or Success*: The dragon can't take this action again until the start of its next turn."
  - name: "Frightful Presence"
    desc: "The dragon uses Spellcasting to cast *Fear*. The dragon can't take this action again until the start of its next turn."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
```
