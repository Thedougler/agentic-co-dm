---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane, nature]
summary: "CR 5 large water elemental with water form, freeze vulnerability, and grappling whelm."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Water Elemental"
found_at:
- "[[doldrums|Doldrums]]"
- "[[central-strait|Central Strait]]"
uid: 8a11b33e-6338-42b7-8c52-a93b96ae74c2
---

# Water Elemental

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Water Elemental"
size: Large
type: elemental
alignment: "Neutral"
ac: 14
hp: 114
hit_dice: "12d10 + 48"
speed: "30 ft., Swim 90 ft."
stats: [18, 14, 18, 5, 10, 8]
damage_resistances: "Acid, Fire"
damage_immunities: "Poison"
condition_immunities: "Exhaustion, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious"
senses: "darkvision 60 ft.; Passive Perception 10"
languages: "Primordial (Aquan)"
cr: 5
traits:
  - name: "Freeze"
    desc: "If the elemental takes Cold damage, its Speed decreases by 20 feet until the end of its next turn."
  - name: "Water Form"
    desc: "The elemental can enter an enemy's space and stop there. It can move through a space as narrow as 1 inch without expending extra movement to do so."
actions:
  - name: "Multiattack"
    desc: "The elemental makes two Slam attacks."
  - name: "Slam"
    desc: "*Melee Attack Roll:* +7, reach 5 ft. 13 (2d8 + 4) Bludgeoning damage. If the target is a Medium or smaller creature, it has the Prone condition."
  - name: "Whelm (Recharge 4-6)"
    desc: "*Strength Saving Throw*: DC 15, each creature in the elemental's space. *Failure:* 22 (4d8 + 4) Bludgeoning damage. If the target is a Large or smaller creature, it has the Grappled condition (escape DC 14). Until the grapple ends, the target has the Restrained condition, is suffocating unless it can breathe water, and takes 9 (2d8) Bludgeoning damage at the start of each of the elemental's turns. The elemental can grapple one Large creature or up to two Medium or smaller creatures at a time with Whelm. As an action, a creature within 5 feet of the elemental can pull a creature out of it by succeeding on a DC 14 Strength (Athletics) check. *Success:* Half damage only."
```
