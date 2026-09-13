---
title: Vashu the Weeping Veil
category: entities
tags: [shattered-sea, npc]
sources:
  - "wiki/_raw/Grung clans.md"
  - "campaign-os:vashu-the-weeping-veil.md"
summary: Named Grung face called Vashu the Weeping Veil, with color and current role unestablished here.
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.37
lifecycle: proposed
lifecycle_changed: "2026-09-12"
tier: supporting
created: 2026-09-12T00:00:00Z
updated: 2026-09-13
type: npc
reveal: unrevealed
campaign: shattered-sea
visibility: dm
relationships:
  - target: "[[Grung clans]]"
    type: related_to
  - target: "[[Calven and Calveno]]"
    type: related_to
---

# Vashu the Weeping Veil

> [!narration] Narration She's small even by Grung standards, lean and coiled, purple hide banded in black at the wrists, ankles, and throat, with a scatter of black spots across her shoulders. Her eyes are solid white, blind. A strip of grey rag hangs from her scalp over one shoulder, over plain monastic wraps. Her tongue clicks against her teeth, steady, without pause, whether she's standing still or crossing the room.

An older female purple-caste [[Grung]]. Lean and sinewy. Deep-purple hide with black bands at wrists, ankles, and throat. Black spots dot her shoulders and back (poison-dart-frog coloring). Blank milk-white eyes. Blind. She wears a tattered grey veil and simple robes.

She guards **Room T1 (Magazine Gamma)** in the [[Calveno Sewer Magazines]]. A [[Purple-Caste Enforcer]] accompanies her.

(Source note: assigned 2026-07-01. DM planning note, not a confirmed play event.)

## The Order

Vashu leads the Still-Water Discipline. This purple-caste order teaches patience, venom, and touch. They learn to fight blind. After mastery, they cover their eyes. The veil is their achievement.

"Weeping Veil" is an order title for a master's special move. For Vashu, it means the toxic mist she releases. She keeps it in a bone vial. The mist is both her title and her bonus action in combat.

Her constant tongue-click sounds nervous to outsiders. It's actually echolocation. She bounces sound waves off objects to see. The sound never stops but sharpens before she strikes. A PC who knows echolocating creatures (like bats) might see the tell with a [[passive Perception]] check. Others just hear a tic.

## Stats & Combat

Winded combat state (Session 06, Scene 4): [[vashu-the-weeping-veil (Winded)|Vashu, the Weeping Veil (Winded)]].

```statblock
layout: Basic 5e Layout
name: Vashu, the Weeping Veil
size: Small
type: humanoid
subtype: grung
alignment: lawful evil
ac: "20 (unarmored, perfected Still-Water Discipline)"
hp: 165
hit_dice: "22d6 + 88"
speed: "30 ft., climb 30 ft."
stats: [14, 20, 18, 11, 20, 13]
saves:
  - Dex: +8
  - Con: +7
  - Wis: +8
skillsaves:
  - Acrobatics: +8
  - Athletics: +5
  - Insight: +8
  - Perception: +8
  - Stealth: +8
damage_immunities: "poison"
condition_immunities: "blinded, poisoned"
senses: "blindsight 40 ft. (blind beyond this radius), passive Perception 18"
languages: "Grung"
cr: 8
traits:
  - name: Blind Discipline
    desc: "Vashu can't use sight and is unaffected by anything that relies on seeing her or on obscured vision. A constant, rapid tongue-click lets her perceive everything within 40 feet by echo, vibration, and scent, ignoring darkness, fog, invisibility, and her own Weeping Veil. An attacker Vashu can perceive gains no benefit from being unseen."
  - name: Standing Leap
    desc: "Vashu's long jump is 30 feet and her high jump is 20 feet, with or without a running start."
  - name: Evasion
    desc: "When Vashu is subjected to an effect that allows a Dexterity saving throw for half damage, she instead takes no damage on a success and half on a failure."
  - name: "Slippery Grip (3/Day)"
    desc: "Vashu has advantage on ability checks and saving throws to avoid or escape being grappled or restrained. In addition, if she fails a saving throw, or a creature attempts to grapple or restrain her, she can choose to succeed on the save instead, or cause the grapple/restrain attempt to automatically fail — she must decide before knowing whether the roll would have succeeded."
  - name: Venom-Wet Strikes
    desc: "A creature that hits Vashu with a melee attack while within 5 feet of her, or that grapples her, must succeed on a DC 16 Constitution saving throw or be poisoned until the start of its next turn."
actions:
  - name: Multiattack
    desc: "Vashu makes three Still-Water Strike attacks."
  - name: Still-Water Strike
    desc: "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage. If the target is poisoned, it also takes 9 (2d8) poison damage."
bonus_actions:
  - name: Tongue Lash
    desc: "Vashu lashes her tongue at one creature she can perceive within 20 feet. Ranged Weapon Attack: +8 to hit. Hit: 5 (1d4 + 3) bludgeoning damage, and Vashu pulls the target up to 15 feet toward her, to an unoccupied space, ending the pull early if it would put the target in danger (e.g. a fall, hazard, or lava). No effect on a target two or more size categories larger than Vashu."
  - name: "Weeping Veil (Recharge 5–6)"
    desc: "Vashu shatters a bone vial, releasing a bitter mist in a 25-foot-radius sphere centered on herself. The area is heavily obscured until the start of her next turn. Each creature that starts its turn in the area, or enters it for the first time on a turn, must succeed on a DC 16 Constitution saving throw or be blinded and poisoned until the end of that turn. Vashu is unaffected. She carries 4 vials."
  - name: Step of the Tide
    desc: "Vashu takes the Dash or Disengage action."
reactions:
  - name: Still-Water Deflection
    desc: "When Vashu or an ally within 10 feet of her is hit by a ranged attack Vashu can perceive, she reduces the damage to that target by 15 (2d10 + 4). If this reduces the damage taken by Vashu herself to 0, she can redirect the missile at a creature she can perceive within 30 feet: +8 to hit, 12 (2d10 + 1) damage of the triggering attack's type."
legendary_actions:
  - name: "Legendary Actions"
    desc: "Vashu can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. Vashu regains spent legendary actions at the start of her turn."
  - name: Reposition
    desc: "Vashu moves up to half her speed without provoking opportunity attacks."
  - name: Still-Water Strike (Costs 1 Action)
    desc: "Vashu makes one Still-Water Strike attack."
  - name: "Pressure Point (Costs 2 Actions, Recharge 5–6)"
    desc: "Vashu strikes a nerve cluster on one creature she can perceive within 5 feet. The target must make a DC 16 Constitution saving throw. On a failure, it is stunned until the end of Vashu's next turn. On a success, its speed is halved and it is poisoned until the end of its next turn."
```

Her Blind Discipline works within 40 feet. It defeats invisibility, darkness, fog, and even her own Weeping Veil. Room T1 is small and low-ceilinged, so her blindsight covers the whole space.

Evasion shields her from ranged attacks. Still-Water Deflection blocks area hits. Slippery Grip makes her hard to hold. Tongue Lash pulls foes toward her. Pressure Point is a legendary action that lets her threaten her foes between their turns.

## Relationships

- [[Purple-Caste Enforcer]]: assigned escort, Room T1/Magazine Gamma
- [[Bazzoth, the Steeped]]: fellow guardian, Room 5/Magazine Beta
- [[Ozvok, the Vermillion Distiller]]: related [[Grung]] alchemist figure
- [[Ozzeth, the Twiceborn]]: fellow guardian, Room T2/Magazine Delta
- [[Grung Elite Warrior]]: generic [[Grung]] combat statline referenced alongside her
- [[Grung clans|Grung Clans]]: faction
- [[Calveno Sewer Magazines]]: guards Room T1/Magazine Gamma of this dungeon
- [[Simone Tabarnack]]: related figure named in source

## Session Log

**Session 06** (`vault/episodes/006/`): the blind one found herself in the Primary Chamber defending [[Solange Barret|Solange]]'s ritual circle. She fought [[Crissdalynn Khinriss|Crissdalynn]] in direct combat, landing Full Order Strike twice (11 and 10 bludgeoning) and using Tongue Lash at range, but despite her Evasion deflecting a [[Catarina Da'Virelli|Catarina]]/Delmar area hit, Crissdalynn's melee attack killed her ("Dead. Dead. I cracked the throat.").
