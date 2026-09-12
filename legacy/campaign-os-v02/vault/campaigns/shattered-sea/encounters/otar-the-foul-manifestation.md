---
type: encounter
status: pending
publish: false
aliases: ["Otar Phase 1", "Manifestation", "Otar Manifests"]
summary: "The Mercatura chamber's opening minutes. A freshly manifested, regenerating slaad hits the crew cold while a secondary extraction clock runs unchecked elsewhere."
created: 2026-07-30
updated: 2026-08-08
tags: [combat]
tier: core
campaigns: [Shattered Sea]
uid: 12227af0-137e-4438-bd66-fd57c32eec1d
---

# Otar the Foul: He Manifests

*Phase 1 of the Session 07 Otar fight. The crew has minutes, not a plan. A summoning circle finishes what a demolition charge started, and something climbs out of the crater already attacking. Hands off to [[otar-the-foul-the-rattle-answers|Phase 2: the Rattle Answers]] the moment its trigger below fires.*

## Opening

**Dramatic Question:** can the crew last long enough for the Rattle to answer?

Session resumes exactly where [[otar-the-foul|Session 06]] cut. Read the box below, then call the save under it before anything else resolves.

> [!read-aloud] Agni
> [[solange-barret|Solange]] is still kneeling at the circle's edge where you last saw her. She says one word into the chamber, *Agni*, and does not run.
>
> The ceiling answers her. A seam of orange opens across thirty feet of stone above the summoning platform, and the sound arrives half a beat behind the light.
>
> You are exactly where the last breath left you. Ahead lies the platform and its circle. Scaffolding stands twenty feet back along every wall. Trapped townsfolk are somewhere in the rubble to your left. Nothing sits between any of you and that ceiling worth calling cover.
>
> Then the whole of it comes down at once.

<!-- -->

> [!check] Dexterity Save — The Ceiling Comes Down
> DC 15, every party member rolls. 4d6 fire and bludgeoning damage, half on a success.
> **Success:** dust and burning debris scatter around you, singed but upright.
> **Failure:** the blast throws you off your feet, prone in the wreckage when it settles.

<!-- -->

> [!mechanic] Perrin-Only Vision Timing
> Perrin-only contact, held inside the same instant as the save above. No time passes at the table or in-world for anyone else. Resolve this vision, then the [[charisma|Charisma]] save below, before revealing any [[dexterity|Dexterity]] save results.

<!-- -->

> [!read-aloud] Perrin: one second, underwater
> The fire doesn't move like fire should. It hangs on its own leading edge, close enough to count the ember shapes twisting inside the orange, and everything past your held breath goes silent.
>
> Your knees go first. Then the chamber tips back and away, and behind your eyes something ancient turns to look at you instead.
>
> Cold water closes over you, dark and oppressive, threat flat against your chest like a hand. Something old moves through that darkness. A shell of ice grown from bone surfaces: thin as a held breath and hard as weapon-steel, radiating cold beyond measure. It burns whoever bites into it. It does not ask.
>
> Water drains away. The fire stands exactly as it stood, the same ember turning in the same place, neither advancing nor receding.

<!-- -->

> [!check] Charisma Save — Perrin: the Surge Answers
> DC 15, Perrin only, resolved at once after the vision and before any Dexterity save damage lands.
> **Success:** a wall of ice erupts between the crew and the blast, steaming until the explosion overwhelms it. Halve the fire damage every crew member takes from this explosion, applied after their own Dexterity save, rounded down.
> **Failure:** the surge doesn't answer in time. The explosion lands at full effect from the Dexterity save alone.

<!-- -->

> [!read-aloud] It Climbs Out
> Dust hangs thick over a thirty-foot crater where the summoning platform used to be. Scaffolding still stands along every wall, twenty feet back.
>
> At her feet, a shadow pools and closes into jaws around her. Three seconds, and she stops being a person. What climbs up from the rubble looks red, toad-skinned, and cracked along every seam, weeping something that catches the torchlight wrong. The air already tastes of rot and green fog, and one of the stuck bystanders is screaming from the rubble to your left.
>
> *(building)* It turns toward the sound, and the ground under it groans like it isn't finished falling.

Otar's own goal is plain: he is newly manifested, regenerating, and driven by instinct alone. Every round spent on him is a round the extraction runs unchecked elsewhere, and the summoning is already past the point of saving Solange.

## Enemy Roster

- [[otar-the-foul|Otar the Foul]]: solo boss at CR 9 and tuned for Session 07. HP 135, five attacks per round, 1 legendary action per round (full rationale on his own page). A brute and hazard driven by instinct, not strategy. A submerged predator surfacing already mid-attack, tasting the air with his tongue before every Tongue Lash, an unconscious tic he never notices. His full numbers, lair actions, and the crew's escape hatch (**the Rattle**) all live on his own page (quoted, not re-derived). [[jean-claude-tabarnack|Jean-Claude]] fights his own family's operation here (his sister [[simone-tabarnack|Simone]] contracted this exact summoning) while [[catarina-davirelli|Catarina]]'s kit (Ragnetto, Strix) is live from round 1 if she's personally arrived.
- 5 [[minor-slaad|Minor Slaad]]: slaad tadpoles that already fed on the sewer's Grung dead and molted further along than a freshly shed tadpole would (Otar's own stalled transformation seeded the rubble with them after Session 06). Real teeth, not fodder. They are the action-economy threat the DM wanted in the opening. This roster uses slaad and Grung (under the three-type cap).
- 2d6 injured bystanders stuck in rubble within 30 ft of the crater (hazard/objects, not [[enemy|enemy]] combatants). Otar attacks them if no PC is within his reach.

## Challenge Calibration

`combat-sim` Monte Carlo tests this exact roster (Otar + 5 Minor Slaad) against the five-PC crew (four core PCs plus [[catarina-davirelli|Catarina]]'s kit active from turn 1), fought to the death with no Rattle. The outcome: **45.4 to 48.8% crew win rate, 51.3 to 54.7% TPK, P(≥1 down) 90.6 to 91.7%, mean ~6.1 rounds** `[modeled, combat-sim v6.4.0, seeds 1/7/42, case s07-phase1-manifestation]`. This is **deadly**.

Read the TPK figure against what this phase truly does. The sim runs every fight to its end. The crew loses only if all drop. Win and TPK rates are opposites: a phase built to be *losable* cannot show low modeled TPK. The real death rate is in [[otar-the-foul-the-rattle-answers|Phase 2]], since Lowering the Stakes converts a forming wipe to Phase 2 when it forms. Solo play in Phase 1 is about a coin flip the crew loses more often, with someone going down in nine out of ten fights.

Dropping Otar to 0 is impossible here (nothing in the room can); the goal is to suppress his 12 HP/round regen where possible and keep the crew standing until [[the-rattle-statblock|the Rattle]]'s trigger fires. Every round spent otherwise costs bystanders and the secondary extraction sites dearly. This page owns Phase 1's own operative numbers (DCs, HP thresholds, phase triggers); [[scene-03-otar-manifests|Session 07, Scene 3: Otar Manifests]] embeds them from here and never restates them.

## Terrain

Room 8, the [[mercatura|Mercatura]] primary chamber is a ~60×50 ft irregular vaulted nexus with a 15 ft ceiling.

- **Drainage channels** converge from the cardinal directions, 3 ft deep (rising to 4 ft on round 3). These create difficult terrain. A prone creature inside has half cover. Small creatures are chest-deep (half speed, disadvantage on melee).
- **Central dry platform** has bright light 10 ft radius (expanding to 20 ft round 3), dim 10 ft beyond. The summoning circle sits here.
- **Scaffolding** reaches 10 ft along all walls, granting +2 AC vs. melee attacks from below. Ranged attacks ignore this cover.

> [!mechanic]
> **Lair actions: the shattered plaza.** Not controlled by Otar (the ground crumbles). On initiative count 20 (losing ties), one occurs, never the same effect two rounds running. **Aftershock:** each creature on the ground within 15 ft of the crater edge, DC 15 Dex save or fall prone. **Choking Dust:** a 15-ft-radius sphere becomes heavily obscured until initiative 20 next round. **Masonry Collapse:** one creature within 40 ft, DC 15 Dex save or take 3d6 bludgeoning. They escape at DC 15 or an ally frees them with an action. Full text quoted from [[otar-the-foul|Otar's page]]. These lair actions stay live into Phase 2 unchanged.

The blast already fired, and the room it left is the fight's floor plan. Rubble and difficult terrain cover the chamber throughout. A 30-ft crater sits open to the sky, while dust lightly obscures everything until initiative count 20 next round. Fire sources are salvageable from the wreckage too: [[torch|Torch]] racks, [[lamp|Lamp]] oil, alchemist's-fire debris, the crew's only lever against Otar's regeneration (see Raising the Stakes, below).

## Tactical Notes

Otar opens standing where Solange was, dazed and newly embodied. Tongue Lashes the nearest visible creature to pull it into melee, then closes (or uses Chaos Pulse if 3+ creatures cluster within 20 ft). At 68 HP (half), Unstable Form activates. Melee attacks gain +2d6 acid, while those who hit him in melee take 2d8 acid back. He has no morale and fights until dead. The 5 Minor Slaad companions have no plan and swarm whoever's nearest. If the fight runs too easy, Otar targets the bystander cluster to force repositioning or Tongue Lashes a PC into the crater for bad positioning. If the crew splits early, he chases the nearest target for 2 rounds, then turns on bystanders. Full behavior profile and design intent: [[otar-the-foul|his own page]].

## Run Sheet

### Foe Roster

| Foe | Init | AC | HP | Flees/breaks at | Action script |
|---|---|---|---|---|---|
| [[otar-the-foul\|Otar the Foul]] | +1 | 16 | 135/135 (regen 12/round unless blocked by fire/acid) | Never (no morale, fights to 0; the fight ends via Lowering the Stakes below, not his break) | Opens Tongue Lash on nearest visible target (Chaos Pulse if 3+ cluster within 20 ft). At 68 HP or less, Unstable Form live (attacks get +2d6 acid and inflict 2d8 acid back to melee attackers) |
| 5× [[minor-slaad\|Minor Slaad]] | +1 | 13 | 26/26 each | Never (no plan or morale; fight until dead) | Each swarms whoever's nearest without plan, using Bites and Claws |

### Round Script

- **R1:** Otar Tongue Lashes the nearest visible PC (Chaos Pulse if 3+ cluster within 20 ft). The 5 Minor Slaad claw free of the rubble and close on whoever's nearest.
- **R2+:** Otar's five-attack Multiattack (Bite, three Claw, Tongue Lash; swap the Tongue Lash for a fourth Claw) every round, plus 1 legendary action at the end of another creature's turn (Lash or Thrash most rounds; Bile Spray costs 2, so it's a two-round save). Minor Slaad keep piling onto whoever's already engaged. A lair action fires on initiative 20 (Aftershock, Choking Dust, or Masonry Collapse, never the same one twice running).
- **Trigger (round 3):** the platform's bright zone expands 10 ft to 20 ft, and the four drainage channels rise 3 ft to 4 ft deep.
- **Trigger (Otar at 68 HP or less):** unstable form activates.
- **Trigger (two PCs unconscious at once, OR party total HP below 25%, OR a forming TPK):** stop at once and move to Lowering the Stakes below.

statblocks: ![[otar-the-foul#Stats & Combat]] · [[minor-slaad|Minor Slaad]]

## Raising the Stakes

- **Trigger:** a PC digs a fire source free and lands a hit with it before initiative 20 next round. **Delta:** fire suppresses Otar's Entropic Regeneration (12 HP per round) until his next turn, the only real lever on his 135 HP total before the Rattle activates. [[crissdalynn-khinriss|Crissdalynn]] is most often free to try it. [[catarina-davirelli|Catarina]]'s Wand of Pyrotechnics is a second fire source once she's in range (still 2 to 3 turns out per her Enemy Roster note).

> [!check] Investigation — Digging a Fire Source Free
> DC 12 for a torch rack, DC 14 for lamp oil or alchemist's-fire debris (only two doses of the latter available).
> **Success:** the source comes free and the hit lands, suppressing Otar's Entropic Regeneration until his next turn.
> **Failure:** the source stays buried. Try again next turn.

## Lowering the Stakes

This dial is the fight's exit before it grinds the crew down further. The win rates behind it live in Challenge Calibration above, not here.

- **Trigger:** two or more PCs go down simultaneously. Stop too if crew HP drops below 25% or a TPK looks imminent. **Delta:** stop at once and hand off to [[otar-the-foul-the-rattle-answers|phase 2 (The Rattle Answers)]], which starts on initiative 20 the following round with its own tuning. Do not run another full round past this trigger.

## Endings

**Win:** phase 1 has no win condition of its own. Its goal is plain: nothing here can drop Otar to 0 (Enemy Roster, above). Reaching the Lowering the Stakes trigger without the crew going down first is the win. The instant it fires, hand off to phase 2 ([[moment-05-the-rattle-answers|The Rattle Answers]]), which carries the tools that close the fight.

**Defeat:** the system prevents a true TPK. A forming TPK is itself one of three Lowering the Stakes triggers, so a defeat spiral becomes Phase 2's handoff before it can finish. If a table plays past that call and Otar stands over a downed crew, he remains a disaster: he turns on the bystanders still stuck in the crater, and the raid at the four other sites finishes unchecked (the same numbers this page's own If Ignored section states: 200 to 300 captives taken, [[calveno|Calveno]]'s cost for the night).

**Disengage/flee:** Otar has no morale to punish a retreat, but nothing else stops for the crew. He turns on any bystander still in reach the moment no PC is near (Enemy Roster). The raid clock keeps running (screams from the [[the-bridge|Bridge]] district past round 3, smoke over [[le-paludi|Le Paludi]] past round 5. See Stakes below). The Rattle's trigger never fires without a crew in the room to read it against. A crew that walks away comes back to a Room 8 gone worse for every unchecked round. Otar does not leave the crater on his own.

## Stakes

Every round costs elsewhere: screams heard from the Bridge district by round 3 (a second strike point active), smoke seen over [[le-paludi|Le Paludi]] by round 5. Bystanders left alone in the crater take Foul Miasma poison damage and direct attacks if Otar has no PC in reach.

Standing notes: [[perrin-black-jaw|Perrin]] resists poison (Foul Miasma runs half-price on him). [[jean-claude-tabarnack|Jean-Claude]]'s [[hunters-mark|Hunter's Mark]] concentration is fragile under Otar's Multiattack and rarely lasts more than a round or two.

## If Ignored

> [!check] Arcana — Disrupting the Circle Before He Manifests
> DC 18 as an action, or 1 minute of careful work.
> **Success:** Otar never manifests. Solange detonates the ceiling as cover and escapes, reporting the primary site's compromise and a [[grung|Grung]] defector's involvement to [[simone-tabarnack|Simone]], who then knows [[jean-claude-tabarnack|Jean-Claude]] is alive and active.
> **Failure:** the ritual completes and Otar manifests as scheduled.

If the crew never reaches Room 8 at all, the detonation fires on schedule regardless. The plaza collapses, Otar erupts into the festival crowd unchecked, and all four secondary breaches open at once. Expect 200 to 300 captives taken if the raid runs unchecked end to end.

## Transition

- Lowering the Stakes trigger fires (two PCs unconscious at once, OR party total HP below 25%, OR a forming TPK). Hand off to [[otar-the-foul-the-rattle-answers|Phase 2 (The Rattle Answers)]], which starts on initiative 20 the following round with no elapsed time (the same fight continuing).

---

*How to read this page: [[runbook-reading-conventions]].*
