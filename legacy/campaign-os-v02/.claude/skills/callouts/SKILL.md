---
name: callouts
description: >-
  The callout standard for a Campaign OS repo (vault/ present) — which `> [!type]` to write
  and its prose contract. Use the moment you're about to type `> [!` on any wiki page, choose a
  callout type, convert an UPPERCASE/generic callout, or style vault/.obsidian/snippets/custom-callouts.css.
  Not Quartz/site CSS. Spoken pictures and spoken lines live in siblings
  wrapped in `[!narration]` / `[!dialogue]`.
---

# callouts

The single source of truth for every callout in this vault: which types exist, what each is
for, and how its prose is written. Blockquote syntax (titles, folding, spacing) is
`obsidian-markdown`'s job. Spoken pictures and spoken lines are `type: narration` /
`type: dialogue` siblings; wrap their bodies in `[!narration]` / `[!dialogue]`
(references below). This skill owns remaining callout containers.

A callout is important by definition — it interrupts the page to grab the DM's eye at the
table. A callout that doesn't earn that interruption belongs in plain prose.

## Choose the type — content first, never color

| The content is... | Type | Contract |
|---|---|---|
| A picture the DM speaks | `narration` | On a `type: narration` sibling only. [references/narration.md](references/narration.md). Extract leftover `[!read-aloud]` from parents into that sibling. |
| A spoken line | `dialogue` | On a `type: dialogue` sibling only. [references/dialogue.md](references/dialogue.md) |
| A rule the DM applies — hazard, trap, trigger, condition | `mechanic` | [references/mechanic.md](references/mechanic.md) |
| Rolls the party can try on this picture | `check` | [references/check.md](references/check.md) — table in the callout |
| Canon the party hasn't reached yet (never a played session or PC backstory) | `spoiler` | [references/spoiler.md](references/spoiler.md) |
| [[vault/refs/vault/quest/references/content\|Content]] on a docs/meta page (`docs/`, `vault/refs/`, vendored SRD/craft reference) | generic set | [references/generic-types.md](references/generic-types.md) |
| An image placeholder awaiting a render | `visual-aid` | owned by the `visual-aids` skill |
| A canon conflict flag or its resolution | `warning` CONTRADICTION / `success` RESOLVED | format: `transcript-ingest`; lifecycle: `canon-review` |

Read the matched reference file before writing the callout — it carries the full prose
contract, one worked example, the conversion table for the misuses found in this vault, and
the type's CSS block.

## Hard rules

- Type is lowercase, always: `> [!mechanic]`, never `> [!MECHANIC]` or `> [!CAUTION]` (lint
  W22 auto-downcases on save).
- Play pages (`vault/`, `vault/campaigns/shattered-sea/pcs/`, `vault/campaigns/`) carry play types only — `mechanic`,
  `check`, `spoiler`, `narration`, `dialogue` — plus `visual-aid` and the two canon-review workflow callouts.
  Leftover `[!read-aloud]` / `[!dialogue]` on a mechanical parent extract to a sibling.
  Generic types (`note`, `tip`, `caution`, `important`, ...) live on docs/meta pages only
  (lint W23 warns on either crossing).
- `> [!dm]` is retired without replacement — Vale flags it (`CampaignOS.RetiredCallout`).
  Touching a page that carries one: reclassify its content by the row it actually matches
  above (`mechanic`, `check`) or extract spoken lines to a `type: dialogue`
  sibling. Background with no at-table action folds into plain prose. Never re-add `[!dm]`.
- `> [!quote]` on a play page extracts to a `type: dialogue` sibling. The generic
  `[!quote]` on a docs/meta page is unaffected.
- One job per callout: one secret, one mechanic, one pictured place's
  rolls. A second picture is a second `[!check]`.
- Never put a `##` heading inside a callout body. (Nesting a callout inside a callout is W104's matcher — `npm run lint -- --rules`.)
- A vault example is not a license. Existing pages still carry pre-standard callouts —
  `[!CAUTION]` secrets, prose-bullet hazards. Match this skill's references, never the page
  you happen to have open (copied misuse is how the drift spread).
- Touching a page that has a pre-standard callout in the region you're editing → convert it
  per the reference file's conversion table in the same edit.

## CSS

Each play type's Obsidian snippet block lives at the bottom of its reference file;
`vault/.obsidian/snippets/custom-callouts.css` is the assembled artifact — every block concatenated,
nothing else. Change a color/icon in the reference file, then rewrite the snippet file to
match. The generic set uses Obsidian's theme built-ins and has no block.
