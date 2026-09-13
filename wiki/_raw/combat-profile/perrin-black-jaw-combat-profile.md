---
type: pc
subtype: combat-profile
pc: "perrin-black-jaw"
pc_level: 5
last_session_data: 6
last_simulated: "2026-07-25"
sim_seed: 1
sim_version: "6.3.0"
confidence_level: "medium"
updated: "2026-07-25"
summary: "Level-5 Bard/Warlock support caster with 9.38 DPR, empirical counter profile, and observed role as party multiplier."
tags: [war, arcane]
uid: c7e0d8b4-de40-4c51-9170-036b4cec98f5
---

Built from [[perrin-black-jaw|Perrin]]'s actual level-5 D&D Beyond export ([[bard|Bard]] 3 / [[warlock|Warlock]] 2). His sheet does not carry [[vicious-mockery|Vicious Mockery]], [[command|Command]], or [[comprehend-languages|Comprehend Languages]].

## Fast Read

Support/control caster with a melee option — Bardic Inspiration is his key damage multiplier, not his own weapon; per his own page's Arc Notes, "the party's decisive force multiplier" · sustained DPR 9.38 vs AC 15 `[simulated]` · nova (p95, own kit, no ally grants) 18.0 vs AC 15 `[simulated]` · effective HP 49 `[sheet]` · Achilles heel: fragile frame, STR -2 with Mortis disadvantage, and a known tactical tell — [[master-kyzil|Kyzil]] named the drum itself as a target mid-spar (S04); deadliest 1v1 corpus opponent is Ruk, 56.4% win `[simulated]`.

## Combat Stats

| Stat | Value | Lane |
|---|---|---|
| AC / HP | 18 (incl. [[cloak-of-protection\|Cloak of Protection]] +1) / 49, 2d8 (Warlock) + 3d8 (Bard) hit dice | `[sheet]` |
| Init / Speed | — | `[sheet]` |
| Hit% vs AC ladder | [[longsword\|Longsword]] (Pact-bonded)/[[green-flame-blade\|Green-Flame Blade]]/[[eldritch-blast\|Eldritch Blast]], all +8, 5% crit: 80/70/60/50% vs AC 13/15/17/19 | `[simulated]` |
| Save bonuses (weak → strong) | STR -1 (Mortis disadvantage), INT +1, DEX +5, CON +3, WIS +4 (prof), CHA +9 (prof) | `[sheet]` |
| Resource pools (per rest) | Bardic Inspiration (shared w/ Cutting Words) ×5, Bard 1st-level slots ×4 ([[healing-word\|Healing Word]] draws here), Bard 2nd-level slots ×2, Pact Magic slots ×2, Pack Tactics reaction ×3 | `[sheet]` |

`node utils/scripts/combat-sim/cli.mjs profile vault/campaigns/shattered-sea/pcs/character-sheets/perrin-black-jaw-sheet.md --seed 1`

Damage/round, whole-turn under `optimal` auto-policy: mean 10.89/9.38/8.24/6.83 at AC 13/15/17/19, p50 12.0/11.0/10.0/0.0, p95 19.0/18.0/18.0/18.0, max up to 33 `[simulated]`. Observed DPR: effectively 0 across six sessions through S06, when he dropped to 0 HP (§ Session Combat Log) — reflects support/control play-style, not build weakness.

Not modeled: [[protection-from-evil-and-good|Protection from Evil and Good]], [[silent-image|Silent Image]], [[minor-illusion|Minor Illusion]], [[mage-hand|Mage Hand]], Magical Cunning (out-of-combat slot recovery), Bardic Inspiration granted to allies, Scurry positioning (no cross-combatant pool-grant primitive). Modeled with caveat: Hex's curses/ability-check disadvantage compile to flat extra damage (debuff-on-others not captured); [[armor-of-agathys|Armor of Agathys]] temp-HP/retaliation don't scale with higher slots, runs only at the slot level used. Green-Flame Blade's fire splash to a second creature models its level-5 primary-target rider. Now modeled by name via the spell library: Hex, [[hideous-laughter|Hideous Laughter]], [[eldritch-blast|Eldritch Blast]], Armor of Agathys.

Enemy hit chance: 40% vs +5, 50% vs +7, 60% vs +9, 70% vs +11. Attacks survived vs +7: 18.7 (5 dmg), 9.3 (10), 6.2 (15), 4.7 (20) `[simulated]`. Poison-damage sources: ~2× effective HP via resistance, plus advantage against poisoned/disease conditions. Escape/mitigation: boneless gives advantage escaping wrestling/restrained; Cutting Words subtracts 1d6 from an incoming roll (shared 5-die pool); Armor of Agathys grants 5 temp HP per Pact slot as a pre-fight buff.

## Counters & Synergy

Hard counters (observed): focus-fire on Perrin himself — Kyzil named the drum as a target (S04), removing him removes the party's Inspiration multiplier. Hard counters (theoretical): wrestling/shove attacks — STR -2 with disadvantage ends melee and nova lines. Soft counters: ranged focus (49 HP lasts ~3 rounds vs three +7 attackers), Stun and Chirr-class WIS saves (+4, middling), area damage (no Evasion). Non-counter: poison (resistance + condition advantage). No answer for: a focused attacker closing distance with no Shield reaction, flight beyond 120 ft, isolated high-CR solo threats.

Worst-5 empirical (1v1 solo, band-filtered): Ruk 56.4%, [[owlbear|Owlbear]] 58.3%, [[elder-mimic|Elder Mimic]] 58.5%, [[mummy|Mummy]] 59.9%, [[winter-wolf|Winter Wolf]] 62.6% `[simulated]`. True hard walls (0.0% win, 1–2 rounds): [[aboleth|Aboleth]], [[adult-black-dragon|Adult Black Dragon]], [[adult-blue-dragon|Adult Blue Dragon]].

Amplifies: the whole party via Bardic Inspiration — each d6 averages ~+2.6 on failed D20 Tests, flipping ~13% of misses; flipped Crissdalynn's failed wrestling contest (15+d6=20 vs Downburst) `[session-04]`; Cutting Words uses the same die against enemy rolls (vs Kyzil, insufficient, S04). Depends on: allies within 60 ft and available charges — his nova line depends on an ally advantage source ([[faerie-fire|Faerie-Fire]] or prone); without it, collapses toward the sustained mean. Observed: S03 spread 3 Inspiration pre-fight; S04 touched four pools in one combat (Healing Word ×2, Inspiration, Cutting Words). Simulated resource spend solo vs [[grung-elite-warrior|Grung Elite Warrior]]: 4.38/encounter `[simulated]` — pools drain on allies, not himself; bardic inspiration is most constrained, 2nd-level slots and pact magic least.

## Session Combat Log

| Session | Encounter | Rounds active | Damage dealt | Damage taken | Hits/attacks | Key moments |
|---|---|---|---|---|---|---|
| 01 | [[saltwright\|Saltwright]] boarding | `[unknown]` | `[unknown]` | `[unknown]` | `[unknown]` | Laid Minor Illusion over the hold doorway; emerged from a deck gap during the breach; resisted [[grung-npc\|Grung]] toxin gas (save passed, no number given) |
| 02 | Conflict aboard ship (vs. Ket) | `[unknown]` | 0 (drew Longsword, didn't attack. Crissdalynn intervened first) | `[unknown]` | 0/0 | Cast Tasha's Hideous Laughter to drop Ket safely instead |
| 03 | [[whip-shark\|Whip Shark]] fight | `[unknown]` | `[unknown]` | `[unknown]` | `[unknown]` | Spent 3 Bardic Inspiration (all three other party members). "Drummed through" the fight. No attack/damage numbers in the source |
| 04 | Kyzil spar + sewers | `[unknown]` | 0 (no attack recorded) | `[unknown]` | 0/0 | Healing Word ×2 (Delmar +7, Crissdalynn +8). Bardic Inspiration saved Crissdalynn's wrestling (15+d6=20 vs. Downburst). Cutting Words attempt vs. Kyzil's attack proved insufficient (failed). Kyzil called out the drum as a target |
| 06 | Primary Chamber fight | `[unknown]` | 0 (no attack recorded) | dropped to 0 HP | 0/0 | Failed death save reached his patron on the deathbed roll (15, needed 10+). Patron intervention allowed him to continue. He stabilized, coughing seawater at 1 HP. He leveled up to Bard 3 (College of Lore) and Warlock 2 (Pact of the Blade) |

> [!dm] Transcription note
> Every "damage dealt" cell above is 0 or `[unknown]`, not a transcription gap. The source simply doesn't record him landing an attack in 6 sessions.

## Calibration

Simulated-vs-observed delta: simulated sustained 9.38 vs AC 15; observed output ~0 over 6 sessions — reflects play-style, not build error. Encounter math should count Perrin as ~0 personal DPR, a defensive/offensive multiplier instead (his die keeps one martial ally functional roughly one extra round per fight). Confidence: mechanical/simulated lines use real sheet inputs, reproducible (high). Resource/synergy observations low confidence (2 sessions with numbers). Offensive observations theoretical (0 attack observations in 6 sessions). Unsimulable: the 18.0 nova figure requires ally advantage AND melee position — Kyzil showed melee as his danger zone, so read it as a low-confidence ceiling, not a table-typical line; cutting words, healing word, [[cure-wounds|cure wounds]], and the Pack Tactics reaction are now real schema primitives, no longer flagged unsimulable. Next data point needed: any session recording his actual attack rolls.
