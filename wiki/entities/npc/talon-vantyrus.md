---
title: Talon Vantyrus
aliases:
  - Vantyrus
category: entities
tags: [shattered-sea, npc]
sources:
  - "Talon Skarn"
  - "campaign-os:talon-vantyrus.md"
  - "campaign-os:osset.md"
  - "Talon Vantyrus update (2026-09-23)"
summary: "Countless master and former Sentinel who now uses Talon Vantyrus as an alias; his original name is [[Osset]], and his apprentice [[talon-skarn]] is trying to kill him under the Rule of Two."
provenance:
  extracted: 0.93
  inferred: 0.07
  ambiguous: 0.0
base_confidence: 0.50
lifecycle: canon
created: 2026-09-12T06:23:47Z
updated: 2026-09-23
type: npc
reveal: unrevealed
campaign: shattered-sea
status: alive
role: rival
location: unknown
faction: Countless
visibility: dm
---
# Talon Vantyrus

![[talon-vantyrus-overview.png|Talon Vantyrus overview: the stillness of the Countless master]]
![[talon-vantyrus-banner.png|Talon Vantyrus, master of the Countless]]

````col
```col-md
flexGrow=2
===
## At a Glance

| **Role** | Rival and master of [[countless|the Countless]] |
| --- | --- |
| **Nature** | Aged snowy-owl aarakocra, once a senior master of the [[high-eyrie|High Eyrie]] and teacher of [[master-kyzil]] |
| **Home** | Unknown; he moves along the Countless's Midchain routes |
| **Wants** | The [[soul-incarnate|Soul Incarnate]]'s transformation technique, and the crack he means to use is [[crissdalynn-khinriss]]'s own unexplained gift |

**Identity.** [[Osset]] is his original name. He now goes by Talon Vantyrus as leader of [[Countless|the Countless]], and **Talon** is a title his agents share.

> **DM thesis:** Vantyrus treats every death he could have foreseen as a death he permitted, so he has stopped recording and started intervening, and the party only ever meets the intervention.
```
```col-md
flexGrow=1
===
> [!narration] Talon Vantyrus
> Feathers the color of old snow cover him shoulder to talon, bled past white by age and altitude both, with black mottling breaking the pale field across his brow and wing coverts. Cold air off the heights clings to him, carrying a faint tang of frost. His eyes are yellow-gold and he watches without blinking. His robes keep the layered construction of Sentinel martial dress and have been stripped of every identifying mark, and a thin blade hangs balanced at his hip beside the crystal top he turns while he thinks. When he finally moves, it costs him nothing, one wing folding tighter to his back, the only warning a lesser argument gets before he ends it.
```
````

## Running Talon Vantyrus

````col
```col-md
flexGrow=1
===
### First meeting

Vantyrus arrives as Talon Vantyrus, master of the Countless, and opens on the work in front of them rather than on himself. He keeps his original name out of the room entirely, not hiding it so much as never offering it. If someone says the name Osset aloud, he stops deciding whether to answer and starts deciding whether to stay.

* "You may sit. You already know what I am asking, or you would not be here."
```
```col-md
flexGrow=1
===
### When posture changes

A plea that stops immediate harm can move him, and so can an argument that accepts the cost of acting. An appeal to patience, procedure, tradition, or doctrine instead of action ends the conversation, and he repeats a demand only when he has already decided the answer.

He will not name himself, describe [[talon-skarn]]'s real standing in the order, or explain how he means to reach [[crissdalynn-khinriss]]. A conversation that turns into an interrogation is one he leaves.
```
````

### Voice

Composed, quiet, and precise. He never raises his voice and rarely repeats himself, and he speaks like a teacher who expects the student to eventually understand.

He does not describe his foresight as destiny. His vocabulary is *avoidable*, *preventable*, *consequence*, *probability*, *intervention*, and *waste*, and he despises any claim that something "had to happen."

* "Nothing had to happen. Something happened, and afterward you invented inevitability so you could survive having done nothing."
* "You mistake stillness for mercy. It has never been mercy."
* "You crossed an ocean because watching was not enough. Do not pretend we disagree about intervention."
* "Tell me the difference between a preventable death and a permitted one."
* "Your heel."

**Doctrine.** Vantyrus broke from the [[sentinels-of-the-eyrie]] because the order **recorded deaths without preventing them**. The [[high-eyrie|Eyrie]] records time, weather, position, water, occurrence, and loss, and its discipline demands observation without interference. Vantyrus came to regard that restraint as complicity, and his answer became the [[Countless]].

| Order | Practice |
| --- | --- |
| [[sentinels-of-the-eyrie]] | Complete record, no action. |
| [[Countless]] | Complete action, no record. |

Countless erases names, passes orders through intermediaries, and hands hired blades one task each, so losses disappear from the ledger. Vantyrus believes knowledge creates responsibility and states the principle without softening it: "If you knew enough to record the death, you knew enough to try."

His corruption lies in how far he carries that principle. Given enough foresight, every choice becomes something to optimize. Chance becomes negligence. Freedom becomes another variable capable of producing unacceptable outcomes.

**Combat.** Vantyrus's build is [[master-kyzil]]'s disciplined Kensei form carried toward prediction, interruption, and control, and the two share that lineage from before their break. His win condition is a decision he can make for the party, not a body count, and he withdraws rather than stands when the exchange turns against him.

![[talon-vantyrus-reference.png|Talon Vantyrus reference sheet: turnaround, costume detail, and expression study]]

```statblock
layout: Basic 5e Layout
dice: true
columns: 2
forceColumns: true
name: Talon Vantyrus
size: Medium
type: humanoid
subtype: aarakocra
alignment: lawful neutral
ac: 22
hp: 238
hit_dice: "28d8 + 112"
speed: "50 ft., fly 80 ft."
stats: [10, 22, 18, 20, 20, 16]
saves:
  - Dex: +12
  - Con: +10
  - Int: +11
  - Wis: +11
skillsaves:
  - Acrobatics: +12
  - Insight: +11
  - Perception: +11
  - Stealth: +12
senses: "passive Perception 21"
languages: "Common, Auran"
cr: 17
traits:
  - name: Evasion
    desc: "When Vantyrus is subjected to an effect that allows him to make a Dexterity saving throw to take only half damage, he instead takes no damage on a successful save and half damage on a failed save."
  - name: Legendary Resistance (3/Day)
    desc: "If Vantyrus fails a saving throw, he can choose to succeed instead."
  - name: Long Sight
    desc: "Vantyrus has advantage on Initiative rolls and can't be surprised while conscious."
  - name: Winter's Stillness
    desc: "While Vantyrus hasn't moved since the end of his last turn, attack rolls against him have disadvantage."
  - name: Fatespinner
    desc: "When Initiative is rolled, Vantyrus rolls three d20s and records the results. Before Vantyrus or a creature he can see within 120 feet makes a D20 Test, Vantyrus can replace the roll with one of the recorded results. He can do so only once per turn, and each recorded result can be used only once."
actions:
  - name: Multiattack
    desc: "Vantyrus makes three Frostglass Blade attacks."
  - name: Frostglass Blade
    desc: "Melee or Ranged Attack Roll: +12 to hit, reach 5 ft. or range 60/120 ft., one target. Hit: 12 (1d12 + 6) slashing damage plus 9 (2d8) force damage. Immediately after a ranged attack, the blade returns to Vantyrus's hand."
  - name: Five Futures Cut (Recharge 5-6)
    desc: "Vantyrus chooses up to five creatures he can see within 60 feet. Each target must make a DC 20 Dexterity saving throw, taking 33 (6d10) force damage on a failed save or half as much damage on a successful one. Vantyrus then teleports to an unoccupied space he can see within 5 feet of one target."
  - name: Binding Grasp
    desc: "One Large or smaller creature Vantyrus can see within 30 feet must succeed on a DC 20 Strength saving throw or be Restrained until the end of Vantyrus's next turn. While Restrained this way, its Speed is 0 as intersecting threads of possible movement collapse around it."
bonus_actions:
  - name: Between Wingbeats
    desc: "Vantyrus takes the Dash or Disengage action."
  - name: Unchosen Step (3/Day)
    desc: "Vantyrus teleports up to 40 feet to an unoccupied space he can see."
reactions:
  - name: Absent Feather
    desc: "Trigger: Vantyrus is hit by an attack roll. Response: Vantyrus gains a +5 bonus to AC against that attack, potentially causing it to miss. If the attack misses, Vantyrus can move up to 10 feet without provoking Opportunity Attacks."
  - name: Sever the Gesture
    desc: "Trigger: A creature Vantyrus can see within 60 feet casts a spell with Verbal or Somatic components. Response: The caster must succeed on a DC 20 Constitution saving throw or the spell fails and has no effect."
legendary_actions:
  - name: ""
    desc: "Legendary Action Uses: 3. Immediately after another creature's turn, Vantyrus can expend one use to take one of the following actions. He regains all expended uses at the start of his turn."
  - name: Flowing Step
    desc: "Vantyrus moves up to half his Speed without provoking Opportunity Attacks."
  - name: Frostglass Blade
    desc: "Vantyrus makes one Frostglass Blade attack."
  - name: Collapse the Thread (Costs 2 Actions)
    desc: "One creature Vantyrus can see within 60 feet must make a DC 20 Wisdom saving throw. On a failed save, it takes 18 (4d8) psychic damage, can't take Reactions, and has disadvantage on the next D20 Test it makes before the end of its next turn. On a successful save, it takes half as much damage only."
```

> [!mechanic] Running the fight
> Vantyrus should feel like he is **interrupting decisions rather than absorbing attacks**, and he should rarely stand and trade damage. Roll his three **Fatespinner** dice openly at the beginning of combat and leave them visible: a low stored roll becomes a threat hanging over the party, and a high roll becomes an outcome he can guarantee for himself or an ally.
>
> 1. Hold position behind **Winter's Stillness** until the action begins.
> 2. Spend **Fatespinner** to ruin a critical roll.
> 3. Make three **Frostglass Blade** attacks.
> 4. Reposition through **Between Wingbeats**, **Flowing Step**, or **Unchosen Step**.
> 5. Answer weapon pressure with **Absent Feather** and a key spell with **Sever the Gesture**.
> 6. Spend **Five Futures Cut** once the party spreads out or believes distance has made them safe.

**The Fatespinner.** The [[fate-spinner]] does not show him a single predetermined future. It exposes nearby possibilities, and he uses it to find the moments where several outcomes remain possible and then forces one branch to become real. At the table that is the **Fatespinner** trait above. Describe his effects as impossible prediction, wing-assisted footwork, temporal afterimages, strikes intercepted before they begin, movements selected from several possible futures, and the Fatespinner rotating as outcomes collapse; do not call them spellcasting unless another creature is explicitly identifying their magical mechanics.

* **Absent Feather.** The attack passes through the version of Vantyrus the attacker expected to hit.
* **Fatespinner.** The dreidel turns once and an already-rolled possibility becomes real.
* **Five Futures Cut.** Several translucent Vantyruses begin different attacks simultaneously. Only one remains when the movement ends.
* **Binding Grasp.** Every direction the target tries to move briefly produces the same image of Vantyrus already waiting there.
* **Sever the Gesture.** He strikes the wrist, wing, breath, focus, or exact moment required to complete the spell.

**Weakness of Long Sight.** Vantyrus does not see an authored future. He sees probable ones, and his read weakens whenever people act without preparation, irrationally, for reasons he does not understand, against their own obvious interests, through genuine self-sacrifice, or in deliberate coordination with chaos and uncertainty. A creature who willingly accepts a terrible consequence to preserve another person's freedom violates the premise beneath his whole philosophy, and he has trouble predicting it. His greatest blind spot is treating people as solvable systems.

**Goals and fronts.** Vantyrus wants the transformation technique of the [[soul-incarnate|Soul Incarnate]], and his route runs through [[crissdalynn-khinriss]]. Exactly how he intends to read, extract, reproduce, or exploit her [[long-sight|Long Sight]] is not yet established. He anchors the [[rule-of-two]], the [[long-sight-hunt]], [[countless-through-the-maw-seal]], [[sentinels-and-countless]], [[schisms-third-name]], and [[soul-incarnates-watch]].

* **Front: The Rule of Two.** *Lifecycle:* active. *Aim:* stay ahead of [[talon-skarn]]'s open contest to kill him long enough to pry the transformation technique loose from the order that raised him, whatever it costs the people still inside it. *Approach:* he gives Skarn access to every technique and treats each lesson as a live weapon aimed back at him, never announces the test, and never deliberately teaches Skarn anything wrong. If Skarn cannot eventually threaten him, Vantyrus considers himself to have failed as a master. Every other task runs through hired blades and paid contacts who learn one job each and never who gave the order. *Off-screen move if unopposed:* keeps testing Skarn's reach while advancing the Countless's hunt for that gift, the shared operation on [[long-sight-hunt]]. *Closes when:* Skarn's move against him becomes more pressing than one fight, or Kyzil realizing what Crissdalynn is holding closes the one crack Vantyrus is counting on. *Clock:* 4 segments, fast-moving once Skarn commits. Filled: 0. *Consequence at fill:* the contest resolves, and Vantyrus falls to his own apprentice or breaks Skarn decisively and preserves the Rule of Two for a generation. *Possible outcomes:* Skarn strikes and loses, proving Vantyrus's doctrine again; Skarn strikes and wins and the Countless gains a new master; or the fight turns against Vantyrus directly and he escapes through **Unchosen Step**, leaving a hired hand or Skarn to cover the gap while the contest continues another day. *PC connection:* runs through [[crissdalynn-khinriss]] directly, because his whole plan is to read what she is carrying before Kyzil or the order realize what she holds. *Quest link:* none yet.

> [!secret] Secrets and future form
> **Osset is Talon Vantyrus.** The party does not know it, and [[master-kyzil]] believes his old master died decades ago.
>
> Vantyrus still considers Kyzil his greatest student, and his only admitted fear is that [[talon-skarn]] may be right. His current physical location is unknown, and whether the Countless probe through the [[drowned-maw]] seal succeeded is unestablished. Do not reveal him physically until the identity connection can matter.
>
> Do not add Soul Incarnate abilities to this stat block. If he acquires the transformation technique, write a second stat block, and let that form move from **seeing several possible futures** to **existing across several possible futures at once**.

## Connections

| Connection | Meaning |
| --- | --- |
| [[Osset]] | Original name. This page is the live alias and current identity. |
| [[master-kyzil]] | His most gifted student at [[high-eyrie]], who refused to leave the order with him and now believes his old master is decades dead. Vantyrus does not primarily want Kyzil dead; he wants Kyzil to finally admit that watching was not enough. |
| [[talon-skarn]] | His apprentice and eventual executioner, prepared by design under the [[rule-of-two]]. Their contest for Vantyrus's life remains open, and neither has called it off. |
| [[crissdalynn-khinriss]] | Unaware target. Her unexplained [[long-sight|Long Sight]] is the one crack in whatever protects the [[soul-incarnate|Soul Incarnate]] technique. He wants to know what Kyzil taught her, and more importantly what Kyzil refused to teach her. |
| [[sentinels-of-the-eyrie]] | The order he broke from over that old rift with Kyzil. He works against it now. |
| [[Countless]] | The order he leads now, built on the Sentinels' own reach with none of its restraint. |
| [[fate-spinner]] | A divinatory focus he carries and a weapon against probability itself. |
