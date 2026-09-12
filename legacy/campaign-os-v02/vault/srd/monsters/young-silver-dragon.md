---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 9 dragon with cold immunity, Rend multiattack, Cold Breath, and Paralyzing Breath."
found_at:
- "[[outer-reach|Outer Reach]]"
- "[[the-drowned-maw|The Drowned Maw]]"
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Young Silver Dragon"
uid: 6bc478a6-2725-497d-9ae2-166e0b10edfc
---

# Young Silver Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Young Silver Dragon"
size: Large
type: dragon
alignment: "Lawful Good"
ac: 18
hp: 168
hit_dice: "16d10 + 80"
speed: "40 ft., Fly 80 ft."
stats: [23, 10, 21, 14, 11, 19]
saves:
  - dex: 4
  - wis: 4
damage_immunities: "Cold"
senses: "blindsight 30 ft., darkvision 120 ft.; Passive Perception 18"
languages: "Common, Draconic"
cr: 9
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of Paralyzing Breath."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +10, reach 10 ft. 15 (2d8 + 6) Slashing damage."
  - name: "Cold Breath (Recharge 5-6)"
    desc: "*Constitution Saving Throw*: DC 17, each creature in a 30-foot Cone. *Failure:* 49 (11d8) Cold damage. *Success:* Half damage."
  - name: "Paralyzing Breath"
    desc: "*Constitution Saving Throw*: DC 17, each creature in a 30-foot Cone. *First Failure* The target has the Incapacitated condition until the end of its next turn, when it repeats the save. *Second Failure* The target has the Paralyzed condition, and it repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically."
```
