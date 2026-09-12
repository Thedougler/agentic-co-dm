# Queue: session-05-full-sweep

Source: ~/ai-os/shattered-sea, everything markdown relevant to session 5 | Gate: MIGRATION-LEDGER.md Round 25 (new-source mode override — see Verdict)
Mode: new-source (the DM directed this content be brought into the campaign as usable prep, not migration-mode disposal)
Started: 2026-07-14

User, verbatim, after the first session-5 sweep triaged the run-guide as refused-not-landed:
"Ingest EVERYTHING like i asked, you don't get to decide what is valuable." Re-scoped:
"just the markdown files" (images/PDF out of scope for this pass).

## Verdict

The run-guide's own content (scene menu, room keys, climax fight, tables) had never been
landed anywhere in campaign-os — only "refused as canon" per the R4 planned-runguide
precedent (correct for *canon*, wrong to read as "nothing to ingest"). Landed in full at
`prep/backlog/session-05-run-guide.md`, `type: encounter`, `status: pending`, new-source
mode (source-ingest's migration-mode has no prep/ path; this is exactly the ordinary case
new-source mode owns).

Every other session-5 markdown file was individually diffed (not assumed) against its
wiki/ counterpart and campaign-os's already-landed pages — see Sources below.

## Sources (all .raw/sessions/session-05/ + wiki/sessions/session-05-run-guide.md)

- [x] wiki/sessions/session-05-run-guide.md — landed in full, see Verdict above
- [x] .raw/sessions/session-05/printshop-packet/docs/core/01-session-05-run-guide.md — stale
  pre-recalibration draft of the same run-guide (824 vs 859 lines; Otar still CR 8, not the
  CR 12 rebuild). Superseded by the wiki copy just landed. No unique facts.
- [x] .raw/…/docs/core/02-calveno-sewers-grung-magazines.md — stale draft of the dungeon page
  (556 vs 704 lines); dungeon page already fully landed at
  world/locations/calveno-sewers-grung-magazines.md across multiple prior rounds. No unique facts.
- [x] .raw/…/docs/core/03-calveno-beffa-grung-raid.md — near-identical to wiki twin (only
  wikilink-path-prefix cosmetics differ); already absorbed into world/factions/grung-clans.md
  Front + the dungeon page (ff8e8f5). No unique facts.
- [x] .raw/…/docs/core/source-manifest.md, .raw/…/docs/core/PRINTSHOP-MANIFEST.md,
  .raw/sessions/session-05/source-manifest.md — packaging/print metadata, not wiki content;
  the "no audio or transcripts recorded yet" line was already cited as corroborating evidence
  in Round 24.
- [x] .raw/…/docs/encounters-and-statblocks/anzolo.md, enzo.md, felix-aho.md, master-kyzil.md,
  nona-black-jaw.md, ruk.md — byte-identical to their landed wiki/world twins. No unique facts.
- [x] .raw/…/docs/encounters-and-statblocks/grung-elite-warrior.md, grung-npc.md — differ from
  wiki only by wikilink-path-prefix cosmetics; both already landed
  (world/creatures/grung-elite-warrior.md; grung-npc itself was never landed as its own page —
  flagged in the new run-guide page's relink list, not created here, out of this line's scope).
- [x] .raw/…/docs/encounters-and-statblocks/otar-the-foul.md — stale pre-recalibration draft
  (CR 8, AC 15, HP 152); world/npcs/otar-the-foul.md already reflects the CR 12 recalibration
  from the newer wiki copy. Verified directly — no gap.
- [x] .raw/…/docs/encounters-and-statblocks/ruma-delacroix.md — stale pre-ally-turn draft
  (still "quartermaster," not yet captured/turned); world/npcs/ruma-delacroix.md already
  carries the full session-05 ally-turn content from the newer wiki copy. Verified directly —
  no gap.
- [x] .raw/…/docs/encounters-and-statblocks/solange-barret.md — wikilink-path cosmetics only;
  already landed at world/npcs/solange-barret.md.
- [x] .raw/…/docs/supporting-context/calveno-jean-claude-beats.md, calveno-palio-dm.md,
  calveno-raid-signs.md, calveno-sandbox-run-guide.md, calveno-situation.md,
  calveno-street-encounters.md — byte-identical to their wiki twins (all already landed or
  already flagged draft-tier per session-06-export's prior blanket check).
- [x] .raw/…/docs/supporting-context/warren-grung-sewers.md — wikilink-path cosmetics only vs
  wiki twin; already landed at world/narrative-islands equivalent content
  (world/locations/warren.md + dungeon page, per R11's calveno-beffa-grung-raid.md absorption).

## Claims

- [x] encounter :: session-05-run-guide :: prep/backlog/session-05-run-guide.md (new) — full
  scene menu, room reference, climax 3-phase boss fight, secrets/clues, stall hooks,
  cliffhangers — new-source mode, status: pending

## Flags

- relink: grung-npc — the base "green-caste sentry" creature stat block has never been landed
  as its own world/creatures/ page (only the lore/grung.md species page and the elite-warrior
  creature exist). Flagged on the new run-guide page; not created here (a new creature page is
  a bigger, separate claim than "ingest the run-guide").
- relink: purple-caste-enforcer, purple-caste-zealot, ozvok-the-vermillion-distiller — same
  situation: named monsters referenced throughout session-05/06 dungeon content, never landed
  as their own creature pages. Flagged on the new run-guide page for a future creature-ingest
  round.
- Battlemap images (`.raw/`, `wiki/assets/`, `tmp/`, `ui/dist/`) and `session-05-run-guide.pdf`
  explicitly out of scope for this pass (user: "just the markdown files").
