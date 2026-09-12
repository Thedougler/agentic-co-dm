---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [undead, horror]
summary: "A Small Neutral Evil wraith (CR 5) that drains life and can raise slain Humanoids as specters under its control."
found_at:
- "[[doldrums|Doldrums]]"
- "[[the-drowned-maw|The Drowned Maw]]"
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Wraith"
uid: b1b784e9-4f80-4b16-99e0-6a35e16fa4cc
---

# Wraith

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Wraith"
size: Small
type: undead
alignment: "Neutral Evil"
ac: 13
hp: 67
hit_dice: "9d8 + 27"
speed: "5 ft., Fly 60 ft. (hover)"
stats: [6, 16, 16, 12, 14, 15]
damage_resistances: "Acid, Bludgeoning, Cold, Fire, Piercing, Slashing"
damage_immunities: "Necrotic, Poison"
condition_immunities: "Charmed, Exhaustion, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious"
senses: "darkvision 60 ft.; Passive Perception 12"
languages: "Common plus two other languages"
cr: 5
traits:
  - name: "Incorporeal Movement"
    desc: "The wraith can move through other creatures and objects as if they were Difficult Terrain. It takes 5 (1d10) Force damage if it ends its turn inside an object."
  - name: "Sunlight Sensitivity"
    desc: "While in sunlight, the wraith has Disadvantage on ability checks and attack rolls."
actions:
  - name: "Life Drain"
    desc: "*Melee Attack Roll:* +6, reach 5 ft. 21 (4d8 + 3) Necrotic damage. If the target is a creature, its Hit Point maximum decreases by an amount equal to the damage taken."
  - name: "Create Specter"
    desc: "The wraith targets a Humanoid corpse within 10 feet of itself that has been dead for no longer than 1 minute. The target's spirit rises as a Specter in the space of its corpse or in the nearest unoccupied space. The specter is under the wraith's control. The wraith can have no more than seven specters under its control at a time."
```
