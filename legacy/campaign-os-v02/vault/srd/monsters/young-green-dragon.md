---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 8 dragon with poison immunity, Amphibious, Rend multiattack, and poisoned immunity."
found_at:
- "[[midchain-south|Midchain South]]"
- "[[verdant-teeth|Verdant Teeth]]"
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Young Green Dragon"
uid: 07237fc0-6ca0-4f9f-93b2-19b390fa21ea
---

# Young Green Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Young Green Dragon"
size: Large
type: dragon
alignment: "Lawful Evil"
ac: 18
hp: 136
hit_dice: "16d10 + 48"
speed: "40 ft., Fly 80 ft., Swim 40 ft."
stats: [19, 12, 17, 16, 13, 15]
saves:
  - dex: 4
  - wis: 4
damage_immunities: "Poison"
condition_immunities: "Poisoned"
senses: "blindsight 30 ft., darkvision 120 ft.; Passive Perception 17"
languages: "Common, Draconic"
cr: 8
traits:
  - name: "Amphibious"
    desc: "The dragon can breathe air and water."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +7, reach 10 ft. 11 (2d6 + 4) Slashing damage plus 7 (2d6) Poison damage."
  - name: "Poison Breath (Recharge 5-6)"
    desc: "*Constitution Saving Throw*: DC 14, each creature in a 30-foot Cone. *Failure:* 42 (12d6) Poison damage. *Success:* Half damage."
```
