---
type: npc
status: canon
publish: false
aliases: []
created: 2026-07-30
updated: 2026-08-02
tags: [combat]
location: "[[warren|Warren]]"
campaigns: [Shattered Sea]
role: []
summary: "A Lizardfolk bodyguard utterly devoted to Nona Black-Jaw. His literal nature prevents deception; he observes threats and lies plainly. Reads the room while Enzo reads the people."
subtype: recurring
voice_actor: Nick
voice_id: ZylsQNbkURIoN0eXIVoB
voice: "Imposing male Lizardfolk bodyguard, middle-aged. Deep, dry, gravelly bass with a faint reptilian rasp. Speaks slowly, evenly, and literally (each word deliberate, flat, calm, always clear). Quietly devoted."
uid: 24cb182d-7378-4141-b29d-a5c7952859ba
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

Read while recording: [[dm-voice-script|voice-profile script]]

**Quote:** "He is lying. I can smell the fear-sweat."

> [!read-aloud]
> Dark olive-green scales with darker banding, large for a [[lizardfolk|Lizardfolk]] with a broad chest. Scars cover both forearms and the left side of his neck where the scales have grown back lighter and rough. He braces against the wall, both hands flat on the table in front of him, watching the doors.

**Roleplay Concept:** literal-minded [[lizardfolk|Lizardfolk]] + unshakeable guardian.

**Opening move:** standing watch · Ruk speaks first · "Who sent you?"

**Lore Sheet:** Ruk is Nona Black-Jaw's bodyguard for twenty years, bound to her through territory, loyalty, feeding rituals, and the protection of the young. His literal nature is his greatest asset: he cannot ignore lies or threats and speaks what he observes plainly. He is currently guarding [[felix-aho|Felix Aho]], a captured [[grung|Grung]] prisoner, at the safe house.

**Toy Chest**

| Field | Value |
|---|---|
| primary_goal | Protect Nona Black-Jaw with his body and presence. |
| consistent_method | Positions himself with his back to the wall, hands on the table, watching all doors. Never ignores a lie or a threat he observes. |
| active_problem | Guarding a captured [[grung\|Grung]] prisoner held at the safe house. |
| performance_hooks | Literal sentinel vibe. Rests at the wall with hands flat on the table, watching all doors. |
| link_of_relevance | Sworn guardian of [[nona-black-jaw\|Nona Black-Jaw]], bound to her through territory, loyalty, feeding rituals, and the defense of the young. |

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

**Pin Down** restrains a creature he's already grappled. **Hungry Jaws** lets him bite for self-healing once per rest (useful when he's absorbing a hit meant for [[nona-black-jaw|Nona]]). **Territorial Senses** means he's never caught flat-footed, and **Relentless Endurance** gives him one free save to stay on his feet if knocked down outright.

## Relationships

- [[nona-black-jaw|Nona Black-Jaw]]: protects her with his body, understands her through territory, loyalty, feeding rituals, and hatchling-defense
- [[enzo|Enzo]]: fellow bodyguard who manages social reads while Ruk manages physical ones
- [[perrin-black-jaw|Perrin]]: pushed him into a seat at Nona's safe house (Session 04)
- [[felix-aho|Felix Aho]]: currently guarding him at the safe house, a captured Grung prisoner
- [[warren|The Warren]]: home base
- [[le-paludi|Le Paludi]]: district containing Nona's kitchen

## Session Log

- **Session 06** (`vault/episodes/006/`): present at the Lothaludi fish market during [[il-gioco-delle-beffe|Il Gioco delle Beffe]]. Pinned and tripped an attacker mid-prank.

- **Session 03** (`vault/episodes/003/`): stood near the door in Nona's kitchen in Le Paludi when Perrin arrived. Told the crying [[rattkin|Rattkin]] mother "Don't worry. Nona will take care of it."

- **Session 04** (`vault/episodes/004/`): pushed Perrin into a seat when they arrived at Nona's safe house. Now guarding [[felix-aho|Felix Aho]] (captured Grung prisoner) at the safe house.
