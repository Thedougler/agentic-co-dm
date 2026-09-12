---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, faith]
summary: "CR 3 lawful evil fiend with poison-dealing Beard attack and infernal-wound Glaive."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Bearded Devil"
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[tail|Tail]]"
uid: 6b9dc019-e900-43d0-a301-bf456755a0ca
---

# Bearded Devil

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Bearded Devil"
size: Medium
type: fiend
alignment: "Lawful Evil"
ac: 13
hp: 58
hit_dice: "9d8 + 18"
speed: "30 ft."
stats: [16, 15, 15, 9, 11, 14]
saves:
  - str: 5
  - con: 4
  - cha: 4
damage_resistances: "Cold"
damage_immunities: "Fire, Poison"
condition_immunities: "Frightened, Poisoned"
senses: "darkvision 120 ft. (unimpeded by magical darkness); Passive Perception 10"
languages: "Infernal; telepathy 120 ft."
cr: 3
traits:
  - name: "Magic Resistance"
    desc: "The devil has Advantage on saving throws against spells and other magical effects."
actions:
  - name: "Multiattack"
    desc: "The devil makes one Beard attack and one Infernal Glaive attack."
  - name: "Beard"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 7 (1d8 + 3) Piercing damage, and the target has the Poisoned condition until the start of the devil's next turn. Until this poison ends, the target can't regain Hit Points."
  - name: "Infernal Glaive"
    desc: "*Melee Attack Roll:* +5, reach 10 ft. 8 (1d10 + 3) Slashing damage. If the target is a creature and doesn't already have an infernal wound, it is subjected to the following effect. *Constitution Saving Throw*: DC 12. *Failure:* The target receives an infernal wound. While wounded, the target loses 5 (1d10) Hit Points at the start of each of its turns. The wound closes after 1 minute, after a spell restores Hit Points to the target, or after the target or a creature within 5 feet of it takes an action to stanch the wound, doing so by succeeding on a DC 12 Wisdom (Medicine) check."
```
