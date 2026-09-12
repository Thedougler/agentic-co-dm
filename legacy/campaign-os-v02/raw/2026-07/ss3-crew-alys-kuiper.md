# Source ingest queue: ss3-crew-alys-kuiper

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/characters/crew/alys-kuiper.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md § Round 3 — `crew ::
entities/characters/crew/alys-kuiper.md → world/npcs/ — ship-crew concept test: crew NPC with a
vessel affiliation, npc skeleton + location/Connections handling per what the source states`)

Gate proof:

- docs/campaign/MIGRATION-LEDGER.md:63 `REVIEWED-BY-HUMAN: 2026-07-13 — same user instruction;
  blessing covers exactly the 14 lines below.` (Round 3 header, line 61)
- docs/campaign/MIGRATION-LEDGER.md:78 `- [ ] crew :: entities/characters/crew/alys-kuiper.md →
  world/npcs/ — ship-crew concept test: crew NPC with a vessel affiliation, npc skeleton +
  location/Connections handling per what the source states`

Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/characters/crew/alys-kuiper.md — triage: npc (crew subtype folds into npc — no
      dedicated `crew` type in wiki-contract.md's `type:` enum), ready

## Claims — entities/characters/crew/alys-kuiper.md

- [x] npc :: Alys Kuiper :: world/npcs/alys-kuiper.md (new) — ship's surgeon, clinical/calm
      roleplay concept, Crown-frigate backstory she won't finish explaining, recruitment hook
      (formal Surgeon's Berth role), credits Shepherd Grigori for the Murrat casualties (%%src: legacy%%)

## THE CREW-AFFILIATION CONVENTION (this line's designated test)

Question: where does a crew NPC's vessel affiliation live — npc `location:` frontmatter, prose in
`## Relationships`, or the ship page's own `## Crew`?

**Decision: `## Relationships`, plain text. `location:` stays empty (`""`).**

Evidence, not judgment call:

- `wiki-contract.md:50-54` — "`npc`: `location` (optional) — a wikilink to the NPC's current
  location page, e.g. `[[old-harbor]]`. A free link, not an enum: an NPC's location is a fact
  about the world (any `location`-type page)..." (emphasis on "any `location`-type page").
- `wiki-contract.md:12` — the `type:` enum lists `location` and `ship` as two separate, distinct
  page types (`type: npc | location | faction | quest | item | lore | pc | session | encounter |
  creature | rule | ship`). A ship page is `type: ship`, never `type: location`.
- Therefore `location:` is contractually scoped to `type: location` targets only (region/island/
  settlement/district/building/dungeon/plane, per `wiki-contract.md:39`). A ship is not a valid
  `location:` target regardless of how central it is to the NPC's identity — pointing `location:`
  at a ship page would be a type violation, not a stylistic choice.
- The source itself never states a location-type page for her either — her whole identity is
  vessel-bound ("Post: Formerly HCS Surety, under Barnaby Rook"), with no town/region/building
  ever mentioned. This is exactly the friction the mission table predicted: crew = ship-crew
  concept, no home. `location: ""` is the honest contract-conformant answer, not a gap.
- The vessel-affiliation fact instead lands in `## Relationships` as a plain-text crew-of line
  (HCS Surety has no `world/ships/` page yet — not one of this round's 20 known real-wikilink
  targets — so it's plain text + `relink:`, per migration-mode link deferral, same treatment as
  Barnaby Rook and Shepherd Grigori below).
- Ship-side reciprocal edit (`world/ships/hcs-surety.md` § Crew) is explicitly NOT this ledger
  line's to make — no such page exists yet in `world/`, so there is nothing to reverse-relink
  into today. Flagged below for whenever the HCS Surety ship page lands.

## Flags

- relinked ✓ (partial) — hcs-surety — `world/ships/hcs-surety.md` landed (canon); the
  `## Relationships` mention now links `[[hcs-surety|HCS Surety]]`
  (link-restoration pass R4, 2026-07-14). The reverse half — adding Alys to
  `world/ships/hcs-surety.md`'s own `## Crew` — is still NOT done: that page is
  `status: canon` and not named on the R4 ledger line's 13 canon paths, so it's
  out of this pass's editable scope (canon_gate). Still deferred.
- relink: barnaby-rook — former captain of the HCS Surety, source `entities/characters/npcs/
  barnaby-rook.md`; not one of this round's 20 known real-wikilink targets. Plain text only.
- relink: shepherd-grigori — credited (by Alys) with saving the Murrat casualties, source
  `entities/characters/npcs/shepherd-grigori.md`; not one of this round's 20 known real-wikilink
  targets. Plain text only.
- tag mapping: source `tags: [recurring]` — a recurrence/origin-style tag, not a Domain tone tag
  and not an entity-identity tag either; no canonical-taxonomy home. DROPPED per WIKI.md § Tag
  taxonomy (no forced mapping onto a tag the source content doesn't actually carry).
- tag mapping: source content carries a genuine, page-own mystery beat — her unexplained
  departure from a Crown frigate service, stated then deliberately unfinished, corroborated as an
  actual in-play beat by `sessions/session-03-scene-04-five-days.md:152` ("She served on a Crown
  frigate. She stops before she finishes saying why she left."). Maps to canonical Domain tag
  `mystery` — logged, applied. Not a forced fit: this is a stated Chekhov's-Gun-shaped secret, not
  a generic "there's more to her" gesture.
- frontmatter drops, matching estratto/ferrin-locke precedent: `campaign`, `audience`,
  `confidence_level`, `sources`, `summary`, `species`, `pronouns`, `banner`, `portrait`,
  `roleplay` — no contract-governed equivalent for `type: npc`; `species: human` and the
  `roleplay` concept line both folded into prose (Player-Known table row + opening paragraph)
  instead of dropped silently.
- `aliases: []`, not `[Alys]` — deliberate, not an oversight. Session logs consistently call her
  "Alys" (short form), which would be a defensible alias by the contract's own definition ("every
  name the table uses for this entity," `wiki-contract.md:15`). But the *source page itself*
  (`alys-kuiper.md`) carries no `aliases:` field at all — unlike `estratto.md`, whose `[the
  Auditor]` alias is stated verbatim in its own source frontmatter. Per Hard Rule 1 (fidelity to
  the source, never invent past it) and matching `ferrin-locke.md`'s identical precedent
  (no source `aliases:` field → landed `aliases: []`), corroborating session usage is used here
  only for the reveal-status determination (rung 2 below), not as a second claims source for page
  content the primary source didn't itself assert.
- reveal signal / status determination — rung 2 of the migration-mode status ladder (source
  session logs show actual play), beats the source's own `audience: dm` / `publish: false`
  frontmatter (which would otherwise read as rung-3 pending, matching the pattern that kept
  `sentinels-of-the-eyrie.md` and `vethka.md` on `canon` despite similar source frontmatter).
  Evidence: `sessions/session-02.md:29` and `sessions/session-02-recap.md:62` (crew-assembled
  roster listing); `sessions/session-02-scene-03-grigori.md:49` (played scene, physical
  description matches this page's Overview almost verbatim); `sessions/session-02-scene-04-
  ship-exploration.md:64,106,202` (full recruitment scene — the Surgeon's Berth negotiation this
  page's own Recruitment section describes, played at the table); `sessions/session-03-scene-02-
  the-shark.md:69` (stabilizes a downed PC in a live combat scene); `sessions/session-03-scene-04-
  five-days.md:108-152` (downtime scene: field medicine, herbalism, and the Crown-frigate
  backstory beat, all played). Landed `status: canon`.
- No CONTRADICTION found — first landing of this NPC and of the HCS Surety/Barnaby Rook/Shepherd
  Grigori names in `world/`; nothing to reconcile against.
