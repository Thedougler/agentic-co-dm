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
invention: true
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

- **The job.** His win condition is the current job, not a duel to 0 hit points. He takes the object if one is at stake. Otherwise he attacks the creature blocking the job, then the carrier, then anyone between him and it. On the carrier, **Cut Loose** turns his hits into dropped pouches and straps until the prize shows, and **Kusarigama** snatches it. Anyone who gets between them takes full damage.
- **The rhythm.** Cut, climb, stoop, mantle. On one turn he attacks, then takes **Step of the Falcon** to Disengage and climbs at least 60 feet. When his chains go quiet and his wings fold tight, the next turn is **Peregrine Stoop**. After the Stoop he is mantled on the ground until his next turn, with Speed 0 and Advantage on attacks against him. That round is the party's window to grapple him and take back whatever he tore loose.
- **Answering the Stoop.** Get the target under cover overhead, because a tree, the vine, or an overhang blocks the dive. Ready an attack or a grapple for when he lands. Keep the prize in a closed hand, because the Stoop tears loose only what nobody holds. [[crissdalynn-khinriss]] can fly up, or [[delmar-fisk]] can fly in his [[flying-boots]], to fight him in the air before he dives. Uncanny Dodge, Deflect Attacks, and Cutting Words all blunt the hit.
- **Default turn.** **Stunning Strike** once on his turn, then **Kusarigama** to pull a target clear of its partner, or **Sai** to blunt the watcher's next attack. He moves the stun from PC to PC, because the one he just stunned is safe from it until his next turn ends.
- **Legendary actions.** After another creature's turn: **Chain Snap** to reopen a pull or snatch a loose prize, **Crossing Sai** to punish a watcher, or **Wingbeat Step** to change his lane, each at most once before his next turn.
- **Kusarigama Tempest.** When two or more creatures are inside its 20-foot Emanation and a pull or the Prone condition changes the fight. On a failed save he chooses pull or Prone for each creature; on a success, damage only.
- **Legendary Resistance.** Each use snaps a length of chain wrap off his forearm, and it falls clinking to the ground. The players can count what he has left.
- **Last Stoop.** At 97 HP or fewer he tears straight up into the sky, unless he is grappled or his Speed is 0. Everyone gets one round to hide the prize, move the carrier under cover, ready an action, or hand it off. His next turn is a Stoop on the carrier, and on the turn after that he leaves, with or without it. If the carrier stays under cover, he chains the carrier toward open sky instead, then leaves.
- **Counterplay.** Ground him with a grapple or restraint, which costs him his action to escape. **Constitution** save `DC 18` resists Stunning Strike. He has AC 19 and no damage resistances. **Deflect Attack** stops only Bludgeoning, Piercing, and Slashing damage, so spells and [[perrin-black-jaw]]'s Radiant or Psychic pact blade go straight through. Spread out against the Tempest, deny clean pulls, and make him spend movement.
- **Measuring.** Every fight is practice for the one he means to win against [[talon-vantyrus]] ([[rule-of-two]]). When a PC lands something he did not see coming, such as a stun that holds, a grapple he cannot slip, or a Cutting Word that turns his blade, he stops for one breath and says, "Again." He remembers that PC, and the next time they meet he opens on them first.
- **Harder.** Start him 60 feet up with the Stoop ready, without raising his AC.

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
    desc: "If Talon fails a saving throw, he can choose to succeed instead. Each time he does, a length of chain wrap snaps from his forearm and falls."
  - name: Skyhunter
    desc: "Opportunity Attacks against Talon have Disadvantage while he is flying."
  - name: Cut Loose
    desc: "When Talon hits a creature with a Katana or Sai attack, he can deal no damage and instead cut loose one object the creature is wearing or carrying but not holding, such as a pouch, strap, sheath, or quiver. The object falls in the creature's space. Talon can't snatch an object with Kusarigama on the same turn he cut it loose."
  - name: Stunning Strike (1/Turn)
    desc: "Immediately after Talon hits a creature with a melee attack during his turn, he can force it to make a DC 18 Constitution saving throw. Failure: The creature has the Stunned condition until the start of Talon's next turn, and it can't be Stunned by this trait again until the end of Talon's next turn. Success: Its Speed is halved until the start of Talon's next turn, and the next attack roll made against it before then has Advantage."
  - name: Last Stoop
    desc: "The first time Talon is Bloodied, he can immediately fly up to 90 feet straight up without provoking Opportunity Attacks, unless his Speed is 0. On his next turn, he uses Peregrine Stoop against the creature carrying what he came for if he can reach it, and otherwise makes a Kusarigama attack against that creature. At the start of his following turn, he flies away at full speed."
actions:
  - name: Multiattack
    desc: "Talon makes three attacks, using Katana, Kusarigama, or Sai in any combination."
  - name: Katana
    desc: "Melee Attack Roll: +11, reach 5 ft. Hit: 17 (2d10 + 6) Slashing damage."
  - name: Kusarigama
    desc: "Melee Attack Roll: +11, reach 20 ft. Hit: 15 (2d8 + 6) Slashing damage. If the target is Large or smaller, Talon can pull it up to 10 feet toward himself. Instead of attacking a creature, Talon can snatch one object within 20 feet of him. If nobody holds the object, he makes the attack roll against AC 10. If a creature holds it, that creature makes a DC 19 Strength or Dexterity saving throw (its choice) instead. On a hit or a failed save, the object flies into Talon's free hand."
  - name: Sai
    desc: "Melee Attack Roll: +11, reach 5 ft. Hit: 13 (2d6 + 6) Piercing damage, and the target has Disadvantage on the next attack roll it makes before the start of Talon's next turn."
  - name: Peregrine Stoop
    desc: "Talon can take this action only if he starts his turn flying at least 60 feet higher than the target, with open sky between them. When he ends a turn that high, his chains fall silent and he folds his wings tight. He dives up to 180 feet in a straight line to a space within 5 feet of the target without provoking Opportunity Attacks; a canopy, roof, or overhang above the target blocks the dive. He then makes one Katana attack with Advantage. Hit: 17 (2d10 + 6) Slashing damage plus 27 (6d8) Slashing damage, and the target has the Prone condition. Instead of the 6d8 damage, Talon can tear loose one object the target is wearing or carrying but not holding and take it into his free hand. Hit or miss, Talon mantles over the target: until the start of his next turn, his Speed is 0 and attack rolls against him have Advantage."
  - name: Kusarigama Tempest (Recharge 5–6)
    desc: "Dexterity Saving Throw: DC 19, each creature of Talon's choice in a 20-foot Emanation originating from him. Failure: 27 (6d8) Slashing damage, and Talon either pulls the creature up to 15 feet toward himself or gives it the Prone condition. Success: Half damage only."
bonus_actions:
  - name: Step of the Falcon
    desc: "Talon takes the Dash or Disengage action."
reactions:
  - name: Deflect Attack
    desc: "Trigger: Talon is hit by an attack roll that deals Bludgeoning, Piercing, or Slashing damage. Response: Talon reduces that damage to himself by 18 (2d10 + 7). If this reduces the damage to 0 and the attack was made with a melee weapon, the attacker makes a DC 19 Strength saving throw. Failure: Talon hooks the weapon away, and it lands in an unoccupied space of his choice within 10 feet of him."
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
