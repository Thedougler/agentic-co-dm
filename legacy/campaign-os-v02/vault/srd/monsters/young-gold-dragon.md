---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 10 dragon with fire immunity, Amphibious, Rend multiattack, and Weakening Breath."
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[sunken-crown|Sunken Crown]]"
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Young Gold Dragon"
uid: f903df30-9017-4f5d-8bdb-2a701d40a289
---

# Young Gold Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Young Gold Dragon"
size: Large
type: dragon
alignment: "Lawful Good"
ac: 18
hp: 178
hit_dice: "17d10 + 85"
speed: "40 ft., Fly 80 ft., Swim 40 ft."
stats: [23, 14, 21, 16, 13, 20]
saves:
  - dex: 6
  - wis: 5
damage_immunities: "Fire"
senses: "blindsight 30 ft., darkvision 120 ft.; Passive Perception 19"
languages: "Common, Draconic"
cr: 10
traits:
  - name: "Amphibious"
    desc: "The dragon can breathe air and water."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of Weakening Breath."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +10, reach 10 ft. 17 (2d10 + 6) Slashing damage."
  - name: "Fire Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 17, each creature in a 30-foot Cone. *Failure:* 55 (10d10) Fire damage. *Success:* Half damage."
  - name: "Weakening Breath"
    desc: "*Strength Saving Throw*: DC 17, each creature that isn't currently affected by this breath in a 30-foot Cone. *Failure:* The target has Disadvantage on Strength-based D20 Test and subtracts 3 (1d6) from its damage rolls. It repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically."
```
