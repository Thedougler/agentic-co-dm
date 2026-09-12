---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "CR 6 lawful evil monstrosity with deadly petrifying gaze and poisoned claws."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Medusa"
found_at:
- "[[shelfworks|Shelfworks]]"
- "[[sunken-crown|Sunken Crown]]"
uid: b7061675-9509-43a5-9571-41842d2b1794
---

# Medusa

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Medusa"
size: Medium
type: monstrosity
alignment: "Lawful Evil"
ac: 15
hp: 127
hit_dice: "17d8 + 51"
speed: "30 ft."
stats: [10, 17, 16, 12, 13, 15]
saves:
  - wis: 4
senses: "darkvision 150 ft.; Passive Perception 14"
languages: "Common plus one other language"
cr: 6
actions:
  - name: "Multiattack"
    desc: "The medusa makes two Claw attacks and one Snake Hair attack, or it makes three Poison Ray attacks."
  - name: "Claw"
    desc: "*Melee Attack Roll:* +6, reach 5 ft. 10 (2d6 + 3) Slashing damage."
  - name: "Snake Hair"
    desc: "*Melee Attack Roll:* +6, reach 5 ft. 5 (1d4 + 3) Piercing damage plus 14 (4d6) Poison damage."
  - name: "Poison Ray"
    desc: "*Ranged Attack Roll:* +5, range 150 ft. 11 (2d8 + 2) Poison damage."
bonus_actions:
  - name: "Petrifying Gaze (Recharge 5-6)"
    desc: "*Constitution Saving Throw*: DC 13, each creature in a 30-foot Cone. If the medusa sees its reflection in the Cone, the medusa must make this save. *First Failure* The target has the Restrained condition and repeats the save at the end of its next turn if it is still Restrained, ending the effect on itself on a success. *Second Failure* The target has the Petrified condition instead of the Restrained condition."
```
