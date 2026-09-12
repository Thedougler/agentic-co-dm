# Source ingest queue: ss-deity-syranita

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/deities/syranita.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — `deity :: entities/deities/syranita.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:11 "REVIEWED-BY-HUMAN: 2026-07-13 — per the user's handoff mission..."
Started: 2026-07-13

WRITE PASS (2026-07-13): fit verdict `(a) lore-as-is` accepted by the orchestrator.
Page written at `world/lore/syranita.md` per the lore skeleton. Both claims below are
unblocked and executed.

## Sources (batch order, smallest file first)

- [x] entities/deities/syranita.md — triage: entity-source, written as lore approximation per accepted fit verdict

## Claims — entities/deities/syranita.md

- [x] lore :: Syranita :: world/lore/syranita.md (new) — deity identity: aarakocra sky-pantheon, secondary/marginal-observance status, cross-refs to Remnis (primary) and Aerdrie Faenya (tertiary), plain text (no wikilinks — neither sibling migrated) (%%src: legacy%%). Landed `status: pending` (never revealed at the table — estratto precedent), not the ledger's default `canon`.
- [x] relationship fact :: "Crissdalynn has marginal observance of Syranita" — written as plain text in `world/lore/syranita.md` § DM Only (no `crissdalynn-khinriss` NPC page exists yet). `relink: crissdalynn-khinriss — once her NPC page lands` flag carried onto the page and restated below.

## Fit verdict

**Recommendation: (a) lore-as-is — no new `deity` type warranted by this file.**

Evidence, from THIS file's actual content (`entities/deities/syranita.md`, 598 bytes,
14-line frontmatter + 3-sentence body):

1. **Zero governed/mechanical data to key.** The wiki-contract.md type enum is
   `npc | location | faction | quest | item | lore | pc | session | encounter`
   (wiki-contract.md:12) — no `deity` member. A new `deity` type would earn its
   keep by carrying governed fields analogous to `npc`'s `location` or `item`'s
   `rarity`/`attunement`. Syranita's source has no domain, symbol, alignment, or
   any other structured field — not even in prose. Compare the sibling deity
   files I read for calibration (`remnis.md`, `aerdrie-faenya.md`,
   `tyr.md`, `umberlee.md`, `valkur.md`, all in the same source directory):
   none of the six use frontmatter-level domain/symbol/alignment keys either —
   where that information appears at all (Tyr: "Lawful Good god of law,
   justice..."; Valkur: "Chaotic Good minor deity of sailors...") it's prose
   inside `summary:` or the body, not a governed key. Inventing
   `domains:`/`symbol:`/`alignment:` frontmatter for a new type would mean
   the schema is aspirational, not fidelity-derived from what the source
   corpus actually populates — a Hard Rule 1 risk across the batch, not just
   this file.
2. **No active-NPC behavior in this file.** wiki-contract.md's `npc` skeleton
   (Player-Known · DM Only · Stats & Combat · Relationships · Appearances)
   earns its shape because NPCs act, fight, and get referenced across
   sessions. Syranita never acts — the entire body is "Aarakocra deity.
   Marginal observance by Crissdalynn... See also Remnis (primary) and
   Aerdrie Faenya." No statblock, no location, no independent agenda. (Note:
   `umberlee.md`, a sibling *not* on this ledger line, DOES read as
   NPC/faction-adjacent — active clergy, a Campaign Secret, Legendary Assets,
   an open plot thread. That file might argue differently if it were ever
   migrated. It isn't this file, and generalizing from a richer sibling to
   this thin stub would be exactly the kind of invented-detail overreach
   Hard Rule 1 forbids.)
3. **Content shape is a clean 1:1 fit for `lore`'s three headings.**
   Player-Known: empty — source's own `status: stub`, `confidence_level:
   inferred`, `publish: false`, and lack of any Session Events/appearance
   record all agree nothing has been revealed at the table. DM Only: the
   entire body (aarakocra sky-pantheon placement, marginal-observance
   framing, cross-references). Sources: `Inbox/Crissdalynn-Khinriss.md`
   (%%src: legacy%%). No forcing, no left-over content, no stub note needed
   beyond what the source already flags as thin (`needs-detail` tag).
4. **Findability check ("would a DM grepping 'what gods exist' be served?").**
   `world/_meta/tags.md`'s canonical taxonomy is Domain-tone (intrigue, heist,
   horror, mystery...) and Project-arc, not entity-subtype — a `deity` tag
   would not fit either canonical category, and forcing one in would be the
   same category error the tags.md Rules section already guards against
   ("prefer an existing canonical tag over adding a new one"). Recommend
   instead the convention the source already uses organically: every source
   deity file's `summary:`/body states "deity" in the first sentence, making
   `grep -ril "deity" world/lore/` effective without any schema change. This
   is a documentation convention to carry forward at write time, not a
   registry/taxonomy edit — flagged for whoever executes the write.
5. **Precedent check against the encounter-type promotion (REVIEW item 13).**
   Encounters got their own type because they had a genuinely distinct,
   *consistent* mechanical shape (Enemy Roster, Challenge Calibration,
   Terrain, Tactical Notes...) that recurred across many source instances and
   didn't fit any existing skeleton. Deities, by contrast, show inconsistent
   per-file shape even among the six siblings I read (Umberlee has "Domain &
   Limits"/"Legendary Assets"/"Theological Tensions"; Tyr has "In the
   Scatter"; Valkur has none of those) — free-form prose headings, not a
   repeating governed schema. That inconsistency is itself evidence against
   a `deity` type: there is no fixed key set to promote.

**If this verdict is accepted**, unblocking claim 1 is a normal `lore`
skeleton instantiation (`docs/campaign/skeletons/lore.md`) with the body content
above under DM Only, `%%src: legacy%%`, `status: canon` per the ledger's stated
legacy-canon disposition default (subject to the same canon-vs-pending check
`ss-npc-estratto.md` Flag 1 raised — this deity has also never been revealed at
the table per its own `status: stub`/no Session Events equivalent, so the same
override to `status: pending` likely applies; left for the write-executing agent
to confirm, not decided here since this dispatch does not write).

## Flags

1. **Claim 2 (Crissdalynn relationship fact) has no page to land on.**
   `crissdalynn-khinriss` is not an NPC page in `world/npcs/` yet (stub check:
   `grep -ril "crissdalynn" world/ pcs/ prep/` → no hits) and no ledger line in
   this migration batch names her. Per source-ingest's migration-mode link
   deferral: do not create her stub from this dispatch. If/when Syranita's
   lore page is written, the Crissdalynn mention goes in as plain text, and
   `relink: crissdalynn-khinriss — once her NPC page lands` is the flag to
   carry forward on that page. **Resolved ✓ (link-pass R6, 2026-07-14):**
   `pcs/crissdalynn-khinriss.md` landed (canon, R5); syranita.md now links
   `[[crissdalynn-khinriss|Crissdalynn Khinriss]]`.
2. **Sibling deity cross-refs (`remnis`, `aerdrie-faenya`) are also unmigrated.**
   Same deferral as Flag 1 — plain text, not wikilinks, if/when written.
3. **This verdict pattern likely generalizes to the sibling `rules ::
   rules/subclasses/swashbuckler.md` ledger line** (MIGRATION-LEDGER.md:33,
   which pre-emptively notes "source-ingest itself flags lore as
   approximation") — not acted on here, out of this dispatch's one-file scope,
   noted for whoever executes that line.
4. **Write pass closure (2026-07-13):** Flags 1-2 executed as specified —
   `world/lore/syranita.md` § DM Only carries both Crissdalynn and the
   Remnis/Aerdrie Faenya cross-refs as plain text with the `relink:` note
   inline. Flag 3 remains open, unchanged, for whoever executes the
   `swashbuckler.md` ledger line.
