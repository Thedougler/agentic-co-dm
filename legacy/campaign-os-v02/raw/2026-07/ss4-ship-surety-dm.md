# Source ingest queue: ss4-ship-surety-dm

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/vehicles/hcs-surety-dm-guide.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md § Round 4 — `ship-dm ::
entities/vehicles/hcs-surety-dm-guide.md → folds into world/ships/hcs-surety.md ## DM Only
(companion pattern, pearl-of-souls precedent) — DISPATCH AFTER parent lands; this line authorizes
editing that page`)

Gate proof:

- docs/campaign/MIGRATION-LEDGER.md:84 `REVIEWED-BY-HUMAN: 2026-07-13 — user instructions: "at
  least 5 rounds of iterative improvements"... Blessing covers exactly the 11 lines below.`
  (Round 4 header, line 82)
- docs/campaign/MIGRATION-LEDGER.md:92 `- [ ] ship-dm :: entities/vehicles/hcs-surety-dm-guide.md
  → folds into world/ships/hcs-surety.md ## DM Only...`
- Parent confirmed landed: commit 2718ec9 (`world/ships/hcs-surety.md`, status: canon).
- `archive/2026-07/INGESTED.tsv` — no hit for `hcs-surety-dm-guide.md`; not previously
  ingested.

Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/vehicles/hcs-surety-dm-guide.md — triage: entity-source (ship DM companion), ready,
      written (companion pattern, folds into `world/ships/hcs-surety.md` ## DM Only, no new page)

## Claims — entities/vehicles/hcs-surety-dm-guide.md

- [x] ship-dm-fold :: Navigation Failures table + notes :: world/ships/hcs-surety.md ## DM Only
      (expand, new ### subsection) — DC-by-water complication table, chart advantage, shallow
      draft edge (%%src: legacy%%)
- [x] ship-dm-fold :: Chase Complications table + Ram note :: world/ships/hcs-surety.md ## DM Only
      (expand, new ### subsection) — range-band complication table, Ram-in-chase mechanics
      (%%src: legacy%%)
- [x] ship-dm-fold :: Crew Casualties table :: world/ships/hcs-surety.md ## DM Only (expand, new
      ### subsection) — HP-threshold crew-loss table; footnote reconciling its 130 HP baseline
      against the Stats & Combat table's 120 HP at-capture figure (%%src: legacy%%)
- [x] ship-dm-fold :: Bastion Facility Events + Defence tables :: world/ships/hcs-surety.md
      ## DM Only (expand, two new ### subsections) — d6 event table, 6d6 defence-roll mechanics
      (%%src: legacy%%)
- [x] ship-dm-fold :: Running Notes (DM pacing/color) :: world/ships/hcs-surety.md ## DM Only
      (expand, new ### subsection) — abstraction guidance, ram telegraph, named crew, upkeep
      pressure, Cook/Surgeon gaps (%%src: legacy%%)
- [x] ship-dm-fold :: Crown Recognition Clock elaboration (refit effect, slows/accelerates) ::
      world/ships/hcs-surety.md ## DM Only (expand existing clock paragraph, not a new subsection)
      — appends to the clock the parent already transcribed verbatim; source's own text is
      "NOW ACTIVE" elaboration, not a restated duplicate (%%src: legacy%%)
- [x] connections-update :: world/ships/hcs-surety.md ## Connections — DM Guide bullet updated
      from `relink: hcs-surety-dm-guide` (pending) to "folded in above" (done) — no future page
      will exist for this companion; the fold IS its landing.

## Reconciliation against parent's existing DM Only prose (line-specific instruction)

- Registered-out-of-Port-Tidefall sentence: parent already has it verbatim from `hcs-surety.md`;
  dm-guide restates the same fact in its own Crown Registration Timeline intro. NOT re-appended —
  duplicate, not elaboration.
- Crown Recognition Clock (Weeks 1–2 / Week 3 / Weeks 4–5 / Week 6+): parent's 4 bullets already
  match dm-guide's table nearly verbatim (both trace to the same underlying clock). NOT
  re-transcribed as a second copy. What dm-guide adds beyond the parent's existing bullets — "the
  clock is now active," the Calveno refit's effect on port-authority-glance vs. veteran-officer
  recognition, and the explicit "what slows / what accelerates" lists — IS new content, appended
  as elaboration to the existing clock paragraph.
- "Source's own dedicated situation page... and full DM chase/recognition tooling ('DM Guide')
  are not part of this dispatch" sentence: this dispatch IS the DM Guide fold, so the DM Guide
  half of that sentence is now false. Edited down to name only the still-un-ingested situation
  page ("Surety — Crown Search").
- Estratto writ paragraph and the `status: lost` axis-note: dm-guide doesn't touch either topic.
  Untouched.
- No other prose overlap between dm-guide and the parent's existing DM Only — the five mechanical
  subsections (Navigation, Chase, Casualties, two Bastion tables) and Running Notes are wholly new
  content with no existing-prose counterpart to reconcile against.

## Cross-reference / real-wikilink resolution

- `[[la-vasca|La Vasca]]` in source → resolves to `world/locations/calveno-la-vasca.md` (landed
  this same Round 4, commit 7196342, title "La Vasca", subtype district). Real wikilink written as
  `[[calveno-la-vasca|La Vasca]]` — target exists now, per DISPATCH.md wikilink policy (stub-check
  re-run below confirms).
- `[[hcs-surety-owners-manual]]`, `[[surety-missing]]`, `[[kalowe-takowan]]`, `[[port-tidefall]]`,
  `[[uncertainty]]` — all still un-landed; plain text, same relink flags the parent page already
  carries (not re-flagged here to avoid duplicate flag noise — see parent's own queue file
  `ss4-ship-surety-parent.md` § Flags for the authoritative list).
- Delmar Fisk (named in source's "what accelerates the clock" list) — PC, not yet ingested;
  `pcs/jean-claude-tabarnack.md` and `pcs/perrin-black-jaw.md` both already carry
  `relink: delmar-fisk — once his page lands`. Not re-flagged here (same dedup reasoning); written
  plain text, consistent with the parent page's own existing plain-text "Delmar" mention in
  Player-Known.
- Sem Holst, Old Faas, Mr. Thunk (source: "already named — use them" crew) — stub check below,
  no pages found. New relink flags added (## Flags).
- Geoffrey Draves — already relink-flagged on the parent page; dm-guide's one-line callback
  ("ex-Crown carpenter who chose the party") is plain text, no new flag needed.

Stub check (grep -ril, world/ pcs/ prep/):

```console
$ grep -ril "sem holst\|old faas\|thunk\|delmar" world/ pcs/
world/ships/hcs-surety.md            # this page's own existing prose
world/lore/human.md                  # unrelated "thunk"-adjacent false-positive (not checked further, no link written)
world/npcs/estratto.md               # unrelated
world/rules/swashbuckler.md          # unrelated
world/factions/waveservants.md       # unrelated
world/items/delmars-cloak-of-the-manta-ray.md   # Delmar's item, not his own page
pcs/perrin-black-jaw.md              # Delmar relink flag origin
pcs/jean-claude-tabarnack.md         # Delmar relink flag origin
world/items/pearl-of-souls.md        # unrelated
```

No `sem-holst.md`, `old-faas.md`, or `thunk.md`-equivalent page anywhere. No `world/npcs/delmar-fisk.md` either — confirms plain text is correct for all four names here.

## Numeric reconciliation (not a CONTRADICTION — different points in time)

- Hull Points: Stats & Combat table = 120 (at time of capture, from `hcs-surety.md`). Source's
  Crew Casualties table states "Thresholds scaled to 130 HP" — this is the *current* (post-refit,
  Uncertainty-era) total; dm-guide's own frontmatter (`status: active`, "the ship is now sailing
  as the Uncertainty... refit complete") confirms it describes the present, not the capture-time
  snapshot the Stats & Combat table documents. Same reasoning the parent page's own queue file
  already applied to `uncertainty.md`'s divergent 130 HP figure (flagged there as "not a
  contradiction... since neither claims to describe the same point in time") — extended here to
  this second in-family source making the identical distinction. Written as an inline `> [!note]`
  footnote directly above the Crew Casualties table so a future reader doesn't read 130 as an
  error against the 120 above it.
- Upkeep: Stats & Combat table = ~28 gp/week (at capture). Source's Running Notes states "~32
  gp/week is a soft pressure tool" — same current-vs-at-capture distinction, footnoted inline in
  the Running Notes subsection rather than a second `[!note]` callout (lower-stakes number, prose
  parenthetical is enough).

## Flags

- relink: sem-holst — named crew member ("already named — use them"), no `world/npcs/sem-holst.md`
  yet. Plain text in DM Only Running Notes.
- relink: old-faas — named crew member, no page yet. Plain text in DM Only Running Notes.
- relink: thunk — named crew member ("Mr. Thunk"), no page yet. Plain text in DM Only Running
  Notes.
- No CONTRADICTION found. The two numeric deltas (120→130 HP, 28→32 gp/week) are the parent page's
  own already-established at-capture-vs-current distinction, not a new source disagreement — see
  Numeric reconciliation above.
- session-pipeline note (unactioned, flag only): dm-guide's content (chase tables, bastion rolls)
  is DM operational tooling, not a claim any session's `state-changes.md` names — no CANONIZE
  convergence to flag here, unlike the parent's alys-kuiper/estratto corroboration pattern.
