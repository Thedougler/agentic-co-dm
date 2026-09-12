# qmd querying reference

Read this when a plain `npm run search:<collection> -- query "..."` underperforms and you need
to craft a sharper query. For everyday lookups, the single-line form in `.claude/skills/llm-wiki-query/SKILL.md` is enough —
start there. Every example below still runs through `npm run search:<collection> --` (or bare
`npm run search --` when no collection shortcut fits) — never invoke `qmd` directly, per
`.claude/skills/llm-wiki-query/SKILL.md`'s Tier 2 note.

qmd returns paths as `qmd://<collection>/<relative-path>`. Strip the prefix and Read the real
path directly (e.g. qmd://vault/campaigns/shattered-sea/npcs/otar-the-foul.md → `vault/campaigns/shattered-sea/npcs/otar-the-foul.md`) —
reading directly gives full content, line numbers, and the page's wikilinks for the
completeness pass in `.claude/skills/llm-wiki-query/SKILL.md`.

## The three query types

`qmd query` accepts a single auto-expanding line (recommended default) **or** a multi-line
document where each line is typed `lex:`, `vec:`, or `hyde:`. Don't mix `expand:` with typed
lines — it's one or the other.

| Type | Method | Give it | Best for |
|---|---|---|---|
| `lex` | BM25 keywords | 2–5 exact terms, no filler | Names, slugs, distinctive jargon, stat-block terms |
| `vec` | Vector similarity | A full natural-language question | Conceptual / thematic recall when you don't know the vocabulary |
| `hyde` | Vector on a hypothetical answer | 50–100 words of what the answer *would* look like | Hard questions where you can describe the answer better than ask it |

The first query in a document gets 2x weight in fusion — lead with your best guess.

## Writing each type

**lex** — keyword precision:
- 2-5 terms, drop articles and filler.
- Exact phrase: quote it — `"sending stone"`.
- Exclude a term: minus prefix — `umberlee -storm` (lex only; not valid in vec/hyde).
- Prefix match is automatic: `perr` matches "Perrin".

**vec** — semantic question:
- Write the actual question in full: `"how is the Uncertainty being repaired in Calveno"`.
- Include context that disambiguates: name the place, faction, or PC involved.

**hyde** — hypothetical document:
- Write a short paragraph in the *vocabulary you expect in the result*, as if it were the
  answer. The retriever matches your fake answer against real pages.

## Combining for hard questions

| Situation | Approach |
|---|---|
| You know the exact term | `lex` only (or just `npm run search:content -- search "..."`) |
| You don't know the vocabulary | single-line `npm run search:content -- query "..."` (auto-expand) or `vec` |
| You want best recall | `lex` + `vec` together |
| Complex / multi-faceted topic | `lex` + `vec` + `hyde` |
| Ambiguous term (e.g. "the Passage") | add an `intent:` line |

Multi-line example:

```bash
npm run search:content -- query $'lex: Nona Black-Jaw favor\nvec: what does Nona want from Perrin in return for the sending stone' \
  --json | jq -r '.[] | "[\(.score)] \(.file)\n\(.snippet)\n"'
```

## intent — disambiguation

`intent:` does not search on its own; it steers expansion, reranking, and snippet selection
when a term is ambiguous in this world. Example: "the Passage" is a faction here, not a
hallway — `intent: the smuggling faction led by Nona` keeps results on-target.

```bash
npm run search:content -- query $'intent: the smuggling faction, not a corridor\nlex: passage'
```

## Output hygiene

`--json` returns objects with `docid`, `score`, `file`, `title`, `context`, `snippet`. The
`context` field repeats the collection description on every result — pure noise, always
project it away:

```bash
npm run search:content -- query "..." --json | jq -r '.[] | "[\(.score)] \(.file)\n\(.snippet)\n"'
```

Or keep structured fields without the noise: `jq 'map(del(.context))'`.

## Collections (this repo)

| Collection | npm script | Root |
|---|---|---|
| `content` | `search:content` | `vault/` |
| `pcs` | `search:pcs` | `vault/campaigns/shattered-sea/pcs/` |
| `sessions` | `search:sessions` | `vault/episodes/` |
| `wiki` | `search:wiki` | `vault/**/*.md` — union of vault/campaigns/shattered-sea/pcs/sessions |
| `external` | `search:external` | Vendored 5e SRD reference material (`vault/srd/monsters/`, `vault/srd/spells/`, `vault/srd/items/`, `vault/srd/classes/`, `vault/srd/feats/`, `vault/srd/species/`, `vault/srd/backgrounds/`) — GM-expert reference/methodology guides, not campaign facts |
| `guardrails` | `search:guardrails` | `docs/` — guardrail docs, campaign runbooks, dashboards |
| `archive` | `search:archive` | `raw/` |
| `inbox` | `search:inbox` | `inbox/` |

Need `content`+`pcs`+`sessions` together? Use `npm run search:wiki --` — one
collection, not three stacked `-c` flags; add `-c external` alongside it for
vendored SRD/craft reference too.

## Maintenance commands (rarely needed by hand — a write hook handles it)

These have no dedicated npm script — invoke bare `qmd` directly for them:

| Command | Effect |
|---|---|
| `qmd status` | Index health, collection counts, staleness |
| `qmd update` | Re-index changed files (fast; lex/get freshness) |
| `qmd embed` | Regenerate vector embeddings (slow; semantic freshness) |
| `qmd get qmd://<collection>/<path>` | Fetch one indexed doc (prefer Reading the real file) |
