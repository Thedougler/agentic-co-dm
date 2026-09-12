---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The named quest structural patterns — Convergence Arc through the Three-Act default — and how to diagnose a stalled active quest."
created: "2026-08-03"
updated: "2026-08-15"
tags: [mystery]
uid: d7728ced-e1a9-4be7-a9c6-602bd92915ee
---

# Quest Structure Reference

Full pattern shapes and origins live in the canonical catalog, indexed at
`.claude/skills/draft-story/references/story-structures.md` (also cited in
`.claude/skills/composing-beats/references/composition.md`) — this file never restates a shape,
only how to operationalize it on a quest page. Every pattern below assumes
`.claude/skills/composing-beats/references/audits.md`'s core rule: plan the threads, and let
the collision emerge from what factions and PCs actually do.

## Convergence Arc

Shape: `.claude/skills/draft-story/references/story-structures-campaign.md` § Convergence Arc.

**Use when**: the quest's real content is several
`vault/campaigns/shattered-sea/factions/*.md` Fronts and PC threads already
heading toward the same place — not when tension needs inventing from
nothing.

**How to build it**: list each thread with its own timeline, in the DM
Only § Structural pattern notes:

```text
Thread: [[faction-slug#Front: Name]] — advancing per its own clock
Thread: [PC]'s draw — triggered by player action, no fixed timeline
Thread: world event — N sessions out
Convergence point: [where/when these overlap]
```

Let threads converge only once they've actually earned it — say so in the
Beats hand-off and hand off to `draft-story` (its DS4 step) to continue;
`world-update`'s clock advancement brings them together. If the party never
gets near the convergence, let the threads collide off-screen and surface
the aftermath as a Beat instead.

## The Slow Burn

Shape: `.claude/skills/draft-story/references/story-structures-campaign.md` § The Slow Burn.

**Use when**: the quest's payoff is a hidden identity or cause the party
should discover through pattern-recognition, not a single gated reveal —
this is the multi-session form of `.claude/skills/composing-beats/references/runtime-surface.md`'s
Three-Clue Rule.

**How to build it**: name 2–3 seed moments in the Beats hand-off (which
sessions, which NPCs/locations carry the seed) and the eventual payoff
condition. Let the payoff land whenever the party pulls the thread, per the
If-Ignored discipline (`.claude/skills/composing-beats/references/audits.md` §4) — if they
never do, the seed becomes world texture, not a dropped plot.

## The Escalation Ladder

Shape: `.claude/skills/draft-story/references/story-structures-campaign.md` § The Escalation Ladder.

**Use when**: a single objective needs to feel like it's actually
building, session over session, rather than flat difficulty scaling.

**How to build it**: state which rung the quest currently occupies in DM
Only, and what player action (or inaction) pushes it up a rung. Anchor the
top rung to a specific PC or place named in `link_of_relevance` — "the
world is at stake" fails If-Ignored's tick test unless it's also *this
PC's* home, ship, or person at stake.

## Parallel Threads

Shape: `.claude/skills/draft-story/references/story-structures-campaign.md` § Parallel Threads.

**Use when**: this quest is genuinely one of several the party could
pursue, and its own advancement (or stalling) needs to stay visible even
while they're elsewhere — `.claude/skills/composing-beats/references/audits.md`'s Ticking
Clock applied at quest scale, not a new mechanic; cite that section rather
than re-deriving the "advances whether or not observed" rule.

**How to build it**: a one-line "current state" + "next step if
unopposed" pair in `## Secrets & Clues`, updated by `world-update` alongside
faction Fronts — this quest's own clock, not a Front (the Subtype Boundary
still applies: a quest doesn't get a `### Front:` heading, that's the
faction guide's territory).

## The Mystery Box

Shape: `.claude/skills/draft-story/references/story-structures-campaign.md` § The Mystery Box.

**Use when**: the quest's draw is a question, not a task ("who sent this
letter" rather than "clear the ruins").

**How to build it**: state which kind up front in `## Secrets & Clues`. A
solvable mystery still needs the Three-Clue Rule
(`.claude/skills/composing-beats/references/runtime-surface.md` §4) — three independent, findable clues,
at least two reachable without combat. An atmospheric mystery is exempt
(there's no answer to clue toward) but must say so explicitly, so a later
session's contradiction reads as an intentional open question rather than
an unplanned retcon.

## The Reversal Arc

Shape: `.claude/skills/draft-story/references/story-structures-campaign.md` § The Reversal Arc.

**Use when**: the opposition (an NPC or faction) has a hidden layer whose
reveal should recontextualize everything the party has done so far.

**How to build it**: name the inversion condition in `## Secrets & Clues`
— what has to happen for the reversal to trigger. It's a structural fact
about the opposition (see the linked NPC's or faction's own secret), not a
scripted event on this quest's own timeline.

## The Pyrrhic Arc

Shape: `.claude/skills/draft-story/references/story-structures-campaign.md` § The Pyrrhic Arc.

**Use when**: the Outcome is likely to be "complete" but the quest's
real payoff is what completing it costs or destabilizes next.

**How to build it**: ask "what fills the vacuum if the party wins outright,
right now?" and name it in `## Secrets & Clues` — a faction that benefits,
a debt that comes due, a Front that starts ticking as a direct result. This
becomes the seed of the *next* quest or Front, planned in advance rather
than sprung on the party as a twist.

## The Cliffhanger

Beats-level device: `writing-cliffhanger-beats` skill owns beat
construction, pressure patterns, escalation, and the quality gate.

**Use when**: `draft-story` (its DS4 step) is drafting this quest's next
Beat and needs a session-ending point. This quest guide flags which Beats
are cliffhanger-worthy (the highest-tension moment naturally reached); the
actual prose lands in `draft-story`, not here.

## Three-Act Structure (adapted)

Shape and multi-scale table: `.claude/skills/draft-story/references/story-structures-classic.md` §
Three-act structure, applied loosely across a quest's full span rather
than scripted per-session.

**Use when**: none of the above patterns fit and the quest is a
comparatively simple single-thread objective — this is the default shape,
not a special case, and most quests don't need a named pattern at all.
Note it as "single-thread, three-act" in `## Secrets & Clues` and move on.

**Sandbox caveat**: the Outcome act is *available*, not scheduled — the
party may resolve the quest at any point once its objective is met, abandon
it, or let it stall. `quest_status` reflects whichever actually happened,
never the plan.

## Diagnosing a stalled quest

Use when a quest has sat at `status: active` for several sessions with no
Beats added — a stall usually means the pattern, not the party, is the
problem. General diagnostic (nothing happening, flat escalation,
disengaged players): `.claude/skills/composing-beats/references/audits.md` §
Diagnosing a stalled or flat journey. Quest-page-specific symptoms not
covered there:

- **"The party keeps ignoring it."** No PC connects strongly enough — the
  `link_of_relevance` is thin or generic. Fix: re-run the PC-Connection
  interview question — a quest with no real pull may simply get abandoned,
  a valid `quest_status`, not a failure to force past.
