# Two ways in

1. **Fresh** — no `vault/episodes/NN-slug/recap-draft.md` exists. Read this session's canon pages
   and transcript directly and write `vault/episodes/NN-slug/recap.md` from scratch (Workflow
   step 2). **Exception: a legacy-sourced session.** If `vault/episodes/NN-slug/transcript.md`'s
   first line reads `LEGACY-SOURCE: <path> — prose recap, no audio`, the
   transcript *is* already a finished, human-written recap — not raw
   table-talk. Don't reconstruct new prose from the canon pages' facts;
   that discards already-good writing and risks introducing drift a
   paraphrase can quietly carry. Instead adapt the source prose close to
   verbatim: keep its sentences, wikilink named entities on first mention
   (resolve to whatever page basename actually exists now — it may differ
   from the legacy source's own link target), drop image-embed lines and
   any section that isn't prose (state-at-break tables, threads-left-open,
   related-links — those map to the canon pages/highlights, not
   `## Recap`), and trim only what the `recap` QC profile's BREVITY row
   would flag. Every
   sentence still needs to trace to a touched canon page (Hard Rule 1) —
   for a legacy session the canon pages' facts were extracted *from* this
   same prose, so verifying is usually confirming, not discovering
   conflicts.
2. **Promote a staged draft** — `draft-story` already
   built `vault/episodes/NN-slug/recap-draft.md` (a session-template instance,
   `status: draft`, `publish: false`, RECAP-gated the same way this skill
   is). Read it, but **do not trust it blindly** — re-verify every claim
   against the canon pages/transcript yourself (this skill, not the
   drafting skill, is accountable for the canon-derived-only rule on the
   file that actually ships). Fold its prose into `vault/episodes/NN-slug/recap.md`'s `## Recap` section,
   tightening to 300–450 words and cutting anything that doesn't
   re-verify. Once promoted, delete `vault/episodes/NN-slug/recap-draft.md` — it is superseded
   staging, and leaving both around violates the single-source rule
   (`vault/refs/runbook-wiki.md` § Single-source rules). This delete is the one case where consuming another
   skill's owned path is correct: promotion is what `vault/episodes/NN-slug/recap-draft.md` was
   staged *for*.

Either way, `vault/episodes/NN-slug/highlights.md` is always originated by this skill — no sibling
skill stages highlights content (`draft-story`'s RECAP mode explicitly
excludes it).
