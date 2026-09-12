---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror]
summary: "CR 2 transparent ooze that engulfs creatures in acidic body, immune to acid damage."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Gelatinous Cube"
found_at:
- "[[shelfworks|Shelfworks]]"
- "[[the-drowned-maw|The Drowned Maw]]"
uid: 419ca5bb-fdd9-4bbf-ab76-b3f8e871dc9c
---

# Gelatinous Cube

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Gelatinous Cube"
size: Large
type: ooze
alignment: "Unaligned"
ac: 6
hp: 63
hit_dice: "6d10 + 30"
speed: "15 ft."
stats: [14, 3, 20, 1, 6, 1]
damage_immunities: "Acid"
condition_immunities: "Blinded, Charmed, Deafened, Exhaustion, Frightened, Prone"
senses: "blindsight 60 ft.; Passive Perception 8"
cr: 2
traits:
  - name: "Ooze Cube"
    desc: "The cube fills its entire space and is transparent. Other creatures can enter that space, but a creature that does so is subjected to the cube's Engulf and has Disadvantage on the saving throw. Creatures inside the cube have Cover|XPHB|Total Cover, and the cube can hold one Large creature or up to four Medium or Small creatures inside itself at a time. As an action, a creature within 5 feet of the cube can pull a creature or an object out of the cube by succeeding on a DC 12 Strength (Athletics) check, and the puller takes 10 (3d6) Acid damage."
  - name: "Transparent"
    desc: "Even when the cube is in plain sight, a creature must succeed on a DC 15 Wisdom (Perception) check to notice the cube if the creature hasn't witnessed the cube move or otherwise act."
actions:
  - name: "Pseudopod"
    desc: "*Melee Attack Roll:* +4, reach 5 ft. 12 (3d6 + 2) Acid damage."
  - name: "Engulf"
    desc: "The cube moves up to its Speed without provoking Opportunity Attacks. The cube can move through the spaces of Large or smaller creatures if it has room inside itself to contain them (see the Ooze Cube [Area of Effect]|XPHB|Cube trait). *Dexterity Saving Throw*: DC 12, each creature whose space the cube enters for the first time during this move. *Failure:* 10 (3d6) Acid damage, and the target is engulfed. An engulfed target is suffocating, can't cast spells with a Verbal component, has the Restrained condition, and takes 10 (3d6) Acid damage at the start of each of the cube's turns. When the cube moves, the engulfed target moves with it. An engulfed target can try to escape by taking an action to make a DC 12 Strength (Athletics) check. On a successful check, the target escapes and enters the nearest unoccupied space. *Success:* Half damage, and the target moves to an unoccupied space within 5 feet of the cube. If there is no unoccupied space, the target fails the save instead."
```
