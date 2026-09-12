
# Draft — Feat

An SRD feat ([[srd/feats/alert|Alert]], [[srd/feats/grappler|Grappler]],
[[srd/feats/magic-initiate|Magic Initiate]], ...) recreated verbatim, or a
setting-native feat authored to the same shape. Its real external standard
is the 5e SRD document's own mechanical feat format, not a narrative wiki.

## Template

`vault/_templates/_srd/_feat.md` — copy it, never retype it from memory,
and owns this page's layout: every field and its order. This guide never
adds, drops, or reorders a field. One shape for every feat, SRD or
homebrew: the category/prerequisite line, then either a single
unlabeled benefit paragraph or one or more bolded benefit blocks, plus an
OPTIONAL `**Repeatable.**` line.

## Read first — before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `vault/refs/vault/_common/hard-rules.md` — the shared and
   mechanical-type rules bind this type, never restated below.
3. `vault/refs/vault/_common/queries.md` — run the stub check now:
   `ls vault/srd/feats/ | grep -i "<feat name>"`. A hit → expand that page
   in place, never duplicate.

`DF1: <three files read, stub-check output pasted>`.

## Hard rules — this type only

- **Verbatim For SRD.** A `vault/srd/feats/` page -> every benefit is
  transcribed from the source text, never paraphrased; no source, no page.
- **Wikilink Every Grant.** Every named condition, skill, spell, class, or
  other page a benefit grants or references -> inline
  `[[slug|Display Name]]` at first mention.
- **Category Line Is Not A Heading.** The category/prerequisite line
  (`*Origin Feat*`, `*General Feat (Prerequisite: ...)*`) stays the
  template's italic line directly under the H1 — never promoted to its
  own `##` heading.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- SRD transcription (confirm the source text/citation) or homebrew
  original (confirm the campaign facts driving the feat)?
- Single unlabeled benefit paragraph, or multiple bolded benefit blocks?
  Match the source's own shape — never split a one-effect feat into
  multiple blocks, never collapse a multi-effect feat into one paragraph.
- Does the source mark the feat repeatable? Only then does the template's
  `**Repeatable.**` line apply.

## Before you ship

Lifecycle `vault/refs/vault/_common/lifecycle.md` · gaps
`vault/refs/vault/_common/degrade.md` · handoffs
`vault/refs/vault/_common/handoffs.md` · boundaries
`vault/refs/vault/_common/out-of-scope.md` · then
`vault/refs/vault/_common/checklist.md`.

## Out of scope

- A player-facing homebrew feat *mechanic* balance review — `rule-prep`'s
  feat subtype.
- Any other vendored SRD reference type (spells, backgrounds, species,
  monsters) — `find-guidelines`.

## Owned paths

`vault/srd/feats/` (`status: srd`, `publish: false`)
and a `homebrew` sibling beside it, created on first use
(`status:` starts `draft`/`canon` per whether it's
already played, `publish: false`).
