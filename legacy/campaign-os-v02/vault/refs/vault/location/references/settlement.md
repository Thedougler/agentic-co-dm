---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Settlement subtype specifics for the location guide — the OPTIONAL Government/Trade/Culture/Defenses sections, when a district earns its own page, output mapping, and checklist addendum."
created: "2026-08-03"
updated: "2026-08-07"
tags: [politics, exploration]
uid: dc892abf-9511-4f13-a9bf-9ce29c217ba0
---

# Draft — Location, Settlement Subtype

Read this when `.claude/skills/draft-content/references/location.md`'s interview
establishes `subtype: settlement` — including a district, which is this
same subtype nested `within:` its parent settlement rather than a region.
Assumes the shared interview and stub check from
`.claude/skills/draft-content/references/location.md` already ran — this file covers only
what's settlement-specific.

## Optional sections

`## Government`, `## Trade`, `## Culture`, `## Defenses` are each
OPTIONAL on `vault/_templates/_campaigns/_location/_location_settlement.md`
— keep only the ones a real
decision has actually been made for (who rules and how; why the economy
matters to the story; a defining custom, faith, or festival; a
fortification that's plot-relevant). Delete the rest outright rather than
filling them with generic filler (`vault/_templates/CLAUDE.md`'s OPTIONAL
convention: state the keep/delete condition, never leave the heading
empty). `## At a Glance` and `## Geography` are never omitted — every
settlement has a Ruled By and a Population, and every physical place
occupies space relative to its neighbours.

## Districts

A district earns its own page only when it needs one: at least one real,
sourced fact of its own (a distinct Notable NPC, draw, or optional-section
detail) that doesn't already belong on the settlement page. A locale with
nothing beyond color is a `### <Name>` sub-location subheading in the
settlement page's own body, never a bulleted name with no target and
never a spawned page that just restates the settlement (`## Districts` on
the template: "a district with no page of its own is a subheading
instead"). Where a district page is warranted, run the standard queries
for its name before instantiating it, same as any other new page
(`vault/refs/vault/_common/queries.md`).

## Output structure

Content flows exactly as `vault/refs/vault/location/references/output.md`
describes for any governed-area page: read-aloud opening, `## At a
Glance`, `## Geography` (compass keys live in frontmatter, not body
prose — `vault/refs/vault/location/references/placement.md`), whichever of
Government/Trade/Culture/Defenses apply, `## Districts` (only if at least
one district page exists), then `## Loot` / `## Notable NPCs`. A district
page follows the same structure at its own scale: its `## At a Glance`
Ruled By or Known For row can point back to the settlement for context.

## Checklist addendum (settlement subtype, in addition to `vault/refs/vault/location/references/checklist.md`'s)

- [ ] `within:` and all four compass keys set, quoted, resolving to real
      pages (`vault/refs/vault/location/references/placement.md`).
- [ ] Every `OPTIONAL` heading kept only where its stated condition
      holds; every deleted one leaves no placeholder text behind.
- [ ] Every district page carries at least one real fact of its own —
      none exists purely for scenery with nothing distinguishing it from
      the settlement page.
Read `vault/refs/vault/location/references/settlement-example.md` for a
full worked example.

## Creative-domain rider

Facts, canon, structure, and visibility are bound (Hard Rules above and
in `.claude/skills/draft-content/references/location.md`, all CLAUDE.md project rules).
**Prose style is free.**
