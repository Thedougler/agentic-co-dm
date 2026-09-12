# Source ingest queue: ss2-lore-vault-first-factor

Source root: /Users/nick/ai-os/shattered-sea/wiki/lore/the-vault-of-the-first-factor.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — Round 2, `lore ::
lore/the-vault-of-the-first-factor.md → restructure → world/lore/`)
Gate proof:

- REVIEWED-BY-HUMAN: 2026-07-13 — user instruction "implement all your recommended
  fixes, then proceed to round two". Blessing covers exactly the 13 lines below.
  (MIGRATION-LEDGER.md:41-42)
- Ledger line: `- [ ] lore :: lore/the-vault-of-the-first-factor.md → restructure →
  world/lore/` (MIGRATION-LEDGER.md:55)
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] lore/the-vault-of-the-first-factor.md — triage: lore/legend, ready

## Claims — lore/the-vault-of-the-first-factor.md

- [x] lore :: The Vault of the First Factor :: world/lore/the-vault-of-the-first-factor.md (new) — legendary hidden Tessarine depository, DM-only legend never revealed at the table (%%src: legacy%%)

## Flags

- Status disposition: source frontmatter is `audience: dm`, `status: active`,
  `confidence_level: low`, `publish: false` — a genuine per-file reveal signal (not a
  library default; contrast campaign-overview's `audience: players`/`publish: true`).
  `sessions/` has no session content yet (only `sessions/CLAUDE.md`) — zero corroborating
  reveal evidence. Landed `status: pending` per estratto/syranita precedent (Round 1
  lines 23, 29): unrevealed DM lore, not canon.
- Tag mapping: source `tags: [tessarine]` is a pure entity-identity tag — DROPPED BY
  DESIGN per WIKI.md § Tag taxonomy, no genuine Domain-tone tag present in source to
  map. Assigned two canonical Domain tags from content tone instead (same
  content-inference precedent campaign-overview used: source had `tags:
  [player-resource]`, landed `tags: [exploration, politics]`): `mystery` (unconfirmed
  legend, no official acknowledgment, "which most observers interpret as confirmation")
  and `exploration` (uncharted limestone spire, finding it is itself a navigation
  challenge).
- relink: tessarine-concordat — once its faction page lands (source links
  `[[tessarine-concordat|Tessarine Concordat]]` twice; not one of the 10
  pre-verified-existing pages for this round). Written as plain text "Tessarine
  Concordat" on the new page.
- relink: midchain — once its location/lore page lands (source links
  `[[midchain|Midchain]]` twice; not one of the 10 pre-verified-existing pages).
  Written as plain text "Midchain" on the new page. Note: `world/lore/grung.md` and
  `world/lore/campaign-overview.md` already plain-text-mention Midchain too — same
  relink target, not a new gap.
- calveno IS a verified-existing page (world/locations/calveno.md) — written as a
  real wikilink `[[calveno|Calveno]]`.
- No subtype field used — source's `subtype: legend` folded into prose (first sentence
  states "A legendary hidden depository..."), matching the syranita.md precedent (no
  invented type key; findability via prose, not frontmatter).
- Legacy frontmatter keys with no contract equivalent (`campaign`, `audience`,
  `confidence_level`, `sources:`) dropped per MIGRATION-LEDGER.md § Flags (accepted
  mission-wide policy, not a new decision).
