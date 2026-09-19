---
title: "Grung"
category: entities
tags: [shattered-sea, creature]
sources:
  - "campaign-os:grung.md"
  - "campaign-os:grung-npc.md"
created: 2026-09-13
updated: 2026-09-13
type: creature
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "A CR 1/4 green-caste grung, the expendable laborer and scout caste of Grung raid operations."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Grung

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Grung"
size: Small
type: humanoid
subtype: grung
alignment: Typically Neutral Evil
ac: 12
ac_note: natural armor
hp: 11
hit_dice: 2d6 + 4
speed: "25 ft., Climb 25 ft."
stats: [7, 14, 15, 10, 11, 10]
saves:
  - dexterity: 4
skillsaves:
  - athletics: 2
  - perception: 2
  - stealth: 4
  - survival: 2
damage_immunities: "poison"
condition_immunities: "poisoned"
senses: "Passive Perception 12"
languages: "Grung"
cr: "1/4"
traits:
  - name: "Amphibious"
    desc: "The grung can breathe air and water."
  - name: "Poisonous Skin"
    desc: "Any creature that grapples the grung or otherwise comes into direct contact with the grung's skin must succeed on a DC 12 Constitution saving throw or become poisoned for 1 minute. A poisoned creature no longer in direct contact with the grung can repeat the saving throw at the end of each of its turns, ending the effect on a success."
  - name: "Standing Leap"
    desc: "The grung's long jump is up to 25 feet and its high jump is up to 15 feet, with or without a running start."
actions:
  - name: "Dagger"
    desc: "Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage plus 5 (2d4) poison damage."
```

**Wants:** Stay hidden and report an intrusion back to [[grung-elite-warrior|the handler]] rather than engage it directly.
**Morale:** Flees immediately if the handler is killed or the grung itself drops below half HP; never fights to the death.

## Description

CR 1/4 humanoid grung — green-caste laborers and scouts, the lowest freeborn caste of [[Grung]] society and the expendable workforce of Grung operations. Weapon hits deal 2d4 poison damage directly; the Poisonous Skin trait is separate.

> [!mechanic]
> **Poisonous Skin stacking.** Grappling or unarmed strikes against a grung's bare skin trigger a DC 12 Constitution save. Fail: poisoned for 1 minute, with disadvantage on attacks and ability checks. Success: no effect. Multiple grung in one fight mean multiple saves per round.

## Ecology

Green-caste grung are laborers, not fighters, drawn from the rainforest-interior clan holds of [[verdant-teeth]] and pressed into garrison duty across [[Midchain North]]. At the [[Calveno Sewer Magazines]] (itself `status: pending`), they serve as sentries alongside a blue-caste handler ([[grung-elite-warrior]]): standing orders are hide at the sound of movement (Stealth +4, advantage in dim light near water), let intruders pass, and report after. They break cover only if intruders interfere with the blackpowder barrels under guard, and even then try to flee and report rather than fight — a sentry discipline built on the caste's low standing within [[grung-clans|Grung Clans]] society, not any lack of nerve.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Provoke into the open | The party lingers near or handles the blackpowder barrels | The grung breaks cover, flees toward the handler, and raises the alarm | [[grung-elite-warrior]] |
| Corner or grapple one | It's caught alone with its escape route cut off | Poisonous Skin triggers on contact, per the Description's Poisonous Skin stacking mechanic | [[Calveno Sewer Magazines]] |
| Capture and interrogate | It's isolated and past its half-HP flee threshold | It talks — naming handler positions and patrol timing rather than dying for [[grung-clans|Grung Clans]] loyalty | [[simone-tabarnack]] |
