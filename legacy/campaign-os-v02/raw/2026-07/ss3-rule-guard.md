# Source ingest queue: ss3-rule-guard

Source root: /Users/nick/ai-os/shattered-sea/wiki/rules/backgrounds/guard.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — Round 3 —
"rules-background :: rules/backgrounds/guard.md → world/rules/ — subtype: background")
Gate: REVIEWED-BY-HUMAN: 2026-07-13 (line 63) covers the 14 Round 3 lines, including
this one (line 73). R2 synthesis in force: status-precedence ladder, de-linkify quoted
evidence, SRD-gear never-link, type-confidence notation, tag tonal-evidence rule.
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] rules/backgrounds/guard.md — triage: rule content (background), ready

## Claims — rules/backgrounds/guard.md

- [x] rule-background :: Guard :: world/rules/guard.md (new) — D&D 5e 2024 Guard
  background, full mechanical transcription (%%src: legacy%%)

## Status determination (migration-mode ladder)

- Rung 1 (explicit unrevealed marker): none in the source body — no "Not yet
  encountered" line, no planned/ directory.
- Rung 2 (source session logs show actual play): checked
  `grep -ril "guard" shattered-sea/wiki/entities/characters/` and PC sheets
  (crissdalynn-khinriss.md, delmar-fisk.md) — no PC has Guard as a background; the
  only "guard" hits are unrelated word matches ("guardrails", a "Guard:" combat
  question in a tactics-primer table). No reveal evidence.
- Rung 3 (per-file audience:players + publish:true): does NOT apply — checked all 17
  background files in the source pile (acolyte, artisan, carouser, charlatan,
  criminal, entertainer, farmer, guard, guide, harper, hermit, merchant, noble, sage,
  sailor, scribe, soldier): every one carries identical `status: unknown,
  audience: dm, publish: false` (only index.md, a navigation file, differs). Uniform
  across the whole sub-pile = export default, not a per-file signal (claim-buckets
  rules-row shortcut) — same shortcut R2 codified for the subclasses/ pile
  (swashbuckler, draconic-sorcery).
- Rung 4 (no signal of any kind) → **DECIDES**: `status: pending`. Falls through
  cleanly to rung 4 once rung 3 is excluded by the uniformity caveat.

Library-default shortcut applies (uniform backgrounds/ pile, same pattern as R2's
subclasses/ pile) — landed `status: pending` with no per-file re-derivation needed.

## Link check

Checked source body against the 20 real-page candidates (estratto, ferrin-locke,
calveno, grimaldis-dispensary, preserved-eel, fish-broth, sentinels-of-the-eyrie,
waveservants, campaign-overview, grung, human, syranita, tyr,
the-vault-of-the-first-factor, gentle-hag, giant-owl, swashbuckler,
draconic-sorcery, vethka, greyteeth-runner) — the Guard background text names none
of them; it is a generic, unattached rules page (no NPC or PC uses this background
in the source repo). No wikilinks written, no relink flags needed.

Equipment list (Spear, Light Crossbow, Bolts, Gaming Set, Hooded Lantern, Manacles,
Quiver, Traveler's Clothes) is SRD/PHB stock gear — plain text, never a link target
(collapsed single note, no per-item relink flags per skill's SRD-gear rule).

## Tags

Source frontmatter: `tags: []` — no tonal or identity tags present to map or drop.
Landed `tags: []` (always legal, no genuine tonal signal in the source text).

## Flags

- none
