---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane]
summary: "Small elemental with frost breath, cold attacks, and death burst (CR 1/2)."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[redwind-isles|Redwind Isles]]"
statblock: inline
name: "Ice Mephit"
uid: de307631-3746-4e1b-8e96-272b5bfb80db
---

# Ice Mephit

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Ice Mephit"
size: Small
type: elemental
alignment: "Neutral Evil"
ac: 11
hp: 21
hit_dice: "6d6"
speed: "30 ft., Fly 30 ft."
stats: [7, 13, 10, 9, 11, 12]
damage_vulnerabilities: "Fire"
damage_immunities: "Cold, Poison"
condition_immunities: "Exhaustion, Poisoned"
senses: "darkvision 60 ft.; Passive Perception 12"
languages: "Primordial (Aquan, Auran)"
cr: "1/2"
traits:
  - name: "Death Burst"
    desc: "The mephit explodes when it dies. *Constitution Saving Throw*: DC 10, each creature in a 5-foot Emanation originating from the mephit. *Failure:* 5 (2d4) Cold damage. *Success:* Half damage."
actions:
  - name: "Claw"
    desc: "*Melee Attack Roll:* +3, reach 5 ft. 3 (1d4 + 1) Slashing damage plus 2 (1d4) Cold damage."
  - name: "Frost Breath (Recharge 6)"
    desc: "*Constitution Saving Throw*: DC 10, each creature in a 15-foot Cone. *Failure:* 7 (3d4) Cold damage. *Success:* Half damage."
  - name: "Fog Cloud (1/Day)"
    desc: "The mephit casts *Fog Cloud*, requiring no spell components and using Charisma as the spellcasting ability. - **At Will:** - **1/Day Each:** *Fog Cloud*"
```
