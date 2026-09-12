# Source ingest queue: ss4-ship-surety-manual

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/vehicles/hcs-surety-owners-manual.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md § Round 4 — `ship-child-manual ::
entities/vehicles/hcs-surety-owners-manual.md → world/ships/hcs-surety-owners-manual.md — AFTER
parent`)

Gate proof:

- docs/campaign/MIGRATION-LEDGER.md:84 `REVIEWED-BY-HUMAN: 2026-07-13 — user instructions: "at
  least 5 rounds of iterative improvements"... Blessing covers exactly the 11 lines below.`
  (Round 4 header, line 82)
- docs/campaign/MIGRATION-LEDGER.md:95 `- [ ] ship-child-manual :: entities/vehicles/hcs-surety-
  owners-manual.md → world/ships/hcs-surety-owners-manual.md — AFTER parent`

Parent status: world/ships/hcs-surety.md exists, `status: canon` (confirmed before starting).
Family plan (source of the child-page disposition below): archive/2026-07/
ss4-ship-surety-parent.md § FAMILY PLAN table — "Child page — player-facing rules reference
(`audience: players`, `publish: true` in source), crew roles/upkeep/travel/combat/guns/bastion
facilities. Distinct audience and distinct function from the DM guide."

Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/vehicles/hcs-surety-owners-manual.md — triage: entity-source (ship-rules child
      page), ready, written

## Claims — entities/vehicles/hcs-surety-owners-manual.md

- [x] ship-child :: HCS Surety — Owner's Manual :: world/ships/hcs-surety-owners-manual.md (new) —
      player-facing standing orders for the *Uncertainty* (ex-HCS Surety): particulars, Ram Bow/
      Shallow Draft refit mods, deck arrangement, crew roles, upkeep, navigation, ship-to-ship
      combat, bastion facilities, port standing. Back-links parent `[[hcs-surety]]`. (%%src: legacy%%)

## Flags

- relink: delmar-fisk — commanding officer/captain, named throughout (masthead, Crew). No
  `delmar-fisk` page yet; matches existing precedent already used on `world/rules/swashbuckler.md`,
  `world/lore/human.md`, `world/items/delmars-cloak-of-the-manta-ray.md`,
  `world/items/pearl-of-souls.md`, `pcs/perrin-black-jaw.md` — same slug, same flag text. Plain
  text throughout.
- relink: crissdalynn-khinriss — source names her "Crissdalynn" (no surname, no brackets) as
  partial Navigator coverage in Article IV's "Current gaps" line. No dedicated page yet;
  `pcs/perrin-black-jaw.md:83` already establishes the full-name slug
  (`relink: crissdalynn-khinriss — once her page lands`) — matched here for consistency rather
  than inventing a bare `crissdalynn` slug. Plain text.
- relink: oleandro-fuschi — source wikilinks `[[oleandro-fuschi|Oleandro]]` (Article IV, crew
  contact at Ponte Bassa). No page anywhere in `world/`/`pcs/`/`prep/` (first mention in this
  migration). Plain text.
- relink: ponte-bassa — named alongside Oleandro as his location ("at Ponte Bassa"), not itself
  bracketed in source. No page yet; `pcs/perrin-black-jaw.md:85,178` already established this
  exact slug/flag text — matched for consistency. Plain text.
- relink: the-drowned-maw — source wikilinks `[[the-drowned-maw|Drowned Maw]]` (Article VI,
  compass-failure zone). No dedicated page yet (multiple pages reference it in prose, e.g.
  `world/lore/campaign-overview.md`, `world/items/pearl-of-souls.md:33`, which already uses this
  exact slug/flag text — matched here). Plain text.
- relink: uncertainty — source wikilinks `[[uncertainty|Uncertainty]]` twice (Article I, footer
  reference line). Per the parent's own queue file FAMILY PLAN: `uncertainty.md` is a 6th,
  deliberately-excluded sibling-shaped source (divergent post-refit stats/captain) whose
  disposition is a future DM call, not this dispatch's. Matches the parent page's own identical
  `relink: uncertainty` flag. Plain text.
- real wikilink (not deferred) :: [[hcs-surety-manifest|Ship Manifest]] — `world/ships/hcs-surety-
  manifest.md` landed mid-dispatch (sibling `ship-child-manifest` line, staleness re-check caught
  it), confirmed `status: canon` before writing this page. Source's own footer reference line uses
  this target; retargeted per the actual filename.
- resolved (not a stub-page relink): hcs-surety-dm-guide — source wikilinks
  `[[hcs-surety-dm-guide|DM Guide]]` twice (Article IX's Crown-recognition pointer, footer
  reference line). Per the family plan, the DM guide folds INTO the parent's own `## DM Only`
  (companion pattern) rather than landing as a separate page — confirmed already executed: the
  parent `world/ships/hcs-surety.md` DM Only now carries Navigation Failures / Chase Complications
  / Crew Casualties content (observed mid-dispatch, sibling `ship-dm` ledger line in flight
  concurrently). Both source mentions were therefore rewritten as real `[[hcs-surety]]` links
  pointing to that page's DM Only section, not left as a `relink:` stub — the target already
  exists under a different filename than the source implies.
- real wikilink (not deferred) :: [[hcs-surety]] — required parent back-link per line-specific
  instruction. Added in the opening Player-Known paragraph and reused for the DM-guide-pointer
  resolution above.
- real wikilink (not deferred) :: [[hcs-surety-layout|Deck Layouts]] — `world/ships/hcs-surety-
  layout.md` landed mid-dispatch (sibling `ship-child-layout` line), confirmed `status: canon`
  before writing this page. Source's own Article III pointer and footer reference line both use
  this target.
- real wikilink (not deferred) :: [[calveno-la-vasca|La Vasca]] — `world/locations/calveno-la-
  vasca.md` already landed (district child page, Round 4 `district` ledger line), `status: canon`.
  Source's own `[[la-vasca|La Vasca]]` link retargeted to the real filename (city-builder
  parent/child convention: `calveno-la-vasca.md`, not a bare `la-vasca.md`).
- Title normalization (not a contradiction): source's own H1 is "Uncertainty — Owner's Manual".
  Landed page title is "HCS Surety — Owner's Manual" to match the sibling convention already
  established by `hcs-surety-layout.md` ("HCS Surety — Deck Layouts") — all family children share
  the parent's registry-title prefix, consistent with the parent page's own naming resolution
  (source title kept, rename tracked via aliases). Source's actual title is preserved verbatim in
  the page's opening prose (the in-fiction masthead quotes "Private Vessel UNCERTAINTY").
- Section mapping (source Articles → skeleton headings), since this source has no natural
  Player-Known/DM-Only split of its own (it's 100% player-facing, per `audience: players`/
  `publish: true`):
  - Player-Known: masthead + Article I overview prose, Article III (Deck Arrangement), Article V
    (Maintenance), Article VI (Passage & Navigation), Article VIII (Facilities & Weekly
    Management), Article IX (Vessel Standing & Port Records).
  - Stats & Combat: Article I stat table + Hull Integrity/AC/Repairs mechanics, Article II (Ram
    Bow, Shallow Draft), Article VII (Action Against Hostile Vessels — range bands, ramming,
    ordnance, gunner's actions, shot types).
  - Crew: Article IV (Ship's Company — roles, rates, requirements, current gaps).
  - DM Only: one short pointer to the parent's DM Only (Crown recognition timeline) — no secret
    content of its own since the whole source is player-facing; kept non-empty per the skeleton's
    required-heading rule rather than leaving it blank.
- tag mapping: source `tags: [player-resource]` — not a Domain-taxonomy tag (WIKI.md § Tag
  taxonomy is tone/genre, not audience-role), and not an identity/origin tag either. No taxonomy
  equivalent exists for "this is a handout" — dropped, matching the parent's `tags: []` precedent.
  Landed `tags: []`.
- frontmatter drops, matching parent/`hcs-surety-layout.md` precedent: `campaign`, `subtype`
  (`ship-rules` — not a governed key for `type: ship`, unlike `location`/`rule`), `audience`,
  `publish` (source `true` — migration-mode `publish:` stays false/absent always, per DISPATCH.md),
  `confidence_level`, `sources`. `summary` folded into Player-Known opening prose instead of
  dropped silently.
- Status determination: rung 2 of the migration-mode status ladder (source-repo session evidence,
  since campaign-os's own `sessions/` only holds 01–02 and this content is post-Session-03 refit
  era) — same ladder as parent and `hcs-surety-layout.md`. Evidence, from the SOURCE repo's own
  session material (shattered-sea wiki, not this repo):
  `wiki/sessions/session-03.md:26` ("HCS Surety is now the *Uncertainty*... Docked at La Vasca,
  Black-Jaw dry dock, Calveno. 5-day repair estimate.") and `:31` ("Delmar's coat locked in
  captain's chest") — establishing the private identity, the La Vasca refit, and Delmar's
  captaincy in actual play, all of which this manual documents as settled fact. Corroborating
  (not deciding) signal: source frontmatter's own `audience: players`/`publish: true` is genuinely
  per-file, not a pile default — the other 3 unlanded siblings in this same family all carry
  `audience: dm`/`publish: false` (checked all 5 source files' frontmatter directly). Landed
  `status: canon`.
- No CONTRADICTION found. Hull Points read 130 here (post-refit) vs. the parent's 120 (at
  capture) — not a conflict, same non-conflict reasoning the parent's own queue file already
  applied to `uncertainty.md`'s divergent stats and `hcs-surety-layout.md`'s queue file repeated
  for its own Crew Casualties HP thresholds: different points in the same ship's timeline, neither
  page claims to describe the other's moment.
- Friction (not actioned, not this dispatch's page to fix): `hcs-surety-layout.md`'s own queue
  file already flagged that the parent page carries inline `%%src: legacy%%` marks after nearly
  every paragraph despite `created: legacy` (banned as noise per Hard Rule 2/DISPATCH.md). This
  page follows the written rule (single page-level citation, no inline marks) rather than the
  parent's apparent pattern. Repeating the flag here since it's the third landed page to notice
  the same drift — routing to canon-review, not fixing the parent (not this line's to edit).
