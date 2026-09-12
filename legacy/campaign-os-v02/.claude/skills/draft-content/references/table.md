
# Draft — Table

Random-roll generator tables — loot, rumors, NPC traits, wilderness
finds, town events, names. A table row is a deliberately open-ended GM
prompt to elaborate live at the table, not an asserted campaign fact —
that's the entire point of a random table, and is why `type: table`
pages are exempt from the wiki's entity-linking and invented-mystery
checks (W25, W63 — `npm run lint -- --rules`). Writing a row
as if it were settled canon (naming a specific NPC, committing to a
specific cause) defeats the point; keep rows generic enough to reroll
and reuse across sessions. Its real external standard is the 5e SRD/DMG's
own d100-table format — confirmed against the SRD trinkets
table's `| d100 | Trinket |` shape, ranged rows included — not a
Forgotten Realms Wiki genre; already matched by this vault's existing
table shape.

## Template

`vault/_templates/_refs/_table.md` — copy it, never retype it from
memory. [[vault/refs/vault/quest/references/structure|Structure]] freely with whatever `## Category`/`### Subcategory`
breakdown the table set needs — no fixed sub-headings, unlike most
content types.

## Read first — before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `vault/refs/vault/_common/hard-rules.md` — the shared rules bind
   this type where they apply (a table has no `pending`→`canon`
   lifecycle — see § Owned paths — so the lifecycle-specific rules don't
   bind).
3. Stub check: `grep -ril "<table topic>" vault/refs/table-*.md`. A hit
   that already covers the topic → expand it in place, add rows or a new
   `## Category`/`### Subcategory` section, never create a duplicate
   table page for the same topic.

`DT1: <files read, stub-check output pasted>`.

## Two paths

- **Migrating an existing source document** (a table from a published
  book, a blog, an archived note) → load `find-guidelines`; this is
  faithful recreation, not authoring — preserve every entry, dice range,
  and category exactly as the source states them, only formatting
  adapts. Set `source:` (the `raw/` path) and `source_url:` (if any) in
  frontmatter.
- **Authoring an original homebrew table** → invent freely. Leave
  `source:`/`source_url:` blank.

## Hard rules — this type only

- **DMG Table Shape.** Each table is a markdown table headed
  `| NdX | <Column Header> |` (e.g. `| 1d20 | NPC Trait |`), rows
  numbered to match the die's full range.
- **Terse Rows.** A phrase or one sentence, a seed to elaborate live,
  never a paragraph.
- **Generic, Not Canon.** A row that reads like a finished campaign fact
  (naming a specific existing NPC or location by page name) has stopped
  being a generic table entry — cut it back to the generic prompt, or it
  belongs on that entity's own page instead.
- **Split Only When It Earns It.** Split a table into
  `campaigns: [Shattered Sea]`-scoped and setting-neutral tables only
  when the campaign-specific rows genuinely outnumber the generic
  ones — otherwise one page, `campaigns:` left at its default.

## Cross-skill coordination

- **`draft-run-guide`** cites specific tables inline
  (`vault/refs/table-<page>.md` § Category) when a scene needs a quick
  roll — this guide never authors run-guide content itself.
- **A row's prompt gets rolled and actually used at the table** → the
  resulting fact belongs on the relevant entity's own page (an NPC's
  `vault/campaigns/shattered-sea/npcs/` page, a location's
  `vault/campaigns/shattered-sea/locations/` page), written by that
  content type's own drafting guide or by `transcript-ingest` once
  played — never back-filled onto the table page itself.

## Before you ship

Lifecycle `vault/refs/vault/_common/lifecycle.md` (this type has no
`canon` promotion and no DM Review Gate — § Owned paths below) · gaps
`vault/refs/vault/_common/degrade.md` · handoffs
`vault/refs/vault/_common/handoffs.md` · boundaries
`vault/refs/vault/_common/out-of-scope.md` · then
`vault/refs/vault/_common/checklist.md` (Toy-field and PC-Connection
items don't apply — a table has neither; the template-instantiation,
heading-lock, wikilink, and lint items still do).

## Out of scope

- A single concrete stat block, NPC, item, or location — their own
  drafting guides.
- Promoting a table row to canon once rolled — the owning entity's page,
  via its own drafting guide or `transcript-ingest`.
- Anything with a `status: pending`→`canon` lifecycle — tables don't
  have one.

## Owned paths

`vault/refs/table-*.md` only. `status: draft`, `publish: false` — tables
don't carry the `pending`→`canon` lifecycle other content types do (a
table is a standing tool, not a fact that survives contact with the
table); no DM Review Gate, no approval step. Every `type: table` page is
exempt from the unlinked-mention check (W25, checked by frontmatter
`type`, not path) — rows are rolled on, not browsed to, so don't force a
cross-link for one.
