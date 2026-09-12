
# Draft — Class

A 5e SRD class or subclass, transcribed from the 2024 Player's Handbook's own
class-table format. Not a narrative page — these are vendored rules
material, and their real external standard is the SRD document itself, never
invention. Done means every trait, table row, and feature reads identically
to the source it was transcribed from.

## Template

Two templates, one per page shape:

- `vault/_templates/_srd/_class.md` — for a class. Fixed headings: `## Core
  <Class> Traits`, `## Becoming a <Class>` (OPTIONAL — only when the class's
  entry path needs explanation beyond the Core Traits table), `## <Class>
  Class Features` (a leveled table plus one `### Level N: <Feature>` heading
  per feature), `## <Class> Subclass: <Subclass Name>` (OPTIONAL — only when
  the class's own subclass is detailed inline rather than on its own page).
- `vault/_templates/_srd/_subclass.md` — for a subclass. Fixed heading:
  repeat `## Level <N>: <Feature>` once per feature the source grants, in
  level order.

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — PC agency, NPC independence.
3. `vault/refs/vault/_common/hard-rules.md` — shared rules; bind this type, never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now, paste the output.

`DF1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **Transcription, Not Invention.** These are transcriptions of the 2024
  SRD's own class-table format, not narrative pages. Every trait, table row,
  and feature is copied from the source text; no source, no page.
- **Two Templates, Two Types.** A class page is `type: class`
  (`vault/_templates/_srd/_class.md`); a subclass page is `type: subclass`
  (`vault/_templates/_srd/_subclass.md`). Never merge the two shapes onto one page unless the
  class template's own OPTIONAL `## <Class> Subclass: <Subclass Name>`
  section applies.
- **Homebrew Never Lives Here.** A HOMEBREW class or subclass is `type: rule`
  and belongs to the `rule-prep` skill, never this guide or these templates.
- **`source:` Is Required.** Point it at the `raw/` archive path the page
  was transcribed from (e.g. `raw/2026-07/05_Fighter.md`); set
  `source_url:` when an up-to-date external source also exists
  (`.claude/rules/external-guides.md`).
- **Wikilink Every Grant.** A feature naming a spell, feat, or other page ->
  inline `[[slug|Display Name]]` at first mention.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- Class or subclass — which template?
- The source text for this transcription — a `raw/` archive path (fills
  `source:`), plus a live `source_url:` if one exists?
- Does the class need `## Becoming a <Class>` (an entry path beyond the Core
  Traits table), and does its own subclass belong inline or on a separate
  subclass page?
- Every level the source grants a feature — one `### Level N: <Feature>`
  (class) or `## Level N: <Feature>` (subclass) heading each, in level order?

## Before you ship

- [[vault/refs/vault/_common/lifecycle|Lifecycle]]: `vault/refs/vault/_common/lifecycle.md`
- Gaps: `vault/refs/vault/_common/degrade.md`
- [[vault/refs/vault/_common/handoffs|Handoffs]]: `vault/refs/vault/_common/handoffs.md`
- Boundaries: `vault/refs/vault/_common/out-of-scope.md`
- Common checklist: `vault/refs/vault/_common/checklist.md`

## Out of scope

- A HOMEBREW class or subclass — `rule-prep`'s domain, never this guide
  (the Homebrew Never Lives Here rule above).
- Any other vendored SRD reference type (spells, feats, backgrounds,
  species, monsters) — `find-guidelines`.
