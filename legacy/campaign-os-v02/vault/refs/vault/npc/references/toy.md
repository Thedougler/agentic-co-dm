---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The five NPC Toy Chest fields, what belongs in each, and the good/bad pair that shows the difference."
created: "2026-08-03"
updated: "2026-08-08"
tags: [intrigue]
uid: de21fdf7-6cd7-4435-b0dd-1ca7ae680dc7
---

# Toy Chest (the five fields)

Write these once, as a markdown table in the DM-only material. No frontmatter
duplication for these five fields — the npc template's only frontmatter key
is `location`, and a second copy of prose fields in YAML
is a sync-drift risk with no machine-readable payoff (unlike PC stats, which
`transcript-ingest` genuinely edits as YAML). One table, one source.

| Field | What goes here |
|---|---|
| `primary_goal` | What they always want — a vector, not a state. What they're moving toward regardless of the party. |
| `consistent_method` | How they pursue it — a gimmick, not a personality. Doable at the table in 5 seconds. |
| `active_problem` | The situation only, for this NPC, right now. Not their feelings about it, not their response to it. |
| `performance_hooks` | One real-world cultural shorthand you can inhabit instantly + one tic, verbal or physical. Nothing more. |
| `link_of_relevance` | The PC-Connection Requirement: which PC, and the specific mechanism. Required. One sentence, wikilinked to the PC's page. |

Field rules (the three universal ones are `.claude/skills/composing-beats/references/runtime-surface.md` §3; these are
the NPC-specific good/bad pairs):

- `primary_goal` — ✓ "Accumulate enough to retire before the audit."
  ✗ "Is ambitious."
- `consistent_method` — ✓ "Feigns helplessness, then names his price. Never
  in writing." ✗ Any analysis tacked on after the behavior — cut it.
- `active_problem` — ✓ "A dockworker witnessed his last handoff and is
  demanding money." ✗ "Is being blackmailed and feels cornered."
- `performance_hooks` — one vibe + one tic, nothing else, no explaining
  what the draw means. The tic may be physical rather than verbal, and a
  physical one has to be something the NPC is seen *doing* at the table:
  ✓ "wraps a mooring rope with one foot while he talks." ✗ "is dextrous
  with his feet." Write the action, never the conclusion the action would
  let a player draw — `vault/refs/stories/prose-and-character-craft.md`
  § NPC entrance, move 3. Blocking for the read-aloud paragraph still
  belongs there, not here.
- `link_of_relevance` — if you can't answer this in one sentence, the NPC
  isn't ready to generate (the PC-Connection Requirement).

## Optional pre-fill technique: image/competence/need/fixation

Before filling the table above, a quick concept-generation formula for an
NPC who should read as capable but flawed: public image + real competence

- one humiliating need + one petty fixation. Example: naval legend /
brilliant tactician / needs royal approval / obsessed with seeming younger
than a rival. Complements the Toy Chest rather than duplicating it — this
formula generates the concept; the five fields above still do the
table-ready behavioral work. Originates from the [Shattered Sea](vault/campaigns/shattered-sea/locations/shattered-sea.md) campaign's
tone doctrine (`vault/campaigns/shattered-sea/lore/shattered-sea-tone-guide.md`), which defaults
to it for every named NPC; any campaign can use it for a "competence
trapped in dysfunction" character.
