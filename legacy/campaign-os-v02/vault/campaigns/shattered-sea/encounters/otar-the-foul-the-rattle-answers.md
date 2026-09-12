---
type: encounter
status: pending
publish: false
aliases: ["The Rattle Answers", "Rattle Surge", "Otar Phase 2"]
summary: "The Rattle triggers at the fight's low point. The Warren answers with its own lair actions and legendary pool, and Otar the Foul falls for good."
created: 2026-07-30
updated: 2026-08-08
tags: [combat]
tier: core
campaigns: [Shattered Sea]
uid: a27e9a38-5249-4774-8c78-3c564704c309
---

# Otar the Foul: The Rattle Answers

*Phase 2 of the Session 07 Otar fight. Picks up the instant [[otar-the-foul-manifestation|Phase 1]]'s trigger fires (two PCs downed at once, crew HP below 25%, or a forming TPK). No transition needed. This is the next thing that happens.*

## Opening

**Dramatic Question:** does the crew land the finishing blow on Otar before Rattle Surge and the acid bleed-back grind them down first?

> [!read-aloud] The Rattle Begins
> One pan sounds past the crater's lip, flat and hard, and a second answers it, then a third, until the beat is coming from every direction at once. Kitchens, cart wheels, window ledges, it all lands on the same rhythm.
>
> The crowd that scattered from the blast comes back over the crater's broken rim, carrying whatever they grabbed in the last few minutes, and a jar of burning lamp oil arcs down to catch red hide square across the eyes.
>
> Forty feet back along the tunnel mouth, a line of stretcher-bearers is already forming.
>
> *(low, then rising)* Whatever this thing thought it had already won, that's over now.

## Enemy Roster

[[otar-the-foul|Otar the Foul]], the same solo boss, carries on from [[otar-the-foul-manifestation|Phase 1]] at whatever HP and shape he holds when the trigger fires. No restart, no reinforcements; by this point the 5 [[minor-slaad|Minor Slaad]] from Phase 1 are already down.

- **Rattle Surge.** The instant the Rattle triggers, Otar's legendary economy jumps from 1 action a round to 3. That is the pre-nerf baseline his own page's source note records, restored as written. He now affords Thrash and a full Bile Spray in the same round, every round.
- **Spawn Tadpoles** comes back into reach. Spend it the first round he drops under 68 HP. The brood is 1d4 [[slaad-tadpole|slaad tadpoles]], shed straight out of his splitting hide, priced into Challenge Calibration below.
- Otar himself has no idea this is happening. At the table it reads as the fight getting more feral, not more tactical.
- His own tic (tasting the air before Tongue Lash) carries over unchanged from Phase 1, the DM's cue for that attack. The Rattle's own voice is the pan-and-kettle rhythm itself, a hundred kitchens landing on one beat.
- His own page quotes his full baseline. The Phase-2 delta is calibration-only, in `vault/campaigns/shattered-sea/pcs/combat-profile/sim-variants/otar-rattle-surge-s07.md`.
- The crowd left standing (per Phase 1's outcome) arrives to help the crew and runs through the Rattle mechanics below instead of this roster.

## Challenge Calibration

- **With the Rattle running** (crew plus Rattle proxy versus Surge Otar at full 135 HP; worst case, trigger fired early, brood not shed): **76.6-77.5% crew win rate, TPK 22.4-23.4%, ~5.4 rounds mean** `[simulated, combat-sim v6.4.0, seeds 1/7/42, scenario s07-phase2-rattle]`.
- **With the brood standing too** (same roster plus 2 slaad tadpoles from the opening, a pessimistic read of a 1d4 clutch shed partway through): **58.6-60.9% win, TPK 39.0-41.4%, ~6.7 rounds mean** `[scenario s07-phase2-rattle-brood]`.
- **A realistic hand-off**, where Phase 1 already cost Otar a third of his HP, runs above **82%**.
- **Declining the Rattle's tools** (same roster, no proxy per the § If Ignored case below): **28.9-30.3% win, TPK 69.7-71.2%** `[scenario s07-phase2-surge-no-rattle]`.

That spread is the phase's whole design: the Rattle answering is worth roughly 48 points of win rate. It turns a fight the crew loses two times in three into one they win three times in four. Against [[otar-the-foul-manifestation|Phase 1]]'s own 45-49% (the same Otar, no crowd), the comeback runs on the numbers alone. Full rationale: `vault/campaigns/shattered-sea/pcs/combat-profile/sim-variants/otar-rattle-surge-s07.md`.

This page owns Phase 2's operative numbers (the DCs, HP thresholds, and phase triggers above), and [[scene-04-the-rattle-answers|Session 07, Scene 4]] embeds them from here instead of restating them.

## Terrain

The crater keeps [[otar-the-foul-manifestation|Phase 1]]'s physical space. Drainage channels, central platform, scaffolding, the lair-action table, and the fire-source DCs all carry over unchanged, with the full detail living on that page. New in Phase 2: the crater's edge is now a working lane, stretcher-bearers staged forty feet back at the tunnel mouth, and the crowd along the rim throwing whatever they grabbed on the way back.

## Tactical Notes

Otar's behavior doesn't change: he has no morale, doesn't retreat, and targets the same [[otar-the-foul-manifestation|Phase 1]] victims. Only his ceiling changes. Unstable Form is likely already active by the time this phase opens. Every melee hit the crew lands costs 2d8 acid back. This cost trades directly against the Rattle's own healing and repositioning tools below. Per Rattle Surge above, run him with 3 legendary actions a round, never 1, from the moment the Rattle triggers. Treat Thrash plus a full Bile Spray every round as the working baseline instead of an escalation saved for a bad round.

[[jean-claude-tabarnack|Jean-Claude]] and [[catarina-davirelli|Catarina]] hold position to land the finishing blow, the same Phase 1 ties carrying over (his family connection to the summoning, her kit's fire feeding Fire Brigade's regen-suppression below). [[delmar-fisk|Delmar]] and [[perrin-black-jaw|Perrin]] are the Rattle's default target for Human Chain, the crew's answer to exactly this go-down moment.

## Run Sheet

### Foe Roster

| Foe | Init | AC | HP | Flees/breaks at | Action script |
|---|---|---|---|---|---|
| [[otar-the-foul\|Otar the Foul]] | +1 | 16 | Carries over from [[otar-the-foul-manifestation\|Phase 1]] at whatever he's at when the trigger fires (Unstable Form, ≤68 HP, likely already live) | Never; no morale, dies only at 0 HP | Multiattack unchanged from Phase 1 (Bite, three Claw, Tongue Lash, swapping the 4th Claw). From the round the Rattle triggers: 3 legendary actions/round (Rattle Surge), not 1 |
| 1d4× [[slaad-tadpole\|Slaad Tadpole]] | +3 | 12 | 10/10 each | Never; mindless | Shed by Spawn Tadpoles (2 legendary actions) the first round Otar drops under 68 HP. Each bites whoever is nearest, and a PC it drops to 0 is the clock in Otar's own § Spawn Tadpoles note |

### Round Script

- **R1 (the round the Rattle triggers):** Otar's turn plays out unchanged from Phase 1. On initiative 20, [[moment-05-the-rattle-answers|the Rattle answers]] for the first time. The crew's lair actions (Human Chain, Fire Brigade, Din of Pans, never the same one twice running), the shared 5-point pool, and Otar's own lair action (Aftershock, Choking Dust, or Masonry Collapse, carried over from Phase 1) all fire on the same count. From here, the crew lands the finishing blow while the pool holds, suppressing regeneration with a Fire Brigade-boosted hit before a bad round burns through the shared pool without result.
- **R2+:** Otar's Multiattack plus 3 legendary actions a round (Thrash and a full Bile Spray, every round) against the Rattle's two lair actions and refreshing 5-point pool. Same cadence, every initiative 20.
- **At Otar under 68 HP:** his hide splits. Spend 2 legendary actions on Spawn Tadpoles and put 1d4 tadpoles on the board beside him.
- **At 0 HP with regen suppressed that round:** Otar falls (see Endings below).

statblocks: ![[otar-the-foul#Stats & Combat]] · [[the-rattle-statblock|The Rattle]]

## Raising the Stakes

- **Trigger:** the crew spends Fire Brigade (1 legendary-pool point) on a landed hit → **Delta:** that hit adds 1d6 fire and suppresses Otar's Entropic Regeneration until his next turn. The pool itself grants the fire source.
- **Trigger:** the crew spends Din of Pans on Otar's turn → **Delta:** Otar must succeed on a [[wisdom|Wisdom]] save (DC per [[otar-the-foul|Otar's page]] § The Rattle) or lose one legendary action next round, worth more now that Rattle Surge has him spending three a round instead of one.

Stacking both in the same round is what actually closes the gap between ~29-30% win (Rattle Surge alone, tools declined) and ~77% (Rattle Surge answered in kind).

## Lowering the Stakes

- **Trigger:** every round, initiative 20, right after Otar's turn → **Delta:** the crew gets two lair actions each round (Human Chain, Fire Brigade, Din of Pans, never the same one twice running). A shared 5-point legendary pool refreshes on the same count. This is [[the-rattle-statblock|The Rattle]], [[warren|The Warren]]'s own answer, already running since [[otar-the-foul-manifestation|Phase 1]]'s trigger fired. Full action list and numbers: [[otar-the-foul|Otar's page]] § The Rattle, not re-derived here. Don't withhold it: once triggered it runs at full strength every round, and the table spends it out loud.

## Endings

**Win:** [[otar-the-foul|Otar]] reduced to 0 HP with Entropic Regeneration suppressed that round. What his death actually stops, and what's left behind, is Stakes below.

**Defeat:** priced in, never designed out. Challenge Calibration's own numbers say 22-23% TPK with the Rattle's tools spent, ~70% if declined. Otar doesn't stop. The same aftermath [[otar-the-foul-manifestation|Phase 1]]'s own § If Ignored states for an unopposed raid applies here too. The extraction at the four secondary sites finishes, 200-300 captives taken, and [[calveno|Calveno]] pays for the whole night, not just this crater. The Rattle's own crowd (Opening box) doesn't disperse; it carries the news, and the dead, out of Room 8.

**Disengage/flee:** no clean disengage exists in this phase. Its opening trigger (two PCs down, total HP under 25%, or a forming TPK) means retreat abandons downed allies to a brute that still heals. Otar doesn't chase past the crater's edge (his tactical profile loses interest after 2 rounds and turns on bystanders instead), so whoever still stands can walk away. The fight goes unfinished, Otar on his feet and still healing in the middle of the plaza. The Rattle's crowd (Opening box) carries the downed clear instead of celebrating a kill.

## Stakes

Otar's death ends both his lair actions and the Rattle's, at once. He doesn't dissolve; he falls, thirty feet of dead outsider cooling in the middle of a [[tessarine-concordat|Tessarine]] trade plaza, the summoning circle still visible beneath the rubble. An open investigation hook into who built it and why stays live afterward: no [[grung|Grung]] built this circle, and someone paid for it.

## If Ignored

The crew may decline the Rattle's tools: treat its lair actions and pool as optional instead of spending them out loud. **Let it happen:** the Surge stays live regardless (that part isn't optional; the crowd turning out does it to Otar all on its own). A table that declines fights at **28.9-30.3% win, TPK 69.7-71.2%** `[simulated, combat-sim v6.4.0, scenario s07-phase2-surge-no-rattle]`, a fight they lose more than two times in three. Nothing forces a table to spend the pool, and nothing catches them quietly when they decline.

## Transition

- Otar falls (Win, above) → [[scene-05-the-factors-debt|Session 07, Scene 5, The Factor's Debt]], the moment the crowd catches its own breath. No elapsed time; the crater's immediate aftermath (crowd, stretcher-bearers) is already in the Opening box above.

---

*How to read this page: [[runbook-reading-conventions]].*
