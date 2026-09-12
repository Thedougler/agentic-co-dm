# Source ingest queue: ss-species-grung

Source root: /Users/nick/ai-os/shattered-sea/wiki/lore/species/grung.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — `species :: lore/species/grung.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:11 "REVIEWED-BY-HUMAN: 2026-07-13 — per the user's handoff mission..."
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] lore/species/grung.md — triage: entity-source (lore), ready

## Claims — lore/species/grung.md

- [x] lore :: Grung :: world/lore/grung.md (new) — species identity, table traits, caste system (%%src: legacy%%)

## Dual-home test (special duty per dispatch instructions)

`ls`/`grep` of both `entities/species/` and `lore/species/` in the source repo:

- `entities/species/` contains exactly one file: `human.md`. **No `grung.md` or
  any grung-named file exists there.** The dual-home structure the ledger line
  anticipates ("entities/species vs lore/species") is real for *human*
  (`entities/species/human.md` + `lore/species/human-culture.md`) but **does
  not materialize for grung** — there is only the one copy, at
  `lore/species/grung.md`.
- `grep -ril grung entities/species/` hits only `human.md`, and only as a
  passing wikilink in a "peoples of the Shattered Sea" list
  (`- [[grung|Grung]]`) — a cross-reference, not a competing grung page.
- **Verdict: no duplicate to reconcile.** `lore/species/grung.md` is treated
  as sole-authoritative by default (it's the only copy), not by a
  comparison-and-choice process. No W9 duplicate-content flag applies — W9
  requires two pages stating the same fact; there is only one. Logging this
  as the dual-home finding itself: the premise "species kept in both dirs"
  is true for the *species* content type in general (human) but false for
  this specific entity (grung). NOTED for the orchestrator in case other
  species ledger lines assume the dual-home pattern holds uniformly — it
  doesn't.

## Flags

1. **Disposition confirmed: canon.** Ledger line pre-declares `status: canon`.
   Source frontmatter carries `status: active`, `audience: players`,
   `publish: true` — an explicit signal (unlike the estratto NPC case) that
   this content was written for and shown to players, not held-back DM prep.
   No internal contradiction (no "not yet encountered" style marker anywhere
   in the source). Canon is the correct call here; no override needed.

2. **Unresolved wikilinks — reciprocal links deferred.** Source links to five
   other entities: `[[grung-clans]]`, `[[verdant-teeth]]`,
   `[[jean-claude-tabarnack]]`, `[[simone-tabarnack]]`,
   `[[peoples-of-the-shattered-sea]]`, plus `[[midchain]]` in body prose.
   Stub check (`grep -ril <name> world/ pcs/ prep/`) returned empty for all
   six — none exist in campaign-os yet. Per migration mode's owned-paths
   restriction and source-ingest's link-deferral rule, written as **plain
   text, not `[[wikilinks]]`**. Relink once each target page lands:
   - relink: grung-clans — once its page lands (likely the faction ledger
     line, `entities/factions/grung-clans.md`, not yet in this migration wave)
   - relink: verdant-teeth — once its page lands
   - relinked ✓ — jean-claude-tabarnack — `pcs/jean-claude-tabarnack.md` landed
     (canon); the "Jean-Claude Tabarnack" prose mention and the `### Related`
     bullet now link `[[jean-claude-tabarnack|Jean-Claude Tabarnack]]`
     (link-restoration pass R4, 2026-07-14)
   - relink: simone-tabarnack — once its page lands
   - relink: peoples-of-the-shattered-sea — once its page lands
   - relink: midchain — once its page lands

3. **Frontmatter fields with no contract home.** Source frontmatter carried
   `subtype: species`, `campaign`, `audience`, `summary`, `sources:` (list
   form) — none are governed keys in wiki-contract.md's `lore` schema (only
   `location` has a `subtype` enum; `lore` has none). Dropped from
   frontmatter. `summary` folded into opening Player-Known prose;
   `sources: [Inbox/Grung.md]` folded into the page's own `## Sources`
   section per the lore skeleton's required heading.

4. **`created`/`touched` have no migration-mode value.** Same gap as the
   estratto ledger line: wiki-contract.md only defines `sNN` or `prep`.
   Used `legacy` as the closest-fidelity placeholder (consistent with the
   estratto precedent), flagged as not a documented enum value.

5. **Tag `grung` doesn't map to the taxonomy — left empty rather than forced.**
   Source tag `grung` is an entity-name tag, not a Domain (tone/genre) or
   Project tag per `world/_meta/tags.md`'s two buckets. Unlike the estratto
   case (where `tessarine`/`homebrew` had a plausible tonal fit —
   `intrigue`/`horror`), no canonical Domain tag (`intrigue, heist, horror,
   mystery, exploration, war, politics, romance`) is an honest fit for a
   species-identity lore page — forcing one (e.g. `exploration`) would be
   inventing a genre signal the source never stated. Left `tags: []` and
   flagging the taxonomy gap instead: the taxonomy currently has no bucket
   for "this page is about species X" — a plausible gap for the DM to
   consider (a `lore` subtype tag family?) but not this agent's call to add
   unilaterally.

6. **Player-Known / DM Only split: source has no DM-only content.** The
   source is flat, undivided prose+tables with no secrets, hooks, or
   DM-facing notes anywhere (`audience: players` covers the whole file).
   Everything went under `## Player-Known`; `## DM Only` is present (skeleton
   requires the heading) but intentionally empty rather than backfilled with
   an invented DM note — Hard Rule 1 (fidelity, never invent past the
   source).
