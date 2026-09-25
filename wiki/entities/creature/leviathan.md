---
title: "Leviathan"
category: entities
tags: ["shattered-sea", "creature"]
sources:
  - "campaign-os:leviathan-narration-appearance.md"
  - "legacy: /Users/nick/shattered-sea/wiki/shattered-sea/location-umberlee-shrine-vel-orn.md"
  - "legacy: /Users/nick/shattered-sea/wiki/shattered-sea/event-delmar-umberlee-bargain.md"
  - "legacy: /Users/nick/shattered-sea/wiki/shattered-sea/pearl-and-the-maw/region-drowned-maw.md"
  - "legacy: /Users/nick/shattered-sea/wiki/shattered-sea/pearl-and-the-maw/vehicle-dead-lady.md"
  - "legacy: /Users/nick/shattered-sea/wiki/shattered-sea/schism-of-the-eyrie/faction-sentinels-of-the-eyrie.md"
  - "/Users/nick/Documents/ai-co-dm/campaigns/shattered-sea/vehicles/Red Lady - Dead Lady.md"
  - "campaign-os:leviathan.md"
summary: "Named horror that answers the Pearl's broadcast across the Maw boundary."
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
tier: supporting
created: 2026-09-13T20:50:00Z
updated: 2026-09-13
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: ""
role: ""
cr: ""
---

# Leviathan

> [!narration] Narration
>

![[leviathan-banner]]

**Wants:** to hunt the open water the breach pulled it into and force any threat back toward that same breach, though [[Auralis]] holds it short of that, and every ship it corners is really that older fight spilling over.
**Morale:** breaks off and submerges the moment its HP drops below half. It hunts for the kill, never the grudge, and never fights to the death.

![[leviathan-narration-appearance]]


## Statblock

**Stats & Combat.**

```statblock
layout: Basic 5e Layout
name: "Leviathan"
size: Gargantuan
type: elemental
alignment: unaligned
ac: 19 (natural armor)
hp: 315
hit_dice: "17d20 + 136"
speed: "20 ft., swim 60 ft."
stats: [26, 14, 26, 6, 16, 10]
saves:
  - Dex: +8
  - Con: +14
  - Wis: +9
skillsaves:
  - Perception: +9
damage_resistances: "lightning; bludgeoning, piercing, and slashing from nonmagical attacks"
damage_immunities: "cold"
condition_immunities: "blinded, exhaustion, frightened, prone"
senses: "blindsight 120 ft. (blind beyond this radius), passive Perception 19"
languages: "understands Aquan but can't speak"
cr: "17"
traits:
  - name: "Amphibious"
    desc: "The Leviathan can breathe air and water."
  - name: "Turbulent Wake"
    desc: "While the Leviathan is within 30 feet of the surface, the water around it churns and boils, and the area within 15 feet of it is difficult terrain for Small or larger creatures."
actions:
  - name: "Multiattack"
    desc: "The Leviathan makes two attacks: one Bite and one Crushing Coil."
  - name: "Bite"
    desc: "Melee Weapon Attack: +14 to hit, reach 15 ft., one target. Hit: 34 (4d12 + 8) piercing damage."
  - name: "Crushing Coil"
    desc: "Melee Weapon Attack: +14 to hit, reach 20 ft., one creature. Hit: 30 (4d10 + 8) bludgeoning damage, and the target is grappled (escape DC 22). Until this grapple ends, the target is restrained, and the Leviathan can't use Crushing Coil on another target."
  - name: "Riftbolt (Recharge 5–6)"
    desc: "The Leviathan discharges planar lightning in a 90-foot line that is 5 feet wide. Each creature in that line must make a DC 19 Dexterity saving throw, taking 66 (12d10) lightning damage on a failed save, or half as much damage on a successful one."
legendary_actions:
  - name: ""
    desc: "The Leviathan can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The Leviathan regains spent legendary actions at the start of its turn."
  - name: "Surge"
    desc: "The Leviathan moves up to half its speed without provoking opportunity attacks."
  - name: "Coil (Costs 2 Actions)"
    desc: "The Leviathan makes one Crushing Coil attack."
  - name: "Submerge Pulse"
    desc: "Each creature within 15 feet of the Leviathan must succeed on a DC 19 Strength saving throw or be knocked prone."
```

## Biology

**Description.**

Sailors who've seen it and lived describe a shape "longer than two ships," flat black and eyeless, hide like wet stone, not scale. It doesn't hunt like a shark working a chum line. It doesn't circle, doesn't test, coming straight up from directly below whatever's loudest, the water around it boiling as lightning cracks a clear sky with no storm behind it. Full accounts don't exist. What does is wreckage, one confirmed survivor, and captains who trade the phrase "Vestra water" without agreeing on what actually does the killing out there.

## Behavior

**Ecology.**

The Leviathan crossed from the Elemental Plane of Water when the [[pearl-of-souls]] turned the breach under [[drowned-maw]] into an attractor and pulled it through the fissure, the first of at least three entities that same pull has drawn across, alongside Ridgeback and Krakling (see Notable Individuals). All three share the same flat-black, eyeless hide, blindsight in place of sight, and full water breathing, marking them as one displaced kind, not three unrelated horrors. [[elemental-plane-of-water|The Elemental Plane of Water]] itself stays undocumented past the breach. What still pushes and scrapes at the fissure from the far side is bigger than anything that's come through yet.

It now ranges The Drowned Maw's lower depths and the open water of [[outer-reach|the Outer Reach]] beyond it, sharing that lightless range with the kraken and dragon-turtle-class predators already established there. [[Auralis]], the demigod construct bound to hold the fissure shut, reads it as a parasitic invader trespassing in the realm that is his alone to Guard.

[[perrin-black-jaw]]'s account is the closest thing to firsthand testimony: something massive rose under the *[[Vestra]]*, the water boiled, lightning cracked a clear sky, and then there was nothing. He never said no one else survived. [[nona-black-jaw]] understood anyway when he tried to tell her in her kitchen. He named it "the Leviathan" only afterward, never at the table, once he needed a word for what took his family's ship.

Whether it actually sank the *Vestra* stays the open question the table hasn't closed: it's the leading account, medium confidence, with [[Umberlee]]'s own motive against Fisk's fleet running as the strongest counter-theory (full case notes in `Inbox/situations/active/what-sunk-the-vestra.md`). The table has settled one fact under that question, not theory: [[Auralis]], not the cloak Perrin credits, actually kept him alive in the wreck, forging an unwitting warlock pact between them that the table doesn't have yet (see [[perrin-black-jaw]] § Arc Notes). He washed up alone on [[keth-naar]] afterward, the only *Vestra* survivor anyone's found.

This convergence (the Pearl of Souls, Perrin's Leviathan encounter, and [[crissdalynn-khinriss|Crissdalynn]]'s unfinished mapping of the Maw) all trace back to the same stretch of water, making it one of the highest-value threads the whole crew is already tangled in, not just Perrin's grudge.

**Notable Individuals.**

Ridgeback and Krakling are the second and third entities the Pearl of Souls' pull has drawn through The Drowned Maw's fissure, not this creature under other names, but the same displaced kind, sharing its flat-black eyeless hide, blindsight, and water breathing. [[algernon-reginald-clyde|Clyde's Bestiary]] documents Ridgeback. Krakling is a juvenile arm-predator sailors have reported near [[Midchain]]. Neither has a page of its own yet.

## Tactics

**Toy Chest.**

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Cut it loose mid-grapple | The Leviathan's Crushing Coil holds a creature | Breaking the grip early costs the Leviathan its follow-up attack that turn and briefly exposes the coil to a called shot | [[perrin-black-jaw]] (the only known survivor of a Vestra-scale grip) |
| Read the boil before the strike | Riftbolt is off recharge, about to fire | Watching the water for the heat shimmer buys one round's warning before the lightning line comes | [[Vestra]] |
| Drive it back toward the breach | The fight happens within reach of The Drowned Maw's fissure | Forcing it toward the rift risks reopening the pull the Pearl of Souls created, and something larger is still pushing from the other side | [[pearl-of-souls]], [[elemental-plane-of-water]] |

**Prepped Reveals.**

**Nature or Arcana — Recognizing the Displaced Kind**

DC 15. Anyone who gets a good look at the hide may roll.
**Success:** the flat-black, eyeless hide and blindsight match two smaller predators sailors have separately reported, Ridgeback and Krakling, confirming more than one Elemental Plane of Water entity has already crossed through The Drowned Maw's breach.
**Failure:** nothing beyond what's already obvious, that this thing doesn't behave like any known sea predator.
