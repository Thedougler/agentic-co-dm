---
status: PASS
lever: skill+claude-md
target: content/ref/craft/prose-aesthetic.md CLAUDE.md
---
# Make prose-aesthetic a live, self-updating guide on any style correction

**Gap:** a fresh agent given a mid-task style correction ("don't say it
'sounds wrong', name the physical detail instead") on ANY piece of writing —
not only inside a dedicated `dev-edit`/`draft-story`/`writers-room` pass —
noted the correction in conversation and moved on, never writing it into
`content/ref/craft/prose-aesthetic.md`. Should: capture the correction into the matching
section of `content/ref/craft/prose-aesthetic.md` same turn, every time, regardless of
which task surfaced it.

**Saves:** without this, every future editing pass recalibrates from a
stale guide and the GM has to re-teach the same correction across
sessions — this is the exact miss `worth-remembering` warns about, applied
to prose voice instead of facts.

**RED:** `transcripts.py recur` (2026-07-22, this repo, 60d, excluding the
live session) found the capture already happened once ad hoc, with no
standing trigger: session `75188ab5` populated *What You Do Not Do* from a
GM correction mid-drafting (2026-07-22T22:27–22:47), but no skill or
CLAUDE.md line instructed that write-back — it happened because the acting
agent happened to notice, not because anything routed it. 3 distinct
sessions / 11 hits total referenced `writing-style` in the same 60-day
window, all as a *read* dependency (calibration), never as a
correction-capture trigger — confirming the write side was unwired.

**Fix applied:** `content/ref/craft/prose-aesthetic.md` description gained a clause —
"or the moment the user corrects a word choice, sentence, rhythm, or prose
habit in the agent's writing — for ANY content, in ANY task... which must
be captured here before the task ends" — and a new `## Keeping this file
live` section spells out the capture procedure (which section to file
under, update *Source Note*). `CLAUDE.md`'s project routing table gained a
mirrored one-line row (same shape as the existing DM-ruling →
`campaign-domain-modeling` row) so the trigger fires even when
`prose-aesthetic` isn't already loaded for calibration.

**GREEN:** verified both halves are already committed (git log 83380454;
`git diff` against `content/ref/craft/prose-aesthetic.md` is empty —
committed, not in-flight). Traced the trigger chain a fresh agent actually
hits: CLAUDE.md's Project section (loaded for any campaign-os work) carries
the row "User corrects a word choice, sentence, rhythm, or prose habit in
the agent's writing — for ANY content, in ANY task, not only a dedicated
editing pass → read prose-aesthetic, capture the correction into it
same turn, never deferred" — this fires independent of whether
`prose-aesthetic` is already loaded for calibration. The guide's
own `## Keeping this file live` section gives the concrete capture
step the ticket's gap named as missing: file the correction under the
matching section (*What You Do Not Do* for a "never do this" correction;
*Prose Style*, *Narrator and Voice*, or *Structure* for a positive
preference), quote the correction and the fix, and update *Source Note*
with the date and task — not a bare "capture it" instruction. This matches
the ticket's own PASS bar: a fresh agent following the trigger has a
concrete where/how, not just a directive to capture.
