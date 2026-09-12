# The LLM-wiki pattern: why this system compiles instead of retrieves

This is the theory layer — the *why* behind the whole session loop. The
`campaign-os` skill's reference files describe mechanisms; this one names the
parent pattern those mechanisms serve, so a weak model can tell a load-bearing
rule from a cosmetic one. Read it once to understand the system; the
operational contracts live elsewhere (`_templates/<type>.md`,
`vault/refs/`).

## Source and credit

Campaign OS is a domain specialization of **Andrej Karpathy's LLM Wiki**
pattern (original gist:
<https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>). Two
sentences carry the whole idea:

> "The LLM writes and maintains the wiki; the human reads and asks questions."
> "The wiki is a persistent, compounding artifact — knowledge is compiled once
> and kept current, not re-derived on every query."

Karpathy's framing: Obsidian is the IDE, the LLM is the programmer, the wiki is
the codebase. Campaign OS keeps that frame exactly — the repo **is** the vault
**is** the codebase — and hardens it for a domain where getting a fact wrong
(an NPC's motive, who knows a secret) breaks the fiction and can't be silently
patched later.

## Compile, don't retrieve — and why it beats chat-memory and RAG

Three ways a model can answer "what does the party know about Otar?":

1. **Chat memory** — recall it from the context window. Fails silently: the
   model invents or drifts a fact and sounds exactly as confident as when it's
   right. This is **canon drift**, failure mode #1, and law **L1** ("grep,
   don't remember") exists solely to ban it.
2. **RAG** — search the raw transcripts at query time and synthesize an answer
   from chunks. Re-derives the same knowledge on every query, re-runs every
   inference, and can resurface a fact the table has since overturned because
   the raw chunk still says it.
3. **Compile** (this system) — the knowledge was already distilled *once*, at
   INGEST time, into a maintained `vault/` page. The query hits
   pre-synthesized, cross-referenced, canon-tiered content. One grep, one read,
   done.

The wiki is a **compiled artifact**, not a cache of the transcripts. INGEST
doesn't summarize a session into a new page and stop — it updates *every*
`vault/` page the session touched, resolves contradictions, and strengthens
cross-links. Each ingest makes the wiki smarter, not just bigger. That is the
whole return on the pipeline's cost, and the reason the session loop is shaped
the way it is.

## The three layers, mapped to this repo

Karpathy's `raw/ → wiki/ → schema` becomes a **four**-stage flow here, because
the campaign domain inserts a human-checkpointed compile step (law **L2**) that
a personal knowledge base doesn't need:

| Karpathy layer | Campaign OS | Notes |
|---|---|---|
| **raw/** (immutable sources) | `vault/episodes/NNN/transcript*.md`, legacy exports | Never edited after the INGEST gate. The transcript is evidence; every canon fact must trace to a line in it (L1). |
| *(the compile step)* | `vault/` pages themselves (including `vault/campaigns/shattered-sea/pcs/`), written at `status: canon` + `vault/episodes/NNN/ingest-review.md` | The stronger-than-Karpathy addition: raw table-talk never edits canon without evidence — INGEST writes the real page directly at `status: canon`, citing the transcript (a session transcript is the highest form of canon this repo has). `vault/episodes/NNN/ingest-review.md` (a small resume pointer + `REVIEWED-BY-HUMAN:` gate, not a fact-bearing ledger) is a human spot-check, not a promotion gate — there is no separate promotion step. |
| **wiki/** (compiled, LLM-maintained) | `vault/` (including `vault/campaigns/shattered-sea/pcs/`) | Template-typed pages, canon-tiered, cross-linked. DM-authoritative. |
| **schema** (the rules) | the `llm-wiki` + `campaign-os` skills, `vault/_templates/`, `vault/refs/runbook-*.md` runbooks | Tells the model *how* to maintain the wiki, mechanically. |

Where Karpathy has a single "the LLM owns wiki/" write path, Campaign OS splits
it: **transcripts write ledgers; ledgers write the wiki** (L2). No step reads
raw table-talk and edits `vault/` in one move. That split is what makes canon
safe and any half-finished ingest resumable from its ledger checkboxes.

## The four mechanisms adopted from the pattern

These are Karpathy-family mechanisms Campaign OS adopts wholesale, tuned to the
domain. All four are **backward-compatible optionals**: a page without them is
valid and treated as the default. No existing page needs backfilling for them
to work.

### 1. Importance tiering — `tier: core | supporting | peripheral`

As the wiki grows past a few hundred pages, re-reading every page on every
ingest wastes tokens. `tier:` (optional frontmatter, default `supporting`)
concentrates effort where connectivity is highest:

| tier | What it is | INGEST behavior | Retrieval priority |
|---|---|---|---|
| `core` | Load-bearing hub — many pages link in (a region, a major faction, the party, a recurring NPC). | Update if the source is even marginally relevant. | Surfaced first in index/full-read passes. |
| `supporting` *(default)* | Normal page, moderate connectivity. | Update when the source has clear new facts for it. | Standard. |
| `peripheral` | One-off, rarely linked (a walk-on NPC, a single-scene location). | Skip unless the source is *primarily* about it. | Last; dropped first when trimming to budget. |

Assignment: new pages default `supporting`; promote to `core` at **≥5 incoming
wikilinks** or when it's a graph bridge; demote to `peripheral` at **≤1 incoming
link and untouched for 5+ sessions**. Human override always wins. This directly
serves the migration's per-round token-cut ratchet: tiering is *why* a hub page
is worth blowing the ratchet on and a walk-on isn't.

### 2. Page summary — `summary:` (≤200 chars, one sentence)

A one-line gist in frontmatter so a reader — or another skill — can preview a
page without opening its body. This is the cheap rung of the retrieval ladder
below: `grep -A2 "^summary:" vault/campaigns/shattered-sea/npcs/*.md` answers "who is this NPC" for
fifty pages at a fraction of reading fifty bodies. Optional; a page without it
falls back to being read in full.

### 3. The retrieval-primitive ladder

The ladder table lives in this skill's `.claude/skills/llm-wiki/SKILL.md` (single source of truth —
every read-side skill follows it). Rationale: reading the vault is the
dominant cost of every read-side operation; a 20-page wiki forgives
full-vault scans, a 400-page one does not.

### 4. Provenance — page-level only

Campaign OS tracks provenance two ways: page-level `created:`/`updated:`
frontmatter (when a page was born and last updated) and git history (which
commit, which session, changed a given line). Neither needs an inline marker
— `git log -p <path>` or `git blame` answers "where did this come from"
without polluting the prose. The `status:` canon tier answers *whether* a
fact is true in the world now, and CONTRADICTION blocks handle two
pages/sources disagreeing.

A DM-only synthesized claim — a motive, connection, or implication no source
states outright — is written in plain prose rather than tagged:

```markdown
## DM Only
- Otar sailed the southern reach before the Sundering.
- Not stated outright, but the timeline suggests he's building toward a play
  against the Waveservants.
- His arrival date in Kalowe is given two ways across sources: s3, and "a
  year prior" — unresolved.
```

Saying the hedge in the sentence itself carries the same information as a
tag would, without adding a syntax a weaker model has to learn and apply
consistently. **Player-Known facts are stated as fact by construction**
(they were revealed at the table), so hedged phrasing belongs under
`## DM Only` or on a `status: pending` page, never in Player-Known prose. A wiki that hides
its guessing rots silently; one that says it plainly stays trustworthy.

## What this pattern offers that Campaign OS deliberately does NOT adopt

Not everything in the extended LLM-wiki ecosystem earns its keep here. Two
mechanisms are declined on purpose — record the reason so no future round
"helpfully" adds them back:

- **Confidence scoring (`base_confidence: 0.0–1.0`).** Declined. In a knowledge
  base, sources vary in reliability and a float estimates that. In a campaign,
  canon is **binary** — a fact was revealed at the table (or DM-ruled) or it
  wasn't — and the `status:` tier already carries that signal exactly. A
  0.0–1.0 score on a canon fact is false precision no skill would act on.
- **Typed `relationships:` frontmatter.** Declined. Campaign relationships live
  as prose + wikilinks in the `## Relationships` / `## Crew` / `## Members`
  sections, which is where the DM reads them. A parallel typed-edge block in
  frontmatter duplicates that (violating rule 6, one fact one page) to power a
  graph feature nothing in this repo consumes. Plain `[[wikilinks]]` +
  Obsidian's own graph view suffice.
- **Automatic page merging (wiki-dedup's `--auto`).** Declined — the merge, not
  the detection. Merging two pages is destructive and, in this domain, a wrong
  merge fuses two distinct entities into corrupt canon (La Vasca is a *district
  of* Calveno, not a spelling of it). So the **detection** half is folded (W17
  surfaces same-entity duplicate candidates, report-only) but the **merge** is
  human-gated through canon-review — never a score threshold, never a script
  picking a winner (project rule 6). A future round must not wire an auto-merge.

- **A setup/bootstrap skill (wiki-setup).** Declined. Repo bootstrap is a
  one-time event this repo is past; incremental building is owned by the
  `campaign-os` skill's `.claude/skills/campaign-os/references/instruction-levers.md` plus
  `guardrails-kit`,
  and new content types by `content-type-scaffold`. A standing skill for a
  verb that fires ~never is pure context load.

The **maintenance** folds this pattern *did* adopt (beyond the four page-level
mechanisms above) are operational, not page-format, so they live in their own
specs: same-entity duplicate detection (W17) and redirect stubs
(format: `canon-review` skill § Workflow step 3; linting: `npm run lint -- --rules` W17/W18), the
human-gated merge procedure (`canon-review` skill § Workflow), and the graph
insights / `tier:` suggestion report.

## How the pattern maps onto the six laws

The six laws in the `campaign-os` skill aren't arbitrary — each enforces one face of this
pattern. If you ever wonder why a law is strict, this is the answer:

| Law | Pattern principle it enforces |
|---|---|
| **L1** grep, don't remember | Compile, don't retrieve — never answer from chat memory. |
| **L2** extraction ≠ application | The human-checkpointed compile step (transcript → ledger → wiki). |
| **L3** default-deny publishing | The wiki is DM-authoritative; player visibility is opt-in, not a leak. |
| **L4** templates, not freeform | Schema layer — a page that doesn't conform stops being queryable. |
| **L5** numbers, not judgment | Countable thresholds a weak model complies with (tier promotion at ≥5 links, ≤200-char summary). |
| **L6** every NEVER carries a replacement | Compile-safe operability under pressure. |
