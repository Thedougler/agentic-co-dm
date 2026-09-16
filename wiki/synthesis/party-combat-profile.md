---
title: "Party Combat Profile"
aliases:
  - Party Combat Profile
category: synthesis
tags: [shattered-sea, lore]
sources:
  - "campaign-os:party-combat-profile.md"
created: 2026-09-13
updated: 2026-09-13
type: lore
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "Party of 4 level-5 PCs. Closed-form 52.61 combined sustained DPR vs AC 15, 65.08 round-1 nova, 328 effective HP vs a +6 attacker. Effective CR Band unmeasured — the sim is unusable."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Party Combat Profile

## Fast Read

Party of 4, all level 5 (tier 2). Combined sustained DPR vs AC 15:
**52.61** `[calculated]` (Delmar 18.13, Crissdalynn 12.63, Jean-Claude
11.60, Perrin 10.25) — at-will routines only, no limited
resources spent. Round-1 nova, everything burning: **65.08**
`[calculated]`. Total effective HP vs a +6 attacker: **328**
`[calculated]`, before any reaction mitigation. Critical weakness:
CHA/INT saves are close to unprotected across all four PCs, and the
remaining concentration caster saves flat. **Effective CR Band:
`[unknown]`** — it derives from party-vs-monster sweeps and the
combat-sim engine is not trusted at this compile; the empirical band
below carries the load instead.

Fidelity: Jean-Claude's block is a `[theoretical]` RAW Ranger 5 kit, no
player sheet on file. `[verify]` Crissdalynn's block declares no Extra
Attack, which a Monk 5 has by RAW — her figures below are one attack
light if the sheet is wrong.

## Combined Combat Table

| PC | Sustained DPR | Nova DPR | AC / EHP | Save weakness |
|---|---|---|---|---|
| Delmar | 18.13 (Blunderbuss +8, [[Sneak Attack]] 3d6 always-on) | 18.13 (no round-1 burst beyond the routine; Lucky rerolls unmodeled) | 16 / 69 | WIS +1, STR +0 |
| Crissdalynn | 12.63 (Quarterstaff +7, bonus Unarmed +8) | 19.50 ([[Flurry of Blows]], 1 Focus Point) | 17 / 70 | CHA +0, INT +0 |
| Jean-Claude | 11.60 (2× +1 Silent Shortbow +9) | 17.20 (+ Dreadful Strike 2d6, 2/long rest) | 16 / 80 | CHA -1, INT +0 |
| Perrin | 10.25 ([[Green-Flame Blade]] +8) | 10.25 ([[Hex]] costs round 1's bonus action; 12.88 from round 2) | 18 / 109 | STR -1, and disadvantage on STR (Mortis) |

`[calculated]` throughout, closed-form against AC 15 for damage and a +6
attacker for EHP, crits at 5% doubling dice. Reaction mitigation sits
outside the EHP column and is not summed into it: Delmar halves one hit
per round ([[Uncanny Dodge]]), Crissdalynn takes 1d10+9
(avg 14.5) off one hit per round (Deflect Attacks), Perrin subtracts
1d6 from a roll five times per long rest (Cutting Words). All three
raise real survivability well above the printed EHP.

Focus-fire potential (round-1 single-target burst, all four, no
advantage bought): **65.08** `[calculated]` — a solo boss needs more
than 65 HP to survive round 1 against a clean focus.

## Weakness Map

Structural: CHA and INT saves are unprotected — Crissdalynn +0/+0,
Jean-Claude -1/+0, Delmar +2/+3; only Perrin's CHA +9 resists a charm
line, and he alone cannot cover the party. Severity high, no counter in
the party's current kit. Concentration runs through Perrin at +3 — a
single focused hit drops [[Hex]]. Perrin's STR save is -1 with
disadvantage on top, so grapples and shoves land on him almost at will.
Party WIS averages +2.25, so a WIS-save AoE stun chain-disables the
back line.

What will TPK this party: a legendary solo with two or more legendary
actions per round that opens on the casters, or any encounter that
wins initiative and lands a WIS-save AoE before Perrin can spend
Bardic Inspiration — the party's damage is heavily back-loaded into
Delmar and Crissdalynn's melee lanes and collapses when those two are
controlled rather than damaged. Unquantified this compile: no sweep
data backs a specific count.

Confirmed synergy (session-cited): Perrin flips ally saves via Bardic
Inspiration (S04 restrain escape). Jean-Claude's Bardic-Inspiration-
boosted save resists [[Ozzeth]]'s
[[Dominate Person]] via Delmar (S06).
[[Healing Word]] and [[Cure Wounds]] sustain
the party (S04) `[session-04, session-06]`.

## Effective CR Band

`[unknown]` this compile. The band derives from `--sweep-count` runs of
each season-relevant monster against the whole party, and the
combat-sim engine is not trusted at this compile — no sweep figure is
recorded rather than record one that cannot be reproduced.

Empirical band (separate lane, `[session-NN]` evidence only): sessions
through S06 show the party punching roughly 1–2 CR above standard —
the DM raised [[otar-the-foul]] to CR 12 on that basis,
and S06's Primary Chamber fight killed [[vashu-the-weeping-veil|Vashu]]
and Ozzeth and held [[solange-barret|Solange]]. Working band until a
sweep replaces it: CR-2 squads safe to 6–7 bodies; CR-5 solos safe to
3–4 (Hard at worst); one legendary solo winnable, two beyond reach.
`[low confidence]` — five sessions of qualitative evidence, no
measurement.

## Encounter Design Parameters

Give them: clustered melee targets for focus fire — the party's 65-point
round-1 burst is its best trick and it wants bodies inside Crissdalynn
and Delmar's reach. A flank to protect activates the lockdown play both
have shown at the table. Pressure them: CHA- or INT-save effects
(charm, banishment, psychic domination), a grappler on Perrin, and
initiative — this party is far more fragile to a lost first round than
its HP total suggests. Avoid: poison leverage on Perrin (resistant), and
small squads with no control tools, which this party deletes. Tuning
knobs: control density and initiative order move this party's odds most,
not HP or AC — a monster that lands one save-or-suck on the back line
changes the fight more than one with 20 more HP.

**Staleness rule:** stale if any PC profile, combatant block, or party
loadout file changed after this page's `last_compiled`/`last_simulated`
dates — recompile before trusting it.
