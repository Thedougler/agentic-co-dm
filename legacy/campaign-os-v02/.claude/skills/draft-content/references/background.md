
# Draft — Background

An SRD background ([[srd/backgrounds/acolyte|Acolyte]], [[srd/backgrounds/criminal|Criminal]],
[[srd/backgrounds/sage|Sage]], [[srd/backgrounds/soldier|Soldier]], ...) recreated
verbatim, or a setting-native background authored to the same shape. Its
real external standard is the 5e SRD document's own mechanical background
format, not a narrative wiki.

## Template

`vault/_templates/_srd/_background.md` — copy it, never retype it from
memory, and owns this page's layout: every field and its order. This
guide never adds, drops, or reorders a field. One shape for every
background, SRD or homebrew: the Ability Scores/Feat/Skill
Proficiencies/Tool Proficiency/Equipment stat-line block.

## Read first — before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `vault/refs/vault/_common/hard-rules.md` — the shared and
   mechanical-type rules bind this type, never restated below.
3. `vault/refs/vault/_common/queries.md` — run the stub check now:
   `ls vault/srd/backgrounds/ vault/srd/backgrounds/homebrew/ 2>/dev/null | grep -i "<background name>"`.
   A hit → expand that page in place, never duplicate.

`DB1: <three files read, stub-check output pasted>`.

## Hard rules — this type only

- **Verbatim For SRD.** A `vault/srd/backgrounds/` page -> Ability Scores,
  Feat, Skill Proficiencies, Tool Proficiency, and Equipment are
  transcribed from the source text, never paraphrased; no source, no page.
- **Wikilink Every Grant.** Every named feat, tool, and equipment item ->
  inline `[[slug|Display Name]]` at first mention.
- **Origin Stays Off This Page.** A background's in-fiction origin, an NPC
  connection, or campaign-specific framing -> its own page
  (`.claude/skills/draft-content/references/lore.md`, `.claude/skills/draft-content/references/npc.md`),
  linked inline — never a new heading here.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- SRD transcription (confirm the source text/citation) or homebrew
  original (confirm the campaign facts driving the package)?

## Before you ship

Lifecycle `vault/refs/vault/_common/lifecycle.md` · gaps
`vault/refs/vault/_common/degrade.md` · handoffs
`vault/refs/vault/_common/handoffs.md` · boundaries
`vault/refs/vault/_common/out-of-scope.md` · then
`vault/refs/vault/_common/checklist.md`.

## Out of scope

- A player-facing homebrew background *mechanic* balance review —
  `rule-prep`'s background subtype.
- Any other vendored SRD reference type (spells, feats, species,
  monsters) — `find-guidelines`.

## Owned paths

`vault/srd/backgrounds/` (`status: srd`,
`publish: false`) and a `homebrew` sibling beside it, created on first use
(`status:` starts `draft`/`canon` per whether it's
already played, `publish: false`).
