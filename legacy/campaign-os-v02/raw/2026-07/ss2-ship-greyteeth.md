# Source ingest queue: ss2-ship-greyteeth

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/vehicles/greyteeth-runner.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — Round 2, `ship ::
entities/vehicles/greyteeth-runner.md → restructure → world/ships/ — Connections
heading + tag policy test`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:41 "REVIEWED-BY-HUMAN:
2026-07-13 — user instruction 'implement all your recommended fixes, then proceed to
round two'. Blessing covers exactly the 13 lines below."
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/vehicles/greyteeth-runner.md — triage: entity-source (ship), ready

## Claims — entities/vehicles/greyteeth-runner.md

- [x] ship :: Greyteeth Runner :: world/ships/greyteeth-runner.md (new) — full ship
  identity: reef runner (sloop), Tier 1, Island Council-built, for-sale-in-Port-Tidefall
  read-aloud/overview/layout/facilities/operational notes, stat block, no standing
  crew, four Connections mentions (Port Tidefall, Midchain, Tessarine Concordat,
  Dravosi Crown) (%%src: legacy%%) — WRITTEN, lint clean.

## Frontmatter decisions

- `ship_class: reef runner (sloop)` — copied verbatim from source frontmatter
  `ship_class` key, free text per rails.
- `tier: 1` — bare int, NOT quoted. Vethka lesson re-applied deliberately:
  the ship-tier enum check compares the raw frontmatter-line string after `:`
  split; `tier: "1"` would store the literal string `"1"` (quotes included)
  which is not in `{"1","2","3","4"}` and fails: `tier: 1` stores `1` and
  passes. Verified by checking that enum-comparison behavior directly before
  writing — not re-guessed from the vethka file alone.
- `home_port: "Port Tidefall"` — plain text, NOT a wikilink. Stub check
  (`find world -iname "*port-tidefall*"`) returns nothing; `world/locations/`
  has no Port Tidefall page yet, so per rails item 3 ("home_port: wikilink only
  if that location page exists") this stays plain text. Source's own
  `home_port: "[[port-tidefall|Port Tidefall]]"` link is deliberately not carried
  over as a live wikilink — would 404 under W3.
- `status: pending` (not `canon`) — see Appearances section on the page for the
  full reveal-signal writeup; short version: zero hits for "greyteeth" in
  `~/ai-os/shattered-sea/wiki/sessions/`, no `## Session Events` heading in the
  source at all (unlike estratto's explicit "Not yet encountered" marker), source
  frontmatter itself is `audience: dm` / `publish: false` — no reveal signal of
  any kind, so this does NOT clear the vethka bar (source session logs sighting
  the vessel). Landed pending, same disposition class as estratto/gentle-hag.
- `aliases: []` — source states only the one name, matching the filename; no
  alternate name text anywhere in the source page.
- `created: legacy` / `touched: legacy` — sanctioned migrated-page convention,
  MIGRATION-LEDGER.md Flags item 2.

## Tag decisions (live test of WIKI.md § Tag taxonomy final bullet)

Source tags: `[maritime, tessarine]`.

- `tessarine` → **DROPPED.** Entity-identity/faction-name tag (Tessarine
  Concordat) — this is the taxonomy's own named example
  ("faction names like dravosi/tessarine" DROP). The relationship it encodes
  (vessel operates in/near Tessarine waters, has no Tessarine registry) is
  carried in prose under `## Connections` instead — one fact, one place.
- `maritime` → **DROPPED, not mapped.** `world/_meta/tags.md`'s canonical
  Domain list (`intrigue, heist, horror, mystery, exploration, war, politics,
  romance`) is narrative *tone*, not literal setting/domain vocabulary.
  "Maritime" names a setting (this is a boat), not a tone — there is no
  genuine tone-equivalent to map it to, and WIKI.md is explicit: "Don't
  force-fit." Forcing it onto e.g. `exploration` just because both involve
  water would be exactly the force-fit the rule forbids.
- New tag added from content-tone reading (same method the vethka precedent
  used — vethka's `[war, heist]` weren't a mapping of its source tag `[grung]`
  either, they were read off the page's actual content): **`exploration`**.
  Signal: the entire page is about fast, shallow-drafted movement through
  reef channels other hulls can't follow ("built for speed, shallow water,
  and reef channels where heavier patrol cutters cannot follow"; "Fastest
  documented Tier 1 hull... no speed penalty in charted reef passages").
  Considered `intrigue` (the no-registry-pennant / no-Crown-or-Concordat-
  registry detail reads as operating outside official notice) and rejected
  it — that detail sits under Operational Notes as an acquisition/legal
  caveat about the sale, not a depicted intrigue plot; picking it would be
  reading a theme into a legal footnote rather than the page's actual
  content center of gravity, which is unmistakably reef-channel travel.
- Final: `tags: [exploration]`.

## Connections (new optional heading — this round's fix, first live use)

Source's own `## Connections` section lists 4 entities: Port Tidefall,
Midchain, Tessarine Concordat, Dravosi Crown. None of the 4 have real pages in
`world/` (stub check: `find world -iname "*port-tidefall*" -o -iname "*midchain*"
-o -iname "*tessarine-concordat*" -o -iname "*dravosi-crown*"` → empty).
Written as plain text under `## Connections` per migration-mode link deferral,
each with a `relink:` flag below. Kept `## Appearances` purely for
session-appearance evidence (empty — see Appearances writeup on the page) —
the heading split held cleanly for a page with zero session evidence and four
non-crew relationship mentions, which is exactly the case it was designed for.

## Flags

- `relink: port-tidefall — once its location page lands` (home port / current
  sale location)
- `relink: midchain — once its location page lands` (operating region)
- `relink: tessarine-concordat — once its faction page lands` (no registry
  held, but named as a relevant political entity)
- `relink: dravosi-crown — once its faction page lands` (no registry held,
  but named as a relevant political entity)
- relinked ✓ — carpenters-shop — not an original `relink:` flag on this page
  (the `### Facilities` bastion-mapping table was written before
  `world/rules/carpenters-shop.md` existed, plain text with no flag logged);
  `world/rules/carpenters-shop.md` landed (Round 3) and R4's dispatch named
  this table cell explicitly. "Carpenter's Shop" now links
  `[[carpenters-shop|Carpenter's Shop]]` (link-restoration pass R4,
  2026-07-14). "Weapons Locker" in the same table stays plain text — no
  `world/rules/weapons-locker.md` page exists.
