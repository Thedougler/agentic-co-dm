---
title: "Water Weird"
aliases:
  - Weird
  - Water Weird
category: entities
tags: [shattered-sea, creature]
sources: []
created: 2026-09-19
updated: 2026-09-19
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "A Water Weird holding Bela Silt-Paw in a flooded Warren chamber."
region: ""
role: ""
cr: ""
---
# Water Weird

````col
```col-md
flexGrow=2
===
## At a Glance

The Water Weird is an elemental that holds [[bela-silt-paw|Bela Silt-Paw]] in a flooded chamber beneath the [[warren]].

- **Habitat.** It remains in the flooded chamber beneath the Warren.
```

```col-md
flexGrow=1
===
> [!narration] Water Weird
> A column of water twists free of the flooded chamber beneath the Warren. Its surface tightens into arms around [[bela-silt-paw|Bela Silt-Paw]], and the whole shape turns toward you without making a sound.
```
````

## Statblock

```statblock
layout: Basic 5e Layout
name: "Water Weird"
size: Medium
type: elemental
alignment: neutral
ac: 13
hp: 58
hit_dice: "9d8 + 18"
speed: "0 ft., swim 60 ft."
stats: [17, 16, 14, 11, 10, 10]
skillsaves:
  - stealth: 5
damage_resistances: "Fire"
damage_immunities: "Poison"
condition_immunities: "Exhaustion, Grappled, Paralyzed, Poisoned, Prone, Restrained, Unconscious"
senses: "Blindsight 30 ft., Passive Perception 10"
languages: "Aquan"
cr: "3"
traits:
  - name: "Invisible in Water"
    desc: "The Water Weird is Invisible while fully immersed in water."
  - name: "Water Form"
    desc: "The Water Weird can enter a Hostile creature's space and stop there. It can move through a space as narrow as 1 inch without squeezing."
actions:
  - name: "Constrict"
    desc: "Melee Attack Roll: +5, reach 10 ft. Hit: 10 (2d6 + 3) Bludgeoning damage. If the target is Medium or smaller, it has the Grappled condition (escape DC 13), and the Water Weird can't use Constrict on another target until the grapple ends. Until then, the target has the Restrained condition."
```
