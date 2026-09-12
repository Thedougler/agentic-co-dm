---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "CR 1/2 monstrosity that destroys metal equipment and armor through its antennae and touch."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[shelfworks|Shelfworks]]"
- "[[calders-tooth|Calder's Tooth]]"
statblock: inline
name: "Rust Monster"
uid: 0cc4baf9-e3d4-4ce0-9a4a-a7b0a90a75fb
---

# Rust Monster

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Rust Monster"
size: Medium
type: monstrosity
alignment: "Unaligned"
ac: 14
hp: 33
hit_dice: "6d8 + 6"
speed: "40 ft."
stats: [13, 12, 13, 2, 13, 6]
senses: "darkvision 60 ft.; Passive Perception 11"
cr: "1/2"
traits:
  - name: "Iron Scent"
    desc: "The rust monster can pinpoint the location of ferrous metal within 30 feet of itself."
actions:
  - name: "Multiattack"
    desc: "The rust monster makes one Bite attack and uses Antennae twice."
  - name: "Bite"
    desc: "*Melee Attack Roll:* +3, reach 5 ft. 5 (1d8 + 1) Piercing damage."
  - name: "Antennae"
    desc: "The rust monster targets one nonmagical metal object—armor or a weapon—worn or carried by a creature within 5 feet of itself. *Dexterity Saving Throw*: DC 11, the creature with the object. *Failure:* The object takes a -1 penalty to the AC it offers (armor) or to its attack rolls (weapon). Armor is destroyed if the penalty reduces its AC to 10, and a weapon is destroyed if its penalty reaches -5. The penalty can be removed by casting the *Mending* spell on the armor or weapon."
  - name: "Destroy Metal"
    desc: "The rust monster touches a nonmagical metal object within 5 feet of itself that isn't being worn or carried. The touch destroys a 1-foot Cube [Area of Effect]|XPHB|Cube of the object."
```
