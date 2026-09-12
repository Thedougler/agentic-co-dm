# Chassis and budget

Use these as a transparent calibration worksheet. The peer dossier wins when a current public benchmark contradicts a broad heuristic. Write assumptions beside every result.

## Core formulas
Start from an official numerical peer. When none fits, use these community-derived first-pass estimates (not official rules; validate against published peers):

- **AC or save DC:** about `12 + half CR` through CR 16.
- **Hit Points:** about `15 + (15 × CR)`.
- **Attack bonus or proficient check:** about `4 + half CR`.
- **Damage per round:** about `5 + (7 × CR)`.
- **Number of attacks:** add attacks around CR 2, 7, 11, and 15; divide total damage among them.
- Above CR 16, compare directly to current official peers — simple formulas diverge.

Also use:
- **PB:** table below (do not import a PC level PB by accident).
- **Save DC (ability-built):** `8 + PB + relevant ability modifier` when building from ability scores rather than the peer shortcut.
- **Average damage:** dice averages (`d4 2.5, d6 3.5, d8 4.5, d10 5.5, d12 6.5`) plus modifiers.
- **Three-round DPR:** script uses × expected damage × hit/failed-save probability; include reactions, recharge (test one-use and two-use for Recharge 5–6), legendary/off-turn, auras, ongoing, summons, and monster-controlled environment. Prefer Multiattack over one enormous attack at moderate/high CR.
- **Area budget:** estimate realistic targets (start with ~2); raise for forced grouping, huge cones, or restrained targets; reduce per-target damage when many will be hit.
- **Effective HP:** model resistance, regeneration, temp HP, healing, avoidance, and immunity against the actual party damage mix.

## PB by rank/CR
| Rank/CR | PB |
|---|---:|
| 0–4 | +2 |
| 5–8 | +3 |
| 9–12 | +4 |
| 13–16 | +5 |
| 17–20 | +6 |
| 21–24 | +7 |
| 25–28 | +8 |
| 29–30 | +9 |

Use a peer check at band edges; rank is a target, not proof of balance.

## Trade rules
1. Pick the intended role and one signature payoff before selecting numbers.
2. Give one strong axis (offense, defense, mobility, control, or support), one support axis, and at least one exploitable weakness.
3. If AC rises above peers, reduce HP, damage, control, or endurance; if broad resistance or immunity appears, make it narrow, bypassable, temporary, or costly.
4. A hard control effect trades against damage, range, frequency, target count, or save reliability. A reaction and a bonus action are not free if both compete for the same turn.
5. Do not stack elite HP, legendary resistance, high saves, broad immunity, regeneration, and escape without adding player targets and clear costs.

## Three-round offense script
| Round | Record | Audit question |
|---|---|---|
| 1 | opening tell, setup, movement, action, recharge | Does the signature appear without an ambush-only assumption? |
| 2 | best likely repeat, target selection, reaction/off-turn use | Is the monster still making a meaningful choice? |
| 3 | payoff, phase, recharge variance, retreat or escalation | Does the total match peers before the fight is likely over? |

Calculate expected damage/control for the script, then compare with two peers. Include miss chance, saves, partial effects, resistance, target count, ally enablement, and likely party response. A routine action should not rely on ideal maximum target count.

## Defense checklist
Check AC and attack avoidance; HP; effective HP by common damage types; saves and save coverage; magic resistance-like features; immunities; regeneration/healing; temporary HP; concealment/cover; movement and escape; legendary resistance; concentration or recharge dependencies; and whether the party has a fair bypass. Add a tell or resource cost when a defense changes the encounter answer. Blank is safer than “immune to everything relevant.”

## Packages
- **Standard:** one action loop, one signature, one reaction or recharge if needed, ordinary defenses, clear weakness.
- **Elite:** roughly two meaningful jobs per round through a reaction, recharge, bonus action, or limited off-turn response; add a phase or lightning rod before simply multiplying HP.
- **Solo:** reliable off-turn actions, multiple target pressures, movement/terrain interaction, phase or bloodied transition, and a way to remain interesting when surrounded. Audit the party number of turns.

## Legendary/off-turn rules (SRD 5.2.1)
Each Legendary Action expends one use, occurs immediately after another creature's turn, and all uses return at the start of the monster's turn. Default: 3 uses; 2–4 options (move, basic attack/pressure, one limited control/area). Rate-limit the strongest option until the start of its next turn. Do not use 2014 variable-cost LA unless the user asks. Budget legendary damage and control into the three-round audit. Reactions answer player choices; they are not free extra turns.

## Action-oriented villain phases
Give each phase a goal, tell, changed decision loop, player answer, and exit condition. A phase may alter terrain, summon a lightning rod, trade defense for offense, or expose a weakness. Telegraph transitions; avoid a full heal unless the encounter has a clear cost and the three-round audit includes it.

## Bloodied transitions
If used, define bloodied as half HP or state the different threshold, make the transition observable, and spend it on a new choice rather than hidden punishment. Recalculate remaining expected rounds after the transition. A bloodied effect should create a player response, not erase a turn or invalidate prior choices.
