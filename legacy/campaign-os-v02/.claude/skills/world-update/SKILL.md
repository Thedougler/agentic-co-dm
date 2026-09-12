---
name: world-update
description: Advance faction and major/recurring-NPC clocks ("Fronts") after canon has moved — post-ingest, in a Campaign OS repo (vault/ present). Use for "world update", "advance the factions/clocks", "tick the world", "what happened offscreen", "what is [faction] doing". Never edits vault/ directly.
---

# World Update

Post-ingest clock advancement: factions and major/recurring NPCs keep pursuing their
own goals on their own timelines whether or not the party is watching. This skill
reads the *now-canon* wiki (never a raw transcript, never chat memory) and proposes
how each tracked Front (clock) moved, as ledger lines a human reviews and `canon-review`
applies — the sole exception is `vault/campaigns/shattered-sea/threads.md`/`vault/campaigns/shattered-sea/spoilers.md`, a non-canon index (Hard Rule 2).

**Boundary with `.claude/skills/draft-content/references/faction.md`:** that guide *defines* Fronts (segments, trigger
conditions, consequence at fill, at PREP time, `status: pending`); this skill only
*moves* Fronts that already exist on a `status: canon` page — a missing Front is a
`.claude/skills/draft-content/references/faction.md` job, hand off rather than inventing one inline.

**Core question, every Front, every run:** *If the party had done nothing, what would
have changed anyway — toward or away from where this season/campaign is headed?*
Factions pursue their own goals; the party is one variable, not the engine.

## Hard rules

1. **Never advance a Front without citing what justifies it.** Grep the wiki, paste
   the hit, cite it by file + line number in the ledger line. No citation, no line —
   same discipline as INGEST citing a transcript `L`-number (L1).
2. **Never edit `vault/` or `vault/campaigns/shattered-sea/pcs/` directly** — one exception,
   `vault/campaigns/shattered-sea/threads.md`/`vault/campaigns/shattered-sea/spoilers.md` (`references/threads-and-spoilers.md`). Propose ledger lines in a world-turn
   ledger; only `canon-review` applies them — convention, not machine-enforced (L2, L6).
3. **Never fire a filled Front silently.** When a proposed advance would bring a
   Front's `**Clock:** N segments — filled: X` to `X == N`, stop for that Front:
   present the consequence quoted from its `**Consequence at fill:**` line and wait
   for the DM to confirm, hold, or reinterpret before writing any line that flips
   `**Lifecycle:**` to `resolved` or executes the consequence. The partial advance up
   to (not through) the fill line may still be proposed on its own.
4. **A DM aside or chat note is never evidence.** Only `status: canon` pages and a
   session's `vault/episodes/NNN/sNN-recap.md` count as what "actually happened" — not a floated idea.
5. **Never define a new Front, or invent a page/home for a thread that has none.** A
   pressure with no actor at all is `.claude/skills/draft-content/references/faction.md`'s degrade-by-asking case — flag it
   and hand off. A lone villain/major/recurring NPC's Front lives on that NPC's own
   page — a legitimate owner.
6. **Every "nothing happened" is still something happening.** A COLD Front that rolls
   a setback still changed something (a rumor, a resource spent, a plan exposed) — see
   `references/clock-advance-workflow.md` § Interpret. A roll that produces zero
   observable change means the proposal wasn't specific enough; rewrite it.
7. **Never write a Front's ledger lines before the DM discusses that Front's roll
   and interpretation.** Stop after interpreting, share the draft lines, collaborate
   on how it advances, then write — every Front, not only a fill (Rule 3 stops
   harder: no writing at all until confirmed).
8. **Ground every proposal in where the season/campaign is headed, not just the
   Front's own page.** Query the active season's throughline (or the campaign
   overview page's Truths if none) during the deep read; name whether it serves
   that or drifts away.

## Gate — confirm this is post-ingest

```
git log --oneline -E --grep '^ingest\(s[0-9]+\)' | head -1
```

Paste the hit and read `sNN` — the session this turn follows. No hit → nothing's
been ingested yet; say so and stop.

```
find vault/campaigns/shattered-sea/episodes -maxdepth 1 -type d -name "0NN" 2>/dev/null
```

(substitute `NN`, zero-padded to 3 digits) → this turn's ledger directory.

**Cross-day idempotency check** — before triage, every run; guards a rerun on a
*later* day between the same two `ingest` commits, where an earlier day's
world-turn file was written but never applied (rationale:
`references/clock-advance-workflow.md` § Cross-day idempotency).

```
find vault/campaigns/shattered-sea/episodes -name "world-turn-*.md" 2>/dev/null
```

(zsh-safe — see `references/shell-safety-notes.md`.)

For every hit under the target session's directory (`NNN` from above), check
which lines are still pending:

```
grep -n "^- \[ \]" vault/episodes/NNN/world-turn-<earlier-date>.md
```

An unchecked line is an already-proposed advance the wiki doesn't yet reflect. Read
the whole file; for any Front this run's triage would cover, if it appears in a
pending line, skip it this run (cite the earlier file/line) or explicitly supersede
it, stating why — never duplicate the proposal silently. A Front with no pending
proposal in any un-applied file triages normally.

## Modes

Both modes produce the same world-turn ledger via the same workflow, differing only
in *when* they run and how much HOT-tier evidence exists.

| Mode | When | HOT-tier evidence |
|---|---|---|
| **Post-session** (default) | Right after `ingest(sNN)`, once the recap exists | `vault/episodes/NNN/sNN-recap.md`, cross-referenced with the checked lines in `vault/episodes/NNN/state-changes.md` |
| **On-demand** | Mid-session or between sessions, DM asks "what are the factions doing" | Whatever's canon as of the last `ingest` — no fresh recap to read; most Fronts will triage WARM or COLD |

Both attribute the ledger to `sNN`, the last ingested session (from the
Gate) — a between-sessions turn stays stamped there until the next session ingests.

## Standard queries

```
grep -rl --include="*.md" "^### Front:" vault/campaigns/shattered-sea/factions/ vault/campaigns/shattered-sea/npcs/ 2>/dev/null
grep -rA20 --include="*.md" "^### Front:" vault/campaigns/shattered-sea/factions/ vault/campaigns/shattered-sea/npcs/ 2>/dev/null
```

(zsh-safe — see `references/shell-safety-notes.md`. Empty output is informative: no
Fronts exist yet, nothing to advance, say so and stop.)

For each Front hit, before proposing anything:

```
grep -n "." <the Front's own page — factions/<slug>.md or npcs/<slug>.md>
grep -ril "<linked NPC/location/quest name>" vault/ vault/campaigns/shattered-sea/pcs/ 2>/dev/null
```

The first pastes the Front's owning page with real line numbers (for citations); the second
follows every wikilink the Front's DM Only / Goals & Fronts prose names. Once per run,
also pull the story's current direction — `references/clock-advance-workflow.md` § Deep read.

Post-session mode's HOT-tier evidence:

```
grep -n "." vault/episodes/NNN/sNN-recap.md
grep -n "^- \[x\]" vault/episodes/NNN/state-changes.md
```

This skill only ever reads and mechanically edits three of a Front's lines
(`**Lifecycle:**`, `**Clock:** ... filled:`, `**Consequence at fill:**` on a
fill) plus, on any `**Lifecycle:**` flip, the page's `has_active_front`
frontmatter flag (`references/ledger-mechanics.md`).

## Workflow (summary — full ritual in the reference file)

1. **Gate check + cross-day idempotency check** (above) — paste the `ingest(sNN)`
   hit; skip or supersede any Front already covered by a pending un-applied
   `world-turn-*.md`.
2. **Collect every Front** (standard queries) and **triage** each `active` one HOT /
   WARM / COLD. Rebuild `vault/campaigns/shattered-sea/threads.md`/`vault/campaigns/shattered-sea/spoilers.md` from this read (self-create if
   missing — `references/threads-and-spoilers.md`). Present the triage table, wait
   for DM confirmation before rolling anything — same review-checkpoint discipline
   as INGEST's ledger review.
3. **Process one Front at a time**, HOT then WARM then COLD: deep read (Front +
   linked entities + season/campaign direction) → Context Brief → propose → roll
   `d20` → interpret → **present to the DM, collaborate on how it advances** (Rule 7)
   → fill check (Rule 3) → write. Cold Fronts fold a hook-strength note
   (Whisper/Ripple/Wave/Collision) into the proposal's description.
4. **Close out**: tag each advanced Front's `APPEAR` description with an urgency word
   (`low`/`medium`/`high`/`critical`) so `draft-run-guide`'s loose-thread greps can
   prioritize it. Leave `REVIEWED-BY-HUMAN: (pending)`, present the ledger to the DM,
   commit the ledger file only (not `vault/`).

## Ledger mechanics — where proposals land

Proposals land in `vault/episodes/NNN/world-turn-<YYYY-MM-DD>.md`, never
`vault/episodes/NNN/state-changes.md`. Grammar: `- [ ] VERB target :: change (citation)`, closed verb set
`FACT`/`APPEAR`/`NEW`/`QUEST`/`REVIEW` — every ordinary advance writes at least one
`FACT` line (Clock/Lifecycle edit) and one `APPEAR` line (dated log entry). This skill
never sets `status: canon` itself — propose the line even under pressure to "just fix
the page directly"; full grammar in the References table below.

## Owned paths

Writes `vault/episodes/NNN/world-turn-<date>.md` (NNN from the Gate) plus, directly (Hard
Rule 2's exception), `vault/campaigns/shattered-sea/threads.md`/`vault/campaigns/shattered-sea/spoilers.md`. Never
`vault/episodes/NNN/state-changes.md`/`vault/episodes/NNN/sNN-recap.md`/`vault/episodes/NNN/sNN-highlights.md` (ingest/recap-writer own those),
never any other `vault/`/`vault/campaigns/shattered-sea/pcs/` path, never a new faction/NPC page or Front (Hard Rule 5).

## References

| File | Covers |
|---|---|
| `references/clock-advance-workflow.md` | Full triage/process ritual, Context Brief format, roll/interpret tables, collisions, cold escalation, quality checklist, worked example |
| `references/front-template.md` | The Front's full field-by-field template and which Lifecycle states get triaged |
| `references/ledger-mechanics.md` | World-turn ledger file path/frontmatter, verb table, citation format, `→`-not-`->` syntax |
| `references/shell-safety-notes.md` | zsh glob/quoting notes for this skill's `find`/`grep` queries |
| `references/threads-and-spoilers.md` | Self-creating and rebuilding `vault/campaigns/shattered-sea/threads.md`/`vault/campaigns/shattered-sea/spoilers.md`, the campaign-level Thread index |

## Degrade by asking

- No `ingest(sNN)` commit at all → tell the DM nothing's been ingested yet, stop.
- A Front missing `**Trigger conditions:**`/`**Consequence at fill:**`, or a brewing
  thread with no owning faction/NPC page → flag/ask, hand off to `.claude/skills/draft-content/references/faction.md`.
- Two Fronts' advances collide in the same window → present both to the DM if not
  obvious which has better position; coin-flip only after the DM declines to call it.
- Ambiguous which `world-turn-<date>.md` an on-demand check belongs to → ask, don't
  silently start a second file.
