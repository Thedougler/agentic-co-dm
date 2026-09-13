---
type: pc
subtype: combat-profile
pc: "crissdalynn-khinriss"
pc_level: 5
last_session_data: "06"
last_simulated: "2026-07-25"
sim_seed: 1
sim_version: "6.3.0"
confidence_level: "medium"
updated: "2026-07-25"
summary: "Level 5 Kensei Monk combat profile: 5.70 DPR vs AC 15, AC 17 baseline, seize-and-carry specialist."
tags: [combat]
uid: 2f342d74-2c95-42e2-a83e-c91d307f383e
---

Built from the real character sheet (`crissdalynn-khinriss-sheet.md`).

## Fast Read

Mobile skirmisher (melee/ranged), Kensei and fists (35 ft walk, 45 ft fly `[sheet, verify]`) · sustained DPR 5.70 vs AC 15 `[simulated]` · nova (with ally [[faerie-fire|Faerie Fire]] advantage) 7.84 vs AC 15 — upper bound, not re-run this cycle `[simulated]` · effective HP 35 `[sheet]` · Achilles heel: flat +0 CHA/INT saves, no Evasion until level 7 — near-certain loss vs any adult dragon 1v1 (0.0% win, TPK ~1.2–1.5 rounds) `[simulated]`.

## Combat Stats

| Stat | Value | Lane |
|---|---|---|
| AC / HP | 17 baseline (Unarmored Defense), +2 with Agile Parry (after Unarmed Strike) / 35 | `[sheet]` |
| Init / Speed | 35 ft walk, 45 ft fly `[sheet, verify]` | `[sheet]` |
| Hit% vs AC ladder | [[quarterstaff\|Quarterstaff]]/[[shortbow\|Shortbow]]/Talons +7: 65/55/45% vs AC 15/17/19. Unarmed Strike (incl. Flurry) +8: 70/60/50% | `[simulated]` |
| Save bonuses (weak → strong) | CHA +0, INT +0, CON +1, WIS +3, STR +4, DEX +7 (proficient) | `[sheet]` |
| Resource pools (per rest) | Ki (Focus): 5 per short or long rest | `[sheet]` |

`node utils/scripts/combat-sim/cli.mjs profile vault/campaigns/shattered-sea/pcs/character-sheets/crissdalynn-khinriss-sheet.md --seed 1`

[[damage|Damage]]/round, full routine ([[combat|combat]]-sim v6.x, quarterstaff action + unarmed/Flurry bonus, auto-policy decides Flurry/Stunning Strike spend): mean 5.70/4.88 at AC 15/17, p95 12.0/12.0, max 20 `[simulated]`. Auto-policy spends ki on Flurry every round it can — an upper bound, since the model doesn't value conservation; ki is the constrained pool, shared across Flurry, Patient Defense/Step of the Wind, Stunning Strike, and Deflect Attacks' redirect.

Not modeled: read the Current (info rider only), [[grappler|Grappler]]/Tavern Brawler's Punch-and-Grab/Push riders, Slow Fall (fall damage only), Kensei's Shot's 1d4 bonus (ranged only, conflicts with Flurry), Wind Caller's [[gust-of-wind|Gust of Wind]] (no push-shove primitive).

Deflect Attacks (reaction): reduces a Bludgeoning/Piercing/Slashing hit (melee or ranged) by 1d10+9 `[sheet]`.

> [!mechanic]
> **Deflect Attacks (redirect).** Spend 1 ki: deal 2d8+4 damage of same type to a creature within 5 ft (melee) or 60 ft (ranged). DC 14 DEX save to avoid.

Escape: 45 ft fly `[sheet, verify]`, seize-and-carry plays (unmodeled).

## Counters & Synergy

Hard counters: AoE CHA/INT saves (both +0) cause removal; enclosed spaces with Restrained `[theoretical]`. Any adult dragon (Black/Blue/Brass) 1v1 — 0.0% win, TPK ~1.2–1.5 rounds `[simulated]`. Soft counters: WIS saves for stuns/fear (+3), ranged fire (Deflect Attacks covers both) `[sheet]`. Worst-5 vs statblock corpus (none catastrophic, all Deadly band): [[night-hag\|Night Hag]] 52.7%, [[incubus\|Incubus]] 54.8%, [[xorn\|Xorn]] 57.1%, [[ghost\|Ghost]] 59.4%, [[succubus\|Succubus]] 66.0% `[simulated]`. No answer for: AoE saves — Evasion comes at level 7.

Amplifies: none modeled. Depends on: an ally's concentration for advantage — [[catarina-davirelli|Catarina]]'s Faerie Fire (+2.12 DPR vs AC 15 `[simulated]`), open vertical space for seize-and-carry. Observed: seize-and-move as signature control `[session-04]`; seized and killed [[vashu-the-weeping-veil|Vashu]] in melee `[session-06]`.

## Session Combat Log

| Session | Encounter | Rounds | Damage dealt | Damage taken | Hits/attacks | Key moments |
|---|---|---|---|---|---|---|
| 04 | [[master-kyzil\|Kyzil]] spar ([[ponte-bassa\|Ponte Bassa]] roof) | ~3 | ~13 redirected | ~13 deflected + fall | `[unknown]` | Seized Kyzil R1 (his natural 1); Deflect + redirect; fell to Downburst |
| 04 | Sewer patrol [[grung-npc\|Grung]] | ~2 | `[unknown]` | 0 noted | `[unknown]` | Clotheslined patrol Grung. 45-ft Kingfisher dive-seize on fleeing purple. Poison shrugged (Hero's Feast) |
| 06 | Primary Chamber (Vashu, [[solange-barret\|Solange]], Grung) | `[unknown]` | `[unknown]` | 11+10 (two Still-Water Strikes, down to 1 HP) | `[unknown]` | Deflected Vashu's Tongue Lash twice (once redirecting onto a Grung). Took two Still-Water Strikes to 1 HP. Killed Vashu in melee. Seized and poisoned Solange before her teleport |

## Calibration

Simulated-vs-observed delta: no numeric session data logged yet, session log uses narrative accounts. Confidence: `medium` — sheet stats solid `[sheet]`, DPR/EHP `[simulated]`, not table-validated. Unsimulable: the Faerie-Fire nova figure (7.84) predates the current spell-library concentration/action-cost model — read as an upper bound, not a fresh run.
