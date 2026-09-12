---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "Huge dragon (CR 14) with acid breath, Cloud of Insects poison attack, and Fear-based spellcasting."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Adult Black Dragon"
found_at:
- "[[doldrums|Doldrums]]"
- "[[midchain-south|Midchain South]]"
uid: 259f0d37-fae5-444c-a80a-2f9496c1ed64
---

# Adult Black Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Adult Black Dragon"
size: Huge
type: dragon
alignment: "Chaotic Evil"
ac: 19
hp: 195
hit_dice: "17d12 + 85"
speed: "40 ft., Fly 80 ft., Swim 40 ft."
stats: [23, 14, 21, 14, 13, 19]
saves:
  - dex: 7
  - wis: 6
damage_immunities: "Acid"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 21"
languages: "Common, Draconic"
cr: 14
traits:
  - name: "Amphibious"
    desc: "The dragon can breathe air and water."
  - name: "Legendary Resistance (3/Day, or 4/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of Spellcasting to cast *Acid Arrow* (level 3 version)."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +11, reach 10 ft. 13 (2d6 + 6) Slashing damage plus 4 (1d8) Acid damage."
  - name: "Acid Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 18, each creature in a 60-foot-long, 5-foot-wide Line. *Failure:* 54 (12d8) Acid damage. *Success:* Half damage."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 17, +9 to hit with spell attacks): - **At Will:** *Detect Magic*, *Fear*, *Acid Arrow* - **1e/Day Each:** *Speak with Dead*, *Vitriolic Sphere*"
legendary_actions:
  - name: "Cloud of Insects"
    desc: "*Dexterity Saving Throw*: DC 17, one creature the dragon can see within 120 feet. *Failure:* 22 (4d10) Poison damage, and the target has Disadvantage on saving throws to maintain Concentration until the end of its next turn. *Failure or Success*: The dragon can't take this action again until the start of its next turn."
  - name: "Frightful Presence"
    desc: "The dragon uses Spellcasting to cast *Fear*. The dragon can't take this action again until the start of its next turn."
  - name: "Pounce"
    desc: "The dragon can move up to half its Speed, and it makes one Rend attack."
```
