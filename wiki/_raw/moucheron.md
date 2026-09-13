---
type: monster
status: canon
publish: false
title: ""
aliases: []
summary: "CR 8 fey species native to Murrat; blood-economy mercenaries who hire out of Kalowe as the Five Blades."
created: 2026-07-30
updated: 2026-08-09
tags: [combat]
tier: supporting
source: ""
source_url: ""
license: ""
found_at:
- "[[midchain-south|Midchain South]]"
- "[[midchain-west|Midchain West]]"
habitat: [Coastal, Forest]
statblock: inline
name: "Moucheron"
cr: 8
ac: 16
hp: 130
str: 12
dex: 19
con: 17
int: 14
wis: 14
cha: 13
campaigns: [Shattered Sea]
reference_image: "_assets/banners/moucheron-banner.webp"
uid: 906298e6-acc4-45d2-bb3c-d648e0ff54ac
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
| Difficult | Two days unfed | Feeds on animals without asking. −2 to all [[charisma\|Charisma]] checks. |
| Desperate | Three days unfed | Biology overrides contract, feeds on any available creature. [[disadvantage\|Disadvantage]] on [[wisdom\|Wisdom]] saves, [[advantage\|Advantage]] on attacks against bloodied creatures. |
| Starving | Four or more days unfed | Attacks to feed, taking 1d8 necrotic per day. Dies at 0 HP. |

**Wants:** a squad wants its next blood keep filled and its contract honored in full, since cash and a clean feed matter more to a Moucheron than the fight itself.
**Morale:** a squad breaks and disengages once two of its members drop, or the instant any one member crosses into Starving mid-fight. The clock outranks the contract.

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

## Description

Native to [[murrat|Murrat]] and the surrounding reef islands of the [[midchain|Midchain]], Moucherons are a fey species built around a blood economy. Villages sit built into cliff faces and canopy, each a separate kin-group running its own economic system where bloodletting is formal and consensual. It settles debts and pays for skilled work. The same exchanges seal agreements between kin-groups. The [[dravosi-crown|Dravosi Crown]] classifies Moucherons alongside [[rattkin|Rattkin]] under species bounty in Crown territories, but files them separately as hazardous wildlife removal at a higher rate.

## Ecology

Murrat itself is hostile to outsiders. Island Moucherons attack anything that lands. The ones who leave to work as mercenaries in the wider Midchain are the same creature, having simply discovered that fighting other people's wars pays better than hunting. Squads hire out of [[kalowe|Kalowe]] in groups of three to six, collectively known as the [[five-blades|Five Blades]]. They are reliable. They don't break contracts or abandon clients under fire, and they state the feeding terms upfront. The caveat is the bloodless job: if a fight doesn't materialize, the feeding clause still stands, and a Moucheron's body runs on a strict clock, growing more irritable by the day unfed until, past three days, biology overrides any standing contract.

A Moucheron at Difficult or worse (two or more days unfed) will not lie about its state if asked directly. It treats the admission as a contractual disclosure, stated plainly for the record.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Offer it a willing blood draw | Any state past Satiated (Hungry or worse) | It resets to Satiated and treats the gift as a contractual disclosure it owes back (a favor or a discount on the next job) | [[five-blades\|Five Blades]] |
| Threaten to report the blood economy to Crown bounty hunters | Any state | It breaks off talks and calls the threat a declared hostility, and its kin-group marks the crew of the [[uncertainty\|Uncertainty]] | [[dravosi-crown\|Dravosi Crown]] |
| Corner it once it's gone three-plus days unfed | Desperate or Starving | Biology overrides any standing contract. It feeds on whoever's nearest, taking 1d8 necrotic itself for each further day denied | [[five-blades\|Five Blades]] |

## Prepped Reveals

- A Moucheron at Difficult or worse won't lie about its state if asked directly. It treats the admission as contractual disclosure, stated plainly, and answers a direct question about its feeding clock the same way.
- The Five Blades carry two to three sealed clay keeps of preserved blood each, treated with stinger anticoagulant to keep two to three days. A Nature or Investigation check on their gear reveals a squad can go that long without a contract before hitting Hungry.

## Notable Individuals

[[ket|Ket]] is a Moucheron, pigeon-sized, sentient, a starving humanoid mosquito, taken from Murrat as a specimen by [[barnaby-rook|Barnaby Rook]] and freed aboard the [[uncertainty|HCS Surety]] when its crew retook the ship. [[barnaby-rook|Rook]] was investigating a connection between the Moucheron and the [[five-blades|Five Blades]] when he took Ket as a specimen. The source establishes the Five Blades are Moucheron, not why [[barnaby-rook|Rook]] escalated from research to specimen capture.

The [[five-blades|Five Blades]] page documents its four Moucheron crew individually: [[varet|Varet]], [[toa|Toa]], [[suke|Suke]], and [[wirra|Wirra]].
