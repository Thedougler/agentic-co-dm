# Source ingest queue: ss-lore-campaign-overview

Source root: /Users/nick/ai-os/shattered-sea/wiki/lore/campaign-overview.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — `lore :: lore/campaign-overview.md → restructure → world/lore/ — status: canon`)
Gate: REVIEWED-BY-HUMAN: 2026-07-13 (docs/campaign/MIGRATION-LEDGER.md line 11), ledger line at line 32.
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] lore/campaign-overview.md — triage: lore (player-facing setting overview), ready

## Claims — lore/campaign-overview.md

- [x] lore :: The Shattered Sea — Campaign Overview :: world/lore/campaign-overview.md (new) — full restructure of the source's prose under Player-Known/DM Only/Sources skeleton, no content invented beyond source (%%src: legacy%%)

## Status decision

`status: canon` (not `pending`). Signal: source frontmatter reads `audience: players`,
`publish: true` — this file was actually live on the legacy campaign's player-facing
wiki, i.e. already delivered to players as a session-zero primer, not unrevealed DM
prep. That satisfies the contract's canon bar ("revealed at the table or ruled by the
DM") even though the mechanism was a handout rather than in-scene narration.

## Player-Known / DM Only split

Read the full source end to end. Found no DM-only truths folded into the prose — every
paragraph is written in second person or general setting-primer voice addressed to
players. The "Edges of the Map" section's mystery hooks ("things that do not fit the
economy yet") are themselves player-facing hook framing, not a withheld GM secret, so
they stayed in Player-Known. `## DM Only` was written honestly empty (with a one-line
citation explaining why) rather than force-splitting content that isn't DM-only.

## Tag mapping

Source tag `player-resource` has no canonical equivalent in `world/_meta/tags.md`
(canonical domain list: intrigue, heist, horror, mystery, exploration, war, politics,
romance — no "reference/meta" bucket exists). Substituted with `exploration` (the page
is majority geography/setting survey) and `politics` (the "Powers on the Water"
section is a faction-relations table) — nearest-canonical mapping per source-ingest §5.
Flagging for the DM/tag-taxonomy maintainer: `player-resource` may be worth adding as
an alias or a new reserved category if more legacy player-handout pages surface in
later waves — not decided here, since `world/_meta/tags.md` is outside this file's
owned paths.

## Flags

Link deferral — none of the 25 entities this source links to have a world/ page yet
(stub check run against world/ pcs/ prep/ before writing; only hit was `calveno` as a
plain-text mention inside `world/npcs/estratto.md`, not a page). Per source-ingest's
migration-mode link deferral, all wikilinks were written as plain text in
`world/lore/campaign-overview.md`; relink each once its page lands:

- relink: Shattered Sea — once its page lands
- relink: Galewall — once its page lands
- relink: Ashwall Islands — once its page lands
- relink: Dravosi Crown — once its page lands
- relink: Central Strait — once its page lands
- relink: Port Tidefall — once its page lands
- relinked ✓ — Calveno — `world/locations/calveno.md` landed; the three plain-text
  "Calveno" mentions (Crown Islands bullet, Powers table x2) now link `[[calveno|Calveno]]`
  (link-restoration pass, 2026-07-13)
- relink: Kalowe — once its page lands
- relink: The Verdant Teeth — once its page lands
- relink: Grung Clans — once its page lands (already migrating: covered by ledger line `faction :: entities/factions/sentinels-of-the-eyrie.md` is a different faction — Grung Clans itself has no ledger line in this stress-test batch). NOT relinked: the "Grung clans" (Verdant Teeth bullet) and "Grung Clans" (Powers table row) mentions still refer to the unmigrated faction, left plain text.
- relink: The High Eyrie — once its page lands
- relinked ✓ — Sentinels of the Eyrie — `world/factions/sentinels-of-the-eyrie.md` landed;
  both mentions (Tail-and-Maw prose, Powers table) plus the short-form "The Sentinels"
  (Edges of the Map prose) now link `[[sentinels-of-the-eyrie|...]]` (link-restoration
  pass, 2026-07-13)
- relink: The Drowned Maw — once its page lands
- relink: The Shelfworks — once its page lands
- relink: Tessarine Concordat — once its page lands
- relink: The Passage — once its page lands
- relink: Umberlee — once its page lands
- relinked ✓ — The Waveservants — `world/factions/waveservants.md` landed; the three
  "Waveservants" mentions (Powers table, Powers prose, Faith prose) now link
  `[[waveservants|Waveservants]]` (link-restoration pass R4, 2026-07-14)
- relink: Aarakocra — once its page lands
- relinked ✓ — Grung (species) — `world/lore/grung.md` landed; the "Peoples of the
  Scatter" mention ("Aarakocra, Grung, Rattkin, and Tabaxi") now links
  `[[grung|Grung]]` (link-restoration pass, 2026-07-13)
- relink: Rattkin — once its page lands
- relink: Tabaxi — once its page lands
- relink: Saltwright — once its page lands
- relink: Beaumont Sel — once its page lands
- relink: Outer Reach — once its page lands

Frontmatter divergence from source: source had `publish: true` (it was live on the
legacy player wiki) — written here as `publish: false` per this repo's default-deny
publish rule (contract item 4 / skill Owned-paths "Never" list); publishing this page
is a separate, explicit PUBLISH-phase decision, not this ingest's to make.

No contradictions found against existing canon (world/ had no prior lore pages —
`world/lore/` was empty but for `.gitkeep`).
