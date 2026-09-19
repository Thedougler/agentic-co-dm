---
title: Aruhe - Spiguar
aliases:
  - Aruhe - Spiguar
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "house (rough draft and image concept 2026-09-08)"
  - "wiki/attachments/spiguar-reference.png (visual reference sheet, 2026-09-14)"
summary: CR 11 solitary grassland ambusher that uses cover for a pounce and drag but loses its edge in open terrain.
provenance:
  extracted: 0.87
  inferred: 0.13
  ambiguous: 0.0
base_confidence: 0.53
lifecycle: proposed
lifecycle_changed: 2026-09-12
tier: supporting
created: 2026-09-12T10:10:00Z
updated: 2026-09-14T00:00:00Z
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: ambusher
cr: 11
relationships:
  - target: "[[grasslands]]"
    type: related_to
  - target: "[[Deer-Stalker]]"
    type: related_to
  - target: "[[Wolfrabbit]]"
    type: related_to
---
# Aruhe - Spiguar

> [!narration] Narration
> A low, spotted cat shape slides through the gold grass, almost invisible beneath a mat of reeds, creepers, and wet green leaves. Amber eyes watch from above a dark muzzle, and ivory saber teeth show before the heavy body drops flatter than a hunting leopard should be able to move. The grass barely whispers until it breaks open at once and the weight of the thing arrives before the roar does.

## Statblock
![[attachments/shattered-sea/creatures/spiguar-of-aruhe-token.jpg|Spiguar of Aruhe Foundry VTT token]]
```statblock
layout: Basic 5e Layout
name: Spiguar
size: Large
type: monstrosity
alignment: unaligned
ac: "17 (natural armor)"
hp: 187
hit_dice: "17d10 + 85"
speed: "60 ft."
stats: [22, 18, 20, 4, 16, 10]
saves:
  - Dexterity: +8
  - Constitution: +9
  - Wisdom: +7
skillsaves:
  - Athletics: +10
  - Perception: +7
  - Stealth: +12
  - Survival: +7
senses: "darkvision 60 ft., passive Perception 17"
languages: "—"
cr: 11
traits:
  - name: "Grass Mantle"
    desc: "In tall grass, brush, or similar vegetation, the spiguar has advantage on Dexterity (Stealth) checks and can take the Hide action as a bonus action. While motionless in such terrain, creatures more than 10 feet away have disadvantage on Wisdom (Perception) checks made to spot it."
  - name: "Reed-Silent Step"
    desc: "The spiguar ignores Difficult Terrain caused by grass, brush, and nonmagical plants. When it moves through tall grass at half speed or slower, it does not leave an obvious crushed trail."
  - name: "Pounce"
    desc: "If the spiguar moves at least 20 feet straight toward a creature and then hits it with a Claw attack on the same turn, the target takes an extra 10 (3d6) slashing damage. If the target is a creature, it must succeed on a DC 18 Strength saving throw or have the Prone condition. If the target is knocked prone, the spiguar can make one Saber Bite attack against it as a bonus action."
actions:
  - name: "Multiattack"
    desc: "The spiguar makes three attacks: one with its Saber Bite and two with its Claws."
  - name: "Saber Bite"
    desc: "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 19 (2d10 + 8) piercing damage. If the target is Large or smaller, it has the Grappled condition (escape DC 18). Until this grapple ends, the spiguar can't use Saber Bite on another target."
  - name: "Claw"
    desc: "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 17 (2d8 + 8) slashing damage."
bonus_actions:
  - name: "Drag Through Grass"
    desc: "The spiguar moves up to half its speed, dragging one creature Grappled by it. This movement ignores Difficult Terrain caused by grass and brush and does not provoke opportunity attacks from the Grappled creature."
  - name: "Cloaking Crouch"
    desc: "The spiguar takes the Hide action."
```

## Visual reference

Heavy spotted cat with a broad head, long tail, large paws, and long ivory saber teeth. Golden-brown fur carries dark rosettes. Amber-gold eyes, a dark nose, and a dark muzzle mark the face. Fresh leaves, dry grass, vines, and plant fibers form a camouflage mantle over the back and shoulders. The mantle breaks up the outline and exposes the spotted face, legs, paws, and banded tail. The palette uses muted jungle green, dry grass brown, golden fur, and dark rosette markings.

## Behavior

- **Habitat.** Spiguars dominate the hottest open cuts of [[grasslands]], especially long channels where shaded banks and eight-foot grass force travelers to choose between cover and clear sight. They favor low rises and game trails. River bends and the line where grass gives way to the darker jungle rim also suit them.
- **Behavior.** A Spiguar takes prey from stillness. It lies beneath its living mantle until wind, insects, and birds treat it as another grass clump, then explodes through the lane in one crushing rush. It does not spend itself on long pursuit into deep water, bare stone, or broken ground.
- **Diet.** It takes whatever stops too long in open lanes: [[Deer-Stalker|Deer-Stalkers]], [[Wolfrabbit|Wolfrabbits]], straying grung, riverbank foragers, and wounded prey flushed by larger claims. It defends a kill fiercely and drags meat into cover before feeding.
- **Social Structure.** It is solitary. A mature Spiguar patrols a hunting range of channels, bends, and grass corridors. Adult Spiguars separate after a brief, violent clash when they meet in the same stretch.

## Tactics

- **Signs.** Sudden silence in noisy grass, heavy prints that appear and vanish, low drag furrows leading into cover, flattened feeding circles, and bones with paired fang punctures. Clumps of spotted fur and mats of reeds or creepers snag on thorn or branch.
- **Instincts.** It keys on movement through lanes, prey that stops to drink, and anything noisy enough to betray its line through the grass. It prefers the first strike from concealment and commits hardest when it can knock prey down or seize one body before the rest can react.
- **Tactics.** It keeps low and closes under cover before launching into a pounce that bowls a target over. Once something is down, it bites deep and drags the prey back into grass where sightlines collapse. If several enemies press it, it uses grass to break line of sight and circles for another ambush instead of standing in the open.
- **Weaknesses.** Deep water and wide bare ground blunt its advantage. Fire and clean overhead sightlines do the same. It will not willingly rush through [[razer-grass|razer-grass]], and open stone or the river costs it much of its edge.
- **Aftermath.** A kill site shows a brief struggle in the open and a worse one in the grass beyond. A pounced lane, blood on seed heads, and a drag trail vanish under bent reeds. A hidden feeding hollow gives off its smell before anyone sees it.

## Art
![[attachments/shattered-sea/creatures/spiguar-of-aruhe.jpg|Spiguar of Aruhe]]
![[attachments/spiguar-reference.png|Spiguar visual reference sheet]]
![[attachments/shattered-sea/creatures/spiguar-of-aruhe-token-stand.jpg|Spiguar of Aruhe token stand]]
