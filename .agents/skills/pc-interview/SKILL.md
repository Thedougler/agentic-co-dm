---
name: pc-interview
description: >-
  Conduct a human-started, one-question-at-a-time character interview and update one PC note
  from stated answers. Use for session zero, "interview my character", or filling gaps in an
  existing PC. Never invoke unprompted; never invent canon, combat math, or player choices.
disable-model-invocation: true
---

# PC Interview

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Identity and branch

Search `wiki/<campaign>/pcs/` and, only for collision checking, `wiki/<campaign>/npcs/` for name/aliases.
No match means create; one PC match means resume; an NPC match or ambiguity is a stop for identity
confirmation. Read the existing note and `hot.md` before asking. Store player handles only, never
real-player PII.

## Interview loop

Ask one question at a time, prefixing `Question N of 20.`; acknowledge briefly, avoid leading
follow-ups, and accept “Skip” while recording it unanswered. Cover, in order: name/call sign;
origin; family; formative change; proud choice; regret/obligation; value; temptation; fear;
desire; protector; distrust; authority; money/status/safety; worldview; misunderstanding; what
would make them leave; what would make them stay; a useful play detail; and a question they want
the world to ask. Then ask once for player handle and class/level if known. Leave unknown mechanics
blank and never fill `pc-state` from prose.

## Synthesize and persist

Map only stated answers into overview, appearance if supplied, gravity/tensions, relationships,
history, open hooks, and a dated `## Interview` round containing the questions actually asked and
answers as given. Preserve prior rounds. Link existing entities; do not mint NPC/item/place notes
inside the interview. Contradictions with protected canon are a DM gate, not a silent overwrite.
Do not set player audience, combat statistics, inventory, or unstated feelings.

Write one note in `wiki/<campaign>/pcs/`, run applicable Obsidian/frontmatter lint, and report
changed paths plus unanswered questions and deferred owner work.

## Campaign-bone gate

Use stated backstory to seed campaign bones, not to script outcomes. Extract who
wronged the PC, who they loved, who hunts them, and what they owe; turn those
facts into optional public stakes, relationships, and pressures that other
skills can make playable. Never force the PC to care, choose, forgive, or follow
one rail.

Before or during a Session 0 interview, confirm the table's tone agreement and
record only agreed tone/boundary information supported by the vault schema. A
cinematic promise must serve that agreement, not override it.
