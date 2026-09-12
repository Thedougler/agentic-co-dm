
# Draft — Species

An SRD species/race recreated verbatim, or a setting-native people authored
to the same shape. Its real external standard is the 5e SRD document's own
mechanical species format, not a narrative wiki.

## Template

`vault/_templates/_srd/_species.md` — copy it, never retype it from
memory. One shape for every species, SRD or homebrew. Fixed
headings: the stat block (Creature Type/Size/Speed/traits), an OPTIONAL
lineage table, `## Related` (OPTIONAL per the template's own condition).

## Read first — before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `vault/refs/vault/_common/hard-rules.md` — the shared and
   mechanical-type rules bind this type, never restated below.
3. `vault/refs/vault/_common/queries.md` — run the stub check now:
   `ls vault/srd/species/ vault/campaigns/shattered-sea/species/homebrew/ | grep -i "<species name>"`.
   A hit → expand that page in place, never duplicate.

`DS1: <three files read, stub-check output pasted>`.

## Hard rules — this type only

- **Verbatim For SRD.** A `vault/srd/species/` page -> every trait is
  transcribed from the source text, never paraphrased; no source, no page.
- **Wikilink Every Grant.** A trait naming a spell, class, or other page ->
  inline `[[slug|Display Name]]` at first mention.
- **Culture Stays Off This Page.** Cultural depth, an NPC connection, or
  demographic presence -> its own page (`.claude/skills/draft-content/references/lore.md`,
  `.claude/skills/draft-content/references/npc.md`, or an existing lore page), linked from
  `## Related`.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- SRD transcription (confirm the source text/citation) or homebrew
  original (confirm the campaign facts driving the traits)?
- Does the source present a lineage/ancestry/heritage choice as a table
  (e.g. Elven Lineages, Draconic Ancestors)? Only then does the template's
  `Table:` block apply.

## Magic grounding

Whenever this page describes a species trait with magical classification implications — a biological or inherited ability a player spell (Detect Magic, Counterspell, Dispel Magic) could interact with, or explicitly cannot — add a `> [!mechanic]` callout. Fill only the fields that apply; omit the rest.

| Field | Required | Notes |
|---|---|---|
| **Tradition** | yes | Arcane / Divine / Primal |
| **School** | yes | One of the eight SRD schools; `unclassifiable` for effects beyond the taxonomy |
| **Spell analogue(s)** | if meaningful | Closest SRD spell(s) or a named homebrew ritual |
| **Homebrew element** | if homebrew | One line on what it adds or differs from SRD |
| **Detect Magic** | yes | School + one sensory sentence, read-aloud ready |
| **Identify** | omit | Biological traits do not receive an Identify block |
| **Counterspell** | if non-obvious | yes / no / not applicable + one-line reason |

Tradition taxonomy: [[magic-in-the-shattered-sea]].

## Before you ship

- Lifecycle — `vault/refs/vault/_common/lifecycle.md`
- Gaps — `vault/refs/vault/_common/degrade.md`
- [[vault/refs/vault/_common/handoffs|Handoffs]] — `vault/refs/vault/_common/handoffs.md`
- Boundaries — `vault/refs/vault/_common/out-of-scope.md`
- Then the checklist — `vault/refs/vault/_common/checklist.md`

## Out of scope

- A player-facing homebrew species/race *mechanic* balance review —
  `rule-prep`'s species subtype
  (`.claude/skills/rule-prep/references/species-design.md`).
- Any other vendored SRD reference type (spells, feats, backgrounds,
  monsters) — `find-guidelines`.

## Owned paths

`vault/srd/species/` (`status: srd`, `publish: false`)
and `vault/campaigns/shattered-sea/species/homebrew/` (`status:` starts
`draft`/`canon` per whether it's already played, `publish: false`).
