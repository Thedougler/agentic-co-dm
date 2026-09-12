# Source ingest queue: ss4-pc-jean-claude

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/characters/pcs/jean-claude-tabarnack.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md:99 — `pc :: entities/characters/pcs/jean-claude-tabarnack.md → pcs/jean-claude-tabarnack.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:84-89 "REVIEWED-BY-HUMAN: 2026-07-13 — user instructions: 'at least 5 rounds of iterative improvements'... 'The PC lines below are the canon-review signature PC creation requires — the user explicitly directed PC-file ingestion. Blessing covers exactly the 11 lines below.'"
This supersedes the R1 hand-off refusal at archive/2026-07/ss-pc-jean-claude.md (ledger:24, commit 501f387) — that refusal was correct under R1's gate (disposition `ask`, no canon-review signature); R4's ledger line is a distinct, later-dated signature naming the exact `pcs/` path, per DISPATCH.md's line-specific override.
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/characters/pcs/jean-claude-tabarnack.md — triage: pc (PC-path-live per R4 ledger override, not character-sheet hand-off), ready

## Claims — entities/characters/pcs/jean-claude-tabarnack.md

- [x] pc :: Jean-Claude Tabarnack :: pcs/jean-claude-tabarnack.md (new) — full PC page from pc skeleton, status canon (canon-by-nature, PC pages) (%%src: legacy%%)

## Flags

1. **Governed keys — source coverage.** wiki-contract.md pc row requires `player`,
   `class_levels`, `hp_max`, `ac`, `inventory:`. Source has: `class_levels` (Gloom
   Stalker Ranger 4, stated directly under `## Mechanics`). Source does NOT state:
   `player` (no real-world player name anywhere — frontmatter/body only ever names
   the character), `hp_max`, `ac` (no numeric stat given at all — `## Mechanics` is
   narrative-mechanical, not a stat block). `inventory:` partially inferable from
   prose (Corto di Velo, red beret, false moustache, worn ranger harness, +1 silent
   shortbow, twenty vials of Simone's tincture) but no source line frames these as a
   formal inventory list — filled as a best-effort list citing the prose, each item
   plain text (no target pages exist).
2. **Deferred links.** simone-tabarnack, pell, corto-di-velo,
   truth-stone, silent-shortbow, boots-of-flying, casa-lupo, studio-orsini,
   master-kyzil, felix-aho, sem-holst, grigori, beaumont,
   the-canister, whip-shark-eggs, flask-of-endless-water, verdant-teeth, midchain,
   sorn — still no target page, plain text. `[[grung]]` was already a real link.
   **Resolved ✓ (link-pass R6, 2026-07-14):** perrin-black-jaw, delmar-fisk,
   crissdalynn-khinriss (Party line), grung-clans (Long-term line), nona-black-jaw
   (Session 04 "Nona's request") all now link on-page. gloom-stalker/ranger/
   hermit stay collapsed SRD/subclass-descriptor prose, not entity links.
3. **CANONIZE stat-pipeline gap.** This source predates the campaign-os stat
   pipeline entirely (wiki-contract.md § PC pages and the stat pipeline: STAT
   ledger lines need a quoted transcript line as evidence). The source gives no
   `hp_max`/`ac`/`player` at all — a future CANONIZE pass cannot backfill these
   from *this* source; it needs either a fresh table-side character-sheet capture
   (dnd5e-character-interview) or a STAT ledger line quoting an actual campaign-os
   session transcript once one exists. Flagging this as the concrete answer to
   the dispatch's closing question.
4. **Status rung.** Rung 2 of the migration-mode status ladder (source-repo
   evidence of actual play) — sessions/01-boarding-of-the-saltwright/state-changes.md:30
   and sessions/02-conflict-is-a-surety/state-changes.md:34 both carry unapplied
   NEW lines for this exact page citing transcript quotes ("The toxin was Simone's.
   Unmistakably hers... He said nothing." / "Jean-Claude filled a wine glass with
   his own blood."). Beats source frontmatter's own `audience: dm`/`publish: false`
   (rung 3 would have said pending — rung 2 fires first and wins).
5. **Tag drop.** Source frontmatter carries `tags: [grung]` — identity/origin tag,
   dropped by design per WIKI.md § Tag taxonomy (names `grung` itself as the
   worked example of a species-identity tag to drop, not map). No canonical
   domain tag (intrigue/heist/horror/mystery/exploration/war/politics/romance)
   fits the page's own tonal content cleanly enough to force one — landed at
   `tags: []`, which the taxonomy names as always legal.
