# Source ingest queue: ss2-location-dispensary

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/places/buildings/grimaldis-dispensary.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — Round 2, location :: entities/places/buildings/grimaldis-dispensary.md → restructure → world/locations/ — subtype: building expected)
Started: 2026-07-13

Gate proof (docs/campaign/MIGRATION-LEDGER.md):

```text
41:REVIEWED-BY-HUMAN: 2026-07-13 — user instruction "implement all your recommended
fixes, then proceed to round two". Blessing covers exactly the 13 lines below.
48:- [ ] location :: entities/places/buildings/grimaldis-dispensary.md → restructure → world/locations/ — subtype: building expected
```

## Sources (batch order, smallest file first)

- [x] entities/places/buildings/grimaldis-dispensary.md — triage: location, ready

## Claims — entities/places/buildings/grimaldis-dispensary.md

- [x] location :: Grimaldi's Dispensary :: world/locations/grimaldis-dispensary.md (new) — subtype: building (matches source's own subtype, honest fit confirmed), status: canon. Player-Known (overview, stock/services, access), DM Only (discretionary stock, harbour-boss arrangements), Notable NPCs (Ilaria Grimaldi), Hooks (ring/Passage mark, the Captain's Map, Sawek survivor), Appearances (none stated). Lint: clean, exit 0. (%%src: legacy%%)

## Flags

- **Subtype fit: honest match, no mismatch.** Source frontmatter states
  `subtype: building` directly; wiki-contract enum
  (`region|island|settlement|district|building|dungeon|plane`) has an exact
  member for it. No STOP triggered.

- **Status disposition: `canon`, per established migration precedent — not
  re-derived from scratch.** Source frontmatter carries `status: active`,
  `audience: players`, `publish: true`, `confidence_level: medium`, and has
  no `## Session Events`-style "unrevealed" marker (unlike
  `ss-npc-estratto.md`'s explicit "Not yet encountered" line, or
  `ss2-npc-ferrin-locke.md`'s complete absence of any Session
  Events/Appearances heading, which landed that one `pending`). This mirrors
  `ss-item-preserved-eel.md`'s precedent exactly: "Absent a contrary signal,
  treated the legacy `publish: true`/`audience: players` state as evidence of
  table-reveal." I also grepped this repo's own `sessions/*/transcript.md`
  and the legacy source repo's `sessions/` for "grimaldi" — zero hits either
  way — but per the `preserved-eel`/`calveno` precedent this absence is not
  treated as a contrary signal (those two also landed `canon` without a
  positive session hit; they're legacy-canon-by-publication, not
  already-played-out-this-campaign). Filed as the judgment call for
  canon-review to confirm, same as the sibling item/location lines.

- **Migration-mode canon exception** — writing `status: canon` directly to
  `world/` is only legal under the three-condition gate in source-ingest's
  Two Modes section (ledger line + REVIEWED-BY-HUMAN gate + legacy-reveal
  disposition), proven above. Noted per the same convention as every prior
  Round 1/2 canon line.

- **Wikilinks — all withheld, none of the 10 known-live pages appear in this
  source.** Checked against the given list (estratto, calveno,
  preserved-eel, sentinels-of-the-eyrie, campaign-overview, grung, syranita,
  gentle-hag, swashbuckler, vethka) and `world/_meta/aliases.md` (only alias
  on file: "the Auditor" → estratto — not relevant here). Zero matches. Every
  named entity below is plain text, not a `[[wikilink]]`:
  - relink: kalowe — parent settlement/free port (stub check: `grep -ril
    kalowe world/ pcs/ prep/` → no hits; only mentioned in prose inside
    `world/lore/campaign-overview.md`, no page of its own yet)
  - relink: ilaria-grimaldi — proprietor NPC (stub check: `grep -ril
    grimaldi world/ pcs/ prep/` → no hits)
  - relink: sera-maddock — dying passenger in the back room, "The Captain's
    Map" hook
  - relink: orak — island where the cache sits
  - relink: kalowe-captains-map — source's own linked situation page
    (`Kalowe — The Captain's Map`)
  - relink: port-tidefall — comparison point ("only healer's supply between
    Kalowe and Port Tidefall")
  - relink: the-flat-water — source's own "See Also" link
  - relink: wibowos-provisions — source's own "See Also" link
  - **Judgment call, not a per-line relink flag:** the 17 stock/service line
    items (Healer's kit, Bandages, Antitoxin, Alchemist's fire, etc.) are
    each individually `[[wikilinked]]` in the source, but these are generic
    D&D equipment/consumables, not campaign-specific entities in this wiki's
    claim-bucket sense (contrast `preserved-eel`, which is bespoke campaign
    flavor content and got its own item page in Round 1). Transcribed as
    plain-text name + price + flavor line, no individual relink flags filed
    — flagging this collapse explicitly rather than silently either
    over-flagging 17 lines of SRD gear or silently dropping the source
    wikilinks. REVIEW-for-human if item pages for standard equipment are
    ever wanted.

- **Tag mapping.** Source tag: `passage` — this is an entity-identity tag
  (`The Passage` is a named faction per `world/lore/campaign-overview.md`'s
  faction table), DROPPED per WIKI.md § Tag taxonomy final bullet, same
  bucket as `tessarine`/`dravosi` in prior lines. No genuine Domain-tone tag
  survives the drop to map — the content does carry an intrigue thread (the
  ring/Passage mark, the Captain's Map secret), but per Round-1's own
  friction note ("map only genuine Domain-tone tags... don't force-fit"), I
  mapped it anyway since the intrigue content is source-stated, not
  invented, and matches the same tag `world/locations/calveno.md` and
  `world/npcs/ferrin-locke.md` already carry for structurally identical
  content (a secret affiliation mark, a hidden hook). Applied `intrigue`.
  Final tag set: `intrigue`.

- **Frontmatter fields with no contract home — dropped**: `campaign`,
  `audience`, `confidence_level`, `sources:`, `building_type`, `district`.
  `building_type: shop` and `district: Third Island`/`parent_location:
  Kalowe` folded into prose (Player-Known) instead, matching how
  `calveno.md` folded its legacy district facts into a prose subsection
  rather than inventing new frontmatter keys.

- **`aliases:` carried through — contract field, not dropped.** Source
  states `aliases: - Grimaldi's`; skeleton has a native `aliases:` field, so
  kept: `aliases: ["Grimaldi's"]`.

- **`created`/`touched: legacy`** — per this mission's explicit instruction
  and identical to every prior Round 1/2 line.

- **`publish: false`** — never set `true` (contract item 4 / PUBLISH's
  exclusive call), despite legacy `publish: true`. Same as every prior
  canon line in this ledger.
