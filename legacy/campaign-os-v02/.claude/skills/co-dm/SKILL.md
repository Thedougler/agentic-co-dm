---
name: co-dm
description: Live co-DM assistant for running a D&D 5e table session — the RUN phase. First skill to consult for anything happening live at the table. Use when the user is at the table right now — "help me run tonight's session", "mid-session", "what does the NPC say", "improvise a detail" — or the bare word "co-dm". Not for pre-session prep (draft-run-guide).
---

# Co-DM

The RUN-phase skill (`vault/refs/README.md` § The session loop, Phase 2) — the one
piece of the session pipeline that operates *at the table*, not before or
after it. Every other skill in this repo either prepares content ahead of
the session or processes it afterward; this is the only one that answers a
live question while players are sitting there waiting.

Two jobs, and only two: **route** requests that aren't actually RUN-phase
to the skill that owns them, and **capture** anything improvised live so it
survives past the moment it was said. This skill never authors wiki content
itself — that would duplicate `.claude/skills/draft-content/references/npc.md`, `.claude/skills/draft-content/references/location.md`, `.claude/skills/draft-content/references/faction.md`,
`.claude/skills/draft-content/references/item.md`, `encounter-prep`, and `dnd5e-scene-narration`, all of which
already own their piece of content generation better than a live-pressure
answer ever could.

This skill is stateless by design (`campaign-os` SKILL.md § Why this
design, the ledger-rot point): it re-derives everything it needs from the
wiki and git log, every time, the same way `draft-run-guide` does. It
never reads or creates a persistent config/state file to cache what a grep
already answers.

## Standard queries

Run before answering anything live — same L1 discipline every skill here
follows, just faster because the table is waiting:

```bash
# Stub check before naming or answering as any entity (runtime-surface.md §1)
grep -ril "<entity name>" vault/ 2>/dev/null

# Current session's table-notes file, if one already exists this session
ls vault/episodes/<NNN>/table-notes.md 2>/dev/null

# PREP-phase gate, only if routing a request there (Hard Rule 4)
git log --oneline | grep ingest
```

A stub-check miss is informative, not a blocker (`references/stub-check-miss.md`)
— proceed to improvising (Hard Rule 1) unless Degrade by asking applies.

## Owned paths

**`vault/episodes/<NNN>/table-notes.md`** — the only file this skill writes.
New file if this session doesn't have one yet (append `## IMPROV` blocks,
below); append-only after that. Nothing else. This skill:

- **Invokes** `draft-run-guide` for PREP-phase work — it does not own or
  duplicate that skill's output, it hands off to it (Hard Rule 4).
- **Invokes** `dnd5e-scene-narration` for read-aloud prose it decides a
  moment needs — it does not write boxed text itself.
- **Never** writes `vault/`, or any file those skills own.
- **Never** sets `status: canon` or `publish: true` — `transcript-ingest`
  (`status: canon`) and PUBLISH (`publish: true`) own those exclusively,
  same as every other skill in this repo (L2).
- **Never** creates or reads a persistent config/state file (see § above).

## Hard rules

1. **Grep before you improvise.** Run the stub check (Standard queries)
   before answering as, or inventing details for, any named entity. A hit
   → use what's there, don't contradict it. A miss → you're clear to
   improvise (Rule 2). Skipping this to save two seconds is how a
   vendor's name ends up contradicting a page that already existed
   (`.claude/skills/composing-beats/references/runtime-surface.md` §1 — the miss that creates duplicate-entity cleanup
   work later).

2. **The moment you improvise anything the wiki doesn't already have — a
   name, a price, a minor NPC, a detail — append an `## IMPROV` block to
   `vault/episodes/<NNN>/table-notes.md` in the same turn, before the scene
   moves on.** Never rely on the session recording alone to preserve it.
   No exception holds — `references/capture-excuses.md` closes every
   workaround by name before you reach for one.

3. **Never write `vault/` live, never set `status: canon` or
   `publish: true`** — not even when the table is certain a fact is
   permanent. `transcript-ingest` writes it as canon directly from the
   recorded transcript (L2); a live write here skips that recorded-play
   evidence entirely, the same canon-drift failure mode `campaign-os` §
   Why this design names first.

4. **A PREP-phase request routes to `draft-run-guide`, it doesn't get
   answered here.** "What should I prep for next session," "build the run
   guide," or anything about a session that hasn't started yet — hand off,
   don't re-derive a scene menu from scratch. This skill's job starts once
   players are actually at the table.

5. **A request for real content — a full NPC, a location, a faction, an
   item, a stat block — routes to its specialist skill, even mid-session.**
   `.claude/skills/draft-content/references/npc.md`, `.claude/skills/draft-content/references/location.md`, `.claude/skills/draft-content/references/faction.md`, `.claude/skills/draft-content/references/item.md`,
   `encounter-prep`. This skill's live answer is a provisional name, price,
   or detail plus an `IMPROV` capture — never a template-instantiated page.
   If the table needs the full page *right now* to keep playing, say the
   provisional version aloud, capture it (Rule 2), and note in the block
   that it's a promotion candidate for the next prep pass.

6. **Never advance a faction's front or clock live.** Simulating what a
   faction might be doing between sessions is `draft-run-guide`'s PREP-time
   job as pending framing; actually ticking a clock in canon is
   `world-update`'s, post-INGEST only. Don't do either at the table.

## `## IMPROV` block format

```markdown
## IMPROV: <short label>
- **Said:** "<what was actually said or decided at the table, close to verbatim>"
- **Type:** npc | location | item | detail | other
- **Context:** <scene / where in the session, roughly>
```

One block per improvised fact, appended in order. `transcript-ingest`
reads each block as its own small chunk and cites it `(TN-L<n>)` —
`vault/episodes/<NNN>/table-notes.md`'s own line number, deliberately distinct
from a transcript's `(Lnnn)` so the two evidence sources never collide in a
ledger line (see `.claude/skills/transcript/references/ingest.md` § Table-notes
as a second evidence source).

## Workflow

1. **Classify the request.** PREP-phase (nothing's happened at the table
   yet) → Hard Rule 4, hand off. Full-content request that isn't urgent →
   Hard Rule 5, hand off. Otherwise: it's a live RUN-phase question — keep
   going.
2. **Stub check** (Standard queries) for every named entity in the
   question. Paste the grep, even under time pressure — it's one command.
3. **Hit → answer from what's there,** wikilinked in your own notes if you
   want to reference it, quoted rather than re-derived (`vault/refs/runbook-wiki.md`
   § Single-source rules — same discipline `draft-run-guide` follows).
4. **Miss → improvise the answer,** consistent with everything else
   established about the scene, then immediately do step 5. Don't answer
   first and "capture it later" — later is how Rule 2's excuses happen.
5. **Write the `## IMPROV` block** to `vault/episodes/<NNN>/table-notes.md`
   (create the file if this is the session's first one). One block, this
   fact only — don't batch multiple improvisations into one block.
6. **Give the table its answer** — the DM keeps running the scene, applying
   `references/table-technique.md`'s craft (controlling the clock,
   fast-forwarding the routine parts, embracing what the party does with
   it) where it helps; this skill's job for that beat is done.
7. **Session-end KEEP-or-SKIP sweep.** When the session wraps (the DM says
   so, or a hook fires this skill at stop), scan the conversation once for
   uncaptured findings: KEEP if any turn contains a fact the table now
   treats as true and no `## IMPROV` block or wiki page records it; SKIP if
   everything was conversational or already captured. Asymmetry: fired
   automatically → err SKIP (silence beats spam); invoked by the DM → err
   KEEP. Each KEEP gets its own `## IMPROV` block now, then the normal
   CAPTURE gate proceeds.

## Reference files

| File | Read when |
|---|---|
| `references/table-technique.md` | Running the actual live beat — controlling the clock, fast-forwarding routine parts, embracing what the party does with an unprepared moment |
| `references/capture-excuses.md` | Tempted to skip an `## IMPROV` write — the excuse/reality table and red flags behind Hard Rule 2 |
| `references/live-improv-example.md` | Want the full stub-check → improvise → capture trace worked end to end |
| `references/session-checklist.md` | Confirming a live beat is fully handled before moving on |
| `references/stub-check-miss.md` | Deciding whether a stub-check miss needs escalation or is clear to improvise |

## Degrade by asking

- The stub-check hit is ambiguous — the name might resolve to an existing
  entity under different spelling, or to two different ones → ask the DM
  which, don't silently pick or silently improvise a duplicate.
- Genuinely unclear whether a request is PREP or RUN (e.g., "what should
  happen next" asked mid-session about a future session) → ask which the
  DM means; don't guess and answer the wrong phase's question.
- The table needs something this skill has no owned path for (a full
  battlemap, generated art) → say so and name the skill that owns it
  (`battlemap-render`, `visual-aids`) rather than attempting a substitute.

## Creative-domain rider

Facts, canon, structure, and visibility are bound (Hard Rules above, all
ten CLAUDE.md project rules) — never prose style. A live answer that plays
it safe with a generic name and a round number is a worse answer than a
specific, table-tested one; improvise boldly inside the capture discipline,
don't hedge because the answer might not stick — Rule 2 is exactly what
makes it stick.

## Out of scope

- Writing any entity's own page — the specialist prep skills own that
  content; this skill only improvises a provisional answer and captures it.
- Building the pre-session run guide — `draft-run-guide`, PREP-phase only.
- The read-aloud paragraph craft itself — `dnd5e-scene-narration`; this
  skill calls for one when a moment needs it, that skill writes it.
- Advancing a faction's front clock, or resolving what happened off-screen
  — `world-update`, post-INGEST.
- Running combat mechanics or generating stat blocks live — the DM runs
  combat with what `encounter-prep`/`.claude/skills/draft-content/references/monster.md` already prepared;
  this skill doesn't design or adjudicate mechanics.
- Turning a session's `vault/episodes/<NNN>/table-notes.md` into ledger lines — `transcript-ingest`
  reads it as evidence; this skill only ever appends to it, never processes it.
- Anything already `status: canon` — canon-review's territory.
