---
title: "Pirate Bosun"
aliases:
  - Pirate Bosun
category: entities
tags: [shattered-sea, creature]
sources:
  - "campaign-os:pirate-bosun.md"
created: 2026-09-13
updated: 2026-09-13
type: creature
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "CR 2 pirate grappler who pins targets for the cutpurses and clears deck space with a chain sweep."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Pirate Bosun

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Pirate Bosun"
size: Medium
type: humanoid
alignment: "any non-lawful"
ac: 15
hp: 45
hit_dice: "6d8 + 18"
speed: "30 ft."
stats: [16, 14, 16, 10, 12, 13]
saves:
  - str: 5
  - con: 5
skillsaves:
  - athletics: 5
  - intimidation: 3
senses: "passive Perception 11"
languages: "Common"
cr: 2
traits:
  - name: "Hold Them Still"
    desc: "The bosun has advantage on Strength (Athletics) checks against a creature if another pirate is within 5 ft. of that creature."
  - name: "Snatch"
    desc: "As an action, a creature within 5 ft. of another creature carrying a Tiny prize object can make a Dexterity (Sleight of Hand) check contested by the bearer's Strength (Athletics) or Dexterity (Acrobatics). On a success, the creature takes the object. The creature has advantage if the bearer is grappled, restrained, prone, or incapacitated. A bearer who has deliberately secured the object has advantage on the contest."
  - name: "Pass the Prize"
    desc: "A creature can hand the prize to an adjacent willing creature as an object interaction."
actions:
  - name: "Multiattack"
    desc: "The bosun makes two Boarding Axe attacks."
  - name: "Boarding Axe"
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage."
  - name: "Hook and Haul"
    desc: "Melee or Ranged Weapon Attack: +5 to hit, reach 10 ft. or range 20/60 ft., one target. Hit: 6 (1d6 + 3) piercing damage, and a Large or smaller target must succeed on a DC 13 Strength saving throw or be pulled up to 10 ft. toward the bosun."
  - name: "Clear the Deck (Recharge 5-6)"
    desc: "The bosun swings a length of chain or heavy boarding hook around it. Every creature of the bosun's choice within 10 ft. must make a DC 13 Strength saving throw. On a failure, the creature takes 7 (2d6) bludgeoning damage, is pushed 10 ft., and falls prone. On a success, the creature takes half damage and is not moved or knocked prone."
```

**Wants:** to pin the prize-bearer flat so a cutpurse can walk up and take it. The bosun makes the theft easy, not the theft itself.
**Morale:** holds as long as the captain is standing. Breaks and runs the moment the captain drops or calls retreat.

## Description

The largest hand on a pirate cutter's deck. The bosun carries a boarding axe in one hand and a hook on a line in the other, and everything about the way they move says "I have done this before and you have not." Their job is to pull a defender off balance and hold someone still long enough for the nimble hands to do the real work.

## Ecology

Pirate bosuns earn the role by surviving more boardings than anyone else in the crew. They work the same [[Midchain]] shipping lanes as the captains they serve, and between boardings they are the enforcer the crew answers to: settling disputes, assigning watches, keeping the hull sound. A bosun who cannot grapple a man in armour on a rolling deck does not keep the title long.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Isolate the bosun from allies | No other pirate within 5 ft. of the bosun's grapple target | Hold Them Still no longer applies, leaving the bosun at a flat +5 instead of advantage, and the bearer can contest more evenly | |
| Topple the bosun after Clear the Deck | Recharge spent, bosun on the ground | No area denial left and no way to stand and grapple in the same turn. The bosun wastes a full round recovering | |
