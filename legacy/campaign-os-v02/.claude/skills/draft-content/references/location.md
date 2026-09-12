
# Draft — Location

A place the party can revisit. Done means the DM can run it from the read-aloud opening and the DM-only material alone.

## Template

Location is three genres, not six subtypes — pick the template
by what kind of place this is, not by copying the nearest existing page:

| Genre | `subtype:` | Template | Why this shape |
|---|---|---|---|
| Site | `building \| plane` | `vault/_templates/_campaigns/_location/_location.md` | A single site with no shop inventory and no room-by-room pipeline: a temple, a warehouse, a planar waypoint, a one-off building the party visits once. Modeled on the Forgotten Realms Wiki's building-article shape (e.g. the Yawning Portal), thinner than the shop template. |
| Site | `shop` | `vault/_templates/_campaigns/_location/_location_shop.md` | A single page, no deeper pipeline. Modeled on the Yawning Portal: where it is, how it's laid out inside, what it feels like, what you can actually get here — plus the `## On Display` shortlist the DM offers this party (`vault/refs/vault/location/references/shop.md`). |
| Governed-area | `settlement` | `vault/_templates/_campaigns/_location/_location_settlement.md` | A governed area the party can walk and a local power actually runs, from a hamlet to a capital. Modeled on Waterdeep: identity/infobox first, then how it's ruled, how it trades, how it lives, how it's defended, who's in it — every section OPTIONAL except what a real [[vault/refs/vault/location/references/settlement\|settlement]] can never lack. A **district** is this same template and this same `subtype: settlement`, nested `within:` its parent settlement instead of a region — it never gets a template of its own. |
| Governed-area | `region` | `vault/_templates/_campaigns/_location/_location_region.md` | A territory the party crosses rather than a place they stand in: an island chain, a strait, a sea band, a stretch of wilds. Modeled on the Sword Coast — near-identical shape to settlement, just a larger scale. An **island** is this same template and this same `subtype: region`, nested `within:` a larger region or the sea itself — it never gets a template of its own. |
| [[vault/refs/vault/location/references/dungeon\|Dungeon]] | `dungeon` | `vault/_templates/_campaigns/_location/_location_dungeon.md` | A site with rooms, levels, and a way in that isn't the governed-area shape. Modeled on Undermountain: what it's built of, how you get in and out, what its levels are, what happened here — genuinely unlike the other two genres, built via the four-phase pipeline below. |

Copy, never retype. Headings fixed, in the template's own order; every
`OPTIONAL` heading states its own keep/delete condition directly under
it — delete it outright when the condition doesn't hold, never leave it
empty.

`dungeon` forks before the sections below apply:
`vault/refs/vault/location/references/dungeon.md`. Settlement- and
region-specific judgment calls (when a district or sub-region earns its
own page; Government/Trade/Culture/Defenses) live in
`vault/refs/vault/location/references/settlement.md` and
`vault/refs/vault/location/references/region.md`.

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md`
2. `.claude/skills/composing-beats/references/audits.md`
3. `vault/refs/vault/_common/hard-rules.md` — bind this type, never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check, paste the output.

`DL1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **Within And Compass Are Required.** Fill `subtype:` (never the
  template's placeholder) and `within:` — quoted wikilink, no alias,
  terminating at `"[[campaigns/shattered-sea/locations/shattered-sea]]"`
  when no containing page exists yet
  (`vault/refs/vault/location/references/placement.md`).
  Fill all four `north_of`/`east_of`/`south_of`/`west_of` keys too, each
  a quoted wikilink, never empty, never "open water"/"none"
  (`vault/refs/vault/location/references/placement.md`).
- **No Space Without A Past.** No space goes undescribed -> a trace of
  original function, texture, or an interactable element, always.
- **Notable NPCs Resolve Or Spawn.** Named NPC -> wikilink or a spawned
  pending stub, never plain text (`vault/refs/vault/location/references/npcs.md`).
- **Dungeon Phase Gate.** One phase at a time, DM confirmation between
  each (`vault/refs/vault/location/references/dungeon.md`).
- **A Shop Shows Its Wares.** A `subtype: shop` page always carries
  `## On Display`, both halves: a continuing-mode `[!read-aloud]` box
  that shows the goods without naming any of them, then 6-10 bullets of
  `[[item]] - price - one clause`, picked with the read-layer commands
  against the party's current level and Weakness Map, a quarter of them
  a tier out of reach to save toward, and no item another shop in the
  same town already has on display. Never picked from memory, never a
  generic stock list, and never the same shortlist for two different
  parties (`vault/refs/vault/location/references/shop.md`).
- **Bastions and Strongholds.** A bastion, stronghold, or player-owned business is a location, with its ownership recorded in frontmatter.
- **Laws and Legal Codes.** Laws and legal codes sit with the settlement that enforces them (its government section); the history of a law is `lore`.
- **Setting Dials At Region Scale.** A `subtype: region` page records the
  dials that vary between regions of one world — law level, government
  type, economy, demographics, climate — where they differ from what
  `.claude/skills/draft-content/references/world.md` already sets world-wide. Identical to
  the world's, and it stays on the world page only.

## Interview — this type only

Ask `vault/refs/vault/_common/interview.md`'s questions, plus: subtype
(`building` / `plane` / `shop` / `dungeon` / `settlement` / `region`);
`within:` target; cultural root; terrain (`geography:`, at least one
tag); all four compass neighbours
(`vault/refs/vault/location/references/placement.md`).

A district is `settlement` nested `within:` its parent settlement. An
island is `region` nested `within:` a larger region or the sea. Neither
is a subtype of its own. Dungeon adds or overrides these questions —
`vault/refs/vault/location/references/dungeon.md`.

## Toy Chest

Four fields — `verb`, `unstable_condition`, `consequence`, `link_of_relevance` — a table in the DM-only material, no frontmatter duplication. Fields: `vault/refs/vault/location/references/toy.md`. Layout: `vault/refs/vault/location/references/output.md`.

## Before you ship

[[vault/refs/vault/_common/lifecycle|Lifecycle]] `vault/refs/vault/_common/lifecycle.md` · gaps `vault/refs/vault/_common/degrade.md` · handoffs `vault/refs/vault/_common/handoffs.md` · boundaries `vault/refs/vault/_common/out-of-scope.md` · then `vault/refs/vault/_common/checklist.md` and `vault/refs/vault/location/references/checklist.md`.

## Reference files

All paths `vault/refs/vault/location/references/`.

| File | Read when |
|---|---|
| `vault/refs/vault/location/references/placement.md` | Filling `within:` and the compass keys, folder placement |
| `vault/refs/vault/location/references/dungeon.md` | `subtype: dungeon` |
| `vault/refs/vault/location/references/shop.md` | `subtype: shop` — Shopkeeper, On Display, Inventory |
| `vault/refs/vault/location/references/dungeon-example.md` | Dungeon worked example + checklist addendum |
| `vault/refs/vault/location/references/settlement.md` | `subtype: settlement`, including a district |
| `vault/refs/vault/location/references/settlement-example.md` | Settlement worked example + checklist addendum |
| `vault/refs/vault/location/references/region.md` | `subtype: region`, including an island, and any travelled-through region |
| `vault/refs/vault/location/references/toy.md` | Writing or checking the Toy Chest |
| `vault/refs/vault/location/references/output.md` | Mapping content onto the template |
| `vault/refs/vault/location/references/npcs.md` | Resolving or stubbing a named NPC |
| `vault/refs/vault/location/references/checklist.md` | Before calling any page done |
| `vault/refs/vault/location/references/example.md` | A worked page, interview to finished |
| `vault/refs/vault/location/references/city-improv.md` | Settlement gets unscripted table time |
| `vault/refs/vault/location/references/tips.md` | General location-prep tips and pitfalls |
| `vault/refs/vault/location/references/monsters-by-adventure-location.md` | Picking monsters appropriate to a location's terrain/setting |
| `vault/refs/vault/location/references/wilderness-travel-and-exploration.md` | Travel pacing and exploration mechanics for a region page |
