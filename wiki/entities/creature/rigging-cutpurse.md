---
title: "Rigging Cutpurse"
aliases:
  - Rigging Cutpurse
category: entities
tags: [shattered-sea, creature]
sources:
  - "campaign-os:rigging-cutpurse.md"
created: 2026-09-13
updated: 2026-09-13
type: creature
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "CR 1/2 agile pirate thief with advantage on prize-snatching and a keep-away toss that turns the fight into a relay."
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
# Rigging Cutpurse

> [!narration] Narration
>

## Statblock

**Stats & Combat.**

```statblock
layout: Basic 5e Layout
name: "Rigging Cutpurse"
size: Medium
type: humanoid
alignment: "any non-lawful"
ac: 14
hp: 22
hit_dice: "5d8"
speed: "30 ft., climb 20 ft."
stats: [10, 16, 10, 12, 12, 13]
skillsaves:
  - acrobatics: 5
  - sleight_of_hand: 7
  - stealth: 5
senses: "passive Perception 11"
languages: "Common"
cr: "1/2"
traits:
  - name: "Snatch"
    desc: "As an action, a creature within 5 ft. of another creature carrying a Tiny prize object can make a Dexterity (Sleight of Hand) check contested by the bearer's Strength (Athletics) or Dexterity (Acrobatics). On a success, the creature takes the object. The creature has advantage if the bearer is grappled, restrained, prone, or incapacitated. A bearer who has deliberately secured the object has advantage on the contest."
  - name: "Expert Thief"
    desc: "The cutpurse has advantage on checks made to Snatch the prize."
  - name: "Pass the Prize"
    desc: "A creature can hand the prize to an adjacent willing creature as an object interaction."
  - name: "Cunning Action"
    desc: "The cutpurse can take the Dash, Disengage, or Hide action as a bonus action."
  - name: "Rigging Runner"
    desc: "Climbing does not cost the cutpurse extra movement."
actions:
  - name: "Shortsword"
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage."
  - name: "Hand Crossbow"
    desc: "Ranged Weapon Attack: +5 to hit, range 30/120 ft., one target. Hit: 6 (1d6 + 3) piercing damage."
bonus_actions:
  - name: "Toss the Loot"
    desc: "While carrying the prize, the cutpurse throws it to an allied creature within 20 ft. that has an empty hand. The ally catches it automatically. If an enemy is within 5 ft. of the receiving pirate, that enemy can use its reaction to make a DC 13 Dexterity check, catching the object instead on a success."
```

**Wants:** to grab the prize and run. Fighting is what the bosun does. The cutpurse's hands are for taking and throwing.
**Morale:** flees the instant it takes any damage while not carrying the prize. If carrying the prize, Dashes toward extraction and tosses to the nearest ally.

## Biology

**Description.**

Light and fast, dressed in dark close-fitting clothes with soft-soled shoes and no armour heavier than a leather vest. Cutpurses climb rigging the way other people walk corridors, and their hands never stop moving. They come aboard from above or from the blind side, wherever nobody is looking.

## Behavior

**Ecology.**

Rigging cutpurses crew the same [[Midchain]] pirate cutters as [[tidehex captains]] and [[pirate-bosun|bosuns]], but captains pick them from port thieves and rooftop runners, not from the forecastle. The sea legs come later, if they come at all. What the captain pays for is hands that can lift a coin purse off a man's belt while he swings a sword at someone else, and the nerve to do it on a rolling deck.

## Tactics

**Toy Chest.**

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Ready an action to intercept a Toss | An enemy stands within 5 ft. of the receiving pirate | The enemy can use its reaction to contest the catch per Toss the Loot, ending the relay on a success | |
| Damage a cutpurse not carrying the prize | Cutpurse takes any damage | It flees, one fewer thief in the relay chain, narrowing the extraction path | |
| Grapple or restrain a cutpurse carrying the prize | Cutpurse held in place | It cannot Dash toward extraction, but Toss the Loot needs no movement, so it can still throw to a free ally within 20 ft. | |
