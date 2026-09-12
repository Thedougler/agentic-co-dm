---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "CR 4 wereboar with shape-shift to boar, curse gore, and charging tusk knockdown."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Wereboar"
found_at:
- "[[midchain-west|Midchain West]]"
- "[[verdant-teeth|Verdant Teeth]]"
uid: 7eb6033c-ee18-4842-8d19-9b4d9e8968c7
---

# Wereboar

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Wereboar"
size: Small
type: monstrosity
alignment: "Neutral Evil"
ac: 15
hp: 97
hit_dice: "15d8 + 30"
speed: "30 ft., Alternate ? ft."
stats: [17, 10, 15, 10, 11, 8]
senses: "Passive Perception 12"
languages: "Common (can't speak in boar form)"
cr: 4
actions:
  - name: "Multiattack"
    desc: "The wereboar makes two attacks, using Javelin or Tusk in any combination. It can replace one attack with a Gore attack."
  - name: "Gore (Boar or Hybrid Form Only)"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 12 (2d8 + 3) Piercing damage. If the target is a Humanoid, it is subjected to the following effect. *Constitution Saving Throw*: DC 12. *Failure:* The target is cursed. If the cursed target drops to 0 Hit Points, it instead becomes a Wereboar under the DM's control and has 10 Hit Points. *Success:* The target is immune to this wereboar's curse for 24 hours."
  - name: "Javelin (Humanoid or Hybrid Form Only)"
    desc: "*Melee or Ranged Attack Roll:* +5, reach 5 ft. or range 30/120 ft. 13 (3d6 + 3) Piercing damage."
  - name: "Tusk (Boar or Hybrid Form Only)"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 10 (2d6 + 3) Piercing damage. If the target is a Medium or smaller creature and the wereboar moved 20+ feet straight toward it immediately before the hit, the target takes an extra 7 (2d6) Piercing damage and has the Prone condition."
bonus_actions:
  - name: "Shape-Shift"
    desc: "The wereboar shape-shifts into a Medium boar-humanoid hybrid or a Small boar, or it returns to its true humanoid form. Its game statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed."
```
