# wiki-cli

The wiki-lint and wiki-indexing engine (`utils/wiki-cli/`): the linter, `VaultIndex`,
SQLite relationship graph, PageRank, vault organiser, and query layer that validate and
analyse the campaign wiki. Campaign OS's process backbone — all other tools consume its
outputs.

## Language

**Finding**:
One violation reported by a linter against one file. A finding has exactly
two valid dispositions: fixed, or escalated to the human for a ruling. It is
never exempted, deferred, or annotated as acceptable
(`docs/adr/0005-lint-findings-block-on-presence-not-severity.md`).
_Avoid_: "warning" as a synonym for a finding that may be left alone — see
Severity below. Avoid "pre-existing", "by-design", "intentional", "vendored"
and "NOTED (not done)" as dispositions; each names a reason not to fix, which
is not one of the two.

**Severity**:
A finding's triage rank for a human reading a sweep — `error` or `warning` on
a rule in `utils/wiki-cli/src/wiki_cli/rules/`. It orders attention and nothing else:
it does not decide whether a finding blocks, and it is not a licence to
proceed past one (`docs/adr/0005-lint-findings-block-on-presence-not-severity.md`).
_Avoid_: "severity" as a synonym for enforcement level, and "it's only a
warning" as a reason to move on — enforcement keys on a finding's presence,
not its rank.

**Backlink**:
An inbound wikilink — the `links-in` count on a page equals its backlink
count. Queried via `wiki links in PAGE`.
_Avoid_: "inbound reference" (vague — a backlink is specifically a wikilink).

**Outlink**:
An outbound wikilink from a page to another. Queried via `wiki links out PAGE`.
_Avoid_: "forward link" (ambiguous with HTML hyperlinks).

**Orphan** (link-graph sense):
A page with zero backlinks in the query scope — no other page links to it.
A report (`wiki links orphans`), never a lint finding (ADR-0038).
_Avoid_: "dead page" (an orphan may be valuable, just undiscovered).

**Redundant link**:
The same source→target wikilink repeated within one section of a page.
Cross-section repeats are intentional (each section stands alone) and not
redundant.
_Avoid_: "duplicate link" for cross-section repeats — those are fine.

**Link graph**:
The `links` edge table over the whole vault, `_templates` included. Queries
scope it (`--include-templates` to surface templates); the index never
excludes.
_Avoid_: "link index" (collides with the `VaultIndex` class, which is broader).

**Template**:
A file at `_templates/<type>.md` — the sole source of truth for a content
type's frontmatter shape, required headings, and enum values
(`vault/_templates/CLAUDE.md:1-4`). Consumed by an agent reading the file
directly, never by Obsidian's Templater plugin at runtime. Three verbs act on
it, each a distinct operation, never interchangeable: **scaffold** creates a
brand-new `_templates/<type>.md` for a type that has none
(`content-type-scaffold` skill); **instantiate** authors one real page from an
existing template's shape (a `-prep` skill's normal job); **conform** repairs
an existing page's drift back to its template's current shape after the
template changed (`content-fixer` agent).
_Avoid_: "Templater template" / "Obsidian template" as a synonym for this
sense. Avoid "scaffold"/"instantiate"/"conform" interchangeably — each names a
different operation on a template.

### Expanded PageRank (ADR-0051)

The vocabulary of the three-signal importance system (`wiki build-gravity`,
`wiki build-agent-access`, `wiki report-hot-pages`). All three scores live on `page_metrics`.

**Structural rank**:
The weighted power-iteration PageRank over the vault link graph. Typed frontmatter
relationship edges (CONTAINS, LOCATED_AT, etc.) carry a 3× multiplier over body wikilinks.
Stored as `page_metrics.pagerank`. Measures objective narrative centrality — how much
of the wiki's link fabric flows through a page.
_Avoid_: "PageRank" unqualified when the distinction from player_gravity or agent_reads matters.

**Player gravity**:
A page's accumulated player attention, derived from corrected session transcripts. The
extractor agent writes `(page, session_num, mention_count)` rows to `page_interactions`
during transcript ingest; gravity score is derived from these at `wiki build-gravity` time.
Three tiers: `active` (mentioned in last N sessions), `encountered` (any prior session),
`unencountered` (default). Stored as `page_metrics.player_gravity` (float) and
`page_metrics.gravity_tier` (text).
_Avoid_: conflating with structural rank — player gravity measures player engagement, not
narrative link-graph centrality.

**Agent reads**:
Rolling count of deliberate `Read` tool calls on a vault page across recent sessions,
tracked via `PostToolUse` hook and ingested by `wiki build-agent-access`. Stored as
`page_metrics.agent_reads`. Diagnostic only — never used to mutate search rankings.
High agent_reads flags context cost concentration; divergence from structural rank and
player gravity identifies unnecessary or misrouted reads.
_Avoid_: "agent gravity" — agent_reads is a diagnostic counter, not a gravity signal.

**Gravity tier**:
The categorical label for a page's player gravity: `active`, `encountered`, or
`unencountered`. Derived from `page_interactions` at build time; window configurable
in `wiki.toml [gravity] active_window`.
_Avoid_: using tier as a ranking signal in isolation — it is a label derived from
mention recency, not a continuous score.

### Vault organiser (ADR-0049)

The vocabulary of the dynamic vault organiser (`wiki organize` / `npm run vault:organize`).
The organiser computes cluster groupings from the vault's relationship graph and
materialises them as folder groups on disk.

**Cluster**:
A set of vault files the organiser groups into one on-disk folder, detected by running
community detection (Louvain) over the vault's weighted relationship graph. A cluster is
viable only when both viability thresholds pass; below either threshold the candidate
dissolves into its parent or stays ungrouped.
_Avoid_: "type folder" for a cluster — a type folder is the old static taxonomy the
organiser replaces; a cluster is a detected, data-driven grouping that may contain many types.

**Anchor**:
The node within a viable cluster that the cluster's folder is named after — the file with
highest intra-cluster centrality. A typed frontmatter key (e.g. `location:`, `within:`)
overrides the computed centrality when explicit. A genuine tie with no frontmatter signal
fires `ANCHOR_AMBIGUOUS` lint and the file stays in its current location.
_Avoid_: "anchor" in the campaign fiction sense — use "anchor" only in the organiser domain;
in fiction, prefer "home port", "seat", or the entity's own name.

**Viability threshold**:
The pair of criteria both required for a candidate cluster to be materialised: minimum
file count (default 4) AND minimum intra-cluster link density (default 0.4). Either
failing dissolves the candidate. Both values are configurable in `wiki.toml [organizer]`.
No hard-coded depth limit — nesting continues only while each sub-cluster also passes
both thresholds.
_Avoid_: treating either threshold as the sole gate — it is always AND, never OR.

**Slug mandate**:
The requirement that every wikilink in the vault uses slug-only format:
`[[slug|Display Text]]`. Path-based links (`[[path/to/slug|Display Text]]`) are
prohibited because the organiser moves files, making path-based links stale on every
reorganise. Enforced by the `PATH_WIKILINK` lint rule; a one-time migration scrub converts
all existing path-based links before the first organiser run.
_Avoid_: "filename link" or "path link" as synonyms — slug mandate is the canonical term.
