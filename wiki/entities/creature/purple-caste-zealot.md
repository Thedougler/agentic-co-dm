---
title: "Purple-Caste Zealot"
aliases:
  - Purple-Caste Zealot
category: entities
tags: [shattered-sea, creature]
sources:
  - "campaign-os:purple-caste-zealot.md"
created: 2026-09-13
updated: 2026-09-13
type: creature
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "A CR 3 purple-caste Grung zealot, a battle-draught frenzied escort that closes with Standing Leap before setting off powder charges lit from its own slow-match."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Purple-Caste Zealot

A CR 3 humanoid Grung, a battle-draught frenzied minion prepped as escort for lieutenants in the back half of the [[Calveno sewer magazine dungeon]]. It escorts [[ozzeth-the-twiceborn]] as part of the dungeon's mobile reserve, not tied to a specific room.

**Tactical Behavior:** it fights on a red-caste battle-draught called Toxin Frenzy, teeth clenched around a lit slow-match. A pair of crude iron powder-charges, Crown ordnance skimmed from the toxin trade, ride at its hip. Powder Charge and Powder Cook-Off both key off fire, not impact: a shove into standing water (this dungeon has plenty) neutralizes the explosive threat entirely without needing to fight through Toxin Frenzy's resistances. Standing Leap closes the gap on archers, flyers, and casters in a single bound.

**Related:**

- [[purple-caste-enforcer]]
- [[Grung|Grung (Green-Caste NPC)]]
- [[grung-elite-warrior]]
- [[grung-clans|Grung Clans (Faction)]]
- [[Calveno Sewer Magazines]]

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Purple-Caste Zealot"
size: Small
type: humanoid
subtype: grung
alignment: Lawful Evil
ac: 14
ac_note: unarmoured (toxin-hardened flesh)
hp: 45
hit_dice: 10d6 + 10
speed: "30 ft., Climb 30 ft."
stats: [16, 16, 13, 8, 11, 9]
saves:
  - strength: 5
  - constitution: 3
skillsaves:
  - athletics: 5
  - perception: 2
damage_immunities: "poison"
condition_immunities: "poisoned, frightened, charmed"
senses: "Passive Perception 12"
languages: "Grung"
cr: "3"
traits:
  - name: "Toxin Frenzy"
    desc: "The zealot is dosed on a red-caste battle-draught. While it has at least 1 hit point, it has resistance to bludgeoning, piercing, and slashing damage, and it is immune to the frightened and charmed conditions. Its melee attacks have advantage, and attack rolls against it have advantage. The draught is killing it, but not before this fight ends."
  - name: "Fuse and Powder"
    desc: "The zealot carries crude iron powder-charges — Crown ordnance skimmed from the toxin trade — and fights with a lit slow-match clenched in its teeth. Black powder ignites only from fire, never from impact or friction, so the burning match is the danger: while it burns, the zealot's charges are live. If the zealot is fully submerged or caught in an effect that douses it (a shove into the tide, a wave, create or control water), its match and powder are soaked: it can't use Powder Charge, and Powder Cook-Off does not trigger. It almost never gets the chance to re-light."
  - name: "Standing Leap"
    desc: "The zealot's long jump is 25 feet and its high jump is 15 feet, with or without a running start. It uses this to close on archers, flyers, and casters in a single bound."
actions:
  - name: "Multiattack"
    desc: "The zealot makes two Toxin-Wet Spear attacks."
  - name: "Toxin-Wet Spear"
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft. (or 10 ft. thrown, range 20/60), one target. Hit: 6 (1d6 + 3) piercing damage, and the target must succeed on a DC 12 Constitution saving throw or take 3 (1d6) poison damage and be poisoned until the start of its next turn."
  - name: "Powder Charge"
    desc: "The zealot touches its match to an iron powder-charge and hurls it at a point it can see within 20 feet (thrown, range 20/60). Each creature within 5 feet of that point must make a DC 13 Dexterity saving throw, taking 10 (3d6) fire damage on a failed save, or half as much on a success. The blast is Loud — heard up to 300 feet away, and it ends any concealment the zealot had. A zealot carries two charges; it cannot use this while its powder is soaked (see Fuse and Powder)."
reactions:
  - name: "Powder Cook-Off"
    desc: "When the zealot is reduced to 0 hit points, the lit slow-match falls into its remaining powder. Each creature within 5 feet of it must succeed on a DC 13 Dexterity saving throw or take 7 (2d6) fire damage. It fights to the death, and then a heartbeat past it. This does not trigger if the zealot's powder has been soaked."
```

## Description

A purple-caste Grung marked by the same deep-violet caste coloring worn by [[purple-caste-enforcer|Purple-Caste Enforcers]], but heavier-built and toxin-hardened past the point of needing armor. It fights with a lit slow-match clenched in its teeth and two crude iron powder-charges, Crown ordnance skimmed from the toxin trade, slung at its hip, and carries a spear built for both melee reach and a thrown follow-up. The red flush under its skin marks the battle-draught working through it; anyone who's seen a Grung on Toxin Frenzy before knows the fight ends when the draught does, one way or the other.

## Ecology

Zealots are Purple-Caste Grung dosed on a red-caste battle-draught and staged as escort muscle, not raised as their own line. They're war-footing conscripts drafted from within [[grung-clans|Grung Clans]] territory in the reef-fringed rainforest of the [[verdant-teeth]], the same stock that supplies [[purple-caste-enforcer|Purple-Caste Enforcers]] and [[grung-elite-warrior|Grung Elite Warriors]]. Like every Grung, it's amphibious and needs to submerge at least an hour a day or take on [[Exhaustion]], a dependency the [[Calveno sewer magazines]]'s flooded tunnels accommodate without effort. The same standing water that keeps a zealot healthy is what neutralizes its explosive threat if a fight turns against it.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Shove or dunk the zealot into standing water before it goes off | Its slow-match and powder charges are still lit and dry | Match and charges soak, killing Powder Charge and Powder Cook-Off outright. It's left fighting with only the Toxin-Wet Spear | [[Calveno Sewer Magazines]] |
| Have a [[Grung]]-speaking PC call out its caste debt mid-fight | Toxin Frenzy blocks the frightened and charmed conditions, not comprehension. The draught keeps it swinging, not deaf | It can't break off, but it snarls back who dosed it or which magazine comes online next, a bardic-inspiration-worthy beat instead of a wasted action | [[jean-claude-tabarnack]] |
