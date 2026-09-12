---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane]
summary: "CR 1/2 Small fire elemental with Death Burst and Fire Breath cone."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Magma Mephit"
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[redwind-isles|Redwind Isles]]"
uid: ce719b18-d07f-44dc-b8be-c1683e942276
---

# Magma Mephit

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Magma Mephit"
size: Small
type: elemental
alignment: "Neutral Evil"
ac: 11
hp: 18
hit_dice: "4d6 + 4"
speed: "30 ft., Fly 30 ft."
stats: [8, 12, 12, 7, 10, 10]
damage_vulnerabilities: "Cold"
damage_immunities: "Fire, Poison"
condition_immunities: "Exhaustion, Poisoned"
senses: "darkvision 60 ft.; Passive Perception 10"
languages: "Primordial (Ignan, Terran)"
cr: "1/2"
traits:
  - name: "Death Burst"
    desc: "The mephit explodes when it dies. *Dexterity Saving Throw*: DC 11, each creature in a 5-foot Emanation originating from the mephit. *Failure:* 7 (2d6) Fire damage. *Success:* Half damage."
actions:
  - name: "Claw"
    desc: "*Melee Attack Roll:* +3, reach 5 ft. 3 (1d4 + 1) Slashing damage plus 3 (1d6) Fire damage."
  - name: "Fire Breath (Recharge 6)"
    desc: "*Dexterity Saving Throw*: DC 11, each creature in a 15-foot Cone. *Failure:* 7 (2d6) Fire damage. *Success:* Half damage."
```
