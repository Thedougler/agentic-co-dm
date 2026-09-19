---
title: Otar the Foul
aliases:
  - Otar the Foul
category: entities
tags: [shattered-sea, npc]
sources: ["Mercatura.md"]
summary: Named opponent whose defeat at Mercatura is a closed Season 1 thread.
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.37
lifecycle: proposed
lifecycle_changed: "2026-09-13"
tier: supporting
created: 2026-09-13T07:50:00Z
updated: 2026-09-13
type: npc
reveal: unrevealed
campaign: shattered-sea
visibility: dm
relationships:
  - target: "[[Mercatura]]"
    type: related_to
---
# Otar the Foul

**Wants:** rend and devastate, chaos rising unfettered in the plaza.

> [!narration] Narration
> Crimson hide, twelve feet tall and toad-like, corrupted and weeping. His jaw gapes blank, eyes vacant. Rot seeps across his red flesh in widening cracks, pouring ichor and green vapor in endless molt. Ages ago his change locked at this form, the hide always splitting while muscle and sinew coil beneath like wild things. He stands in the crater, confused, his weight sinking the ground. Fluid pools where his feet shred earth.


**Roleplay Concept:** ancient chaos, summoned destruction free.

**Opening move:** standing in the crater where Solange materialized, disoriented and newly embodied · Otar does not speak · he roars, tongue lashing reflexively toward movement

Not a random slaad pulled from Limbo (few scholars track slaadi by name), this one has a true name: Otar the Foul, OH-tar in the slaad-tongue root, guttural and blunt. A shadow pools at Solange's feet, becoming jaws that close with thick black ichor. He consumes her in two to three violent seconds, not killing her or taking over her mind. What stands afterward is Otar wearing her flesh: a red slaad (aberration), primary-chamber boss of the Beffa [[Grung]] Raid on [[calven-and-calveno]]. Witnesses see the full change, while the townsfolk outside see only the result: the Mercatura plaza falls and something massive, red, and toad-like climbs from the crater. Cracks run through his hide as he molts, weeping fluid and green fog. Otar is ancient and rotting, his transformation stopped centuries ago at red and won't resume. He is wild and free. [[Simone]]'s circle linked itself to his power using methods the Grung didn't develop, built by a contractor who knew what they were summoning. That person's identity is unknown.

The summoning circle sits in the [[Calveno Sewer Magazines]]' primary detonation chamber, part of the [[Mercatura]] collector system running beneath the plaza above.

**Toy Chest**

| Field | Value |
|---|---|
| Primary goal | Rend and consume everything in reach, chaotic and unfettered. |
| Consistent method | Erupts chaotically, lashing and pulsing to shred prey, while regeneration sustains through all wounds. |
| Active problem | Surrounded by adventurers in the plaza with townsfolk trapped in rubble within reach. |
| Performance hooks | Primal chaos incarnate · weeps ichor from deepening cracks as he molts. |
| Link of relevance | Summoned to destroy Mercatura plaza, ultimately defeated by [[delmar-fisk|Delmar]] and the adventurers. |

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Otar the Foul"
size: Large
type: aberration
alignment: "chaotic neutral"
ac: 16
ac_note: "natural armor"
hp: 135
hit_dice: "12d10 + 69"
speed: "40 ft., climb 20 ft."
stats: [20, 12, 22, 5, 8, 6]
saves:
  - strength: 9
  - constitution: 10
skillsaves:
  - athletics: 9
  - perception: 3
damage_resistances: "cold, lightning, thunder"
condition_immunities: "charmed, frightened, poisoned"
senses: "darkvision 60 ft., passive Perception 13"
languages: "Slaad (does not communicate)"
cr: 9
sim:
  abilities:
    - kind: periodic_effect
      trigger: start_of_turn_self
      effect: regen
      amount: 12
      suppressed_if_damaged_by: [fire, acid]
    - kind: periodic_effect
      trigger: start_of_turn_others
      effect: damage
      dice: "1d6"
      damage_type: poison
traits:
  - name: Foul Miasma
    desc: "Otar exudes a 10-foot radius of noxious fumes — the byproduct of a stalled caste transformation. The area is lightly obscured. Creatures other than Otar that start their turn in the miasma take 4 (1d6) poison damage."
  - name: Entropic Regeneration
    desc: "Otar regains 12 hit points at the start of its turn if it has at least 1 hit point. If Otar takes fire or acid damage, this trait doesn't function at the start of its next turn."
  - name: Legendary Resistance (2/Day)
    desc: "If Otar fails a saving throw, it can choose to succeed instead."
  - name: Magic Resistance
    desc: "Otar has advantage on saving throws against spells and other magical effects."
  - name: Unstable Form
    desc: "When Otar is reduced to half its hit points (68 HP) or fewer, its skin splits and weeps iridescent fluid. Its melee attacks deal an additional 2d6 acid damage, and any creature that hits it with a melee attack within 5 feet takes 9 (2d8) acid damage."
actions:
  - name: Multiattack
    desc: "Otar makes five attacks: one Bite attack, three Claw attacks, and one Tongue Lash attack. It can replace the Tongue Lash attack with a fourth Claw attack."
  - name: Bite
    desc: "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) piercing damage. On a hit, the target must succeed on a DC 16 Constitution saving throw or be infected with a Slaad egg (Slaad Tadpole disease — no immediate effect; 3 months to manifest)."
  - name: Claw
    desc: "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 12 (2d6 + 5) slashing damage."
  - name: Tongue Lash
    desc: "Melee Weapon Attack: +8 to hit, reach 40 ft., one target. Hit: 10 (1d8 + 5) bludgeoning damage, and the target must succeed on a DC 16 Strength saving throw or be pulled up to 35 feet toward Otar and grappled (escape DC 16). Otar can grapple one creature this way at a time."
  - name: "Chaos Pulse (Recharge 6)"
    desc: "Otar slams both fists into the ground. Each creature within 20 feet must make a DC 16 Dexterity saving throw. On a failure, a creature takes 22 (4d10) force damage and is knocked prone. On a success, a creature takes half damage and isn't knocked prone. Rubble and debris in the area become difficult terrain."
reactions:
  - name: Rubble Surge
    desc: "When a creature Otar can see moves more than 15 feet in a single turn while within 30 feet of it, Otar can use its reaction to hurl a chunk of plaza rubble. The target must succeed on a DC 16 Dexterity saving throw or take 11 (2d10) bludgeoning damage and have its speed reduced to 0 until the end of its current turn. This reaction can target flying creatures."
legendary_actions:
  - name: ""
    desc: "Otar can take 1 legendary action, choosing from the options below, only at the end of another creature's turn. Otar regains its spent legendary action at the start of its turn."
  - name: Lash
    desc: "Otar makes one Tongue Lash attack."
  - name: Thrash
    desc: "Otar thrashes violently. Each creature within 5 feet must succeed on a DC 16 Strength saving throw or be pushed 10 feet and knocked prone."
  - name: "Bile Spray (Costs 2 Actions)"
    desc: "Otar vomits a 15-foot cone of caustic bile. Each creature in the cone must succeed on a DC 16 Constitution saving throw or take 14 (4d6) acid damage. With only 1 legendary action/round, this effectively takes Otar two full rounds to save up for."
  - name: "Spawn Tadpoles — suppressed in Phase 1, reachable in Phase 2"
    desc: "Otar's rotting hide splits open, spilling 1d4 slaad tadpoles (see [[slaad-tadpole]]) — his general kit's option when fought alone. Costs 2 legendary actions, which his reduced 1/round pool can no longer reach in Phase 1; he's already flanked by 5 [[minor-slaad|minor slaad]] there anyway (further along the same molt Otar's own hide sheds, narrated as slaad tadpoles that already fed on the sewer's grung dead) — the escort fills this trait's role instead. Once [[Phase 2]]'s Rattle Surge restores his 3/round legendary economy, the cost is reachable again, and Phase 2's own calibration prices it in — the engine can't spawn a combatant mid-fight, so the spawned brood is fielded from the opening instead, 2 tadpoles standing in for the 1d4."
```

**Retuning (canon corrected 2026-07-24).** The statblock is truth. This prose drifted and was re-tuned for Session 07, then again on 2026-07-25 for `combat-sim v6.4.0`. The combat primer shows the adventurers punch 1 to 2 CR above normal; focus fire, save-stacking, and holds have made every fight through Session 04 easy. The original CR 8 build undertuned that.

Session 07 opens Otar alongside 5 [[minor-slaad]] companions, tadpoles already fed on Grung dead and further along their molt. The DM wanted action pool, so tuning Otar down offsets that.

[[Phase 1]] and [[Phase 2]] track this CR 9 build's current tuning as the fight develops.

**Design intent.** Foul Miasma (2d6 poison/turn) taxes melee range without punishing ranged groups, while Tongue Lash (30-ft hold plus pull) counters ranged kiting. Regeneration (12 HP/round, fire or acid only) demands fire or acid to stop it, blocking fast kills. Chaos Pulse punishes bunching. Legendary actions are quick and dumb, using Lash to pull creatures in and Thrash to clear melee, with Bile Spray punishing bunching. Lair actions stem from the unstable plaza, not Otar's cunning, making the fight feel like managing a crisis instead of outsmarting a commander. Each round on Otar matters because it's one round the extraction at the four secondary sites continues running, and the real boss is the clock.

**Behavioral profile.** Otar opens standing where Solange was, disoriented and newly embodied, and Tongue Lashes the nearest creature to pull it into melee. If 3+ creatures bunch within 20 ft, he opens with Chaos Pulse instead. At 68 HP (half), his Unstable Form starts, though he never retreats, yields, or reasons, just fights until dead. He is a brute hazard, chaotic, more obstacle than opponent. If the fight runs easy, he targets the townsfolk to force movement. Otherwise he lets the adventurers focus-fire and may Tongue Lash a PC into the crater for bad positioning. If the adventurers split early, he pursues the nearest target for 2 rounds before losing focus and attacking the townsfolk through chaos. If the adventurers have Heroes' Feast active (skipped the long rest), they have more buffer and [[the Rattle]] (below) becomes less likely to show.

**Weakness (fire/acid):** stopping regeneration is the key. Fire or acid ends the healing cycle. Without them, the adventurers grind against 135 HP as Otar heals big chunks each round. Otar's Bile Spray deals acid, and a splash near him stops his regeneration. Fire that stops regeneration early keeps the clock from doubling.

**The trapped townsfolk & the clock:** 2d6 injured townsfolk lie trapped in rubble within 30 ft of the crater. Otar attacks them if no PC blocks him, dealing d6 damage per round (1 or 2 hits each). Foul Miasma harms them too. Every round here is one the extraction elsewhere gains, with screams from [[Bridge]] after round 3 and smoke from [[le-paludi]] after round 5. Adventurers must choose: finish Otar or save people.

**Death:** when Otar dies, all lair actions stop (both his and the Rattle's). He does not dissolve. He falls into the rubble, bleeding fluid, thirty feet of dead outsider cooling in the plaza. The summoning circle stays faintly visible beneath. Someone brought this thing here on purpose and knew its name.


See [[Phase 1]] and [[Phase 2]] for terrain, DM pacing, and tuning info for this fight.

> [!mechanic]
> **Lair actions (the shattered plaza):** Not controlled by Otar. The ground ruptures. On turn count 20 (losing ties), one occurs (never repeat):
>
> - **Aftershock.** Creatures on the ground within 15 ft of the crater edge: DC 15 Dex save or fall prone.
> - **Choking Dust.** A 15-ft-radius sphere becomes obscured until turn count 20 next round.
> - **Masonry Collapse.** One creature within 40 ft: DC 15 Dex save or take 11 (3d6) bludgeoning and become stuck (escape DC 15).

The Warren's alarm fires when the fight tilts toward total loss.

> [!mechanic]
> **The Rattle (the [[Warren]] fights beside you):** The Warren's alarm system as action pool. When the fight tips toward TPK, the adventurers gain lair actions and an epic-action pool mirroring Otar. **Trigger:** two PCs down, OR adventurer HP below 25%, OR the DM reads forming TPK. Starts turn 20 next round. Stays until Otar falls. Does not kill Otar. Refuses to let adventurers lose. Each round the Warren gives **two** adventurer lair actions (turn 20, right after Otar's, DM or adventurers pick, no repeats): **[[Human]] Chain** (frees one prone/buried/stuck/grappled PC, half speed toward crater, no opportunity attacks); **Fire Brigade** (add 1d6 fire to one hit, suppresses Otar's regen next turn); **Din of Pans** (Otar: DC 10 Wisdom save or loses one epic action). Adventurer epic pool contains 5 shared actions, spent one per turn, refreshing turn 20. **[[Colla]]'s Toss** (1 action; 2d4+2 HP or save to downed/hurt PC within 30 ft); **Shoulder In** (1 action; PC moves or Dodges); **[[Ruk]] Wades In** (2 actions; attacks or breaks a hold). Details: [[Phase 1]] and [[Phase 2]].

The fight shifts when the Rattle joins.

> [!mechanic]
> **Rattle Surge (Phase 2 only):** The instant the Rattle triggers, Otar's epic pool jumps from 1 to 3 per round. This is the baseline restored, not invented. He doesn't react to the crowd smartly. The fight feels feral. At 3 actions per round he does Thrash and Bile Spray every round. Bile Spray escalates to 4d6-5d6 acid. Spawn Tadpoles (below) becomes reachable. This gives adventurers a new, urgent problem. Note: `combat-sim` v1 doesn't score the new tadpole combatant. Details: [[Phase 2]] § Challenge Calibration.

His worst ability opens in Phase 2.

> [!mechanic]
> **Spawn Tadpoles (the brood underfoot).** New epic action (2 LA cost): Otar sheds a clutch of [[slaad tadpoles]] from his rotting hide. Cheap and cheap. But a tadpole that drops a creature to 0 HP doesn't just leave a body. That creature risks transforming into a [[minor-slaad]] under Otar's control. It's the same fate Solange suffered, scaled down. Use it reactively like other epic actions (never a targeting decision). When a PC goes down near Otar, this becomes the real clock. Allies have three rounds to pull the body clear or make a Medicine check. After that, it's not a body anymore. It's another combatant.

## Connections

- [[solange-barret]]. Otar appears through her body. The ritual consumes her when complete, not kills her.
- [[simone-tabarnack]]. Contracted the summoning. Never appears on site.
- Calveno. The Beffa Grung Raid. The operation the summoning anchors.
- [[Calveno Sewer Magazines]]. The primary detonation chamber and summoning circle.

- [[jean-claude-tabarnack]]. Ragnetto never targets him.
- [[Warren]]. Floods the plaza with the Rattle if the fight turns to TPK.
- [[a-sliver-of-the-unstable-form]]. A fragment of his healing flesh from the crater.

## Session Log

**Session 06** (`vault/episodes/006/`). Manifested at the session's close when [[solange-barret|Solange]] completed the ritual in the Primary Chamber, spoke "Agni," and detonated the ceiling, beginning Otar's change. Described in play as becoming "a 12-foot-tall monster," the fight continues into the next session.

**Session 07** (`vault/episodes/007/`). Fight resumes in the [[Mercatura]] plaza crater. Otar stands 12 ft tall, red hide weeping fluid. His wounds heal on their own. Play confirms the regeneration.

Five slug-like creatures the color of Otar's own hide claw loose from the rubble and scatter toward the crowd. One catches and starts eating a trapped villager. Its body looks more and more [[Human]], an early Spawn Tadpoles sighting. Play confirms Foul Miasma deals automatic poison damage to anyone starting their turn in the 10-ft radius.

> [!mechanic]
> **Tongue Lash (legendary action).** Hits [[delmar-fisk|Delmar]] for 11 bludgeoning, halved by Uncanny Dodge, without landing the hold. Hits [[crissdalynn-khinriss|Crissdalynn]] next; she deflects the full 11 damage and tries to bounce it back, but Otar dodges its own tongue.
> **Ground slam.** DC 16 Dexterity save, everyone within 20 ft: 25 force damage, half on a save.

Transcript

Killed in the Calveno crater after [[master-kyzil|Kyzil]] answered [[delmar-fisk|Delmar]]'s whistle and cut down 5 [[minor-slaad]] with his daggers. The town's Rattle woke too, with townsfolk banging pots and pans and throwing lamp oil as the adventurers used the shared action pool.

Delmar threw the final blow, flying in to swing the recovered chair into Otar's throat before shooting him in the eye. Otar fell into the rubble and rotted, leaving a small scrap of paper in the corpse that nobody has read yet. Source: Transcript.
