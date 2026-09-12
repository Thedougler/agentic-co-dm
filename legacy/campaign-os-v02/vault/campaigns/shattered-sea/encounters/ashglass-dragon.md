---
type: encounter
status: pending
publish: false
title: ""
aliases: []
summary: "A solo young red dragon defends its caldera lair and molten-slag hoard on Ashglass — a genuinely lethal fight for a level-5 party."
created: "2026-08-08"
updated: "2026-08-08"
tags: [combat, exploration]
tier: supporting
campaigns: [Shattered Sea]
uid: 3c805981-970d-4730-b930-134c78fd1829
---

# Ashglass Dragon

*A territorial young red dragon holds the caldera floor and its molten-slag hoard against anything that climbs the rim — and it has never lost.*

## Opening

**Dramatic Question:** Does the party leave Ashglass with the hoard, or does the dragon add them to the wreckage on the slope?

> [!read-aloud]
> The rim gives way to a bowl of black glass maybe eighty feet across, its floor still radiating heat you can feel through your boots. At the far side, a mound of slag glitters — gold and gem-glints fused into rock that never fully cooled, forty feet off. Steam-thin cracks vent along the near wall, hissing without pattern. And coiled across the top of the hoard mound itself, head low, wings half-folded, is the young red dragon — awake, watching your rim-line silhouettes, and already breathing out through its nostrils in a slow curl of smoke. It hasn't moved yet. It doesn't need to.

## The Toy

| Field | Value |
|---|---|
| `primary_goal` | Prove that a single, patient apex predator can out-scale a full party's action economy — numbers don't automatically win a fight. |
| `consistent_method` | Holds the high ground on the hoard mound; opens with Fire Breath the instant two or more targets cluster within its cone, then closes to Rend whoever's already hurt, never repeating a target while a fresher one stands. |
| `active_problem` | The dragon has already killed every salvage crew that's climbed the rim; their gear and remains litter the slope below as unread evidence, and its territory has gone uncontested long enough that it no longer expects a real fight. |
| `performance_hooks` | Vibe: a kaiju that doesn't roar until the fight is already lost for someone. Tic: it never strikes the same target twice in a row once that target bleeds — it wants everyone to have been hurt before anyone dies. |
| `link_of_relevance` | Open-world side content — DM-confirmed no PC-specific connection; the party's stake is whatever they decide the hoard/rumor is worth. |
| `terrain_shift` | The first successful Fire Breath or a dragon wing-buffet (round 2 or later) kicks a standing ash cloud across whichever zone it lands in — see § Terrain. |
| `objective` | Not strictly kill-everything: claiming any part of the hoard and retreating counts as a win, same as dropping the dragon outright. |

## Enemy Roster

- **Young Red Dragon** (solo boss, role: Bruiser with an Artillery burst) — [[young-red-dragon|Young Red Dragon]], reused directly, no reskin to its math. Tactical personality for this fight: **Territorial** — attacks anything on the caldera floor or hoard mound, does not give chase past the rim.

![[young-red-dragon#Stats & Combat]]

## Challenge Calibration

**Level 5 (current party).** `[simulated, combat-sim v6.4.0, seed 1]` — `pnpm sim sim-combat party vault/srd/monsters/young-red-dragon.md --seed 1` against the real party (Perrin, Catarina, Delmar, Crissdalynn, Jean-Claude, all level 5): **40.4% win** (95% CI 38.5–42.3%), **P(≥1 PC down) 78.1%**, **P(TPK) 59.6%**, mean rounds 4.0, mean party HP loss 77.2%. Effective Difficulty Rating: **Deadly** (fires on P(win) < 0.75, P(≥1 down) > 0.5, and P(TPK) ≥ 0.05 — all three trip). Effective CR scalar 0.92 — this single dragon sits almost exactly at the party's break-even point, i.e., a coin-flip TPK, not a safe "hard" fight. The sim's own difficulty-ladder search confirms this reading: reaching even an achievable "Deadly" band (81% win) requires *weakening* the dragon (HP 178→160, −1 flat damage, breath recharge floor +2) — the dragon as printed is harder than the top of that ladder. Primary driver of lethality: the breath weapon's recharge floor (weakening it alone would swing P(win) by +9.5%), consistent with `party-combat-profile.md` naming any adult-dragon-class breath/save-heavy solo as this party's structural weak point (Crissdalynn and the casters carry the worst individual matchups against dragon-type threats). This is the DM-approved calibration: genuinely lethal, not a soft "Deadly-on-paper" fight.

**Level 8–10.** `[theoretical]` — no level 8–10 PC sheets exist in this repo to simulate directly, so this reading falls back to the standard baseline (`combat-calibration.md` § Procedure) rather than an empirical sim. Lazy Encounter Benchmark: a solo monster is deadly at 5th+ level when its CR ≥ 1.5× average character level. At level 9 (mid-band), that threshold is CR 13.5 — this dragon's CR 10 sits under it, landing around Hard rather than Deadly by the formula. Average party HP scales roughly from `(level×7)+3` per character — level 5 ≈ 38/PC (194 total, matching the real party's actual total HP) to level 9 ≈ 66/PC (~330 total) — while the dragon's own damage output (Rend, Fire Breath) doesn't scale with the party's level at all. Net read: at level 8–10 this fight should cost real resources and can still down a PC on a bad breath save, but the party's HP and action-economy cushion should absorb a loss without the near-coin-flip TPK risk the level-5 sim shows. Re-run the sim once level 8–10 PC sheets exist rather than trusting this extrapolation past that point.

## Terrain

Two zones, extending [[ashglass|Ashglass]]'s own upper-slope hazards into the lair itself rather than inventing new ones:

- **Caldera Floor** (the open approach, ~40 ft. across). Broken ash-and-glass ground underfoot; a mound of jagged slag near the rim wall offers half cover to anyone who reaches it.

  > [!mechanic]
  > **Unstable footing.** Any creature moving at more than half speed across this zone must succeed on a DC 12 Dexterity save or fall prone and slide 10 feet, taking 1d6 bludgeoning damage from the broken glass.

- **Hoard Ledge** (the raised mound the dragon holds, ~15 ft. higher than the floor). The hoard itself — fused gold and gem-glints — sits here; three unmapped heat vents ring its base.

  > [!mechanic]
  > **Heat vents.** A creature that comes within 5 feet of a vent without first spending a turn testing the ground triggers it: every creature within 10 feet takes 2d6 fire damage, half on a successful DC 13 Dexterity save. Vents recharge after 1 minute and give no warning before they first trigger.

  > [!mechanic]
  > **Ash cloud (terrain_shift).** The first Fire Breath that connects, or any wing-buffet from round 2 on, kicks a standing ash cloud across the zone it lands in. That zone becomes heavily obscured until the end of the encounter; any creature that starts its turn there must succeed on a DC 13 Constitution save or spend its action coughing instead of acting.

## Tactical Notes

The dragon opens from the Hoard Ledge, using its elevation and the Caldera Floor's open ground to line up Fire Breath the instant two or more PCs stand within 30 feet of each other — it has killed enough crews to know clustered targets are the kill. Once its breath is on recharge, it drops to the Caldera Floor and closes with Rend, always finishing whichever target it last hurt before it moves to a fresh one (its tic, § The Toy). Being Territorial, it never leaves the caldera to chase a retreating party past the rim — the fight is winnable by disengaging, not just by outlasting it. It breaks off entirely only once badly hurt (Run Sheet flee threshold below), taking to the air and abandoning the hoard rather than pressing a fight it can no longer win outright.

## Run Sheet

### Foe Roster

| Foe | Init | AC | HP | Flees/breaks at | Action script |
|---|---|---|---|---|---|
| Young Red Dragon | +0 | 18 | 178/178 | ≤35 HP (~20%) | Opens with Fire Breath on the largest cluster in range; once on recharge, closes to Rend the most recently hurt target; takes wing and disengages entirely at the flee threshold |

### Round Script

- **R1:** Dragon holds the Hoard Ledge and uses Fire Breath (if two or more PCs cluster within its 30-ft. cone) or Multiattack Rend on the nearest PC if no cluster presents.
- **R2+:** Fire Breath on recharge (5–6) whenever it lines up two or more targets; otherwise Multiattack Rend, always finishing its last target before switching. Terrain_shift fires the first time breath connects or from round 2 on a wing-buffet — see § Terrain's Ash cloud entry.
- **Trigger — HP ≤35:** the dragon takes wing (Fly 80 ft.), disengages from melee without provoking, and does not return to the caldera floor this encounter.

Statblock: [[young-red-dragon|Young Red Dragon]] — quoted above in § Enemy Roster.

## Raising the Stakes

- **Trigger:** two or more PCs stand within 15 feet of each other for a second consecutive round → **Delta:** the dragon's next Fire Breath is guaranteed to catch every clustered PC in its cone (no positioning roll needed to line it up) — the volcanic heat radiating off the caldera floor also adds 2d6 to the breath's damage (16d6 → 18d6, DC 17 Dex half).
- **Trigger:** the dragon drops below 89 HP (50%) with no PC having retreated toward the rim → **Delta:** it takes to the air for two rounds, gaining a dive-bomb Rend (advantage on the attack roll from height) before landing back on the Hoard Ledge.

## Lowering the Stakes

- **Trigger:** a PC is reduced to 0 HP → **Delta:** the dragon's tactical personality shifts off that target immediately — it does not multiattack a downed PC again this encounter, turning instead to the nearest still-standing threat, buying the party a free turn to stabilize.
- **Trigger:** the party visibly retreats toward the caldera rim (any PC moves to leave the Caldera Floor or Hoard Ledge zone toward the exit) → **Delta:** the dragon does not pursue past the rim (Territorial personality) and forgoes any bonus-action or opportunity attack against the retreating PC.

## Endings

**Win:** the dragon is dropped to 0 HP or forced past its flee threshold and disengages for good. The hoard is accessible but still fused into the slag — nothing here specifies extraction time or tools; that's the party's next problem, not this encounter's.

**Defeat:** a PC or the whole party going down here goes down for real — no forced-retreat mechanic intervenes. If the dragon has no living threat left to prioritize, it finishes off anyone who hasn't stabilized before its next turn. A full TPK changes nothing about the island: the dragon returns to guarding its hoard, and the party's gear becomes the next crew's warning sign on the slope, same as every crew before them.

**Disengage/flee:** the party can break off at any point by clearing the caldera rim; the dragon (Territorial) does not give chase beyond it. Whatever ground, HP, and resources were already spent are lost, and the dragon keeps the hoard, unclaimed. Nothing about the island or the dragon changes — it's the identical lethal fight waiting the next time anyone climbs back up.

## Stakes

What's actually on the line: the fused gold-and-gem hoard on the Hoard Ledge, and nothing beyond it — no faction, no PC thread, no clock. Winning or claiming any part of the hoard is worth whatever the party decides treasure is worth to them; losing costs them exactly what they spent getting here (resources, HP, possibly PCs) and leaves the hoard untouched.

## If Ignored

Nothing changes. The dragon stays exactly where it is — no clock, no escalation, no expanding threat. If the party never climbs Ashglass, the island sits precisely as described on its own page, waiting for the next salvage crew foolish enough to try.

## Transition

- Dragon dropped or driven past its flee threshold, hoard claimed or left behind → [[ashglass-crater]], same day.
- Party disengages or flees before the dragon is beaten → [[ashglass]], same day.

---

*How to read this page: [[runbook-reading-conventions]].*
