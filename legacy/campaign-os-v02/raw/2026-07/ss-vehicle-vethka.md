# Source ingest queue: ss-vehicle-vethka

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/vehicles/vethka.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — `vehicle ::
entities/vehicles/vethka.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:11 "REVIEWED-BY-HUMAN:
2026-07-13 — per the user's handoff mission (procedure item 4 verbatim):
'Migration-mode canon writes are the sanctioned bootstrap-and-audit exception
(progress.md REVIEW item 17) — pending user blessing was the old status; the
user's current instruction to ingest legacy canon IS that blessing for this
mission's scope.' Blessing covers exactly the 15 lines below, nothing else."
Started: 2026-07-13

TRIAGE-ONLY DISPATCH (original, superseded below): this agent's mandate
(ledger line 31, "GAP BY DESIGN — ship type was deferred pending a real
vessel request; this ingestion is that trigger; agent stops BLOCKED,
orchestrator patches") was originally scoped as a spec proposal only, not a
page write. The un-defer spec below was accepted verbatim by the orchestrator
(the `ship` type now exists — commit `ed63957` — with skeleton
`docs/campaign/skeletons/ship.md` and its type-key-enum and skeleton-heading
entries registered for the new type). This re-dispatch (WRITE PASS, 2026-07-13)
executes the actual page write against that now-existing spec.

## WRITE PASS — 2026-07-13

- [x] `world/ships/vethka.md` written from `docs/campaign/skeletons/ship.md`
  (copied, not retyped). `ship_class: war proa`, `tier: 1`, `home_port: ""`
  (source states none — correctly left unset, not guessed). Body: read-aloud
  - Overview → Player-Known; the source's lone `[!dm]` Tactical Profile
  callout → DM Only; Stats table verbatim → Stats & Combat; caste/crew
  breakdown → Crew; Connections (Grung Clans, Verdant Teeth, both plain text
  — neither page exists yet) + revealed-ness disposition evidence →
  Appearances (see Friction below — the skeleton has no dedicated
  Connections/Relationships heading, so Connections was folded into
  Appearances per this file's own earlier spec-proposal mapping, line
  "Connections → Appearances").
- [x] Status: `canon`, not `pending`. Source's own frontmatter (`status:
  active`, `audience: players`, `publish: true`, `confidence_level:
  confirmed`) carries no "not yet encountered" caveat (unlike
  `world/npcs/estratto.md`, which does and landed `pending`). Corroborated
  from the source repo's session material: `sessions/session-04-day-5.md`
  narrates the party directly sighting the *vethka* extraction fleet;
  `sessions/session-04.md` (the wrapping session note) is `status: complete`;
  `sessions/session-05-run-guide.md` and `sessions/session-06-run-guide.md`
  (dated `session_date: 2026-07-02`) both carry "pursuit of the *vethka*"
  forward as an already-established hook, not a hypothetical.
- [x] Tags: `[war, heist]` — nearest canonical Domain tags
  (`world/_meta/tags.md`) for a raiding vessel used in a slaving-extraction
  raid; the source's own `tags: [grung]` isn't a Domain tag (same taxonomy
  gap already flagged in Flags item 3 below and on the parallel `species ::
  grung` ledger line — not re-litigated here).
- [x] Lint: zero unresolved blocks (first pass caught `tier: "1"` — YAML-quoted
  string vs. the enum's bare-int comparison; fixed to `tier: 1`, re-ran clean).

## Sources (batch order, smallest file first)

- [x] entities/vehicles/vethka.md — triage: entity-source, written (spec
  un-defer completed by orchestrator; this dispatch executed the page write)

## Claims — entities/vehicles/vethka.md

- [x] ship :: Vethka :: world/ships/vethka.md (new) — full ship identity:
  Grung Tier 1 war proa, read-aloud description, caste breakdown (blue-caste
  navigate, purple-caste raid, orange-caste build, red-caste poison bench),
  hull/stat block (Tier 1, HP 70, AC 11, Excellent maneuverability, Very Low
  profile, Crew 2/12, Cargo 2 tons), tactical profile (reef-country ambush
  doctrine) (%%src: legacy%%) — WRITTEN, lint clean
- [x] relationship fact :: "Vethka hull is single-piece Verdant Teeth
  ironpillar hardwood, adze-worked by Grung Clans orange-caste artisans" —
  stub check (`grep -ril "grung.clans\|verdant.teeth" world/ pcs/ prep/`) still
  finds no dedicated `world/factions/grung-clans.md` or `world/locations/
  verdant-teeth.md` page (re-checked at write time — unchanged since the
  original triage dispatch). Written as plain text under Appearances >
  Connections on `world/ships/vethka.md`, with `relink: grung-clans — once
  its faction page lands` and `relink: verdant-teeth — once its location page
  lands` carried forward as flags (below).

## Un-defer spec proposal

**Recommendation: add a `ship` type (not `vehicle`) — minimal, single-file
shape for now; defer the multi-file companion pattern until a Tier-3 vessel
triggers it.**

### Why `ship`, not `vehicle`

Argued from the source corpus, not genre convention (all 30 files in
`entities/vehicles/`, sampled via frontmatter dump):

- The source's own `subtype` key is split almost evenly — 16 files use
  `subtype: ship`, 14 use `subtype: vehicle` — so the source itself doesn't
  settle this; it's not a signal either way.
- The one field nearly every detailed file *does* share is `ship_class`
  (25/30 files: "war proa", "Heavy Frigate", "cutter", "brigantine", "Ship of
  the Line"...) — never `vehicle_class`. That's the recurring governed-key
  candidate, and it's ship-named.
- 30/30 files in this directory are watercraft. Zero land or aerial vehicles
  exist in the source to justify a broader `vehicle` umbrella today — that
  would be speculating past what the corpus contains (Hard Rule 1). If a
  non-nautical vehicle is ever migrated, that becomes its own trigger for a
  broader/second type, same deferral discipline that produced this proposal.
- `travel-events/SKILL.md`'s own gap-flag language already leans this way:
  "no `ship` type... whoever eventually specs a `ship` (or vehicle) type"
  (line 3), and its craft-source citation names `docs/campaign/legacy-
  skills/prep-ship/` — a skill that called itself "ship" throughout despite
  filing to the `vehicles/` folder.
- campaign-os's existing `world/` layout is plural-of-`type`
  (`npcs/`, `locations/`, `factions/`, `items/`, `quests/`, `lore/`) — `type:
  ship` files to `world/ships/`, staying consistent with that pattern instead
  of introducing a folder name (`vehicles/`) that doesn't match any other
  type's naming.

### Frontmatter keys

Universal fields (`type`, `status`, `publish`, `aliases`, `created`,
`touched`, `tags`) apply unchanged. New type-specific keys, argued from what
the 30-file fleet actually populates, not invented ahead of it:

- `ship_class` (required, free text — **not** an enum). The fleet's values
  are genuinely open vocabulary (20+ distinct strings observed: "war proa",
  "reef runner (sloop)", "Ship of the Line", "cargo galleon"...) — matches
  how `item`'s type/material stays prose rather than a closed key (wiki-
  contract.md's item bullet explicitly reasons this way already).
- `tier` (optional, enum `1 | 2 | 3 | 4`) — add as a governed enum key. This
  one genuinely is closed: the archived `prep-ship/references/SHIP-RULES.md`
  § Ship Tiers defines exactly four tiers with a stated progression
  principle, and every fleet file that states a tier uses 1-4 (never 5+,
  never fractional). Optional because several fleet entries (the Fisk's
  Fleet ships: `heft.md`, `the-narrow.md`, `loud-argument.md`, `fernen.md`,
  `red-lady.md`'s sibling group; `ships-index.md`-only entries like `the-
  glass-debt`/`the-velvet-noose`) never state one.
- `home_port` (optional, free wikilink, unvalidated) — mirrors the existing
  `npc` type's optional `location` key exactly (wiki-contract.md's own
  reasoning: "a fact about the world... not a closed set of values, so it
  stays unvalidated the way wikilinks generally are"). Present on ~9/30 fleet
  ships (`greyteeth-runner`, `hcs-warrant`, `lasting-insult`, `saltwright`,
  `tessarine-amberreach`, `tessarine-silkvane`, `the-bad-receipt`, `the-
  quorum`, `uncertainty`). Vethka itself has none (a raiding vessel with no
  stated home port) — correctly left absent, not guessed.

**Explicitly NOT proposing** `hull_points`/`hull_ac`/`captain`/`owner`/
`current_location`/`banner`/`asking_price` as frontmatter keys, despite all
appearing somewhere in the fleet. Reasoning: campaign-os frontmatter is
deliberately minimal — only `pc` carries mechanical stats in frontmatter
(`hp_max`, `ac`), and wiki-contract.md's own stated reason is "so INGEST/
CANONIZE can update stats with a YAML edit instead of prose surgery." `npc`
— the closest sibling to a background ship — carries **zero** frontmatter
combat stats; HP/AC for NPCs live in the body's `Stats & Combat` heading,
exactly where `vethka.md`'s own source already puts its Tier/HP/AC/Crew/
Cargo table. A ship is `pc`-like (frontmatter mechanical stats, fast-update)
only when it's the *party's own, actively-tracked* vessel — and no such ship
is in this migration batch (the closest candidate, `hcs-surety`/
`uncertainty`, is Tier 1→refit and not on the ledger's 15 lines). Deciding
that split now would be inventing past this file's evidence; flagged below
for whoever migrates the party's actual ship to resolve.

### Skeleton headings

Propose `["Player-Known", "DM Only", "Stats & Combat", "Crew", "Appearances"]`
as the `ship` skeleton's heading set. This is `npc`'s exact 5-heading shape
(`Player-Known, DM Only, Stats & Combat, Relationships, Appearances`) with
only `Relationships` → `Crew`, because a ship's durable relationships in this
corpus are near-universally crew (captain, named crew, caste/role
breakdown) rather than the broader web an NPC page links (allies, rivals,
family). `vethka.md`'s own body already maps cleanly onto this: Overview +
read-aloud → Player-Known; caste/crew detail and the DM-only tactical callout
→ DM Only / Crew; the Stats table → Stats & Combat; Connections → Appearances
(once grung-clans/verdant-teeth pages exist to link).

### Schema patch (exact locations)

1. `.claude/skills/campaign-os/references/wiki-contract.md:12` — `type: npc |
   location | faction | quest | item | lore | pc | session | encounter` →
   append `| ship`.
2. Same file — add a new type-specific-keys bullet (after the existing `npc`
   bullet) documenting `ship_class`, `tier`, `home_port` per above.
3. New file needed, not an edit: `docs/campaign/skeletons/ship.md`, following
   the `item.md`/`npc.md` skeleton format (frontmatter block with the new
   keys defaulted, then the five `##` headings empty) — doesn't exist yet,
   must be authored when the un-defer executes.
4. `world/ships/` directory doesn't exist yet — created on first `ship` page
   write.

### Affected skills (report only — none edited by this dispatch)

- **`.claude/skills/travel-events/SKILL.md`** — the skill's own description
  line and body (lines 3, 22, 53, 91, 333-340) all assert "no `ship` type
  exists... a flagged gap, not this skill's job." Once `ship` lands, these
  need rewording — **not** to make travel-events author ship pages (it
  still explicitly hands off ship-entity authoring, by design), but to stop
  claiming the type doesn't exist and instead point at wherever ship pages
  now get authored (see next point).
- **`.claude/skills/campaign-os/references/skills-registry.md:138`** — the
  `travel-events` row's "Craft content preserved" cell reads "Ship-as-page-
  type stays a GAP (no `ship` type in wiki-contract) — flag, don't invent."
  Needs updating once the type lands. More significantly: **no skill in the
  registry currently owns ship-page authoring.** `travel-events` explicitly
  refuses it; the legacy `prep-ship` skill that could is archived at
  `docs/campaign/legacy-skills/prep-ship/SKILL.md` (Tier Model, Ship Page
  Structure, `references/SHIP-GENERATE.md`/`SHIP-RULES.md` all still there,
  unrefactored). A new `ship-prep` registry row, mining that archive the same
  way `travel-events` already mined its travel/navigation half, is the
  natural next step — but authoring a new skill is out of this gap-probe's
  scope; flagged, not built.

## Flags

1. **Frontmatter-stats question deferred, not decided.** Whether the party's
   own ship (once migrated — likely `hcs-surety`/`uncertainty`, not on this
   15-line ledger batch) needs `pc`-style frontmatter `hull_points`/`hull_ac`
   for fast mechanical updates is explicitly left open above. Resolve it when
   that file is actually migrated, not from this thin single-vessel sample.
2. **Tier-3 multi-file companion pattern not specced.** The source fleet's
   `hcs-surety` family (`hcs-surety.md` + `hcs-surety-dm-guide.md` +
   `hcs-surety-layout.md` + `hcs-surety-manifest.md` + `hcs-surety-owners-
   manual.md`) matches the archived `prep-ship` skill's "Tier 3 subfolder"
   structure exactly (`index.md`/`layout.md`/`manifest.md`/`owners-
   manual.md`/`dm-guide.md`) and has a real precedent in this system already
   — `location`'s settlement/district page-tree. `vethka.md` is Tier 1,
   single-file, no companions, so this dispatch doesn't need the answer.
   Flagged for whoever migrates a Tier 3 vessel to design (probably by
   analogy to `city-builder`'s settlement-tree pattern) rather than invented
   here ahead of that trigger.
3. **`grung` tag has no taxonomy home.** `vethka.md`'s `tags: [grung]` (and
   the wider fleet's `dravosi`, `maritime`, `tessarine`, `fisk-fleet`,
   `waveservants`, `rattkin` tags) don't map to any canonical Domain tag in
   `world/_meta/tags.md` (intrigue/heist/horror/mystery/exploration/war/
   politics/romance) nor is there a Project-arc tag yet (that section is
   empty at bootstrap). `tags.md` is human-owned (`%%GENERATED-BY-HUMANS —
   automated pipelines read, never write%%`) — this dispatch does not
   propose additions to it, only surfaces that any migrated fleet page will
   soft-flag W13 on its tags until the human either adds Project-arc tags or
   normalizes these as aliases. Unrelated to the ship-type gap itself;
   surfaced because it will otherwise surprise whoever executes the write.
4. **Claim 2's link targets (`grung-clans`, `verdant-teeth`) are themselves
   mid-migration by a parallel ledger-line agent** (species ::
   lore/species/grung.md, ledger line 30, still unchecked at time of this
   dispatch). Same plain-text deferral as `ss-deity-syranita.md` Flags 1-2 —
   not acted on here. **Still true at write-pass time (2026-07-13):** grepped
   again immediately before writing `world/ships/vethka.md` — no
   `world/factions/grung-clans.md` or `world/locations/verdant-teeth.md`
   exists yet, so both relink flags carry forward unresolved (the `## Appearances`
   › Connections bullet "Grung Clans — builders and operators..." stays
   plain text).

   **Link-restoration pass (2026-07-13):** `world/lore/grung.md` (the species
   page, a separate entity from the `grung-clans` faction above) landed. The
   three generic species-level "Grung" mentions in this page's prose (read-aloud
   box "Twelve Grung can crouch...", Player-Known "the Grung term for this
   class of vessel", DM Only "Grung Standing Leap means...") now link
   `[[grung|Grung]]`. The Connections bullet's "Grung Clans" (the faction)
   was left untouched — different entity, still no page.
5. **WRITE-PASS FRICTION — `ship` skeleton's `Appearances` heading is
   overloaded.** This queue file's own earlier spec proposal (§ Skeleton
   headings) mapped the source's "Connections" section to `Appearances`
   ("Connections → Appearances (once grung-clans/verdant-teeth pages exist to
   link)"), but the established sibling precedent for `Appearances` on other
   migrated pages (`world/npcs/estratto.md`, `world/factions/sentinels-of-
   the-eyrie.md`) uses that heading exclusively for session-appearance /
   revealed-ness evidence, not relationships — `npc`'s skeleton has a
   separate `Relationships` heading for that; `ship`'s skeleton dropped it in
   favor of `Crew` and never replaced it. `world/ships/vethka.md` resolves
   this by putting both sub-uses under one `## Appearances` heading with
   internal sub-labels ("Connections" / "Revealed-ness"), which reads a
   little cluttered on a single-relationship-pair page and will read worse
   on a fleet page with many named crew/owner/rival relationships (see the
   30-vessel-fleet friction note in the dispatch report). Flagged for whoever
   authors the `ship-prep` skill (§ Affected skills above) to decide: either
   restore a dedicated `Relationships`/`Connections` heading on the `ship`
   skeleton, or formally document the fold-in as intentional. Not resolved
   here — skeleton edits are out of a single-page write dispatch's scope.
