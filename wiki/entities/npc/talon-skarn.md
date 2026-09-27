---
title: Talon Skarn
aliases:
  - Talon Skarn
  - Skarn
category: entities
tags: [shattered-sea, npc]
sources:
  - "campaign-os:talon-skarn.md"
  - "wiki/_archive/Talon Skarn.md"
  - "wiki/entities/quest/rule-of-two.md"
  - "wiki/entities/faction/countless.md"
  - "journal/sessions/shattered-sea/11/Session-11-Recap.md"
created: 2026-09-12
updated: 2026-09-27
type: npc
reveal: revealed
campaign: shattered-sea
status: alive
role: rival
location: "[[river-slack-basin]]"
faction: "[[Countless]]"
visibility: dm
summary: "Talon Vantyrus's peregrine apprentice in the Countless, a CR 13 flying monk hunting the Fate Spinner; under the Rule of Two he will one day try to kill his master."
---
# Talon Skarn

![[talon-skarn-reference-sheet.jpg|Talon Skarn character reference sheet]]

````col
```col-md
flexGrow=2
===
## At a Glance

Skarn is the Countless's blade on the party: he hunts the [[fate-spinner]] for [[talon-vantyrus]], and he wants the object, not a duel.

- **Role.** Vantyrus's apprentice in the [[Countless]], and a CR 13 flying skirmisher.
- **Nature.** A peregrine aarakocra monk, the living expression of the [[rule-of-two]].
- **Wants.** The Fate Spinner for Vantyrus now. Vantyrus's death once he has trained well enough.
- **Home.** The Midchain.
- **Allegiance.** Vantyrus and the Countless. He is loyal for now.
- **Kit.** Katana, two sai, and two kusarigama.
- **Now.** In [[crissdalynn-khinriss]]'s face at the [[river-slack-basin]], one Legendary Resistance spent, with the Fate Spinner still on her.
```

```col-md
flexGrow=1
===
> [!narration] Talon Skarn
> Talon Skarn is a broad peregrine aarakocra about five feet tall, heavy wings lifted behind a dark robe. Pale chest feathers climb into a black and cream face, red-orange crown feathers flare above steady amber-gold eyes, and his yellow beak is tipped in black. The robe hangs in dark layers over wrapped ankles and bare talons. Cloth wraps and loose chains cover his forearms, and the links click once and settle whenever he shifts his grip on the long straight sword in one hand and the hooked blade on its chain in the other.
```
````

## At the Table

- **The job.** His win condition is the current job, not a duel to 0 hit points. He takes the object if one is at stake. Otherwise he attacks the creature blocking the job, then the carrier, then anyone between him and it. He cuts gear before throats.
- **Opening.** Wings lift and chains click. He drops out of the sky with **Peregrine Dive**, or sets the distance with **Kusarigama**.
- **Default turn.** **Stunning Strike** once on his turn, then **Kusarigama** to pull a target clear of its partner, or **Sai** to blunt the watcher's next attack.
- **Legendary actions.** After another creature's turn: **Chain Snap** to reopen a pull, **Crossing Sai** to punish a watcher, or **Wingbeat Step** to change his lane, each at most once before his next turn.
- **Kusarigama Tempest.** When two or more creatures are inside its 20-foot Emanation and a pull or the Prone condition changes the fight. On a failed save he chooses pull or Prone for each creature; on a success, damage only.
- **If pressured.** **Step of the Falcon** to Disengage, **Wingbeat Step** to change lane, and **Deflect Attack** on the first solid hit. At 97 HP or fewer, he finishes the current job if he can, and otherwise leaves.
- **Counterplay.** Ground him with a grapple or restraint. **Constitution** save `DC 18` resists Stunning Strike. He has AC 19 and no damage resistances. Spread out against the Tempest, deny clean pulls, and make him spend movement.
- **Easier.** Remove Legendary Resistance and start Kusarigama Tempest uncharged.
- **Harder.** Start him in the air, without raising his AC.

## Statblock

```statblock
layout: Basic 5e Layout
dice: true
columns: 2
forceColumns: true
name: Talon Skarn
size: Medium
type: humanoid
subtype: aarakocra
alignment: lawful neutral
ac: 19
hp: 195
hit_dice: "23d8 + 92"
speed: "50 ft., fly 90 ft."
stats: [14, 22, 18, 12, 20, 14]
saves:
  - dexterity: 11
  - constitution: 9
  - wisdom: 10
skillsaves:
  - acrobatics: 16
  - insight: 10
  - perception: 10
  - stealth: 11
senses: "Passive Perception 20"
languages: "Auran, Common"
cr: 13
traits:
  - name: Evasion
    desc: "When Talon is subjected to an effect that allows him to make a Dexterity saving throw to take only half damage, he instead takes no damage on a successful save and half damage on a failed save. He can't use this trait while Incapacitated."
  - name: Legendary Resistance (3/Day)
    desc: "If Talon fails a saving throw, he can choose to succeed instead."
  - name: Skyhunter
    desc: "Opportunity Attacks against Talon have Disadvantage while he is flying."
  - name: Peregrine Dive
    desc: "If Talon flies at least 30 feet downward in a straight line immediately before hitting a creature with his Katana, the attack deals an extra 13 (3d8) Slashing damage, and the target must succeed on a DC 18 Strength saving throw or have the Prone condition. Talon can deal this extra damage only once per turn."
  - name: Stunning Strike (1/Turn)
    desc: "Immediately after Talon hits a creature with a melee attack during his turn, he can force it to make a DC 18 Constitution saving throw. On a failed save, the creature has the Stunned condition until the start of Talon's next turn. On a successful save, its Speed is halved until then, and the next attack roll made against it before then has Advantage."
actions:
  - name: Multiattack
    desc: "Talon makes three attacks, using Katana, Kusarigama, or Sai in any combination."
  - name: Katana
    desc: "Melee Attack Roll: +11, reach 5 ft. Hit: 17 (2d10 + 6) Slashing damage."
  - name: Kusarigama
    desc: "Melee Attack Roll: +11, reach 20 ft. Hit: 15 (2d8 + 6) Slashing damage. If the target is Large or smaller, Talon can pull it up to 10 feet toward himself."
  - name: Sai
    desc: "Melee Attack Roll: +11, reach 5 ft. Hit: 13 (2d6 + 6) Piercing damage, and the target has Disadvantage on the next attack roll it makes before the start of Talon's next turn."
  - name: Kusarigama Tempest (Recharge 5–6)
    desc: "Talon whirls both chained sickles around himself. Each creature of his choice in a 20-foot Emanation must make a DC 19 Dexterity saving throw. Failure: 27 (6d8) Slashing damage, and Talon either pulls the creature up to 15 feet toward himself or gives it the Prone condition. Success: Half damage only."
bonus_actions:
  - name: Step of the Falcon
    desc: "Talon takes the Dash or Disengage action."
reactions:
  - name: Deflect Attack
    desc: "Trigger: Talon is hit by an attack roll. Response: Talon reduces the attack's damage to himself by 18 (2d10 + 7). If this reduces the damage to 0, Talon can immediately move up to 10 feet without provoking Opportunity Attacks."
legendary_actions:
  - name: ""
    desc: "Legendary Action Uses: 3. Immediately after another creature's turn, Talon can expend one use to take one of the following actions. He regains all expended uses at the start of his turn."
  - name: Chain Snap
    desc: "Talon makes one Kusarigama attack. He can't use Chain Snap again until the start of his next turn."
  - name: Crossing Sai
    desc: "Talon makes one Sai attack. He can't use Crossing Sai again until the start of his next turn."
  - name: Wingbeat Step
    desc: "Talon moves up to half his Speed without provoking Opportunity Attacks. He can't use Wingbeat Step again until the start of his next turn."
```

## Secrets

- **The Rule of Two.** It is an open secret between Skarn and Vantyrus that Skarn will try to kill his master once he has trained well enough. Until then he serves. Vantyrus treats the attempt as a standing threat, and Skarn has no reason to stop after one failed approach. The winner takes control of the Countless ([[rule-of-two]]).

## Connections

- [[talon-vantyrus]] — his master, and his eventual target.
- [[Countless]] — the order he serves; he and the one-job contacts interpret Vantyrus's orders.
- [[crissdalynn-khinriss]] — the Fate Spinner's carrier.
- [[rule-of-two]] — the contest for the Countless.

## Log

- **[[Session-11-Recap]]** — On Crissdalynn's last watch at the Slack Basin, he dropped out of the dark. His first strike missed her, and he went for the pack that might hold the Fate Spinner. She hit him hard enough to stun him; he spent one Legendary Resistance and stayed on her. Play stopped there, with the Spinner still on her.

## Art

![[talon-skarn-portrait.jpg|Talon Skarn portrait]]
![[talon-skarn-token.png|Talon Skarn token]]
