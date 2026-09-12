# Source ingest queue: ss2-creature-giant-owl

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/creatures/background/giant-owl.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md § Round 2 — `creature ::
entities/creatures/background/giant-owl.md → restructure → world/creatures/ — creature
type at n=2`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:41 "REVIEWED-BY-HUMAN:
2026-07-13 — user instruction \"implement all your recommended fixes, then proceed
to round two\". Blessing covers exactly the 13 lines below."
Started: 2026-07-13

Type gap check: none needed. `type: creature` already landed (commit ed63957,
probed and shipped against `world/creatures/gentle-hag.md`). This is the n=2
instance the ledger line calls out — testing whether the skeleton and its
`### Related`-under-DM-Only convention hold for a second, unrelated source file.

## Sources (batch order, smallest file first)

- [x] entities/creatures/background/giant-owl.md — triage: entity-source
      (creature-shaped, generic bestiary entry — no individual campaign
      identity, same bucket as gentle-hag) — written to
      `world/creatures/giant-owl.md`, `type: creature`

## Claims — entities/creatures/background/giant-owl.md

- [x] creature identity + full statblock :: Giant Owl :: `world/creatures/
      giant-owl.md` § Stats & Combat — CR 1/4 celestial, AC 12, HP 19 (3d10+3),
      Flyby trait, Talons action, at-will/1st-level innate spellcasting
      (Detect Evil and Good, Detect Magic, Clairvoyance), inside the
      ```statblock``` fence verbatim per the gentle-hag.md precedent
      (%%src: legacy%%)
- [x] habitat/lore prose :: Giant Owl :: `world/creatures/giant-owl.md` §
      DM Only — "Forests and highlands. In the Shattered Sea, associated with
      the Crown Islands." Crown Islands has no page in `world/`/`pcs/`/`prep/`
      (stub check: `grep -ril "crown.island" world/ pcs/ prep/` → one hit,
      `world/lore/campaign-overview.md`, which only mentions the name in prose
      and isn't itself a Crown Islands page) — left as plain text,
      `relink: crown-islands — once its page lands` (%%src: legacy%%)
- [x] related-entity links :: Giant Constrictor Snake, Giant Axe Beak ::
      `world/creatures/giant-owl.md` § DM Only › ### Related — target pages do
      not exist yet (stub check: `grep -ril "giant.constrictor.snake\|giant.axe.beak"
      world/ pcs/ prep/` → no hits; no ledger line in this batch names either).
      Written as plain text per migration-mode link deferral;
      `relink: giant-constrictor-snake — once its page lands` and
      `relink: giant-axe-beak — once its page lands` flags carried below.
      Confirms the `### Related`-under-DM-Only convention gentle-hag improvised
      recurs cleanly on a second, unrelated source (n=2 signal the ledger line
      asked about).

## Flags

1. **Status override applied — same pattern as gentle-hag/estratto.** Source
   has no Session Events / appearance marker of any kind (`grep -ril "giant
   owl" /Users/nick/ai-os/shattered-sea/wiki/` → only index/bestiary listing
   pages and `entities/places/islands/aldenmere.md`'s flavor prose about wild
   giant owls on that island — no session transcript or "encountered" marker
   anywhere; confirmed no hits in campaign-os `sessions/*/transcript.md`
   either). Reads as an unused bestiary entry, never brought to the table.
   Landed `status: pending`, overriding the ledger's default `canon`
   disposition.
2. **Related-entity links deferred, live.** Giant Constrictor Snake and Giant
   Axe Beak (source's own `## Related` section) — plain text in
   `world/creatures/giant-owl.md` § DM Only › ### Related.
   `relink: giant-constrictor-snake — once its page lands`,
   `relink: giant-axe-beak — once its page lands`.
3. **Habitat link deferred, live.** Crown Islands (source's `## Habitat`
   prose, originally a `[[crown-islands|Crown Islands]]` wikilink in the
   source) — plain text in § DM Only. `relink: crown-islands — once its page
   lands`.
4. **Tag dropped, not substituted — this is the divergence from gentle-hag's
   tag handling.** Source `tags: [combat]` has no canonical equivalent in
   `world/_meta/tags.md` (canonical Domain-tone tags: intrigue, heist, horror,
   mystery, exploration, war, politics, romance). Gentle Hag's own `combat`
   tag was mapped to `horror` on tone grounds (the page's own closing line was
   explicitly horror-themed). Giant Owl carries no comparable tonal signal
   anywhere in the source — a neutral celestial bestiary statblock with no
   distinct Domain-tone content. Forcing `horror` (or any other canonical tag)
   onto it would violate WIKI.md § Tag taxonomy's "don't force-fit" rule, so
   `combat` is dropped with no substitute; landed `tags: []`.
5. **Frontmatter drop.** Legacy keys with no contract equivalent (`campaign`,
   `audience`, `confidence_level`, `sources`, `page`, `statblock`, and the
   ability-score/`cr`/`creature_type`/`environment` fields) dropped per the
   gentle-hag precedent (Flag 5 there) — all mechanical fields already live
   inside the `statblock` codeblock; `creature` carries no type-specific
   governed frontmatter keys today. `aliases: [Giant Owl]` also dropped to
   `[]`, matching gentle-hag's identical drop of its own name-only alias.
6. **Skeleton/convention hold confirmed at n=2.** Player-Known · DM Only ·
   Stats & Combat · Appearances headings and the `### Related`-under-DM-Only
   sub-heading both mapped cleanly onto this second, structurally-identical
   but topically-unrelated source with no skeleton changes needed.
