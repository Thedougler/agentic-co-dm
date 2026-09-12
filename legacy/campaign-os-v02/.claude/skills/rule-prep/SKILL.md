---
name: rule-prep
description: Design homebrew D&D 5e rules content — a class, subclass, background, spell, feat, species, condition, or house-rule subsystem — in a Campaign OS repo. Use for "homebrew a subclass", "design a spell for [PC]", "I want a new class", "make a homebrew feat", "this needs a house rule". Not an item (item GUIDE) or creature (monster GUIDE).
---

# Rule Prep

Prep family, Phase 1 (PREP). Turns "I want a subclass that does X" into a
template-conforming, DM-approved homebrew rule—mirrors `.claude/skills/draft-content/references/item.md`'s shape
exactly (`vault/_templates/_srd/_rule.md` mirrors `vault/_templates/_srd/_item.md`'s
`## Mechanics` / `## Provenance` structure), adapted for mechanics a
character *builds around* rather than carries. Cites
`.claude/skills/composing-beats/references/runtime-surface.md`, `.claude/skills/composing-beats/references/audits.md`,
and `vault/refs/homebrewing-mechanics.md` (the flavor-first/SRD-splice/
iterate/edge-test/party-utility method run before any mechanic is designed —
Hard Rule 4) throughout instead of restating their rules; this file and its
`references/*.md` cover only what's specific to rules content.

## Subtype routing

A rule's `subtype` is one of: `class | subclass | background | condition |
subsystem | spell | feat | species`. Set it in frontmatter during the
interview; the template pre-fills `subsystem` as a placeholder — always
set the real value, never leave the default by accident.

- **`class`, `subclass`** → `references/class-design.md` — a subclass is
  designed against its base class's anatomy, so both routes share one file.
- **`spell`** → `references/spell-design.md`.
- **`species`** → `references/species-design.md`.
- **`feat`, `background`, `condition`, `subsystem`** →
  `references/minor-subtype-guidance.md` — none of these four carries
  enough design math for its own file.

## Standard queries

Run before creating anything, and again before writing any prose that
names another established entity:

```
grep -ril "<rule name/concept>" vault/ 2>/dev/null
grep -rl --include=transcript.md -i "<rule name/concept>" vault/episodes/ 2>/dev/null
```

(Two commands, not one glued together — per
`.claude/skills/world-update/references/shell-safety-notes.md`.)

A hit on the first query is the stub check (`.claude/skills/composing-beats/references/runtime-surface.md` §1):
expand that page in place, never create a duplicate. A hit that's an
existing RAW option with the same fantasy beats inventing a homebrew one
— reskin or lightly modify it (Hard Rule 1). Empty output is informative:
nothing established yet, invent freely within the rails. Empty or noisy
output never concludes "doesn't exist" — escalate up the `llm-wiki-query`
skill's tiers first (`npm run search:content -- search "<terms>"` keyword,
then `-- query` semantic; skill contract item 1 — the entity may live
under an alias or different wording).

## Owned paths

Instantiated from `vault/_templates/_srd/_rule.md` — copy it, don't retype it from
memory. `status: draft` while incomplete, `status: pending` only after the
DM Review Gate (Hard Rule 7) is satisfied. Never writes to `vault/srd/rules/`
directly (`transcript-ingest` moves prep → world, once played) and never
sets `status: canon` or `publish: true`.

## Hard rules

1. **About to create anything → run Standard queries above.** A
   lightly-reflavored existing class/subclass/spell/feat/species with the
   same fantasy always wins over a new design — only build new when the
   fantasy or mechanical niche genuinely isn't satisfiable by existing
   content.
2. **About to write `pc_connection` with nothing named → stop, name it.**
   Never a silent default (`.claude/skills/composing-beats/references/runtime-surface.md` §2) — name the specific PC
   building a character around this rule, or the DM's own reason for
   adding it as a house rule available to the whole table. Lands in
   `pc_connection`, not just working notes.
3. **About to design any feature for a `class` → pass the Niche Test
   first.** All three questions in `references/class-design.md` § The
   Niche Test before any feature is designed — a "no" to any means the
   concept is a subclass, background, or feat instead (§ Subtype
   routing). About to design mechanics for any other subtype → state its
   core fantasy in one sentence before mechanics (mirrors
   `.claude/skills/draft-content/references/item.md`'s One-Thing Discipline).
4. **Before designing any mechanic → read `vault/refs/homebrewing-mechanics.md`**
   for the flavor-first/SRD-splice/iterate/edge-test method. **About to
   balance any design → cite a named comparable, never
   vibes.** Every subtype's reference file states the relevant benchmark
   table — cite 2 real published comparables (or the specific benchmark
   row for a `class`/`subclass`) and confirm comparable power. Clearly
   stronger → scale down the design, don't shrink the citation.
5. **About to design a `subclass` → read the base class's trap column
   first.** `references/class-design.md` § Subclass benchmarks' "Watch
   out" column for the base class before designing — Aura of Protection,
   Sneak Attack frequency, and ki-starvation are named traps a new
   subclass can trip.
6. **About to write any effect under `## Mechanics` → bound it and label
   it.** Label each effect `**[HB]**` or `**[RAW]**`; state action cost,
   range, duration, and recovery (long rest / short rest / X charges /
   at-will) explicitly — an unbounded power is the single most common
   balance mistake here, same as `.claude/skills/draft-content/references/item.md`'s own finding.
7. **About to flip `status:` from `draft` to `pending` → present and wait
   for approval first.** Present the core fantasy/niche (Hard Rule 3),
   the balance citation (Hard Rule 4), and any subclass trap checked
   (Hard Rule 5); wait for approval. A misbalanced class-level option is
   harder to retract once a PC has built around it than an item is —
   leave `status: draft` if stopping before approval; never invent an
   approval.
8. **About to write any part of the page → sandbox discipline binds it.**
   Describe what the rule *is* and does; never write what a PC decides,
   feels, or wants about having it (`.claude/skills/composing-beats/references/audits.md` §1).
9. **About to finalize the page → read the flavor description back
   first** (`.claude/skills/composing-beats/references/runtime-surface.md` §6).
10. **About to set `status:` past `pending` or touch `publish:` → stop.**
    That's `transcript-ingest`'s move, triggered by the content actually
    reaching the table.
11. **About to guess on a gap the interview didn't answer → stop, ask
    instead.** See § Degrade by asking.

## Interview

Ask every uncovered item below at once, never serially (`.claude/skills/composing-beats/references/runtime-surface.md` §2):

- Which subtype — class, subclass, background, spell, feat, species,
  condition, or subsystem (§ Subtype routing)?
- Which PC is this for, or is it a DM house rule for the whole table? (Hard Rule 2)
- What's the core fantasy or mechanical niche, in one sentence? (Hard Rule 3)
- For a `subclass`: which base class, and at what level (3rd/6th/10th/14th or the class's own unusual slot)?
- For a `spell`: what slot level, and is it meant to be concentration?
- Is there an existing RAW option this could reskin instead? (Hard Rule 1)

## Output structure

Fixed H2s for `type: rule`: `## Mechanics`, `## Provenance` — nothing
added, nothing removed, this order. No `## Player-Known`/`## DM Only`
split: `publish:`/`status:` on the page itself is the visibility gate
(`.claude/skills/composing-beats/references/runtime-surface.md` §8, lint W20/W21). Full section-by-section mapping,
the DM-only Toy-equivalent table (`core_fantasy`, `balance_citation`,
`pc_connection`, `subclass_trap_checked`), and the Player-Known/DM-Only
drafting lens: `references/output-structure.md`.

## Degrade by asking

- Interview questions unanswered → ask all at once (§ Interview), never invent the subtype, the PC connection, or the core fantasy.
- Genuinely a DM-wide house rule, no single PC → still worth stating explicitly (Hard Rule 2), not a default; confirm rather than assume.
- Can't state the core fantasy in one sentence → the design isn't ready; ask the DM to narrow it (Hard Rule 3).
- Can't name 2 real comparables → read the SRD/PHB yourself first; if still stuck, ask the DM rather than guessing a power level from vibes.
- DM Review Gate not yet run → leave `status: draft`; never flip to `pending` on an assumed approval.

## Workflow

1. **Interview** (§ above) — gather what's missing, all at once, starting with the subtype.
2. **Standard queries** — stub check + RAW-reskin check. A full-concept hit means reskin and stop; continue only when a genuine new design is warranted.
3. **Instantiate** `vault/_templates/_srd/_rule.md`, `status: draft`, fill `<Name>` and the real `subtype:` value. Coining the rule's name, or 2+ names already in circulation for it? Settle the name first via `campaign-domain-modeling` (canonical term + `_Avoid_` synonyms) — the page carries the mechanic, campaign-domain-modeling owns the word.
4. **Read the matching reference file** (§ Subtype routing) before designing any mechanic.
5. **Fill sections** per § Output structure: DM-only table first (core fantasy, balance citation, PC connection), then Mechanics, then Provenance, then the Player-Known flavor pass last.
6. **Prose pass** (Hard Rule 9), then **DM Review Gate** (Hard Rule 7) — present and wait for approval before flipping `status:` to `pending`.

## Checklist (run before calling the rule done)

- [ ] Standard queries run and pasted; stub check clean, or a RAW reskin was used instead of a fresh design.
- [ ] `subtype:` frontmatter set to the real value, not the template's `subsystem` placeholder (unless `subsystem` is genuinely correct).
- [ ] PC-Connection Requirement (or explicit DM house-rule reason) named in `pc_connection`.
- [ ] Core fantasy stated in one sentence; Niche Test passed if `class`.
- [ ] Balance citation names 2 real comparables, or the specific benchmark row, with confirmed-comparable power.
- [ ] `subclass` only: the base class's "watch out" trap checked.
- [ ] Every effect in `## Mechanics` is `[HB]`/`[RAW]`-labeled, bounded, names its edge cases.
- [ ] Template H2s present, in order: `Mechanics`, `Provenance` — no `## Player-Known`/`## DM Only` heading anywhere on the page.
- [ ] **DM Review Gate run and passed** before `status:` left `draft`.
- [ ] `status:` at `draft` or `pending` only; `publish:` untouched (`false`).

## Creative-domain rider

Facts, canon, structure, and visibility are bound (Hard Rules above, all
CLAUDE.md project rules; `.claude/skills/composing-beats/references/runtime-surface.md`'s own creative-domain rider,
cited not restated). **Prose style is free.** A generic "+1 to everything"
subclass or a timid flavor description that could belong to any option is
a contract violation, not a safe default — push for the specific mechanic
and the specific fantasy over the safe one.

## Out of scope

- A magic item — `.claude/skills/draft-content/references/item.md`'s territory.
- A monster/creature stat block — `.claude/skills/draft-content/references/monster.md`'s territory.
- A named foe's own page, Toy Chest, or villain stat approach —
  the npc guide's territory.
- Anything already `status: canon` — canon-review's territory; this skill
  only ever touches `draft`/`pending` pages.
- Writing `vault/srd/rules/` directly, or flipping `status:`/`publish:` past
  `pending` — `transcript-ingest`'s and PUBLISH's move exclusively.

## Reference files

| File | Read when |
|---|---|
| `references/class-design.md` | `subtype: class` or `subtype: subclass` — the Niche Test, class anatomy, spellcasting classification, feature distribution, core resource design, capstone guidance, per-class subclass benchmarks, feature-level power budget |
| `references/spell-design.md` | `subtype: spell` — the three balance axes, damage/CC/utility/healing benchmarks, upcast scaling, concentration tax, spell-school expectations |
| `references/species-design.md` | `subtype: species` (also the low end of its feature-budget table for a `background`'s single feature) — the feature budget system, worked examples, ASI guidelines, subrace rules |
| `references/minor-subtype-guidance.md` | `subtype: feat`, `background`, `condition`, or `subsystem` — the four subtypes with no dedicated design-math file of their own |
| `references/output-structure.md` | Filling the rule page's sections — the Player-Known/DM-only split, the DM-only Toy-equivalent table field-by-field |
| `references/worked-example.md` | Seeing the full interview-to-page flow worked end to end (fixture, not real campaign content) |
