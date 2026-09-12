# Source ingest queue: ss2-item-fish-broth

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/items/common/fish-broth.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md § Round 2 — `item :: entities/items/common/fish-broth.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:41 "REVIEWED-BY-HUMAN: 2026-07-13 — user instruction \"implement all your recommended fixes, then proceed to round two\". Blessing covers exactly the 13 lines below."
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/items/common/fish-broth.md — triage: entity-source, ready

## Claims — entities/items/common/fish-broth.md

- [x] item :: Fish Broth :: world/items/fish-broth.md (new) — food item identity, availability, description (%%src: legacy%%)

## Flags

1. **Disposition: canon, per legacy publish signal.** Source frontmatter carries
   `status: active`, `audience: players`, `publish: true` and no `## Session
   Events` heading or any other unrevealed-content marker — same pattern the
   sibling `ss-item-preserved-eel` ingest used to land `status: canon`.
   Followed identically here. Filed as the judgment call for canon-review to
   confirm.

2. **Migration-mode canon exception.** Per source-ingest's Two Modes section,
   this agent wrote `status: canon` directly under the three-condition
   migration gate proven at the top of this file (ledger line + REVIEWED-BY-
   HUMAN gate + disposition is already-revealed legacy content) — the
   sanctioned exception to shared-contract item 5.

3. **Real wikilink — Calveno.** Source body names "[[calveno|Calveno]]" (the
   Ponte Bassa's city). `world/locations/calveno.md` exists (confirmed) and
   is on the round-2 real-links allowlist — written as a real wikilink
   `[[calveno|Calveno]]`.

4. **Withheld link — Ponte Bassa.** Source body also names "Ponte Bassa" as
   the specific tavern. Stub check (`grep -ril "ponte.bassa" world/ pcs/
   prep/`) → no hits, and Ponte Bassa is not on the round-2 10-page real-link
   allowlist. Written as plain text "the Ponte Bassa", no `[[wikilink]]`, per
   Migration-mode link deferral.
   - relink: ponte-bassa — once its page lands

5. **Frontmatter fields with no contract home — dropped.** Source frontmatter
   carried `campaign`, `audience`, `confidence_level`, `sources:`,
   `item_type: consumable`, `homebrew: false` — none are governed keys in
   wiki-contract.md's item schema (item type and homebrew status are
   explicitly named as staying out of item frontmatter). Dropped, not
   shoehorned into a substitute field.

6. **`created`/`touched` set to `legacy`.** Same placeholder the sibling item
   ingest and this task's explicit instruction both use for migrated content
   predating the pipeline.

7. **Tags — origin tag dropped, no Domain-tone tag to map.** Source carried a
   single tag, `homebrew` — an origin tag, dropped by design per WIKI.md §
   Tag taxonomy's final bullet (origin lives in `[HB]`/`[RAW]` mechanic
   labels, not frontmatter tags). No genuine Domain-tone tag is present in
   the source to map, so the page lands with `tags: []` rather than a forced
   substitution.

8. **`rarity`/`attunement` already conformed — no shoehorn needed.** Source
   already stated `rarity: common`, `attunement: false`, both valid enum
   members per wiki-contract.md's item schema (`common | uncommon | rare |
   very rare | legendary`; `true | false`). No STOP triggered. Carried
   through unchanged.

9. **No mechanics beyond identity/flavor stated.** Source gives no cost,
   weight, or consumable-effect mechanics (unlike preserved-eel's "4 cp").
   `## Mechanics` left as a stub note rather than an invented price, per
   Hard Rule 1 and the item bucket's "incomplete mechanics get a stub
   note, never invented balance numbers — hand off to item-prep" guidance.
