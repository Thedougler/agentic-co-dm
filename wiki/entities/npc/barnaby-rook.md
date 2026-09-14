---
title: "Barnaby Rook"
aliases:
  - Barnaby Rook
category: entities
tags: ["shattered-sea", "npc"]
sources:
  - "campaign-os:barnaby-rook-narration-appearance.md"
  - "story-so-far.md"
  - "campaign-os:barnaby-rook.md"
summary: "Boarded the Crown cutter Surety during the Saltwright fight and went into the water twice."
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.37
lifecycle: proposed
lifecycle_changed: "2026-09-13"
tier: supporting
created: 2026-09-13T19:35:00Z
updated: 2026-09-13
type: npc
reveal: unrevealed
campaign: shattered-sea
visibility: dm
---
# Barnaby Rook

# Barnaby Rook

![[Barnaby Rook Banner]]
![[Barnaby Rook Portrait]]

**Wants:** to choke every irregular captain out of the [[calders-tooth-and-port-tidefall]] corridor for the [[dravosi-crown]], narrowed since his fall off the Surety's rigging to running down the crew who defected or surrendered under him.

![[Barnaby Rook Narration Appearance]]


The face of the Crown's tightening grip on [[calders-tooth-and-port-tidefall]], Rook is a hard [[dravosi-crown]] privateer captain who boards under colour of law and expects weaker captains to surrender before violence begins. When talk fails, he pivots to fear.

He speaks in flat statements, not conversation. Each one is a command. He absorbs hits and comes back stronger. Threat is silent, never loud. It turns lethal in moments. He shows no hesitation about shooting crew members for defection.

He runs the inspection and shakedown campaign around Tidefall, replacing [[norrington-kingsly]] as the harder choice. Where his predecessor negotiated routine fees, Rook pursues names, contraband, and compliant captains, and he recognizes betrayal instantly: when Geoffrey surrendered at the [[Saltwright]], Rook knew at once. The Crown chain runs through [[Dorian Bishop]] to [[rupert-knighton]], and Rook serves as their tool, answering to both. He works the inspection corridor between the [[crown-islands]] and the [[central-strait]], the same stretch [[commander-gideon-ault]]'s [[hcs-warrant]] patrols out of [[Harwick]], with Crown authority stacked two ships deep along that water, and he crews the Surety with [[dravosi-deckhand|Dravosi Deckhands]].

He was first met in Session 01, boarding the Saltwright. Rook stayed on deck while [[beaumont-sel|Beaumont]] distracted the crew below. When the last [[dravosi-deckhand]] dropped his sword, Rook called out: *"I'll shoot you myself for that, you turncoat."* Jean-Claude hit him with the [[Flask of Endless Water]] at the gangplank and threw him back, but he got up and fired at [[beaumont-sel|Beaumont]]. Her plate deflected the shot. The session ended with him alone and furious.

In Session 02, Rook retook the Surety alone, though his crew had either died or defected, including [[geoffrey-draves]]. Crissdalynn bent his flintlock shot with her wind and caught the follow-up on her bracers, while [[beaumont-sel|Beaumont]] threw [[Bisou]] through a gun port to handle the cannon. Delmar knocked Rook from the rigging into the water twice, wind-thrown chairs both times. Something long and eel-like swam near him in the dark water, and he didn't resurface. Presumed dead. Crissdalynn fished his hat out with a boat hook.

The crew searched his cabin and cargo, finding 45 gp, [[letters-of-marque]], and a blunderbuss in the cabin, plus 110 gp and two garnets under the floor, and a pendant marked *For Mira, from the sea*. A crate held flintlocks, Mira's Blade, and twenty vials of [[Grung]] poison that Jean-Claude knew from the Alchemist in Session 01. Mira's Blade went to [[perrin-black-jaw|Perrin]].

Rook held captive a [[Moucheron]] named Ket as "a specimen," driven by curiosity about the [[five-blades]] mercenaries who operate out of [[Kalowe]]. The crew freed Ket, who ate and flew home to [[Murrat]].

The tincture ties him to [[simone-tabarnack]]'s supply chain. The same Grung poison reached him as a privateer. The crew doesn't yet know the full connection. His death may not have reached Rupert Knighton up the Crown chain.

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: Captain Barnaby Rook
size: Medium
type: entity
subtype: "human"
alignment: "lawful neutral"
ac: 17
hp: 120
hit_dice: "12d8 + 36"
speed: "30 ft."
stats: [14, 16, 16, 13, 12, 14]
saves:
  - dexterity: 5
  - constitution: 5
skillsaves:
  - athletics: 4
  - intimidation: 4
  - perception: 3
senses: "passive Perception 13"
languages: "Common"
cr: 3
traits:
  - name: Officer's Advantage
    desc: "While at least two allies are within 30 ft. of Rook and can hear him, he has advantage on initiative rolls and cannot be surprised."
  - name: Cornered Wolf
    desc: "When Rook has no living allies within 30 ft., his Parry reaction reduces damage by 1d10 + 6 instead of 1d10 + 4, and it applies to ranged attacks as well as melee. Additionally, he has advantage on saving throws."
  - name: Naval Footwork
    desc: "Rook can Disengage as a bonus action."
bonus_actions:
  - name: Disengage (Naval Footwork)
    desc: "Rook disengages without provoking opportunity attacks and moves up to his speed."
actions:
  - name: Multiattack
    desc: "Rook makes two attacks: each is either a Cutlass attack or a Flintlock Pistol attack. He cannot make more than one Flintlock attack per turn unless he takes an action to reload."
  - name: Cutlass
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) slashing damage. On a hit, Rook can forgo the damage to shove the target up to 5 ft. in any direction (no save)."
  - name: Flintlock Pistol
    desc: "Ranged Weapon Attack: +5 to hit, range 30/90 ft., one target. Hit: 12 (2d8 + 3) piercing damage. Once fired, requires an action to reload. Rook carries a brace — he has two pistols, each loaded once."
reactions:
  - name: Parry
    desc: "When an attack hits Rook, he reduces the damage by 1d10 + 4 (or 1d10 + 6 if Cornered Wolf is active). He must be holding a melee weapon and be aware of the attacker. Applies to melee only unless Cornered Wolf is active."
legendary_description: "Rook can take 3 legendary actions per round, choosing from the options below. Only one legendary action option can be used at a time, and only at the end of another creature's turn. Rook regains spent legendary actions at the start of his turn."
legendary_actions:
  - name: Reposition (Costs 1 Action)
    desc: "Rook moves up to half his speed without provoking opportunity attacks."
  - name: Cutlass Strike (Costs 2 Actions)
    desc: "Rook makes one Cutlass attack. He can use the shove option on a hit."
  - name: Pistol Reload (Costs 2 Actions)
    desc: "Rook reloads one expended flintlock pistol. He does not fire it — this sets up his next turn or a future legendary action."
lair_actions:
  - desc: "On initiative count 20 (losing initiative ties), Barnaby Rook issues a command to the crew of the HCS Surety, choosing one of the following lair actions. He cannot use the same lair action two rounds in a row."
  - desc: "Arm the Guns. Rook orders the gun crew to uncover the hatches of the Surety's two deck-level cannons and ready them for firing. No immediate effect — the guns are primed. This enables Fire the Guns on the following round."
  - desc: "Fire the Guns. If the Surety's cannons were Armed last round, Rook commands both gun crews to fire. Each cannon discharges in a 30-foot cone extending from its gun port along the deck. Each creature or object in either cone must make a DC 14 Dexterity saving throw, taking 4d10 bludgeoning damage on a failed save, or half on a success. Structures and objects in either cone automatically take the full damage."
  - desc: "Call to Arms. If Rook has been reduced below half his hit point maximum (60 hp), he calls out to all remaining crew aboard the Surety. Up to 1d4+1 Dravosi Deckhands appear at the start of Rook's next turn in unoccupied spaces aboard the Surety."
```

CR 3 boarding specialist and Phase 3 boss of the Saltwright with lair actions aboard the HCS Surety. Rook fights flat and controlled, absorbing hits and regrouping without escalating.

With two or more allies near, Officer's Advantage helps him in initiative and resists surprise. Without allies, Cornered Wolf makes him dangerous alone. His Parry and saves get better.

Naval Footwork lets him move away and disengage without cost. He repositions or reloads as needed. A clean [[knock]] off his footing costs him that disengage outright, and [[delmar-fisk|Delmar]] used exactly that to put him in the water twice. Aboard the Surety, his lair actions transform the ship into a weapon. One round spent on Arm the Guns prepares Fire the Guns the following round. Dropping him below half HP triggers Call to Arms.

## Connections

- [[norrington-kingsly]]: his predecessor, replaced by Rook as the harder choice.
- [[dravosi-crown]]: the naval and inspection authority both serve.
- [[Uncertainty|HCS Surety]]: his ship.
- [[geoffrey-draves]]: crew member. Rook saw his surrender at the Saltwright as betrayal.
- [[Dorian Bishop]], [[rupert-knighton]]: the officers up the Crown ladder Rook answers to.
- [[beaumont-sel]]: commands the Saltwright. She deflected his shots twice in Session 01.
- [[Ket]]: a Moucheron Rook held captive. Rook wanted to learn about the [[five-blades]] in [[Kalowe]].
- Mira's Blade: found in his cargo. It went to Perrin.
- [[simone-tabarnack]]: supplied his Grung tincture during his time with the Dravosi Crown.

## Session Log

- **Session 01: boarding of the Saltwright**. Kept above decks during the hold ambush, threatens [[geoffrey-draves]], caught by the Flask of Endless Water on the gangplank, fires his flintlock at [[beaumont-sel|Beaumont]] (deflected). Ends the session unharmed and alone. `vault/episodes/001/transcript.md:25,37-39,49,59,73`.
- **[[Session 02: conflict aboard the Surety]]**. Retakes the Surety alone, fires on Crissdalynn (deflected), gets knocked into the water twice by Delmar and taken by something eel-like. The crew searches his cabin and cargo afterward. `vault/episodes/002/transcript.raw.md:25,29,31,33,35,69,91`.
