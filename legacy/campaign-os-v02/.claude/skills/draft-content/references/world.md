
# Draft — World

The outermost container: every campaign, season, session and one-shot sits inside one. Done means a DM can site a brand-new campaign anywhere on this page and know what is already true there.

## Template

`vault/_templates/_world.md` — copy it, never retype it.

Headings are fixed and in this order:

`## Map` (OPTIONAL — delete outright with no map) · `## Overview` · `## Geography` · `## Peoples & Powers` · `## Faith & Pantheon` · `## Cosmology & Planes` · `## History & Calendar` · `## Campaigns in This World` · `## GM Notes`.

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — PC agency, NPC independence.
3. `vault/refs/vault/_common/hard-rules.md` — shared rules; bind this type, never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now, paste the output.

`DW1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **A World Holds, It Does Not Detail.** A region, faction, deity or event with real content of its own gets its own page and a wikilink from here -> a world page that restates a child page's facts is a rule-8 duplication, not thoroughness. Every section on this page is an index with prose, not a gazetteer. "Holds" means the world-level setting dials: technology level, law level, government type, economy, demographics, and climate or weather — borrowed from industry standards like GURPS's Tech Level scale and Traveller's Universal World Profile, world-knobs that remain true across every campaign and location seated here.
- **The Inheritance Boundary Is Stated, Never Implied.** `subtype: published` or `hybrid` -> `## GM Notes` names which material comes from the published setting and which is this table's own. A later session must never have to guess which facts it is safe to overwrite.
- **Published Material Is Summarized, Never Vendored.** A published setting is described in original prose with `author: hb`; copying its text in is a licensing problem, not a shortcut. `author: srd` is only for material the SRD actually licenses.
- **Homebrew Borders Canon, Never Overwrites It.** An original region added to a published world is sited on water or land confirmed genuinely unmapped in the source -> moving, renaming or contradicting a published place makes every third-party reference at the table wrong. `## GM Notes` names the real neighbour it borders — what makes the addition read as inherited, not bolted on.
- **`current_date` Is The World's Clock.** Written so it sorts (`1495 DR`), and it is the world's now — a campaign's own chronology lives on its timeline page, never restated here.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- Invented whole, a published setting, or a published setting with additions? Sets `subtype`.
- `subtype: hybrid` -> what is inherited and what is ours, named explicitly before any prose is written.
- What year is it, in what calendar? Sets `current_date`.
- Which campaigns run here, and where in the world does each one sit?
- What is true everywhere in this world that a player must walk in knowing? Fills `### Tenets` — three to five, no more.

## Before you ship

[[vault/refs/vault/_common/lifecycle|Lifecycle]] `vault/refs/vault/_common/lifecycle.md` · gaps `vault/refs/vault/_common/degrade.md` · handoffs `vault/refs/vault/_common/handoffs.md` · boundaries `vault/refs/vault/_common/out-of-scope.md` · then `vault/refs/vault/_common/checklist.md` and `vault/refs/vault/world/references/checklist.md`.

## Reference files

| File | Read when |
|---|---|
| `vault/refs/vault/world/references/checklist.md` | World-only checklist additions |
| `vault/refs/vault/location/references/region.md` | Splitting a region out to its own page |
| `vault/refs/ideas/villains-and-themes.md` | Writing world-level powers with interiority |
