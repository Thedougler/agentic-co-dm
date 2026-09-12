---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "CR 11 huge neutral evil monstrosity with lightning breath, constricting grasp, and acid swallow."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Behir"
found_at:
- "[[redwind-isles|Redwind Isles]]"
- "[[ashwall-islands|Ashwall Islands]]"
uid: 3583542b-41cd-4023-a3c1-777367312abc
---

# Behir

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Behir"
size: Huge
type: monstrosity
alignment: "Neutral Evil"
ac: 17
hp: 168
hit_dice: "16d12 + 64"
speed: "50 ft., Climb 50 ft."
stats: [23, 16, 18, 7, 14, 12]
damage_immunities: "Lightning"
senses: "darkvision 90 ft.; Passive Perception 16"
languages: "Draconic"
cr: 11
actions:
  - name: "Multiattack"
    desc: "The behir makes one Bite attack and uses Constrict."
  - name: "Bite"
    desc: "*Melee Attack Roll:* +10, reach 10 ft. 19 (2d12 + 6) Piercing damage plus 11 (2d10) Lightning damage."
  - name: "Constrict"
    desc: "*Strength Saving Throw*: DC 18, one Large or smaller creature the behir can see within 5 feet. *Failure:* 28 (5d8 + 6) Bludgeoning damage. The target has the Grappled condition (escape DC 16), and it has the Restrained condition until the grapple ends."
  - name: "Lightning Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 16, each creature in a 90-foot-long, 5-foot-wide Line. *Failure:* 66 (12d10) Lightning damage. *Success:* Half damage."
bonus_actions:
  - name: "Swallow"
    desc: "*Dexterity Saving Throw*: DC 18, one Large or smaller creature Grappled by the behir (the behir can have only one creature swallowed at a time). *Failure:* The behir swallows the target, which is no longer Grappled. While swallowed, a creature has the Blinded and Restrained conditions, has Cover|XPHB|Total Cover against attacks and other effects outside the behir, and takes 21 (6d6) Acid damage at the start of each of the behir's turns. If the behir takes 30 damage or more on a single turn from the swallowed creature, the behir must succeed on a DC 14 Constitution saving throw at the end of that turn or regurgitate the creature, which falls in a space within 10 feet of the behir and has the Prone condition. If the behir dies, a swallowed creature is no longer Restrained and can escape from the corpse by using 15 feet of movement, exiting Prone."
```
