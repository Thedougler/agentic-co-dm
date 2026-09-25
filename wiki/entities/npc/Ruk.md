---
title: Ruk
category: entities
tags: [shattered-sea, npc]
sources:
  - "Nona Black-Jaw"
  - "campaign-os:ruk.md"
summary: Bodyguard at Nona Black-Jaw's kitchen who has guarded Passage witnesses.
created: 2026-09-12T06:23:47Z
updated: 2026-09-13
type: npc
reveal: revealed
campaign: shattered-sea
status: alive
role: contact
location: Calveno
faction: Passage
visibility: dm
---

# Ruk

````col
```col-md
flexGrow=2
===
## At a Glance

| **Role**   | Contact; bodyguard |
| ---------- | ------------------ |
| **Nature** | Literal-minded [[lizardfolk]] and unshakeable guardian; impassive, observant, and not unkind. |
| **Home**   | [[Warren|The Warren]] and [[le-paludi]], especially Nona's kitchen and safe house |
| **Wants**  | To protect [[nona-black-jaw|Nona Black-Jaw]] with his body and presence. |
| **Leverage** | His literal nature means he cannot ignore lies or threats he observes; he states them plainly. |
| **Limit**  | He is bound to Nona through territory, loyalty, feeding rituals, and the protection of the young. |

> **DM thesis:** Ruk is Nona's physical shield: a patient sentinel who reads threats literally and answers them with his body.
```

```col-md
flexGrow=1
===
> [!narration] Ruk
> Dark olive-green scales with darker banding make Ruk large for a [[lizardfolk]], with a broad chest. Scars cover both forearms and the left side of his neck where the scales have grown back lighter and rough. He braces against the wall, both hands flat on the table in front of him, watching the doors.
```
````

## Running Ruk

````col
```col-md
flexGrow=1
===
### First meeting

Ruk stands watch with his back to the wall, both hands flat on the table, watching all doors. He speaks first.

> *Ruk*: “Who sent you?”
```

```col-md
flexGrow=1
===
### When posture changes

Ruk opens to direct statements, food offered before demands, and anyone who respects the safety of the young or the territory he guards. He closes when someone lies, threatens Nona or a protected person, or crosses him twice. He never ignores a lie or threat he observes.

He is currently guarding [[felix-aho]], a captured [[Grung]] prisoner, at the safe house. Ruk manages physical reads while [[enzo]] manages social ones. He is Nona Black-Jaw's bodyguard of twenty years and understands her through territory, loyalty, feeding rituals, and hatchling-defense.
```
````

### Voice

Ruk speaks in measured, flat, literal sentences with clear words. He cannot hide lies or threats and states what he observes plainly. At the table he reads the room while others see the people; Nona has used this skill for years. He gives food first, but after someone crosses him twice he stops being kind.

**The ask:** *“Who sent you?”*

**The refusal:** *“He is lying. I can smell the fear-sweat.”*

**Under pressure:** *“You threatened her. I heard you.”*

The voice-profile script remains the recording reference: [[voice-profile script]].

**Combat.**

```statblock
layout: Basic 5e Layout
name: Ruk
size: Medium
type: entity
subtype: lizardfolk
alignment: neutral
ac: 16
hp: 104
hit_dice: 16d8+48
speed: "30 ft., swim 30 ft."
stats: [20, 10, 18, 8, 14, 7]
saves:
  - strength: 8
  - constitution: 7
skillsaves:
  - perception: 5
  - athletics: 8
  - survival: 5
  - insight: 5
senses: "passive Perception 15"
languages: "Common, Draconic"
cr: 6
traits:
  - name: Hold Breath
    desc: "Ruk can hold his breath for 15 minutes."
  - name: Relentless Endurance
    desc: "Once per day, when Ruk is reduced to 0 HP but not killed outright, he drops to 1 HP instead."
  - name: Territorial Senses
    desc: "Ruk cannot be surprised while conscious. He has advantage on Wisdom (Insight) checks."
  - name: Wrestler
    desc: "Ruk has advantage on Strength (Athletics) checks to grapple or shove. He can make attacks against other creatures without releasing a creature he is grappling."
actions:
  - name: Multiattack
    desc: "Ruk makes three attacks: two with his greatclub and one bite."
  - name: Greatclub
    desc: "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage."
  - name: Bite
    desc: "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) piercing damage. On a hit, the target is grappled (escape DC 16). Ruk's attacks against a grappled creature have advantage."
bonus_actions:
  - name: Hungry Jaws
    desc: "Ruk makes one bite attack. On a hit, he regains hit points equal to the damage dealt. Once used, this trait cannot be used again until he finishes a short or long rest."
  - name: Pin Down
    desc: "While Ruk has a creature grappled, he forces it to make a DC 16 Strength saving throw. On a failure, the creature is also restrained until the start of Ruk's next turn."
```

CR 6 grappler. Ruk closes and locks a target down instead of trading blows at range: **wrestler** lets him restrain or shove without losing his other attacks, while **Bite** seizes on a hit. Every attack against that target then lands with advantage.

**Pin Down** restrains a creature he's already grappled. **Hungry Jaws** lets him bite for self-healing once per rest (useful when he's absorbing a hit meant for [[nona-black-jaw|Nona]]). **Territorial Senses** means he's never caught flat-footed, and **Relentless Endurance** gives him one free save to stay on his feet if knocked down outright.
## Connections

- [[nona-black-jaw]]: protects her with his body, understands her through territory, loyalty, feeding rituals, and hatchling-defense
- [[enzo]]: fellow bodyguard who manages social reads while Ruk manages physical ones
- [[perrin-black-jaw|Perrin]]: pushed him into a seat at Nona's safe house (Session 04)
- [[felix-aho]]: currently guarding him at the safe house, a captured Grung prisoner
- [[Warren|The Warren]]: home base
- [[le-paludi]]: district containing Nona's kitchen

**Session log.**

- **Session 06** (`vault/episodes/006/`): present at the Lothaludi fish market during [[il-gioco-delle-beffe]]. Pinned and tripped an attacker mid-prank.

- **Session 03** (`vault/episodes/003/`): stood near the door in Nona's kitchen in Le Paludi when Perrin arrived. Told the crying [[Rattkin]] mother "Don't worry. Nona will take care of it."

- **Session 04** (`vault/episodes/004/`): pushed Perrin into a seat when they arrived at Nona's safe house. Now guarding [[felix-aho]] (captured Grung prisoner) at the safe house.
