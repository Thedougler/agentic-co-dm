# Source ingest queue: ss3-item-delmars-cloak

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/items/uncommon/delmars-cloak-of-the-manta-ray.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md § Round 3 — `item-uncommon :: entities/items/uncommon/delmars-cloak-of-the-manta-ray.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:63 "REVIEWED-BY-HUMAN: 2026-07-13 — same user instruction; blessing covers exactly the 14 lines below." (line 68 names this file.)
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/items/uncommon/delmars-cloak-of-the-manta-ray.md — triage: entity-source, ready

## Claims — entities/items/uncommon/delmars-cloak-of-the-manta-ray.md

- [x] item :: Delmar's Cloak of the Manta Ray :: world/items/delmars-cloak-of-the-manta-ray.md (new) — item identity, owner, history, RAW mechanics (%%src: legacy%%)

## Flags

1. **Disposition: canon — status ladder rung 3.** Rung 1 (explicit unrevealed
   marker) does not apply: the file lives in `entities/items/uncommon/`, not a
   `planned/` dir, and its body carries no "Not yet encountered" line. Rung 2
   (session-log actual-play evidence) was checked but not used as the
   deciding rung: `session-01-recap.md`'s art-prompt text describes Delmar
   Fisk in a "salt-stiff scarlet admiral coat with gold epaulettes" during
   the session-1 Saltwright scenes, which plausibly is this cloak, but that
   match requires inferring identity from a costume description rather than
   the source naming the item — too indirect to cite as a rung-2 hit under
   Hard Rule 1 (fidelity, not inference). Rung 3 fires cleanly instead:
   source frontmatter carries `status: active`, `audience: players`,
   `publish: true`, and this is a genuinely per-file signal, not a pile-wide
   export default — confirmed by checking all 44 sibling files in
   `entities/items/uncommon/`: four of them (`corto-di-velo.md`,
   `puntura.md`, `silent-shortbow.md`, `wind-callers-boom.md`) carry
   `audience: dm` / `publish: false`, proving the pile varies file-by-file.
   Same disposition pattern as `ss-item-preserved-eel` and
   `ss2-item-fish-broth`.

2. **Migration-mode canon exception.** Per source-ingest's Two Modes section,
   this agent wrote `status: canon` directly under the three-condition
   migration gate proven at the top of this file (ledger line + REVIEWED-BY-
   HUMAN gate + disposition is already-revealed legacy content) — the
   sanctioned exception to shared-contract item 5.

3. **Withheld link — Delmar Fisk (owner).** Expected per the ledger line
   itself ("owner Delmar Fisk has no page (relink)"). Stub check (`grep -ril
   "delmar.fisk" world/ pcs/ prep/`) confirms no `delmar-fisk` page exists
   yet — he is named as a PC on `world/lore/human.md` and flagged there too,
   but PC-page creation is out of this skill's owned paths (character-sheet/
   PC boundary). Written as plain text "Delmar Fisk", no `[[wikilink]]`.
   - relink: delmar-fisk — once his page lands

4. **Withheld link — Umberlee.** Source History section names Umberlee as
   the deity/event that sank Fisk's fleet. Stub check: no `umberlee` page in
   `world/`. Not on the Round-3 real-link allowlist. Written as plain text.
   - relink: umberlee — once its page lands

5. **Withheld link — Crissdalynn Khinriss.** Source History section names
   Crissdalynn as the PC who dove to save Fisk. Stub check: no
   `crissdalynn-khinriss` page in `world/npcs/` (same gap already flagged on
   `world/lore/syranita.md`). Not on the Round-3 real-link allowlist. Written
   as plain text.
   - relink: crissdalynn-khinriss — once her page lands

6. **No real wikilinks from the 20-page Round-3 allowlist applied.** Source
   body mentions only Delmar Fisk, Umberlee, and Crissdalynn Khinriss — none
   of the 20 named real-link targets (estratto, ferrin-locke, calveno,
   grimaldis-dispensary, preserved-eel, fish-broth, sentinels-of-the-eyrie,
   waveservants, campaign-overview, grung, human, syranita, tyr,
   the-vault-of-the-first-factor, gentle-hag, giant-owl, swashbuckler,
   draconic-sorcery, vethka, greyteeth-runner) appear in this source.

7. **Frontmatter fields with no contract home — dropped.** Source frontmatter
   carried `campaign`, `confidence_level`, `sources:`, `item_type: wondrous`,
   `current_holder` — none are governed keys in wiki-contract.md's item
   schema. `current_holder` is carried instead as an Owner line in
   `## Player-Known` prose (plain text + relink flag), same treatment the
   source gave it as visible top-of-body text, not a DM-secret.

8. **`rarity`/`attunement` already conformed — no shoehorn needed.** Source
   already stated `rarity: uncommon`, `requires_attunement: true`, both valid
   per wiki-contract.md's item schema enum (`common | uncommon | rare | very
   rare | legendary`; `attunement: true | false`). No STOP triggered. Carried
   through unchanged (`attunement: true`).

9. **Tags — origin tag dropped, no Domain-tone tag to map.** Source carried
   `homebrew` (origin tag, dropped by design per WIKI.md § Tag taxonomy) and
   `maritime`, which has no canonical Domain entry in `world/_meta/tags.md`
   (intrigue/heist/horror/mystery/exploration/war/politics/romance) and no
   genuine tonal match in the page's own content — a family-heirloom rescue
   story doesn't cleanly read as any single one of those tones. Per the
   Round-3 tag tonal-evidence rule, landed at `tags: []` rather than forcing
   a fit.

10. **`## DM Only` left empty.** Source states nothing beyond the History
    paragraph, which reads as the PC-owner's own known backstory (his
    heirloom, his rescue) rather than DM-secret content — placed under
    `## Player-Known` instead, matching the source's own placement of that
    prose above any DM-gated heading. No genuinely DM-only fact was stated,
    so the heading is left empty (same pattern as `ss-item-preserved-eel`).

11. **`created`/`touched` set to `legacy`.** Same placeholder every migrated
    item page in this ledger uses.

## Lint

See commit for output.
