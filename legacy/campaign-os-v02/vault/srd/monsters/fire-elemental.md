---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane, nature]
summary: "CR 5 large fire elemental immune to fire and poison, surrounded by damaging aura and capable of moving through narrow spaces."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Fire Elemental"
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[outer-reach|Outer Reach]]"
uid: 2db3cd09-9c58-4f6b-89cf-a294a840f4d6
---

# Fire Elemental

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Fire Elemental"
size: Large
type: elemental
alignment: "Neutral"
ac: 13
hp: 93
hit_dice: "11d10 + 33"
speed: "50 ft."
stats: [10, 17, 16, 6, 10, 7]
damage_resistances: "Bludgeoning, Piercing, Slashing"
damage_immunities: "Fire, Poison"
condition_immunities: "Exhaustion, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious"
senses: "darkvision 60 ft.; Passive Perception 10"
languages: "Primordial (Ignan)"
cr: 5
traits:
  - name: "Fire Aura"
    desc: "At the end of each of the elemental's turns, each creature in a 10-foot Emanation originating from the elemental takes 5 (1d10) Fire damage. Creatures and flammable objects in the Emanation start Hitazard burning."
  - name: "Fire Form"
    desc: "The elemental can move through a space as narrow as 1 inch without expending extra movement to do so, and it can enter a creature's space and stop there. The first time it enters a creature's space on a turn, that creature takes 5 (1d10) Fire damage."
  - name: "Illumination"
    desc: "The elemental sheds Bright Light in a 30-foot radius and Dim Light for an additional 30 feet."
  - name: "Water Susceptibility"
    desc: "The elemental takes 3 (1d6) Cold damage for every 5 feet the elemental moves in water or for every gallon of water splashed on it."
actions:
  - name: "Multiattack"
    desc: "The elemental makes two Burn attacks."
  - name: "Burn"
    desc: "*Melee Attack Roll:* +6, reach 5 ft. 10 (2d6 + 3) Fire damage. If the target is a creature or a flammable object, it starts burning."
```
