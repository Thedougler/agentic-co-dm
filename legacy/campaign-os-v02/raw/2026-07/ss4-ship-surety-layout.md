# Source ingest queue: ss4-ship-surety-layout

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/vehicles/hcs-surety-layout.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md:93 — `ship-child-layout ::
entities/vehicles/hcs-surety-layout.md → world/ships/hcs-surety-layout.md (child page, contract
family pattern) — AFTER parent`)

Gate proof:

- docs/campaign/MIGRATION-LEDGER.md:84 `REVIEWED-BY-HUMAN: 2026-07-13 — user instructions: "at
  least 5 rounds of iterative improvements"... Blessing covers exactly the 11 lines below.`
  (Round 4 header, line 82)
- docs/campaign/MIGRATION-LEDGER.md:93 `- [ ] ship-child-layout :: entities/vehicles/
  hcs-surety-layout.md → world/ships/hcs-surety-layout.md (child page, contract family pattern) —
  AFTER parent`
- Parent gate: world/ships/hcs-surety.md landed canon (commit 2718ec9, per line-specific brief) —
  "AFTER parent" satisfied.
- INGESTED.tsv check: `grep -F "hcs-surety-layout.md" archive/2026-07/INGESTED.tsv` — no hit,
  not previously ingested.

Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/vehicles/hcs-surety-layout.md — triage: entity-source (ship child page, family
      plan already scoped in ss4-ship-surety-parent.md), ready, written

## Claims — entities/vehicles/hcs-surety-layout.md

- [x] ship-child :: HCS Surety — Deck Layouts :: world/ships/hcs-surety-layout.md (new) —
      three-deck room-by-room layout, tactical notes, bastion slot mapping; child of
      world/ships/hcs-surety.md per contract's family pattern (%%src: legacy%%, page-level only)

## Naming resolution (matches parent precedent)

Source page is titled "Uncertainty — Deck Layouts" and frames the ship under its post-refit
identity throughout (`Now sailing as [[uncertainty|the Uncertainty]]`). Parent's own naming
resolution (queue file ss4-ship-surety-parent.md) already settled this family on the **source
title** — filename `hcs-surety` / `hcs-surety-layout` — with the rename carried as an alias/prose
mention, not the page title. Same resolution applied here for consistency within the family:
title `# HCS Surety — Deck Layouts`, opening prose keeps the Uncertainty mention as plain
descriptive text (both names already resolve — `hcs-surety` is a real page, `uncertainty` is not
yet, so it stays a relink flag, not a wikilink, matching parent's own treatment of that name).

## Section mapping (ship type: Player-Known · DM Only · Stats & Combat · Crew · Appearances)

- Player-Known: general physical shape (three decks, dimensions, purpose) — safe/public-level
  description in the source's own opening italics block, plus the general deck-existence facts
  actual play already corroborates (galley, hold — see Status determination below). The
  room-by-room tactical tables themselves are DM pull-up reference, not table-known text.
- DM Only: one structural note carrying the source's own `audience: dm` framing forward (matches
  parent's own DM Only pattern of one meta-note about the source's framing) — no secret/hidden
  content found in this source beyond ordinary tactical reference (it's the party's own ship, not
  an antagonist asset with concealed plot).
- Stats & Combat: the three deck tables (Weather Deck, Gun Deck, Hold) verbatim, plus Bastion Slot
  Mapping — matches contract's "ship stats live in a body table... under Stats & Combat."
- Crew: this source has no crew content (all crew facts live on the parent page already). Left as
  a pointer back to the parent per contract's "children back-linking the parent," not duplicated.
- Connections: the source's own `## Connections` list, filtered through the standard relink rules
  below.

## Flags

- relink: uncertainty — same disposition as flagged on the parent's own queue file
  (ss4-ship-surety-parent.md FAMILY PLAN); no page yet, not part of this 5-file family, DM
  disposition call still open. Plain text throughout this page too.
- still deferred (canon_gate) — hcs-surety-manifest: `world/ships/
  hcs-surety-manifest.md` landed (canon) at link-restoration pass R4
  (2026-07-14). This flag lives on `world/ships/hcs-surety-layout.md` itself,
  which is `status: canon` and not named on R4's 13-path ledger line — out of
  this pass's editable scope. Not resolved.
- relink: hcs-surety-dm-guide — source's own `## Connections` names "DM Guide — tactical and
  operational reference"; sibling companion-fold, ledger `ship-dm`, not yet dispatched. Plain
  text.
- real wikilink (not deferred) :: [[hcs-surety]] — required back-link per contract's child-page
  pattern ("children back-linking the parent"); parent page confirmed canon and landed. Added to
  both the opening prose (source already names it: "Hull unchanged from [[hcs-surety|HCS Surety]]"
  in its own source text) and this page's own `## Connections`.
- reverse-relink flag — checked at link-restoration pass R4 (2026-07-14),
  still NOT actioned. The parent page `world/ships/hcs-surety.md`'s own
  `## Connections` "Deck Layouts" line is a real candidate now that this page
  is landed, but `hcs-surety.md` is `status: canon` and R4's own ledger line
  names only 13 paths — `hcs-surety.md` is not one of them. canon_gate still
  blocks this edit even for the dedicated link-restoration pass. Still
  deferred; needs its own ledger line to resolve.
- tag mapping: source `tags: [maritime]` — not in `world/_meta/tags.md`'s controlled vocabulary
  (checked: no hit). Also a likely export-default across the whole vehicle sub-pile (claim-buckets
  rules-row shortcut: uniform frontmatter across a pile isn't a per-file signal) — every vessel
  source file in this family plan (parent, this page) carries the same tag. Dropped, matching
  parent's own `tags: []` landing. No canonical Domain tag forced — this page's content is
  reference tables (room dimensions, hazard DCs), not prose carrying a dominant tone.
- frontmatter drops, matching parent/vethka/greyteeth-runner precedent: `campaign`, `audience`,
  `confidence_level`, `sources`, `summary` (folded into Player-Known's opening prose instead of
  dropped silently). `subtype: ship-layout` has no contract-governed equivalent for `type: ship`
  child pages (contract governs `ship_class`/`tier`/`home_port` only, no `subtype` key for this
  type) — dropped; the child-vs-parent distinction is carried by the filename pattern
  (`<ship-slug>-<part-slug>.md`) and the Crew section's back-link note, not a frontmatter key.
- ship_class / tier: both directly stated in THIS source file's own text (opening italics:
  "Patrol cutter. 80 ft × 22 ft beam. Three decks."; Bastion Slot Mapping: "4 facility berths at
  Tier 1") — carried onto this page's frontmatter as source-stated facts, not borrowed from the
  parent/a sibling. `home_port` not stated in this source; landed `""` per `vethka.md` precedent
  (key present, empty value, not omitted).
- Uncertainty-refit content (bracketed inline notes throughout the source: new figurehead, ram
  plate, Weapons Locker gear swap, Surgeon's Berth relocation, crew-mess conversion, refit galley
  in the hold, decommissioned brig) — transcribed verbatim into the Stats & Combat tables per
  fidelity (the source states these as facts about the current, in-play ship, not speculative
  future prep — Session 03's refit is already corroborated canon on the parent page). Not treated
  as a contradiction against the parent's "at time of capture" stat block: both pages describe
  different points in the same ship's timeline, same non-conflict reasoning the parent's own queue
  file already applied to `uncertainty.md`.
- Status determination: rung 2 of the migration-mode status ladder (actual play beats source
  frontmatter's `audience: dm`/`publish: false`) — same ladder, same rung as the parent, evidence
  specific to this page's own room-level content (not just "the ship appears"):
  `sessions/01-boarding-of-the-saltwright/transcript.md:33` (weather-deck action — "launched her
  up through the hatch... wings snapped open the moment she cleared the weather deck," matching
  this page's own Weather Deck / Companionway Hatch zones) and `sessions/01-boarding-of-the-
  saltwright/transcript.md:49` (the gangplank standoff, matching the Foredeck zone's boarding
  context) on the Saltwright side of the same boarding action carrying onto the Surety;
  `sessions/02-conflict-is-a-surety/transcript.md:47,49` (Shepherd Grigori scene — "the HCS Surety
  galley," matching this page's Deck 2 Galley zone) and `:51` ("Ket watches from his brass cage in
  the HCS Surety hold," matching this page's Deck 3 / former Prisoner brig zone, pre-decommission
  at that point in the timeline). Landed `status: canon`.
- No CONTRADICTION found against `world/ships/hcs-surety.md` (parent) or other landed pages. The
  parent's own "Interior reflected Crown patrol service — officer cabin aft, crew hammocks
  forward, boarding locker amidships, chart table forward, two-prisoner cage bolted below"
  corroborates this page's own pre-refit room layout rather than conflicting with it.
- Provenance note (friction, not actioned on this page): the parent page `world/ships/hcs-surety.
  md` carries inline `%%src: legacy%%` marks after nearly every paragraph despite being a single,
  fully-migrated legacy source (`created: legacy`). source-ingest's Hard Rule 2 and DISPATCH.md's
  Writing section both state inline `%%src: legacy%%` is "banned as noise" on a fully-migrated
  page — page-level `created: legacy` says it once. This page (`hcs-surety-layout.md`) follows the
  written rule literally: single page-level citation, no inline marks. Flagged for the DM /
  canon-review rather than silently matched to the parent's (apparently non-conforming) pattern or
  silently fixed on the parent (canon-gate: not this dispatch's ledger line to edit).
