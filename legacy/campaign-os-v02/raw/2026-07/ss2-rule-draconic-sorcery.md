# Source ingest queue: ss2-rule-draconic-sorcery

Source root: /Users/nick/ai-os/shattered-sea/wiki/rules/subclasses/draconic-sorcery.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md:56 — `rules ::
rules/subclasses/draconic-sorcery.md`)

Gate proof (three-condition check, source-ingest skill § Migration mode):

- (a) ledger names this source + disposition — MIGRATION-LEDGER.md:56:
  `- [ ] rules :: rules/subclasses/draconic-sorcery.md → restructure →
  world/rules/ — subtype: subclass; pending per codified library-default
  shortcut`
- (b) REVIEWED-BY-HUMAN gate satisfied — MIGRATION-LEDGER.md:41-42:
  `REVIEWED-BY-HUMAN: 2026-07-13 — user instruction "implement all your
  recommended fixes, then proceed to round two". Blessing covers exactly the
  13 lines below.` (draconic-sorcery is one of those 13 Round 2 lines)
- (c) disposition is the codified library-default shortcut, not a fresh
  canon/pending call — `references/claim-buckets.md:64`: "Migration status
  shortcut: a rules-library file whose frontmatter matches its whole sub-pile
  verbatim (uniform audience/status/publish) carries an export default, not a
  reveal signal — land `pending` unless a transcript shows the table using
  it." Cited, not re-derived (task instruction; see also
  `ss-rules-swashbuckler.md`'s full first-derivation of this same shortcut).

Started: 2026-07-13

**Status verdict: `pending`, applied via the codified shortcut, not
re-derived.** Source frontmatter (`status: unknown`, `audience: dm`,
`publish: false`) — checked against sibling files in
`rules/subclasses/` (same uniform export-default pattern the swashbuckler
dispatch found across all 27 files in that directory, itself the precedent
that got the shortcut codified into claim-buckets.md's rule row). No
`sessions/` transcripts exist yet (`grep -ril "draconic\|sorcer" sessions/
2>/dev/null` — no hits, no `sessions/` subdirs at all), so no table-use
signal overrides the default. `type: rule` / `subtype: subclass` already
exist as governed schema (added for swashbuckler, commit ed63957) — no probe,
no type-fit argument needed this pass.

## Sources (batch order, smallest file first)

- [x] rules/subclasses/draconic-sorcery.md — triage: entity-source
  (mechanical rules reference), DONE — written to
  `world/rules/draconic-sorcery.md`

## Claims — rules/subclasses/draconic-sorcery.md

- [x] identity/summary :: Draconic Sorcery :: `world/rules/draconic-sorcery.md`

  ## Player-Known — Sorcerer subclass, Player's Handbook (2024), innate

  draconic-ancestry magic, generalist AC/HP/elemental powerhouse
  (%%src: legacy%%)
- [x] mechanics (5 leveled features) :: Draconic Sorcery ::
  `world/rules/draconic-sorcery.md` ## Mechanics — Draconic Resilience (L3,
  HP + unarmored AC), Draconic Spells (L3, always-prepared spell list by
  level), Elemental Affinity (L6, chosen damage type resistance + CHA damage
  bonus), Dragon Wings (L14, bonus-action Fly Speed 60ft, 1/LR), Dragon
  Companion (L18, free/no-slot Summon Dragon, optional non-Concentration
  version), each labeled [RAW, Player's Handbook (2024)] (%%src: legacy%%)
- [x] related-links :: "Sorcerer", "Clockwork Sorcery" :: stub check
  (`grep -ril "sorcerer" world/ pcs/ prep/`, `grep -ril "clockwork"
  world/ pcs/ prep/`) — both empty, neither page exists and neither is in
  this round's 10-page allow-list (estratto, calveno, preserved-eel,
  sentinels-of-the-eyrie, campaign-overview, grung, syranita, gentle-hag,
  swashbuckler, vethka). Written as plain text in ## Provenance, not
  wikilinks. `relink: sorcerer — once its page lands`,
  `relink: clockwork-sorcery — once its page lands`.

## Fit verdict

Not re-derived — `type: rule` / `subtype: subclass` already exist as
governed schema (the `rule` type's heading set and `subtype` enum),
added by the swashbuckler dispatch (`ss-rules-swashbuckler.md`'s full
argument, commit ed63957). This file is a second same-directory,
same-shape source (`rules/subclasses/`, official PHB 2024 content, uniform
library-default frontmatter) — no new type-fit probe needed, per the task's
"rule type n=2" framing.

## Flags

1. **Two relink flags, no NPC/entity in play this time.** Unlike
   swashbuckler's Delmar Fisk (a DM-Only relationship fact), this source's
   only two proper-noun mentions are its own `## Related` cross-references
   (`Sorcerer`, `Clockwork Sorcery`) — both other rule-type pages, not yet
   migrated, not on this round's 10-page allow-list. Written as plain text
   under ## Provenance: `relink: sorcerer — once its page lands`,
   `relink: clockwork-sorcery — once its page lands`.
2. **Tags: `[]`, flagged legal.** Source `tags: []` (already empty — no
   entity-identity or origin tags to drop). Domain-tone taxonomy
   (`world/_meta/tags.md`) has no tag fitting pure mechanical subclass
   content (intrigue/heist/horror/mystery/exploration/war/politics/romance
   all miss) — `[]` with this flag is legal per WIKI.md § Tag taxonomy final
   bullet + the swashbuckler precedent (same empty-tags outcome).
3. **Lint clean, no NOTED items.** See commit for exit code. No
   two-failed-fix loop triggered (Hard Rule 6 not invoked).
4. **Status verdict: `pending` via the codified shortcut — friction note.**
   The task's own framing asks whether the shortcut saved the re-derivation
   it was built for: yes — this dispatch did zero type-fit argumentation and
   zero independent status-verdict derivation, both fully inherited from
   `ss-rules-swashbuckler.md` and `claim-buckets.md:64`. The only genuine
   judgment calls left at n=2 were the two relink checks and the tags check,
   both mechanical stub-check lookups, not design calls.
