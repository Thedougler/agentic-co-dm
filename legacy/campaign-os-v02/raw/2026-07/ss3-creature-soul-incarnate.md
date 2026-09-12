# Source ingest queue: ss3-creature-soul-incarnate

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/creatures/planned/soul-incarnate.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md § Round 3 — `creature-planned ::
entities/creatures/planned/soul-incarnate.md → world/creatures/ — CROSS-SOURCE TEST: this entity's
identity facts already live on world/factions/sentinels-of-the-eyrie.md (canon, Front + DM Only);
reconcile, never duplicate (L6) — the creature page carries the statblock/mechanics, the faction
page keeps the situation; planned/ dir = rung-1 unrevealed → pending`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:63 "REVIEWED-BY-HUMAN: 2026-07-13 — same
user instruction; blessing covers exactly the 14 lines below." (Round 3 header, line 61)
Started: 2026-07-13

Cross-source reconciliation note (this is the round's designated test): the entity's *situation*
facts (Front: The Soul Incarnate's Watch, Master Kyzil's ignorance, the fissure-record behavior,
the Auralis mirror, Crissdalynn Khinriss's pilgrimage connection) already live on the canon
`world/factions/sentinels-of-the-eyrie.md` page (landed Round 1, `ff53e88`). Read in full before
writing this page. No genuine contradiction found between the two sources — see Reconciliation
below. Per L6 (one fact, one page), those situation facts are NOT restated here; this page carries
only what the *creature* source itself states (statblock mechanics + the monk-lichdom origin/
nature lore) and wikilinks to the faction page for everything else.

## Sources (batch order, smallest file first)

- [x] entities/creatures/planned/soul-incarnate.md — triage: entity-source (creature-shaped,
      named individual with an already-canonized situation elsewhere — statblock + origin lore
      only remain this page's to carry) — written to `world/creatures/soul-incarnate.md`,
      `type: creature`

## Claims — entities/creatures/planned/soul-incarnate.md

- [x] creature identity + full statblock :: Soul Incarnate :: `world/creatures/soul-incarnate.md`
      § Stats & Combat — CR 16 undead, AC 17, HP 136 (16d8+64), monk-flavored ki traits/actions
      (Drain Ki, Evasion, Incarnation, Incorporeal Movement, Ki Pool, Ki-Empowered Strikes, Magic
      Resistance, Turn Resistance; Multiattack, Longstaff, Unarmed Strike, Empty Body, Flurry of
      Blows, Patient Defense, Step of the Wind, Deflect Missiles), inside the ```statblock``` fence
      verbatim per the gentle-hag/giant-owl precedent (%%src: legacy%%)
- [x] origin/nature lore :: Soul Incarnate :: `world/creatures/soul-incarnate.md` § DM Only —
      "A monk who achieved lichdom through years of meditation, then ritual desiccation... The
      physical body mummifies and becomes the phylactery; the consciousness rises as a ki-form: a
      hovering figure traced in glowing meridian lines, incorporeal and unbounded by normal
      physical limits." Transcribed verbatim; this is genuinely new information not present on the
      canon faction page (which states WHERE the phylactery is sealed but not HOW the creature
      became a lich) — no overlap, no reconciliation call needed for this claim (%%src: legacy%%)
- [x] DM-secrecy marker :: Soul Incarnate :: `world/creatures/soul-incarnate.md` § DM Only —
      "Planned as a late-campaign secret reveal. Do not integrate into any public-facing wiki
      content until confirmed." carried as a `[!dm]` callout, matching the source's own callout
      styling and the gentle-hag/giant-owl DM-secrecy precedent (%%src: legacy%%)
- [x] related-entity links :: "Who Is the True Head of the Sentinels" (situation) + Sentinels of
      the Eyrie (faction) :: `world/creatures/soul-incarnate.md` § DM Only › ### Related —
      RECONCILED, not a plain relink. Stub check: `find world -iname "*sentinels-true-head*"` →
      no hits; MIGRATION-LEDGER.md:57 shows this situation was already absorbed into the canon
      faction page during Round 2 ("situation :: situations/dormant/sentinels-true-head.md → DONE
      1b69422 — absorbed into canon sentinels page"). No standalone page exists or should exist —
      written as prose noting the absorption, pointing to `[[sentinels-of-the-eyrie]]` § Front: The
      Soul Incarnate's Watch. The sibling "Sentinels of the Eyrie" related-link resolves directly:
      `[[sentinels-of-the-eyrie]]` is on the allowed real-wikilink list for this round
      (%%src: legacy%%)

## Reconciliation — canon world/factions/sentinels-of-the-eyrie.md vs. this creature source

Read in full before writing. Findings, checked against every claim in the creature source:

- Both sources agree the Soul Incarnate is a lich of the monk variety, and both frame it as a
  late-game/unrevealed secret (creature source: "planned late-campaign secret reveal"; faction
  page: "a late-game revelation, not stated as delivered at the table... treated here as an
  unrevealed DM secret"). Consistent, not duplicated.
- The creature source's statblock `alignment: "Any Alignment"` is the generic 5e stat-block
  template value (transcribed verbatim inside the fence, same treatment as every other statblock
  field) — not a narrative characterization, so it does not contradict the faction page's prose
  description "truly neutral." Different fields, different purposes; no CONTRADICTION block
  warranted.
- Location fact (phylactery "sealed within the basalt sea stack beneath High Eyrie") exists ONLY
  on the canon faction page — the creature source's Lore section never states a location. No
  overlap to reconcile; nothing added to this page about location (would be inventing past this
  source, Hard Rule 1).
- Situation facts that live exclusively on the faction page and are NOT restated here (L6):
  Master Kyzil's ignorance of the Soul Incarnate's conscious existence, the fissure-record
  escalation behavior, the Auralis-unaware-mirror detail, Crissdalynn Khinriss's pilgrimage
  connection, and the Front "The Soul Incarnate's Watch" (Lifecycle: dormant) itself. All covered
  by the `[[sentinels-of-the-eyrie]]` wikilink in this page's § Related instead.
- Verdict: no contradiction found. Reconciliation resolved by division of labor (creature page =
  statblock + origin nature; faction page = situation + Front), not by picking a winner between
  competing claims — there were no competing claims, only complementary ones.

## Flags

1. **Status: `pending`, rung 1 of the migration-mode status ladder.** Source directory is
   `entities/creatures/planned/` — an explicit unrevealed marker (the directory name itself), which
   is rung 1 of source-ingest's status-determination precedence and beats every other signal.
   Matches the ledger line's own disposition call.
2. **Related-entity link for the absorbed situation is prose, not a wikilink — by design, not
   deferral.** "Who Is the True Head of the Sentinels" has no standalone page (absorbed into the
   faction page in Round 2) and never will; this isn't a `relink:` flag (those are for pages that
   don't exist *yet*), it's a permanent redirection to `[[sentinels-of-the-eyrie]]`.
3. **`Source: Pointy Hat` line dropped.** The legacy file's italicized real-world attribution line
   under its Lore section (external homebrew-content credit) has no equivalent field anywhere in
   wiki-contract.md's creature skeleton or any sibling creature page (gentle-hag/giant-owl carry no
   such line) — dropped per the same "no contract equivalent" precedent as frontmatter drops below,
   not carried into the page body.
4. **Frontmatter drops, matching gentle-hag/giant-owl precedent.** `campaign`, `audience`,
   `confidence_level`, `sources`, `summary`, and the `cr` field (mechanical, already inside the
   `statblock` fence) all dropped — no contract-governed equivalent for `type: creature`.
   `aliases: [Soul Incarnate]` dropped to `[]` (name-only alias identical to the title, same drop
   gentle-hag/giant-owl both made).
5. **Tag: source `tags: [undead]` dropped, not mapped — entity-identity tag, not tone (WIKI.md §
   Tag taxonomy: "Migrated legacy tags: entity-identity tags... are DROPPED BY DESIGN").** A
   genuine tonal signal exists elsewhere in the source instead: the DM callout itself ("Planned as
   a late-campaign secret reveal. Do not integrate into any public-facing wiki content until
   confirmed") is mystery-toned — concealment/reveal is exactly what the canonical `mystery` tag
   covers, and the canon faction page this creature is entangled with already carries `mystery`
   too. Mapped source-tag-absent-but-content-present, one worked mapping (matches the gentle-hag
   combat→horror precedent's evidentiary bar), not a general rename rule. Landed `tags: [mystery]`.
6. **Skeleton/convention hold confirmed at n=3.** Player-Known · DM Only · Stats & Combat ·
   Appearances headings and the `### Related`-under-DM-Only sub-heading both mapped cleanly onto a
   third, structurally distinct source (a DM-secret named individual with an existing canon
   cross-reference, vs. gentle-hag/giant-owl's unused generic bestiary entries) with no skeleton
   changes needed.
7. **No CONTRADICTION block written.** See Reconciliation section above — genuinely no conflicting
   claim was found between this source and the canon faction page it overlaps with.
