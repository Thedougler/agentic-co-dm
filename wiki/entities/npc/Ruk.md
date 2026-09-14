---
title: Ruk
category: entities
tags: [shattered-sea, npc]
sources:
  - "Nona Black-Jaw"
  - "campaign-os:ruk.md"
summary: Bodyguard at Nona Black-Jaw's kitchen who has guarded Passage witnesses.
lifecycle: canon
created: 2026-09-12T06:23:47Z
updated: 2026-09-13
type: npc
reveal: unrevealed
campaign: shattered-sea
status: alive
role: contact
location: Calveno
faction: Passage
visibility: dm
---

# Ruk

*A Lizardfolk bodyguard utterly devoted to protecting Nona Black-Jaw, whose literal nature and impassive presence make him her most reliable shield.*

```meta-bind-button
label: ⏺ Record Voice Profile
style: primary
action:
  type: command
  command: obsidian-shellcommands:shell-command-voiceprstart
```

```meta-bind-button
label: ⏹ Stop
style: destructive
action:
  type: command
  command: obsidian-shellcommands:shell-command-voiceprstop0
```

```meta-bind-button
label: ✔ Save Voice Profile
style: default
action:
  type: command
  command: obsidian-shellcommands:shell-command-voiceprsave0
```

Read while recording: [[voice-profile script]]

**Quote:** "He is lying. I can smell the fear-sweat."

> [!narration] Narration
> Dark olive-green scales with darker banding, large for a [[Lizardfolk]] with a broad chest. Scars cover both forearms and the left side of his neck where the scales have grown back lighter and rough. He braces against the wall, both hands flat on the table in front of him, watching the doors.

**Roleplay Concept:** literal-minded [[Lizardfolk]] + unshakeable guardian.

**Opening move:** standing watch · Ruk speaks first · "Who sent you?"

**Lore Sheet:** Ruk is Nona Black-Jaw's bodyguard for twenty years, bound to her through territory, loyalty, feeding rituals, and the protection of the young. His literal nature is his greatest asset: he cannot ignore lies or threats and speaks what he observes plainly. He is currently guarding [[Felix Aho]], a captured [[Grung]] prisoner, at the safe house.

**Toy Chest**

| Field | Value |
|---|---|
| Primary goal | Protect Nona Black-Jaw with his body and presence. |
| Consistent method | Positions himself with his back to the wall, hands on the table, watching all doors. Never ignores a lie or a threat he observes. |
| Active problem | Guarding a captured [[Grung]] prisoner held at the safe house. |
| Performance hooks | Literal sentinel vibe. Rests at the wall with hands flat on the table, watching all doors. |
| Link of relevance | Sworn guardian of [[Nona Black-Jaw]], bound to her through territory, loyalty, feeding rituals, and the defense of the young. |

**Voice & Delivery:** measured, flat, literal speech with clear words. He cannot hide lies or threats and states them plain. Not unkind, yet he'll give food first. Cross him twice and he stops being kind. At the table he reads the room while others see the people. Nona has used this skill for years.

## Stats & Combat

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

**Pin Down** restrains a creature he's already grappled. **Hungry Jaws** lets him bite for self-healing once per rest (useful when he's absorbing a hit meant for [[Nona Black-Jaw|Nona]]). **Territorial Senses** means he's never caught flat-footed, and **Relentless Endurance** gives him one free save to stay on his feet if knocked down outright.

## Connections

- [[Nona Black-Jaw]]: protects her with his body, understands her through territory, loyalty, feeding rituals, and hatchling-defense
- [[Enzo]]: fellow bodyguard who manages social reads while Ruk manages physical ones
- [[Perrin Black-Jaw|Perrin]]: pushed him into a seat at Nona's safe house (Session 04)
- [[Felix Aho]]: currently guarding him at the safe house, a captured Grung prisoner
- [[Warren|The Warren]]: home base
- [[Le Paludi]]: district containing Nona's kitchen

## Session Log

- **Session 06** (`vault/episodes/006/`): present at the Lothaludi fish market during [[Il Gioco delle Beffe]]. Pinned and tripped an attacker mid-prank.

- **Session 03** (`vault/episodes/003/`): stood near the door in Nona's kitchen in Le Paludi when Perrin arrived. Told the crying [[Rattkin]] mother "Don't worry. Nona will take care of it."

- **Session 04** (`vault/episodes/004/`): pushed Perrin into a seat when they arrived at Nona's safe house. Now guarding [[Felix Aho]] (captured Grung prisoner) at the safe house.
