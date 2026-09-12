# Source ingest queue: ss-location-calveno

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/places/settlements/calveno/calveno-reference.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — `location :: entities/places/settlements/calveno/calveno-reference.md → restructure → world/locations/ — status: canon; subtype per contract enum`)
Started: 2026-07-13

Gate proof (docs/campaign/MIGRATION-LEDGER.md):

```text
11:REVIEWED-BY-HUMAN: 2026-07-13 — per the user's handoff mission (procedure item 4
25:- [ ] location :: entities/places/settlements/calveno/calveno-reference.md → restructure → world/locations/ — status: canon; subtype per contract enum
```

## Sources (batch order, smallest file first)

- [x] entities/places/settlements/calveno/calveno-reference.md — triage: location, ready (unblocked by contract patch, commit 90aaace)

## Claims — entities/places/settlements/calveno/calveno-reference.md

- [x] location :: Calveno :: world/locations/calveno.md (new) — subtype: settlement, status: canon. Player-Known districts/access/power table, DM Only none stated, Notable NPCs (Iacopo Fieschi, Nona Black-Jaw, Catarina Da'Virelli, Anzolo), Hooks (Rattkin Warren beneath Le Paludi, the Passage anchor point). Lint: clean, exit 0. (%%src: legacy%%)

## Flags

- **RESOLVED — subtype enum patched.** Was BLOCKED: wiki-contract.md's
  `location` subtype enum (`region | island | building | dungeon | plane`)
  had no honest fit for a multi-district settlement/city. Commit 90aaace
  patched the enum to `region | island | settlement | district | building |
  dungeon | plane`, adding `settlement` (city-builder's tree root) and
  `district` (child page within a settlement tree). `world/locations/
  calveno.md` written with `subtype: settlement` — the honest fit this flag
  originally found missing. Unblocked and ingested 2026-07-13.
- **Tag substitution flag.** Legacy tags `tessarine`, `passage` have no
  canonical or aliased match in `world/_meta/tags.md` (canonical set:
  intrigue, heist, horror, mystery, exploration, war, politics, romance;
  alias list empty — confirmed by re-read at ingest time). Mapped to nearest
  canonical tags instead: `politics` (Council seats, hereditary debt
  leverage as civic power) and `intrigue` (privacy-for-sale, hidden Rattkin
  infrastructure beneath the visible city). Neither legacy tag added to the
  taxonomy — flagging the substitution per rail 4 rather than silently
  dropping the tessarine/passage flavor.
- **Estratto / campaign-overview link-upgrade check — not applicable.**
  `world/npcs/estratto.md` and `world/lore/campaign-overview.md` now exist
  and both mention "Calveno" in plain text, but the *source file being
  ingested here* (calveno-reference.md) never names Estratto or references
  campaign-overview-level facts — grepped, zero hits. No real wikilink to
  create from this claim. (The reverse direction — updating estratto.md /
  campaign-overview.md's plain-text "Calveno" mentions into `[[calveno]]`
  links now that this page exists — is out of this ledger line's owned
  paths; NOTED (not done), not this task's file to touch.)
  **Resolved by the link-restoration pass (2026-07-13):** all plain-text
  "Calveno" mentions in `world/npcs/estratto.md` (3) and
  `world/lore/campaign-overview.md` (3) now link `[[calveno|Calveno]]` — see
  those files' own queue entries (`ss-npc-estratto.md`,
  `ss-lore-campaign-overview.md`).
- relink: iacopo-fieschi — once its page lands (source links `[[iacopo-fieschi]]`, not created here per migration-mode link deferral)
- relink: nona-black-jaw — resolved ✓ (promoted to standalone page, commit 677cd6c; link already live pre-R6)
- relink: catarina-davirelli — resolved ✓ (link-pass R6, 2026-07-14)
- relink: anzolo — once its page lands
- relink: tessarine-concordat — once its page lands
- relink: le-paludi — once its page lands
- relink: warren — resolved ✓ (link-pass R6, 2026-07-14)
- relink: the-passage — once its page lands
- relink: kats-curios — once its page lands
- relink: calveno-locations — once its page lands (index page, source's own "See Also")
- Legacy tags `tessarine`, `passage` have no canonical or aliased match in
  `world/_meta/tags.md` (canonical set: intrigue, heist, horror, mystery,
  exploration, war, politics, romance; alias list empty). Would need mapping
  or a taxonomy addition once the subtype block clears — not resolved here
  since no page was written.
- `confidence_level: confirmed` in the legacy frontmatter (not a
  wiki-contract.md key) supports `status: canon` — applied:
  `world/locations/calveno.md` written with `status: canon` on that basis.
  Legacy schema itself asserted this was settled, not speculative, content.
