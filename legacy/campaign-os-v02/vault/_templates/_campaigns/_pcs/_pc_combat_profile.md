---
type: pc
subtype: combat-profile
owner_skill: ".claude/skills/combat-profiles/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality
pc: "{pc-slug}"
pc_level: {number: null}
last_session_data: {session number or "none": null}
last_simulated: "{date or 'never'}"
sim_seed: {number or "none": null}
sim_version: "{dndsim version or 'none'}"
confidence_level: "{high|medium|low|theoretical}"
updated: "{date}"
uid: af8c47c2-9d22-40b0-ad7c-e28f9a910f50
---

Five sections, in order. Every value tags its lane inline: `[simulated]`
(a `pnpm sim` run, seed + version in frontmatter), `[calculated]` (hand
math, no-script fallback only), `[session-NN]` (real table data).
Terse — a row or a clause per fact, never a paragraph.

## Fast Read

Role (3–5 words) · sustained DPR `[simulated]` · nova DPR `[simulated]` ·
effective HP `[calculated]` · Achilles heel (one clause).

## Combat Stats

| Stat | Value | Lane |
|---|---|---|
| AC / HP |  | `[sheet]` |
| Init / Speed |  | `[sheet]` |
| Hit% vs AC ladder |  | `[simulated]` |
| Save bonuses (weak → strong) |  | `[sheet]` |
| Resource pools (per rest) |  | `[sheet]` |

`npm run dndsim -- sim-combat` command that produced the simulated row goes on its own line
below the table. Any ability the sim run did NOT model: one line, named,
never silently absorbed into the DPR figure.

## Counters & Synergy

Hard counters (75%+ output reduction) and soft counters (25–75%), each
tagged `[observed]`/`[simulated]`/`[theoretical]`; what amplifies or
depends on this PC — one line each, mechanism named, no prose padding.

## Session Combat Log

Append-only table: session | encounter | dmg dealt | dmg taken |
hits/attacks | note. Record 0s honestly. Approximate figures get a `~`
prefix.

## Calibration

Simulated-vs-observed delta and why, in one line; confidence per data
category; unsimulable abilities the DPR figure doesn't capture, named.

Anti-patterns: `.claude/skills/combat-profiles/references/profiles.md`.
Loadout authoring and sim invocation:
`.claude/skills/combat-profiles/references/simulation.md` +
`utils/dndsim/CLAUDE.md`.
