---
name: llm-wiki-query
description: >-
  The mandatory default for finding anything in this Campaign OS wiki, before asserting,
  inventing, or assuming any campaign fact. Triggers: "look up", "what do we know about",
  "who/where is", "what happened with", "is there a page for", "what's the current state
  of". Read-only.
---

# llm-wiki-query

The wiki carries hundreds of pages and you hold almost none of them in context. Confidently
inventing a fact that contradicts canon — a renamed NPC, a ship that sank two sessions ago, a
faction that wants the opposite of what you said — is the single worst failure mode in a
sandbox wiki. This skill exists to make that impossible: when a campaign fact matters, retrieve
it instead of guessing (L1).

Two non-negotiables:

1. **Never assert an in-world fact you have not found in a wiki page** (or confirmed is
   genuinely absent). If you can't find it, say so — don't fill the gap with invention.
2. **Gather complete context, not the first hit.** A page rarely stands alone — the NPC links
   to a faction, a situation, a location, a session. Incomplete context produces answers that
   are locally right and globally wrong.

## Name the question's shape first

One line, before any tier — the shape sets how deep the completeness pass must go:

- **factual** ("who is X") — one page + its summary-level neighbors.
- **relationship** ("how do X and Y relate") — both pages, plus any page both link to.
- **multi-hop** ("how is X connected to Z") — walk `[[wikilinks]]` hop by hop, ≤3 hops,
  reporting the chain; no chain in 3 hops → report the gap, don't force one.
- **synthesis** ("compare / summarize everything about") — gather every relevant page
  (summaries first) before writing a word.
- **gap** ("do we know X?") — the absence-answer discipline below is the whole job.

## The tiered method

Climb the tiers in order. **Stop the moment you have a confident, complete answer** — most
lookups never reach Tier 2. Each tier is more powerful and more expensive than the last.

### Tier 1 — grep + qmd search (fast, deterministic)

No LLM needed — you need a match, not a rerank. Always invoke qmd through its `npm run
search:<collection>` script (package.json) — never bare `qmd` — so the collection is explicit
and consistent with every other guardrail in this repo:

```bash
grep -rli "<name>" vault/ --include="transcript.md"                # which files mention it
grep -A2 "^summary:" vault/campaigns/shattered-sea/npcs/<slug>.md                  # read the summary before the body
npm run search:content -- search "<distinctive terms>"       # BM25 keyword, sub-second
```

**Read the summary before the full file** — often the summary is the whole answer. Then Read
the actual matched file directly: qmd/grep tell you *which* file, the file is the source of
truth (full content, line numbers, wikilinks for the completeness pass below).

### Tier 2 — qmd query, semantic (comprehensive, ~15-20s)

Reach here when you don't know the exact vocabulary — conceptual/thematic questions, fuzzy
memory, synonyms — or Tier 1 came up empty or partial:

```bash
npm run search:content -- query "what favor does Nona want from Perrin" --json \
  | jq -r '.[] | "[\(.score)] \(.file)\n\(.snippet)\n"'
```

Use `npm run search --` (no `:<collection>` suffix) to search every collection at once (the
usual entity-resolution move); scope to one when noise from process docs drowns a name (table
below). The `jq` filter drops qmd's per-result `context` blob — pure noise, repeats the
collection description every line.

Need `world`+`pcs`+`sessions`+`external` together? Use `npm run search:wiki --` — one
collection, not four stacked `-c` flags. It's what `inbox:similar` also uses.

Craft a sharper query — `lex`/`vec`/`hyde` fields, an `intent:` line for an ambiguous term
("the Passage" is a faction here, not a hallway) — read
[`references/qmd-querying.md`](references/qmd-querying.md) when the plain single-line form
underperforms; it's the right starting point otherwise.

**Collections in this repo:**

| Collection | npm script | Root | Use |
|---|---|---|---|
| `content` | `search:content` | `vault/` | Canon + pending wiki pages — default for any in-world fact |
| `pcs` | `search:pcs` | `vault/campaigns/shattered-sea/pcs/` | Player-character pages |
| `sessions` | `search:sessions` | `vault/episodes/` | Transcripts, ledgers, recaps — play evidence |
| `wiki` | `search:wiki` | `vault/**/*.md` | Union of vault/campaigns/shattered-sea/pcs/sessions — the way to search all of them together in one collection |
| `external` | `search:external` | `vault/srd/monsters/`, `vault/srd/spells/`, `vault/srd/items/`, `vault/srd/classes/`, `vault/srd/feats/`, `vault/srd/species/`, `vault/srd/backgrounds/` | Recreated GM-expert reference/methodology guides (5e SRD, Sly Flourish's LGMRD/Monster Builder, etc) — not campaign facts; search before improving `vault/_templates/`, skills, or any other campaign-os element (CLAUDE.md Project zone) |
| `guardrails` | `search:guardrails` | `docs/` | Guardrail docs, campaign runbooks, dashboards — process, not canon |
| `archive` | `raw/` | Ingested source queue files, by month — historical, not canon |
| `inbox` | `inbox/` | Files staged for ingestion, not yet processed — empty between ingest runs |

## The completeness pass (always)

A single page is a starting point, not an answer:

- **Follow inline `[[wikilinks]]` and the page's Relationships/Crew/Members sections** — an
  NPC's faction, home location, the situation they're entangled in, the ship they crew.
- **Read summaries first.** For each linked page, `summary:` frontmatter usually tells you
  whether you need the full body.
- **Pull current state.** If the entity appears in an active situation, that present-tense
  state overrides older page prose.

Stop expanding once further pages stop changing the answer — complete enough to be correct,
not the whole vault.

## Reporting what you found

- **Search, then paste — the hit is the answer's spine.** Never paraphrase a canon fact you
  did not just read this turn. `qmd get` or Read the hit, quote it.
- **Cite provenance by page.** Point at the wikilink that owns the fact: *"Otar is Solange
  Barret in disguise ([[otar-the-foul]])."* A claim backed by no wiki page is unestablished.
- **Label the canon tier.** A `status: canon` hit is established; `status: pending`/`draft` is
  prep that hasn't survived the table (project rule 9) — mark it "(pending — not yet canon)."
- **Flag stale canon.** A cited canon page unedited for 5+ sessions (its `updated:` date or
  `git log -1 --format=%ad -- <path>` vs the current session number) gets "(canon — last
  touched sNN)" so the DM knows it may lag the live world. Computed at read time, never stored.
- **Close with what you consulted:** *"Consulted: [[otar-the-foul]], [[kalowe]]."*
- **No hit is an answer.** State "not established in the wiki" — never fill the hole from chat
  memory or a `status: pending`-only hit. Name what you searched: *"No `vault/` page states Otar's
  birthplace — grep and `qmd query` both empty. Unstated; needs a table reveal or a DM ruling."*
- **Surface contradictions, never resolve them silently.** Two pages disagree → append a
  `> [!warning] CONTRADICTION` block to the page and open `canon-review` — never quietly pick
  one (project rule 2).

**Answering at the players' knowledge level.** When the question is "what would the party
know," or anywhere a player can see the answer, answer from Player-Known prose only — skip
every `## DM Only` section and every `status: pending` page (project rule 4, default-deny):

```bash
awk '/## DM Only/{exit} {print}' vault/campaigns/shattered-sea/npcs/otar-the-foul.md   # body up to DM Only
```

If the only hit is under `## DM Only`, the player-facing answer is "the party doesn't know
that."

## Index freshness

A write hook re-indexes the vault after wiki edits, so qmd's keyword search and file list stay
current automatically. Vector embeddings regenerate in the background and lag slightly behind
brand-new pages — a page written this session may not yet surface in `qmd query`, which is
fine, since you already hold it in context; grep and `qmd search` (keyword) catch it
immediately. `qmd status` stale → `qmd update` re-indexes on demand.

## Quick reference

| Need | Tool |
|---|---|
| Find pages by exact name / term | `grep -rli` or `npm run search:content -- search "…"` (Tier 1) |
| Find pages by meaning / concept | `npm run search:content -- query "…" --json \| jq …` (Tier 2) |
| Read a known page | Read the file directly (full content + wikilinks) |
