# Manual lore consistency review

The rule table (`npm run lint -- --rules`) catches structural
drift — a broken link, a missing key, a stale tag — but it cannot read
prose for meaning, and it cannot reason about
in-world time. After working the automated report, do a manual pass over the
files it flagged or that you touched during fixes. Temporal consistency (when
things happened, whether movements and durations are physically possible,
whether "current state" claims have decayed) is the highest-value part of
this pass — a compounding knowledge base is only as reliable as its internal
coherence.

## What to check

**Contradicted facts across files.** When a page states a fact about another
entity (location, allegiance, status, an event), open the target entity's
page and verify the claim matches. Common drift patterns:

- An NPC page places them in one location; a faction or quest page's prose
  places them somewhere else at the same time.
- A session recap attributes an event to one session number; the affected
  entity's page attributes it to a different one.
- A faction page lists someone as a member; that person's own page says they
  left.
- A location page names its current authority; that authority's own page
  doesn't list the location among its holdings.

When you find a contradiction: check the session ledger / transcript (the
primary source) to determine which version is correct. If one side is a
clear outlier against everything else — including the rest of its own
page — that's a drafting error, not competing canon: fix it and say so,
citing the unanimous evidence (same standard canon-review applies to an
unanimous case). If the sources genuinely split, append a `> [!warning]
CONTRADICTION` block to the page and a `- [ ] REVIEW <page> :: ... (Lnnn)`
ledger line (block format: `transcript-ingest` SKILL.md § Contradictions;
ledger line: `npm run lint -- --rules` W16) — never resolve a
genuine split yourself.

**Temporal consistency.** Judgment work no table entry can do — it requires
understanding when things happened in-world, what was physically possible
given distances and durations, and whether pages reflect the world as it
stands after the most recent session. Session ledgers
(`vault/episodes/<NN>/state-changes.md`)
and transcripts are the authoritative timeline.

- *Session-number accuracy.* A page citing "session 03" for an event —
  verify against that session's own recap/ledger, not the session where it
  was merely discussed.
- *In-world day sequencing.* Where a session's ledger or scenes carry day
  numbering, entity/situation pages referencing those events must be
  consistent with the day they occurred (a multi-day repair can't finish a
  day before it started).
- *Location-time plausibility.* An entity or the party can't be in two places
  in the same window unless travel between them is plausible in the elapsed
  time — check this against however this campaign's travel actually works
  (a nautical or overland campaign has real transit times; don't assume
  either without checking `vault/` for the actual method).
- *"Current state" decay.* Pages carry present-tense claims
  ("currently docked at X", "allied with Y"). Each has a session of origin;
  when a later session changes it, every page that cached the old state
  needs updating. A callout labeled "as of session N" reads as authoritative
  and rots silently if nobody revisits it.
- *Causal ordering.* When a page describes a consequence, verify the cause
  already occurred in the ledger/transcript record — this catches
  world-building written ahead of play describing outcomes that haven't
  happened at the table yet.
- *Concurrent timelines.* Multiple threads running at once (a faction's
  clock, a quest's beats, an NPC's own movements) referencing the same
  in-world day must agree on what that day looks like.

**How to do it.** Don't audit the whole timeline at once — start from the
files the automated sweep flagged or the ones you touched fixing them. For
each temporal claim, trace it back to its session source (state-changes.md,
the transcript, or the recap). Use the `llm-wiki-query` skill for a cross-reference
search wider than a direct grep can reach. When you find a mismatch, fix the
clear error the same way as above; for a genuine split, CONTRADICTION block
+ REVIEW ledger line + canon-review, never a silent pick.

**Entity identity.** Two pages may describe the same entity under different
names — this is W17's job to detect at scale (name-similarity across
same-type pages); a manual pass catches the one-off case W17's heuristic
misses. Either way: never merge or resolve on your own. Flag it for
canon-review the same way W17 does — quote both pages' identifying details,
recommend nothing, leave both pages intact until the ruling lands.

## When to do a manual pass

- **After ingest** — new source material is the highest-frequency cause of
  lore drift; the pages it just touched are the first place to look.
- **After working the automated report** — the flagged files are already
  open in context; scan their prose while you're there.
- **After world-update** — clock advances and front resolutions can
  invalidate claims already written on entity pages.
- **When asked** — "check consistency", "does this all hang together",
  "anything contradictory" all trigger this pass directly, table or no
  table.

## What NOT to do

- Don't read every page in the vault hunting for contradictions — target
  files the automated sweep flagged or that reference each other (the
  `llm-wiki-query` skill is the tool for "what else touches this").
- Don't invent lore to close a gap. If two pages disagree and the ledger/
  transcript doesn't clarify, escalate — don't pick a side.
- Don't silently change an established fact just because a session moved it
  on — that's a legitimate correction (make it, cite the session). Two
  pages disagreeing with no session backing either way is a genuine split,
  not a call to make alone.
