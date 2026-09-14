---
title: "Dravosi Enforcer"
category: entities
tags: [shattered-sea, creature]
sources:
  - "campaign-os:dravosi-enforcer.md"
created: 2026-09-13
updated: 2026-09-13
type: creature
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "A Dravosi Crown veteran built for confined boarding fights, crowd suppression, hooks, gangplanks, and violence carried out like just another inspection."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Dravosi Enforcer

[[Dravosi Crown]] veterans assigned to boarding actions and crowd suppression. Built for confined-space fighting, they know how to use a hook to pull someone off their feet, and they know how to use a gangplank as a kill zone.

Related: [[Dravosi Deckhand]], [[Dravosi Crown]].

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: Dravosi Enforcer
size: Medium
type: entity
subtype: "human"
alignment: "lawful neutral"
ac: 12
hp: 32
hit_dice: "5d8 + 10"
speed: "30 ft."
stats: [15, 11, 14, 10, 10, 11]
skillsaves:
  - athletics: 4
  - intimidation: 2
senses: "passive Perception 10"
languages: "Common"
cr: "1/2"
traits:
  - name: Sea Legs
    desc: "Difficult terrain caused by ship movement, waves, or wet deck does not cost this creature extra movement."
  - name: Pack Tactics
    desc: "The enforcer has advantage on attack rolls against a creature if at least one of the enforcer's allies is within 5 ft. of the creature and the ally isn't incapacitated."
actions:
  - name: Multiattack
    desc: "The enforcer makes two Cutlass attacks, or one Cutlass attack and one Boarding Hook attack."
  - name: Cutlass
    desc: "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) slashing damage."
  - name: Boarding Hook
    desc: "Melee Weapon Attack: +4 to hit, reach 10 ft., one target. Hit: 5 (1d6 + 2) piercing damage. On a hit, the target must succeed on a DC 12 Strength saving throw or be pulled up to 5 feet toward the enforcer and knocked prone."
```

## Description

Recognizable by the boarding kit: cutlass, hooked boarding pole, and a Crown-grey coat heavier than a [[Dravosi Deckhand]]'s inspection uniform. Where a deckhand works a routine check and shouts for backup, an enforcer is the backup — sent down first into a hold or across a gangplank in pairs, trained to press an advantage rather than hold a line. [[Dravosi Crown]] boarding parties field enforcers behind the first wave of deckhands, using them to finish what an inspection turns into a fight.

## Ecology

Enforcers crew [[Dravosi Crown]] patrol vessels working the [[Central Strait]]'s shipping lanes and the inspection posts around [[Calder's Tooth]], the Crown's naval reach over free-sailor traffic passing between the [[Crown Islands]] and [[Midchain]]. The rank is a step up from [[Dravosi Deckhand]] — a sailor who survived a first boarding and got issued a hook instead of a crossbow — and enforcers are assigned in pairs, which is why Pack Tactics describes how they actually fight: never alone into a hold, always working a target together. Off duty they carry the same flat, by-the-book manner as any Crown inspector, reciting registry standards and rating forms; that manner drops the instant a target resists.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Kill the light in an enclosed boarding space | The fight happens in a dark hold or unlit passage | The enforcer has no darkvision and fights blind past the reach of a lantern; he's tracked and hit by sound and smell alone until he reaches a light source | [[Dravosi Crown]] |
| Down or isolate his partner | Another enforcer or ally is no longer within 5 ft., incapacitated or dead | Pack Tactics drops out — he's fighting alone at a flat +4 with no advantage, and starts weighing whether a manifest check is worth dying over | [[Dravosi Deckhand]] |
| Wound and question a captured enforcer about patrol routes or a specific ship | He's bloodied, disarmed, and alone, with no officer left to speak for him | He recites what's on his own rating sheet — registry numbers, waypoint schedules — and nothing beyond his own patrol, the same flat recitation Crown inspection drills into every enforcer | [[Dravosi Crown]] |
