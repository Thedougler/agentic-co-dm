# Degrade by asking

- No `ingest(sNN)` commit → stop and say so; don't draft ahead of the gate
  (see Gate).
- A touched page's claim or its transcript wikilink doesn't resolve → don't
  guess the quote; ask the human which passage it should be, or drop it
  from the candidate pool.
- Fewer than 3 clean in-world quotes survive the filter → tell the human
  the session was thin on highlight-worthy moments and ask whether to ship
  fewer than 3 or widen the transcript window searched, rather than padding
  with an OOC line to hit the count.
- Ambiguous session number (more than one `vault/episodes/NNN` dir with an
  un-ingested transcript) → ask which session, don't assume "the latest."
- A touched page and another page visibly disagree (one page's new content
  contradicts what a different page currently says) → that's an INGEST-time
  `CONTRADICTION` block's job, not this skill's; if you spot one uncaught,
  flag it to the human rather than silently picking a side or writing
  around it.
