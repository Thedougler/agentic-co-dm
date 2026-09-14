---
title: "Island Mimic"
category: entities
tags: [shattered-sea, creature]
sources:
  - "campaign-os:island-mimic.md"
created: 2026-09-13
updated: 2026-09-13
type: creature
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "A mimic grown to island scale over centuries, wearing a small tropical paradise as bait for a full generous day before its bay closes."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Island Mimic

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Island Mimic"
size: Gargantuan
type: monstrosity
alignment: Unaligned
ac: 17
hp: 122
hit_dice: "7d20 + 49"
speed: "0 ft."
stats: [24, 6, 24, 2, 13, 4]
saves:
  - Con: +11
  - Wis: +5
damage_vulnerabilities: "fire"
damage_immunities: "bludgeoning, piercing, and slashing from nonmagical attacks; poison"
condition_immunities: "charmed, exhaustion, frightened, grappled, paralyzed, petrified, poisoned, prone, restrained, stunned, unconscious"
senses: "tremorsense 1 mile; passive Perception 11"
languages: "understands no languages but understands when it is being burned"
cr: 12
traits:
  - name: "Legendary Resistance (3/Day)"
    desc: "If the island fails a saving throw, it can choose to succeed instead."
  - name: "Fire Release"
    desc: "Whenever the island takes fire damage, it immediately releases every creature within 30 feet of the damage's source, ending the Grappled condition on each of them."
  - name: "Adhesive Ground (Interior Only, While Triggered)"
    desc: "The ground adheres to any creature on the island's interior. When Adhesive Ground triggers, every creature already on the interior has the Grappled condition. Any creature that afterward enters or starts its turn on the interior likewise has the Grappled condition, automatically, no saving throw. Escape DC 17 Athletics or Acrobatics. Ability checks made to escape have Disadvantage."
  - name: "Total Release (0 Hit Points)"
    desc: "The island can't be killed by damage. When it is reduced to 0 hit points, it lets go completely: every creature it has Grappled is freed, Adhesive Ground ends, the heads stop closing and grind back open to their full 240-foot width, and the island goes dormant and drifts off to heal. It is not dead, and it will be somewhere else within the season."
  - name: "Wounded Resolve"
    desc: "The first time the island is reduced to 62 hit points or fewer, it stops being patient: for the rest of the encounter, its Heads Close lair action narrows the gap by 40 feet instead of 20, to the same 14-foot minimum. This doesn't stack with Close the Throat — once Wounded Resolve is active, Heads Close already narrows by 40 feet, and spending legendary actions on Close the Throat has no further effect."
actions:
  - name: "Multiattack"
    desc: "The island uses Crush twice, targeting two different creatures it is grappling."
  - name: "Crush"
    desc: "Constitution Saving Throw: DC 17, one creature Grappled by the island. Failure: 40 (6d8 + 13) Bludgeoning damage. Success: Half damage."
legendary_actions:
  - name: ""
    desc: "The island can take 3 legendary actions, choosing from the options below, but only while its Adhesive Ground trait is active. Only one legendary action can be used at a time and only at the end of another creature's turn. The island regains spent legendary actions at the start of its turn."
  - name: "Draw Under"
    desc: "One creature Grappled by the island is pulled up to 15 feet toward the island's interior."
  - name: "The Ground Breathes"
    desc: "Each creature within 20 feet of a point the island can sense must succeed on a DC 17 Strength saving throw or have the Prone condition."
  - name: "Close the Throat (Costs 2 Actions)"
    desc: "The gap between the bay's rock arms narrows by 40 feet instead of 20 the next time the Heads Close lair action resolves, to the same 14-foot minimum. This doesn't stack with Wounded Resolve — once the island has dropped to 62 hit points or fewer, Heads Close already narrows by 40 feet, and this option has no further effect."
lair_actions:
  - desc: "On initiative count 20 (losing initiative ties), the island takes a lair action to cause one of the following effects. The island can't use the same effect two rounds in a row."
  - desc: "The Heads Close. The gap between the bay's rock arms, 240 feet (eighty yards) wide when the heads begin closing, narrows by 20 feet, to a minimum of 14 feet — the width held open by a dead ship's spine, wedged in the throat long before this crew arrived."
  - desc: "Warm Water Surges. The pool at the stream's source boils over in a rush of steam, heavily obscuring a 15-foot-radius area around it until initiative count 20 on the next round."
  - desc: "Fruit Falls. Every fruit-bearing tree on the island drops its fruit at once, in a sound like applause."
```

**Behavior states**

| State | Trigger | Behavior |
|---|---|---|
| **Patient** | The crew stays at the waterline, on the beach | Takes nothing at the waterline; offers a full generous day of water, fruit, and a flat bay before doing anything |
| **Adhesive Ground** | Anyone stands on the interior (past the treeline, at the stream's source, or up the slope for fruit) | Automatically Grapples everyone standing there at once (escape roll below) and narrows the 240-foot gap by 20 feet a round via its Heads Close lair action; taking fire damage frees every Grappled creature within 30 feet of the source |
| **Wounded Resolve** | Reduced to **62 HP** or fewer | Heads Close narrows the gap 40 feet a round instead of 20; at 0 HP it releases every Grappled creature and goes dormant to drift off and heal |

> [!check] Athletics or Acrobatics — Escaping Adhesive Ground
> DC 17; either skill, disadvantage on the check. Any creature Grappled by the island's Adhesive Ground may attempt this on its own turn.
> **Success:** the creature pulls free of the ground, ending the Grappled condition on itself.
> **Failure:** the ground holds. The creature stays Grappled.

**Wants:** crews should choose it as shelter, not search it as treasure. It feeds on whoever a full day inland lures in, but a wreck jams its own throat, so it can only bait, never simply close.
**Morale:** it never breaks, and nothing this crew carries can kill it. Hurt, it stops being patient. A burned grove or a broken headland speeds the bay shut, and it stops waiting for stragglers.

![[island-mimic-narration-narrator]]


## Description

A mimic that survived long enough to stop being a chest, then a chair, then anything a hand could lift, grown to island scale instead. Every chart of the Southern islands disagrees about where this one sits, and none of them puts a flag on it. The best landfall in the region carries no claim, and a becalmed crew holds both facts happily without connecting them. Sailors already know the standard mimic warning: check every chest, because it wants to look like treasure and it hates fire. None of that sounds like advice about an island, and nobody who needed it has ever come back to write one.

## Ecology

The whole island is one animal, old past reckoning. Soil has packed into the seams of its shell while roots thread through cracked plate, a beach grown scaled over the hide showing through. And it waits. It follows shipping traffic, drifting slowly enough that three separate charts can disagree about its position without any of them staying wrong for long. A crew gets a full generous day, and it takes nothing at the waterline. The cold stream, the fruit no bird has touched, the bay flat enough to careen in: each one baits a walk inland, where the stream runs warm and the fruit hangs better up the slope.

An island this size originated the doctrine every surviving mimic now runs on, centuries before anything small enough to pass for furniture carried it into a tavern: *stop being a chest.* Don't be the thing they come to take, because the thing they come to take gets searched and gets a sword swung at it. Be the thing they come to rest in. Treasure gets opened. Shelter gets *chosen*. It taught its own doctrine to at least one descendant small enough to pass for furniture. That one left, and has never gone back within sight of the coast (see [[Elder Mimic|the Elder Mimic]]).

One example sits in the Northern [[Midchain]], where it appeared between known islands in a channel that used to be open water: [[The Unplotted]].

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Walk past the treeline, toward the stream's source, or up the slope for fruit | Adhesive Ground hasn't triggered yet (the crew is still down at the waterline) | The ground grips everyone standing on the interior at once ([[Grappled]]; see the Escaping Adhesive Ground check under Stats & Combat), and the heads of the bay start grinding shut behind them | |
| Burn a grove near anyone the ground has already gripped | Adhesive Ground is live. Someone gets caught. | Fire frees every Grappled creature within 30 feet of the flames immediately, the one true thing sailors already know about mimics still working at this scale | [[Delmar Fisk]]'s habit of calling a wreck "salvage" before he lets himself call it a grave. This island hands him a bay full of both, and asks him to misname it twice before he understands what he is looking at. |
| Drive a ship into the closing gap, or use the bow-in wreck already wedged there | The heads of the bay are narrowing toward their floor | The dead ship's spine holds the throat open to a floor of 14 feet (the width it's held for nine years), the one door the island can't undo | The *[[Uncertainty]]*, the crew's own way out |

## Prepped Reveals

Bow-in wrecks fill the bay with hulls whole and decks empty of remains (four total). A ship that strikes a reef doesn't keep its masts, and these came in whole and stopped. Everything above the waterline on the beach is the lie, while the wrecks are honest. Time on the beach is free. It reacts the instant anyone steps onto the interior, whether that's an hour in or a full day. This crew can hurt the island, but nothing they carry can kill it. Lost limbs, burned groves, or broken headlands still leave it an island. Wounded, it stops being patient.

Calibrated for a party of five PCs, levels 5 to 10, two of whom already fly: [[Crissdalynn Khinriss|Crissdalynn]] innately at 45 feet, and [[Delmar Fisk|Delmar]] at 30 on the boots of flying, which run four hours on a charge. Party AC runs 16 to 18, HP 35 to 49, per `vault/campaigns/shattered-sea/pcs/*.md`. CR 12 as written, landed by averaging a defensive CR near 12 (raw HP 122, doubled to an effective 244 by immunity to nonmagical bludgeoning, piercing, and slashing plus poison) against an offensive CR near 12 (Multiattack Crush, roughly 80 average damage per round split across two Grappled targets). See `vault/refs/vault/monster/references/cr-tables.md` §1 and §6 for the benchmark. Treat the CR as a difficulty number: damage can't kill the island, but bringing it to 0 HP is the true measure of victory. At 0 HP the island lets go, all Grappled creatures go free, and dormancy takes hold. Both flying PCs escape the bay alone, but neither abandons the *[[Uncertainty]]*, so the ship becomes their anchor point and reason to stay. Winning means forcing the island to 0 HP (roughly twelve rounds at the base rate, six under Wounded Resolve) or shepherding the crew and ship through the closing gap. Burning the grove also buys time by slackening the throat long enough for escape.
