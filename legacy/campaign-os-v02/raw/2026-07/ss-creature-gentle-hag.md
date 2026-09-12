# Source ingest queue: ss-creature-gentle-hag

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/creatures/background/gentle-hag.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md:28 — `creature ::
entities/creatures/background/gentle-hag.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:11 "REVIEWED-BY-HUMAN:
2026-07-13 — per the user's handoff mission (procedure item 4..."
Started: 2026-07-13

RE-DISPATCH EXECUTED 2026-07-13: the gap this queue file's Gap verdict flagged is
closed — `type: creature` landed in commit ed63957 (wiki-contract.md:12,108-111;
`docs/campaign/skeletons/creature.md` + `.claude/skills/campaign-os/assets/
skeletons/creature.md`; its skeleton-heading entry registered for the new
type), choosing this queue file's verdict (a) (dedicated type) over verdict (b) (lore
approximation) — the commit message cites the 135-file bestiary volume in the
source repo as clearing the promotion bar item 4 asked about. This dispatch
executed the write against that patched skeleton.

## Sources (batch order, smallest file first)

- [x] entities/creatures/background/gentle-hag.md — triage: entity-source
      (creature-shaped; skeleton gap now closed) — written to
      `world/creatures/gentle-hag.md`, `type: creature`

## Claims — entities/creatures/background/gentle-hag.md

- [x] creature identity + full statblock :: Gentle Hag :: `world/creatures/
      gentle-hag.md` § Stats & Combat — CR 7 fey, AC 16, HP 102 (12d8+48), Fey
      Clarity / Persistent Charm / Joyous Loyalty / Magic Resistance traits,
      CHA-based spellcasting (Command, Guiding Bolt, Sleep at will; Blur/Hold
      Person/Misty Step/Suggestion 3/day; Counterspell/Slow 2/day), 4 actions
      (Painful Glamor, Gentle Charm, Gentle Push, Summon Happiness), inside the
      ```statblock``` fence per the estratto.md:118-173 precedent (%%src: legacy%%)
- [x] coven actions :: Gentle Hag (requires 2 other hags within 30 ft.) ::
      `world/creatures/gentle-hag.md` § Stats & Combat › ### Coven Actions —
      Shared Spellcasting, Siphon Joy (thrall sacrifice mechanic), Gentle Gaze
      (10,000gp magic item craft) (%%src: legacy%%)
- [x] lore/flavor prose :: Gentle Hag :: `world/creatures/gentle-hag.md` §
      DM Only — thematic description ("horror is not that she is cruel. It is
      that she is not"), persistent-charm-as-permanent-retainer concept
      (%%src: legacy%%)
- [x] related-entity link :: Haunt Hag :: `world/creatures/gentle-hag.md` §
      DM Only › ### Related — target page does not exist yet (stub check:
      `grep -ril "haunt.hag" world/ pcs/ prep/` → no hits, no ledger line in
      this migration batch names her/it either). Written as plain text per
      migration-mode link deferral; `relink: haunt-hag — once its page lands`
      flag carried below.

## Gap verdict

**Recommendation: (b) `lore` honestly fits, with a documented precedent already
governing this exact content shape — no `wiki-contract.md` schema patch
needed. The real gap is one missing row in source-ingest's own
`references/claim-buckets.md`, not a missing wiki type.**

This is a narrower conclusion than the ledger line's "no creature page type"
framing implies. That framing is *literally* true (wiki-contract.md's type enum —
`npc | location | faction | quest | item | lore | pc | session | encounter`,
wiki-contract.md:12 — has no `creature` member) but functionally the system
already has a considered, deliberate home for exactly this content, established
independently by a sibling skill before this dispatch ever ran. Evidence:

1. **`encounter-design`'s own Wiki placement section already routes this exact
   shape.** `.claude/skills/encounter-design/SKILL.md:46-49` (§ Wiki placement,
   the fork also restated at :230-234 § Named foe vs. generic creature):
   > "Generic/homebrew creature meant to be reused across encounters → its own
   > `type: lore` page (`prep/backlog/<creature-slug>.md`), stat block under
   > `## DM Only`. A creature used once → stays inline in the encounter page, no
   > separate file."
   Gentle Hag is exactly this bucket: a homebrew (`sources: [Homebrew, Pointy
   Hat]`) monster-manual-style entry, not a unique named individual with an
   established campaign identity. Its "name" is a species/monster-type label —
   the same pattern as its own `## Related` link, "Haunt Hag" (a sibling
   monster-type entry, not a personal name) — and its `environment: forest,
   urban` field is generic placement, not a campaign-specific location. Compare
   `## Named foe vs. generic creature` (SKILL.md:215-234): a **named, may-recur**
   antagonist gets `npc-prep`; Gentle Hag has no PC connection, no established
   campaign presence, no unique backstory tying her to this table — she reads as
   "a Gentle Hag" the same way a monster manual entry reads as "a Bandit
   Captain," reusable across encounters. This decision was made deliberately by
   a sibling skill, independent of this dispatch — it is not this agent
   inventing a fit after the fact.
2. **Zero governed/mechanical frontmatter to key, mirroring the `deity ::
   syranita` precedent's reasoning (`archive/2026-07/ss-deity-syranita.md`
   § Fit verdict item 1).** The source's frontmatter carries `cr: 7`,
   `creature_type: fey`, `environment: forest, urban`,
   `str/dex/con/int/wis/cha`, `statblock: inline`, `page: 0` — none of these
   are governed keys in wiki-contract.md's "Type-specific required keys" table
   (wiki-contract.md:22-44) for ANY type, `npc` included. The precedent already
   on the wiki for exactly this data shape is `world/npcs/estratto.md`: a full
   CR 6 warforged statblock (traits, spells, actions, reactions) lives entirely
   inside a ```` ```statblock ```` code fence under `## Stats & Combat`
   (estratto.md:118-173) — none of AC/HP/CR/ability-scores is promoted to
   frontmatter there either. A new `creature` type would only earn its keep by
   carrying a governed field the existing types can't — this source supplies
   none; every mechanical fact it states already has a home inside a codeblock
   under an existing type's `DM Only`/`Stats & Combat` heading.
3. **The actual gap: source-ingest's own triage table has no row for this.**
   `.claude/skills/source-ingest/references/claim-buckets.md`'s "Source types"
   table (lines 7-22) has ten rows; the closest, `entity-source` ("Named NPC,
   item, or creature details" → "`npc`/`item` skeleton + reciprocal links"),
   *conflates* creature details into `npc`/`item` and never mentions `lore` —
   silently contradicting `encounter-design`'s already-established
   generic-creature-to-`lore` routing above. The "Claim buckets (full)" table
   (lines 50-67) has the same blind spot: no row for "generic/homebrew
   creature, no individual campaign identity." That's the one concrete place
   this dispatch found a genuine hole — not in `wiki-contract.md`'s type enum,
   but in the routing table THIS skill reads before triaging a source. A
   `creature`-shaped source handed to a fresh source-ingest run today would
   default-triage to `entity-source` → `npc`, silently overriding
   `encounter-design`'s own considered decision, unless a human (or this
   dispatch) catches it — which is exactly what happened here.
4. **Precedent check against `encounter`'s own promotion history.**
   `encounter` was promoted
   from a `type: session` stopgap to a real type because it had "a genuinely
   distinct, *consistent* mechanical shape... that recurred across many source
   instances and didn't fit any existing skeleton" (the same test
   `ss-deity-syranita.md` § Fit verdict item 5 applied to reject a `deity`
   type). This migration batch names exactly one `creature`-triaged source
   (MIGRATION-LEDGER.md — no sibling `creature ::` lines found by
   `grep -n creature MIGRATION-LEDGER.md`). One instance is not "many source
   instances recurring" — the promotion bar `encounter` cleared. If the
   Shattered Sea wiki's full `entities/creatures/` directory turns out to hold
   many more bestiary entries in a later migration wave, that volume would be
   the actual argument for a dedicated `creature` type + skeleton + its
   type-schema registration, plus
   `docs/campaign/skeletons/creature.md` and its
   `.claude/skills/campaign-os/assets/skeletons/creature.md` mirror. That
   volume test is this dispatch's one open question — flagged below, not
   decided here, since a single 96-line source file cannot answer a "how many
   more are coming" question.

**Where `lore` fits and where it needs a human call, if this verdict is
accepted:**

- `## Player-Known`: thin/empty by default — nothing in the source states this
  creature has been revealed at the table (no Session Events / appearance
  marker exists in the source at all, unlike `estratto.md`'s explicit "(Not
  yet encountered.)"). `status` should land `pending`, not the ledger's default
  `canon`, same override `ss-npc-estratto.md`'s own Flag 1 already established
  for exactly this "never revealed" signal — left for the write-executing
  agent to confirm.
- `## DM Only`: the full ```` ```statblock ```` code fence verbatim, the Coven
  Actions section, and the Lore prose paragraph — all DM-facing prep content.
- `## Sources`: `%%src: legacy%%`, citing the source's own `sources: [Homebrew,
  Pointy Hat]`.
- No frontmatter patch needed for `lore` itself — it has no type-specific
  governed keys in wiki-contract.md today, and this source doesn't need one
  (item 2 above).

## Minimal patch, if verdict (b) is accepted (nothing schema-level required)

1. **`​.claude/skills/source-ingest/references/claim-buckets.md`** — add one row
   to the "Source types" table (near `entity-source`) distinguishing "named
   individual" from "generic/homebrew creature, no campaign identity," pointing
   the latter at `lore` and citing `encounter-design/SKILL.md`'s § Wiki
   placement fork as the authority — same shape as the existing
   `rules-or-homebrew` row's "lore skeleton (approximation — no `rules` type
   exists)" note. Add a matching row to the "Claim buckets (full)" table.
2. No `wiki-contract.md` edit — `lore`'s type-enum membership and skeleton
   already cover this, and it needs no new governed key (nothing to govern).

## If verdict (a) is preferred instead (orchestrator wants a dedicated `creature`

type — e.g. because the volume question in item 4 resolves toward "many more
are coming")

Then the patch is schema-level and touches, minimally:

- `wiki-contract.md:12` — add `creature` to the type enum; add a
  "Type-specific required keys" row (candidates actually populated by this
  source: `creature_type` free text, `cr` numeric/string, `environment` free
  text — mirroring how `location`'s `subtype` is governed today; ability
  scores stay inside the statblock codeblock, not frontmatter, per item 2's
  Estratto precedent — do not promote those). These three fields read as free
  text in every source file checked, not closed enums, so they likely stay
  ungoverned like `npc`'s `location` key (wiki-contract.md:40-44) rather than
  becoming a closed enum.
- `wiki-contract.md:80-97` (Required skeleton per type) — new row, e.g.
  Player-Known · DM Only · Stats & Combat · Related Creatures · Appearances
  (mirrors `npc`'s skeleton shape, since a creature entry is npc-adjacent
  structurally, just without a personal identity).
- `docs/campaign/skeletons/creature.md` **and**
  `.claude/skills/campaign-os/assets/skeletons/creature.md` (both copies,
  confirmed as a maintained pair for every other skeleton today) — new
  skeleton file per the heading list above.
- `.claude/skills/source-ingest/references/claim-buckets.md` — same row
  addition as the minimal-patch path, but pointed at `creature` instead of
  `lore`.

## Flags

1. **RESOLVED (re-dispatch).** Volume question answered by the orchestrator:
   commit ed63957's message cites 135 bestiary files in the source repo,
   clearing the promotion bar; verdict (a) (dedicated `creature` type) shipped.
2. **Related-entity link still deferred, live.** `Haunt Hag` (source's own
   `## Related` section) has no page in `world/`/`pcs/`/`prep/` and no ledger
   line in this batch names it. Written as plain text in `world/creatures/
   gentle-hag.md` § DM Only › ### Related. `relink: haunt-hag — once its page
   lands.`
3. **Status override applied.** Source has no Session Events / appearance
   marker at all (not even estratto.md's explicit "Not yet encountered")  —
   this reads as an unused bestiary entry, never brought to the table. Landed
   `status: pending`, overriding the ledger's default `canon` disposition —
   same override `ss-npc-estratto.md`'s Flag 1 established for the identical
   "no reveal signal" case.
4. **Tag substitution.** Source `tags: [combat, homebrew]` has no canonical
   equivalent in `world/_meta/tags.md` (canonical domain tags: intrigue,
   heist, horror, mystery, exploration, war, politics, romance; no
   `combat`/`homebrew` alias listed). Mapped to nearest canonical: `horror`
   (matches the page's own closing line and estratto.md's precedent of
   tagging `horror` for a similarly unsettling premise). `combat`/`homebrew`
   dropped, not invented as new canonical tags — per REVIEW item 8, tag
   taxonomy is not this dispatch's to expand.
5. **Frontmatter drop.** Legacy keys with no contract equivalent
   (`campaign`, `audience`, `confidence_level`, `sources`, `cha/con/cr/
   creature_type/dex/environment/int/page/statblock/str/wis`) dropped per
   MIGRATION-LEDGER.md Flags — mechanical fields already live inside the
   `statblock` codeblock (wiki-contract.md:111, the Estratto precedent);
   `creature` carries no type-specific governed frontmatter keys today
   (wiki-contract.md:22-54 has no `creature` row), so nothing needed a home.
6. **This verdict pattern generalized as predicted (former Flag 3).** The
   orchestrator's patch (commit ed63957) also shipped `rule` and `ship` types
   in the same commit, confirming the prediction that this pattern would
   extend to the sibling `rules ::`/`vehicle ::` ledger lines.
