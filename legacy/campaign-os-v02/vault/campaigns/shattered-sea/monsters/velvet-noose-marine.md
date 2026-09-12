---
type: monster
status: draft
publish: false
aliases: ["Velvet Noose Corsair"]
summary: "Corsair marine aboard the Velvet Noose — pairs on a target, holds position when two of four are down, retreats on the Captain's signal."
created: "2026-08-11"
updated: "2026-08-11"
tags: [combat]
tier: supporting
source: ""
source_url: ""
found_at:
- "[[central-strait|Central Strait]]"
- "[[midchain|Midchain]]"
habitat: [Coastal]
statblock: inline
name: "Velvet Noose Marine"
cr: 0.5
ac: 11
hp: 32
str: 15
dex: 11
con: 14
int: 10
wis: 10
cha: 11
campaigns: [Shattered Sea]
owner_skill: ".claude/skills/draft-content/references/monster.md"
uid: 9e5f1a6b-3c4d-4a7e-1b0f-8c9d0e1f2a3b
---

# Velvet Noose Marine

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Velvet Noose Marine"
size: Medium
type: humanoid
alignment: "neutral evil"
ac: 11
hp: 32
hit_dice: "5d8 + 10"
speed: "30 ft."
stats: [15, 11, 14, 10, 10, 11]
skillsaves:
  - athletics: 4
  - intimidation: 2
senses: "Passive Perception 10"
languages: "Common"
cr: "1/2"
traits:
  - name: Sea Legs
    desc: "Difficult terrain caused by ship movement, waves, or wet deck does not cost this creature extra movement."
  - name: Pack Tactics
    desc: "This creature has advantage on attack rolls against a creature if at least one of this creature's allies is adjacent to the target and the ally isn't incapacitated."
actions:
  - name: Multiattack
    desc: "The marine makes two Mace attacks."
  - name: Mace
    desc: "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) bludgeoning damage."
```

**Wants:** hold the boarding zone and keep any path to the quarterdeck blocked until the Captain signals withdrawal.
**Morale:** holds when 2 of 4 marines are down; retreats to the rope ladder when the Captain calls it aloud.

> [!read-aloud]
> Four of them take positions at the stern rail without looking at anyone in particular. They do not draw weapons. They do not need to — the Noose is ninety yards off with the long cannon port closed and the gun-crew visible on deck.

## Description

[[the-velvet-noose|Velvet Noose]] boarding marines: disciplined, unhurried, and keyed entirely to the Captain's rhythm. They arrive last, position without instruction, and say nothing during the parley. They are not guards. They are punctuation.

## Ecology

The Noose's marines rotate between shipboard duty, harbour work in [[midchain|Midchain]], and the occasional port enforcement job the Captain takes on contract. They do not serve for prize money — the Noose pays a wage above the Crown rate, which buys a specific kind of silence and a specific kind of professionalism.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Split the pairing | One marine isolated from its partner while both above half HP | The isolated marine holds position rather than advance; the unsupported partner hesitates | [[encounter-velvet-noose-intercept\|Velvet Noose Intercept]] |
| Cut the grapple-lines | Two or more lines cut in a single turn during full boarding | Boarding rate stops; marines already aboard hold but no new ones come over — the Captain's ceasefire condition | [[encounter-velvet-noose-intercept\|Velvet Noose Intercept]] |
| Signal the retreat | Captain calls withdrawal aloud at ≤25 HP or First Mate falls | Marines follow on the Captain's next turn; First Mate covers the ladder | [[mave-sorn\|Mave Sorn]] |
