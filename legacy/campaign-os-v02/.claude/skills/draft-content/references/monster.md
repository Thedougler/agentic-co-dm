
# Draft — Monster

A reusable creature kind — ecology and stats for a species meant to recur
across encounters, never a named individual. Done means a bestiary-ready
stat block any DM can drop into a matching encounter, calibrated against
this party.

## Template

One template for every creature, `vault/_templates/_srd/_monster.md` —
copy it. A creature may be `srd` bulk-ingested, `third_party` vendored by
`find-creature`, or `homebrew` originated in this campaign; the page shape
is otherwise identical regardless. Modeled on the Forgotten Realms Wiki's creature-article shape (Beholder, [[owlbear|Owlbear]]), it scales the same way for an iconic monster and a minor one: what it is, how it fights, where and how it lives, what a DM needs to run it.

Page path: `vault/campaigns/shattered-sea/monsters/<slug>.md`. Every heading is fixed and required except `## Toy Chest` (required only for an original homebrew creature; otherwise OPTIONAL — keep only what the sourcebook doesn't already cover), `## Prepped Reveals`, and `## Notable Individuals` (both OPTIONAL, delete when empty).

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — PC agency; a creature kind
   moves on its own timeline regardless of the party.
3. `vault/refs/vault/_common/hard-rules.md` — the shared rules,
   including the mechanical-type section; they bind this type and are
   never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now
   and paste the output.

`DCR1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **The Recurrence Fork.** Before writing, ask: does this kind recur, or is it a one-off? A one-off routes to `encounter-prep`. A named individual routes to `.claude/skills/draft-content/references/npc.md`. A recurrent kind gets a creature page: name only the species/kind; omit `## Relationships` heading.
- **Sourcing.** `source:`/`source_url:`/`license:` are required for a transcribed or vendored creature; fill from the actual source, not invented. Delete `owner_skill:` once instantiated — template-only.
- **The Wants And Morale Lines.** For a narrative-notable creature, add two mandatory lines (one line each, bold-led): `**Wants:**` (what this creature always wants; what's disrupting that now — compressed from the Toy Chest rows) and `**Morale:**` (pre-decided break/flee condition; not a restatement of HP). A stock monster at `status: draft` omits this block.
- **Statblock Is Always Inline.** Write the fenced `statblock` codeblock on this page under `## Statblock`, `name:` matching frontmatter (`statblock: inline` is fixed, not a choice — it registers the codeblock into the Fantasy Statblocks bestiary). `vault/refs/vault/monster/references/statblock-format.md` for syntax and WotC wording.
- **The Sim Sweep.** Extends Calibrate Against The Real Party — a new
  homebrew creature also runs `pnpm sim sim-combat party <monster.md>
  --sweep-count --min-count 1 --max-count 1` as a sanity check.

## Interview — this type only

Ask these in the same message as `vault/refs/vault/_common/interview.md`'s shared questions:

- Reused across encounters, or one-off? (The Recurrence Fork — routes to `encounter-prep` or `.claude/skills/draft-content/references/npc.md`.)
- Existing creature to vendor, existing stat block to reskin, or genuinely new? (Before inventing: check `find-creature` and reskin candidates. Only write original stats when both checks come up empty.)
- Creature type and ecological role — predator, pest, guardian, pack hunter — and habitat.
- Legendary or lair-worthy? → `vault/refs/vault/monster/references/cr-design.md` § Solo boss / elite suite.

## Toy Chest

For narrative-notable creatures: write a table in the DM-only section with four fields (`verb`, `unstable_condition`, `consequence`, `link_of_relevance`). This table never appears in frontmatter, only once in the page. From this table, compress the Wants/Morale lines (see Hard rules above).
Field definitions: `vault/refs/vault/monster/references/toy.md`.
Layout and wiring: `vault/refs/vault/monster/references/output.md`.

## Before you ship

In order: [[lifecycle|Lifecycle]] `vault/refs/vault/_common/lifecycle.md` → Gaps `vault/refs/vault/_common/degrade.md` → [[handoffs|Handoffs]] `vault/refs/vault/_common/handoffs.md` → Boundaries `vault/refs/vault/_common/out-of-scope.md` → Checklists `vault/refs/vault/_common/checklist.md` and `vault/refs/vault/monster/references/checklist.md`.

## Reference files

| File | Read when |
|---|---|
| `vault/refs/vault/monster/references/cr-design.md` | Designing any stat block from scratch, or validating a CR |
| `vault/refs/vault/monster/references/cr-tables.md` | Looking up the CR/DPR benchmark, HP, ability-score, or condition numbers |
| `vault/refs/vault/monster/references/lightning-rods.md` | Statting a CR-4+ creature for a party of 5th level or higher |
| `vault/refs/vault/monster/references/reskin-templates.md` | Reskinning when no close SRD analog exists |
| `vault/refs/vault/monster/references/statblock-format.md` | Writing the statblock codeblock and its bestiary wiring |
| `vault/refs/vault/monster/references/toy.md` | Filling any Toy Chest field |
| `vault/refs/vault/monster/references/output.md` | Laying out sections, the Player-Known/DM-Only drafting lens |
| `vault/refs/vault/monster/references/ecology.md` | Picking `found_at:` region-scale locations |
| `vault/refs/vault/monster/references/example.md` | A full worked page, interview to finished |
| `vault/refs/vault/monster/references/bosses-and-minions.md` | Pairing boss monsters with minion types and environments by CR for boss battles |
| `vault/refs/vault/monster/references/building-a-quick-monster.md` | Quick monster-building method with CR table and step-by-step guidance |
| `vault/refs/vault/monster/references/combinations.md` | Combining 5e monsters of varying CR into hard encounters by party size and structure |
| `vault/refs/vault/monster/references/difficulty-dials.md` | Four tuning dials (HP, count, damage, attacks) for on-the-fly monster adjustment |
| `vault/refs/vault/monster/references/general-use-combat-stat-blocks.md` | Seven reskinnable stat blocks (CR 1/8–15) with full mechanics and usage guidance. Its Minion/Soldier/Brute/Specialist/Myrmidon/Sentinel/Champion names are CR tiers — a different axis from `vault/refs/vault/monster/references/roles.md`'s tactical roles below, not a rename of them |
| `vault/refs/vault/monster/references/lazy-tricks-for-running-monsters.md` | Quick-reference CR statistics, monster features, and dice-average lookup table |
| `vault/refs/vault/monster/references/monster-builder-overview.md` | Index and licensing for Sly Flourish's Lazy GM's 5e Monster Builder Document |
| `vault/refs/vault/monster/references/monster-builder-read-me-first.md` | Intro and attribution for the Lazy GM's 5e Monster Builder (LGMMBRD) |
| `vault/refs/vault/monster/references/roles.md` | Seven tactical combat roles — Ambusher, Artillery, Bruiser, Controller, Defender, Leader, Skirmisher — with when-to-use and placement guidance. A creature has one role and one CR tier; the two are chosen independently |
| `vault/refs/vault/monster/references/running-hordes.md` | Horde combat rules: damage pooling, attack resolution, area effects |
| `vault/refs/vault/monster/references/templates.md` | Five monster templates (elemental, dire, fiendish, spell-infused) for reskinning |
| `vault/refs/vault/monster/references/tiers-of-play.md` | Matching monster CR to character tier (1st–20th level) |
| `vault/refs/vault/monster/references/undead-templates.md` | Converting any monster to skeleton, zombie, ghoul, wight, wraith, or vampire spawn |
