---
type: monster
status: draft
publish: false
aliases: []
found_at:
- "[[the-drowned-maw|The Drowned Maw]]"
- "[[shelfworks|Shelfworks]]"
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "CR 15 monstrosity that grapples with its Bite, injects lethal poison, and can Swallow up to three foes."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Purple Worm"
uid: 912578b3-7a6a-44b7-8130-b14560bb1ab3
---

# Purple Worm

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Purple Worm"
size: Gargantuan
type: monstrosity
alignment: "Unaligned"
ac: 18
hp: 247
hit_dice: "15d20 + 90"
speed: "50 ft., Burrow 50 ft."
stats: [28, 7, 22, 1, 8, 4]
saves:
  - con: 11
  - wis: 4
senses: "blindsight 30 ft., tremorsense 60 ft.; Passive Perception 9"
cr: 15
traits:
  - name: "Tunneler"
    desc: "The worm can burrow through solid rock at half its Burrow Speed and leaves a 10-foot-diameter tunnel in its wake."
actions:
  - name: "Multiattack"
    desc: "The worm makes one Bite attack and one Tail Stinger attack."
  - name: "Bite"
    desc: "*Melee Attack Roll:* +14, reach 10 ft. 22 (3d8 + 9) Piercing damage. If the target is a Large or smaller creature, it has the Grappled condition (escape DC 19), and it has the Restrained condition until the grapple ends."
  - name: "Tail Stinger"
    desc: "*Melee Attack Roll:* +14, reach 10 ft. 16 (2d6 + 9) Piercing damage plus 35 (10d6) Poison damage."
bonus_actions:
  - name: "Swallow"
    desc: "*Strength Saving Throw*: DC 19, one Large or smaller creature Grappled by the worm (it can have up to three creatures swallowed at a time). *Failure:* The target is swallowed by the worm, and the Grappled condition ends. A swallowed creature has the Blinded and Restrained conditions, has Cover|XPHB|Total Cover against attacks and other effects outside the worm, and takes 17 (5d6) Acid damage at the start of each of the worm's turns. If the worm takes 30 damage or more on a single turn from a creature inside it, the worm must succeed on a DC 21 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, each of which falls in a space within 5 feet of the worm and has the Prone condition. If the worm dies, any swallowed creature no longer has the Restrained condition and can escape from the corpse using 20 feet of movement, exiting Prone."
```
