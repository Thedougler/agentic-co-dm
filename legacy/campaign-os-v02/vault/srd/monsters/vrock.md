---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, faith]
summary: "CR 6 large demon with demonic restoration, magic resistance, poison spores, and stunning screech."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Vrock"
found_at:
- "[[doldrums|Doldrums]]"
- "[[kalowe|Kalowe]]"
uid: 6f7c5c30-4394-4de2-8cd0-06bd33e72fd8
---

# Vrock

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Vrock"
size: Large
type: fiend
alignment: "Chaotic Evil"
ac: 15
hp: 152
hit_dice: "16d10 + 64"
speed: "40 ft., Fly 60 ft."
stats: [17, 15, 18, 8, 13, 8]
saves:
  - dex: 5
  - wis: 4
  - cha: 2
damage_resistances: "Cold, Fire, Lightning"
damage_immunities: "Poison"
condition_immunities: "Poisoned"
senses: "darkvision 120 ft.; Passive Perception 11"
languages: "Abyssal; telepathy 120 ft."
cr: 6
traits:
  - name: "Demonic Restoration"
    desc: "If the vrock dies outside the Abyss, its body dissolves into ichor, and it gains a new body instantly, reviving with all its Hit Points somewhere in the Abyss."
  - name: "Magic Resistance"
    desc: "The vrock has Advantage on saving throws against spells and other magical effects."
actions:
  - name: "Multiattack"
    desc: "The vrock makes two Shred attacks."
  - name: "Shred"
    desc: "*Melee Attack Roll:* +6, reach 5 ft. 10 (2d6 + 3) Piercing damage plus 10 (3d6) Poison damage."
  - name: "Spores (Recharge 6)"
    desc: "*Constitution Saving Throw*: DC 15, each creature in a 20-foot Emanation originating from the vrock. *Failure:* The target has the Poisoned condition and repeats the save at the end of each of its turns, ending the effect on itself on a success. While Poisoned, the target takes 5 (1d10) Poison damage at the start of each of its turns. Emptying a flask of Holy Water on the target ends the effect early."
  - name: "Stunning Screech (1/Day)"
    desc: "*Constitution Saving Throw*: DC 15, each creature in a 20-foot Emanation originating from the vrock (demons succeed automatically). *Failure:* 10 (3d6) Thunder damage, and the target has the Stunned condition until the end of the vrock's next turn."
```
