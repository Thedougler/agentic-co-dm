# Source ingest queue: ss4-district-la-vasca

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/places/settlements/calveno/la-vasca.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — Round 4 — `district :: entities/places/settlements/calveno/la-vasca.md → world/locations/calveno-la-vasca.md — subtype: district, parent [[calveno]] (city-builder filename convention; first district child)`)
Started: 2026-07-13

Gate proof (docs/campaign/MIGRATION-LEDGER.md):

```text
84:REVIEWED-BY-HUMAN: 2026-07-13 — user instructions: "at least 5 rounds of iterative
85:improvements", "include rounds on ingestion testing and refinement from
86:~/ai-os/shattered-sea raw [interpreted: notebooklm-export/ + Inbox/, the unformatted
87:piles] to test against unformatted documents, and also the player character related
88:files". The PC lines below are the canon-review signature PC creation requires — the
89:user explicitly directed PC-file ingestion. Blessing covers exactly the 11 lines below.
96:- [ ] district :: entities/places/settlements/calveno/la-vasca.md → world/locations/calveno-la-vasca.md — subtype: district, parent [[calveno]] (city-builder filename convention; first district child)
```

## Sources (batch order, smallest file first)

- [x] entities/places/settlements/calveno/la-vasca.md — triage: location-source, ready

## Claims — entities/places/settlements/calveno/la-vasca.md

- [x] location :: La Vasca :: world/locations/calveno-la-vasca.md (new) — subtype: district (per ledger line), status: canon (rung 2 — actual play, see Flags). Player-Known (arrival facts, At a Glance table), DM Only (password, interior detail, Cobb's [!dm] guidance + sample lines, Services menu, revealed-ness note), Notable NPCs (Cobb, plain text), Hooks (Cobb→Nona report, the manifests), Appearances (Session 3, source-repo citation only). (%%src: legacy%%)

## Flags

- **subtype/hierarchy tension — followed the ledger line as written, flagging
  for review.** The source's own frontmatter places La Vasca *inside* Le
  Paludi (`building_type: private-drydock`, `district: Le Paludi`) — a
  single building within one of Calveno's five real districts (Mercatura,
  Bridge, Arsenal, Le Paludi, Velo Quarter — see `world/locations/
  calveno.md` § Districts). The ledger line directs `subtype: district`
  with `[[calveno]]` as the *direct* parent, skipping the Le Paludi level
  entirely — that's a district nested inside what wiki-contract.md defines
  as a single-level settlement→district tree, and arguably a better fit for
  `subtype: building` under a future `calveno-le-paludi.md` district page.
  Followed the ledger's explicit instruction per source-ingest's canon
  discipline (the ledger line is the law, not mine to override) and wrote
  `subtype: district`, parent `[[calveno]]` — flagging the hierarchy
  question for wave review rather than silently resolving it.
- **Status determination — rung 2 (actual play), not rung 3
  (frontmatter).** Source frontmatter is `audience: dm`, `publish: false`,
  own `status: active` — none of those alone justify `canon` under the
  migration-mode ladder (rung 3 requires *per-file* `audience: players` +
  `publish: true`, which this isn't). Rung 2 applies instead: the source
  repo's session-03 recap directly corroborates the party physically at La
  Vasca — arrival, Cobb greeting them, ship in dry dock, 5-day repair —
  citing `shattered-sea/wiki/sessions/session-03-recap.md:111,193,226` and
  the raw form `.raw/sessions/session-03/notes/Session-03-Recap.md:
  122,208,241`. `world/locations/calveno-la-vasca.md` written `status:
  canon` on that basis. Facts the recap does NOT corroborate (access
  password, Cobb's reporting mechanism, interior tool/manifest detail,
  Services menu) stayed in `## DM Only` per rule 10 (unsure whether
  something was revealed at the table means it wasn't) — page-level
  `status: canon` does not promote every granular fact to Player-Known.
- **Tag substitution — `passage` dropped, `intrigue` mapped.** Legacy tag
  `passage` names the smuggling org "the Passage" (identity tag, dropped by
  design — WIKI.md § Tag taxonomy). One genuine tonal mapping made instead:
  `intrigue` — the page's own content carries it (password-gated hidden
  access, a cover story, an informant relationship where warmth and
  reporting-on-a-friend coexist). Same substitution precedent as
  `ss-location-calveno.md`'s queue file.
- **Estratto — dispatch's conditional link NOT applied.** The dispatch
  prompt flagged "La Vasca is Estratto's stated current location" as a
  possible real link (`world/npcs/estratto.md` exists). Checked: the
  *source file being ingested here* (`la-vasca.md`) never names Estratto,
  Auditor, Concordat, Fisk, warforged, or construct — zero hits. Fidelity
  rule (Hard Rule 1) forbids importing a fact my own source doesn't state,
  even when a sibling page states it independently. No Estratto link/
  mention added to `calveno-la-vasca.md`.
  **Reverse-relink — resolved ✓ (link-restoration pass R4, 2026-07-14).**
  `world/npcs/estratto.md` (status: pending, not canon — editable) had both
  plain-text mentions converted: `[[calveno|Calveno]] — [[calveno-la-vasca|La Vasca]]`
  (infobox row) and `[[calveno|Calveno]] / [[calveno-la-vasca|La Vasca]] — current deployment location`
  (Relationships bullet).
- **Calveno's side — checked at link-restoration pass R4 (2026-07-14), NOT
  applied.** `world/locations/calveno.md`'s `### Districts` Le Paludi
  paragraph describes the district in prose but never names "La Vasca" as a
  string anywhere on the page (grep confirmed zero hits) — La Vasca is the
  Black-Jaw family's private dry dock (a building), not the district itself,
  so there is no plain-text mention to convert. Also moot: `calveno.md` is
  canon and not named on R4's ledger line even if a mention existed. Still
  not edited.
- relink: cobb — once its page lands (no `world/npcs/cobb.md` exists yet;
  zero hits anywhere in `world/`/`pcs/`, case-insensitive)
- relink: le-paludi — once its page lands (mentioned in `calveno.md` §
  Districts prose too, still no dedicated page)
- relink: warren — once its page lands (aka "the Warren")
- relink: nona-black-jaw — once its page lands
- **resolved ✓ (link-pass R6, 2026-07-14)** — perrin-black-jaw: `calveno-la-vasca.md`
  is on R6's ledger line now; "arrangement through Perrin" links `[[perrin-black-jaw|Perrin]]`.
- **resolved ✓ (link-pass R6, 2026-07-14)** — hcs-surety: "formerly the HCS
  Surety" (Player-Known) links `[[hcs-surety|HCS Surety]]`.
- relink: the-passage — once its page lands (org name in the "Known To"
  row; same flag `ss-location-calveno.md` already carries)
- Services menu (registry plate removal, hull caulking, timber and
  fittings): source links these as `[[wikilink]]`s but they read as generic
  service line-items, not concrete named entities per Stub Creation's "never
  for a vague reference" rule — no per-item relink flags added, one
  collapsed note only (same treatment as SRD/PHB stock gear).
