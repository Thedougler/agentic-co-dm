
# Draft — Puzzle

A puzzle, trap, hazard, trial, or composite challenge — riddle, lock,
ward, environmental puzzle, mechanical trap, ongoing terrain danger, or
structured test of competence. Chain-load `writing-traps-trials` for the
craft workflow (steps 1–11); this guide owns the repo integration.

Covers all challenge forms under one `type: puzzle` page — a `subtype:`
key (`puzzle | trap | hazard | trial | composite`) tells them apart;
everything else is structurally identical: a surface players perceive,
a hidden mechanism only the DM knows, paths to interact with it, and
consequences for getting it wrong.

A trivial one-off DC bullet inline in a dungeon room's Features list
(`.claude/skills/draft-content/references/location.md`'s dungeon subtype, Phase 4) stays
there — it never earns its own page; this guide is for an obstacle worth
reusing, revisiting, or handing off. Unsure which → ask the DM rather than
defaulting to inline.

## Template

`vault/_templates/_srd/_puzzle.md` — copy it, never retype it from
memory. Exactly these H2s, in this order: `## At a Glance`,
`## Surface` (with `### Immediate`, `### Investigation`,
`### Mastery`), `## DM Truth`, `## Interaction`,
`## Consequences & Escalation`, `## Bypasses & Exploits`,
`## Rewards & Discoveries`, `## Aftermath`, `## Scaling Knobs`. No
Player-Known/DM-Only heading split (`.claude/skills/composing-beats/references/runtime-surface.md`
§8): `## Surface` carries the narration embed, `## DM Truth`
carries the `[!mechanic]` truth, `## Surface`/`## Interaction`
carry `[!check]` callouts, and any standing hazard rule in
`## Consequences & Escalation` carries `[!mechanic]` —
`publish:`/`status:` gates visibility, not the heading.

## Read first — before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `vault/refs/vault/_common/hard-rules.md` — the shared rules bind
   this type, never restated below.
3. `vault/refs/vault/_common/queries.md` — run the stub check now:
   `grep -ril "<puzzle/trap name or concept>" vault/ vault/campaigns/shattered-sea/pcs/`
   and `grep -rl --include=transcript.md -i "<name>" vault/episodes/`. A
   hit → expand that page in place, never duplicate. Empty output is
   informative, not conclusive — escalate through `llm-wiki-query`'s tiers
   first.

`DP1: <three files read, stub-check output pasted>`.

## Hard rules — this type only

- **Bypass Required.** Finishing with no no-roll solution in
  `## Bypasses & Exploits` -> stop — every puzzle or trap needs a
  bypass reachable by reasoning or preparation, not just a check to fail.
- **Classify Honestly.** Setting `subtype` -> `puzzle` (reasoning solves
  it), `trap` (triggers on its own), `hazard` (environmental danger),
  `trial` (structured test), or `composite` (two or more forms) — never
  leave the template placeholder.
- **Cite The Table, Don't Invent.** A DC, damage die, or severity from
  vibes -> read `vault/refs/table-random-traps.md`'s Damage Severity and
  Save DC tables or `vault/refs/gameplay-toolbox-traps.md`'s Traps
  section, and cite the tier.
- **Every Check Has Two Outcomes.** A `[!check]` with only one outcome ->
  stop — every check needs a success and a failure line, and the failure
  states its cost (`.claude/skills/callouts/references/check.md`).
- **Redundant Conclusions.** Gating progression on one hidden conclusion
  with no redundancy -> run the Three-Clue Rule
  (`.claude/skills/composing-beats/references/audits.md` §3) before finalizing.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- Puzzle, trap, hazard, trial, or composite (subtype)? What room,
  dungeon, or item is it attached to?
- Which PC does this pull on, and how
  (`.claude/skills/composing-beats/references/runtime-surface.md` §2 — a pure-mechanic obstacle is
  still a DM call, never a default)?
- What's the real mechanism — the DM truth the party is working against?
- Target difficulty/severity for the party's level?
- Does failure need to be survivable, or is this meant to actually stop
  the party?

## Before you ship

Lifecycle `vault/refs/vault/_common/lifecycle.md` · gaps
`vault/refs/vault/_common/degrade.md` · handoffs
`vault/refs/vault/_common/handoffs.md` · boundaries
`vault/refs/vault/_common/out-of-scope.md` · then
`vault/refs/vault/_common/checklist.md`.

## Cross-skill coordination

- **A dungeon room's own trap/puzzle, complex enough for its own page** →
  `.claude/skills/draft-content/references/location.md` links here instead of inlining it;
  this guide never authors the room itself.
- **A trap embedded mid-fight** → `encounter-prep`'s Terrain section links
  here for anything reused or complex; a genuine one-off hazard stays
  inline on the encounter page.
- **A locked or warded item** → `.claude/skills/draft-content/references/item.md` owns the
  item page; this guide covers the lock/ward mechanism only if it's
  complex enough to reuse or detach from the item itself.

## Out of scope

- NPCs, locations, factions, items, encounters, and random tables — their
  own drafting guides.
- A trivial inline room-feature trap (see above).
- Writing `vault/campaigns/shattered-sea/puzzles/` past `status: pending`,
  or flipping `publish:` — ingest's and PUBLISH's move exclusively.

## Owned paths

`vault/campaigns/shattered-sea/puzzles/<slug>.md` — `status: draft` while
assembling, `status: pending` once table-ready, edited in place from
there. Never `status: canon` or `publish: true`
(`transcript-ingest`'s and PUBLISH's exclusive moves).
