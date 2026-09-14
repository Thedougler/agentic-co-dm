---
title: "Boarding Raider"
category: entities
tags: [shattered-sea, creature]
sources:
  - "campaign-os:boarding-raider.md"
created: 2026-09-13
updated: 2026-09-13
type: creature
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "CR 1 pirate bruiser who charges to knock targets prone and shoves defenders out of the cutpurses' path."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Boarding Raider

# Boarding Raider

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Boarding Raider"
size: Medium
type: humanoid
alignment: "any non-lawful"
ac: 14
hp: 32
hit_dice: "5d8 + 10"
speed: "30 ft."
stats: [15, 14, 14, 9, 11, 10]
skillsaves:
  - athletics: 4
senses: "passive Perception 10"
languages: "Common"
cr: 1
traits:
  - name: "Boarding Rush"
    desc: "If the raider moves at least 15 ft. straight toward a creature before hitting it with a Cutlass attack on the same turn, the target must succeed on a DC 12 Strength saving throw or fall prone."
  - name: "Snatch"
    desc: "As an action, a creature within 5 ft. of another creature carrying a Tiny prize object can make a Dexterity (Sleight of Hand) check contested by the bearer's Strength (Athletics) or Dexterity (Acrobatics). On a success, the creature takes the object. The creature has advantage if the bearer is grappled, restrained, prone, or incapacitated. A bearer who has deliberately secured the object has advantage on the contest."
  - name: "Pass the Prize"
    desc: "A creature can hand the prize to an adjacent willing creature as an object interaction."
actions:
  - name: "Multiattack"
    desc: "The raider makes two Cutlass attacks."
  - name: "Cutlass"
    desc: "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage."
  - name: "Shoulder Check"
    desc: "The raider attempts to violently reposition a creature within 5 ft. The target must make a DC 12 Strength saving throw. On a failure, the raider either pushes the target up to 10 ft. or knocks it prone."
```

**Wants:** to hit someone hard enough to put them on the deck so a cutpurse can walk up behind. The raider does not care about the prize itself.
**Morale:** fights until bloodied (half HP), then backs toward the extraction point and uses Shoulder Check to clear a lane.

## Description

Broad and heavy, built for the first thirty seconds of a boarding action. Raiders wear studded leather over bare arms and carry a cutlass in each hand. They come over the rail at a dead run, shoulder-first, and their job is to put the first defender on the ground before the rest of the crew arrives.

## Ecology

Boarding raiders fill the same role on a [[Midchain]] pirate cutter that a [[Dravosi Enforcer]] fills on a Crown vessel: the heavy hand behind the lighter crew. Where the enforcer works hooks and gangplanks by Crown procedure, the raider works momentum and surprise. Most are former dock brawlers or failed prizefighters who found that the same skills pay better at sea.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Deny the charge line | The raider cannot move 15 ft. in a straight line (wall, obstacle, Sentinel, grapple) | Boarding Rush never triggers. The raider hits at a flat +4 with no knockdown, and becomes a mediocre damage dealer | |
| Shove the raider prone first | Raider is prone before its turn | It burns half its movement standing, cannot reach the 15-ft. charge threshold, and Shoulder Check from the ground has no leverage | |
