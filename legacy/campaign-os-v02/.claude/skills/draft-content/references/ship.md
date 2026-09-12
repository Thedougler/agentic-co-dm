
# Draft — Ship

A vessel the party sails, fights, or owns. Done means DM-grade mechanical
reference, table-ready the moment the ship matters — and a silhouette a
player would recognise from the read-aloud alone.

## Template

`vault/_templates/_srd/_ship.md` — copy it, never retype it from memory. Headings stay
fixed and in order: `## Stats & Combat · ## Crew · ## Session Log`, with an
optional `## Connections` between Crew and Session Log when the vessel has
durable non-crew relationships.

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — PC agency; named crew and
   rival captains are NPCs with their own agency.
3. `vault/refs/vault/_common/hard-rules.md` — the shared rules,
   including the mechanical-type section; they bind this type and are never
   restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now and
   paste the output.

`DS1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **The Tier Comes First.** About to design stats, crew, or cost -> set the
  tier from the interview first, never work backwards
  (`vault/refs/vault/ship/references/tiers-and-crew.md` §1).
- **The Crew Is Stated.** About to write crew -> name who holds every
  filled role and say which are open, never leave it implied
  (`vault/refs/vault/ship/references/tiers-and-crew.md` §3).
- **The Acquisition Is Resolved.** About to write how the ship was got ->
  name it and resolve it through the fiction, never just the outcome
  (`vault/refs/vault/ship/references/acquisition-and-variants.md` §1).
- **The Multi-File Fork.** About to give a Tier-3 vessel a page family ->
  a single page is the default
  (`vault/refs/vault/ship/references/output.md`).
- **The Mobile-Location Check.** About to finalize -> a ship is a mobile
  location, so run its flavor description against
  `vault/refs/vault/location/references/tips.md`'s six-point checklist first.
- **The DM Review Gate.** About to flip `status:` `draft` -> `pending` ->
  present tier, crew, acquisition, and any variant, then wait for approval
  (`vault/refs/vault/ship/references/checklist.md`).

## Interview — this type only

Ask these in the same message as
`vault/refs/vault/_common/interview.md`'s shared questions:

- Which PC, or a shared party vessel?
- Target tier (1–4), and any variant it should specialize into?
- Acquisition — Buy / Steal / Mutiny / Prize / Build?
- Who crews it: PCs in roles, named hirelings, roles left open?
- A home-base bastion, or purely a vehicle? If a bastion, which facilities
  now (`vault/refs/vault/ship/references/bastion.md`)?
- The party's single long-term vessel, or a one-off NPC-owned ship?

## Ship Toy

Six fields written once as a table after the stat line, no heading of its
own: `tier_justification`, `pc_connection`, `acquisition_method`,
`crew_composition`, `current_status`, `bastion_facilities`.
Fields: `vault/refs/vault/ship/references/toy.md`.
Layout: `vault/refs/vault/ship/references/output.md`.
Frontmatter keys: `vault/refs/vault/ship/references/frontmatter.md`.

## Before you ship

Lifecycle `vault/refs/vault/_common/lifecycle.md` · gaps
`vault/refs/vault/_common/degrade.md` · handoffs
`vault/refs/vault/_common/handoffs.md` · boundaries
`vault/refs/vault/_common/out-of-scope.md` · then
`vault/refs/vault/_common/checklist.md` and
`vault/refs/vault/ship/references/checklist.md`.

## Reference files

| File | Read when |
|---|---|
| `vault/refs/vault/ship/references/tiers-and-crew.md` | Setting tier, stating stats, filling crew roles, checking upkeep |
| `vault/refs/vault/ship/references/bastion.md` | The ship serves as the party's home base |
| `vault/refs/vault/ship/references/acquisition-and-variants.md` | Naming acquisition, applying a variant, adding an enhancement |
| `vault/refs/vault/ship/references/toy.md` | Writing the Ship Toy table's values |
| `vault/refs/vault/ship/references/output.md` | Mapping onto headings, or building a multi-file family |
| `vault/refs/vault/ship/references/frontmatter.md` | Filling `ship_class`, `tier`, `home_port` |
| `vault/refs/vault/ship/references/example.md` | A full worked page, interview to finished |
