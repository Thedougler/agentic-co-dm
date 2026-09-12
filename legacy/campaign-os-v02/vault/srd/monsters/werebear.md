---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "CR 5 werebear with shape-shift to large bear, curse bite, and multiattack rend."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Werebear"
found_at:
- "[[midchain-west|Midchain West]]"
- "[[midchain-south|Midchain South]]"
uid: 36923f0e-d4bd-4cfa-a7ae-392ae68861c7
---

# Werebear

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Werebear"
size: Small
type: monstrosity
alignment: "Neutral Good"
ac: 15
hp: 135
hit_dice: "18d8 + 54"
speed: "30 ft., Alternate ? ft., Climb 30 ft. (bear form only)"
stats: [19, 10, 17, 11, 12, 12]
senses: "darkvision 60 ft.; Passive Perception 17"
languages: "Common (can't speak in bear form)"
cr: 5
actions:
  - name: "Multiattack"
    desc: "The werebear makes two attacks, using Handaxe or Rend in any combination. It can replace one attack with a Bite attack."
  - name: "Bite (Bear or Hybrid Form Only)"
    desc: "*Melee Attack Roll:* +7, reach 5 ft. 17 (2d12 + 4) Piercing damage. If the target is a Humanoid, it is subjected to the following effect. *Constitution Saving Throw*: DC 14. *Failure:* The target is cursed. If the cursed target drops to 0 Hit Points, it instead becomes a Werebear under the DM's control and has 10 Hit Points. *Success:* The target is immune to this werebear's curse for 24 hours."
  - name: "Handaxe (Humanoid or Hybrid Form Only)"
    desc: "*Melee or Ranged Attack Roll:* +7, reach 5 ft or range 20/60 ft. 14 (3d6 + 4) Slashing damage."
  - name: "Rend (Bear or Hybrid Form Only)"
    desc: "*Melee Attack Roll:* +7, reach 5 ft. 13 (2d8 + 4) Slashing damage."
bonus_actions:
  - name: "Shape-Shift"
    desc: "The werebear shape-shifts into a Large bear-humanoid hybrid form or a Large bear, or it returns to its true humanoid form. Its game statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed."
```
