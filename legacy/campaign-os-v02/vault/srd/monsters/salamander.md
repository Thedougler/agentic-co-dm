---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane]
summary: "CR 5 fire elemental with aura, magical flame spear, and constriction attack."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[shattered-sea|The Shattered Sea]]"
statblock: inline
name: "Salamander"
uid: fd49e639-18dd-472f-b39d-b2f1d7009736
---

# Salamander

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Salamander"
size: Large
type: elemental
alignment: "Neutral Evil"
ac: 15
hp: 90
hit_dice: "12d10 + 24"
speed: "30 ft., Climb 30 ft."
stats: [18, 14, 15, 11, 10, 12]
damage_vulnerabilities: "Cold"
damage_immunities: "Fire"
senses: "darkvision 60 ft.; Passive Perception 10"
languages: "Primordial (Ignan)"
cr: 5
traits:
  - name: "Fire Aura"
    desc: "At the end of each of the salamander's turns, each creature of the salamander's choice in a 5-foot Emanation originating from the salamander takes 7 (2d6) Fire damage."
actions:
  - name: "Multiattack"
    desc: "The salamander makes two Flame Spear attacks. It can replace one attack with a use of Constrict."
  - name: "Flame Spear"
    desc: "*Melee or Ranged Attack Roll:* +7, reach 5 ft. or range 20/60 ft. 13 (2d8 + 4) Piercing damage plus 7 (2d6) Fire damage. HitomThe spear magically returns to the salamander's hand immediately after a ranged attack."
  - name: "Constrict"
    desc: "*Strength Saving Throw*: DC 15, one Large or smaller creature the salamander can see within 10 feet. *Failure:* 11 (2d6 + 4) Bludgeoning damage plus 7 (2d6) Fire damage. The target has the Grappled condition (escape DC 14), and it has the Restrained condition until the grapple ends."
```
