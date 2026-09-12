---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "CR 3 monstrosity that Ethereal Jaunts between planes and delivers a paralyzing poison Bite."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[outer-reach|Outer Reach]]"
- "[[midchain-east|Midchain East]]"
statblock: inline
name: "Phase Spider"
uid: 3d8397f5-cb22-40c3-89d4-2c91bcd47223
---

# Phase Spider

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Phase Spider"
size: Large
type: monstrosity
alignment: "Unaligned"
ac: 14
hp: 45
hit_dice: "7d10 + 7"
speed: "30 ft., Climb 30 ft."
stats: [15, 16, 12, 6, 10, 6]
senses: "darkvision 60 ft.; Passive Perception 10"
cr: 3
traits:
  - name: "Ethereal Sight"
    desc: "The spider can see 60 feet into the Ethereal Plane while on the Material Plane and vice versa."
  - name: "Spider Climb"
    desc: "The spider can climb difficult surfaces, including along ceilings, without needing to make an ability check."
  - name: "Web Walker"
    desc: "The spider ignores movement restrictions caused by webs, and the spider knows the location of any other creature in contact with the same web."
actions:
  - name: "Multiattack"
    desc: "The spider makes two Bite attacks."
  - name: "Bite"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 8 (1d10 + 3) Piercing damage plus 9 (2d8) Poison damage. If this damage reduces the target to 0 Hit Points, the target becomes Stable, and it has the Poisoned condition for 1 hour. While Poisoned, the target also has the Paralyzed condition."
bonus_actions:
  - name: "Ethereal Jaunt"
    desc: "The spider teleports from the Material Plane to the Ethereal Plane or vice versa."
```
