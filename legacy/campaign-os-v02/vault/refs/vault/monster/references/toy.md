---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The creature Toy Chest's four fields — verb, unstable_condition, consequence, link_of_relevance — vocabulary and good/bad examples for mid-encounter draws."
created: "2026-08-03"
updated: "2026-08-07"
tags: [combat]
uid: 8d3be387-cb49-4313-bb65-e51c280557f9
---

# Toy Chest (four fields) — field-level examples

Write these once, as a markdown table in the DM-only material. No
frontmatter duplication — a second YAML copy of prose fields is a
sync-drift risk with no machine-readable payoff. One row per interactive
draw this creature offers a DM mid-encounter, never a vague "is
dangerous" line.

| Field | What goes here |
|---|---|
| `verb` | What a PC can do to or with this creature mid-encounter — a concrete action, not a trait. |
| `unstable_condition` | What state has to be true for that action to work — a condition the table can create or notice. |
| `consequence` | What actually happens as a result — observable, specific. |
| `link_of_relevance` | The PC-Connection Requirement's connection: which PC or campaign thread this creature's presence pulls on, wikilinked. Required — or the explicit DM scenery call. |

- `verb` — ✓ "Track its strike pattern across repeated hits." ✗ "Fight
  it."
- `unstable_condition` — ✓ "Three ships hit in the same reef break within
  a season." ✗ "It's been active for a while."
- `consequence` — ✓ "The party can predict its next likely target and
  stage an ambush." ✗ "Something happens."
- `link_of_relevance` — if you can't answer this in one sentence, the
  creature isn't ready to generate (The PC-Connection Requirement).

## What moved out of the Toy Chest

The table covers interactive draws only, not the whole creature. A
sensory tell that lets the table recognize this creature belongs in the
`> [!read-aloud]` callout or `## Description`; a repeatable behavior
pattern belongs in `## Ecology`; what it always wants and its current
disruption compress into the page's `**Wants:**` line
(`.claude/skills/draft-content/references/monster.md`).
