# Claim buckets — full source-typing and decomposition reference

Read this when triaging a source (§ Source types) or decomposing a `ready` source into
claims (§ Claim buckets onward). Page types and their structure come from
`ls _templates/` and the template files themselves, not this file — this
file holds triage rules and routing judgment calls a template can't answer.

## Source types (triage)

Classify each source file against this table before deciding ready/blocked/skipped.

| Type | Signs | Primary output |
|---|---|---|
| `entity-source` | Named NPC, item, or creature details | `npc`/`item` template + reciprocal links |
| `location-source` | A place, settlement, dungeon, travel site | `location` template, or a page tree for a multi-part settlement |
| `faction-source` | Group agenda, membership, moves, a named pressure | `faction` template; Front clocks per SKILL.md Hard Rule 4 |
| `quest-source` | A plot thread with beats and an outcome state | `quest` template |
| `rules-or-homebrew` | Mechanics, table rulings, class/subclass options | `rule` template — open `_templates/rule.md` for its `subtype:` enum and mechanics format; a rules-library file whose frontmatter matches its whole sub-pile verbatim (uniform audience/status/publish) carries an export default, not a reveal signal — land it `pending` unless a transcript shows the table using it |
| `handout-or-player-facing` | In-world text meant for players | `lore` template, `audience`/`publish` left for the DM (this skill never sets `publish: true`) |
| `session-record` | Session number, chronology, "what happened last time" | **Hand off** to `transcript-label`/`transcript-ingest` — never decomposed here |
| `character-sheet` | Ability scores, class/level, equipment for a PC | **Hand off to decompose** (chain-load `dnd5e-character-interview`/`combat-profiles`) — PC creation is a canon-review-signed event. Match on the TARGET too: source frontmatter `subtype: pc` or a `vault/campaigns/shattered-sea/pcs/`-dir path refuses even when the body is narrative prose, not stats. The PDF itself still gets copied verbatim into `_assets/character-sheets/` (SKILL.md § Owned paths) — that copy is not decomposition, it happens regardless of hand-off |
| `pc-tactical-note` | DM-side primer/levers/spotlight guidance keyed to an existing PC (dm/ primers) | **Refuse** — natural home is that PC's `## Arc Notes (DM Only)`, which no ingest skill may originate (PC-page boundary); queue-flag for the DM. NOTE: no skill currently owns Arc Notes authoring — flagged gap |
| `internal-equivalent-check` | System/meta doc whose function campaign-os already provides (interview guides, process docs, hub/index pages) | **Map, don't duplicate** — hunt the equivalent: FIRST `grep -rn "<source filename/section keywords>" .claude/skills/*/SKILL.md` (a skill may name the file's replacement verbatim), then `.claude/rules/skills.md` + `docs/` + `vault/refs/`; queue-file records source → equivalent + coverage gaps; no wiki page |
| `asset` | Image, audio, or map file | **Hand off** to `battlemap-render` (maps) or `visual-aids` (art) — triage only |
| `research-or-guidance` | Process notes, writing standards, meta material, a design/craft methodology with no campaign-specific facts | `guide` template, the source's topically-appropriate `vault/refs/` directory (`stories/`, `ideas/`, `vault/<type>/`, or flat at the top level for cross-cutting doctrine — `vault/refs/README.md` indexes the split) — condensed for agent consumption; `skipped` only when `internal-equivalent-check` already covers the same territory, or the DM says it's not worth keeping |
| `narrative-island` / `sandbox-run-guide` | Prospective DM run-guide for a locale: Strong Start, Planned Events, NPCs, Clocks (frontmatter often says so) | **Map, don't migrate** — run guides are `draft-run-guide`'s to build fresh from live wiki state; event groupings are run-guide-scoped only (U8). Embedded fact-seeds count as canon only where a session record corroborates them — cite THAT source via its own ledger line, never this document |
| `conversational-source` | Turn-taking data that is NOT a session transcript: a Discord/chat log of between-session RP, a DM planning chat, a CSV/TSV of names, a Q&A doc | Identify the format, then cluster claims by topic (§ Unstructured & conversational sources below) and route each into the type row above it matches — never a template of its own |

## Unstructured & conversational sources

A handed-over source can be turn-taking data rather than a document: a Discord/chat
export, a DM planning chat, a CSV/TSV of names, a Q&A doc. Identify the format first
(timestamps, user/turn markers, delimited columns — when in doubt, just read it),
then distill substance — **never summarize message-by-message.** Cluster extracted
claims by **topic**, not by speaker turn or row order: a 50-message planning chat
about three NPCs yields three NPC claims, not fifty. Skip greetings, meta-conversation,
and repetitive back-and-forth. Route each clustered claim into the normal triage (the
table above) and Claim buckets below — the fidelity-only contract still applies (Hard
Rule 1): cluster and cite, never invent connective tissue the turns didn't state.

An actual session transcript — chronological table-play, even one that's only ever
existed as a chat log — is not this row: Hard Rule 5 hands it to `transcript-label`/
`transcript-ingest` regardless of its raw format.

## Temporal discipline — historical vs planned (R7 codification)

- **Historical (played) material**: `canon` ONLY with a play citation (this
  repo's `vault/episodes/`; source-repo session evidence during migration, per the
  status ladder). A recap/log of play = `session-record` row (hand off,
  LEGACY-SOURCE gate). An op-log/change-log of the source wiki itself =
  `internal-equivalent-check` (log.md precedent — its function here is
  `raw/INGESTED.tsv` + `git log`; this project keeps no standing
  progress-tracking ledger file — git log is the history).
- **Planned/future (unplayed) material**: NEVER canon, never recap-visible.
  Durable entity facts from a planned pile → `vault/` page at
  `status: pending`, ladder rung 1 (soul-incarnate precedent). Run-guide/
  staging material → map, don't migrate (session-05 precedent; a missing
  recap/day-file census in the source repo proves unplayed). Migration
  owned paths are `vault/` only (including `vault/campaigns/shattered-sea/pcs/`), at
  `status: pending` (ss7-planned-runguide gap).
- **Resolved situations**: absorb as history — Lifecycle: resolved / DM Only
  past events — never as live pressure; source sections superseded by the
  outcome are dropped and noted in the queue file (nonas-favor precedent).

## Ready, blocked, or skipped

Mark `ready` only when:
- The source's authority is clear (raw notes, DM-authored, or already-established
  legacy canon — state which in the queue line).
- The claim's target page type is clear from the table above.
- No unresolved DM judgment changes what would be written.

Mark `blocked` when:
- Two sources (or a source and existing canon) conflict — CONTRADICTION block first,
  then re-triage as blocked pending canon-review, not silently `ready`.
- Entity identity is ambiguous (could be an existing page or a new one).
- The source needs a Front's clock fields but doesn't state them (Hard Rule 4) — write
  the identity portion `ready`, leave the Front itself `blocked` pending `.claude/skills/draft-content/references/faction.md`.

Mark `skipped` when:
- It's process/research material with no campaign content (`research-or-guidance`,
  DM confirms it's not canon-bound).
- It's a duplicate of a more authoritative source already ingested (grep the target
  page's `sources:`/citations first — if this exact source path is already cited
  there, it's already been processed).
- The DM explicitly says not to ingest it.

A `skipped` line stays in the queue file, checked, with the reason inline — visible
history of the decision, not a silent drop.

## Claim buckets

Run `ls _templates/` for the current page types, then open the matching
`_templates/<type>.md` for the claim: its frontmatter, headings, and
`<!-- AGENT: ... -->` comment give the structure and the prep skill to
chain-load (`vault/_templates/CLAUDE.md` — templates are the sole source of
truth for content shape). No separate mapping table is kept here; the
following are judgment calls a template can't answer — which type a claim
routes to, or that it routes to none:

- A named individual with relationships is an `npc`; a generic/reusable
  kind with no individual identity is a `creature`.
- A multi-part settlement fidelity-transcribes as a parent `location` page
  plus child `location` stubs (`location-prep`'s settlement-subtype
  page-tree pattern) — never invent a Theme/Goal/Rides the source doesn't
  state.
- A faction pressure with a stated trigger and consequence goes in
  `## Goals & Fronts` using the Front template (`world-update`'s §
  "The Front" is the authoritative field list) — transcribe verbatim, this
  is formatting existing facts, not authoring a new Front. A stated
  timeframe with no segment count ("~2 more seasons") goes into the Clock
  field in the source's own words, never converted to `N segments`.
- A faction pressure without a stated trigger/consequence gets its identity
  portion only; flag the Front as incomplete and route to `.claude/skills/draft-content/references/faction.md`
  (Hard Rule 4).
- A pressure/situation with no owning faction has no template type —
  situations absorb into faction Fronts by design. Write the identity
  facts into whatever linked page's body prose already exists, flag it in
  the queue file, and ask the DM (Degrade by asking).
- A portable scenario cluster ("island") decomposes onto the owning entity
  pages (location/npc/faction claims) — it is never a page of its own.
  Event groupings are run-guide-scoped only — events appear within the run guide's
  thread structure — never a standalone artifact. Owning pages don't exist yet?
  Flag and stop; don't originate a page tree the ledger line doesn't name.
- A structural note (what changed, why) goes in the queue file's
  `## Flags` or the wave's commit message — never a wiki page of its own.

## Extraction pass

One pass for facts, not prose, per source:
- Names and aliases.
- Places and paths between them.
- Relationships stated between entities.
- Decisions, promises, threats, debts already resolved in the source (not
  speculation).
- Faction moves, deadlines, clocks — only if the source states the mechanics.
- Rules/rulings as written.
- Secrets the source explicitly marks as hidden/DM-only.
- Open questions the source itself flags as unresolved.

Use exact source wording only for names, quoted dialogue, and table-critical phrasing.
Rewrite everything else into concise wiki reference text — but never add a detail,
motive, or consequence the source doesn't supply (Hard Rule 1). This is the one place
this skill's fidelity contract most resembles the legacy skill's canon discipline: a
claim promoted past what the source actually says is the same failure whether it
happens during transcript ingest or source ingest.

## Canon discipline — do not promote a claim if it is

- Speculation the source itself labels as a guess or rumor (still a `lore`/`quest`
  claim, but frontmatter `status` stays `draft`/`pending`, never migration-mode
  `canon`, and cite it as speculative in the body).
- An inference this skill is making rather than something the source states.
- A possible future outcome rather than an established fact.
- Vague enough that no specific page can own it ("the crown", "a sailor," "the old
  temple") — per Stub Creation below, only concrete referenced entities get stubs.

## Writeback order

1. Create missing concrete stubs first (so links don't dangle).
2. Update owner pages with the claim's facts.
3. Add reciprocal links for durable relationships.
4. Flag incomplete Fronts/situations rather than inventing their missing fields.
5. Check the claim off in the queue file.

## Stub creation

Create a stub only for a concrete entity or place the source names with enough
identity to route — never for a vague reference.

Minimum stub: copy the real `_templates/<type>.md` for the claim's type
verbatim (L4) — don't retype its headings from memory, and don't invent a
generic shape here, since each type's required H2s differ (`npc`:
Stats & Combat/Relationships/Session Log; `location`: Notable NPCs/Hooks/
Session Log; `faction`: Members/Goals & Fronts/Session Log; etc. — W5 reads
the authoritative list straight off each template). Fill the frontmatter
(`status: draft`, `publish: false`, `tags: [stub]`) and add one line of flat
body prose:

```markdown
Stub created during llm-wiki-ingest from `<source path>`. Needs DM expansion
before use at table.
```

Fill in only the sections the source actually supplies content for; leave the
rest with the stub note above rather than inventing filler. Once the stub
check (SKILL.md Standard queries) finds this page on a later source, expand
it in place — the second source's claims append, they don't overwrite what
the first source established, unless it explicitly supersedes (Contradictions
below).

## Contradictions

When two sources — or a source and existing canon — conflict on the same claim:

1. Append a CONTRADICTION block to the page being written (exact
   format: `transcript-ingest` SKILL.md § Contradictions — quote both claims, cite both paths, name the detecting process as
   `llm-wiki-ingest: <source-slug>`).
2. Leave the page's existing content untouched; do not silently prefer either version.
3. Flag it in the queue file's `## Flags` section with both source paths.
4. Continue to the next claim — a contradiction blocks that one claim, not the wave.
5. `canon-review` (human-in-the-loop skill) resolves it later; this skill never picks
   a winner (Hard Rule 7).
