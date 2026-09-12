# Source ingest queue: ss2-faction-waveservants

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/factions/waveservants.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md:50 —
`faction :: entities/factions/waveservants.md → restructure → world/factions/`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:41 "REVIEWED-BY-HUMAN:
2026-07-13 — user instruction 'implement all your recommended fixes, then proceed
to round two'. Blessing covers exactly the 13 lines below." Line 50 (waveservants)
is one of those 13.
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/factions/waveservants.md — triage: entity-source, ready

## Claims — entities/factions/waveservants.md

- [x] faction :: Waveservants :: world/factions/waveservants.md (new) — clergy
  identity, shrine practice, other-power relationships, current-table-state note,
  no invented Front clock (%%src: legacy%%)

## Flags

1. **`status: canon` — signal that decided it, independently verified per the
   sentinels-of-the-eyrie precedent (not taken on faith from the ledger line,
   which states no disposition for this row at all — unlike the npc/deity rows
   that spell out `status:`).** Evidence, all in the source repo (read for
   reveal-signal purposes only, not as content source for this page — Hard Rule
   1 keeps the page's own claims scoped to `entities/factions/waveservants.md`):
   - `player-primer.md` lines 33, 77, 133, 141, 155 name "the Waveservants" and
     Umberlee's tribute-collection custom as established, player-facing setting
     knowledge (session-zero handout material, same evidentiary class as the
     sentinels precedent's primer citation).
   - The source repo carries a dedicated player-facing page,
     `lore/umberlee-and-waveservants.md`, with `audience: players`,
     `publish: true` — stronger reveal signal than sentinels had (no equivalent
     standalone player page existed for that faction).
   - `sessions/session-04-day-3.md:218` puts Branca and the Waveservant Shrine
     into actual at-the-table play state ("Branca has been in the shrine for
     four dawns... a rumor... has reached Ponte Bassa"), corroborating the
     source page's own "Current Table State" section as real session content,
     not unrevealed DM prep.
   `status: canon` stands.

2. **Front clock — Hard Rule 4.** Source states an agenda (collect tribute,
   witness maritime obligations, operate harbor shrines, refuse almost no one)
   but no segments/trigger/consequence-at-fill anywhere. Written as identity/
   agenda prose in `## Goals & Fronts` only, explicitly not a Front. Flagged for
   `faction-prep` if the DM wants this mechanized.

3. **Members — conservative read, corroborating context flagged not asserted.**
   The source file's own "Current Table State" section places
   [[branca|Branca]] at the Waveservant Shrine but does not itself state her
   role or faction membership in that file's text. The source repo's separate
   NPC file `entities/characters/npcs/branca.md` (out of this ledger line's
   scope — not one of Round 2's 13 lines) independently identifies her as
   "Senior Waveservant" — cited here only as corroborating context for a future
   npc-ingest wave, never asserted as this page's own sourced claim (Hard Rule
   1: fidelity to *this* source file only). No formal membership roster is
   otherwise stated.

4. **Unresolved wikilinks — plain text + `relink:` flags, no stub pages
   created (migration-mode link deferral).** Entities the source names that
   have no `world/`/`pcs/` page yet:
   - `umberlee` (deity) — `relink: umberlee — once its page lands`
   - `dravosi-crown` (faction) — `relink: dravosi-crown — once its page lands`
   - `tessarine-concordat` (faction) — `relink: tessarine-concordat — once its page lands`
   - `the-drowned-maw` (location) — `relink: the-drowned-maw — once its page lands`
   - `the-passage` (faction/org) — `relink: the-passage — once its page lands`
   - `branca` (npc) — `relink: branca — once its page lands`
   - `delmar-fisk` — resolved ✓ (link-pass R6, 2026-07-14): `pcs/delmar-fisk.md`
     landed (canon, R5); the `## DM Only` "for Delmar Fisk" mention now links
     `[[delmar-fisk|Delmar Fisk]]`.
   - `waveservant-shrine` (location) — `relink: waveservant-shrine — once its page lands`
   - `vel-orn` (location) — `relink: vel-orn — once its page lands`
   - `umberlee-and-waveservants` (player-facing lore page) — `relink: umberlee-and-waveservants — once its page lands`

5. **Real wikilinks used (both on the 10-page confirmed-exist list AND named
   in the source text):**
   - [[sentinels-of-the-eyrie|Sentinels of the Eyrie]] — source states "The
     Sentinels of the Eyrie established their monastic tradition to counter
     them."
   - [[calveno|Calveno]] — source's Current Table State places the Waveservant
     Shrine in Calveno.
   Of the other 8 pages the orchestrator confirmed exist (estratto,
   preserved-eel, campaign-overview, grung, syranita, gentle-hag, swashbuckler,
   vethka), none are named anywhere in this source file's text — no link
   written for them (a same-title-list page isn't a citation).

6. **Reverse-relink — resolved ✓ (link-pass R4, 2026-07-14).**
   `world/factions/sentinels-of-the-eyrie.md` line 14's "Waveservants of
   Umberlee" now links `[[waveservants|Waveservants]]`.

7. **Tags — both source tags dropped, none substituted.** Source frontmatter
   tags were `umberlee`, `waveservants` — both entity-identity tags (a deity
   name and this very faction's own name) per WIKI.md § Tag taxonomy's
   "Migrated legacy tags" rule: DROPPED BY DESIGN, not mapped, the relationship
   belongs in prose/wikilinks instead. No genuine Domain-tone tag
   (intrigue/heist/horror/mystery/exploration/war/politics/romance) fits this
   content without force-fitting — tribute collection and shrine neutrality
   isn't intrinsically any one of the 8 canonical tones the way sentinels'
   "unexplained-phenomenon record-keeping" mapped cleanly to
   mystery/exploration. Tags left empty (`tags: []`) rather than stretched;
   logged here per the taxonomy rule's "log each mapping in the ingest queue
   file" instruction — this is a logged non-mapping, not a silent drop.

8. **Frontmatter fields with no contract home.** Source frontmatter carried
   `campaign`, `audience`, `confidence_level`, `sources:` — none governed
   faction keys in wiki-contract.md. Dropped, same as the sentinels precedent.

9. **`created`/`touched: legacy`.** Same placeholder as prior migration-mode
   pages — `wiki-contract.md` only defines `sNN`/`prep`; `legacy` is the
   sanctioned closest-fidelity value (MIGRATION-LEDGER.md round-1 friction F4).
