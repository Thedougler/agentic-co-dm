# Line passes — three passes with disjoint jobs

Reached from [SKILL.md](../SKILL.md)'s `DS6`. Line editing over a **finished**
draft. Every pass returns findings first — inline markup plus Polish Notes —
and applies nothing until the GM approves. Developmental work (structure,
pacing, dialogue, POV) is `content-fixer`'s job — it runs unprompted on any
edited vault file (`vault/refs/stories/developmental-craft.md`), not a step in
this pass; canon-continuity is `continuity-checker`'s.

## Pick the pass and the register

No pass number given -> ask: "Pass 1 (correctness), 2 (refinement), or 3
(final sweep)?" — suggest the target's `edit_pass` frontmatter value + 1 where
the key exists. Then identify the audience; the register decides how hard
Pass 2 bites:

| Register | Pass 2 removes | Pass 2 keeps |
|---|---|---|
| Player-facing (a story, read-aloud, handouts, lore flavor, recap prose) | AI vocabulary, metronomic rhythm, em-dash asides, filler, synonym cycling | Lush imagery, long flowing sentences, sensory density, dramatic weight |
| DM-facing (run guides, prep notes, DM-intel, page body facts) | Everything above PLUS all significance inflation, promotional language, any prose where a table or list would scan faster | Terseness. DM prose is scannable or it is wrong |

Player-facing evocative prose is *supposed* to be lush. A pass that flattens
voice has failed. Read `vault/refs/stories/prose-aesthetic.md` before judging
any stylistic choice — a pattern it declares intentional is never a finding.

## Pass 1 — Correctness

Fix what is broken: grammar, syntax, punctuation, agreement, tense drift.
Never chase style — a phrase that is grammatically fine but stylistically weak
gets a "Pass 2: <reason>" note, not a fix (style fixed twice drifts twice).
Polish Notes are one line: what was corrected and why.

## Pass 2 — Refinement

Assume errors are fixed; this is the assertive pass — the full de-slop
catalog, walked in order over the whole draft
(`vault/refs/stories/ai-tells.md` holds every pattern with fixes and examples):

1. **Structure tells** — formulaic section shapes, every-list-same-length,
   identical paragraph sizes. Vary lengths; let some sections end without a bow.
2. **Significance inflation** — "testament to", "pivotal moment",
   promotional-brochure words (vibrant, nestled, breathtaking). Delete; state
   the specific fact. Hits DM-facing prose hardest; earned drama stays on
   player-facing prose.
3. **AI vocabulary** — Tier 1 on sight (delve, tapestry, realm-as-filler,
   leverage, myriad); Tier 2 in clusters. The fix is often restructuring, not
   a synonym swap.
4. **Grammar tics** — copula avoidance ("serves as" -> "is") when clustering,
   superficial -ing tails, negative parallelisms, forced rule-of-three,
   synonym cycling, false ranges.
5. **Rhythm and burstiness** — metronomic 15-25-word sentences -> mix short
   punches with long builds; em-dash discipline (count first); strip
   mechanical boldface and inline-header lists.
6. **Hedging and filler** — "it's worth noting", "in order to", hedge stacks
   ("could potentially"), vague attributions, generic closers ("only time
   will tell"). Say the thing.
7. **Transitions** — Moreover/Furthermore/Additionally -> the real logical
   connector, or nothing; let paragraph breaks do the work.
8. **Concision** — Strunk's rules ([concision.md](concision.md)): active
   voice, positive form, concrete language, omit needless words, emphatic
   word last.

Distracting word repetitions: offer up to three alternatives in the note,
never force one. Pass 2 Polish Notes carry two parts on one line —
`what was done | rationale` — so the GM can judge each change cold.

## Pass 3 — Final sweep

Read as if seeing the text fresh. Flag only what genuinely sticks out — a
slipped error, anything that makes a reader pause involuntarily. Minimal by
design: never re-litigate Pass 2's calls, never new scope. Proposing many
changes -> stop and recommend another Pass 2 instead of continuing (an
escalating final pass is a runaway, not rigor).

## Output — findings first, always

For each paragraph with findings: the paragraph with inline ~~strikethrough~~
deletions and **bold** additions, followed by its Polish Note, numbered
sequentially across the document (PN1, PN2…). Clean paragraphs are skipped,
not echoed. Process the whole document; no commentary outside the notes.
Read-aloud text additionally gets the read-it-aloud test — it is literally
spoken at the table; flag anything no DM would say to a live room.

## Approve, apply, record

The GM approves all, some, or by number ("apply all but PN4") — never apply an
unapproved finding, never treat silence as approval. Apply only approved
changes as targeted Edits, never a whole-file rewrite. More than 40 changed
lines on a pending page -> review in chunks of 20 (project rule 7). Then set
the target's `edit_pass:` frontmatter to this pass's number where the key
exists (this file is that key's only writer); absent key on a legacy page ->
leave frontmatter untouched. Stories carry no frontmatter, so `edit_pass`
never applies to them. Re-run repo lint on the file.

## Rules

1. **Style-only.** Never change a fact, a proper noun, a `[[wikilink]]` target
   or its display text, frontmatter beyond `edit_pass`, or a quote attributed
   to a speaker (highlights quotes are verbatim by `recap-writer`'s contract).
2. **Proper nouns never rotate.** One name per entity, wikilinked on first
   mention; a plain pronoun is fine, an epithet is not.
3. **Count before claiming.** "Em-dash overuse" or "uniform rhythm" gets
   asserted only after actually counting; never from an impression.
4. **Preserve what's already human.** A clean paragraph is left untouched;
   sanding away every irregularity produces the very uniformity this pass
   removes.
5. **Quoted material is exempt.** Text inside quotation marks, code blocks, or
   cited from a transcript is never rewritten.
6. **Nothing applies unapproved.** Findings -> GM decision -> edits, every
   pass, no exception for "obvious" fixes.
7. **Facts are never fixed here.** Unsure whether a name, spelling, or claim
   is right? Look it up via `llm-wiki-query` — never "fix" it inline. A fact
   that looks wrong gets `NOTED (not done): <claim> <file:line>`; fact fixes
   belong to the owning prep guide.

External cross-references: `vault/refs/stories/language-edit.md`
(an equivalent three-pass language-editing system in a different
fiction-writing vault) and
`vault/refs/stories/writing-style-profile.md` (an equivalent
author-aesthetic-profile mechanism paralleling
`vault/refs/stories/prose-aesthetic.md`).
