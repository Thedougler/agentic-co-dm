---
status: PASS
lever: claude-md
target: CLAUDE.md docs/guardrails/PROJECT.md
---
# Agents fix any actionable issue found in context, never park it as NOTED (not done)

**Gap:** a fresh agent (main thread or subagent) mid-task notices a fixable
issue in a file already open in its context — a doc past its word-count
cap, a stale reference, a lint debt, a spec violation — that its own edit
didn't cause and the current task didn't ask for. Old behaviour: log it as
`NOTED (not done): <thing> <file:line>` (or "out of scope", "pre-existing",
"a follow-up") and move on, per CLAUDE.md's kit iron rule ("change only
lines the task requires, log the rest as NOTED"). Should: fix it this turn,
or dispatch a background Agent for volume, treating "pre-existing" /
"not caused by my edit" as *not* a valid reason to defer.

**Saves:** every deferred NOTED is a re-discovery tax on some future
session — the same file gets re-read, the same gap re-diagnosed, the same
judgment call re-made, and most NOTED lines are never swept up at all
(fix-on-discovery's own queue exists because deferred setup friction rots).
Fixing at discovery time is strictly cheaper: the file's already in
context, the fix is already understood, and a background Agent absorbs the
cost without derailing the main task.

**RED:** user-reported, quoting a real subagent turn: *"CODE.md sits at
~1175 words, slightly over _FORMAT.md's ~1,100-word cap — but that's
pre-existing (my edit only reworded the trigger line, same length), not
something this session's edits caused. NOTED (not done):
docs/guardrails/CODE.md word-count cap — out of scope for a restructuring
today."* Grounded via `transcripts.py recur "NOTED \(not done\)"`
(2026-07-29, this repo, excluding the live session): 77 distinct sessions,
233 total hits — a heavily recurring pattern, not a one-off.

**Fix applied:** `CLAUDE.md`'s Project-zone bullet ("Found a fixable issue
mid-task...") widened from a named category list (bug/canon
conflict/QC fail/lint debt) to "any fixable issue in a file already in your
context", with an explicit override of the kit iron rule's NOTED default
and an explicit close of the "pre-existing" loophole; `NOTED (not done)`
narrowed to only a finding genuinely outside the session's reach. The
background-Agent dispatch clause now also names the smallest/quickest
viable model (Haiku by default, step up only if the fix itself needs
subagents of its own) instead of just "non-fable", per user follow-up.
`docs/guardrails/PROJECT.md`'s PJ6 (which restated the old NOTED default
for prose) updated to point at the new CLAUDE.md rule instead of
restating a NOTED default; PJ11's now-stale "(overrides PJ6...)" cross-ref
corrected.

**GREEN:** 3/3 — pool of 3 fresh Haiku testers, each given the CODE.md
word-count-cap scenario blind, all rejected NOTED/deferral and named Haiku
for the dispatched background Agent. Judge quote: "Dispatch a background
Agent with: model: 'haiku' (explicit non-fable model as required, Haiku is
appropriate for doc refactoring)." (tester 1); "Model: haiku (explicit,
smallest sufficient for trimming)" (tester 2); "Model: Haiku (explicit
non-fable, smallest/quickest model per CLAUDE.md line 42)" (tester 3).
Negative held: no tester invented fixes for files never opened, none
dropped the original wikilink-fix task to go trim CODE.md instead of
dispatching it.
