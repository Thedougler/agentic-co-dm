---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 17 Chaotic Evil dragon with fire immunity, fire breath, and offensive spellcasting."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Adult Red Dragon"
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[midchain-south|Midchain South]]"
uid: 5a4f2f17-59d5-4b24-baa8-75f001efaf52
---

# Adult Red Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Adult Red Dragon"
size: Huge
type: dragon
alignment: "Chaotic Evil"
ac: 19
hp: 256
hit_dice: "19d12 + 133"
speed: "40 ft., Climb 40 ft., Fly 80 ft."
stats: [27, 10, 25, 16, 13, 23]
saves:
  - dex: 6
  - wis: 7
damage_immunities: "Fire"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 23"
languages: "Common, Draconic"
cr: 17
traits:
  - name: "Legendary Resistance (3/Day, or 4/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of Spellcasting to cast *Scorching Ray*."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +14, reach 10 ft. 13 (1d10 + 8) Slashing damage plus 5 (2d4) Fire damage."
  - name: "Fire Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 21, each creature in a 60-foot Cone. *Failure:* 59 (17d6) Fire damage. *Success:* Half damage."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 20, +12 to hit with spell attacks): - **At Will:** *Command*, *Detect Magic*, *Scorching Ray* - **1/Day Each:** *Fireball*"
legendary_actions:
  - name: "Commanding Presence"
    desc: "The dragon uses Spellcasting to cast *Command* (level 2 version). The dragon can't take this action again until the start of its next turn."
  - name: "Fiery Rays"
    desc: "The dragon uses Spellcasting to cast *Scorching Ray*. The dragon can't take this action again until the start of its next turn."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
```
