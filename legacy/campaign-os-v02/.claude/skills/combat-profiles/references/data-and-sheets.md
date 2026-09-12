# Character sheet conversion and session data extraction

Read the relevant half when the main SKILL.md's Workflow sends you here.

## Owned-paths rationale

`vault/campaigns/shattered-sea/pcs/combat-profile/` and `vault/campaigns/shattered-sea/pcs/character-sheets/` sit inside
`vault/campaigns/shattered-sea/pcs/` (a wiki lint root) but carry no page schema of their own —
same precedent as `vault/ideas/`: DM
tooling/derived intelligence, not campaign canon, needs no
canon-review oversight to write or update (nothing here is a fact of
record — it's recomputed analysis, regeneratable from `vault/campaigns/shattered-sea/pcs/*.md` + session
evidence + the sim at any time).
Adapted from an earlier, non-portable version of this same method —
trimmed to what this architecture still needs: the PDF/session-ingest
staging directories that version assumed don't exist here, so every path
below points at what this repo actually has — `vault/campaigns/shattered-sea/pcs/*.md` frontmatter,
`vault/episodes/NNN/transcript.md`, and this skill's own
`vault/campaigns/shattered-sea/pcs/combat-profile/`/`vault/campaigns/shattered-sea/pcs/character-sheets/`.

## Attribute pages

A sheet conversion has two halves. The human-readable half is four governed
wiki pages under `vault/campaigns/shattered-sea/pcs/`, each instantiated from its own template:

| Facet | Path | Template |
|---|---|---|
| Ability scores, saves, skills, speeds, proficiencies | `vault/campaigns/shattered-sea/pcs/stats/{pc-slug}-stats.md` | `vault/_templates/_campaigns/_pcs/_pc_stats.md` |
| Traits, features, actions, bonus actions, reactions, feats | `vault/campaigns/shattered-sea/pcs/abilities/{pc-slug}-abilities.md` | `vault/_templates/_campaigns/_pcs/_pc_abilities.md` |
| Spellcasting, cantrips, known/prepared, slots | `vault/campaigns/shattered-sea/pcs/spells/{pc-slug}-spells.md` | `vault/_templates/_campaigns/_pcs/_pc_spells.md` |
| Attunement, carried gear, caches, currency | `vault/campaigns/shattered-sea/pcs/inventory/{pc-slug}-inventory.md` | `vault/_templates/_campaigns/_pcs/_pc_inventory.md` |

These sit inside the wiki lint roots, so W1/W5/W54 enforce their
frontmatter and heading shape — unlike `vault/campaigns/shattered-sea/pcs/combat-profile/`/
`vault/campaigns/shattered-sea/pcs/character-sheets/`, where nothing does. A
non-caster gets no spells page rather than an empty one.

The machine half is `{pc-slug}-sheet.md`: the source citation, the
`[verify]` flags, and the `## Combatant Block`. It restates nothing the
four pages carry. `ac`, `hp_max`, `class_levels`, and `level` stay in
`vault/campaigns/shattered-sea/pcs/{pc-slug}.md` frontmatter and appear in none of the five.

`last_synced:` on all four attribute pages and the sheet moves together, in
one pass — a page left behind reads as current and is not.

A character sheet is a real fact about a played character, not
speculative prep: `status: canon` is set on write for each of the four
attribute pages, no separate approval step.

## Character sheet conversion

Only needed when a profile requires mechanical detail `vault/campaigns/shattered-sea/pcs/<name>.md`
frontmatter doesn't carry (save bonuses, attack routines, spell lists,
resource pools) and the player has a fuller sheet (PDF or plain text) to
convert. Skip this whole section if frontmatter + Session Log already
cover what the profile needs (SKILL.md Hard Rule 7).

**File:** `vault/campaigns/shattered-sea/pcs/character-sheets/{pc-slug}-sheet.md` — canonical
mechanical reference this skill's own calculations cite. The player's raw
sheet is a reference copy only, never edited; check
`_assets/character-sheets/{pc-slug}-character-sheet.pdf` first (the durable copy
`llm-wiki-ingest` places there per its SKILL.md § Owned paths, when the sheet
arrived that way) before asking the player for it again.

**Reading a PDF sheet:** never a plain Read of the PDF and never any
markitdown-ts-derived `.md` companion — both surface only the static text
layer, silently dropping filled-in form-field values on a fillable-form PDF
(a character-sheet export is exactly this shape, and doing so has produced a
real, corrected error on this page before). Load the `anthropic-skills:pdf`
skill and extract directly: PyMuPDF/pypdf form-field read (`page.widgets()` /
`get_fields()`) for a fillable form, pdfplumber/pdftotext for a plain-text or
scanned sheet.

Frontmatter and section order: `vault/_templates/_campaigns/_pcs/_pc_sheet.md` (single source of
truth for shape).

## Combatant block

The sheet's final section (`vault/_templates/_campaigns/_pcs/_pc_sheet.md` §9) is the
machine-parseable sim input — the same Fantasy Statblocks ` ```statblock ` fence
every NPC and creature uses, with the repo's `sim:` extension namespace
(top-level and per-action) carrying what the native fence vocabulary can't
express. Schema: `utils/dndsim/CLAUDE.md`; worked example with
real numbers: `vault/campaigns/shattered-sea/pcs/character-sheets/perrin-black-jaw-sheet.md`.

Source-tag vocabulary (the single home — SKILL.md Hard Rule 2 points
here): `[sheet]` (the character sheet states it), `[srd]` (read this turn
from a cited SRD page), `[sheet+srd]` (the sheet names the
thing, the page supplies the number — cite the path), `[session-NN]`
(observed at the table), `[calculated]` (agent arithmetic over tagged
inputs), `[simulated]` (copied verbatim from a sim run), `[frontmatter]`
(from `vault/campaigns/shattered-sea/pcs/*.md` frontmatter), `[pcs-page]` (from a `vault/campaigns/shattered-sea/pcs/*.md` body),
`[assumed]` (RAW-derived default where no source picks), `[theoretical]`
(no source at all), `[unknown]` (value genuinely unknowable), plus the
`[verify]` modifier (transcribed as-printed, needs checking).

Build procedure:

1. Every value derives from a line in the sheet's own sections above —
   final numbers, items folded in (an AC that already includes a cloak
   stays folded; don't re-derive from stats).
2. A `[verify]`-tagged sheet value is transcribed as-printed with the tag
   carried into the block as a YAML comment on that line.
3. A value the sheet doesn't state and no in-repo source supplies stays
   OUT of the block — the sim states the exclusion; never fill a gap with
   a plausible number. A value the sheet doesn't state but a cited
   SRD page does (a spell's dice from its SRD page, a
   class feature's numbers from its class page) enters tagged
   `[srd]`/`[sheet+srd]` with the page path recorded on the line — the
   *choice* is the sheet's, the *number* is the page's. What stays
   banned is exactly the plausible-sounding estimate with no source.
4. Attacks and saves go in `actions:`/`bonus_actions:` as SRD-grammar
   `desc:` prose (2014 or 2024 phrasing — both parse). Class features
   become schema primitives, never class names: an inspiration die is a
   `sim.resources` entry + a `reroll_add`/`damage_reduction` reaction on
   the triggering entry; a smite is a `sim.abilities:` `extra_damage`;
   Shield is a `reactions:` entry with `sim: { kind: ac_bonus }`. A heal
   is any action/bonus_action entry with `sim.heal: { dice }`. Anything
   with no primitive goes to the profile's unsimulable list instead.
5. No sheet at all → a low-fidelity block from `vault/campaigns/shattered-sea/pcs/*.md` frontmatter
   (`ac`, `hp_max`, and whatever `## Session Log`/Arc Notes evidence
   supports), with `# low-fidelity` commented at the top of the fence; the
   party profile stamps the caveat on any band built from it.
6. `sim.side: party` is required — this is what makes the sim treat the
   sheet as a PC rather than a monster; the `w-combatant-block` lint rule
   enforces it (and hard-errors on any surviving retired ` ```combatant ` fence)
   on every edit — obey its FIX lines.

**Quality rules:** every number verifiable from the source — a value that
looks wrong (a save that doesn't match ability mod + proficiency) gets a
`[verify]` tag, never a silent "fix" (the player may have an item or
feature not visible in what you're reading). No editorializing — this is
a mechanical reference, not the profile itself; "good for..." commentary
belongs in the combat profile's § Calibration, not here. Skip mundane
equipment (rope, rations); include magic items and anything with a
mechanical effect.

**Keeping in sync:** when a player reports a level-up or a new sheet,
re-read it, diff mentally against what's here, update, bump
`last_synced`, and flag every profile that cites this sheet as stale
(SKILL.md Hard Rule 1's staleness check).

## Session data extraction

Run when updating a profile from real session combat data (SKILL.md
Workflow step 6).

**Source priority:** `vault/episodes/NNN/transcript.md` is this
architecture's one source of truth for what happened at the table (no
staged combat-summary equivalent exists here, unlike the legacy
skill's assumed pipeline) — read the relevant combat scene directly.
A `vault/`/`vault/campaigns/shattered-sea/pcs/` page may already state a fact worth citing instead of
re-deriving it from raw transcript prose.

**Per-PC, per-encounter, extract:** rounds active, total damage dealt,
total damage taken, attacks attempted/hit, saves forced/passed/failed,
resources spent, 1-2 key moments. Per-encounter (party-wide): total
rounds, enemy count/types, estimated CR, outcome, party HP at end.

**Extraction rules:**

1. **Record actuals, not intentions.** "Delmar dealt 17 damage with Sneak
   Attack" is an extraction. "Delmar could deal up to 2d6+4+2d6" is a
   theoretical figure — it belongs in § Combat Stats, not the log.
2. **Mark uncertainty, never invent.** `~14` = approximate; `[unknown]` =
   not stated in the source; `[inferred]` = derived from context ("badly
   wounded" ≈ 50% HP). A number with no source is `[unknown]`, never a
   guessed clean figure (SKILL.md Hard Rule 2 — this is the rule's
   sharpest edge: don't let a plausible-sounding estimate stand in for a
   number you haven't actually confirmed against the transcript).
3. **Record circumstances alongside numbers** — advantaged/disadvantaged,
   ideal conditions for the PC's build, or shut down by something
   specific. This context feeds § Calibration, not just the raw log
   row.
4. **Negative data is data.** A PC who dealt 0 damage, missed every
   attack, or was incapacitated is important — it feeds the Counter
   Profile and the theoretical-vs-observed delta.
5. **Don't double-count a synergy.** If [[perrin-black-jaw|Perrin]]'s Bardic Inspiration turned
   Delmar's miss into a hit: record the damage under Delmar (he dealt
   it), note the inspiration spend under Perrin's § Combat Stats, note
   the combo in both PCs' § Counters & Synergy.

**After appending new log entries:** recalculate observed averages (DPR,
hit rate, damage taken per round), flag any calibration shift worth a
§ Calibration update (observed DPR diverging from theoretical by
>25%, a counter confirmed at table, a synergy confirmed, a new weakness
discovered), and flag the party profile stale if any PC profile changed
(SKILL.md Workflow step 6).

**Handling gaps:** no exact damage numbers → estimate from the monster's
stat block and the described outcome, marked `~`. No round count →
estimate from narrative pacing (most combats run 3-5 rounds), marked `~`.
PC absent from the combat → record `rounds: 0, damage: 0, taken: 0` with
a note, not an omitted row.
