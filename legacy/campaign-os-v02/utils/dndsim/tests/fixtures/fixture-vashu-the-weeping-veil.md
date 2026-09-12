---
type: npc
status: canon
publish: false
aliases: [Vashu, "The Weeping Veil"]
created: legacy
updated: legacy
tags: [grung, combat]
location: "[[calveno-sewers-grung-magazines]]"
campaigns: [Shattered Sea]
role: []
---

# Vashu, the Weeping Veil

Not yet encountered — pre-staged for the reveal, per `status: pending`.

> [!read-aloud] She's small even by grung standards, lean and coiled, purple hide banded in black at the wrists, ankles, and throat, with a scatter of black spots across her shoulders. Her eyes are solid white, blind. A strip of grey rag hangs from her scalp over one shoulder, over plain monastic wraps. Her tongue clicks against her teeth, steady, without pause, whether she's standing still or crossing the room.

An older female purple-caste grung — lean and sinewy with age, deep-purple hide banded in black at the wrists, ankles, and throat, with a scatter of black spots across her shoulders and back (poison-dart-frog aposematism, not warpaint or rank marking); blind eyes gone fully blank milk-white; a tattered grey rag veil draped over her head and simple monastic wraps.

> [!CAUTION]
> Vashu is a senior master of the Still-Water Discipline, a purple-caste martial tradition built on patience, venom, and reading an opponent by touch and vibration instead of sight. Adepts train blind by choice and cover their eyes once they've mastered the discipline's core forms — the veil marks that milestone, not an injury or a punishment. "Weeping Veil" is her order name, not a birth name: masters take a title tied to their signature technique, and hers is the toxic mist she weeps from a bone vial (Weeping Veil, the bonus action).

The tongue-click reads as a nervous compulsion — it isn't. It's active echolocation, the working half of Blind Discipline. It never stops, and it sharpens — faster, tighter — right before she strikes or moves to intercept. A PC who's spent real time around an echolocating creature (bat, dolphin, similar) can read that tell with a passive Perception/Insight check the DM sets on the spot; everyone else just hears a habit.

Guards **Room T1 (Magazine Gamma)** of the [[calveno-sewers-grung-magazines|Calveno Sewer Magazines]] dungeon, with 1 [[vault/shattered-sea/monsters/purple-caste-enforcer|Purple-Caste Enforcer]] escort (source note: "assigned 2026-07-01 — party had reached Room 6/Ruma and neutralized Room 4/Magazine Alpha" — an in-source DM planning note, not a corroborated play event; no session file confirms it).

Blind Discipline defeats invisibility, darkness, and obscurement-based tactics within 40 ft — including her own Weeping Veil. Fits the low 5-ft ceiling and cramped footprint of T1 especially well: blindsight covers the whole room regardless of light or fog. Evasion plus Still-Water Deflection make her resilient against ranged and AoE parties. Slippery Grip makes her difficult to grapple or pin down; Tongue Lash lets her drag scattered targets back into reach; Pressure Point sits on her legendary actions, pressuring the party between other creatures' turns instead of competing with Multiattack on her own.

## Stats & Combat

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
source: "Homebrew"
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

## Relationships

Wikilinks withheld for entities without a landed page yet — see ingest queue `## Flags`.

- [[vault/shattered-sea/monsters/purple-caste-enforcer|Purple-Caste Enforcer]] — assigned escort, Room T1/Magazine Gamma
- [[bazzoth-the-steeped|Bazzoth, the Steeped]] — fellow guardian, Room 5/Magazine Beta
- [[vault/shattered-sea/npcs/ozvok-the-vermillion-distiller|Ozvok, the Vermillion Distiller]] — related grung alchemist figure
- [[ozzeth-the-twiceborn|Ozzeth, the Twiceborn]] — fellow guardian, Room T2/Magazine Delta
- [[grung-elite-warrior|Grung Elite Warrior]] — generic grung combat statline referenced alongside her
- [[grung-clans|Grung Clans]] — faction
- [[calveno-sewers-grung-magazines|Calveno Sewer Magazines]] — guards Room T1/Magazine Gamma of this dungeon
- [[simone-tabarnack|Simone Tabarnack]] — related figure named in source

## Session Log

None. Not yet encountered — sessions 05/06 have no play records corroborating the source's own "party reached Room 6" note; canon evidence for the dungeon ends at session 04, which discovers the plot but does not reach Room 4/T1. `status: pending` accordingly.
