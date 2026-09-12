---
type: monster
status: draft
publish: false
aliases: []
found_at:
- "[[the-drowned-maw|The Drowned Maw]]"
- "[[doldrums|Doldrums]]"
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "CR 11 Huge monstrosity with heat aura, powerful bite that grapples, and ability to swallow creatures whole."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Remorhaz"
uid: 766c59d8-9a2e-4a78-b0ca-709f340773d4
---

# Remorhaz

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Remorhaz"
size: Huge
type: monstrosity
alignment: "Unaligned"
ac: 17
hp: 195
hit_dice: "17d12 + 85"
speed: "40 ft., Burrow 30 ft."
stats: [24, 13, 21, 4, 10, 5]
damage_immunities: "Cold, Fire"
senses: "darkvision 60 ft., tremorsense 60 ft.; Passive Perception 10"
cr: 11
traits:
  - name: "Heat Aura"
    desc: "At the end of each of the remorhaz's turns, each creature in a 5-foot Emanation originating from the remorhaz takes 16 (3d10) Fire damage."
actions:
  - name: "Bite"
    desc: "*Melee Attack Roll:* +11, reach 10 ft. 18 (2d10 + 7) Piercing damage plus 14 (4d6) Fire damage. If the target is a Large or smaller creature, it has the Grappled condition (escape DC 17), and it has the Restrained condition until the grapple ends."
bonus_actions:
  - name: "Swallow"
    desc: "*Strength Saving Throw*: DC 19, one Large or smaller creature Grappled by the remorhaz (it can have up to two creatures swallowed at a time). *Failure:* The target is swallowed by the remorhaz, and the Grappled condition ends. A swallowed creature has the Blinded and Restrained conditions, it has Cover|XPHB|Total Cover against attacks and other effects outside the remorhaz, and it takes 10 (3d6) Acid damage plus 10 (3d6) Fire damage at the start of each of the remorhaz's turns. If the remorhaz takes 30 damage or more on a single turn from a creature inside it, the remorhaz must succeed on a DC 15 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, each of which falls in a space within 5 feet of the remorhaz and has the Prone condition. If the remorhaz dies, any swallowed creature no longer has the Restrained condition and can escape from the corpse by using 15 feet of movement, exiting Prone."
```
