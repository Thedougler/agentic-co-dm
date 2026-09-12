# Source ingest queue: ss3-location-plane-water

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/places/planes/elemental-plane-of-water.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — Round 3, location-plane :: entities/places/planes/elemental-plane-of-water.md → world/locations/ — subtype: plane (enum's untested member))
Started: 2026-07-13

Gate proof (docs/campaign/MIGRATION-LEDGER.md):

```text
63:REVIEWED-BY-HUMAN: 2026-07-13 — same user instruction; blessing covers exactly the
64:14 lines below. R2 synthesis in force (e1c4185): status-precedence ladder, de-linkify
65:quoted evidence, SRD-gear never-link, type-confidence notation, tag tonal-evidence rule.
...
71:- [ ] location-plane :: entities/places/planes/elemental-plane-of-water.md → world/locations/ — subtype: plane (enum's untested member)
```

## Sources (batch order, smallest file first)

- [x] entities/places/planes/elemental-plane-of-water.md — triage: location, ready

## Claims — entities/places/planes/elemental-plane-of-water.md

- [x] location :: Elemental Plane of Water :: world/locations/elemental-plane-of-water.md (new) — subtype: plane (source frontmatter states `subtype: plane` itself; wiki-contract's `location` enum has an exact member — the enum's untested member per the ledger line), status: pending (rung 3: source's own frontmatter states `audience: dm`, `publish: false` per-file — explicit unrevealed signal). Player-Known (physical manifestation, access, connected sites), DM Only (planar nature analysis, mortal-connections web, Pearl of Souls attractor mechanic), Notable NPCs (Leviathan/Ridgeback/Krakling — judgment call, see Flags), Hooks (widening fissure, Pearl of Souls beacon), Appearances (none — no session-log hit either repo). (%%src: legacy%%)

## Flags

- **Honest-fit check: place, not pure cosmology lore.** Source states
  `Access: breach through the Drowned Maw fissure` and a "Known Locations"
  table naming three concrete, reachable sites (The Drowned Maw, Antheri
  Ruins, The Shelfworks) with type/notes columns — this is a plane a party
  could physically travel to via a stated access method, not an abstract
  cosmology reference page. Source's own frontmatter already carries
  `type: entity, subtype: plane`, matching wiki-contract's `location` enum
  member exactly (`region | island | settlement | district | building |
  dungeon | plane`, wiki-contract.md:39). Verdict: **location**, subtype
  `plane`. No STOP triggered — the untested enum member fits clean on first
  contact.

- **Status disposition: `pending`, rung 3 of the migration-mode ladder.**
  Checked in ladder order:
  1. No explicit "Not yet encountered" line or `planned/`-directory
     placement — rung 1 does not fire.
  2. Grepped the *source* repo's `sessions/` for `elemental plane of
     water`, `leviathan`, and `drowned maw` (case-insensitive) — zero hits
     across all session/scene/recap files. Rung 2 does not fire (no
     positive reveal evidence).
  3. This file's own frontmatter states `audience: dm` and `publish: false`
     **per-file**, explicitly — not an inherited pile-default (contrast
     `grimaldis-dispensary.md`, which carried per-file `audience: players`
     - `publish: true` and landed `canon` on this same rung). Rung 3 fires
     here in the opposite direction: explicit DM-only/unpublished signal →
     `pending`.
  4. Not reached — rung 3 decided it.

- **Migration-mode write authority.** Writing directly to `world/` in
  migration mode requires (a) a ledger line naming this source (line 71,
  quoted above) and (b) the `REVIEWED-BY-HUMAN` gate satisfied (line 63,
  quoted above) — both proven. The skill's extra carve-out for writing
  `status: canon` directly does not apply here since the ladder landed
  `pending`, not `canon` — same posture as `ferrin-locke.md` and
  `giant-owl.md` in Rounds 1–2, which also wrote directly to `world/` at
  `status: pending` under conditions (a)+(b) alone.

- **Wikilinks — all withheld, none of the 20 known-live pages appear in
  this source.** Checked the source's every `[[wikilink]]` against the
  given list (estratto, ferrin-locke, calveno, grimaldis-dispensary,
  preserved-eel, fish-broth, sentinels-of-the-eyrie, waveservants,
  campaign-overview, grung, human, syranita, tyr,
  the-vault-of-the-first-factor, gentle-hag, giant-owl, swashbuckler,
  draconic-sorcery, vethka, greyteeth-runner) and confirmed by direct stub
  check (`grep -ril <name> world/ pcs/`) against every entity the source
  actually links. Zero matches either way. Every named entity below is
  plain text, not a `[[wikilink]]`:
  - relink: leviathan — first entity through the fissure, apex predator
    origin (stub check: no hits)
  - relink: the-drowned-maw — breach site, source's primary connected site
    (stub check: no hits; "Shattered Sea" itself mentions "the Drowned
    Maw" only in prose, per `world/lore/campaign-overview.md:19`, same
    unlinked-mention precedent)
  - relinked ✓ — pearl-of-souls — `world/items/pearl-of-souls.md` landed; the two
    "Pearl of Souls" mentions (DM Only prose, Hooks bullet) now link
    `[[pearl-of-souls|Pearl of Souls]]` (link-restoration pass R4, 2026-07-14)
  - relink: antheri-ruins — containment ruins site (stub check: no hits)
  - relink: shelfworks — salvage site (stub check: mentioned in prose only
    inside `world/lore/campaign-overview.md`, no page of its own)
  - relink: auralis — guards the Maw, aware of the incursion (stub check:
    mentioned in prose only inside
    `world/factions/sentinels-of-the-eyrie.md`, no page of its own)
  - relink: ridgeback — second entity through the fissure (stub check: no
    hits)
  - relink: krakling — juvenile arm-predator, third entity (stub check: no
    hits)
  - relink: perrin-black-jaw — source's own "See Also" link (stub check:
    no hits; note `world/locations/calveno.md` names a "Nona Black-Jaw,"
    a different individual — not treated as a match). `pcs/perrin-black-jaw.md`
    landed (canon) at link-restoration pass R4 (2026-07-14), but no plain-text
    "Perrin Black-Jaw"/"Perrin" mention exists anywhere on
    `world/locations/elemental-plane-of-water.md` to convert — the source's
    "See Also" link was never transcribed onto this page as prose. Nothing to
    relink without adding new content (out of scope). Still deferred.
  - "Shattered Sea" itself: left as plain text, unflagged — matches
    established convention across every prior migrated page (it is the
    campaign-setting name, not an entity page target;
    `world/lore/campaign-overview.md` doesn't self-link or flag it either).

- **Judgment call: Leviathan/Ridgeback/Krakling housed under "Notable
  NPCs."** These are creatures/threats, not persons, and the location
  skeleton has no separate "creatures" heading. Following the same pattern
  precedent set for a location's "Notable NPCs" section (Calveno lists
  named individuals tied to the place), I housed the three named
  planar-incursion entities there as the closest-fit skeleton heading
  rather than inventing a new heading. Flagging this explicitly per the
  `### Related`-convention precedent (Round 1 creature dispatch) — a
  future user/skill call if a dedicated "Notable Creatures" heading is
  ever wanted for plane/dungeon pages with monster inhabitants instead of
  NPCs.

- **Tag mapping.** Source tag: `drowned-maw` — an entity/location-identity
  tag (names the breach site, not a tone), dropped per WIKI.md § Tag
  taxonomy (same bucket as `tessarine`/`passage`/`dravosi` in prior
  lines) — no canonical or alias equivalent exists. Genuine Domain-tone
  content is source-stated, not invented: an undocumented, widening planar
  breach with an unexplained "far side" ("The full planar nature is not
  yet documented") and an active monster incursion (three planar predators
  crossing over) — mirrors the exact tonal shape of
  `world/lore/the-vault-of-the-first-factor.md` and
  `world/factions/sentinels-of-the-eyrie.md`, both tagged `[mystery,
  exploration]` for structurally identical undocumented/frontier content.
  Applied `mystery, exploration`. Final tag set: `mystery, exploration`.

- **Frontmatter fields with no contract home — dropped**: `campaign`,
  `audience`, `confidence_level`, `sources:`, `plane_type`, `banner`.
  `plane_type: elemental-plane` folds into prose ("one of the four
  elemental planes," already source-stated in the Overview). `access:
  breach through the Drowned Maw fissure` folds into a Player-Known Key
  Facts table (no `location`-specific `access` key in wiki-contract.md;
  `access` stays prose the same way Calveno's Key Facts table carries an
  `Access` row without a frontmatter key).

- **`created`/`touched: legacy`** — per this mission's explicit instruction
  and identical to every prior Round 1/2/3 line.

- **`publish: false`** — never set `true` (contract item 4 / PUBLISH's
  exclusive call), despite... actually source also states `publish:
  false` here, so no override needed — first line in this mission where
  the legacy value and the contract default already agree.

- **`aliases: []`** — source states no `aliases:` key at all (unlike
  `grimaldis-dispensary.md`'s "Grimaldi's"); left empty, no name variant
  stated in the text itself.
