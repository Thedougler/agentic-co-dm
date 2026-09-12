# Source ingest queue: ss4-ship-surety-manifest

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/vehicles/hcs-surety-manifest.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md § Round 4 — `ship-child-manifest ::
entities/vehicles/hcs-surety-manifest.md → world/ships/hcs-surety-manifest.md — AFTER parent`)

Gate proof:

- docs/campaign/MIGRATION-LEDGER.md:84 `REVIEWED-BY-HUMAN: 2026-07-13 — user instructions: "at
  least 5 rounds of iterative improvements"... Blessing covers exactly the 11 lines below.`
  (Round 4 header, line 82)
- docs/campaign/MIGRATION-LEDGER.md:94 `- [ ] ship-child-manifest :: entities/vehicles/
  hcs-surety-manifest.md → world/ships/hcs-surety-manifest.md — AFTER parent`

Parent gate: `world/ships/hcs-surety.md` exists, `status: canon`, committed (2718ec9) — confirmed
by Read before writing. This dispatch does NOT edit the parent.

Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/vehicles/hcs-surety-manifest.md — triage: entity-source (ship-manifest subtype,
      child of hcs-surety family), ready, written

## Claims — entities/vehicles/hcs-surety-manifest.md

- [x] ship (child) :: HCS Surety — Manifest :: world/ships/hcs-surety-manifest.md (new) —
      post-Session 02 room-by-room cargo/arms/provisions inventory, updated through the La Vasca
      refit; back-links parent [[hcs-surety]] (%%src: legacy%%)

## Status determination

Rung 2 of the migration-mode status ladder (actual play beats source's own `audience: dm`/
`publish: false` frontmatter — same rung the parent landed on). Evidence, this repo's own
sessions: `sessions/02-conflict-is-a-surety/transcript.md:69` — "Rook's cabin: 45 gp, letters of
marque, a blunderbuss. Under the floor: 110 gp, two garnets. The cargo held a pendant engraved
*For Mira, from the sea*, and a crate — flintlocks, Mira's Blade, twenty vials of Grung poison
tincture..." — directly corroborates this page's "Gun Deck — Former Captain's Cabin" table (45 gp,
110 gp, 2 garnets, blunderbuss, letters of marque) and "General Cargo" table (seized goods
crate/pendant, confiscation crate/flintlocks/Grung tincture). Landed `status: canon`.

Additional corroboration (not contradiction): `pcs/jean-claude-tabarnack.md` inventory already
lists "Twenty vials of Simone's tincture — kept hidden in HCS Surety cargo, said nothing to the
party" — matches this page's Confiscation crate entry exactly (qty 20, Jean-Claude controlling).
Not a CONTRADICTION; corroborating.

## Frontmatter drops (matching parent `hcs-surety.md` precedent)

`campaign`, `audience`, `confidence_level`, `sources`, `summary` dropped — no contract-governed
equivalent for `type: ship`. Source `updated:` field folded into `touched: legacy` per the
migrated-content convention, not carried as its own key.

`ship_class` / `tier` / `home_port` omitted entirely (not present, not empty strings) — this
source (a manifest, not a hull description) states none of these, and lint's `TYPE_KEY_ENUMS`
check rejects an empty-string `tier` as a present-but-invalid value — first-attempt lint
failure, fixed by omitting the key rather than leaving
it empty, since presence isn't enforced. Fidelity-only also means not restating the parent's own
values onto a second page from a source that doesn't itself say them — a reader following
[[hcs-surety]] gets those facts from the one page that actually states them.

Tag: source `tags: [maritime]` — not in `world/_meta/tags.md`'s canonical vocabulary (checked;
no `maritime`/`nautical`/`ship` domain tag exists), and not an identity/origin tag either — it's
simply not-yet-canonical. No force-fit substitute; landed `tags: []` (contract: "always legal").

## Section mapping (ship skeleton has 5 required H2s; this source is table-heavy, not prose-heavy)

- **Player-Known**: bulk of the manifest — Weather Deck, Crew Quarters, Galley ×2, Chart Table,
  Surgeon's Berth, Crew Mess, Former Captain's Cabin, Chain Locker, Provisions Store, former Brig
  note, General Cargo, Currency Summary. This is the party's own ship; its general inventory reads
  as known-to-the-table, not DM secret (nothing in the source itself is marked hidden-from-players).
- **DM Only**: provenance/status footnote (source's own `audience: dm` frontmatter vs. this
  contract's canon-tier `status:` — same non-conflation footnote pattern as the parent page) plus
  one prep-lead note (the "Galewall anchorage" map marking — an unresolved hook the source itself
  states, not invented).
- **Stats & Combat**: Weapons Locker + Powder Magazine tables — the combat-loadout content, which
  fits this heading better than Player-Known's general-inventory framing. Hull/AC/speed stats stay
  on the parent only (not restated here).
- **Crew**: this source has no crew roster (that's the parent's own section) — stub note pointing
  to `[[hcs-surety]]` § Crew, per fidelity (no roster in this source to transcribe).
- **Appearances**: same rung-2 evidence writeup as Status determination above, prose form (the
  literal `- [[sNN-slug]]` append-only bullet stays CANONIZE's to write, per contract).
- **Connections** (optional H2, skeleton carries it): back-link to parent plus every relink flag
  below, grouped here so Appearances stays pure session evidence — same convention the parent page
  used.

## Flags

- real wikilink (not deferred) :: [[hcs-surety|HCS Surety]] — parent back-link, required per
  line-specific dispatch instruction. Parent exists, `status: canon`, committed 2718ec9.
- real wikilink (not deferred) :: [[calveno-la-vasca|La Vasca]] — the refit location. Source
  itself wikilinked `[[la-vasca|La Vasca]]`, but the page that actually landed (confirmed by Read,
  canon) is `world/locations/calveno-la-vasca.md` (slug differs from the source's own guess —
  city-builder's district-child filename convention, `<settlement>-<district>`). Linked to the
  real target, not the source's stale slug guess.
- real wikilink (not deferred) :: [[jean-claude-tabarnack|Jean-Claude]] — PC page already landed
  (`pcs/jean-claude-tabarnack.md`, `status: canon`); confirmed via stub check before writing. Used
  in the Confiscation crate note ("20 vials... Jean-Claude controlling").
- relink: uncertainty — "The ship now sails as Uncertainty." Not part of this 5-file family (see
  parent's own FAMILY PLAN disposition note in `archive/2026-07/ss4-ship-surety-parent.md`);
  not re-litigated here, same plain-text treatment.
- relink: cobb — "Items marked Refit were added by Cobb..." No `world/npcs/cobb.md` yet (confirmed:
  `world/locations/calveno-la-vasca.md` § Notable NPCs and `pcs/perrin-black-jaw.md` both already
  flag the identical relink — third page now naming this gap).
- relink: nona-black-jaw — "...on Nona Black-Jaw's account." No page yet (same gap already flagged
  by `pcs/perrin-black-jaw.md` and the parent's own FAMILY PLAN discussion).
- relink: barnaby-rook — "Captain's log (Rook's)" and "letters of marque... Rook's privateer
  authority." No page yet (same gap the parent already flags).
- relink: dravosi-crown — "Crown Islands survey charts," "Crown commission papers." No page yet
  (same gap the parent already flags).
- relink: delmar-fisk — "Loaded blunderbuss ... Status: Delmar." No `pcs/delmar-fisk.md` yet
  (session ledger's own unapplied `NEW pcs/delmar-fisk.md` line, confirm-PC-on-review caveat still
  open per `docs/campaign/MIGRATION-LEDGER.md`'s session pipeline — not this dispatch's to create).
- relink: sem-holst — "Sem's tool kit... Not party property." No `world/npcs/sem-holst.md` yet
  (session 02 state-changes' own unapplied `NEW world/npcs/sem-holst.md` line: "Sem Holst the
  shipwright").
- relink: signal-lantern — appears twice (aft-rail + hold partner), custom mechanic ("25-word
  Passage messages up to 30 miles" — ties to `world/factions/the-passage.md`, also not yet landed).
  Distinct from generic ship gear; worth its own future `item` page. No `world/items/
  signal-lantern.md` yet (stub check run, confirmed empty).
- relink: letters-of-marque — "Crown commission papers / letters of marque... Rook's privateer
  authority; useful as forgeable reference." Setting-specific narrative document tied to a named
  NPC's authority, not a generic template — flagged as a future `item`/`lore` candidate rather than
  collapsed into the generic-gear note below. No page yet (stub check run, confirmed empty).
- ~~relink: hcs-surety-layout~~ SUPERSEDED at staleness recheck — sibling landed mid-run
  (`3a78e41 ingest(ss4-ship-surety-layout)`, `status: canon`) after this page's original draft.
  Upgraded to a real `[[hcs-surety-layout|HCS Surety Deck Layouts]]` wikilink in Connections.
- Noted, not reconciled (independent editorial call, not a contradiction): the layout sibling
  restated `ship_class: patrol cutter` / `tier: 1` on its own child-page frontmatter (matching the
  parent's values), where this page instead omitted those keys per the fidelity-only reasoning
  above (this source doesn't state them). Both pass lint; flagging the divergence for a human
  consistency call across the family, not fixing it myself — the family's own convention on
  whether child pages restate parent hull-class data isn't settled by this dispatch's ledger line.
- generic ruleset/provisions collapse (Hard Rule "SRD/PHB stock gear is never a link target," same
  reasoning extended to generic ship chandlery/provisions): Potion of Healing (SRD item — no
  campaign-specific mechanics beyond a standard consumable), Anchor chain, Salt fish, Rice, Dried
  beans, Fresh citrus, Water cask, Small beer barrel, Cooking oil. Source wikilinked all of these;
  none has a `world/items/` page (stub check run, confirmed empty for every one); no per-item
  relink flags — one collapsed note per skill instruction. Landed as plain text.
- No CONTRADICTION found. This page's inventory corroborates rather than conflicts with
  `sessions/02-conflict-is-a-surety/transcript.md:69` and `pcs/jean-claude-tabarnack.md`'s own
  inventory line (see Status determination above). `Mira's Blade` — named in the transcript as
  taken from the same crate and given to Perrin — is correctly ABSENT from this manifest (it left
  the ship), consistent, not a gap.
- session-pipeline convergence (flag for CANONIZE, not actioned here): this page's underlying
  facts (cabin loot, cargo crates) are also implicitly covered by `sessions/02-conflict-is-a-surety/
  state-changes.md`'s unapplied `NEW world/ships/hcs-surety.md` line (same pattern the parent
  flagged) — when CANONIZE processes that line it will find both the parent and this child already
  landed; corroborate in place, don't duplicate.

## Staleness recheck (before finalizing)

`find world pcs -name "*.md" -newer archive/2026-07/ss4-ship-surety-manifest.md` run
immediately before commit — see report for result; any new sibling landing re-resolved before
commit if it names an entity this page mentions.
