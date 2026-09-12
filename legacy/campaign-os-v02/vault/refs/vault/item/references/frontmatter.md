---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The rarity, attunement, form, found_at, and value frontmatter keys and their allowed values, no provenance field."
created: "2026-08-03"
updated: "2026-08-08"
tags: [craft]
uid: 08e825fb-aebf-4897-bb1a-17b4d231def3
---

# Frontmatter: rarity, attunement, form, found_at, and value

`vault/_templates/_srd/_item.md` declares `rarity`, `attunement`, `form`,
`found_at`, and `value` as `item`-specific frontmatter keys — the
template's own enum comments are the allowed-values authority; this file
states only what those comments don't: sequencing, cross-references, and
edge cases.

Set `rarity`/`attunement` in frontmatter, not as body-table rows — set
the real values during the Rarity Comes First and Attunement Decision
Tree rules, before the DM Review Gate; the template pre-fills
`rarity: common` / `attunement: false` as placeholders only. Every
mechanic is still `[HB]`/`[RAW]`-labeled at the power level regardless of
whether the item itself is SRD, third-party, or homebrew.

`form` — set once the item's category is settled; feeds cross-type
filtering (e.g. a dashboard grouped by `form`).

`found_at` (mandatory) is the shop(s) or place(s) where players can
find/obtain this item in play — the item's current holder once already
acquired. Plain wikilinks, not prose with an embedded link; the
`current_holder` Item Toy row remains the place for the *prose*
explanation of how/why they hold it. Fill `found_at:` with the same
page(s) `current_holder` already names, when they resolve to pages —
don't invent a second answer.

`value` (mandatory) is this item's worth in gold as a plain gp string
(e.g. `"50 gp"`), regardless of whether it's actively for sale — not
conditional on a named vendor the way a shop asking price is.
