---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 5 dragon hybrid with elemental breath weapon and clawed melee attacks."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Half-Dragon"
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[crown-islands|Crown Islands]]"
uid: d132357b-44cb-4d9b-8679-9b230188f7c6
---

# Half-Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Half-Dragon"
size: Medium
type: dragon
alignment: "Neutral"
ac: 18
hp: 105
hit_dice: "14d8 + 42"
speed: "40 ft."
stats: [19, 14, 16, 10, 15, 14]
saves:
  - dex: 5
  - wis: 5
damage_resistances: "Damage type chosen for the Draconic Origin trait below"
senses: "blindsight 10 ft., darkvision 60 ft.; Passive Perception 15"
languages: "Common, Draconic"
cr: 5
traits:
  - name: "Draconic Origin"
    desc: "The half-dragon is related to a type of dragon associated with one of the following damage types (DM's choice): Acid, Cold, Fire, Lightning, or Poison. This choice affects other aspects of the stat block."
actions:
  - name: "Multiattack"
    desc: "The half-dragon makes two Claw attacks."
  - name: "Claw"
    desc: "*Melee Attack Roll:* +7, reach 10 ft. 6 (1d4 + 4) Slashing damage plus 7 (2d6) damage of the type chosen for the Draconic Origin trait."
  - name: "Dragon's Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 14, each creature in a 30-foot Cone. *Failure:* 28 (8d6) damage of the type chosen for the Draconic Origin trait. *Success:* Half damage."
bonus_actions:
  - name: "Leap"
    desc: "The half-dragon jumps up to 30 feet by spending 10 feet of movement."
```
