---
type: pc
subtype: combat-profile
pc: "delmar-fisk"
pc_level: 5
last_session_data: "06"
last_simulated: "2026-07-26"
sim_seed: 1
sim_version: "6.4.0"
confidence_level: "medium"
updated: "2026-07-26"
summary: "Combat-simulation profile for Delmar Fisk built from real character sheet."
tags: [combat]
uid: 5a0e131b-01fc-4f8f-94d2-05d9b585c029
---

Built from the real character-sheet PDF. Save-bonus checkboxes are illegible; [[rapier|Rapier]]/[[musket|Musket]] attack stats remain unlisted (both `[verify]`).

## Fast Read

Mobile ranged/melee skirmisher — Sneak Attack (3d6) riding the Blunderbuss is the real damage engine, weapon dice secondary · sustained DPR 16.78 vs AC 16 `[simulated]` · effective HP 38 raw, AC 16 `[sheet]`, survives 4.4 expected +7-to-hit attacks at 10 dmg each `[calculated]` (Uncanny Dodge not included) · Achilles heel: solo alpha strikes before his first turn — [[aboleth|Aboleth]] (0% win, ~2.9 rounds), [[adult-black-dragon|Adult Black Dragon]] (0%, ~1.4 rounds), [[adult-blue-dragon|Adult Blue Dragon]] (0%, ~1.2 rounds) `[simulated]`; Withdraw/Steady Aim kiting tools unmodeled.

## Combat Stats

| Stat | Value | Lane |
|---|---|---|
| AC / HP | 16 / 38 max | `[sheet]` |
| Init / Speed | — | `[sheet]` |
| Hit% vs AC ladder | Blunderbuss +8 (incl. crit): 70/65/60% vs AC 15/16/17 | `[simulated]` |
| Save bonuses (weak → strong) | DEX +8, INT +3 `[sheet+srd, calculated]` per [[rogue\|Rogue]] table; rest `[unknown]`, checkboxes illegible | `[sheet]` |
| Resource pools (per rest) | Luck Points ×3 ([[long-rest\|Long Rest]]) | `[sheet]` |

`node utils/scripts/combat-sim/cli.mjs profile vault/campaigns/shattered-sea/pcs/character-sheets/delmar-fisk-sheet.md --seed 1`

Damage/round (Blunderbuss routine, Sneak Attack 3d6 once/turn + Lucky reroll built in): mean 17.93/16.78/15.66 at AC 15/16/17, p50 22.0/21.0/20.0, p95 35.0/34.0/36.0 `[simulated]`. Observed: one-shot kill via 1/1 [[pistol|pistol]] Sneak Attack on a purple-caste enforcer `[session-06]` — sample size 1, too small to average.

Not modeled: Cunning Strike's Withdraw (no movement-rider primitive), Steady Aim (no self-advantage-one-shot primitive), Fancy Footwork (no Opportunity-Attack mechanic), Weapon Mastery's Slow/Vex properties (no printed attack line for Musket/Rapier), Tavern Brawler (not relevant to real-weapon kit), Firearm Specialist's misfire reroll/free reload (no misfire mechanic), Luck's impose-[[disadvantage|Disadvantage]]-on-attacker half (only reroll-a-miss models).

Escape: [[winged-boots|Winged Boots]] (fly 30 ft), [[cloak-of-the-manta-ray|Cloak of the Manta Ray]] (swim 60 ft), both attuned. Uncanny Dodge (Rogue 5, reaction, halves one attack/turn) doesn't fold into the closed-form survived-count below — shows qualitatively in worst-matchup results instead. Expected attacks survived at +7: 12.2 (5 dmg) / 6.1 (10 dmg) / 4.1 (15 dmg) / 3.0 (20 dmg) `[simulated]`.

## Counters & Synergy

Hard counters: [[aboleth|Aboleth]] (0%, ~2.9 rounds), Adult Black Dragon (0%, ~1.4 rounds), [[adult-blue-dragon|Adult Blue Dragon]] (0%, ~1.2 rounds) — all one-shot him before his turn `[simulated]`. Soft counters: [[drider|Drider]] 50.2%, [[hydra|Hydra]] 51.1%, [[chuul|Chuul]] 51.7%, [[minotaur-of-baphomet|Minotaur of Baphomet]] 53.4%, [[half-dragon|Half-Dragon]] 55.2% `[simulated]` — better than the pre-real-sheet worst-5 ([[pirate-captain|Pirate Captain]], [[black-dragon-wyrmling|Black Dragon Wyrmling]], [[nightmare|Nightmare]], [[awakened-tree|Awakened Tree]], [[doppelganger|doppelgänger]], all 88–94% loss) due to real HP and weapon. No answer for: any solo monster with a first-round alpha strike clearing his 38 HP before his turn.

Amplifies: nothing modeled (no support features on the block). Depends on: isolated-target positioning for Rakish Audacity's no-[[advantage|Advantage]]-needed Sneak Attack clause (assumed always-on). Observed: [[catarina-davirelli|Catarina]] enchanted the Blunderbuss in S06 (+1 to-hit/dmg, self-loading) — figures assume post-enchantment.

## Session Combat Log

| Session | Encounter | Rounds | Damage dealt | Damage taken | Hits/attacks | Key moments |
|---|---|---|---|---|---|---|
| 06 | Primary Chamber fight | `[unknown]` | one-shot kill (purple-caste enforcer) | `[unknown]` | 1/1 pistol sneak attack | One-shot a purple-caste enforcer with a pistol sneak attack ("replaced with a pink mist"); resisted [[ozzeth-the-twiceborn\|Ozzeth]]'s [[dominate-person\|Dominate Person]] (natural 19 + Jean-Claude's Bardic Inspiration = 20); shot Ozzeth's arm off, setting up the kill; Catarina enchanted his blunderbuss mid-combat. Leveled up to Rogue 5 |

## Calibration

Simulated-vs-observed delta: one S06 kill-shot matches the sim range but is too small to average. Confidence: `medium` — real sheet is solid; one session's data and two `[verify]` flags (save checkboxes, Pistol to-hit) keep it from `high`. Unsimulable: Luck Points average spend 0.5/encounter against deadliest fights (0.52 vs Adult Black Dragon) `[simulated]`.
