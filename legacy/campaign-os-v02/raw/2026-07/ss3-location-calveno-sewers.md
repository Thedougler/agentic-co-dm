# Source ingest queue: ss3-location-calveno-sewers

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/places/dungeons/calveno-sewers-grung-magazines.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — Round 3 —
`location-dungeon :: entities/places/dungeons/calveno-sewers-grung-magazines.md
→ world/locations/ — subtype: dungeon; child of canon [[calveno]] — real
parent link, no tree invention beyond the one file`)
Started: 2026-07-13

Gate proof (docs/campaign/MIGRATION-LEDGER.md):

```text
63:REVIEWED-BY-HUMAN: 2026-07-13 — same user instruction; blessing covers exactly the
64:14 lines below. R2 synthesis in force (e1c4185): status-precedence ladder, de-linkify
65:quoted evidence, SRD-gear never-link, type-confidence notation, tag tonal-evidence rule.
...
70:- [ ] location-dungeon :: entities/places/dungeons/calveno-sewers-grung-magazines.md → world/locations/ — subtype: dungeon; child of canon [[calveno]] — real parent link, no tree invention beyond the one file
```

## Sources (batch order, smallest file first)

- [x] entities/places/dungeons/calveno-sewers-grung-magazines.md — triage: location, ready

## Claims — entities/places/dungeons/calveno-sewers-grung-magazines.md

- [x] location-dungeon :: Calveno Sewer Magazines — Grung Raid Infrastructure ::
  world/locations/calveno-sewers-grung-magazines.md (new) — subtype: dungeon,
  status: pending (rung 3 of the status-determination ladder: source
  frontmatter `audience: dm`/`publish: false` — see Flags item 1 for why
  rung 2 was NOT used despite the source's own in-play claim). Player-Known
  (access points, ambient sensory conditions), DM Only (intel baseline,
  poison mechanics, topology, full 10-room key with dimensions/features/
  DCs/encounters, long-rest clock, Three Clue Audit, treasure summary,
  pacing/loud/stealthy/negotiate/fight-modifiers/escape/extraction-clock/
  safety-valve/drama-suite/box-of-doom, if-ignored consequence, map-asset
  note), Notable NPCs (13 named figures/guardians), Hooks (raid-plan and
  Warren-investigation cross-references, if-ignored pointer), Appearances
  (Session 05/06 claim left unconfirmed — no recap exists to corroborate).
  Parent link: real `[[calveno|Calveno]]` wikilink in the opening
  paragraph — calveno.md itself NOT edited (see reverse-relink flag
  below). (%%src: legacy%%)

## Flags

- **Status-determination ladder — rung conflict, resolved to rung 3.** The
  source's own text asserts actual play ("the party is resuming from Room
  6 after Session 05") and the battlemap filenames are labelled
  `session-05`, which looks like rung-2 evidence (source session logs
  show actual play). But per rule 10 and the ladder's own evidence bar
  ("cite the file:line"), I could not find an independent session-05 or
  session-06 *recap* in the source repo to corroborate it — only
  `session-05-run-guide.md` / `session-06-run-guide.md` (DM prep guides,
  not play logs) and `wiki/sessions/session-0{1,2,3}-recap.md` (recaps
  exist only through Session 03). `world/ships/vethka.md`'s own
  Revealed-ness note (already-ingested, Round 2 wave) cites
  `sessions/session-04-day-5.md status:complete` as real corroboration
  for a Session 4 claim — no equivalent file exists for Session 05/06.
  Absent that corroboration, rung 3 fired instead on the source's own
  frontmatter (`audience: dm`, `publish: false`) → `status: pending`.
  Re-run this determination once `sessions/session-02-recap.md` and any
  later session material are ingested (Round 3's own `session ::
  sessions/session-02-recap.md` line, and beyond).
- **Parent back-link — reverse-relink flag, not applied here.** `[[calveno|Calveno]]`
  is a real, live link from this page. The reverse direction —
  `world/locations/calveno.md`'s own Hooks section pointing back down to
  this dungeon — is calveno.md's file to edit, not this ledger line's
  (task instruction: do NOT edit calveno.md). Flagging for the link-
  restoration pass / a human decision on whether Calveno's page should
  surface its sewer-magazine dungeon in Hooks.
- **Tag mapping.** Source tags (`grung`, `combat`, `poison`, `dungeon`) are
  all either entity-identity or generic/mechanical — none are canonical
  domain tags (`intrigue, heist, horror, mystery, exploration, war,
  politics, romance`) and none have an alias — dropped by design per
  WIKI.md § Tag taxonomy. Mapped instead to two tags the page's own
  content genuinely carries: `heist` (multi-site infiltrate/disarm-before-
  detonation structure with explicit stealth/negotiate/loud branches) and
  `exploration` (room-by-room dungeon-crawl structure). Not a general
  rename rule — logged per-file as required.
- **26 entities the source wikilinks but this repo has no page for yet** —
  written as plain text per migration-mode link deferral, no stubs
  created:
  - relink: simone-tabarnack — once its page lands
  - relinked ✓ — jean-claude-tabarnack — `pcs/jean-claude-tabarnack.md` landed
    (canon); the "Jean-Claude Tabarnack" NPC entry and both short-form
    "Jean-Claude" mentions now link `[[jean-claude-tabarnack|Jean-Claude]]`
    (link-restoration pass R4, 2026-07-14)
  - relink: nona-black-jaw — once its page lands
  - relinked ✓ — perrin-black-jaw — `pcs/perrin-black-jaw.md` landed (canon);
    the "Perrin Black-Jaw" NPC entry and the Hooks mention now link
    `[[perrin-black-jaw|Perrin Black-Jaw]]` (link-restoration pass R4, 2026-07-14)
  - relink: felix-aho — once its page lands
  - relink: catarina-davirelli — once its page lands
  - relink: master-kyzil — once its page lands
  - relink: solange-barret — once its page lands
  - relink: bazzoth-the-steeped — once its page lands
  - relink: vashu-the-weeping-veil — once its page lands
  - relink: ozzeth-the-twiceborn — once its page lands
  - relink: ozvok-the-vermillion-distiller — once its page lands
  - relink: purple-caste-enforcer — once its page lands
  - relink: purple-caste-zealot — once its page lands
  - relink: grung-elite-warrior — once its page lands
  - relink: grung-npc — once its page lands
  - relink: grung-wildling — once its page lands
  - relink: grung-clans — once its page lands
  - relink: otar-the-foul — once its page lands
  - relink: warren — once its page lands
  - relink: warren-grung-sewers — once its page lands
  - relink: le-paludi — once its page lands
  - relinked ✓ — la-vasca — real slug is `world/locations/calveno-la-vasca.md`
    (canon), not `la-vasca` — see MIGRATION-LEDGER.md R4 mission note. Both
    "La Vasca" mentions (Player-Known tidal-passage prose, Topology Route D)
    now link `[[calveno-la-vasca|La Vasca]]` (link-restoration pass R4, 2026-07-14)
  - relink: il-gioco-delle-beffe — once its page lands
  - relink: calveno-beffa-grung-raid — once its page lands
  - relink: session-06-run-guide — once its page lands
- **Real wikilinks used (2 of the 20-page allow-list matched the source's
  actual content):** `[[calveno|Calveno]]` (parent, real link, page
  NOT edited) and `[[grung|Grung]]` (species page, linked once on first
  mention in the opening paragraph — the term recurs dozens of times
  through the room key, so every other mention stays plain text "Grung"
  per normal single-link-per-page convention, matching how other migrated
  pages e.g. `world/ships/vethka.md` link `[[grung|Grung]]` once and
  leave later mentions plain). `vethka` does not appear anywhere in this
  specific source file (checked, zero hits) so no link opportunity
  existed despite being on the allow-list.
- **SRD-adjacent gear never linked**, per rail 4: Globe of Invulnerability
  scroll, handler crossbows/bolts, alchemist's-fire debris, torch racks —
  all left as plain text, no link targets, no relink flags (generic
  mechanics, not campaign entities).
- **Map assets not transferred.** The source cites 11 canonical battlemap
  PNGs plus a printshop packet archive under `wiki/assets/sessions/
  session-05/maps/` and `.raw/sessions/session-05/`. Out of this skill's
  owned paths (asset embedding is `battlemap-render`/`visual-aids`
  territory) — noted in the page's own DM Only § Map assets and here, not
  actioned.
