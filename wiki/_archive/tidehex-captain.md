---
type: monster
status: pending
publish: false
aliases: []
summary: "CR 5 pirate spellcaster captain who coordinates theft operations with fog, command magic, and a telekinetic snatch."
created: 2026-08-16
updated: "2026-08-16"
tags: [combat, intrigue]
tier: supporting
source: ""
found_at:
- "[[midchain]]"
- "[[midchain-west]]"
habitat: [Coastal]
statblock: inline
name: "Tidehex Captain"
cr: 5
ac: 16
hp: 93
str: 14
dex: 18
con: 18
int: 13
wis: 14
cha: 18
campaigns: [Shattered Sea]
owner_skill: ".claude/skills/draft-content/references/monster.md"
uid: da926b9e-e482-4de2-ad79-dc6aa9d48d98
---

# Tidehex Captain

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Tidehex Captain"
size: Medium
type: humanoid
alignment: "any non-lawful"
ac: 16
hp: 93
hit_dice: "11d8 + 44"
speed: "30 ft."
stats: [14, 18, 18, 13, 14, 18]
saves:
  - dex: 7
  - wis: 5
  - cha: 7
skillsaves:
  - deception: 7
  - perception: 5
  - sleight_of_hand: 7
senses: "passive Perception 15"
languages: "Common plus two others"
cr: 5
traits:
  - name: "Sea Legs"
    desc: "The captain has advantage on saving throws and ability checks to resist being knocked prone or moved against its will."
  - name: "Snatch"
    desc: "As an action, a creature within 5 ft. of another creature carrying a Tiny prize object can make a Dexterity (Sleight of Hand) check contested by the bearer's Strength (Athletics) or Dexterity (Acrobatics). On a success, the creature takes the object. The creature has advantage if the bearer is grappled, restrained, prone, or incapacitated. A bearer who has deliberately secured the object has advantage on the contest."
  - name: "Pass the Prize"
    desc: "A creature can hand the prize to an adjacent willing creature as an object interaction."
  - name: "Spellcasting"
    desc: "The captain's spellcasting ability is Charisma (spell save DC 15, +7 to hit with spell attacks). The captain can cast the following:\nAt will: mage hand, minor illusion, shocking grasp\n2/day each: command, fog cloud, misty step\n1/day each: hold person, invisibility"
actions:
  - name: "Multiattack"
    desc: "The captain makes two Cutlass or Tide Bolt attacks."
  - name: "Cutlass"
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage plus 3 (1d6) force damage."
  - name: "Tide Bolt"
    desc: "Ranged Spell Attack: +7 to hit, range 60 ft., one target. Hit: 13 (2d8 + 4) force damage."
  - name: "Arcane Snatch (Recharge 5-6)"
    desc: "The captain targets one visible creature within 30 ft. holding or openly carrying a Tiny object. The target makes a DC 15 Strength or Dexterity saving throw (its choice). On a failure, the captain magically tears the object from the creature's grasp and pulls it into an empty hand. If the object has been deliberately secured to the creature, the target makes the save with advantage."
bonus_actions:
  - name: "Captain's Orders"
    desc: "The captain chooses one allied pirate within 30 ft. that can hear them. That pirate can immediately move up to half its speed without provoking opportunity attacks, make a Snatch attempt against an adjacent creature, or pass the prize to another adjacent pirate."
reactions:
  - name: "Slip Between Worlds"
    desc: "When a creature misses the captain with a melee attack, the captain magically teleports up to 10 ft. to an unoccupied space it can see. This movement does not provoke opportunity attacks."
```

**Wants:** to take the prize and get every hand back to the ship alive. A dead crewmate costs more than the cargo is worth.
**Morale:** breaks off the instant the crew secures the prize or two of the boarding party drop, whichever comes first.

## Description

A pirate captain who learned to pull fog and force from waters that teach hard lessons. The magic is practical: fog to hide an approach, a command to make someone drop what they hold. Nothing about it looks scholarly. The gestures are quick, one-handed, performed without breaking stride or dropping a cutlass.

## Ecology

Tidehex captains command the cutter-class raiders that hunt the [[midchain|Midchain]] shipping lanes, the [[doldrums|Doldrums]] calms, and the shoal approaches to [[midchain-west|Midchain West]]. A captain who can call fog at will takes prizes without burning powder, and crews tolerate the strangeness because a tidehex captain's boarding party comes home. Most learned their craft crewing vessels that passed too close to places where the sea holds old things, picking up tricks the way other sailors pick up scars.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Kill the captain | The boarding party has no second caster | Every spell effect ends and Captain's Orders go silent. The plan collapses into a knife fight the crew cannot win | |
| Disperse the fog | First fog cloud removed by wind, [[gust\|Gust]], or similar | The captain must spend a second daily use to re-cover. Only two per day, and the second covers the retreat | |
| Secure the prize beneath armour or chain it to yourself | Bearer announces a deliberate securing measure before the fight | Bearer has advantage on Snatch contests and Arcane Snatch saves. Smart precautions matter | [[fate-spinner\|Fate Spinner]] |
| Force a melee miss on purpose | A character deliberately whiffs to trigger Slip Between Worlds | The captain teleports to a predictable spot, and the second attacker can be waiting there | |
