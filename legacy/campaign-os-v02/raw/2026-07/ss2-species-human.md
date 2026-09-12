# Source ingest queue: ss2-species-human

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/species/human.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — Round 2, line 53:
"species :: entities/species/human.md → restructure → world/lore/ — LIVE W9
dual-home test (lore/species/human-culture.md is the known counterpart)")
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/species/human.md — triage: lore (species mechanics, PHB-derived), ready

## Claims — entities/species/human.md

- [x] lore :: Human (species) :: world/lore/human.md (new) — species identity,
  table traits, class-like feature traits (%%src: legacy%%)

## W9 dual-home duty (LIVE test)

Read both source copies in full:

- `entities/species/human.md` (my ledger file — the one I transcribe from)
- `lore/species/human-culture.md` (the known counterpart — read-only comparison,
  never transcribed from directly)

`diff` result (byte-exact): the two files are **content-identical** in every line
of body prose, the H1, the stat table, the Traits section, and the Connections
list. The only differences are two frontmatter fields:

- `type:` — `entity` in `entities/species/human.md` vs. `lore` in
  `lore/species/human-culture.md` (the counterpart already carries the type this
  migration assigns; corroborates the `world/lore/` restructure target)
- `updated:` — `2026-05-31` vs. `2026-06-06` (the counterpart was touched 6 days
  later, no content change accompanies it)

**Shared facts — transcribed from:** `entities/species/human.md` exclusively (my
ledger file), per the ledger's "ingest ONLY your ledger file" instruction. Every
fact on `world/lore/human.md` — creature type, size, speed, life span, the three
Traits (Resourceful/Skillful/Versatile), the Sigil-origin/diversity prose, and the
three Connections links — appears verbatim in both source copies, so nothing was
cherry-picked from the counterpart; it happens to agree with the file I'm bound to.

**Contradictions found: NONE.** Zero body-content deltas between the two copies —
nothing to CONTRADICTION-block.

**Facts ONLY in `lore/species/human-culture.md` (orphaned, NOT transcribed):
NONE.** The `diff` shows no body text unique to the counterpart — only the two
frontmatter field values noted above, which are not "facts" in the
Player-Known/DM-Only sense and carry no independent content to route to a future
ledger line.

**W9 verdict:** the "dual-home" premise holds structurally (two files, two paths)
but is a **degenerate case at the content layer** — same species, same file body,
byte-identical prose, differing only in `type:`/`updated:` frontmatter. No merge
decision, no split decision, and no orphaned-fact backlog to route: there is
nothing left in the counterpart that isn't already on `world/lore/human.md`. This
is the mirror-image finding of grung's Round-1 note ("W9 test vacuous here, would
fire on human") — it fires here, and resolves to "duplicate export of the same
prose," not a genuine content fork.

## Flags

- `relink: rattkin` — source links `[[rattkin|Rattkin]]`; no `rattkin` page exists
  in `world/` yet (not on the 10-page EXIST list). Left as plain text
  "Rattkin" on `world/lore/human.md`. Re-link once a rattkin ledger line lands.
- `relink: delmar-fisk` — source links `[[delmar-fisk|Delmar Fisk]]`; no
  `delmar-fisk` page exists in `world/` yet (not on the 10-page EXIST list, and
  matches `world/rules/swashbuckler.md`'s existing identical flag for the same
  NPC). Left as plain text "Delmar Fisk" on `world/lore/human.md`.
- `[[grung|Grung]]` link IS live — `world/lore/grung.md` exists (Round 1). Written
  as a real wikilink.
- Status: landed `status: canon` — source frontmatter (`status: active`,
  `audience: players`, `publish: true`) carries the same profile that migrated
  `world/lore/grung.md` and `world/factions/sentinels-of-the-eyrie.md` to canon
  (core, already-in-play species mechanics, not "not yet encountered" prep). No
  reveal-signal caveat found anywhere in the source text.
- Tags: source `tags: []` on both copies — nothing to map under WIKI.md § Tag
  taxonomy (no Domain-tone tags present to migrate, no entity-identity/origin tags
  to drop).
