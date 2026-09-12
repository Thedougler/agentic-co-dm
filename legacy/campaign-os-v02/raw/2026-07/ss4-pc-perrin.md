# Source ingest queue: ss4-pc-perrin

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/characters/pcs/perrin-black-jaw.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md:100 —
`pc :: entities/characters/pcs/perrin-black-jaw.md → pcs/perrin-black-jaw.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:84-89 "REVIEWED-BY-HUMAN:
2026-07-13 — user instructions: \"at least 5 rounds of iterative improvements\"...
\"and also the player character related files\". The PC lines below are the
canon-review signature PC creation requires — the user explicitly directed PC-file
ingestion. Blessing covers exactly the 11 lines below." Line 100 is one of the 11.
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/characters/pcs/perrin-black-jaw.md — triage: PC identity/narrative
  profile (Foundation/Beliefs/Pressure/Carries/Party/Threads/Combat/Session Events;
  no `## Mechanics` stat block, unlike jean-claude-tabarnack.md's sheet shape) —
  ready under R4's explicit PC-path authorization (see Flags #1 for the
  jean-claude-line divergence this created).
- [ ] entities/characters/pcs/perrin-black-jaw-sheet.pdf — triage: character-sheet
  (PDF) — skipped, no PDF tooling by design (ledger line's own text). No hand-off
  invoked; stats it would complete live as stub notes on the written page.
- [ ] dm/perrin-primer.md — triage: PC-tactical/DM-primer — NOT folded, per ledger
  line's explicit carve-out ("dm/perrin-primer.md content remains flagged for Arc
  Notes (separate decision)"). Already triaged in full by the R2 refusal at
  archive/2026-07/ss2-dm-perrin-primer.md — this line just re-confirms that
  triage stands and the content is NOT pulled into Arc Notes this round.

## Claims — entities/characters/pcs/perrin-black-jaw.md

- [x] pc :: Perrin Black-Jaw :: pcs/perrin-black-jaw.md (new) — full PC page,
  governed keys (player, class_levels, inventory) filled from source; hp_max/ac
  stubbed (source states neither); status canon, rung 2 (in-play evidence, cited
  below) (%%src: legacy%%)

## Flags

1. **Jean-claude-line divergence (parallel sibling under the same R4 PC-path
   authorization).** `archive/2026-07/ss-pc-jean-claude.md` (the parallel
   dispatch for ledger line 99, same Round 4, same REVIEWED-BY-HUMAN gate at
   MIGRATION-LEDGER.md:84-89) triaged its source as `character-sheet` and
   **refused** to write `pcs/jean-claude-tabarnack.md`, citing SKILL.md's
   Owned-paths "Never" bullet ("PC creation is a canon-review-signed event... not
   this skill's to originate") — the same reasoning the R2 refusal
   (`ss2-dm-perrin-primer.md`) used before R4's authorization existed. That refusal
   does not appear to have weighed the R4 ledger-header text naming both PC lines
   as themselves *constituting* the canon-review signature ("The PC lines below are
   the canon-review signature PC creation requires — the user explicitly directed
   PC-file ingestion"), nor the DISPATCH-prompt-level twist repeating the same
   instruction for both PC lines. This dispatch's own line-specific twist
   ("Target: pcs/perrin-black-jaw.md from docs/campaign/skeletons/pc.md... Status:
   canon (canon-by-nature)") gave an unambiguous, current, more-specific
   instruction to write the page, so this agent proceeded — but the two sibling
   dispatches reached opposite conclusions from the same authorization text. Flag
   for orchestrator/human: either the jean-claude line needs re-dispatch under the
   same explicit instruction this line received, or this line's page needs to be
   un-written if the refusal was actually correct. Not resolved unilaterally here —
   named for wave review.
2. **PDF sheet, not processed** — `perrin-black-jaw-sheet.pdf` (845KB), per ledger
   line's own text ("no PDF tooling by design"). Its stats (ability scores, full
   equipment, exact HP/AC) would complete the `hp_max`/`ac`/full `inventory` stubs
   left on the written page. A future pass with PDF tooling (or the DM transcribing
   it by hand) is the only path to close those stubs — canon-review territory per
   the ledger line, not a re-triage of this source.
3. **dm/perrin-primer.md — confirmed NOT folded**, per the ledger line's explicit
   carve-out. R2's refusal (`ss2-dm-perrin-primer.md`) already named the correct
   eventual destination (this PC's `## Arc Notes (DM Only)` section) now that the
   page exists — that fold is still a separate human-gated decision, not executed
   here. `pcs/perrin-black-jaw.md` now exists, so R2 Flag #2's precondition
   ("Once `pcs/perrin-black-jaw.md` exists...") is satisfied; the fold itself
   remains undone pending that separate decision.
4. **relink: jean-claude-tabarnack** — resolved ✓ (link-pass R6, 2026-07-14),
   Party section now links `[[jean-claude-tabarnack|Jean-Claude Tabarnack]]`.
5. **relink: delmar-fisk** — resolved ✓ (link-pass R6, 2026-07-14), Party
   section now links `[[delmar-fisk|Delmar Fisk]]`.
6. **relink: crissdalynn-khinriss** — resolved ✓ (link-pass R6, 2026-07-14),
   Party section now links `[[crissdalynn-khinriss|Crissdalynn Khinriss]]`.
7. **relink: cobb** — no page yet. Plain text.
8. **relink: vestra** (ship) — no page yet (`world/ships/` has `vethka.md` and
   `greyteeth-runner.md` only — confirmed a different ship, not a naming variant:
   Vethka is a Grung war proa per its own page, unrelated to the Black-Jaw family
   fishing vessel). Plain text.
9. **relink: leviathan** — no page yet (`world/creatures/` checked). Plain text.
10. **relink: auralis** — no page yet. Plain text.
11. **relink: perrins-cloak-of-the-manta-ray** — no page yet. NOT the same entity
    as the existing `world/items/delmars-cloak-of-the-manta-ray.md` (checked the
    source files for both: distinct heirlooms, distinct families, distinct physical
    descriptions — mottled grey-green cloak vs. a red admiral's coat). Plain text,
    own future page.
12. **relink: miras-blade** — no page yet, but IS independently corroborated in
    `sessions/02-conflict-is-a-surety/state-changes.md:52` (`NEW
    world/items/miras-blade.md`) — a sibling line already queued to create it.
    Plain text here; will resolve once that line lands.
13. **relink: sending-stone-nona** — resolved ✓ (link-pass R6, 2026-07-14),
    "Nona's sending stone" (What he carries) now links `[[sending-stone-nona]]`.
14. **relink: nona-black-jaw** — resolved ✓ (link-pass R6, 2026-07-14), first
    mention (Current pressure) now links `[[nona-black-jaw|Nona Black-Jaw]]`;
    later mentions stay plain per single-link-per-page convention.
15. **relink: beaumont-sel** — no page yet. Plain text.
16. **relink: ket** — resolved ✓ (link-pass R6, 2026-07-14), Session Log
    "kill Ket" now links `[[ket|Ket]]`.
17. **relink: master-kyzil** — no page yet. Plain text.
18. **relink: ponte-bassa** — no page yet. Plain text.
19. **Not relinked, no page type fits**: "abyss vision" (Session 03) and "Nona and
    Anzolo" (Session 03) are source-side cross-reference labels, not entities with a
    skeleton type — left as plain prose, no relink flag (nothing to eventually
    convert).
20. **Rule/species content, collapsed**: Bard, Warlock, Rattkin are PHB-core-class /
    campaign-species references — Bard and Warlock are stock SRD/PHB classes
    (collapsed, no per-item relink, same treatment as stock gear per skill rule).
    Rattkin is campaign-specific (already a tag in `world/_meta/tags.md`'s absence —
    checked, `rattkin` is NOT a canonical/alias tag there, dropped from this page's
    `tags:` per project rule "identity/origin tags drop") but has no `world/`
    lore/rule page yet either — one collapsed plain-text note, not a per-mention
    relink, since it's the PC's own species descriptor repeated throughout, not a
    single reference.
21. **Stub fields**: `hp_max`, `ac` — source states neither anywhere (no numeric
    stats in the narrative profile at all). Left blank with a stub note per Hard
    Rule 1 — not guessed. See Flag #2 (PDF sheet) for the eventual source.
22. **Status rung**: canon, rung 2 (in-play evidence) — cited in-page. Corroborating
    citations: `sessions/01-boarding-of-the-saltwright/transcript.md:29` ("But
    Perrin had laid a Minor Illusion..."),
    `sessions/01-boarding-of-the-saltwright/state-changes.md:31` (NEW pcs/ line,
    PC inferred), `sessions/02-conflict-is-a-surety/state-changes.md:35` ("Perrin
    cast Tasha's Hideous Laughter." / "Perrin told the crew who he was: a
    Black-Jaw." — PC-confidence-upgrade language, matching this dispatch's brief).
23. **Session Log linking**: campaign-os only has `sessions/01-boarding-of-the-
    saltwright/` and `sessions/02-conflict-is-a-surety/` migrated so far (Sessions
    03-04 in the source are not yet migrated as campaign-os session files). Used
    real relative paths for sessions 01-02 (not wikilinks — `world/_meta/index.md`
    aliases both session-type pages identically as `[[state-changes]]`, which would
    be ambiguous as a link target); Sessions 03-04 cited as `%%src: legacy%%`
    prose-only, no session file to link yet.
