---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[redwind-isles|Redwind Isles]]"
tags: [combat]
summary: "Gargantuan ancient red dragon (CR 24) with devastating fire breath, scorching ray spells, and commanding presence."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Ancient Red Dragon"
uid: ff692309-da4e-4b09-8cd7-43de24ac334d
---

# Ancient Red Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Ancient Red Dragon"
size: Gargantuan
type: dragon
alignment: "Chaotic Evil"
ac: 22
hp: 507
hit_dice: "26d20 + 234"
speed: "40 ft., Climb 40 ft., Fly 80 ft."
stats: [30, 10, 29, 18, 15, 27]
saves:
  - dex: 7
  - wis: 9
damage_immunities: "Fire"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 26"
languages: "Common, Draconic"
cr: 24
traits:
  - name: "Legendary Resistance (4/Day, or 5/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of Spellcasting to cast *Scorching Ray* (level 3 version)."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +17, reach 15 ft. 19 (2d8 + 10) Slashing damage plus 10 (3d6) Fire damage."
  - name: "Fire Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 24, each creature in a 90-foot Cone. *Failure:* 91 (26d6) Fire damage. *Success:* Half damage."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 23, +15 to hit with spell attacks): - **At Will:** *Command*, *Detect Magic*, *Scorching Ray* - **1e/Day Each:** *Fireball*, *Scrying*"
legendary_actions:
  - name: "Commanding Presence"
    desc: "The dragon uses Spellcasting to cast *Command* (level 2 version). The dragon can't take this action again until the start of its next turn."
  - name: "Fiery Rays"
    desc: "The dragon uses Spellcasting to cast *Scorching Ray* (level 3 version). The dragon can't take this action again until the start of its next turn."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
```
