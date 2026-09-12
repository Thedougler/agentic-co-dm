---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane]
summary: "CR 1/2 Small fire elemental with flammable touch and Death Burst."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Magmin"
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[redwind-isles|Redwind Isles]]"
uid: 9735e299-cb1d-48d1-a5e3-32090b885faa
---

# Magmin

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Magmin"
size: Small
type: elemental
alignment: "Chaotic Neutral"
ac: 14
hp: 13
hit_dice: "3d6 + 3"
speed: "30 ft."
stats: [7, 15, 12, 8, 11, 10]
damage_immunities: "Fire"
senses: "darkvision 60 ft.; Passive Perception 10"
languages: "Primordial (Ignan)"
cr: "1/2"
traits:
  - name: "Death Burst"
    desc: "The magmin explodes when it dies. *Dexterity Saving Throw*: DC 11, each creature in a 10-foot Emanation originating from the magmin. *Failure:* 7 (2d6) Fire damage. *Success:* Half damage."
actions:
  - name: "Touch"
    desc: "*Melee Attack Roll:* +4, reach 5 ft. 7 (2d4 + 2) Fire damage. If the target is a creature or a flammable object that isn't being worn or carried, it starts burning."
bonus_actions:
  - name: "Ignited Illumination"
    desc: "The magmin sets itself ablaze or extinguishes its flames. While ablaze, the magmin sheds Bright Light in a 10-foot radius and Dim Light for an additional 10 feet."
```
