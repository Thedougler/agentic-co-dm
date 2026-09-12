---
type: pc
subtype: party-combat-profile
owner_skill: ".claude/skills/combat-profiles/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality
party_level: {number: null}
party_size: {number: null}
last_simulated: "{date or 'never'}"
sim_seed: {number or "none": null}
sim_version: "{dndsim version or 'none'}"
confidence_level: "{high|medium|low|theoretical}"
last_compiled: "{date}"
uid: 898bd487-e4ec-4904-a811-6e8fa4f762a9
---

Compiled from every current `pc-combat-profile.md`. Five sections, in
order. Same lane tags as the PC template — `[simulated]` /
`[calculated]` / `[session-NN]`, never merged, terse throughout.

## Fast Read

Party size/level/tier · combined sustained DPR · combined nova (round 1)
· total effective HP · critical weakness (one clause) · Effective CR
Band (Trivial/Easy/Medium/Hard/Deadly), fidelity caveat if any PC's
combatant block is low-fidelity.

## Combined Combat Table

| PC | Sustained DPR | Nova DPR | AC / EHP | Save weakness |
|---|---|---|---|---|

Focus-fire potential (round-1 single-target burst, all PCs — the
minimum HP a solo boss needs to survive round 1) as one line below the
table.

## Weakness Map

Structural weaknesses (always present, severity, counter if any) and
what will TPK this party (one concrete scenario, sim-backed where one
exists) — one line each.

## Effective CR Band

One row per swept monster: monster | break-even count | win% | P(TPK) |
Effective CR scalar. Threshold-mapped band plus, on its own line, any
empirical session-evidence adjustment (simulated band always preserved
alongside it). Derivation:
`.claude/skills/combat-profiles/references/profiles.md` § Effective CR
Band.

## Encounter Design Parameters

Give-them / pressure-them / avoid / tuning knobs — one line each,
concrete.

**Staleness rule:** stale if any PC profile, combatant block, or party
loadout file changed after this page's `last_compiled`/`last_simulated`
dates — recompile before trusting it.
