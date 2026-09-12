# Source ingest queue: ss2-situation-sentinels-head

Source root: /Users/nick/ai-os/shattered-sea/wiki/situations/dormant/sentinels-true-head.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — `situation ::
situations/dormant/sentinels-true-head.md → absorb into
world/factions/sentinels-of-the-eyrie.md (## Goals & Fronts identity facts + DM
Only, NO invented clocks) — sanctioned canon-page expand via this unchecked line
(canon_gate migration exception)`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:41 "REVIEWED-BY-HUMAN:
2026-07-13 — user instruction \"implement all your recommended fixes, then
proceed to round two\". Blessing covers exactly the 13 lines below." Round-2
line at MIGRATION-LEDGER.md:57. canon_gate.py exit 0 (unchecked ledger line
names the target path).
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] situations/dormant/sentinels-true-head.md — triage: faction-source (a
  pressure/situation with a real owning faction, Sentinels of the Eyrie),
  ready — owning faction page exists at `status: canon` (round-1 landed it)

## Claims — situations/dormant/sentinels-true-head.md

- [x] situation :: Who Is the True Head of the Sentinels :: world/factions/
  sentinels-of-the-eyrie.md (expand — `## DM Only` + `## Goals & Fronts` +
  `## Members`) — Soul Incarnate identity, motive, and observation-record
  detail; Master Kyzil added as a named member; Front identity written
  (`### Front: The Soul Incarnate's Watch`, Lifecycle: dormant), NO Clock/
  Trigger conditions/Consequence-at-fill (Hard Rule 4 — source states none
  of these verbatim) (%%src: legacy%%)

## Flags

1. **Reconciliation, not duplication (L6).** The target page's `## DM Only`
   already carried a one-paragraph flag from the round-1 faction ingest:
   "the order's 200-year record is kept by a Soul Incarnate sealed beneath
   High Eyrie — the Sentinels' true head is not their visible leadership...
   Flagged in the queue file for faction-prep if the DM wants a working
   Front built from it." That paragraph was left untouched (existing canon
   prose, not this ledger line's to rewrite) and this source's much richer
   material — the Soul Incarnate's nature (neutral lich, monk variety, no
   allegiances), Master Kyzil's ignorance of it, the two-centuries record
   pattern, the Auralis-blind-spot detail, Crissdalynn's pilgrimage as the
   connecting thread, and the at-table reveal framing — was appended as new
   paragraphs directly after it, not restated as a second version of the
   same claim. No contradiction was found between the two: the source is
   exactly what the round-1 flag predicted it would be (the identity behind
   the flagged secret), so this is elaboration, not conflict — no
   CONTRADICTION block needed.

2. **Front written, Clock omitted (Hard Rule 4).** The source states a
   `Lifecycle: dormant` situation with a `Pressures` section and an `If
   Ignored` section, but no segment count, no named trigger condition with
   a specific advance-per-event rule, and no single observable/irreversible
   consequence-at-fill — "the Maw crisis escalates" is prose stakes, not a
   tick-test-passing consequence. Per SKILL.md Hard Rule 4 and
   claim-buckets.md's "Faction pressure without stated trigger/consequence"
   row: wrote `### Front: The Soul Incarnate's Watch` with Lifecycle,
   Primary goal, Consistent method, Off-screen move (drawn near-verbatim
   from the source's own "If Ignored" section, which the source DOES
   state), and PC connection — all identity, no Clock/Trigger
   conditions/Consequence-at-fill line. Explicitly flagged in the Front
   block itself, routing to `faction-prep` if the DM wants a working clock
   built from this identity.

3. **`dormant` lifecycle mapped cleanly.** Source frontmatter
   `status: dormant` / `lifecycle: dormant` maps 1:1 onto the Front
   template's own `**Lifecycle:** dormant` enum value
   (`.claude/skills/faction-prep/SKILL.md` Front template) — same clean
   mapping the round-1 `ss-situation-draves` queue file worked out on paper
   but couldn't use (no Front existed there to attach it to). Here it
   attaches directly.

4. **Unresolved wikilinks — written as plain text, not `[[wikilinks]]`.**
   Source links to seven other entities, none of which are among the 10
   pages confirmed to exist in campaign-os `world/` this wave (estratto,
   calveno, preserved-eel, sentinels-of-the-eyrie, campaign-overview,
   grung, syranita, gentle-hag, swashbuckler, vethka) or listed in
   `world/_meta/aliases.md`:
   - `soul-incarnate` (creature entry) — relinked ✓ — `world/creatures/
     soul-incarnate.md` landed; six "Soul Incarnate" mentions across DM Only,
     Members, and Goals & Fronts on `world/factions/sentinels-of-the-eyrie.md`
     now link `[[soul-incarnate|Soul Incarnate]]` (one per paragraph/block,
     the section heading itself left unlinked) (link-restoration pass R4,
     2026-07-14)
   - `high-eyrie` (location) — `relink: high-eyrie — once its page lands`
     (same open flag as the round-1 `ss-faction-sentinels` queue file)
   - `master-kyzil` (NPC — now also named in `## Members`, still no page) —
     `relink: master-kyzil — once its page lands`
   - `crissdalynn-khinriss` (confirmed PC per round-1 flag, out of this
     skill's owned paths) — `relink: crissdalynn-khinriss — once a pcs/
     page exists for her`
   - `crissdalynns-pilgrimage` (situation/quest-shaped, no page type
     confirmed) — `relink: crissdalynns-pilgrimage — once its page lands`
   - `auralis` (entity, unclear type from this source alone) — `relink:
     auralis — once its page lands`
   - `pearl-of-souls` (item, named once in source's own Connections list,
     not used in any absorbed prose — no claim written for it, no relink
     needed unless a future source states more)

5. **No tag changes.** This is a canon-page *expansion*, not a new page —
   `faction_status: active` and the existing `tags: [mystery, exploration]`
   already fit this material (undead-continuity mystery, still no new
   Domain tag needed); frontmatter left untouched per rails item 4.

6. **Frontmatter untouched, including `touched:`.** Rails item 4 says leave
   the canon page's frontmatter untouched except nothing, and log here if
   `touched` arguably should change from `legacy` — it does, in the sense
   that this is a live 2026-07-13 edit, not the original legacy migration
   write. Left as `legacy` per explicit instruction; flagging for the
   orchestrator/DM in case a future convention wants `touched` bumped on
   migration-exception expansions distinct from the original migration
   write.
