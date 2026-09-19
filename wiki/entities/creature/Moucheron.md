---
title: "Moucheron"
category: entities
tags: [shattered-sea, creature]
sources:
  - "campaign-os:moucheron.md"
created: 2026-09-13
updated: 2026-09-13
type: creature
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "CR 8 fey species native to Murrat; blood-economy mercenaries who hire out of Kalowe as the Five Blades."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Moucheron

![[moucheron-banner]]

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Moucheron"
size: Small
type: fey
alignment: Any
ac: 16
hp: 130
hit_dice: 20d6 + 60
speed: "30 ft., fly 60 ft."
stats: [12, 19, 17, 14, 14, 13]
saves:
  - dexterity: 7
  - constitution: 6
skillsaves:
  - acrobatics: 7
  - perception: 5
senses: "Darkvision 60 ft., Passive Perception 15"
languages: "Common, Sylvan"
cr: "8"
traits:
  - name: "Magic Resistance"
    desc: "Advantage on saving throws against spells and other magical effects."
  - name: "Sanguivore — Satiated"
    desc: "If the Moucheron hit with its Stinger last turn: no opportunity attacks against it, and AC becomes 17."
  - name: "Sanguivore — Voracious"
    desc: "If the Moucheron did not hit with its Stinger last turn: +1 bonus to all attack and damage rolls."
actions:
  - name: "Multiattack"
    desc: "Four Fey Blade attacks. Can replace one with a Stinger attack."
  - name: "Fey Blade"
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft. Hit: 14 (3d6+4) piercing damage."
  - name: "Stinger"
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft. Hit: 11 (2d6+4) piercing damage."
  - name: "Feeding Frenzy (2/Day, Bonus Action)"
    desc: "After hitting a Bloodied creature with Stinger, gain both Satiated and Voracious benefits simultaneously until the end of next turn."
```

**Behavior states**

| State | Trigger | Behavior |
|---|---|---|
| Satiated | Fed within the last day | Normal, sociable, professional; Sanguivore's Satiated trait active. |
| Hungry | One day unfed | Irritable, asks for a willing draw; Voracious active, Satiated lost. |
| Difficult | Two days unfed | Feeds on animals without asking. −2 to all Charisma checks. |
| Desperate | Three days unfed | Biology overrides contract, feeds on any available creature. Disadvantage on Wisdom saves, Advantage on attacks against bloodied creatures. |
| Starving | Four or more days unfed | Attacks to feed, taking 1d8 necrotic per day. Dies at 0 HP. |

**Wants:** a squad wants its next blood keep filled and its contract honored in full, since cash and a clean feed matter more to a Moucheron than the fight itself.
**Morale:** a squad breaks and disengages once two of its members drop, or the instant any one member crosses into Starving mid-fight. The clock outranks the contract.


## Description

Native to [[Murrat]] and the surrounding reef islands of the [[Midchain]], Moucherons are a fey species built around a blood economy. Villages sit built into cliff faces and canopy, each a separate kin-group running its own economic system where bloodletting is formal and consensual. It settles debts and pays for skilled work. The same exchanges seal agreements between kin-groups. The [[dravosi-crown]] classifies Moucherons alongside [[Rattkin]] under species bounty in Crown territories, but files them separately as hazardous wildlife removal at a higher rate.

## Ecology

Murrat itself is hostile to outsiders. Island Moucherons attack anything that lands. The ones who leave to work as mercenaries in the wider Midchain are the same creature, having simply discovered that fighting other people's wars pays better than hunting. Squads hire out of [[Kalowe]] in groups of three to six, collectively known as the [[five-blades]]. They are reliable. They don't break contracts or abandon clients under fire, and they state the feeding terms upfront. The caveat is the bloodless job: if a fight doesn't materialize, the feeding clause still stands, and a Moucheron's body runs on a strict clock, growing more irritable by the day unfed until, past three days, biology overrides any standing contract.

A Moucheron at Difficult or worse (two or more days unfed) will not lie about its state if asked directly. It treats the admission as a contractual disclosure, stated plainly for the record.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Offer it a willing blood draw | Any state past Satiated (Hungry or worse) | It resets to Satiated and treats the gift as a contractual disclosure it owes back (a favor or a discount on the next job) | [[five-blades]] |
| Threaten to report the blood economy to Crown bounty hunters | Any state | It breaks off talks and calls the threat a declared hostility, and its kin-group marks the crew of the [[Uncertainty]] | [[dravosi-crown]] |
| Corner it once it's gone three-plus days unfed | Desperate or Starving | Biology overrides any standing contract. It feeds on whoever's nearest, taking 1d8 necrotic itself for each further day denied | [[five-blades]] |

## Prepped Reveals

- A Moucheron at Difficult or worse won't lie about its state if asked directly. It treats the admission as contractual disclosure, stated plainly, and answers a direct question about its feeding clock the same way.
- The Five Blades carry two to three sealed clay keeps of preserved blood each, treated with stinger anticoagulant to keep two to three days. A Nature or Investigation check on their gear reveals a squad can go that long without a contract before hitting Hungry.

## Notable Individuals

[[Ket]] is a Moucheron, pigeon-sized, sentient, a starving humanoid mosquito, taken from Murrat as a specimen by [[barnaby-rook]] and freed aboard the [[Uncertainty|HCS Surety]] when its crew retook the ship. [[barnaby-rook|Rook]] was investigating a connection between the Moucheron and the [[five-blades]] when he took Ket as a specimen. The source establishes the Five Blades are Moucheron, not why [[barnaby-rook|Rook]] escalated from research to specimen capture.

The [[five-blades]] page documents its four Moucheron crew individually: [[Varet]], [[Toa]], [[Suke]], and [[Wirra]].
