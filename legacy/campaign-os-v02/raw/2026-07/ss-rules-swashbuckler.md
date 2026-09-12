# Source ingest queue: ss-rules-swashbuckler

Source root: /Users/nick/ai-os/shattered-sea/wiki/rules/subclasses/swashbuckler.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — `rules ::
rules/subclasses/swashbuckler.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:11 "REVIEWED-BY-HUMAN:
2026-07-13 — per the user's handoff mission (procedure item 4 verbatim):
'Migration-mode canon writes are the sanctioned bootstrap-and-audit exception
(progress.md REVIEW item 17) — pending user blessing was the old status; the
user's current instruction to ingest legacy canon IS that blessing for this
mission's scope.' Blessing covers exactly the 15 lines below, nothing else."
Started: 2026-07-13

WRITE PASS (2026-07-13): the gap flagged below is closed — `type: rule` now
exists (commit ed63957), skeleton `docs/campaign/skeletons/rule.md`
(Player-Known · DM Only · Mechanics · Provenance), `subtype: class | subclass |
background | condition | subsystem` now a governed enum value for the
`rule` type. Recommendation (b) from the `## Fit verdict` below was
accepted verbatim — item-shaped
skeleton, ported subtype. Page written: `world/rules/swashbuckler.md`,
`subtype: subclass`. All three claims below are now DONE.

**Status verdict (canon vs. pending):** `pending`. Source frontmatter
(`audience: dm`, `status: unknown`, `publish: false`) is uniform across all 27
files in `rules/subclasses/` — a bulk-exported reference-library default, not a
per-file revealed signal, unlike `campaign-overview.md`'s genuine
`audience: players` / `publish: true` session-zero-handout signal (→ canon).
`grep -ril "swashbuckler\|delmar" sessions/` returns no hits (`sessions/` has
no transcripts yet — L10: unsure whether revealed at the table means it
wasn't). The `delmar-fisk` NPC page this content would hang off doesn't exist
yet, and the one existing mention of him (`world/npcs/estratto.md`) is itself
`status: pending`. Same shape as the `syranita.md` precedent (DONE d13847c +
14fafec — pending, stub/inferred, never revealed), not the
`campaign-overview.md` one.

## Sources (batch order, smallest file first)

- [x] rules/subclasses/swashbuckler.md — triage: entity-source (mechanical rules
  reference), DONE — written to `world/rules/swashbuckler.md`

## Claims — rules/subclasses/swashbuckler.md

- [x] identity/summary :: Swashbuckler :: `world/rules/swashbuckler.md` ##
  Player-Known — Rogue subclass, Xanathar's Guide to Everything (2014),
  CHA-based duelist/pirate archetype (%%src: legacy%%)
- [x] mechanics (5 leveled features) :: Swashbuckler ::
  `world/rules/swashbuckler.md` ## Mechanics — Fancy Footwork (L3, no OA after
  melee strike), Rakish Audacity (L3, CHA-to-Initiative + no-ally-needed Sneak
  Attack), Panache (L9, CHA(Persuasion) vs WIS(Insight) contest with
  hostile/non-hostile branches), Elegant Maneuver (L13, bonus-action Advantage
  on Acrobatics/Athletics), Master Duelist (L17, reroll a missed attack 1/SR or
  LR), each labeled [RAW, Xanathar's Guide to Everything (2014)]
  (%%src: legacy%%)
- [x] relationship fact :: "Delmar Fisk is a Swashbuckler Rogue" ::
  `world/rules/swashbuckler.md` ## DM Only — stub check
  (`grep -ril "delmar" world/ pcs/ prep/`) found no `delmar-fisk` NPC page
  (only an incidental mention inside `world/npcs/estratto.md`); no ledger line
  in this migration batch names Delmar Fisk. Per migration-mode link deferral:
  written as plain text, `relink: delmar-fisk — once his NPC page lands`, no
  `[[delmar-fisk]]` wikilink yet.

## Fit verdict

**Recommendation: (b), precedented — add a new `rule` type, modeled on the
`item` skeleton's shape (Player-Known · DM Only · Mechanics · Provenance), not
on `lore`'s (Player-Known · DM Only · Sources). Do not default the 103-file
`rules/` pile to `lore`-as-is.**

This is the opposite conclusion from the sibling `ss-deity-syranita.md` verdict
(which correctly kept a thin, inert deity stub on `lore`) — flagged there
(Flag 3) as "this verdict pattern likely generalizes to swashbuckler." It does
not: the deity file had zero mechanical content and a clean 1:1 fit for lore's
three headings; this file is dense, leveled, mechanical reference content that
lore has no heading for. Judging this file on its own facts, not on that
precedent:

1. **This is RAW, not homebrew — the claim-buckets row that authorizes `lore`
   doesn't actually name this content.** `source-ingest`'s own claim-buckets
   table (`.claude/skills/source-ingest/references/claim-buckets.md:64`) routes
   "Homebrew rule/ruling" → `lore`, flagged as an approximation. Swashbuckler's
   frontmatter cites `Xanathar's Guide to Everything (2014)` — official WotC
   content, not a DM ruling or house rule. I checked all 27 files in
   `rules/subclasses/` and all cite official books (PHB 2024, Tasha's, XGtE,
   Forgotten Realms sourcebooks) with zero `Homebrew` sources among them; the
   same is true of `classes/`, `backgrounds/`, `conditions/` by frontmatter
   sampling. The lore-as-approximation escape hatch was written for homebrew
   content and is being asked to also carry ~75 files of official rules
   reference it was never scoped for.

2. **Lore's DM Only heading is meaningless for this content — it would sit
   empty or get abused as a dumping ground.** `lore`'s shape (Player-Known /
   DM Only / Sources) earns its keep on content that splits into "what the
   table has learned" vs. "secret plot facts the DM is holding back"
   (wiki-contract.md:67-73). A subclass writeup has no secrets: every one of
   Fancy Footwork/Rakish Audacity/Panache/Elegant Maneuver/Master Duelist is
   public player-facing mechanical text the player reads directly off a class
   feature. Forcing it under `lore` means either (a) DM Only sits empty on
   ~75 pages (a heading the wiki contract requires present regardless of
   whether the page has real content for it), or (b) writers start using
   DM Only for "balance
   notes/DM rulings on this feature," which is legitimate content but has
   nowhere else to go under lore's 3 headings and blurs the line lore draws
   for every other page type.

3. **`item` already solved this exact problem — reuse its shape instead of
   inventing a new one.** `wiki-contract.md:34-38` states explicitly:
   "Item type (weapon/armor/wondrous/etc.) and whether it's homebrew stay out
   of frontmatter — the Player-Known stat line and the `[HB]`/`[RAW]` mechanic
   labels already carry that." `item`'s skeleton is Player-Known · DM Only ·
   Mechanics · Provenance (`docs/campaign/skeletons/item.md`). That is a
   near-exact structural match for a
   rules page: Player-Known = short-summary/fluff (this file's own opening
   paragraph), Mechanics = the 5 leveled features (with `[RAW]`/`[HB]` labels
   per feature — this file is uniformly `[RAW]`; a subsystems-directory
   homebrew page like `ship-combat.md` would be uniformly `[HB]`), Provenance
   = source book + edition (`Xanathar's Guide to Everything (2014)`), DM Only
   = optional balance/table-specific ruling notes when a DM has one. A new
   `rule` type inheriting this shape, not lore's, is the smaller schema
   addition (copy an existing precedent) and the more honest one (it doesn't
   pretend mechanical content is narrative content).

4. **Type-greppability breaks under `lore`, and the pile is big enough that
   this matters.** wiki-contract.md's stated design goal (line 4) is "a
   database a weak model can query with grep and trust." Folding this file
   under `type: lore` merges it with genuine narrative worldbuilding
   (`world/lore/campaign-overview.md`, deity stubs, etc.) — `grep "^type:
   lore$"` across a fully-migrated `rules/` tree stops answering "what
   subclasses/classes/conditions exist" or "what house rules are we running"
   at all; a DM has to fall back to prose/tag scanning across ~97 lore pages
   for a `rules`-shaped question, which is exactly the failure mode
   wiki-contract.md's type field exists to prevent. `type: rule` (or
   `type: rules`, naming judgment call for whoever executes) restores that
   query directly, the same way `type: item`/`type: quest` do for their
   domains.

5. **The pile is genuinely heterogeneous, not uniform — a `subtype` key
   pays for itself the way `location`'s does.** I sampled sources across all
   7 subdirectories: `subclasses/` (27), `classes/` (14), `backgrounds/` (18),
   `conditions/` (16) are ~100% official-book RAW (75 files, no DM-secret
   content). `subsystems/` (14) and `core/` (5) are a real mix — some official
   (`bastions.md`, `carpenters-shop.md`: DMG 2024) and some genuinely homebrew
   or third-party-adapted (`ship-combat.md`, `ship-mechanics.md`,
   `ship-operations.md`, `ship-stats.md`, `ship-upgrades.md`,
   `surgeons-berth.md`, `mortis.md`: `sources: [Homebrew]`; `core/*.md`:
   sourced from Pointy Hat YouTube / rpgbot.net third-party guides, not WotC).
   The source's own `subtype:` frontmatter key (present on all 103 files:
   `class`/`subclass`/`background`/`condition`/`subsystem`/`facility`/`rule`)
   already tracks this split. Recommend porting it as a governed `subtype`
   enum for the `rule` type, same precedent as `location`'s
   `subtype: region | island | settlement | ...` enum:
   `class | subclass | background | condition | subsystem`. This directly
   answers the "what house rules exist" query the ledger line's own framing
   raised: `grep "^subtype: subsystem$" world/rules/*.md` (or similar) plus a
   scan for `[HB]` in Mechanics gets there; `type: lore` cannot.

6. **What breaks if `lore`-as-is ships anyway, concretely:** (a) the schema
   still validates cleanly — heading-presence and enum checks catch a
   missing section or a bad value, not a wrong type-category choice, so
   this is a silent, not a loud, failure, meaning the wrong call here
   doesn't self-correct on its own; (b) publish review gets harder,
   not easier — a future publish pass over `type: lore` pages has to
   re-distinguish "DM narrative fiction, safe once DM Only is stripped" from
   "near-verbatim reproduction of WotC's own published feature text," a
   copyright-adjacent distinction lore's reviewers aren't primed to make,
   where a dedicated `rule` type could carry that flag explicitly (e.g. a
   `Provenance` note "reproduces XGtE p.X wording — publish review required");
   (c) the `[HB]`/`[RAW]` convention wiki-contract.md already names for
   exactly this canon-vs-homebrew problem has no heading to live on under
   lore, so 19+ homebrew subsystem/core files lose the one piece of metadata
   a DM most needs when skimming ("is this rule actually house-ruled or is it
   RAW").

**Cost surface if (b) is accepted** (not executed here — probe only): (i)
`wiki-contract.md`'s type enum line 12 gains `rule`; (ii) new
`docs/campaign/skeletons/rule.md` copying `item.md`'s 4-heading shape and
carrying the `rule` type's governed `subtype` enum (`class | subclass |
background | condition | subsystem`); (iii) `WIKI.md`'s tag-taxonomy /
type-list documentation gets the new type added wherever the 9-type enum is
restated. All three are small, bounded, single-file edits — not a rearchitect —
but they are cross-cutting contract changes outside this dispatch's owned path
(`archive/2026-07/` only) and outside a single-file triage probe's
mandate. This is the decision input the handoff's "house-rules home:
undecided" line asked for; building the type is a separate, human-approved
step.

## Flags

1. **Delmar Fisk relink pending.** Written to `world/rules/swashbuckler.md` ##
   DM Only as plain text, no `[[delmar-fisk]]` wikilink. Still no `delmar-fisk`
   NPC page and no ledger line in this batch creates one — carries forward to
   the orchestrator's link-restoration pass per `relink: delmar-fisk — once his
   NPC page lands`. **Resolved ✓ (link-pass R6, 2026-07-14):** `pcs/delmar-fisk.md`
   landed (canon, R5); swashbuckler.md now links `[[delmar-fisk|Delmar Fisk]]`.
2. **This verdict disagrees with the precedent flagged in
   `ss-deity-syranita.md` Flag 3** ("this verdict pattern likely generalizes
   to swashbuckler"). It doesn't — the two source files have materially
   different content shapes (inert narrative stub vs. dense leveled mechanics)
   and the claim-buckets `lore`-approximation row was written for homebrew
   content, which this file is not. Noting the disagreement explicitly so the
   orchestrator doesn't silently average the two verdicts.
3. **This verdict is scoped to `rules/subclasses/` and the official-content
   majority of the 103-file pile.** The `subsystems/`/`core/` homebrew minority
   (~19 files) still fits a `rule` type (via `subtype: subsystem` +
   `[HB]` labels) but was not itself the subject of this dispatch — sampled
   only for the heterogeneity argument in point 5 above, not fully triaged.
4. **Naming judgment call resolved:** `type: rule` (singular) was the value
   actually shipped (commit ed63957) in `docs/campaign/skeletons/rule.md`
   and the wiki contract's type enum — used as-is, matching the
   source's own `subtype: subclass` frontmatter key verbatim.
5. **Lint clean, no NOTED items.** Exit 0, zero WIKI-LINT blocks. No
   two-failed-fix loop triggered (Hard Rule 6 not invoked).
6. **Status verdict: `pending`, not `canon`.** See the "WRITE PASS" status
   verdict note above the claims list — source's `audience: dm` signal is a
   library-wide default (all 27 `rules/subclasses/*.md` files carry it
   identically), not evidence this specific content was ever used at this
   table; no session transcripts exist yet to confirm otherwise.
