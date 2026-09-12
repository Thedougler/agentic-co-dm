# Source ingest queue: ss-npc-estratto

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/characters/npcs/estratto.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — `npc :: entities/characters/npcs/estratto.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:11 "REVIEWED-BY-HUMAN: 2026-07-13 — per the user's handoff mission..."
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/characters/npcs/estratto.md — triage: entity-source, ready

## Claims — entities/characters/npcs/estratto.md

- [x] npc :: Estratto :: world/npcs/estratto.md (new) — full NPC identity, voice, writ, statblock, combat tactics (%%src: legacy%%)

## Flags

1. **Disposition override: canon → pending.** Ledger line 23 defaults to
   `status: canon (revealed legacy NPC unless source says otherwise)`. The
   source's own `## Session Events` heading reads `*(Not yet encountered.)*`
   — explicit signal this NPC has never actually appeared at the table. Per
   wiki-contract.md's own tier definition, `canon` means "Revealed at the
   table or ruled by the DM"; this NPC is neither. Per source-ingest's Two
   Modes gate condition (c) — "the disposition is canon because the content
   is already-revealed legacy material, not new prep" — that condition fails
   for this specific file even though the ledger line pre-declared it canon.
   Written `status: pending` instead, citation kept as `%%src: legacy%%`
   (factual provenance, not a status claim). Filed as the primary judgment
   call for canon-review / the DM: confirm pending-in-world/npcs/ is
   acceptable, or this page should move to prep/ instead (see report).

2. **Unresolved wikilinks — reciprocal links deferred.** The source links to
   six other entities ([[tessarine-concordat]], [[uncertainty]],
   [[hcs-surety]], [[delmar-fisk]], [[admiral-fisk]], [[calveno]]/
   [[calveno-la-vasca|la-vasca]]). None of these pages exist in world/ yet. Migration mode's
   Owned Paths restrict this agent to writing only the file named on the
   ledger line being executed (world/npcs/estratto.md) — creating stub pages
   for these six entities would exceed that scope and risks colliding with
   sibling agents' own ledger lines (e.g. the location agent may create
   `calveno-reference.md`, not `calveno.md`). Written as **plain text, not
   `[[wikilinks]]`**, to avoid a W3 hard-fail on an unresolvable link.
   Flagged for a follow-up pass once those ledger lines land.
   - relinked ✓ — `calveno` — `world/locations/calveno.md` landed; all three
     plain-text "Calveno" mentions (infobox `Currently` row, Player-Known
     prose, Relationships bullet) now link `[[calveno|Calveno]]`
     (link-restoration pass, 2026-07-13). "La Vasca" itself has no page
     (calveno.md has no alias for it) and stays plain text.
   - relinked ✓ — `la-vasca` — real page is `world/locations/calveno-la-vasca.md`
     (canon), landed since the note above was written. The two "La Vasca"
     mentions (infobox `Currently` row, Relationships bullet) now link
     `[[calveno-la-vasca|La Vasca]]` (link-restoration pass R4, 2026-07-14)
   - relinked ✓ — `hcs-surety` — `world/ships/hcs-surety.md` landed (canon).
     The three `*HCS Surety*` mentions (Player-Known/DM Only prose x2,
     Relationships bullet) now link `*[[hcs-surety|HCS Surety]]*`
     (link-restoration pass R4, 2026-07-14)
   - still deferred: tessarine-concordat, uncertainty, delmar-fisk,
     admiral-fisk — no pages exist for any of these yet.

3. **Frontmatter fields with no contract home.** Source frontmatter carried
   `campaign`, `audience`, `confidence_level`, `species`, `sources:` — none
   are governed keys in wiki-contract.md's npc schema. Dropped from
   frontmatter; `species` folded into the Player-Known stat table as prose;
   the rest have no equivalent (noted, not invented a substitute).

4. **`created`/`touched` have no migration-mode value.** wiki-contract.md
   only defines `sNN` or `prep` for these fields. Neither fits legacy
   migrated content. Used `legacy` as the closest-fidelity placeholder —
   flagged since this isn't a documented enum value.

5. **Tags don't map to the taxonomy.** Source tags `tessarine`, `homebrew`
   are neither canonical Domain tags nor listed aliases in
   world/_meta/tags.md (Project tags are empty at bootstrap). Substituted
   `intrigue`, `horror` (closest canonical fit to the content's tone) and
   dropped the source's own tags rather than adding new canonical entries
   unilaterally.
