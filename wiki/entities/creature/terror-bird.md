---
title: Terror-Bird
aliases:
  - Aruhe - Terror-Bird
  - Terror-Birds
  - Terror-Bird
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "house (wiki creature.terror-bird; living-stock 2026-09-05)"
  - "campaign-os:terror-birds.md"
  - "Session 12 refile (2026-09-27)"
created: 2026-09-12
updated: 2026-09-27
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: bruiser
cr: 13
invention: true
summary: "A CR 13 flightless ambush bird on Aruhe that stands at a shaded rim like a mossy stump, charges in a straight line, and swallows one body whole."
---
# Terror-Bird

````col
```col-md
flexGrow=2
===
## At a Glance

A terror-bird does not want a fight. It wants one body, and it will charge across open ground to take it and carry it home to its rim.

- **Habitat.** Shaded rims above open grass cuts around [[grasslands]], [[the-river]], and [[the-long-meadow]]. Each adult holds about a quarter mile of edge.
- **Treasure.** None. Its rim holds bone scraps and sour, pressed-flat feeding circles.
```

```col-md
flexGrow=1
===
> [!narration] Terror-Bird
> A terror-bird is a flightless bird taller than a horse, black-feathered and draped in moss and ferns until it looks more like a stump than an animal. Its hooked beak is as long as a man's arm and lined inside with rows of teeth. Scaled grey legs end in talons as long as a forearm, and ragged wings hang half-open at its sides. It stands at the edge of the trees for hours, still as a trunk, with one yellow eye open.
```
````

## Statblock

![[attachments/shattered-sea/creatures/terror-bird-of-aruhe-v4.jpg|Terror-Bird overview]]
```statblock
layout: Basic 5e Layout
name: "Terror-Bird"
size: Huge
type: monstrosity
alignment: unaligned
ac: "16 (natural armor)"
hp: 200
hit_dice: "16d12 + 96"
speed: "60 ft."
stats: [24, 14, 22, 3, 16, 8]
saves:
  - constitution: 10
  - wisdom: 7
skillsaves:
  - perception: 7
  - stealth: 6
senses: "Passive Perception 17"
languages: "—"
cr: 13
traits:
  - name: "Tremor Stride"
    desc: "Any creature within 30 feet of the terror-bird that is touching the ground feels it coming. The terror-bird can't surprise a creature that is touching the ground or has Tremorsense."
  - name: "Moss-Grown"
    desc: "The terror-bird has Advantage on Dexterity (Stealth) checks made in forest or jungle, where it passes for a mossy stump."
  - name: "Straight Charge"
    desc: "When the terror-bird moves at least 20 feet toward a target on its turn, it moves in a straight line and can't turn more than 45 degrees. It will not move into grass taller than itself, into deep water, or through a stand of razer-grass, and its turn ends at the edge of any of them."
  - name: "Gag"
    desc: "If the terror-bird takes 25 damage or more on a single turn from a creature inside it, or 40 damage or more on a single turn from outside it, it makes a DC 18 Constitution saving throw at the end of that turn. Failure: it regurgitates each swallowed creature, which lands in an unoccupied space within 10 feet with the Prone condition."
actions:
  - name: "Multiattack"
    desc: "The terror-bird makes one Serrated Beak attack and one Talon Rake attack."
  - name: "Serrated Beak"
    desc: "Melee Attack Roll: +12, reach 10 ft. Hit: 22 (3d10 + 7) Piercing damage, and the target has the Grappled condition (escape DC 18). Until the grapple ends, the target has the Restrained condition and the terror-bird can't use Serrated Beak on another target. The grapple ends if the terror-bird takes 20 damage or more on a single turn."
  - name: "Talon Rake"
    desc: "Melee Attack Roll: +12, reach 10 ft. Hit: 17 (3d6 + 7) Slashing damage."
  - name: "Swallow"
    desc: "The terror-bird makes one Serrated Beak attack against a Medium or smaller creature it is grappling. Hit: the target is swallowed and the grapple ends. A swallowed creature has the Blinded and Restrained conditions, has Total Cover against attacks and effects from outside, and takes 14 (4d6) Acid damage at the start of each of the terror-bird's turns. If the terror-bird dies, a swallowed creature can escape the corpse using 5 feet of movement, exiting Prone."
```

## Tactics

- **Opening.** It waits at its rim until prey steps into the open, then charges the nearest body in the open, up to 60 feet, and uses Multiattack.
- **Signature.** The charge. Its tell is the ground shaking underfoot before the bird is seen, and a stump at the rim unfolding its legs. Answers: get into tall grass, deep water, or razer-grass; step aside or strike it from beside its line so it overruns its target; or hit it for 20 damage in one turn to open the beak.
- **Adapts.** If its target reaches cover it will not enter, it stops at the edge, rakes the nearest creature still in the open, and charges again on its next turn.
- **Weaknesses.** It cannot turn sharply, and it will not follow prey into grass taller than itself, deep water, or razer-grass.
- **Morale.** Once it has swallowed one creature, it turns and runs to its rim and stands still to digest. It backs off to its rim without prey once it has 140 hit points or fewer.

> [!narration] In action
> The ground jumps under your boots a heartbeat before the stump at the rim stands up on two scaled legs. It comes straight at you, head low, wings stiff, every stride thudding up through the soles of your feet.

## Behavior

- **Habits.** It stands at a shaded rim for hours, still as a trunk, with one yellow eye open on the open ground. It does not fly. Its ragged wings keep its balance in the charge and spread wide in threat.
- **Diet.** It runs down whatever crosses the open and swallows smaller bodies whole. It digests standing at its rim.
- **Group.** Solitary. Two adults' territories can meet at one stretch of open ground, and each hunts only its own half. It gives [[bear-elk]] room, and [[crown-squid]] and [[bloodhawk]]s take a terror-bird only when the ground favors them.
- **Body.** Moss and ferns grow straight out of its feathers, and it has carried them for decades without noticing.
- **Signs.** Dust hopping on the path, tremors underfoot, talon prints deeper than a hand, and flattened sour feeding circles with bone in them.
- **Aftermath.** Torn moss, claw furrows, churned dust, crushed grass, sour bolus, and a lane through the grass that smaller animals stop using.
