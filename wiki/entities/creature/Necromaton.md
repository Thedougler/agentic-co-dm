---
title: "Necromaton"
category: entities
tags: [shattered-sea, creature]
sources:
  - "campaign-os:necromaton.md"
created: 2026-09-13
updated: 2026-09-13
type: creature
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "CR 20 artificer lich whose phylactery is a biological anchor organ inside a self-built construct body, running three chassis variants (Base, Flying, Bulldozer) that share one soul via Soul Transfer"
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Necromaton

## Stats & Combat

### Base Model (Ground)

```statblock
layout: Basic 5e Layout
name: "Necromaton (Base)"
size: Medium
type: undead
alignment: "any alignment"
ac: 19
hp: 153
hit_dice: "18d8 + 72"
speed: "30 ft."
stats: [16, 18, 19, 20, 14, 15]
saves:
  - constitution: 10
  - intelligence: 11
skillsaves:
  - arcana: 11
  - investigation: 11
  - medicine: 8
  - "sleight of hand": 10
damage_resistances: "cold"
damage_immunities: "necrotic, poison; bludgeoning, piercing, and slashing from nonmagical attacks"
condition_immunities: "charmed, exhaustion, frightened, paralyzed, poisoned"
senses: "truesight 120 ft., passive Perception 12"
languages: "the languages it knew in life"
cr: "20"
traits:
  - name: "Necromaton Phylactery"
    desc: "The Necromaton's body is its phylactery, anchored by a biological soul component. It is permanently destroyed only if all of its construct bodies are destroyed."
  - name: "Magic Resistance"
    desc: "The Necromaton has advantage on saving throws against spells and other magical effects."
  - name: "Turn Resistance"
    desc: "The Necromaton has advantage on saving throws against any effect that turns undead."
  - name: "Inventory"
    desc: "The Necromaton is always aware of the exact location of all of its phylactery bodies."
  - name: "Soul Transference"
    desc: "The Necromaton can move its soul to another of its construct bodies. Doing so takes an amount of time based on the distance to that body: instantaneous within 500 feet, 1 hour within 10 miles, 1 day within 60 miles, 1 week anywhere else on the same plane, or 1 week to reach another plane."
spells:
  - "Spellcasting. The Necromaton casts spells using Intelligence as its spellcasting ability (spell save DC 19, +11 to hit) and requires no material components."
  - "At will: Mage Hand, Mending, Alarm, Catapult, Magic Missile (4th level), Thunderwave (3rd level)"
  - "3/day each: Counterspell, Heat Metal, Hold Person, Magic Weapon, Scorching Ray, Shatter"
  - "2/day each: Fireball (5th level), Haste, Protection from Energy, Resilient Sphere"
  - "1/day each: Animate Objects (7th level), Arcane Hand (7th level), Wall of Force, Seeming"
actions:
  - name: "Spellcasting"
    desc: "The Necromaton casts spells using Intelligence as its spellcasting ability (spell save DC 19, +11 to hit) and requires no material components. At will: Mage Hand, Mending, Alarm, Catapult, Magic Missile (4th level), Thunderwave (3rd level). 3/day each: Counterspell, Heat Metal, Hold Person, Magic Weapon, Scorching Ray, Shatter. 2/day each: Fireball (5th level), Haste, Protection from Energy, Resilient Sphere. 1/day each: Animate Objects (7th level), Arcane Hand (7th level), Wall of Force, Seeming."
  - name: "Arm Cannon"
    desc: "Ranged Weapon Attack: +9 to hit, range 150/600 ft., one target. Hit: 17 (4d6 + 3) lightning damage."
  - name: "Arm Torch"
    desc: "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 17 (4d6 + 3) bludgeoning damage plus 7 (2d6) fire damage."
legendary_actions:
  - name: ""
    desc: "The source material lists four legendary action options but does not state how many the Necromaton can take per round. Standard 5e convention for a CR 20 solo is 3, but that specific number is not sourced; a DM call before this creature is run at the table."
  - name: "Missile"
    desc: "The Necromaton casts Magic Missile, using a 4th-level spell slot."
  - name: "Spell"
    desc: "The Necromaton casts a spell it knows that doesn't deal damage, using a spell slot as normal."
  - name: "Arm Attack"
    desc: "The Necromaton makes one Arm Cannon or Arm Torch attack."
  - name: "Propulsed Backstep"
    desc: "The Necromaton moves up to its speed without provoking opportunity attacks."
lair_actions:
  - desc: "On initiative count 20, the Necromaton takes one of the following lair actions; the source does not state whether it can repeat the same one on consecutive rounds."
  - desc: "The Necromaton extends necromantic energy to constructs within 90 feet of it. Until initiative count 20 on the next round, those constructs' attacks deal an extra 1d8 necrotic damage on a hit."
  - desc: "The Necromaton sends a shock through one construct within 60 feet of it. Until initiative count 20 on the next round, that construct's speed is doubled and it can take two actions and two reactions on each of its turns."
  - desc: "The Necromaton grants arcane gifts to constructs within 30 feet of it. Until initiative count 20 on the next round, each of those constructs can use its action to cast Mending, restoring 2d6 hit points to a construct it touches instead of Mending's normal effect."
```

### Flying Model

Small chassis, built for a scout/sniper role. Every field below overrides
Base; the source's own delta format leaves every other field (saves,
skillsaves, resistances/immunities, senses, languages, spells, legendary
actions, lair actions) matching the Base Model.

```statblock
layout: Basic 5e Layout
monster: "Necromaton (Base)"
name: "Necromaton (Flying)"
size: Small
ac: 17
hp: 135
hit_dice: "18d6 + 72"
speed: "30 ft., fly 60 ft. (hover)"
stats: [16, 20, 19, 20, 14, 15]
actions-:
  - name: "Arm Cannon"
actions+:
  - name: "Arm Cannon"
    desc: "Ranged Weapon Attack: +11 to hit, range 150/600 ft., one target. Hit: 19 (4d6 + 5) lightning damage."
traits+:
  - name: "Sniper"
    desc: "The Necromaton has no disadvantage on ranged attack rolls against targets beyond normal range, and its Arm Cannon deals an extra 1d6 damage against a target when no creatures are within 5 feet of that target."
```

### Bulldozer Model

Large chassis, built for a tank role. Every field below overrides Base;
all other fields inherit unchanged, same as the Flying Model above.

```statblock
layout: Basic 5e Layout
monster: "Necromaton (Base)"
name: "Necromaton (Bulldozer)"
size: Large
ac: 21
hp: 171
hit_dice: "18d10 + 72"
speed: "50 ft., burrow 30 ft."
stats: [20, 18, 19, 20, 14, 15]
actions-:
  - name: "Arm Torch"
actions+:
  - name: "Arm Torch"
    desc: "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 19 (4d8 + 5) bludgeoning damage."
traits+:
  - name: "Charge"
    desc: "If the Necromaton moves at least 20 feet straight toward a target and then hits it with an Arm Torch attack on the same turn, the target takes an extra 9 (2d8) bludgeoning damage and must succeed on a DC 19 Strength saving throw or be knocked prone."
```

**Base (Ground)** above is the primary registered block for this
Necromaton's one shared soul. **[[Flying]]** and **Bulldozer**
recall it and override only the fields the source states as different,
and the source's own delta format leaves every unlisted field matching
Base. Lair Actions live on the Base block only, since they belong to the
Necromaton's lair and not to any single chassis, so they apply no matter
which body is currently active in a fight. The source is Pointy Hat.

**Wants:** to keep existing indefinitely, building, maintaining, and moving its soul between as many construct bodies as it can sustain, so that no single body's ruin is ever its end.
**Morale:** a single construct body reaching 0 hit points doesn't end the fight. Its soul relocates to another body it maintains (Soul Transference) unless every body it has is already destroyed, and only losing every one ends it, permanently.

> [!narration] Narration
> Metal footsteps land too evenly, the stride locked to the same length every time, the knees rigid through each step.
>
> One arm ends in a cannon housing, the other in a torch nozzle still ticking as it cools.
>
> Nothing about the construct breathes, and nothing about it needs to. Whatever used to be a person moved into this body a long time ago, and it isn't going anywhere.
>
> It doesn't blink, because there's nothing in the sockets to blink. It's already looking straight at you.


## Description

Common knowledge about this specific creature kind isn't established yet
in this campaign. No Necromaton has appeared at the table, so no
in-world rumor or folk warning exists until the DM stages an encounter.
What the read-aloud description above gives away is all a witness would
have to go on: metal, unhurried, and armed for a fight it doesn't expect
to lose.

## Ecology

A Necromaton is an artificer who achieved lichdom by building a construct
body and transferring their soul into it, anchored by a biological
component (typically a preserved organ) housed inside the construct. The
metal body is a vessel. The organ is the true phylactery. A Necromaton can
build and inhabit as many construct bodies as it can maintain, moving its
soul between them, and it must constantly maintain and eventually replace each
body's biological anchor as it decays. A Necromaton is never finished
building. The source gives no sensory tell for running this creature
beyond its physical description (a metal chassis, an Arm Cannon or Arm
[[Torch]] housing); a DM call once it's staged for a real encounter.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Destroy a construct body the Necromaton currently occupies | It has at least one other maintained body still standing | Its soul relocates there (Soul Transference) instead of ending the fight; only losing every body ends it | |
| Crack open a downed body and examine its anchor organ | The Necromaton has already lost a construct body in this fight | An Arcana or Investigation check reveals how decayed that anchor is, and lets an artificer's eye, like [[catarina-davirelli]]'s, read the chassis's own engineering choices at a glance | [[catarina-davirelli]] |
| Track down and destroy every body it maintains | Its hunters have found every construct body it maintains | The Necromaton is permanently destroyed, its only true end | |

## Prepped Reveals

The source states that destroying every construct body a Necromaton
maintains permanently ends it. A party that finds and destroys a single
body has not, on that basis alone, ended the fight. How
many bodies a Necromaton currently maintains, and where they are, is a DM
call the source doesn't answer generically. It's specific to whichever
Necromaton the DM stages.
