# recap.md and highlights.md — full field spec

## Writing recap.md

Instantiate `vault/_templates/_episodes/_session_recap.md`
if starting fresh (copy it, don't retype the frontmatter block from
memory). Fill in:

- Frontmatter: `type: session`, `subtype: recap`, `status: pending`, `publish: false`,
  `created:`/`updated:` (today's real date), `number:`, `date:`, `title:` from the
  session directory / `vault/episodes/<NN-slug>/ingest-review.md` header.
- `# Session {NN} — {Title}`
- `## Recap` — player-facing prose, what happened as the players
  experienced it, built from the pages the `ingest(sNN)` commit touched,
  with transcript color. Wikilink every named entity on first mention.
  Keep the narrator's voice consistent with the prior recap you read in
  step 2. Close on the open question, threat, or hook the next session
  picks up — this closing line is what that session's run-guide `## Recap`
  `[!read-aloud] Last Time` box quotes or restates almost verbatim to cut
  straight into its opening moment
  (`vault/_templates/_episodes/_session_recap.md`) — write it as a handoff, never a
  self-contained ending.
- `## Highlights link` and `## Ingest review link` — plain path
  references (backticked path, not `[[wikilinks]]`) to
  `vault/episodes/NN-slug/highlights.md` and `vault/episodes/NN/ingest-review.md`
  respectively — the latter may already be deleted by RECAP time
  (`vault/refs/runbook-ingest.md`); link the path anyway, it's a provenance
  pointer, not a live-file guarantee. Every session's highlights file
  shares the same basename (`vault/episodes/<NN-slug>/highlights.md`) across sessions — a bare
  `[[highlights]]` would be ambiguous the moment a second session exists.
  A plain path reference sidesteps that collision entirely; don't
  wikilink either of these two.

`## Recap` is 300–450 words. Hook by sentence two. Every sentence earns
its place (`vault/refs/qc-recap.md`).

## Finding and writing the highlights

For each page the `ingest(sNN)` commit touched (and any
other transcript passage worth surfacing), read the transcript around
its cited passage and apply this three-step filter:

- **In-world filter (Hard Rule 7).** Is this a character speaking,
  acting, or something the DM narrates about the world — or is it table
  talk about something outside the fiction? Keep only the former.
- **Walk to the natural boundary.** The transcript packs long
  utterances into single lines; a quote clipped mid-thought reads as
  garbled. Read one or two lines either side of your landing point and
  cut the quote at a real sentence boundary, not an arbitrary L-number.
- **Speaker is already resolved.** `vault/episodes/<NN-slug>/transcript.md` carries `**Name:**`
  labels from the CAPTURE labeling pass — attribute directly, no
  external speaker map needed.

Write `vault/episodes/NN-slug/highlights.md`: instantiate
`_templates/session-highlights.md` (own `created`/`updated`, today's real date),
`## Quotes` (3–8 entries,
`**[[wikilink|Speaker]]** (L{n}): "verbatim quote"`), `## Moments`
(1–3 one-line entries, each citing an L-number or the touched page it
comes from). Note candidates you discarded as OOC only if it's cheap to
do inline while working — it is not a required section.

**Adversarial continuity pass.** If `.claude/agents/continuity-checker.md`
is present, spawn the `continuity-checker` subagent over the drafted
`vault/episodes/<NN-slug>/recap.md` (`vault/refs/runbook-agents.md`) — it greps `vault/ vault/campaigns/shattered-sea/pcs/ vault/episodes/` for
every claim and returns `CLEAR` or `CONFLICT:` blocks. For each CONFLICT,
fix the recap to match canon; if the canon page is the one that looks
wrong, don't touch it — open `canon-review` instead (L2). Absent →
`NOTED: continuity-checker not built — skipped adversarial pass`.
