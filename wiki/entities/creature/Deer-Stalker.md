---
title: Deer-Stalker
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "campaign-os:deer-stalkers.md"
  - "house (wiki creature.deer-stalker, upgraded)"
summary: CR 8 solitary Aruhe ambusher that isolates prey, drags it from the group, and retreats when allies close in.
provenance:
  extracted: 0.98
  inferred: 0.02
  ambiguous: 0.0
base_confidence: 0.4
lifecycle: proposed
lifecycle_changed: 2026-09-12
tier: supporting
created: 2026-09-12T00:00:00Z
updated: 2026-09-13
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: ambusher
cr: 8
relationships:
  - target: "[[Aruhe - Quiet Forest]]"
    type: related_to
  - target: "[[Aruhe - The Marshes]]"
    type: related_to
  - target: "[[Aruhe - Razer-Grass]]"
    type: related_to
---
# Deer-Stalker

> [!narration] Narration
> The Deer-Stalker stands roughly eight feet tall on long, cloven-hoofed hind legs, its shaggy brown coat broken by pale patches across the shoulders and back. A long white deer face and broad branching antlers rise above its front-heavy body, while overlong forelimbs hang past its knees and end in black, fingered claws stained dark with blood. Pale eyes stay fixed over a wet black muzzle, where blood and spit thread from its teeth into the leaf rot.

## Statblock
![[attachments/shattered-sea/creatures/deer-stalker-of-aruhe-token.png|Deer-Stalker of Aruhe Foundry VTT token]]
```statblock
layout: Basic 5e Layout
name: "Deer-Stalker"
size: Large
type: monstrosity
alignment: unaligned
ac: "16 (natural armor)"
hp: 97
hit_dice: "13d10 + 26"
speed: "40 ft., climb 20 ft."
stats: [16, 20, 16, 6, 18, 6]
saves:
  - dexterity: 8
  - wisdom: 7
skillsaves:
  - Stealth: 10
  - Perception: 7
  - Survival: 7
senses: "darkvision 120 ft., passive Perception 17"
languages: "—"
cr: 8
traits:
  - name: Assassinate
    desc: "During its first turn, the deer-stalker has Advantage on attack rolls against creatures that haven't taken a turn. Once per turn, when it hits a creature that has no conscious ally within 10 feet of it, the attack deals an extra 10 (3d6) damage."
  - name: Evasion
    desc: "If the deer-stalker is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, it instead takes no damage on a successful save and half on a failed one. It can't use this trait if it has the Incapacitated condition."
actions:
  - name: Multiattack
    desc: "The deer-stalker makes three Claw attacks."
  - name: Claw
    desc: "Melee Attack Roll: +8, reach 10 feet, one target. Hit: 14 (2d8 + 5) Slashing damage. If the target is Medium or smaller and the deer-stalker isn't grappling another creature, the target has the Grappled condition (escape DC 16)."
  - name: Lunge and Drag
    desc: "The deer-stalker moves up to its Speed and makes one Claw attack against a creature it can reach. On a hit, if the target has the Grappled condition, the deer-stalker can move up to half its Speed while carrying it; this movement doesn't provoke Opportunity Attacks from that target."
bonus_actions:
  - name: Cunning Action
    desc: "The deer-stalker takes the Dash or Disengage action."
reactions:
  - name: Break Contact
    desc: "Trigger: The deer-stalker is hit by an attack while at least two hostile creatures are within 30 feet of it. Response: The deer-stalker moves up to half its Speed toward dim light, darkness, or natural foliage without provoking Opportunity Attacks."
```

## Visual reference

The supplied character reference sheet establishes the Deer-Stalker at roughly eight feet tall, with a shaggy brown-and-cream coat, broad branching antlers, a long pale muzzle, pale forward eyes, blood-stained forelimbs, black clawed hands, and cloven hind hooves. Its front-heavy upright silhouette keeps the overlong arms reaching below the knees.

![[attachments/shattered-sea/creatures/deer-stalker-of-aruhe-reference-sheet.png|Deer-Stalker character reference sheet]]

## Behavior

- **Habitat.** Deer-Stalkers keep to the dim edges of [[Aruhe - Quiet Forest|the Quiet]] and [[Aruhe - The Marshes|the Marshes]], using game trails, wet paths, root shadows, and grassland margins where a sick deer shape can stand half-hidden. They avoid [[Aruhe - Razer-Grass]].
- **Behavior.** A Deer-Stalker stands over a carcass like a sick deer. If disturbed, it crashes away too loudly, circles back through the dim, and repeats a voice it heard until one person follows.
- **Diet.** It eats fresh kills and interrupted carcasses, tearing soft meat first and leaving sweet rot around the site. Its hunger is animal and territorial, not a separate controlling force.
- **Social Structure.** It is solitary. Two Deer-Stalkers ignore one another, and neither contests a [[Aruhe - Bear-Elk|Bear-Elk]] or [[Aruhe - Terror-Bird|terror-bird]].

## Tactics

- **Signs.** Deer tracks become handlike claw marks, with blood on low leaves, dragged carcasses, torn bark at shoulder height, long pauses in ordinary forest sound, sweet rot, and a familiar voice repeated wetly from the wrong place.
- **Instincts.** It wants the one person who answers a sound or touches its meal alone. It does not use the voice to control anyone; it uses the sound to make separation feel safe.
- **Tactics.** It opens with Multiattack against the isolated target while Assassinate applies. It uses Lunge and Drag to cross the gap and carry that target away, or Cunning Action to reposition. When two or more enemies close, it uses Break Contact and resets the hunt.
- **Weaknesses.** Keep allies within 10 feet, force it into bright or open ground, and refuse to follow a voice without the group. It will not walk through [[Aruhe - Razer-Grass]].
- **Aftermath.** An encounter leaves an interrupted kill site, blood threads on leaves and roots, clawed drag marks, hoofprints that stop making sense, and a lingering stink of sweet rot. There is usually nothing worth keeping.

## Art
![[attachments/shattered-sea/creatures/deer-stalker-of-aruhe-01.jpg|Deer-Stalker of Aruhe]]
![[attachments/shattered-sea/creatures/deer-stalker-of-aruhe-02.jpg|Deer-Stalker of Aruhe]]
![[attachments/shattered-sea/creatures/deer-stalker-of-aruhe-03.jpg|Deer-Stalker of Aruhe]]
