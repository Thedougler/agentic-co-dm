# Source ingest queue: ss-island-port-tidefall

Source root: /Users/nick/ai-os/shattered-sea/wiki/narrative-islands/port-tidefall-dockfront.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md:36 — `narrative-island ::
narrative-islands/port-tidefall-dockfront.md → relocate to the U8 narrative-island home
(prep-side scene grouping) — agent verifies the home exists before writing`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:11 "REVIEWED-BY-HUMAN:
2026-07-13 — per the user's handoff mission (procedure item 4 verbatim)..."
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] narrative-islands/port-tidefall-dockfront.md — triage: narrative-island
  (cross-entity scene cluster: 8 sub-locations, 6 named NPCs, prices, DC
  sequences, hooks, all under one "Port Tidefall dockfront" premise), **blocked
  — U8 home exists but does not fit this file as a relocation target** (see
  Flags)

## Claims — narrative-islands/port-tidefall-dockfront.md

- none written. Per Flags below, the U8 home is not a page-type destination
  a file can be relocated into; no claim was decomposed onto world/ or
  prep/ pages.

## Flags

1. **The U8 home was found and read in full, and it does not fit this file's
   disposition ("relocate").** Location:
   `.claude/skills/session-run-guide/references/scene-cards.md` § "Scene
   groupings (absorbed from prep-island — REVIEW item 12)" (built by commits
   `72a6b82` + `95836b9`). Quoting the home's own text: a grouping is "**a
   shared Thread Name across scene cards**, nothing more" — not a new page
   type or frontmatter block. `entry_points:` maps onto the group's cards'
   own `Available:` lines; `contains_situations:`/`linked_islands:` maps onto
   ordinary `Hook out:` lines. Critically: "**Durable beyond tonight →
   Portability above, not this section.** If the cluster's premise should
   survive whether or not the party engages it tonight, its content belongs
   on the owning entity's page... per Portability. A grouping label is scoped
   to *this run guide* only — **never a standalone artifact the next PREP
   cycle has to rediscover.**"

   The `session-run-guide` build's own design intent states this
   even more directly: "the concept is prep/run-time scene organization,
   **not a durable wiki fact needing its own page**." A Thread Name only
   exists *inside* an actual `session-run-guide` scene-card set, authored
   live during PREP for a specific upcoming session. There is no queue,
   holding page, or "future island" artifact the U8 mechanism offers to
   relocate a file into — it is generated fresh, per session, from cards that
   already exist for that session.

   `port-tidefall-dockfront.md` is exactly the case the home's own rule
   excludes: `status: active`, no session attached, sourced from a standing
   `Inbox/Port-Tidefall.md` note, `updated: 2026-06-06` — durable prep
   content that has not yet survived contact with the table (contract item
   9) and is not tied to any specific upcoming session's card set. By the
   home's own stated rule, this content does not get "relocated" as a
   grouping; it gets decomposed onto the owning entities' pages (location
   Hooks, faction Fronts, quest Beats, NPC DM-Only sections) — the same
   claim-bucket decomposition this skill already applies to every other
   source type. There is nowhere to "relocate" this .md file *to* under U8.

2. **A second, older doc in the same skill gives a different — and stale —
   answer, never reconciled with U8.** `references/claim-buckets.md` § Source
   types (source-ingest's own reference file, last touched in commit `8fea0bb`
   at 2026-07-13 20:22:38, i.e. **before** U8 landed at 21:32:04 the same day)
   says: "Portable scenario cluster ('island') → Same page-tree treatment as
   a multi-part settlement — No `island` type exists either — reuse the
   location-tree pattern rather than inventing a type." This predates and
   was never updated to point at the U8 resolution — it is the pre-U8 answer
   to the exact question U8 later settled differently (U8: fold into owning
   entities' existing fields per Portability; claim-buckets.md: build a new
   location page-tree). The two prescriptions don't actually contradict on
   the *destination* (both ultimately say "the owning entity's page/tree,
   not a new type") but claim-buckets.md's phrasing ("reuse the location-tree
   pattern") reads as license to originate a brand-new `Port Tidefall`
   parent-location page tree from this one file, which the migration-mode
   owned-paths restriction does not authorize here (this ledger line names
   only the one source file, not a license to originate new location
   entities un-requested by any ledger line). NOTED (not done): reconcile
   claim-buckets.md's island row to point at scene-cards.md § Scene groupings
   instead of restating the pre-U8 location-tree answer — flagging for the
   DM/orchestrator, not this single-file agent's call to edit a shared skill
   reference file.

3. **Decomposition was checked and is not currently possible without
   originating new pages this ledger line doesn't authorize.** Stub-checked
   every named entity in the source (`port-tidefall`, `delmar`, `perrin`,
   `jean-claude`, `vrtek`, `maret`, `waveservant`, `chandlery`, `tessarine`,
   `fort-crestwall`, `governors-seat`, `surety-missing`, `umberlees-message`,
   `margaret-porcelain`) against `world/`, `pcs/`, `prep/`. Only
   `world/npcs/estratto.md`, `world/lore/campaign-overview.md`, and
   `world/lore/grung.md` matched, all coincidentally (Tessarine and
   Waveservant appear in `campaign-overview.md`'s general lore, not as
   entity pages; the "jean-claude" hit is `grung.md`, unrelated). No location,
   NPC, or faction page exists yet for Port Tidefall or any of its
   sub-locations/NPCs. Per claim-buckets.md's own "Location... a multi-part
   settlement becomes a page tree — parent + child location stubs" guidance,
   the *parent* Port Tidefall location page does not exist to hang children
   off of, and originating it is a different, not-yet-dispatched ledger line
   (this migration's other lines each own exactly one source file — no line
   in `MIGRATION-LEDGER.md` requests a fresh `location :: Port Tidefall`
   page). Writing one here would exceed migration mode's owned-paths
   restriction ("only the specific file(s) named on the ledger line being
   executed" — source-ingest SKILL.md § Owned paths).

4. **Verdict: home exists, does not fit as a relocation target, nothing
   written.** Per this task's own instruction ("If the home turns out not to
   exist or not to fit this file, STOP and report precisely"), stopping here
   rather than forcing either (a) a literal relocation into U8 (impossible —
   U8 isn't a page destination) or (b) an unrequested new Port Tidefall page
   tree (exceeds this ledger line's owned-paths scope). Recommends to the
   DM/orchestrator: either (i) dispatch a fresh `location :: Port Tidefall`
   ledger line first, then re-run this file's claims against that parent
   page plus per-claim location/NPC/item child stubs, decomposed the normal
   claim-bucket way (not as a "grouping"); or (ii) leave this source
   unmigrated until an actual session is being run-guided for Port Tidefall's
   dockfront, at which point `session-run-guide` authors its own scene cards
   fresh from this legacy file as raw reference material (not a relocation),
   per U8's "never a standalone artifact the next PREP cycle has to
   rediscover."

5. **Reciprocal-link deferral N/A.** Nothing was written to `world/`, `pcs/`,
   or `prep/`, so there is no page to carry `relink:` flags. All entity names
   above remain unlinked in this queue file only (plain text, no
   `[[wikilink]]`), consistent with migration-mode link deferral even though
   no page exists to defer *from*.
