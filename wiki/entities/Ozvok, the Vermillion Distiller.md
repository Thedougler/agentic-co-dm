---
title: "Ozvok, the Vermillion Distiller"
category: entities
tags: ["shattered-sea", "npc", "combat"]
sources:
  - "campaign-os:ozvok-the-vermillion-distiller.md"
created: 2026-09-13
updated: 2026-09-13
type: npc
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "A shelved Lawful Evil Grung alchemist-lieutenant (CR 5) held in reserve for the Calveno Sewer Magazines dungeon, whose Chemical Awakening at 90 HP or first melee hit shifts him from ranged toxin-th"
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Ozvok, the Vermillion Distiller

Ozvok is a small [[Grung]] who is Lawful Evil. He works as an alchemist and [[Grung]] officer. He throws acid, poison, and tar at enemies, then drinks elixirs to grow faster and more deadly in close combat. His Drunken Nonchalance makes him hard to scare. He gains advantage against charm and fear effects.

Ozvok joined the prep for the [[Calveno Sewer Magazines]] dungeon as a fourth lieutenant but got **shelved from the Session 06 lineup (2026-07-03)**. [[Ozzeth, the Twiceborn]] took his slot. This kept the three main lieutenants from feeling alike, since one is a drunk alchemist, one is a blind monk, and one is a mage-abomination. Ozvok would have been a second drunk alchemist like [[Bazzoth, the Steeped]]. He stays ready for future use. The tidal harbor fits his Amphibious trait, and his Legendary [[Action]] suite works well for solo or duo fights. He guards no room yet and has no placement.

Chemical Awakening triggers at no cost when he takes his first melee hit or drops to 90 hit points or fewer, whichever comes first. Players can't stop it. Bark Orders works with minions before the Awakening. After it triggers, he's fast enough to leave minions and strike the rear. Use the Legendary Action suite only for solo or duo fights. Skip it if he has three or more minions.

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: Ozvok, the Vermillion Distiller
size: Small
type: humanoid
subtype: grung
campaign: shattered-sea
alignment: lawful evil
ac: 14
ac_class: "natural armor (Phase 2: 17)"
hp: 130
hit_dice: 20d6 + 60
speed: "25 ft., climb 25 ft. (Phase 2: 40 ft., climb 40 ft.)"
stats: [10, 16, 16, 18, 12, 16]
saves:
  - dexterity: 6
  - constitution: 6
  - intelligence: 7
skillsaves:
  - nature: 7
  - perception: 4
  - intimidation: 6
damage_immunities: "poison"
condition_immunities: "poisoned"
senses: "passive Perception 14"
languages: "Grung, Common"
cr: 5
traits:
  - name: Poisonous Skin
    desc: "Any creature that grapples Ozvok or otherwise touches him, or hits him with a melee attack while within 5 feet, takes 5 (2d4) poison damage."
  - name: Standing Leap
    desc: "Ozvok's long jump is up to 25 feet and his high jump up to 15 feet, with or without a running start."
  - name: Amphibious
    desc: "Ozvok can breathe air and water."
  - name: Drunken Nonchalance
    desc: "Ozvok is too far gone to rattle. He has advantage on saving throws against being charmed or frightened."
actions:
  - name: Hurl Concoction
    desc: "Ozvok throws a bottle at a point he can see within 60 feet, where it bursts in a 15-foot radius. He chooses one concoction as he throws: Caustic Flask (DC 15 Dexterity save, 21 (6d6) acid damage on a failure or half on a success; the ground becomes difficult terrain until the end of Ozvok's next turn, dealing 5 (2d4) acid damage to a creature that starts its turn there); Reeking Draught (DC 15 Constitution save, 18 (4d8) poison damage on a failure or half on a success, poisoned until the end of its next turn on a failure); or Sticky Bomb (DC 15 Dexterity save, 10 (3d6) acid damage on a failure or half on a success, restrained by hardening tar on a failure — DC 15 Strength check as an action to break free)."
  - name: Sludge Bottle
    desc: "Ranged Weapon Attack: +6 to hit, range 30/90 ft., one target. Hit: 12 (2d8 + 3) poison damage."
  - name: "The Vintage (Recharge 5-6)"
    desc: "Ozvok uncorks his prize vial into a 20-foot-radius sphere centered on a point he can see within 60 feet. Each creature in the area makes a DC 15 Constitution saving throw, taking 35 (10d6) poison damage on a failure, or half as much on a success. A creature that fails is also poisoned until the end of its next turn. The area is lightly obscured and is difficult terrain until the end of Ozvok's next turn; a creature that starts its turn there takes 7 (2d6) poison damage."
bonus_actions:
  - name: Bark Orders
    desc: "Ozvok commands one ally he can see within 60 feet. That ally can immediately use its reaction to move up to its speed and make one weapon attack."
  - name: Swig
    desc: "Ozvok takes a long pull from his cask. He gains 7 temporary hit points and ends the frightened or poisoned condition on himself."
reactions:
  - name: Grease the Approach
    desc: "When a creature enters a space within 10 feet of Ozvok, he flicks a slick vial at its feet. The creature must succeed on a DC 15 Dexterity saving throw or fall prone, and its speed becomes 0 until the end of its turn."
  - name: "Vanishing Draught (1/Day)"
    desc: "When Ozvok is reduced to 45 hit points or fewer, or when he chooses to flee, he smashes a vial at his feet in a burst of red smoke, teleports up to 90 feet to an unoccupied space he can see, and is invisible until the end of his next turn."
legendary_actions:
  - name: Toss a Bottle
    desc: "Ozvok makes one Sludge Bottle attack."
  - name: Rally
    desc: "Ozvok uses Bark Orders."
  - name: "Caustic Leap (Costs 2 Actions)"
    desc: "Ozvok moves up to his speed without provoking opportunity attacks. Each creature within 5 feet of where he lands makes a DC 15 Dexterity saving throw, taking 10 (3d6) acid damage on a failure, or half as much on a success."
```

**Chemical Awakening (Phase 2).** The first time Ozvok takes melee damage, or the first time he drops to 90 hit points or fewer, whichever is first, he uses his reaction. He gulps back a handful of elixirs and shifts into a faster, deadlier phase.

If he has no reaction left, this happens at the start of his next turn instead. Either way, it doesn't change initiative order.

His AC becomes 17, his speed becomes 40 ft./climb 40 ft., and he gains 22 temporary hit points. He can Dash or Disengage as a bonus action.

He gains Multiattack (two Toxin-Slick Blade attacks, or swap both for one Hurl Concoction), Toxin-Slick Blade (*Melee [[Weapon Attack]]:* +7 to hit, reach 5 ft., one target. *Hit:* 9 (2d4 + 4) piercing and 7 (2d6) poison), and Chemical Leap as a bonus action (jumps to 30 feet without making opportunity attacks provoked, then one Toxin-Slick Blade strike on a creature within 5 feet of landing). All changes last the rest of the encounter.

**Legendary Actions (Optional).** Use this suite only if running Ozvok solo or with few minions. Drop it entirely if he has three or more minions. Ozvok can take 2 legendary actions from the options above, using one at a time and only at the end of another creature's turn. He regains spent legendary actions at the start of his turn.

## Relationships

- [[Vashu the Weeping Veil|Vashu, the Weeping Veil]] (fellow prepped guardian for [[Calveno Sewer Magazines]])
- [[Bazzoth, the Steeped]] (fellow drunk-alchemist archetype; Ozvok lost the slot to him)
- [[Ozzeth, the Twiceborn]] (took the Delta/T2 slot Ozvok would have filled)
- [[Grung Elite Warrior]] (generic Grung combat statline referenced alongside him)
- [[Grung clans|Grung Clans]] (faction)
- Calveno Sewer Magazines (dungeon they prepped him for, then shelved)
- [[Simone Tabarnack]] (related figure named in source)
