---
type: pc
subtype: combat-profile
pc: "catarina-davirelli"
pc_level: 5
last_session_data: "none"
last_simulated: "2026-07-25"
sim_seed: 1
sim_version: "6.3.0"
confidence_level: "theoretical"
updated: "2026-07-25"
summary: "Level 5 Artillerist Artificer. Ranged blaster with 13.91 sustained DPR vs AC 15. AC 16/HP 38. Concentration-focused with weak melee fallback."
tags: [combat]
uid: 75cb1602-1085-482a-a3f3-0a79b818e85c
---

## Fast Read

Ranged blaster (INT) · sustained DPR 13.91 vs AC 15 `[simulated]` · nova DPR 28.0 vs AC 15 (p95) `[simulated]` · effective HP 38 raw, AC 16 `[sheet]` · Achilles heel: flat CON +5 concentration save (no War Caster) — grapplers and reach attackers break her focus; toughest matchup [[vashu-the-weeping-veil|Vashu, the Weeping Veil]] (Winded), 50.4% win `[simulated]`.

## Combat Stats

| Stat | Value | Lane |
|---|---|---|
| AC / HP | 16 (Breastplate) / 38, 5d8 hit dice | `[sheet]` |
| Init / Speed | — | `[sheet]` |
| Hit% vs AC ladder | [[fire-bolt\|Fire Bolt]]/Shocking Grasp/[[scorching-ray\|Scorching Ray]]/Cannon +9: 85/75/65/55% vs AC 13/15/17/19, 5% crit. Flintlock Pistol +3 `[verify]`: 55/45/35/25%, 5% crit | `[simulated]` |
| Save bonuses (weak → strong) | STR +1, WIS +1, CHA +0, DEX +2, CON +5, INT +8; concentration flat CON +5 | `[sheet]` |
| Resource pools (per rest) | Eldritch Cannon ×1, Infuse Item ×2 items, 1st-level slots ×4, 2nd-level slots ×2 (Scorching Ray/Shatter/[[catapult\|Catapult]]) | `[sheet]` |

`node utils/scripts/combat-sim/cli.mjs profile vault/campaigns/shattered-sea/pcs/character-sheets/catarina-davirelli-sheet.md --seed 1`

Damage/round ([[fire-bolt|Fire Bolt]] + Flintlock Pistol, the sheet's declared routine): mean 15.94/13.91/11.95/9.89 at AC 13/15/17/19, p95 29.0/28.0/27.0/25.0, max up to 56 `[simulated]`. Eldritch Cannon, [[scorching-ray|Scorching Ray]], and [[shatter|Shatter]] carry real damage dice but sit outside the routine, so they don't appear in this table — they do spend resources in full-kit encounter sims: 39.5 dmg / 4.84 resources vs [[aboleth|Aboleth]] (4.5 rounds), 9.9 dmg / 1.13 resources vs [[adult-black-dragon|adult-black-dragon]] (1.3 rounds), 0.1 dmg / 1.97 resources vs [[adult-blue-dragon]] (1.3 rounds) `[simulated]` — her 3 deadliest 1v1 losses (§ Counters & Synergy).

Enemy hit chance vs her AC (before Shield, which adds +5 but isn't folded in): 50% vs +5, 60% vs +7, 70% vs +9. Attacks survived vs +7: 12.2 (5 dmg/hit), 6.1 (10), 4.1 (15), 3.0 (20) `[simulated]`.

Not modeled: [[heat-metal|Heat Metal]] (no re-trigger primitive), [[tashas-caustic-brew|Tasha's Caustic Brew]] (no per-turn damage-over-time primitive), [[tortoise-shell|Tortoise Shell]] (no flat-AC-set primitive), Eldritch Cannon's Protector temp-HP/statblock (no persistent-summon primitive), Infuse Item (no combat-facing primitive). Modeled with caveat: [[grease|Grease]] (only initial save models), [[false-life|False Life]] (flat 9 temp HP, no per-slot scaling), Aid (bonus to [[catarina-davirelli|Catarina]] only, scales per slot), [[blur|Blur]] (fails vs Blindsight/Truesight), [[magic-weapon|Magic Weapon]] (+1 damage, caster-only), [[absorb-elements|Absorb Elements]] (no 1d6 retaliatory rider), [[thunderwave|Thunderwave]] (push + object damage model, outside routine).

## Counters & Synergy

Hard counters: grapplers/reach attackers break concentration `[theoretical]`; [[aboleth|Aboleth]], [[adult-black-dragon|Adult Black Dragon]], [[adult-blue-dragon|Adult Blue Dragon]] — 0% win, 1.3–4.5 rounds `[simulated]`. Soft counters: range denial, no-spell zones `[theoretical]`; Vashu (Winded) 50.4%, [[vampire-spawn]] 53.3%, [[the-rattle-statblock]] 54.2%, [[winter-wolf]] 54.9%, [[owlbear]] 55.7% `[simulated]`. Non-counter: surprise ([[alert|Alert]] blocks it).

Amplifies: whole party via advantage spell (costs a real slot, no longer free) — [[shocking-grasp|Shocking Grasp]] denies reactions `[theoretical]`. Depends on: frontline support to protect her concentration.

## Session Combat Log

Not yet played (see `vault/campaigns/shattered-sea/pcs/catarina-davirelli.md` Session Log). Append session, encounter, dmg dealt, dmg taken, hits/attacks, note once she's at the table.

## Calibration

Simulated-vs-observed delta: none yet, 0 sessions `[theoretical]`. Confidence: mechanical/simulated figures reproducible at stated seed; all observed data `theoretical` (`confidence_level: theoretical` unchanged). Unsimulable: no `--loadout` spell-nova run exists — Scorching Ray/Cannon full-kit ceiling is above the routine-only DPR table above.
