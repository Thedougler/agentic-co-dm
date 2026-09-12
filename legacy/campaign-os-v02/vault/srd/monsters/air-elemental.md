---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane, nature]
summary: "CR 5 Neutral elemental with air form, thunder immunity, and a whirlwind crowd control ability."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[redwind-isles|Redwind Isles]]"
- "[[central-strait|Central Strait]]"
statblock: inline
name: "Air Elemental"
uid: d3c44e3e-8675-4943-a764-09273bae1787
---

# Air Elemental

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Air Elemental"
size: Large
type: elemental
alignment: "Neutral"
ac: 15
hp: 90
hit_dice: "12d10 + 24"
speed: "10 ft., Fly 90 ft. (hover)"
stats: [14, 20, 14, 6, 10, 6]
damage_resistances: "Bludgeoning, Lightning, Piercing, Slashing"
damage_immunities: "Poison, Thunder"
condition_immunities: "Exhaustion, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious"
senses: "darkvision 60 ft.; Passive Perception 10"
languages: "Primordial (Auran)"
cr: 5
traits:
  - name: "Air Form"
    desc: "The elemental can enter a creature's space and stop there. It can move through a space as narrow as 1 inch without expending extra movement to do so."
actions:
  - name: "Multiattack"
    desc: "The elemental makes two Thunderous Slam attacks."
  - name: "Thunderous Slam"
    desc: "*Melee Attack Roll:* +8, reach 10 ft. 14 (2d8 + 5) Thunder damage."
  - name: "Whirlwind (Recharge 4-6)"
    desc: "*Strength Saving Throw*: DC 13, one Medium or smaller creature in the elemental's space. *Failure:* 24 (4d10 + 2) Thunder damage, and the target is pushed up to 20 feet straight away from the elemental and has the Prone condition. *Success:* Half damage only."
```
