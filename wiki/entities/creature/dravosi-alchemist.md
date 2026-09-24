---
title: "Dravosi Alchemist"
aliases:
  - Dravosi Alchemist
category: entities
tags: [shattered-sea, creature]
sources:
  - "campaign-os:dravosi-alchemist.md"
created: 2026-09-13
updated: 2026-09-13
type: creature
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: revealed
campaign: shattered-sea
visibility: dm
summary: "A Dravosi Crown support officer who turns shipboard supplies, medicinals, and weaponized compounds into tactical leverage."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
region: ""
role: ""
cr: ""
---
# Dravosi Alchemist

> [!narration] Narration
>

## Statblock

**Stats & Combat.**

```statblock
layout: Basic 5e Layout
name: Dravosi Alchemist
size: Medium
type: entity
subtype: "human"
alignment: "lawful neutral"
ac: 13
hp: 22
hit_dice: "4d8 + 4"
speed: "30 ft."
stats: [9, 14, 12, 16, 12, 10]
saves:
  - intelligence: 5
skillsaves:
  - arcana: 5
  - medicine: 3
  - nature: 3
senses: "passive Perception 11"
languages: "Common"
cr: 1
traits:
  - name: Sea Legs
    desc: "Difficult terrain caused by ship movement, waves, or wet deck does not cost this creature extra movement."
  - name: Alchemical Bandolier
    desc: "The alchemist carries a bandolier of labelled compounds. Her throwable attacks draw from this stock; each is limited as noted. If she is killed or incapacitated, the bandolier and its remaining contents can be looted."
actions:
  - name: Dagger
    desc: "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage."
  - name: "Poison Gas Canister (2/Day)"
    desc: "The alchemist hurls a sealed canister at a point within 30 ft. The canister shatters on impact and releases a toxic cloud in a 10-ft radius. Each creature in the area must succeed on a DC 13 Constitution saving throw or be poisoned until the start of the alchemist's next turn. The cloud persists until the start of the alchemist's next turn; any creature that ends its turn in the area must repeat the save."
  - name: "Incendiary Flask (2/Day)"
    desc: "The alchemist hurls a flask at a point within 30 ft. Each creature within 5 ft. of that point must succeed on a DC 13 Dexterity saving throw or take 7 (2d6) fire damage and catch fire. A burning creature takes 2 (1d4) fire damage at the start of each of its turns. A creature or an adjacent creature can use an action to extinguish the flames."
  - name: "Frag Canister (2/Day)"
    desc: "The alchemist hurls a canister at a point within 30 ft. The canister detonates on impact, spraying shrapnel in a 10-ft radius. Each creature in the area must succeed on a DC 13 Dexterity saving throw, taking 10 (3d6) piercing damage on a failed save or half as much on a successful one."
```

**Wants:** to protect Crown cargo and crew by identifying a threat early and neutralizing it with her bandolier before a fight closes to blades.
**Morale:** breaks the instant her bandolier runs dry or she drops below half HP — without compounds left to throw, she has nothing but a dagger and no reason left to stand.


## Biology

**Description.**

A [[dravosi-crown]] warrant officer responsible for shipboard stores, medicinals, and, when the situation calls for it, weaponised compounds. She works the same boarding parties as the Crown's [[dravosi-deckhand]]s and [[dravosi-enforcer]]s, reporting up through officers like [[barnaby-rook]]. She does not think of herself as a fighter. She thinks of herself as the officer who keeps the hold stocked and the wounded patched, and who reached for a canister only because something at the gangplank meant to take both.

## Behavior

**Ecology.**

Dravosi alchemists ride Crown patrol vessels along [[Calder's Tooth]] and the [[central-strait]], where they keep a ship's stores, dose the injured, and turn cargo-hold chemistry into canisters and flasks the moment a boarding turns hostile. Trained to treat every escalation as a supply problem first, she reaches for the bandolier before the dagger, and logs every compound she burns as inventory loss rather than a kill.

**Session Log.**

- Session 01: deployed a [[Grung]] toxin canister at the gangplank standoff during the boarding of the [[Saltwright]]; [[jean-claude-tabarnack|Jean-Claude]] and [[perrin-black-jaw|Perrin]] resisted, [[crissdalynn-khinriss|Crissdalynn]]'s [[Gust]] redirected the cloud back, and the crew of the Saltwright brought her down (`vault/episodes/001/transcript-dm-notes.md:30,32`).

## Tactics

**Toy Chest.**

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Kill or incapacitate her before her bandolier is spent | She still carries unused canisters or flasks | The bandolier and its remaining compounds can be looted and reused | [[dravosi-crown]] |
