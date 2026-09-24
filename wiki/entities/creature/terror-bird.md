---
title: Aruhe - Terror-Bird
aliases:
  - Aruhe - Terror-Bird
  - Terror-Birds
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "house (wiki creature.terror-bird; living-stock 2026-09-05)"
  - "campaign-os:terror-birds.md"
summary: CR 13 Blight-corrupted axebeak apex predator on Aruhe whose ground-shaking charge ends in a beak clamp and swallow.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
tier: supporting
created: 2026-09-12T05:40:07Z
updated: 2026-09-18T06:59:22Z
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: bruiser
cr: 13
relationships:
  - target: "[[grasslands]]"
    type: related_to
  - target: "[[the-river]]"
    type: related_to
  - target: "[[crown-squid]]"
    type: related_to
---
# Aruhe - Terror-Bird

> [!narration] Narration
> Taller than a horse, a black Terror-Bird tears through the jungle with ragged wings spread for balance. Moss clings to its feathers. A yellow eye, serrated beak, hooked talons, and teeth inside that beak identify the predator. Each talon is as long as a forearm. Dust jumps beneath each stride as it bears down the path. The ground shakes before it reaches you.

## Statblock

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
  - Con: +10
  - Wis: +7
skillsaves:
  - Perception: +7
  - Stealth: +6
senses: "passive Perception 17"
languages: "—"
cr: 13
traits:
  - name: "Tremor Stride"
    desc: "Any creature within 30 feet of the terror-bird that is touching the ground can feel it approaching. The terror-bird cannot surprise creatures that have tremorsense or that are touching the ground."
  - name: "Blight-Grown"
    desc: "Moss and vegetation grow directly from the terror-bird's feathers. The terror-bird has advantage on Dexterity (Stealth) checks made in forested or jungle terrain."
actions:
  - name: "Multiattack"
    desc: "The terror-bird makes two attacks: one with its Serrated Beak and one with its Talon Rake."
  - name: "Serrated Beak"
    desc: "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 22 (3d10 + 7) piercing damage, and the target is grappled (escape DC 18). Until this grapple ends, the target is restrained, and the terror-bird can't use its Serrated Beak on another target."
  - name: "Talon Rake"
    desc: "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 17 (3d6 + 7) slashing damage."
  - name: "Swallow"
    desc: "The terror-bird makes one Serrated Beak attack against a Medium or smaller creature it is grappling. If the attack hits, the target is swallowed, and the grapple ends. The swallowed creature is Blinded and Restrained, has total cover against attacks and other effects outside the terror-bird, and takes 14 (4d6) acid damage at the start of each of the terror-bird's turns. If the terror-bird takes 25 damage or more on a single turn from a creature inside it, it must succeed on a DC 18 Constitution saving throw at the end of that turn or regurgitate the creature, which falls Prone within 10 feet. If the terror-bird dies, a swallowed creature is no longer Restrained and can escape from the corpse."
```

## Behavior


- **Habitat.** Terror-Birds occupy shaded rims, grass cuts, and hard-running lanes around [[grasslands|the Grasslands]] and [[the-river|the River]]. Each adult claims about a quarter-mile of edge territory where open ground gives it room for one committed charge. It ranges from the Rot toward the Hunger in the deep interior and appears on the approach to the central grove.
- **Behavior.** A still Terror-Bird reads as a mossed trunk with one yellow eye until it chooses to move. It does not fly. Its ragged wings provide balance and threat display around the charge.
- **Diet.** It runs down exposed prey and swallows smaller bodies whole. Feeding leaves flattened digest-circles, bone, and sour bolus. Its hunger remains animal rather than commanded by the Blight gardens. ^[inferred]
- **Social Structure.** It is solitary. Each bird claims a quarter-mile territory and avoids other large Aruhe predators by instinct. [[bear-elk|Bear-Elk]] routes get room, while [[crown-squid|crown squid]] and [[bloodhawk|bloodhawks]] take a Terror-Bird only when terrain gives them a cleaner angle.
- **Blight Growth.** Moss and vegetation have grown through its feathers for decades. The island is reclaiming the bird as it reclaimed the terraces, and the bird does not notice or resist it. ^[inferred]

## Tactics


- **Signs.** A yellow eye inside mossed black feathers, trunk-like stillness at a shaded rim, dust hopping on the path, tremors underfoot, talon prints deeper than a person's hand, and a sour feeding circle pressed flat in the grass.
- **Instincts.** It waits as cover. When prey breaks into the open, the ground-shake gives away its charge. It commits to one straight rush. Eight-foot grass, deep water, or a white [[razer-grass|razer-grass]] stand ends the hunt.
- **Tactics.** It opens with a visible charge and closes fast. It clamps with Serrated Beak and rakes anything nearby. When it isolates one body, it uses Swallow on a Medium or smaller grappled target.
- **Weaknesses.** Its strength is commitment, not turning. It is bad at sharp changes of direction, dense grass, deep water, razer-grass barriers, and prey that refuses the open lane it wants.
- **Aftermath.** An encounter leaves torn moss, claw furrows, churned dust, crushed grass, sour bolus, bone scraps, and a lane through the jungle where smaller creatures no longer approach.
