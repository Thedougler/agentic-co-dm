---
title: "Blight"
category: entities
tags: [shattered-sea, creature]
sources:
  - "campaign-os:blight.md"
created: 2026-09-13
updated: 2026-09-13
type: creature
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "A druid lich whose phylactery is a place, the Death Bloom in Aruhe's interior. Its combat numbers degrade in stages as the Bloom takes damage."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Blight

# Blight

![[Blight Banner]]

## Stats & Combat

### Stage 1 (Death Bloom Intact)

```statblock
layout: Basic 5e Layout
name: "Blight (Stage 1)"
size: Large
type: undead
alignment: "any alignment"
ac: 18
hp: 275
hit_dice: "34d10 + 102"
speed: "30 ft., climb 30 ft."
stats: [20, 14, 16, 17, 20, 15]
saves:
  - constitution: 9
  - wisdom: 11
skillsaves:
  - nature: 10
  - perception: 11
  - survival: 11
damage_resistances: "cold, necrotic, poison; bludgeoning, piercing, and slashing from nonmagical attacks"
condition_immunities: "charmed, exhaustion, frightened, paralyzed, poisoned"
senses: "darkvision 120 ft., passive Perception 21"
languages: "Druidic, the languages it knew in life"
cr: "19"
traits:
  - name: "Rooted Phylactery"
    desc: "While the Death Bloom remains intact, a destroyed Blight reforms at the Death Bloom in 1d10 days. Destroying the Death Bloom prevents this permanently."
  - name: "Corrupted Ground"
    desc: "The Blight can move through nonmagical plants without spending extra movement and without being slowed by them, and difficult terrain within 1 mile of the Death Bloom costs it no extra movement."
  - name: "Turn Resistance"
    desc: "The Blight has advantage on saving throws against any effect that turns undead."
spells:
  - "Spellcasting. The Blight casts spells using Wisdom as its spellcasting ability (spell save DC 19, +11 to hit) and requires no material components."
  - "At will: Druidcraft, Produce Flame, Thorn Whip"
  - "3/day each: Entangle, Moonbeam, Plant Growth, Spike Growth"
  - "2/day each: Insect Plague, Wall of Thorns"
  - "1/day each: Circle of Death, Foresight, Sunburst"
actions:
  - name: "Multiattack"
    desc: "The Blight makes two Rotten Claw attacks."
  - name: "Rotten Claw"
    desc: "Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 16 (2d10 + 5) slashing damage plus 10 (3d6) poison damage."
  - name: "Acid Bloom (Recharge 5-6)"
    desc: "The Blight causes corrosive sap to erupt in a 20-foot-radius sphere centered on a point it can see within 60 feet. Each creature in that area must make a DC 19 Dexterity saving throw, taking 36 (8d8) acid damage on a failed save, or half as much damage on a successful one."
legendary_actions:
  - name: ""
    desc: "The Blight can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The Blight regains spent legendary actions at the start of its turn."
  - name: "Grasping Roots"
    desc: "Roots burst from the ground in a 10-foot square the Blight can see within 60 feet. Each creature there must succeed on a DC 19 Strength saving throw or be restrained until the end of its next turn."
  - name: "Rotten Claw (Costs 2 Actions)"
    desc: "The Blight makes one Rotten Claw attack."
  - name: "Spore Burst (Costs 2 Actions)"
    desc: "One creature the Blight can see within 30 feet must succeed on a DC 19 Constitution saving throw or be poisoned until the end of its next turn."
  - name: "Feed the Bloom (Costs 3 Actions)"
    desc: "The Blight regains 20 hit points, drawn from the Death Bloom."
```

### Stage 2 (Death Bloom Damaged)

```statblock
layout: Basic 5e Layout
monster: "Blight (Stage 1)"
name: "Blight (Stage 2)"
ac: 16
hp: 165
hit_dice: "22d10 + 44"
stats: [18, 12, 14, 15, 17, 12]
saves:
  - constitution: 6
  - wisdom: 7
skillsaves:
  - nature: 6
  - perception: 7
senses: "darkvision 90 ft., passive Perception 17"
cr: "13"
traits-:
  - name: "Corrupted Ground"
traits+:
  - name: "Corrupted Ground"
    desc: "The Blight can move through nonmagical plants without spending extra movement and without being slowed by them."
spells:
  - "Spellcasting. The Blight casts spells using Wisdom as its spellcasting ability (spell save DC 15, +7 to hit) and requires no material components."
  - "At will: Druidcraft, Produce Flame, Thorn Whip"
  - "2/day each: Entangle, Moonbeam, Spike Growth"
  - "1/day each: Insect Plague, Wall of Thorns"
actions-:
  - name: "Rotten Claw"
  - name: "Acid Bloom (Recharge 5-6)"
actions+:
  - name: "Rotten Claw"
    desc: "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) slashing damage plus 7 (2d6) poison damage."
  - name: "Acid Bloom (Recharge 6)"
    desc: "The Blight causes corrosive sap to erupt in a 15-foot-radius sphere centered on a point it can see within 60 feet. Each creature in that area must make a DC 15 Dexterity saving throw, taking 22 (4d10) acid damage on a failed save, or half as much damage on a successful one."
legendary_actions-:
  - name: "Spore Burst (Costs 2 Actions)"
  - name: "Feed the Bloom (Costs 3 Actions)"
legendary_actions:
  - name: ""
    desc: "The Blight can take 2 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The Blight regains spent legendary actions at the start of its turn."
  - name: "Grasping Roots"
    desc: "Roots burst from the ground in a 10-foot square the Blight can see within 60 feet. Each creature there must succeed on a DC 15 Strength saving throw or be restrained until the end of its next turn."
  - name: "Rotten Claw (Costs 2 Actions)"
    desc: "The Blight makes one Rotten Claw attack."
```

### Stage 3 (Death Bloom Nearly Destroyed)

```statblock
layout: Basic 5e Layout
monster: "Blight (Stage 1)"
name: "Blight (Stage 3)"
ac: 14
hp: 75
hit_dice: "10d10 + 20"
speed: "20 ft., climb 10 ft."
stats: [15, 10, 12, 12, 13, 10]
saves-:
  - constitution
  - wisdom
skillsaves-:
  - nature
  - perception
  - survival
skillsaves:
  - nature: 3
senses: "darkvision 60 ft., passive Perception 11"
damage_resistances: "poison; bludgeoning, piercing, and slashing from nonmagical attacks"
condition_immunities: "charmed, exhaustion, frightened, poisoned"
cr: "7"
traits-:
  - name: "Turn Resistance"
spells-:
  - "Spellcasting. The Blight casts spells using Wisdom as its spellcasting ability (spell save DC 19, +11 to hit) and requires no material components."
actions-:
  - name: "Multiattack"
  - name: "Rotten Claw"
  - name: "Acid Bloom (Recharge 5-6)"
actions:
  - name: "Rotten Claw"
    desc: "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage plus 4 (1d8) poison damage."
  - name: "Acid Seep (Recharge 6)"
    desc: "A 10-foot-radius patch of ground the Blight can see within 30 feet wells up with acid. Each creature there must make a DC 12 Dexterity saving throw, taking 10 (3d6) acid damage on a failed save, or half as much damage on a successful one. The patch remains as a hazard for 1 minute, and any creature that enters it or starts its turn there for the first time on a turn must make the same save."
legendary_actions-:
  - name: "Grasping Roots"
  - name: "Rotten Claw (Costs 2 Actions)"
```

A Pointy Hat homebrew build — The Blight, a druid lich — reconstructed from scratch per `creature-prep`'s CR-and-monster-design method, not transcribed from any vendored source, unlike [[Necromaton]] and [[Hierarch]]. Stage 1 (Death Bloom intact) is the primary registered block above; Stage 2 (Death Bloom damaged) and Stage 3 (Death Bloom nearly destroyed) recall it and override only the fields that change — swap stat blocks live, mid-fight, at the trigger points below, since this is a phylactery-health gate, not a standard 50%-HP phase transition.

**Behavior states**

| State | Trigger | Behavior |
|---|---|---|
| Stage 1 | Death Bloom whole | Fights near the height of her strength. |
| Stage 2 | Real damage lands on the Death Bloom | Weaker and duller across the board. |
| Stage 3 | Death Bloom near ruin | Turns desperate, leans on hazards in the surrounding room. |

**Wants:** to hold [[Aruhe]] inviolate in her drowned companion's memory, punishing any hand that takes the island's fruit, river catch, foraged growth, or trapped game, though every real fight against her chips the Death Bloom itself, the one thing she can't regrow as fast as she's asked to defend it.
**Morale:** falls back a stage with each real hit that reaches the Death Bloom, weaker and more desperate at every step down. Only wrecking the Bloom outright ends her for good.

> [!narration] Narration
> The treeline opens onto a grove that shouldn't still be standing this deep into an abandoned island, grass too green, fruit hanging heavy and unpicked, the air sweet with rot that never finishes rotting. At the center, a single tree holds fruit that was already ripe when whoever planted it died, its roots shifting under ground that doesn't just look disturbed, like something underneath is still breathing. A voice comes from everywhere in the grove at once, patient and certain, asking who gave you leave to walk here. Nothing about the tree has hands, and it doesn't need any.


## Description

[[Aruhe]] hosts an active Blight, and the abandoned island's interior is its dungeon. Sailors who know the island at all know two things about it: it's the best landfall in the region, and nothing that's tried to take from it has come back to say so. Any [[Grung]] or other invader who lays a hand on Aruhe's plenty, its fruit, its river catch, its foraged growth, or its trapped game, meets Nature's fury in full, and the island takes them back into the dirt. The [[grung-clans|Grung Clans]] patrol the reefs nearby but refuse to land.

## Ecology

A Blight starts as an Archdruid who fuses their soul and body to a piece of land they want to protect, and the ritual kills them. What's left is a druid lich whose phylactery is not an object or a living being but **a place**, the Death Bloom, a spot deep in the protected land. Other liches die when someone finds and smashes a phylactery object; not a Blight. The Death Bloom is a location, a dungeon whoever hunts it has to clear, and no item exists anywhere for them to steal. While the Death Bloom stands, a destroyed Blight comes back.

This one's power drops as damage to the Death Bloom piles up. With the Bloom whole, she fights at Stage 1, near the height of her strength; real damage knocks her down to Stage 2, weaker and duller across the board; near-ruin drops her further, to Stage 3, where she turns desperate and leans on hazards in the room around her. Wreck the Death Bloom outright, and she stays dead for good.

Background horror creatures like this one are rare in this campaign. She's one of the few staged so far, alongside the still-unplaced [[gentle-hag]], another fey hag horror.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Land real damage on the Death Bloom | Bloom whole (Stage 1) | She falls back a stage, weaker and duller (Stage 2), then desperate and hazard-leaning (Stage 3) | [[Aruhe]] |
| Take Aruhe's fruit, river catch, foraged growth, or trapped game | Any invader on the island | Nature's fury falls on the taker, and the island drags them into the dirt | [[grung-clans|Grung Clans]] |

## Prepped Reveals

This Blight was once a captive Archdruid, held on [[Karath]] and drugged into casting for the [[grung-clans|Grung Clans]]' hatchery, until she and a fellow captive burned it down and ran for the cliff, going off its edge together into the half-mile channel beyond. He took an arrow on the open stone past the treeline, four strides short of the cliff, and by the time her feet found Aruhe's sand, he was twenty feet behind her, already gone. The island opened a path for her that led to a grove at its center, where a tree stood in fruit already, the same fruit he used to eat. She buried him under it, and that tree is the Death Bloom now. She bound her own soul into the ground over his grave and asked the island for one thing in return. Aruhe's own page names the island in Grung and what the name means.
