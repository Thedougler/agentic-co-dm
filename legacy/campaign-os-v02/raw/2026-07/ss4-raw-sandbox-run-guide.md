# Source ingest queue: ss4-raw-sandbox-run-guide

Source root: /Users/nick/ai-os/shattered-sea/notebooklm-export/2026-06-14/calveno-sandbox-run-guide.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md:98 — `raw ::
notebooklm-export/2026-06-14/calveno-sandbox-run-guide.md → triage per
claim-buckets — out-of-wiki source shape (notebooklm schema); run-guide-class
content likely maps/refuses; agent judges honestly`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:84 "REVIEWED-BY-HUMAN:
2026-07-13 — user instructions: 'at least 5 rounds of iterative improvements'
... 'Blessing covers exactly the 11 lines below.'" Line 98 is one of the 11.
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] notebooklm-export/2026-06-14/calveno-sandbox-run-guide.md — triage:
  `narrative-island` / `sandbox-run-guide` (own frontmatter: `type:
  narrative-island`, `subtype: sandbox-run-guide`) — a DM-facing prep
  operating document (Strong Start, Toy Fields, 5 Rides, Scene Spine, Scene
  Menu, NPC Bench, Secrets & Clues, Clocks, Agency Guardrails), **not** a
  session record (prospective "how to run this," not retrospective "what
  happened") — read in full, 311 lines, **refuses as a document; blocked as
  claim decomposition** (see Flags)

## Claims — notebooklm-export/2026-06-14/calveno-sandbox-run-guide.md

- none written. Per Flags below, this document's own type has no wiki
  skeleton and no ledger-authorized destination; its embedded entity claims
  are blocked pending ledger lines this dispatch does not carry.

## Flags

1. **Document-level verdict: maps, doesn't duplicate — refuses as a page.**
   No skeleton type in `wiki-contract.md`'s 8 types covers
   `narrative-island`/`sandbox-run-guide`. The function this document serves
   — a single DM-facing operating guide assembling entities + scenes for a
   specific upcoming stretch of play — is exactly what the `session-run-guide`
   skill already owns (`.claude/skills/session-run-guide/SKILL.md`): it builds
   `prep/next-session/run-guide.md`, singular fixed filename, freshly
   assembled from **live wiki state** each time (Hard Rule 5: "grep, never
   memory of a state file"), never migrated wholesale from an old export.
   Migrating this file verbatim as a wiki page would create a second,
   competing, stale operating-guide artifact outside that skill's one-file
   contract. `claim-buckets.md`'s own "island" row agrees: "the cluster
   itself is never a page."

2. **Direct precedent: `archive/2026-07/ss-island-port-tidefall.md`
   (same round-4 predecessor, same failure shape).** That queue file worked
   the identical question for `port-tidefall-dockfront.md` and reached the
   same U8-grounded conclusion (`scene-cards.md` § "Scene groupings": a
   grouping is "a shared Thread Name across scene cards... never a standalone
   artifact") plus the same owned-paths block (decomposition onto owning
   entities requires pages this ledger line doesn't name). This file is an
   even cleaner instance — its own frontmatter self-labels `subtype:
   sandbox-run-guide`, removing the ambiguity port-tidefall's bare
   `narrative-island` type had.

3. **Claim-level: stub-checked every named entity — almost nothing has an
   owning page yet, and none are named on this ledger line.**

   ```bash
   grep -ril "<name>" world/ pcs/ prep/ world/_meta/aliases.md
   ```

   `NONE` for: nona-black-jaw, savia-brentino, batta-zusto, giacomo-moretti,
   master-kyzil, cobb, oleandro-fuschi, marta-orsini, prospero-morsani,
   catarina-davirelli, ettore, il-gioco-delle-beffe, simone-tabarnack,
   la-vasca, acqua-nera, carpenters-slip, moretti-and-sons, casa-lupo,
   studio-orsini, cabinet-of-morsani, kats-curios, waveservant-shrine, vestra,
   calveno-districts, calveno-street-encounters, calveno-raid-signs,
   calveno-improv, calveno-beffa-grung-raid, surety-missing, warren (as its
   own page — the string only hits incidentally inside other pages' prose).
   One entity, **Ferrin Locke, already has a page** —
   `world/npcs/ferrin-locke.md` (status: pending, `%%src: legacy%%`,
   migrated via a different, more specific source per
   `archive/2026-07/ss2-npc-ferrin-locke.md`) — and it already carries
   `relink pending: warren-ferrin-locke` for exactly the thread this run
   guide's "Ferrin Locke" island names. This run guide adds no fact to that
   page the more specific source didn't already establish (handler Petra
   Venn, family leverage in Le Paludi), and `world/npcs/ferrin-locke.md` is
   not named on this ledger line, so it is not this dispatch's to edit.
   Originating any of the missing pages (Nona Black-Jaw, the Warren, Savia
   Brentino, the six shop/NPC pairs, etc.) would exceed migration mode's
   owned-paths restriction — "only the specific file(s) named on the ledger
   line being executed" (`source-ingest` SKILL.md § Owned paths). Line 98
   names only the source file itself, with disposition "triage," not a
   destination.

4. **The underlying facts are canon-shaped, but this document is not their
   citable source — a corroborating session record is, and that's a
   different file/skill's job.** `/Users/nick/ai-os/shattered-sea/
   notebooklm-export/2026-06-03/session-03-recap.md:99-226` confirms Calveno,
   La Vasca, Cobb, and Nona Black-Jaw were actually played (Perrin's Warren
   reunion, the Vestra-debt beat this run guide forecasts as a
   "complication" happens near-verbatim in the recap). That recap is a
   `session-record`-typed source (Hard Rule 5) belonging to
   `transcript-ingest`/a future ledger line, not this skill — migration
   status determination for these entities, when their pages are eventually
   created, should cite the recap (rung 2: "Source session logs... show the
   entity in actual play"), never this prospective run guide (rung 1 territory
   — pre-play framing throughout: "she will not take a cold approach," "the
   job is 220gp," conditional "if he acts").

5. **Verdict: nothing written, consistent with the port-tidefall precedent.**
   Recommends to the DM/orchestrator: (i) a future round dispatches
   `location :: Nona Black-Jaw's Table / the Warren`, `npc :: Nona
   Black-Jaw`, `npc :: Savia Brentino`, etc. as their own ledger lines,
   sourced from the session-03/04 recaps (canon, played) rather than this
   run guide (prep, unplayed-as-written) — this run guide can then serve as
   *reference color* for those pages' DM Only sections, cited
   `%%src: legacy%%` alongside the recap; or (ii) leave this source
   unmigrated permanently once `session-run-guide` exists as the live
   mechanism — a future PREP cycle for Calveno-adjacent play authors its own
   scene cards fresh, using this file only as background reading, never a
   relocation target (U8's own rule, restated in Flag 1 above).

6. **Reciprocal-link deferral N/A.** No page was written, so there are no
   `relink:` flags to carry. Entity names above stay plain text in this
   queue file only.

7. **No lint run.** No file under `world/`/`pcs/`/`prep/` was created or
   modified.

8. **Triage-table gap, 2nd instance (fix-on-discovery candidate, not this
   agent's file to edit).** `claim-buckets.md` § Source types (the initial
   triage table) has no row naming `narrative-island`/`sandbox-run-guide`
   directly — an agent triaging by that table alone only discovers the
   "island" bucket several sections later, under § Claim buckets, after
   already guessing `entity-source`/`quest-source` from the many named NPCs.
   `ss-island-port-tidefall.md` Flag 2 already NOTED that the island row
   itself is stale (predates the U8 resolution in `scene-cards.md`, points at
   a "location-tree" answer U8 later overrode). This file hits the identical
   staleness a second time. Both fixes are shared-skill-reference edits
   outside a single-file migration dispatch's owned paths (same restraint
   `ss-island-port-tidefall.md` exercised) — flagged for the
   orchestrator/DM, not applied here.
