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

Golden-brown spotted cat with long saber teeth and a broad head. Fresh leaves, dry grass, vines, and plant fibers form a camouflage mantle over the back and shoulders—the mantle breaks up the silhouette and conceals the form while exposing the spotted face, legs, and banded tail.

![[attachments/shattered-sea/creatures/spiguar-of-aruhe.jpg|Spiguar of Aruhe]]
![[attachments/spiguar-reference.png|Spiguar visual reference sheet]]
![[attachments/shattered-sea/creatures/spiguar-of-aruhe-token-stand.jpg|Spiguar of Aruhe token stand]]

## Behavior

**Habitat.** Spiguars hunt long channels of [[grasslands]] where eight-foot grass and shaded banks force travelers to choose between concealment and clear sight. They favor low rises and game trails, as well as river bends and the line where grass gives way to the darker jungle rim.

**Hunting method.** A spiguar lies motionless in its living mantle until wind, insects, and birds treat it as another grass clump. Then it explodes through the lane in one crushing rush. It does not pursue prey far into deep water, bare stone, or broken ground.

**Diet.** Spiguars take whatever stops too long in open lanes: [[Deer-Stalker|Deer-Stalkers]], [[Wolfrabbit|Wolfrabbits]], straying grung, riverbank foragers, and wounded prey flushed by larger predators. A kill is defended fiercely and dragged into cover before feeding begins.

**Solitary and territorial.** A mature spiguar patrols a hunting range of channels, bends, and grass corridors. When two adults meet in the same stretch, they separate after a brief, violent clash.

## Tactics

**Signs of presence.** Sudden silence in noisy grass, heavy prints that appear and vanish, low drag furrows leading into cover, flattened feeding circles, and bones marked by paired fang punctures. Clumps of spotted fur and mats of reeds or creepers snag on thorn or branch.

**What triggers attack.** The spiguar keys on movement through lanes, prey that stops to drink, and anything noisy enough to betray a traveling line through grass. It prefers its first strike from concealment and commits hardest when it can knock something prone or seize one body before the rest of the group can act.

**Combat flow.** It keeps low and closes under cover before launching a pounce that bowls a target over. Once something is down, it bites deep and drags the prey back into grass where sightlines collapse. If several enemies press it, the spiguar uses grass to break line of sight and circles for another ambush rather than standing in the open.

**Vulnerabilities.** Deep water and wide bare ground strip its advantage. Fire and clean overhead sightlines do the same. The spiguar will not willingly rush through [[razer-grass|razer-grass]]. Open stone and river crossings cost it much of its edge.

**After a kill.** A kill site shows a brief struggle in the open lane, then a worse one in the grass beyond. A pounced lane bears blood on seed heads and drag trails that vanish under bent reeds. The hidden feeding hollow will give off its smell before anyone sees it.
