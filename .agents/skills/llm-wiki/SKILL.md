---
name: llm-wiki
description: >
  Three-layer wiki architecture (raw → wiki → schema), page templates, provenance, and trust model.
  Use for wiki architecture, page templates, provenance markers, confidence/lifecycle, wiki environment variables, or a format/trust question the operating skill does not own.
---

# LLM Wiki — Knowledge Distillation Pattern

## Three-Layer Architecture

### Layer 1: Raw Sources (immutable)

The user's original documents — articles, papers, notes, PDFs, conversation logs, bookmarks, and images. Never modified by the system. Located via `OBSIDIAN_SOURCES_DIR` in `.env`. Images are first-class sources: ingest skills read them via vision support and treat interpreted content as inferred unless verbatim transcribed.

The in-vault `_raw/` staging folder is different: a scratch inbox for quick captures awaiting promotion (see `wiki-capture` and `wiki-ingest`). `wiki-ingest` moves rather than deletes from `_raw/` on promotion, since some files have no other copy.

### Layer 2: The Wiki (LLM-maintained)

Interconnected Obsidian markdown files organized by category — compiled, cross-referenced, navigable. Each page has YAML frontmatter, `[[wikilinks]]`, and provenance. Located via `OBSIDIAN_VAULT_PATH` in `.env`.

### Layer 3: The Schema (this skill + config)

Categories, conventions, page templates, and operational workflows governing wiki structure.

## Wiki Organization

The vault has two levels of structure: **categories** (what kind of knowledge) and **projects** (where the knowledge came from).

### Categories

Organize pages into these default categories (customizable in `.env`):

| Category | Purpose | Example |
|---|---|---|
| `concepts/` | Ideas, theories, mental models | `concepts/transformer-architecture.md` |
| `entities/` | People, orgs, tools, projects | Campaign vault: `entities/{type}/name.md` (depth 1). Generic llm-wiki examples may stay flat. |
| `skills/` | How-to knowledge, procedures | `skills/fine-tuning-llms.md` |
| `references/` | Summaries of specific sources; academic papers use the Paper Deep-Dive Template (below) | `references/attention-is-all-you-need.md` |
| `synthesis/` | Cross-cutting analysis across sources | `synthesis/scaling-laws-debate.md` |
| `journal/` | Timestamped observations, session logs | `journal/2024-03-15.md` |

### Campaign types

When the vault has `wiki/AGENTS.md`, campaign entities still live under llm-wiki categories (`entities/`, `journal/`, …) and also set campaign `type` from that file. Category is the **top-level** folder (`category: entities`); `type` may be a **depth-1** subfolder under that category (`entities/npc/…`). Do not set `category` to the type. Do not invent types. See `wiki/AGENTS.md` Entities path. Campaign **page** filenames use space-free kebab slugs from `title` (FM `title` stays human-readable) — see `wiki/AGENTS.md` § Page filenames (issue #80). Strip legacy `Aruhe` place prefixes and `00`/`00-` prefixes; no spaces.

### Projects

Project-specific knowledge lives under `projects/<project-name>/<category>/`. General knowledge goes in the global category directory. Cross-reference between them with wikilinks.

```
$OBSIDIAN_VAULT_PATH/
├── projects/
│   ├── my-project/
│   │   ├── my-project.md      ← overview (named after project, not _project.md)
│   │   ├── concepts/          ← project-scoped category pages
│   │   └── ...
├── concepts/                   ← global (cross-project) knowledge
├── entities/
└── ...
```

**Naming rule:** Overview file must be `<project-name>.md` — Obsidian's graph view uses filenames as labels; `_project.md` makes every project node identical.

Project overview page frontmatter: `title`, `category: project`, `tags`, `source_path` (Claude project path), `created`, `updated`. Body: one-paragraph summary, then `## Key Concepts` and `## Related` with wikilinks.

## Special Files

Every wiki has these files at its root:

### `index.md`
A content-oriented catalog organized by category. Each entry has a one-line summary and tags. Rebuild this after every ingest operation. Format:

```markdown
# Wiki Index

## Concepts
- [[transformer-architecture]] — The dominant architecture for sequence modeling ( #ml #architecture)
- [[attention-mechanism]] — Core building block of transformers ( #ml #fundamentals)

## Entities
- [[andrej-karpathy]] — AI researcher, educator, former Tesla AI director ( #person #ml)
```
**Format rule**: Add a space after the opening `(` and tags.
❌ Don't: `description (#tag)` — breaks tag parsing
✅ Do: `description ( #tag)` — proper spacing and tag parsing

### `log.md`
Chronological append-only record tracking every operation. Each entry is parseable:

```markdown
## Log

- [2024-03-15T10:30:00Z] INGEST source="papers/attention.pdf" pages_updated=12 pages_created=3
- [2024-03-15T11:00:00Z] QUERY query="How do transformers handle long sequences?" result_pages=4
- [2024-03-16T09:00:00Z] LINT issues_found=2 orphans=1 contradictions=1
- [2024-03-17T10:00:00Z] ARCHIVE reason="rebuild" pages=87 destination="_archives/..."
- [2024-03-17T10:05:00Z] REBUILD archived_to="_archives/..." previous_pages=87
```

### `.manifest.json`
Tracks every ingested source — path, timestamps, wiki pages produced. Backbone of delta/append/staleness detection. See `wiki-status` for full schema.

**Canonical source keys.** MUST be absolute paths with `~` and env vars expanded (e.g. `/Users/me/.claude/projects/.../abc.jsonl`, never `~/.claude/...`). Mixed forms let the same file be tracked twice, causing re-ingestion. Always expand before comparing or writing. Repair with `scripts/manifest.py normalize <vault>`.

**Recording provenance.** Populate `pages_created` and `pages_updated` with vault-relative paths so re-ingestion can find pages to revisit.

## Page Template

When creating a new wiki page, use this structure:

```markdown
---
title: Page Title
category: concepts
tags: [ml, architecture]
aliases: [alternate name]
relationships:
  - target: "[[concepts/related-concept]]"
    type: extends
sources: [papers/attention.pdf]
summary: One or two sentences, ≤200 chars, so a reader (or another skill) can preview this page without opening it.
provenance:
  extracted: 0.72
  inferred: 0.25
  ambiguous: 0.03
base_confidence: 0.65
lifecycle: draft
lifecycle_changed: 2024-03-15
tier: supporting
created: 2024-03-15T10:30:00Z
updated: 2024-03-15T10:30:00Z
---

# Page Title

One-paragraph summary of what this page covers.

## Key Ideas

- The source's central claim, paraphrased directly.
- A generalization the source implies but doesn't state outright. ^[inferred]
- A figure two sources disagree on. ^[ambiguous]

Use [[wikilinks]] to connect to related pages.

## Open Questions

Things that are unresolved or need more sources.

## Sources

- [[references/attention-is-all-you-need]] — Original paper
```

## Paper Deep-Dive Template

Academic papers (arXiv/conference) with load-bearing figures or equations use a richer body template instead of the generic Page Template. See [`paper-template.md`](paper-template.md).

## Provenance Markers

Every claim has one of three provenance states. Framework defaults — a vault's `AGENTS.md` may extend them.

| State | Marker | Meaning |
|---|---|---|
| **Extracted** | *(no marker — default)* | A paraphrase of something a source actually says. |
| **Inferred** | `^[inferred]` suffix | An LLM-synthesized claim — a connection, generalization, or implication the source doesn't state directly. |
| **Ambiguous** | `^[ambiguous]` suffix | Sources disagree, or the source is unclear. |

Example:

```markdown
- Transformers parallelize across positions, unlike RNNs.
- This is why they scale better on modern hardware. ^[inferred]
- GPT-4 was trained on roughly 13T tokens. ^[ambiguous]
```

**Frontmatter summary:** Optionally surface the rough mix at the page level so the user can scan for speculation-heavy pages without reading them:

```yaml
provenance:
  extracted: 0.72   # rough fraction of sentences/bullets with no marker
  inferred: 0.25
  ambiguous: 0.03
```

These are best-effort numbers written by the ingest skill at create/update time. `wiki-lint` recomputes them and flags drift. The block is optional — pages without it are treated as fully extracted by convention.

## Typed Relationships

Plain `[[wikilinks]]` in page bodies carry no semantic weight — they indicate "related to" but not *how*. The optional `relationships:` frontmatter block adds typed, directional edges to the knowledge graph.

### The `relationships:` block

```yaml
relationships:
  - target: "[[Transformer Architecture]]"
    type: extends
  - target: "[[LSTM]]"
    type: contradicts
  - target: "[[Attention Mechanism]]"
    type: implements
```

Each entry has two required fields:
- `target` — a wikilink (using the same format as `OBSIDIAN_LINK_FORMAT`) to the related page
- `type` — one of the allowed semantic types below

### Allowed relationship types

The table below is the framework default allowlist. A vault's `AGENTS.md` may extend it; consumers must use the effective allowlist and preserve owner semantics without coercion.

| Type | Meaning | Example |
|---|---|---|
| `extends` | This page builds on or generalises the target | GPT extends Transformer Architecture |
| `implements` | This page is a concrete realisation of the target concept | BERT implements Masked Language Modelling |
| `contradicts` | This page's claims conflict with or refute the target | Evidence A contradicts Evidence B |
| `derived_from` | This page is based on or adapted from the target | Fine-tuning is derived from Transfer Learning |
| `uses` | This page depends on or relies on the target | RAG uses Vector Databases |
| `replaces` | This page supersedes or deprecates the target | GPT-4 replaces GPT-3 |
| `related_to` | Catch-all: related but no stronger directional type applies | Concept A is related to Concept B |

### Rules

- **Optional** — omit the block if no typed relationships are known. Untagged wikilinks are treated as `related_to` by `wiki-export`.
- **Direction matters** — the declaring page is the *source*; `target` is the destination.
- When in doubt, use `related_to` or omit.

Consumers: `wiki-export` (typed edges), `cross-linker` (writes typed entries), `wiki-query` (multi-hop path queries via bounded BFS over `relationships:` adjacency, frontmatter-only).

## Confidence and Lifecycle

Every page carries two orthogonal trust signals plus an optional supersession link. Framework defaults below — a vault's `AGENTS.md` may extend lifecycle values or make trust fields optional.

Lint/trust consumer schema: `OBSIDIAN_ALLOWED_LIFECYCLES`, `OBSIDIAN_ALLOWED_RELATIONSHIP_TYPES`, `OBSIDIAN_REQUIRED_TRUST_FIELDS`, `OBSIDIAN_SCHEMA_SOURCE`. Precedence: CLI > environment/config > framework defaults (lifecycle and relationship extensions additive). Explicit blank values fail closed. `wiki-lint/SKILL.md` owns invocation.

### Required fields

```yaml
base_confidence: 0.65          # [0.0, 1.0] — time-independent quality estimate. Stored once, recomputed on content change.
lifecycle: draft               # draft | reviewed | verified | disputed | archived
lifecycle_changed: 2024-03-15  # ISO date of last state transition
# lifecycle_reason: "..."      # optional free-text — why the state changed; surfaced by wiki-query
# superseded_by: "[[new-page]]" # wikilink; only when lifecycle=archived
```

`lifecycle_reason` and `superseded_by` are optional. Never fabricate them.

### Confidence formula

The formula is a **manual base score**, not a deterministic URL classifier:

```
base_confidence = lineage_count_score * 0.5 + source_quality_score * 0.5

lineage_count_score  = min(independent_evidence_lineages / 3, 1.0)
source_quality_score = avg(reviewed quality score per independent lineage)
```

After calculating the raw score, assess whether the evidence covers the page's material claims. Partial coverage may justify keeping or lowering the score; unsupported material claims require source/claim repair before any confidence change. Avoid small score churn without meaningful epistemic change.

**Source-quality scores** (use the highest-matching bucket):

| Bucket | Score | Examples |
|---|---|---|
| `paper` | 1.0 | arXiv, conference proceedings |
| `official` | 0.9 | `*.gov`, vendor docs |
| `documentation` | 0.85 | well-maintained third-party docs |
| `book` | 0.8 | books, technical references |
| `repository` | 0.75 | content-addressed repository/code evidence |
| `blog` | 0.55 | personal blogs |
| `session_transcript` | 0.5 | conversation history or completed operation |
| `forum` | 0.4 | Stack Overflow, HN, Reddit, issue-grade reports |
| `unknown` | 0.4 | catch-all/current config |
| `llm_generated` | 0.3 | LLM synthesis or unvalidated memory seed |

**An independent evidence lineage** is an origin that can corroborate a claim independently. Canonical source IDs remain useful for identity, but identity alone does not prove independence. Collapse dependent evidence before counting:

- files, releases, and commits from one repository → one repository lineage;
- retry/review/fix tasks in one workstream → one task lineage;
- parent/child Kanban records → one task lineage;
- byte-identical memories across profiles → one memory lineage;
- a snapshot plus the mutable source it captures → one lineage;
- aliases or metadata references resolving to one origin → one lineage.


**Per-skill defaults** (ingest skills compute this automatically):

| Skill | base_confidence | lifecycle |
|---|---|---|
| `wiki-ingest` (URL) | `0.17 + 0.5 × classify(url)` | `draft` |
| `wiki-ingest` (single doc) | per-source classifier | `draft` |
| `wiki-ingest` (multi-doc) | `min(N/3,1)×0.5 + avg_q×0.5` | `draft` |
| `wiki-research` | varies, often 0.85+ | `draft` |
| `wiki-capture` | 0.42 | `draft` |
| `*-history-ingest` | 0.42 | `draft` |
| `wiki-update` | 0.59 | `draft` |
| `wiki-synthesize` | `min(input_pages.base_confidence)` | `draft` |

### Lifecycle state machine

Five states. **`stale` is not a state** — it is a computed overlay: `is_stale = (today − updated) > 90 days`.

| State | Entered by | Notes |
|---|---|---|
| `draft` | Any ingest skill on first write | Default for all new pages |
| `reviewed` | Human edit only | |
| `verified` | Human edit only | Time alone never demotes verified pages |
| `disputed` | Manual edit only | Overrides every state except `archived` in display |
| `archived` | Manual edit, or ingest skill setting `superseded_by` | Terminal |

Only ingest skills set `draft`. All other transitions require a human editor. Update `lifecycle_changed` whenever the state changes.

## Importance Tiering

`tier:` controls ingest update priority and retrieval ordering.

### Three tiers

| Tier | Meaning | Ingest behavior | Query priority |
|---|---|---|---|
| `core` | Load-bearing pages — many other pages depend on them (high incoming-link count or bridge position). Always worth updating. | Always update if the source is even marginally relevant | Surfaced first in index and full-read passes |
| `supporting` *(default)* | Standard wiki pages with moderate connectivity | Update when the source has clear new claims for this page | Standard priority |
| `peripheral` | Low-connectivity pages — rarely linked, narrowly scoped | Skip unless the source is *primarily* about this topic | Last resort; skipped when trimming to context budget |

### Assignment rules

- **New pages:** default to `tier: supporting`
- **Promote to `core`:** when a page accumulates ≥5 incoming wikilinks **or** is flagged as a bridge by `wiki-status` insights mode
- **Demote to `peripheral`:** when a page has ≤1 incoming link and hasn't been updated in 90+ days
- **Human override always wins** — edit `tier:` manually to lock a page at any level
- Existing pages without `tier:` are treated as `supporting` (backward compatible — no migration needed)

### Consumers

`wiki-ingest` (update gating), `wiki-query` (retrieval ordering), `wiki-status` insights (tier suggestions — never auto-writes), `wiki-lint` (flags missing `tier:`).

## Retrieval Primitives

Use the cheapest primitive that answers the question — **escalate only when insufficient**.

| Need | Primitive | Relative cost |
|---|---|---|
| Does a page exist? What's its title/category/tags? | Capped `qmd`/`rg` / frontmatter grep first; full `index.md` only if needed | **Cheapest** |
| 1–2 sentence preview of a page | Read the `summary:` field in its frontmatter | **Cheap** |
| A specific claim or section inside a page | `Grep -A <n> -B <n> "<term>" <file>` — returns only the matching lines plus context | **Medium** |
| Whole-page content | `Read <file>` | **Expensive** — last resort |
| Relationships across pages | `Grep "\[\[.*?\]\]"` across the vault, or walk wikilinks from a known page | Case-by-case |

**Search commands:** prefer ripgrep (`rg`) when available; fall back to `grep`/`find`. Capitalized `Grep`/`Glob` are tool-generic primitives.

Consumers: `wiki-query`, `cross-linker`, `wiki-lint`, `wiki-status` (insights). New vault-reading skills cite this section. Anti-patterns scanned by `scripts/context-waste-scan.py` — see `docs/agents/context-waste-method.md`. First-turn file cost and ranked skill load: `wiki health` → `context`; follow `context.act`.

## QMD Index Freshness

QMD is an optional search index; the markdown vault is the source of truth. Write skills refresh QMD after vault writes via `scripts/qmd-maintain.sh` (use `--embed` only for explicit foreground embedding). If QMD refresh fails, keep vault changes and report status separately. Read-only skills do not refresh QMD.

## Core Principles

Core principles in AGENTS.md (compile don't retrieve, track everything, connect with wikilinks, frontmatter required, single source of truth, keep context warm) are always loaded. These extend them:

1. **Compound over time.** Each ingest makes the wiki smarter, not just bigger. Merge into existing pages, resolve contradictions, strengthen cross-references.
2. **Provenance matters.** Every claim traces to a source. Note which source prompted each update.
3. **Mark inferences.** Default = extracted. `^[inferred]` for synthesis, `^[ambiguous]` for contested claims.
4. **Human curates, LLM maintains.** The human decides what to add and what to ask. The LLM handles bookkeeping.

## Link Format

All internal links connecting wiki pages are controlled by `OBSIDIAN_LINK_FORMAT` from the resolved config (default: `wikilink`).

| Setting | Syntax | Example |
|---|---|---|
| `wikilink` *(default)* | `[[path/to/page]]` or `[[path/to/page\|display text]]` | `[[concepts/foo\|foo]]` |
| `markdown` | `[display text](relative/path.md)` | `[foo](../concepts/foo.md)` |

### Generating markdown-format links

When `OBSIDIAN_LINK_FORMAT=markdown`:
1. Compute the path from the **current file's directory** to the **target `.md` file** using `..` to climb up as needed.
2. Use the page title or a natural phrase as display text.
3. Always include the `.md` extension.

| Current file | Target | Relative link |
|---|---|---|
| `index.md` | `concepts/foo.md` | `[foo](concepts/foo.md)` |
| `concepts/foo.md` | `entities/bar.md` | `[bar](../entities/bar.md)` |
| `projects/my-project/my-project.md` | `concepts/foo.md` | `[foo](../../concepts/foo.md)` |
| `projects/my-project/concepts/arch.md` | `entities/bar.md` | `[bar](../../../entities/bar.md)` |

Affects only newly written or updated links — existing vault content is not migrated (use `cross-linker` or `wiki-lint` for that).

## Config Resolution Protocol

**All skills must resolve config using this algorithm — do not hard-code `.env` or `~/.obsidian-wiki/config` directly.** This ensures single-vault, multi-vault, project-local, and VPS setups all work correctly.

### Resolution order

0. **Inline vault override (`@name`)** — if the user's request contains an `@<name>` token (e.g. `@work save this`, `query @personal about X`), resolve `~/.obsidian-wiki/config.<name>` directly and use its `OBSIDIAN_VAULT_PATH`. This **overrides** both the CWD `.env` walk-up and the active symlink, and applies to **that invocation only** — never run `ln -sf` or otherwise change the active vault for an `@name` request. If `~/.obsidian-wiki/config.<name>` doesn't exist, tell the user it doesn't exist and list the available vaults (the `wiki-switch` **List** logic), then stop — do **not** silently fall back to the default. The `@name` is a routing directive, not content: strip it out before treating the rest of the request as the actual instruction or page text.
1. **Walk up from CWD** — look for a `.env` file in the current directory, then each parent, up to `$HOME`. Stop at the first `.env` that contains `OBSIDIAN_VAULT_PATH`.
2. **Global config** — if no local `.env` found, read `~/.obsidian-wiki/config`.
3. **Prompt setup** — if neither exists, tell the user: "No config found. Run `wiki-setup` to initialize your wiki."

`@name` is a **per-invocation override** — it targets one vault for one request. `/wiki-switch <name>` is the **persistent default** — it re-points the active symlink for all future requests.

### Vault-scoped state

Skills that write runtime state (e.g. `daily-update`) must scope that state to the resolved vault, not to a global path. Use:

```
VAULT_ID=$(echo "$OBSIDIAN_VAULT_PATH" | md5sum 2>/dev/null || md5 -q - <<< "$OBSIDIAN_VAULT_PATH" | cut -c1-8)
STATE_DIR="$HOME/.obsidian-wiki/state/$VAULT_ID"
```

### Standard "Before You Start" block

Every skill's setup section should read:

> **Resolve config** — follow the Config Resolution Protocol in AGENTS.md. Honor an inline `@name` override first, then walk up from CWD for `.env`, fall back to `~/.obsidian-wiki/config`, else prompt setup. This gives `OBSIDIAN_VAULT_PATH` and any tool-specific path overrides.

## Environment Variables

Configured via `.env` (see `.env.example`). Only `OBSIDIAN_VAULT_PATH` is required.

- `OBSIDIAN_VAULT_PATH` — Where the wiki lives **(required)**
- `OBSIDIAN_SOURCES_DIR` — Where raw source documents are
- `OBSIDIAN_CATEGORIES` — Comma-separated list of categories
- `WIKI_SKIP_PROJECTS` — Comma-separated substrings; any project dir whose name contains one is excluded from history ingest (scan + delta + manifest). See the "Project Scoping" step in the history-ingest skills.
- `CLAUDE_HISTORY_PATH` — Where to find Claude conversation data
- `CODEX_HISTORY_PATH` — Where to find Codex session data
- `HERMES_HOME` — Where to find Hermes agent data
- `OPENCLAW_HOME` — Where to find OpenClaw data
- `COPILOT_HISTORY_PATH` — Where to find Copilot session data
- `OBSIDIAN_LINK_FORMAT` — Internal link syntax: `wikilink` (default) or `markdown`
- `WIKI_TOKEN_WARN_THRESHOLD` — Emit a warning in `wiki-status` when the full-wiki token estimate exceeds this value (default: `100000`). Set to `0` to disable. See `wiki-status` for the token footprint report.
- `CODE_UNDERSTANDING_BACKEND` — how wiki-update understands a project before distilling: `auto` (CodeGraph when available, else builtin ast-extract + rg; default), `builtin`, or `codegraph` (explicitly require; warn/error if unavailable).
- `CODE_UNDERSTANDING_CODEGRAPH_BIN` — optional path to the codegraph binary when it isn't on PATH.

No API keys are needed — the agent running these skills already has LLM access built in.

## Modes of Operation

The wiki supports three ingest modes:

| Mode | When to use | What happens |
|---|---|---|
| **Append** | Small delta, incremental updates | Compute delta via manifest, ingest only new/modified sources |
| **Rebuild** | Major drift, fresh start needed | Archive current wiki to `_archives/`, clear, reprocess all sources |
| **Restore** | Need to go back | Bring back a previous archive |

Use `wiki-status` to see the delta and get a recommendation. Use `wiki-rebuild` for archive/rebuild/restore operations.

