---
type: monster
status: canon
publish: false
aliases: []
summary: "A young Dravosi Crown patrol sailor trained for inspections, boarding duties, and buying time for heavier Crown response."
created: 2026-07-30
updated: 2026-08-09
tags: [combat]
tier: supporting
source: ""
found_at:
- "[[calders-tooth|Calder's Tooth]]"
- "[[central-strait|Central Strait]]"
habitat: [Coastal]
statblock: inline
name: "Dravosi Deckhand"
cr: 0.125
ac: 13
hp: 11
str: 11
dex: 13
con: 12
int: 9
wis: 10
cha: 8
campaigns: [Shattered Sea]
owner_skill: ".claude/skills/draft-content/references/monster.md"
uid: 3c984776-e5ec-4c20-8c7b-381e39838036
---

# Dravosi Deckhand

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: Dravosi Deckhand
size: Medium
type: entity
subtype: "human"
alignment: "lawful neutral"
ac: 13
hp: 11
hit_dice: "2d8 + 2"
speed: "30 ft."
stats: [11, 13, 12, 9, 10, 8]
skillsaves:
  - athletics: 2
senses: "passive Perception 10"
languages: "Common"
cr: "1/8"
traits:
  - name: Sea Legs
    desc: "Difficult terrain caused by ship movement, waves, or wet deck does not cost this creature extra movement."
actions:
  - name: Cutlass
    desc: "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) slashing damage."
  - name: Hand Crossbow
    desc: "Ranged Weapon Attack: +3 to hit, range 80/320 ft., one target. Hit: 4 (1d6 + 1) piercing damage."
reactions:
  - name: Alert Call
    desc: "When this creature takes damage, it shouts an alarm audible up to 300 feet away. Any hidden creatures within earshot are no longer hidden from creatures that hear the alarm."
```

## Description

[[dravosi-crown|Dravosi Crown]] patrol sailors assigned to routine inspections and boarding duties, most stationed out of gate posts like [[calders-tooth|Calder's Tooth]]'s inspection port. Young, underpaid, and drilled just enough to bluff confidence at a gangway, a Deckhand checks manifests and blocks the way aboard with a hand on the cutlass hilt; the moment resistance starts, the job is to shout and buy time until a [[dravosi-enforcer|Dravosi Enforcer]] arrives to finish it.

## Ecology

Deckhands work in pairs or trios aboard Crown patrol cutters like the [[hcs-relentless|HCS Relentless]], rotating between shipboard duty and shore postings along the [[central-strait|Central Strait]]. They defer instantly to any Enforcer or officer present and rarely act alone; caught without backup, a Deckhand stalls rather than fights.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Bribe | Deckhand alone, off the ship's manifest log | Waves the party through without a search, but reports the exchange to a superior later | [[calders-tooth\|Calder's Tooth]] |
| Provoke into shouting | Deckhand takes damage before it can act | Alert Call triggers immediately, ending stealth and drawing any nearby Enforcer | [[dravosi-enforcer\|Dravosi Enforcer]] |
| Disarm | Deckhand reduced below half HP | Drops the cutlass and backs toward the nearest exit rather than press the fight | |
