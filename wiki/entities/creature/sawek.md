---
title: "Sawek"
category: entities
tags: [shattered-sea, creature]
sources: ["central-strait-crossing.md"]
summary: "Rumored apex predator of the Central Strait's dark southern Midchain approaches."
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.37
lifecycle: proposed
lifecycle_changed: "2026-09-13"
tier: supporting
created: 2026-09-13T20:52:00Z
updated: 2026-09-13
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
relationships:
  - target: "[[central-strait]]"
    type: related_to
  - target: "[[central-strait-crossing]]"
    type: related_to
region: ""
role: ""
cr: ""
---

# Sawek

> [!narration] Narration
>

![[sawek-banner]]

## Statblock

**Stats & Combat.**

```statblock
layout: Basic 5e Layout
name: Sawek
size: Huge
type: monstrosity
alignment: unaligned
ac: 14
ac_class: natural armour
hp: 95
hit_dice: 9d12 + 36
speed: "5 ft., swim 40 ft."
stats: [20, 16, 18, 6, 14, 4]
saves:
  - strength: 8
  - constitution: 7
skillsaves:
  - perception: 5
  - stealth: 6
senses: "blindsight 60 ft. (underwater only), darkvision 120 ft., passive Perception 15"
languages: "—"
cr: 5
traits:
  - name: Keen Smell
    desc: "The Sawek has advantage on Wisdom (Perception) checks that rely on smell."
  - name: Patient Hunter
    desc: "While stationary in its lair, the Sawek makes no sound and requires no Stealth check. A creature looking directly into the lair entrance must succeed on a DC 18 Wisdom (Perception) check to detect movement in the dark below."
  - name: Water Breathing
    desc: "The Sawek can breathe only underwater."
actions:
  - name: Multiattack
    desc: "The Sawek makes one Bite attack and two Tentacle attacks."
  - name: Bite
    desc: "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 18 (3d8 + 5) piercing damage. The Sawek has advantage on this attack roll if the target is Grappled."
  - name: Tentacle
    desc: "Melee Weapon Attack: +8 to hit, reach 20 ft., one target. Hit: 12 (2d6 + 5) bludgeoning damage. The target is Grappled (escape DC 16) and Restrained until the grapple ends. The Sawek can maintain up to two grapples simultaneously."
  - name: "Crush (Recharge 5-6)"
    desc: "One Grappled creature takes 28 (4d12) bludgeoning damage and must succeed on a DC 16 Constitution saving throw or be Incapacitated until the end of its next turn."
bonus_actions:
  - name: Drag Under
    desc: "The Sawek moves one Grappled creature up to 30 feet directly toward the lair entrance. If this carries the creature into the blue hole, the creature enters the lair: total darkness, fully submerged."
```

**Perception — Spotting the Sawek's Lair**

DC 18 Wisdom; only a creature looking directly into the lair entrance may roll.
**Success:** movement stirs in the dark water below — something large is waiting.
**Failure:** the entrance looks empty and still; the sawek is free to ambush when prey comes into reach.

This entry's statblock is the general bestiary build. The [[Kalowe — The Sawek Bounty]] quest carries a separate, tuned combat write-up for its own territorial sawek — run that page's version for that encounter specifically, not this one.

## Biology

**Description.**

[[Kalowe]]'s reef divers call it the sawek; colonial sailors call it the blue devil, after its preference for the caves lining blue holes as its lair. The front half is shark: broad, muscle-dense, jaws wide enough to take a man at the shoulder, skin a deep blue-grey that reads as black in dim water. The rear half is octopus: eight tentacles, each up to twenty feet long at full extension. It fits inside a cave entrance that looks too small to hold anything of note.

## Behavior

**Ecology.**

The sawek is an ambush predator — the tentacles emerge from the entrance and grab whatever is within range, and the shark half takes over once prey is in reach. It can maintain a grapple on two targets at once and drags a grappled creature back toward its lair. While stationary in its lair, the sawek is silent and requires no Stealth check. It has advantage on Perception checks that rely on smell and breathes only underwater. [[Kalowe]] divers mark claimed holes with a length of cord tied to a reef stake, the only signal that a given blue hole is already taken.

## Tactics

**Toy Chest.**

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Chum the water near a marked blue hole | The cord marker hasn't been checked to confirm the hole is empty | The sawek surfaces to investigate, trading its ambush advantage for a fight in open water | [[Kalowe — The Sawek Bounty]] |
| Cut or move a diver's claimed-hole cord | Nobody's confirmed the lair behind it is unoccupied | The next diver or PC to check the hole walks into a live ambush instead of an empty cave | [[Kalowe]] |
| Loot the lair floor mid-fight | The sawek is still alive and hasn't fled | Splits the party's attention between salvage and the fight, risking a grapple on whoever's distracted | [[Kalowe — The Sawek Bounty]] |
