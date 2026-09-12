---
name: session-history-prep
description: Compile or refresh a PC's standalone session-history page from their PC page's Session Log — a read-derived view, never a second source of truth, in a Campaign OS repo. Use for "compile session history for <PC>", "build a session-history view", "refresh <PC>'s session-log page". Not new session events (transcript-ingest) or combat data (combat-profiles).
---

# Session History Prep

This is a read-derived compile, not an
authoring skill that originates facts — see § Owned paths for the one
deliberate deviation.

Compiles `vault/campaigns/shattered-sea/pcs/session-logs/<name>-session-log.md` (`vault/_templates/_episodes/_session_history.md`) from
a PC's own `vault/campaigns/shattered-sea/pcs/<name>.md` `## Session Log` section — a standalone reading
view onto the same facts, not a second place those facts live. The PC page
stays canonical; this page never gets ahead of it and is never cited as a
source itself.

## Standard queries

Run before compiling:

```
cat vault/campaigns/shattered-sea/pcs/<name>.md                             # the canonical Session Log this page compiles from
cat vault/campaigns/shattered-sea/pcs/session-logs/<name>-session-log.md 2>/dev/null    # existing satellite, if any — check its last_compiled date
```

Satellite missing → fresh compile. Satellite exists and `last_compiled`
already covers every entry in `vault/campaigns/shattered-sea/pcs/<name>.md`'s Session Log → nothing to
do, say so. Satellite exists but stale → recompile in place, no re-ask.

## Owned paths

Writes `vault/campaigns/shattered-sea/pcs/session-logs/<name>-session-log.md` only. Never touches `vault/campaigns/shattered-sea/pcs/<name>.md`
itself — that page's `## Session Log` is `transcript-ingest`'s territory
(INGEST-time appends), not this skill's. Never sets `publish:` — the
publish proposal's move, same as any other page.

## Workflow

1. **Standard queries** — read the PC's own Session Log and the existing
   satellite (if any).
2. **Instantiate** `vault/_templates/_episodes/_session_history.md` (fresh compile) or open
   the existing satellite page (recompile) — copy the template, don't
   retype it.
3. **Timeline** — mirror every Session Log entry verbatim (same wording,
   same wikilinks, same citations), most recent first — the reverse of the
   source's own order (every existing PC page runs its Session Log oldest
   first). An entry the source states, this page restates; nothing more.
4. **Arc Threads** — read the compiled Timeline end to end and name the
   throughlines only visible across multiple entries (a recurring name, an
   escalating stake, a setup-and-payoff pair). Each thread cites the dated
   entries it draws from. No thread invents a fact the Timeline doesn't
   already carry — degrade by leaving Arc Threads thin rather than reaching
   for a pattern that isn't really there.
5. **Write** `vault/campaigns/shattered-sea/pcs/session-logs/<name>-session-log.md`, `last_compiled:` set to today's
   date, `status:` matching the source PC page's own status (canon stays
   canon; a page compiled off a `pending` PC page stays `pending` too —
   never ahead of its source).

## Degrade by asking

+ The PC's own Session Log is empty → say so, don't compile an empty
  Timeline as if it were a finished page; ask whether to hold off until
  there's real play data.
+ An apparent arc thread is genuinely ambiguous (two readings, no clear
  throughline) → leave it out rather than force a synthesis the Timeline
  doesn't support.

## Checklist (run before calling the page done)

+ [ ] Standard queries run — both the source PC page and any existing
      satellite read before writing.
+ [ ] Timeline mirrors the source Session Log exactly — no reworded
      entries, no dropped citations, no added claims.
+ [ ] Every Arc Threads claim traces to a dated Timeline entry.
+ [ ] `last_compiled` set to today; `status` matches the source PC page's
      own status, never ahead of it.
+ [ ] `vault/campaigns/shattered-sea/pcs/<name>.md` itself untouched by this skill.

## Out of scope

+ Appending a new session's events to a PC's own `## Session Log` —
  `transcript-ingest`'s job, at INGEST.
+ Combat data, DPR, or difficulty calibration — `combat-profiles`.
+ Narrative, backstory, or Arc Notes content — `dnd5e-character-interview`
  (fresh create/gap-fill) or `canon-review` (a contradiction on an
  already-canon page).
