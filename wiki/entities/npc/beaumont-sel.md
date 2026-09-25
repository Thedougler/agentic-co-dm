---
title: Beaumont Sel
aliases:
  - Beaumont Sel
category: entities
tags: [shattered-sea, npc]
sources:
  - "inbox/archive/FILED-2026-09-05-tessarine-concordat.md"
  - "wiki/journal/Session 02 - Recap.md"
  - "campaign-os:beaumont-sel.md"
summary: Passage operative and family-linked courier who introduced himself to the crew as a Friend of the Passage.
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
tier: supporting
created: 2026-09-13T06:31:54Z
updated: 2026-09-23
type: npc
reveal: revealed
campaign: shattered-sea
location: "[[kalowe]]"
status: alive
role: operative
faction: Passage
visibility: dm
relationships:
  - target: "[[passage]]"
    type: related_to
  - target: "[[nona-black-jaw]]"
    type: related_to
  - target: "[[perrin-black-jaw]]"
    type: related_to
---
# Beaumont Sel

````col
```col-md
flexGrow=2
===
## At a Glance

| **Role**   | Captain of the *Saltwright* |
| ---------- | --------------------------- |
| **Nature** | A shell-worn, quiet tortle who handles trouble like bad weather: wait it out when possible, pay what is necessary when not. |
| **Home**   | [[kalowe]]; the [[Midchain]] route |
| **Wants**  | To keep the Saltwright and its passengers alive, paid for, and clear of Crown trouble. |
| **Leverage** | Eleven years on the route, a trusted crew, the Salvaged [[Antheri]] Plate, and [[Bisou]]'s delivery tricks. |
| **Limit**  | His passengers' reckless impulses are not his responsibility, and he does not hurry for anyone. |

> **DM thesis:** Beaumont is a patient merchant captain whose quiet route knowledge and monkey companion turn practical kindness into reliable Passage access.
```

```col-md
flexGrow=1
===
> [!narration] Beaumont Sel
> Wide and low, Beaumont is built to be hard to move. His river-mud-brown shell is ridged and worn blunt by salt air, with a mirror-bright Salvaged Antheri Plate fitted over a fist-sized dent. Sun-bleached leather covers one eye; a short-stemmed clay pipe rests at the corner of his undershot jaw. His capuchin monkey, [[Bisou]], rides his shoulder with her tail looped once around his neck.
```
````

## Running Beaumont Sel

````col
```col-md
flexGrow=1
===
### First meeting

Beaumont meets the crew at the wheel of the *Saltwright*, holding eye contact too long, saying too little, then moving. In Session 01 he held [[barnaby-rook]]'s attention while passengers fought below, then joined the deck fight.

> *Beaumont*: “The route is clear enough. Get aboard.”
```

```col-md
flexGrow=1
===
### When posture changes

Beaumont remains unhurried while dealing with ordinary inspection or route trouble. He becomes active when passengers are endangered: his Salvaged Antheri Plate deflected Rook's flintlock shot, and he uses [[Bisou]] as a delivery mechanism for potions, alchemical items, and black-powder sabotage.

In Session 02 he threw Bisou through a gun port to foul the [[uncertainty|Surety]]'s cannon, introduced himself as a Friend of the Passage, and passed on [[nona-black-jaw|Nona]]'s message.
```
````

## Voice

Beaumont speaks in an unhurried patois and short practical statements. He volunteers nothing about himself, knows the difference between routine inspection and Crown pressure, and lets [[Bisou]] read the room before he reacts.

**The ask:** *“Tell me where you're going and whether you can pay.”*

**The refusal:** *“That is your trouble, not mine.”*

**Under pressure:** *“Bisou.”*

**Route and history.** Beaumont has run the *Saltwright* out of [[kalowe]] on the [[Midchain]] route for eleven years. He pulled [[crissdalynn-khinriss]] and [[delmar-fisk]] from the water after their fleet went down and gave them passage west without questions. In Session 02 he slid a Truth Stone to Jean-Claude, listened to Delmar's claim of a friend in [[Admiral Fisk]], read the weather toward Calveno, and let Bisou remove 15 gp of shinies from the Surety as fair business before the Saltwright pulled away.
**Stats & Combat.**

```statblock
layout: Basic 5e Layout
name: Beaumont Sel
size: Medium
type: entity
subtype: tortle
alignment: neutral good
ac: 19
hp: 44
hit_dice: 8d8+8
speed: "15 ft."
stats: [18, 8, 14, 12, 14, 13]
saves:
  - strength: 6
  - constitution: 4
skillsaves:
  - athletics: 6
  - perception: 4
  - intimidation: 3
senses: "passive Perception 14"
languages: "Common, Aquan"
cr: 2
traits:
  - name: Salvaged Antheri Plate
    desc: "Ranged weapon attacks against Beaumont are made at disadvantage. The Antheri alloy's mirror-bright surface throws a hard glare at anyone trying to draw a bead on it."
  - name: Hold Breath
    desc: "Beaumont can hold his breath for 1 hour."
  - name: Old Bones
    desc: "Beaumont's speed is 15 ft. When he Dashes, he moves 20 ft. total rather than doubling his speed."
actions:
  - name: Multiattack
    desc: "Beaumont makes one Uppercut and one Jab. He can replace either attack with a Throw."
  - name: Uppercut
    desc: "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) bludgeoning damage."
  - name: Jab
    desc: "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d4 + 4) bludgeoning damage."
  - name: Throw
    desc: "One creature within 5 ft. makes a contested Strength (Athletics) check against Beaumont (+6). On a failure, the target takes 7 (1d6 + 4) bludgeoning damage, is moved up to 10 ft. in a direction Beaumont chooses, and falls prone."
  - name: The Kalowe Maneuver
    desc: "Beaumont tosses a potion of healing alongside Bisou to a creature within 30 ft. that is unconscious or at half hit points or fewer. Bisou lands, uncorks the potion, and empties it into the target's mouth — the target regains 2d4 + 2 hit points. Bisou returns to Beaumont's shoulder at the start of his next turn. Requires one available potion of healing; Bisou must not be incapacitated. Beaumont currently has three potions."
  - name: The Calveno Maneuver
    desc: "Beaumont hands Bisou an alchemical item. Bisou moves up to 60 ft., delivers it to a point of Beaumont's choosing, triggers it, and drops it there. The item activates at the start of Beaumont's next turn. Bisou then moves 15 ft. away as a free reaction. Requires an available alchemical item; Bisou must not be incapacitated."
  - name: The Tidefall Maneuver
    desc: "Beaumont tosses Bisou toward a target creature within 30 ft. Bisou locates and soaks any exposed black powder on the target. The target must succeed on a DC 12 Dexterity saving throw or have all black powder weapons rendered inoperable until dried. Bisou returns to Beaumont's shoulder at the start of his next turn. Bisou must not be incapacitated."
```

Beaumont fights the way he does everything else, without hurry and without wasted motion. He plants his wide, low frame and trades Uppercuts and Jabs at close range instead of chasing an opening. His shell and his years both argue against extending himself further than he has to. Old Bones caps his Dash at a flat 20 ft. instead of doubling his speed.

The Salvaged [[Antheri]] Plate patched into his shell throws off ranged attacks with a hard, mirror-bright glare.

His real weapon is [[Bisou]]: he throws her, hands her things, and trusts her to deliver.

- **The [[kalowe]] Maneuver** lobs a potion of healing alongside her to a downed ally, who gets it emptied straight into their mouth.
- **The [[calven-and-calveno]] Maneuver** sends her with an alchemical item up to 60 ft. She plants it and triggers it remotely.
- **The [[calders-tooth-and-port-tidefall]] Maneuver** sends her to soak an exposed black powder supply so it won't fire.

All three depend on Bisou being conscious and reachable, most often his shoulder, and each returns her to him by the start of his next turn.

## Connections

- [[Bisou]], a capuchin monkey, serves as his shoulder companion for the full eleven years he has run the [[Midchain]]. Threw her through a gun port to jam Rook's cannons. Tosses her into combat as a delivery mechanism.
- [[crissdalynn-khinriss]], [[delmar-fisk]] (both pulled from the water after her fleet went down, given passage west).

- [[barnaby-rook]] (Crown captain). The Salvaged Antheri Plate deflected his flintlock shot in Session 01. The Plate patches a dent in his shell and throws off ranged attacks.
- [[perrin-black-jaw]], [[the-passage]] (the crew's first contact with the network, made when Beaumont identified himself as a Friend of the Passage after he took the Surety).
- [[jean-claude-tabarnack]] (given the Truth Stone).
- [[nona-black-jaw]] (passed on her message about her lost grandson). She believed someone had already sent [[anzolo]].

- [[Saltwright]], [[kalowe]], [[Midchain]] (his merchant brig running the eleven-year Midchain route out of Kalowe). He read the weather toward [[calven-and-calveno]] the morning it departed.
- Crew: [[lenne-vor]] (navigator), [[drav-holke]] (bosun), [[Wessa]] (cook), [[Fen]] (ordinary sailor).

**Session log.**

- **Session 01: boarding of the Saltwright** held Rook's attention at the wheel during the hold ambush. Joined the fight on deck. Deflected Rook's flintlock shot with the Salvaged Antheri Plate. `vault/episodes/001/transcript.md:25,59`.
- **[[Session 02: conflict is a surety]]** solved the cannon problem by throwing [[Bisou]] through a gun port. Settled accounts with Perrin, Jean-Claude, and Nona's message. Departed at dawn for [[kalowe]] via Calveno as a friend earned. `vault/episodes/002/transcript.raw.md:31,35,39-43,71,93-94`.
