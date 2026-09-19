# Batch B eval citations (entity design)

Written under `/workspace/batch-b-evals/` only. Source skills live in
`/home/box/agentic-co-dm/.agents/skills/{dnd-5e-magic-item-design,spell-design,vehicle-design}/`
and were **not** modified. Do **not** treat this folder as authorization to
edit `/home/box/agentic-co-dm` until explicitly told.

Will become `.agents/skills/_eval-notes/batch-b-citations.md` when promoted.

Pattern bar: `.agents/skills/faction-design/evals/evals.json` and
`city-design/evals/evals.json` (typed `assertions[{text,type}]` only; no
`expectations[]` string arrays). Types used:
`content` | `structure` | `process` | `guardrail` | `quality`.

Audit input: `/workspace/eval-audit/batch-b-entity-report.md`.

---

## Deferred mapping (digest note)

| Template | Correct owner skill | Notes |
| --- | --- | --- |
| `wiki/templates/hazard.md` (flora hazard; `type: item`, `kind: flora hazard`) | **`dnd-5e-magic-item-design`** | Flora-hazard **page** authorship belongs here — **not** `traps-trials`. Batch B **narrowed** this suite to `item.md` only; flora-hazard template evals are **deferred** (optional later fold-in). |
| `wiki/templates/creature.md` | **`homebrew-monsters-5e`** | Creature page authorship — **not** authored in this Batch B pass. |
| — | *(none)* | **No** `hazard-design` or `creature-design` skills exist. Do not invent those skill folders to "complete" the mapping. |
| traps / challenge craft | `traps-trials` | Challenge telegraph/counterplay — must **hand off** flora-hazard frontmatter to item-design; no `hazard.md` structure ownership. |

**Out of scope this pass (CoS Batch B narrowed):** creature / hazard / homebrew-monsters / traps-trials eval authorship.

---

## dnd-5e-magic-item-design

| | Path |
| --- | --- |
| **Template** | `wiki/templates/item.md` (+ `contracts/item.yml`) |
| **Improve** | `wiki/entities/item/fate-spinner.md` (preferred). Alt exemplar: `pearl-of-souls.md` (plot/artifact; citation only). Craft-rich ref: `blade-of-the-lost-grip.md`. |
| **Resist invent** | same Fate Spinner — secret body-control curse + Sentinels-as-forgers provenance as silent canon |
| **Create fixture** | Tideglass Compass (labeled invention) |
| **Flesh stub** | `wiki/entities/item/black-lotus-heart.md` (preferred). Alt: `bent-offering-farthing.md` |
| **Linked canon (improve)** | `crissdalynn-khinriss`, `master-kyzil`, `delmar-fisk` / `red-lady` attunement, Changed Record, `talon-skarn` Session 11 Held at `river-slack-basin`, `sentinels-of-the-eyrie` non-intervention tension |
| **Linked canon (flesh)** | Black Lotus / Aruhe harvest context only — no ecology rewrite as canon |

**Wiki-template evals:** ids 1–4  
**Craft evals converted to typed assertions:** ids 5–12  
(pitch-before-mechanics, comparator-matrix, power-envelope-trade, once-per-turn-rider, spell-access-and-concentration, cursed-player-agency, party-role-and-travel, combining-rares)

**Dropped vs old 12 (weakest / redundant):**  
`current-research-not-memory` (folded into comparator process); `sentient-and-evolving`; `legacy-2014-recalibration`; `published-benchmarks-not-fluff` (style meta).

**Eval count:** 12 (4 wiki-grounded + 8 craft extras; ≥4 wiki-grounded met)

**Flora / hazard.md:** ownership affirmed above; **no** hazard.md structure eval in this suite (narrowed to item.md).

---

## spell-design

| | Path |
| --- | --- |
| **Template** | `wiki/templates/spell.md` (+ `contracts/spell.yml`) |
| **Improve** | **Labeled work fixture** in prompt: *Saltwake Veil* (no live `type: spell` pages; no `wiki/entities/spell/` folder) |
| **Resist invent** | Ancient Aruhe druids created the taking rule as canon — ground resistance in `wiki/entities/lore/taking-on-aruhe.md` (fallen vs living claim). Do **not** invent `ancient-druids-taking-spell` as vault canon. |
| **Create fixture** | Ledgerbind (labeled invention) |
| **Flesh stub** | **Labeled stub fixture** in prompt: *Red Wake Knell* |
| **Explicit non-exemplars** | `wiki/entities/item/spell-scroll-*.md` — **items**, not spell pages |
| **Storage path judgment** | SKILL text says `wiki/<campaign>/spells/`; vault siblings use `wiki/entities/{item,vehicle}/`. Evals assert work gate + `type: spell` + template shape; allow proposing either durable path without silent canon. |

**Eval count:** 4 (all wiki-template themes; improve/flesh use labeled fixtures)

---

## vehicle-design

| | Path |
| --- | --- |
| **Template** | `wiki/templates/vehicle.md` (+ `contracts/vehicle.yml`) |
| **Improve** | `wiki/entities/vehicle/Uncertainty.md` (existing eval subject; partial Sheet) |
| **Also cited (shape refs)** | `red-lady-dead-lady.md`, `hcs-ordinance.md` (template-shaped / Crown warship practice — not primary improve) |
| **Resist invent** | same Uncertainty — hidden cannons / ram / enchanted sails as silent canon |
| **Create fixture** | Cobalt Receipt (labeled invention) |
| **Flesh stub** | `wiki/entities/vehicle/glass-debt.md` (preferred). Alt: `velvet-noose.md` |
| **Linked canon (improve)** | HCS Surety rename; Gargantuan AC 11 / 130 HP; La Vasca / Calveno (`calven-and-calveno`) refit; crew Geoffrey Draves, Sem Holst, Alys Kuiper, Old Faas, Thunk, Noor; Aruhe movement; `hcs-ordinance` interception; Thunk cannon *credit* ≠ sheeted weapons |
| **Linked canon (flesh)** | `central-strait` sighting; Crown patrol break; `velvet-noose` link |

**Eval count:** 4

---

## Counts summary

| Skill | Evals | Wiki-template (improve/resist/create/flesh) | Craft extras |
| --- | ---: | ---: | ---: |
| dnd-5e-magic-item-design | 12 | 4 | 8 |
| spell-design | 4 | 4 | 0 |
| vehicle-design | 4 | 4 | 0 |
| **Total** | **20** | **12** | **8** |

Schema: all suites use `skill_name` + `evals[{id,prompt,expected_output,assertions[{text,type}]}]` — **no** `expectations[]`.

---

## Judgment calls

1. **Fate Spinner over Pearl of Souls for item improve:** Fate Spinner already has runnable Changed Record mechanics + holder/attunement canon matching item.md jobs; Pearl of Souls is plot/artifact with narrative effect and no balance numbers — better as citation than primary improve. Blade of the Lost Grip remains craft-rich reference, not the vault improve primary.
2. **Black Lotus Heart over Bent Offering Farthing for flesh:** Heart has Aruhe/Black Lotus harvest hook that can ground a proposed consumable/magic effect; Farthing is intentionally mundane superstition (weaker "flesh toward runnable item" case). Farthing kept as alt.
3. **Spell improve/flesh as labeled fixtures:** Zero live `type: spell` pages; seeding vault pages would modify `/home/box/agentic-co-dm` (forbidden). Fixtures live only in prompts, explicitly non-canon.
4. **Spell storage path:** Assert template + frontmatter + work gate; do not hard-fail on `wiki/<campaign>/spells/` vs `wiki/entities/spell/` until campaign convention is decided — both acceptable proposals.
5. **Uncertainty Unknown lines:** Improve eval requires leaving blank speed/weapons/component numbers Unknown or labeled invention — matches live page honesty. Thunk's cannon credit stays crew pressure, not a Weapons row presented as canon.
6. **Glass Debt over Velvet Noose for vehicle flesh:** Same thin sighting stub pattern; Glass Debt named first in steering; Velvet Noose acceptable alt (same Strait/Crown canon).
7. **Craft cap at 12 for item:** Converted 8 strongest mechanical themes to typed assertions; dropped 4 weakest/redundant from the legacy 12. Wiki-grounded floor (≥4) met by ids 1–4.
8. **hazard.md deferred, not reassigned:** Still owned by `dnd-5e-magic-item-design` for flora pages; traps-trials must not claim it. Not authored here because Batch B narrowed to `item.md`.
9. **Graders vs live completeness:** Score **output** template conformance; live Uncertainty / Fate Spinner / stubs may be pre-template or partial — that is expected for improve/flesh inputs.
