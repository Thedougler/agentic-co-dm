---
title: Enzo
category: entities
tags: [shattered-sea, npc]
sources:
  - "Nona Black-Jaw"
  - "campaign-os:enzo.md"
summary: Bodyguard at Nona Black-Jaw's kitchen safehouse who holds the door with Ruk.
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

# Enzo

*(This is not [[vincenzo-black-jaw]], coincidental name similarity only, distinct characters. W17 flag resolved, canon-review 2026-07-14.)*

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

*Polished enforcer in tailored silk, Nona Black-Jaw's personal bodyguard and the quietest threat in any room.*

**Wants:** to stay alert, catching every threat before it reaches Nona.

**Quote:** "Nona asked you a question."

> [!narration] Narration
> Black jaguar [[Tabaxi]], compact and solid, face composed and watchful. Ears alert to track the room. A long pale scar cuts from his left cheekbone down to his jaw, an old wound standing out against the obsidian of his fur. Dark tailored suit with collar buttoned tight, shoes mirror-polished to a shine. Claws filed and gleaming. He stands slightly behind and to Nona's right, weight on his back foot, one hand always free while the other passes bread and dried fish to whoever comes close, reading each face as it takes from him.

**Roleplay Concept:** polished mob enforcer + attentive bodyguard.

**Opening move:** flanking Nona as she passes bread and fish to the crew gathered at the crater's rim · Enzo speaks first · "You should take some. Long day ahead."

**Lore Sheet:** bodyguard to **Nona Black-Jaw**, working out of [[le-paludi]] and [[Warren|The Warren]]. Reads every guest for threats and intentions through micro-gestures and silence. Uses a lit cigar as a timer for Nona's patience. If it burns too low while she waits for an answer, he unsheathes one claw. More comfortable with violence than with people.

**Toy Chest**

| Field | Value |
|---|---|
| Primary goal | Keep Nona alive and aware, reading every guest for threats and lies. |
| Consistent method | Communicates through silence and small signals: tap of ash, weight shift, glance, or claw. |
| Active problem | The raid brought new faces to the [[Mercatura]] and new guards to the quays. One person cannot read everyone at once. |
| Performance hooks | Polished enforcer vibe. Taps his cigar ash against the table rim to mark conversation rhythm. |
| Link of relevance | Arranged safe passage and consolation for [[perrin-black-jaw]]'s surviving crew on Nona's order (Session 03). |

**Voice & Delivery:** never raises his voice, speaking with complete politeness regardless of message. "Nona asked you a question" lands as threat or favor depending on context. Holds doors and pulls chairs, reading crew like a banker reads a ledger while signaling to Nona with ash taps and weight shifts. Comfortable with violence, prefers it to talk.

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: Enzo
size: Medium
type: entity
subtype: tabaxi
alignment: neutral
ac: 16
hp: 78
hit_dice: 12d8+24
speed: "30 ft., climb 20 ft."
stats: [12, 20, 14, 14, 14, 15]
saves:
  - dexterity: 8
  - wisdom: 5
skillsaves:
  - perception: 5
  - stealth: 8
  - intimidation: 5
  - acrobatics: 8
senses: "darkvision 60 ft., passive Perception 15"
languages: "Common, Thieves' Cant"
cr: 5
traits:
  - name: Feline Agility
    desc: "Once before finishing a short or long rest, Enzo can double his speed until the end of his turn. He cannot use this trait again until he moves 0 feet on one of his turns."
  - name: Cat's Claws
    desc: "Enzo can use his claws to climb at 20 ft. They function as natural weapons."
  - name: Evasion
    desc: "When Enzo is subjected to an effect that allows a Dexterity saving throw for half damage, he takes no damage on a success and half damage on a failure."
actions:
  - name: Multiattack
    desc: "Enzo makes three attacks: two with his rapier and one with his claws."
  - name: Rapier
    desc: "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) piercing damage."
  - name: Claws
    desc: "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 8 (1d6 + 5) slashing damage."
  - name: Cut Clean
    desc: "Once per turn, when Enzo hits with his rapier and has advantage on the attack roll or an ally is within 5 ft. of the target, he deals an extra 10 (3d6) piercing damage."
bonus_actions:
  - name: Cunning Step
    desc: "Enzo takes the Dash, Disengage, or Hide action."
reactions:
  - name: Uncanny Dodge
    desc: "When an attacker Enzo can see hits him with an attack, he halves the attack's damage against him."
  - name: Interpose
    desc: "Replaces Uncanny Dodge. When a creature Enzo can see targets [[nona-black-jaw]] with an attack, Enzo moves up to his speed toward the attacker without provoking opportunity attacks, and that attack roll is made with disadvantage."
```

## Connections

- [[nona-black-jaw]], bodyguard, household
- [[Ruk]], fellow bodyguard
- [[le-paludi]], operates out of
- [[the-passage]] / [[the-black-jaw-run|Black-Jaw Run]], role tied to
- [[perrin-black-jaw]], present at Perrin's reunion with Nona; sent to arrange consolation for the *[[Vestra]]*'s crew and to call off attacks against him

## Session Log

**Session 06** (`vault/episodes/006/`). Present at the Lothaludi fish market during [[il-gioco-delle-beffe]]. He intercepted a chalk-powder attacker.

**Session 03** (`vault/episodes/003/`). Present in Nona's kitchen in [[le-paludi]] when Perrin arrived. He leaned against the far wall. After Nona met with the crew, she sent Enzo to arrange consolation for the *Vestra*'s surviving crew and call off the attacks she'd set against Perrin.

**Session 04** (`vault/episodes/004/`). Opened the door at Nona's safe house. He growled at the crew before letting them in.
