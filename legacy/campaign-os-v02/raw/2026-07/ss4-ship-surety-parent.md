# Source ingest queue: ss4-ship-surety-parent

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/vehicles/hcs-surety.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md § Round 4 — `ship-parent ::
entities/vehicles/hcs-surety.md → world/ships/hcs-surety.md — Tier-3 family PARENT (5 source
files total); this line = parent page only; family plan documented in queue file`)

Gate proof:

- docs/campaign/MIGRATION-LEDGER.md:84 `REVIEWED-BY-HUMAN: 2026-07-13 — user instructions: "at
  least 5 rounds of iterative improvements"... Blessing covers exactly the 11 lines below.`
  (Round 4 header, line 82)
- docs/campaign/MIGRATION-LEDGER.md:91 `- [ ] ship-parent :: entities/vehicles/hcs-surety.md →
  world/ships/hcs-surety.md — Tier-3 family PARENT (5 source files total); this line = parent
  page only; family plan documented in queue file`

Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/vehicles/hcs-surety.md — triage: entity-source (ship skeleton), ready, written

## Claims — entities/vehicles/hcs-surety.md

- [x] ship :: HCS Surety :: world/ships/hcs-surety.md (new) — Dravosi Crown patrol cutter,
      Tier 1, captured Session 01, renamed Uncertainty after Session 03 refit; parent page of a
      5-file Tier-3 family (%%src: legacy%%)

## FAMILY PLAN (5 source files total — this page is 1 of 5; 4 siblings NOT ingested here)

Read all 4 sibling source files to plan (frontmatter + opening only, per source-ingest's "large
sources: headings/frontmatter first" guidance) — content itself is NOT decomposed into claims by
this dispatch, per line-specific instruction ("Don't ingest sibling content yourself").

| Sibling source | subtype (source fm) | Plan | Target |
|---|---|---|---|
| `hcs-surety-dm-guide.md` | `dm-guide` | **Fold into parent's `## DM Only`** — companion pattern, `pearl-of-souls.md` precedent (its `-dm` companion folded into the item's own DM Only, "one-entity-one-page convention"). Content is DM-facing operational tooling (navigation-failure tables, chase complications, the *active* Crown recognition clock, bastion/defence mechanics) — same relationship as an item's public/DM companion pair, not a distinct entity. | `world/ships/hcs-surety.md` § DM Only (edit, not new page) |
| `hcs-surety-layout.md` | `ship-layout` | **Child page** — full three-deck room-by-room layout with tactical notes and bastion-slot mapping. This is reference material a DM pulls up mid-scene, not a fact folded into the parent's prose; matches contract's child-page criterion (`<ship-slug>-<part-slug>.md`, "children back-linking the parent"). | `world/ships/hcs-surety-layout.md` (new child, ledger: `ship-child-layout`) |
| `hcs-surety-manifest.md` | `ship-manifest` | **Child page** — itemized post-Session-02 inventory by room, tracked through the La Vasca refit. Same reasoning as layout: reference table, not prose fact. | `world/ships/hcs-surety-manifest.md` (new child, ledger: `ship-child-manifest`) |
| `hcs-surety-owners-manual.md` | `ship-rules` | **Child page** — player-facing rules reference (`audience: players`, `publish: true` in source), crew roles/upkeep/travel/combat/guns/bastion facilities. Distinct audience and distinct function from the DM guide; matches contract's child-page pattern, not a DM Only fold (folding player-facing rules into the parent's Stats & Combat would bury a stand-alone reference doc other skills may want to link independently, e.g. `ship-prep`). | `world/ships/hcs-surety-owners-manual.md` (new child, ledger: `ship-child-manual`) |

All 4 already have ledger lines (MIGRATION-LEDGER.md:92-95, `ship-dm`/`ship-child-layout`/
`ship-child-manifest`/`ship-child-manual`), each explicitly "AFTER parent" / "DISPATCH AFTER
parent lands" — this dispatch is that trigger. Parent page committed below; siblings are 4
separate future dispatches, not this one's to execute.

**`uncertainty.md` is explicitly NOT one of the 5.** A 6th sibling-shaped source file exists at
`entities/vehicles/uncertainty.md` (post-refit identity: different captain [Delmar Fisk], updated
stats [hull_points 130 vs. 120, hull_ac 11 w/ forward-hull bonus, ram bow, 4 ft draft, `status:
active`/`condition: pristine` vs. this page's `status: lost`/`condition: worn`], `tags: [maritime,
recurring]` vs. this page's `[dravosi]`). The line-specific brief's own math ("5 source files
total") confirms it's deliberately excluded from this family — the ledger's disposition for it
is a future call (a 6th ledger line, not yet written), not this dispatch's. Per the line-specific
instruction "reconcile naming: source page title vs the rename; aliases: field is the tool," the
resolution executed here is: this page keeps the **source title** ("HCS Surety" — matches the
`hcs-surety.md`/`world/ships/hcs-surety.md` filename/ledger path) and records the rename via
`aliases: [Uncertainty, CS-1147]`, sourced from `hcs-surety.md`'s own text (its subtitle line
states the rename and links `[[uncertainty|the Uncertainty]]`; its Connections section lists
"Uncertainty — current identity; full refit record"). `uncertainty.md`'s *divergent* content
(new captain, new stats, refit-era facilities) is NOT transcribed onto this page — that would
mean writing claims from a source file this ledger line doesn't name. Flagged below for the DM:
whether `uncertainty.md` becomes a 6th ledger line that *expands this same page* (post-refit
state update, since it's naming the same hull) or a separate page is a disposition call outside
this dispatch's scope.

## Flags

- relink: barnaby-rook — former commanding officer, `entities/characters/npcs/barnaby-rook.md`
  in source repo; no `world/npcs/barnaby-rook.md` yet. Plain text throughout (Player-Known,
  Crew, Connections).
- relink: capn-gorgeous — enforcer, killed Session 01; no page yet. Plain text in Crew.
- relink: geoffrey-draves — ship's carpenter, defected to party Session 01; no page yet. Plain
  text in Crew. (Note: MIGRATION-LEDGER.md Round 1 area shows a `situation :: draves` line
  elsewhere in this ledger's history — not re-litigated here; this page's own mention stays
  plain text regardless, since no `world/npcs/geoffrey-draves.md` exists in `world/` today.)
- relink: dravosi-crown — registered authority; no `world/factions/dravosi-crown.md` yet
  (`world/lore/tyr.md` and `world/ships/greyteeth-runner.md` mention "Dravosi" in aliases.md but
  neither is this faction's own page). Plain text in Connections.
- relink: surety-missing — "Crown Search," the active situation page the source links for the
  Crown Recognition Clock's escalation track; no page yet (no owning faction stated in source
  either — homeless situation per claim-buckets, DM call whether it gets its own page or folds
  into a future `dravosi-crown` faction's Front). Clock content transcribed verbatim into this
  page's DM Only in the meantime (claim-buckets: "write the identity facts wherever they land").
- relink: kalowe-takowan — "Ship Disguise — Kalowe" option; no page yet, unclear type (rule?
  item?). Plain text in Connections, one collapsed note.
- relink: port-tidefall — registry port ("registered out of Port Tidefall under Lieutenant B.
  Rook"). No `world/locations/port-tidefall.md` yet (`world/ships/greyteeth-runner.md` already
  defers the same target the same way). `home_port:` frontmatter set to plain string `"Port
  Tidefall"` — matches `greyteeth-runner.md`'s exact precedent (plain text in a wikilink-typed
  key when the target doesn't exist yet, not a stub `[[wikilink]]`).
- relink: uncertainty — see FAMILY PLAN above; not a page yet, not part of this family, DM
  disposition call flagged there.
- still deferred (canon_gate) — hcs-surety-layout / hcs-surety-manifest /
  hcs-surety-owners-manual — this page's own future family children/DM-fold;
  see FAMILY PLAN table. All three landed (canon) as of link-restoration pass
  R4 (2026-07-14), and this page's own Connections section still names them
  in plain text — but `world/ships/hcs-surety.md` itself is `status: canon`
  and not named on R4's 13-path ledger line, so restoring these three
  wikilinks is out of this pass's editable scope. Not resolved.
  hcs-surety-dm-guide never became a separate page (folded into this page's
  own DM Only per `ss4-ship-surety-dm.md`) — nothing to relink for that one.
- real wikilink (not deferred) :: [[alys-kuiper]] — added to `## Crew` per line-specific
  instruction. Source `hcs-surety.md` itself only names Rook/Gorgeous/Draves + "8 privateer
  ratings" (unnamed), but `world/npcs/alys-kuiper.md` (already landed, DONE 49d1e23) states "Post:
  Formerly HCS Surety, under Barnaby Rook" in its own Player-Known table, and its own queue file
  (`archive/2026-07/ss3-crew-alys-kuiper.md` § Flags) explicitly pre-authorizes this exact
  reverse-relink: "Once `world/ships/hcs-surety.md` lands, restore the wikilink AND add Alys to
  that page's own `## Crew`." Executed here. Citation: corroborating page, not this source file —
  `%%src: legacy%%` still applies (both pages migrate the same legacy corpus).
- real wikilink (not deferred) :: [[estratto]] — added to `## Connections` per line-specific
  instruction. Source `hcs-surety.md` doesn't mention Estratto at all; `world/npcs/estratto.md`
  (already landed, `status: pending`) states in its own DM Only: "Estratto currently holds a
  debt-recovery writ for the vessel players know as the *Uncertainty* (Concordat records: the
  *HCS Surety*)." `estratto.md`'s own queue file already deferred this exact link ("still
  deferred: ... hcs-surety ... — no pages exist for any of these yet") pending this page's
  landing. Executed here (this page → estratto, one direction only — editing `estratto.md` itself
  to restore its own deferred link is the link-restoration pass's job, not this dispatch's,
  per DISPATCH.md's "reciprocal links into pages you don't own" rail).
- tag mapping: source `tags: [dravosi]` — entity-identity/origin tag (a faction/nation name).
  DROPPED per WIKI.md § Tag taxonomy. No replacement canonical Domain tag forced: this page's
  own prose (patrol-service overview, facilities inventory, crew roster, capture-and-refit
  session log) doesn't carry one dominant tone the way `vethka.md`'s raiding-vessel read-aloud
  carried `war`/`heist` — the one violent beat (Session 01 boarding) is reported flatly as a
  log entry, not written with that tone on this page itself. Landed `tags: []` (contract:
  "always legal," no force-fit).
- frontmatter drops, matching `vethka.md`/`greyteeth-runner.md` precedent: `campaign`,
  `audience`, `confidence_level`, `sources`, `summary` — no contract-governed equivalent for
  `type: ship`; `summary` content folded into the read-aloud + Overview prose instead of dropped
  silently. Source's own `status: lost` (its wiki's status vocabulary, not ours) is NOT the same
  axis as this contract's canon-tier `status:` — noted in DM Only as a citation footnote so a
  future reader doesn't conflate the two.
- session-pipeline convergence (flag for CANONIZE, not actioned here): `sessions/
  01-boarding-of-the-saltwright/state-changes.md:19` and `sessions/02-conflict-is-a-surety/
  state-changes.md:24` both carry an unchecked `[ ] NEW world/ships/hcs-surety.md` line, still
  unapplied. This migration-mode write lands the page first (authorized separately by the
  MIGRATION-LEDGER.md line above). When CANONIZE eventually processes those two session
  state-changes files, it will find the page already exists — expand/corroborate in place, same
  pattern already executed for `world/npcs/alys-kuiper.md` at `sessions/
  02-conflict-is-a-surety/state-changes.md:22` ("Page already exists ... corroborates rather than
  duplicates"). `## Appearances` on this page cites the two session transcripts by file:line
  (status-determination evidence) but does NOT write the literal `- [[sNN-slug]]` append-only
  bullets — that format is CANONIZE's to append, not this skill's (contract: "maintained by
  CANONIZE").
- Status determination: rung 2 of the migration-mode status ladder (actual play beats the
  source's own `audience: dm`/`publish: false` frontmatter). Evidence, in this repo (not the
  source repo — a rarer case than usual, since campaign-os's own sessions 01-02 already exist):
  `sessions/01-boarding-of-the-saltwright/transcript.md:49,83,94` (the Session 01 boarding
  itself: "The gangplank between the Saltwright and the HCS Surety was where things got
  complicated," plus two further named mentions) and `sessions/02-conflict-is-a-surety/
  transcript.md:73,81,99,116` (Session 02: "The HCS Surety set heading for Calveno," the storm/
  whip-shark strikes, and the summary table). Landed `status: canon`.
- No CONTRADICTION found between `hcs-surety.md` and existing `world/` pages. `alys-kuiper.md`'s
  "Formerly HCS Surety, under Barnaby Rook" and `estratto.md`'s writ description both corroborate
  rather than conflict with this source. `uncertainty.md`'s divergent post-refit stats are a
  *different source file* describing a *later state*, not ingested here — not a contradiction
  against this page's own (earlier, at-capture) stat block, since neither claims to describe the
  same point in time; flagged above as a disposition question, not resolved as a contradiction.
