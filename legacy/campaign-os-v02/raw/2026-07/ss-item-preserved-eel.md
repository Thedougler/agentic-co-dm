# Source ingest queue: ss-item-preserved-eel

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/items/common/preserved-eel.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — `item :: entities/items/common/preserved-eel.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:11 "REVIEWED-BY-HUMAN: 2026-07-13 — per the user's handoff mission..."
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/items/common/preserved-eel.md — triage: entity-source, ready

## Claims — entities/items/common/preserved-eel.md

- [x] item :: Preserved Eel :: world/items/preserved-eel.md (new) — food item identity, availability, price (%%src: legacy%%)

## Flags

1. **Disposition: canon, per legacy publish signal.** Source frontmatter carries
   `status: active`, `audience: players`, `publish: true` — this content was
   already player-facing in the legacy wiki, and unlike the sibling
   `ss-npc-estratto` ingest (which found an explicit "*(Not yet encountered.)*"
   Session Events marker overriding the ledger's default), this source has no
   `## Session Events` heading or any other "unrevealed" signal. Absent a
   contrary signal, treated the legacy `publish: true`/`audience: players` state
   as evidence of table-reveal and kept the ledger's declared `status: canon`
   disposition as-is. Filed as the judgment call for canon-review to confirm.

2. **Migration-mode canon exception, same tension as the npc line.** Per
   source-ingest's Two Modes section, migration mode is the sanctioned
   exception to shared-contract item 5 ("never flip `status: canon`" —
   CANONIZE/PUBLISH exclusively). Noted here for the same reason the sibling
   ingest flagged it: this agent wrote `status: canon` directly, which is only
   legal under the three-condition migration gate proven above.

3. **Unresolved wikilink — reciprocal link deferred.** Source body links to
   `[[low-lamp|Low Lamp]]`. No `low-lamp` page exists yet in world/pcs/prep
   (stub check: `grep -ril "low.lamp" world/ pcs/ prep/` → no hits). Written as
   plain text "the Low Lamp", no `[[wikilink]]`, per Migration-mode link
   deferral (never create a stub page for a source's mere link target).
   - relink: low-lamp — once its page lands

4. **Frontmatter fields with no contract home — dropped.** Source frontmatter
   carried `campaign`, `audience`, `confidence_level`, `sources:`,
   `item_type: food`, `homebrew: false` — none are governed keys in
   wiki-contract.md's item schema. `item_type` and `homebrew` are explicitly
   named as staying out of item frontmatter (wiki-contract.md: "Item type
   ... and whether it's homebrew stay out of frontmatter"); the rest have no
   equivalent key and were dropped, not invented a substitute for.

5. **`created`/`touched` set to `legacy`.** Same placeholder used by the
   sibling npc ingest — not a documented wiki-contract.md enum value (only
   `sNN` or `prep` are named) but the closest-fidelity fit for migrated
   content predating the pipeline, per this task's explicit instruction.

6. **Tags substituted — approximate, flagged.** Source tags `homebrew`,
   `maritime` are neither canonical Domain tags nor listed aliases in
   world/_meta/tags.md (Project tags empty at bootstrap; canonical Domain set
   is tone/genre-only: intrigue, heist, horror, mystery, exploration, war,
   politics, romance — none are physical/origin descriptors). Substituted
   `exploration` as the nearest tonal fit for maritime/seafaring flavor
   content; dropped `homebrew` entirely (content-origin, not tone/genre — no
   canonical tag covers that axis, and adding one unilaterally isn't this
   skill's call). This is a weak substitution — flagged for canon-review, not
   asserted as a confident mapping.

7. **`rarity`/`attunement` already conformed — no shoehorn needed.** Source
   already stated `rarity: common`, `attunement: false`, both valid enum
   members per wiki-contract.md's item schema (`common | uncommon | rare |
   very rare | legendary`; `true | false`). Carried through unchanged.
