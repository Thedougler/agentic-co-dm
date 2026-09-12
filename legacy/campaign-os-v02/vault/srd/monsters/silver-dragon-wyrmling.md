---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "A CR 2 lawful good young dragon with cold breath and a devastating paralyzing breath weapon."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[outer-reach|Outer Reach]]"
statblock: inline
name: "Silver Dragon Wyrmling"
uid: c754e66b-3de4-4597-af6b-497a0a3c3055
---

# Silver Dragon Wyrmling

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Silver Dragon Wyrmling"
size: Medium
type: dragon
alignment: "Lawful Good"
ac: 17
hp: 45
hit_dice: "6d8 + 18"
speed: "30 ft., Fly 60 ft."
stats: [19, 10, 17, 12, 11, 15]
saves:
  - dex: 2
  - wis: 2
damage_immunities: "Cold"
senses: "blindsight 10 ft., darkvision 60 ft.; Passive Perception 14"
languages: "Draconic"
cr: 2
actions:
  - name: "Multiattack"
    desc: "The dragon makes two Rend attacks."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +6, reach 5 ft. 9 (1d10 + 4) Piercing damage."
  - name: "Cold Breath (Recharge 5-6)"
    desc: "*Constitution Saving Throw*: DC 13, each creature in a 15-foot Cone. *Failure:* 18 (4d8) Cold damage. *Success:* Half damage."
  - name: "Paralyzing Breath"
    desc: "*Constitution Saving Throw*: DC 13, each creature in a 15-foot Cone. *First Failure* The target has the Incapacitated condition until the end of its next turn, when it repeats the save. *Second Failure* The target has the Paralyzed condition, and it repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically."
```
