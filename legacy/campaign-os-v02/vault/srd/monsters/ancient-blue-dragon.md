---
type: monster
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 23 Gargantuan Lawful Evil dragon with Lightning Breath, Rend attacks, and spellcasting."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[redwind-isles|Redwind Isles]]"
- "[[crown-islands|Crown Islands]]"
statblock: inline
name: "Ancient Blue Dragon"
uid: 2eef4e91-3bbc-4a9b-ab84-c7e405baad7d
---

# Ancient Blue Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Ancient Blue Dragon"
size: Gargantuan
type: dragon
alignment: "Lawful Evil"
ac: 22
hp: 481
hit_dice: "26d20 + 208"
speed: "40 ft., Burrow 40 ft., Fly 80 ft."
stats: [29, 10, 27, 18, 17, 25]
saves:
  - dex: 7
  - wis: 10
damage_immunities: "Lightning"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 27"
languages: "Common, Draconic"
cr: 23
traits:
  - name: "Legendary Resistance (4/Day, or 5/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of Spellcasting to cast *Shatter* (level 3 version)."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +16, reach 15 ft. 18 (2d8 + 9) Slashing damage plus 11 (2d10) Lightning damage."
  - name: "Lightning Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 23, each creature in a 120-foot-long, 10-foot-wide Line. *Failure:* 88 (16d10) Lightning damage. *Success:* Half damage."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 22): - **At Will:** *Detect Magic*, *Invisibility*, *Mage Hand*, *Shatter* - **1e/Day Each:** *Scrying*, *Sending*"
legendary_actions:
  - name: "Cloaked Flight"
    desc: "The dragon uses Spellcasting to cast *Invisibility* on itself, and it can fly up to half its Fly Speed. The dragon can't take this action again until the start of its next turn."
  - name: "Sonic Boom"
    desc: "The dragon uses Spellcasting to cast *Shatter* (level 3 version). The dragon can't take this action again until the start of its next turn."
  - name: "Tail Swipe"
    desc: "The dragon makes one Rend attack."
```
