---
title: "Purple-Caste Enforcer"
aliases:
  - Purple-Caste Enforcer
category: entities
tags: [shattered-sea, creature]
sources:
  - "campaign-os:purple-caste-enforcer.md"
created: 2026-09-13
updated: 2026-09-13
type: creature
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "A CR 1/2 grung enforcer, a Pack Tactics escort that grapples with a prehensile tongue before finishing with a venom-coated spear."
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
# Purple-Caste Enforcer

> [!narration] Narration
>

A CR 1/2 humanoid grung — low-tier purple-caste muscle serving as a Pack Tactics spear-and-tongue skirmisher, escort for named lieutenants in the back half of the [[Calveno sewer magazine dungeon]]. Encountered in Session 06's Primary Chamber fight: [[delmar-fisk|Delmar]] one-shot one with a pistol sneak attack ("before the groin that was standing there is replaced with a pink mist"). Staged as escort for [[vashu-the-weeping-veil|Vashu, the Weeping Veil]] at Room T1 (Magazine Gamma) of the [[Calveno Sewer Magazines]].

**Tactical Behavior:** Binding Tongue lashes out to grapple/restrain a target at range; Venom-Coated Spear follows up in melee with a poison rider. Pack Tactics grants advantage whenever an ally (Vashu) is adjacent to the same target. The grapple Binding Tongue sets up is the setup move for Vashu's Pressure Point finisher.

**Related:**

- [[purple-caste-zealot]]
- [[Grung|Grung (Green-Caste NPC)]]

## Statblock

**Stats & Combat.**

```statblock
layout: Basic 5e Layout
name: "Purple-Caste Enforcer"
size: Small
type: humanoid
subtype: grung
alignment: Lawful Neutral
ac: 14
ac_note: natural agility
hp: 22
hit_dice: 4d6 + 8
speed: "25 ft., Climb 25 ft."
stats: [12, 15, 14, 10, 12, 10]
damage_immunities: "poison"
condition_immunities: "poisoned"
senses: "Darkvision 30 ft., Passive Perception 11"
languages: "Grung"
cr: "1/2"
traits:
  - name: "Pack Tactics"
    desc: "The enforcer has advantage on an attack roll against a creature if at least one of the enforcer's allies is within 5 feet of the creature and the ally isn't incapacitated."
  - name: "Standing Leap"
    desc: "The enforcer's long jump is 25 feet and its high jump is 15 feet, with or without a running start."
actions:
  - name: "Venom-Coated Spear"
    desc: "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage, and the target must succeed on a DC 11 Constitution saving throw or take 2 (1d4) poison damage and be poisoned until the start of its next turn."
  - name: "Binding Tongue"
    desc: "The enforcer's prehensile tongue lashes out at one creature within 10 feet. The target must succeed on a DC 12 Dexterity saving throw or be grappled (escape DC 12). While grappled this way the target is also restrained. The enforcer cannot use Binding Tongue again while it maintains this grapple."
```

**Wants:** Land Binding Tongue on whatever target Vashu is pressing, so the grapple holds it still for her Pressure Point finisher.
**Morale:** Breaks and flees once Vashu falls or the enforcer itself drops below half HP — it won't die guarding a blind master who's already down.

## Biology

**Description.**

A purple-caste grung armed with a venom-coated spear and a prehensile, whip-like tongue used to grapple and restrain at range. Its hide runs deep violet, darker and glossier than the green-caste laborers it stands escort over. Where a green-caste sentry (see [[Grung]]) is built to flee and report, an enforcer is built to hold a line: heavier build, a poison-slicked spearhead, and the discipline to fight in support of a named lieutenant rather than alone.

## Behavior

**Ecology.**

Purple-caste enforcers are drawn from the warrior line of [[Grung]] caste society, the rank [[grung-clans|Grung Clans]] field as escort muscle for named lieutenants rather than rear-guard security. Like every grung they are amphibious and must submerge for at least an hour daily or take on Exhaustion, tying even a garrisoned enforcer back to the flooded channels of the [[Calveno Sewer Magazines]] and the reef-fringed rainforest of the [[verdant-teeth]] it was raised in. At Calveno an enforcer stands post at Room T1 (Magazine Gamma) beside [[vashu-the-weeping-veil|Vashu, the Weeping Veil]] — the mirror of the [[purple-caste-zealot]] [[ozzeth-the-twiceborn|Ozzeth]] keeps at Room T2 (Magazine Delta) — and the pairing is deliberate: Vashu fights blind by the Still-Water Discipline's own teaching, and the enforcer's Binding Tongue is what puts a target inside her reach before her Pressure Point ever needs to land.

## Tactics

**Toy Chest.**

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Stay outside 10 feet | No target has closed within Binding Tongue's range yet | The enforcer has to close on foot first, losing the turn it would've spent setting Vashu up | [[vashu-the-weeping-veil|Vashu, the Weeping Veil]] |
| Break the grapple immediately | Binding Tongue has landed and the enforcer is maintaining it | The enforcer can't use Binding Tongue again until it lets go, and Vashu loses the opening it was feeding her Pressure Point | [[Calveno Sewer Magazines]] |
| Isolate it from Vashu | Vashu is no longer within 5 feet of the same target | Pack Tactics drops out and the enforcer fights alone at a flat +4 with no advantage | [[grung-clans|Grung Clans]] |
