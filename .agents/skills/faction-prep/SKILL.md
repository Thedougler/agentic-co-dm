---
name: faction-prep
description: >
  Create or expand a runnable faction note in an ai-co-dm campaign. Triggers: "create a page
  for [faction]", "detail [faction]", "who runs [organization]". Checks index.md for existing
  stubs before creating, and decides whether the faction warrants a clock in hot.md. Full trigger
  list in the skill body.
---


# Faction prep

## Work gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Reject leaves no page. Invention is required when the wiki lacks the fact: set `invention: true` and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]` for wiki claims. Show the DM any contradiction with an existing page. Never present invention as a wiki fact. Never write silent canon. A craft `type` becomes `canon` only after DM accept.

Players see nothing until the DM accepts and presents.

Done when: the page is inspectable Work, `lifecycle: proposed`, invention flagged, grounding named.

File durable output under `wiki/` (entities/journal as appropriate); templates live in `wiki/templates/`. Replace knowledge-bank language with wiki language, and point at `docs/agents/work.md` rather than restating its glossary. Keep craft procedure.

## When to use

Use for a faction's current agenda, active relationships, independent movement,
clock, or DM-ready toolbox. Use `npc-design` for a face, `narrative-islands` for
competing forces in one situation, and `world-tick` for reviewed advancement.

## GM-prep gates

Prepare the faction as a living system, not a plot device. Distinguish active
NPCs/factions from past or inactive ones; record who wants what, what changes if
ignored, and the next visible move. Maintain a compact faction relationship
matrix when several factions matter. Keep only the facts the DM will not
improvise, use modular offers/tells, and make the page findable in under 30
seconds. Link the nearest atomic MOC/index; Organizer owns MOC structure.

## Faction Page Structure

**Frontmatter:** universal/entity fields auto-fill. Author the domain values: `status` (`active | dormant | dissolved`) and a `summary` of 2 sentences (what they want + how they operate).

**Required body sections:**

- **Agenda** — what they are pursuing right now, not just their long-term goal. A
  vector, not a state.
- **Membership** — who belongs, how they're organized, hierarchy shape
- **Methods** — how they operate (coercion, trade, information, violence, politics)
- **Public Face** — what common knowledge says about them (the cover story)
- **Clock** — if active: name, segments (4 or 6), trigger condition, consequence at fill

**Clock decision rule:** If the faction has an agenda that advances independently of the
party, it gets a clock in `hot.md`. Add it there after writing the page.

---

## Filing

- Page path: `wiki/<slug>/factions/<Name>.md`
- Add to `wiki/<slug>/factions/00 Factions.md` under `## entities/factions`
- If faction gets a clock: add entry to `wiki/<slug>/hot.md` faction clocks block
- Add reciprocal links to all referenced entities

Load `obsidian-markdown` before writing any prose. **DM-facing reference** throughout — all
faction content is DM-only operational reference.


## Sibling boundaries

Use `npc-design` for faction faces, `narrative-islands` for competing forces, and `world-tick` for reviewed off-screen advancement. Do not roll or canonize a future move during faction prep. Run `./scripts/after-write` after vault writes.

## Momentum and politics gate

Every active faction needs an independent next move, including what happens if
the party goes quiet. Let strongholds, routes, resources, and relationships
produce politics: control should alter offers, access, reputation, and pressure,
not merely change a map label. Make the consequence of inaction visible and
interruptible; never turn a faction clock into a hidden punishment.
