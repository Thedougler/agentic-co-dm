---
type: npc
status: pending
publish: false
aliases: ["Vashu (Winded)"]
created: 2026-07-30
updated: 2026-08-09
tags: [combat]
summary: "Vashu's Session 06 Scene 4 winded combat state — sprint-depleted Still-Water reserves drop her to AC 18, 80 HP, CR 5, and cost her legendary actions."
subtype: minor
location: "[[calveno-sewers-grung-magazines|Calveno Sewers]]"
campaigns: [Shattered Sea]
role: []
uid: 2c00aa28-08d6-43a6-811e-de699cac3b58
---

# [[vashu-the-weeping-veil|Vashu, the Weeping Veil]] (Winded)

This session's combat state of [[vashu-the-weeping-veil|Vashu, the Weeping Veil]]. She spent her Still-Water reserves during a flat-out sprint from Room T1 to reach the summoning circle in [[scene-04-fight-continues|Session 06, Scene 4]], which also removes her legendary actions. For full background and appearance, see her own page. Delta and calibration source: `vault/campaigns/shattered-sea/pcs/combat-profile/sim-variants/vashu-winded-s06.md`.

> [!read-aloud]
> A purple blur comes up through the east channel at a dead run, rhythmic clicking announcing its presence a moment before a small purple [[grung-npc|Grung]] with milk-white eyes plants herself between you and the circle, breathing hard with her veil plastered flat against her skull.

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: Vashu, the Weeping Veil (Winded)
size: Small
type: humanoid
subtype: grung
alignment: lawful evil
ac: "18 (unarmored, perfected Still-Water Discipline, winded)"
hp: 80
hit_dice: "20d6 + 20"
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
cr: 5
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
    desc: "A creature that hits Vashu with a melee attack while within 5 feet of her, or that grapples her, must succeed on a DC 14 Constitution saving throw or be poisoned until the start of its next turn."
actions:
  - name: Multiattack
    desc: "Vashu makes one Still-Water Strike attack and one Tongue Lash attack."
  - name: Still-Water Strike
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage. If the target is poisoned, it also takes 9 (2d8) poison damage."
bonus_actions:
  - name: Tongue Lash
    desc: "Vashu lashes her tongue at one creature she can perceive within 20 feet. Ranged Weapon Attack: +7 to hit. Hit: 5 (1d4 + 3) bludgeoning damage, and Vashu pulls the target up to 15 feet toward her, to an unoccupied space, ending the pull early if it would put the target in danger (e.g. a fall, hazard, or lava). No effect on a target two or more size categories larger than Vashu."
  - name: "Weeping Veil (Recharge 5–6)"
    desc: "Vashu shatters a bone vial, releasing a bitter mist in a 25-foot-radius sphere centered on herself. The area is heavily obscured until the start of her next turn. Each creature that starts its turn in the area, or enters it for the first time on a turn, must succeed on a DC 14 Constitution saving throw or be blinded and poisoned until the end of that turn. Vashu is unaffected. She carries 4 vials."
  - name: Step of the Tide
    desc: "Vashu takes the Dash or Disengage action."
reactions:
  - name: Still-Water Deflection
    desc: "When Vashu or an ally within 10 feet of her is hit by a ranged attack Vashu can perceive, she reduces the damage to that target by 15 (2d10 + 4). If this reduces the damage taken by Vashu herself to 0, she can redirect the missile at a creature she can perceive within 30 feet: +7 to hit, 12 (2d10 + 1) damage of the triggering attack's type."
```

## Relationships

Same NPC as [[vashu-the-weeping-veil|Vashu, the Weeping Veil]]. See her page for the full relationship list.

## Session Log

- **Session 06**: [[catarina-davirelli|Catarina]] hits her with [[fire-bolt|Fire Bolt]] (15 fire damage), then on the next turn has her homunculus Strix land a [[shocking-grasp|Shocking Grasp]] (13 lightning damage). Vashu turns and locks onto Catarina in response. Delmar's blunderbuss shot (identified in play as hitting "the blind one") forces a DEX save against the explosive follow-up. Vashu fails the save, but the DM rules her Evasion trait halves the damage instead.

- Confirmed: [[transcript]]: "Vashu turns around you and without looking at you, she does seem to have locked onto you now. He's pissed her off." / "Zaxu's dex mod is plus 5… it's a 10! That's not good. Okay, well, I guess I'm going to use Evasion and instead take half damage."
