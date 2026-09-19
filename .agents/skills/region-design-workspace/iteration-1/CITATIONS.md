# Batch A eval citations (retarget)

Written under `/workspace/batch-a-retarget/` only. Source skills live in
`/home/box/agentic-co-dm/.agents/skills/{city,region,lore,npc,place}-design/`
and were **not** modified. Do **not** treat this folder as authorization to
edit `/home/box/agentic-co-dm` until explicitly told.

## Lint / path note (Wiki Linter)

Wiki Linter **lint-clean verdicts** (`hard_fail=false`) for preferred
exemplars used by this retarget:

| Kind | Preferred path | Notes |
| --- | --- | --- |
| **city** | `wiki/entities/place/Mercatura.md` (`kind: city`) | Preferred city-design **IMPROVE** |
| **region** | `wiki/entities/region/aruhe.md` | Already OK; still place-kernel body → assert **output** region.md conformance |
| **lore** | `wiki/entities/lore/taking-on-aruhe.md` | Already OK; assert **output** lore.md conformance |
| **npc** | `wiki/entities/npc/varn.md` | Preferred npc-design **IMPROVE** (replaces `nona-black-jaw`) |
| **place** | `wiki/entities/place/high-eyrie.md` | Preferred place-design **IMPROVE** (replaces `print-braid`); alt flesh `river-slack-basin.md` |
| **settlement→city flesh** | `wiki/entities/place/calven-and-calveno.md` (`kind: settlement`) | Linter-clean flesh / upgrade target — **not** primary city improve |
| **faction pattern** | `wiki/entities/faction/sentinels-of-the-eyrie.md` | Pattern bar reference; no faction eval change |

Graders score **output template conformance**, not whether the live vault
page already fills every template section. Pre-template shape (e.g. Aruhe
place-kernel body; Mercatura thin city stub) is expected on improve/flesh
inputs.

Pattern bar: `.agents/skills/faction-design/evals/evals.json` (typed
`assertions` only; no `expectations` string arrays).

---

## city-design

| | Path |
| --- | --- |
| **Template** | `wiki/templates/city.md` (`type: place`, `kind: city`; no `city.yml`) |
| **Improve** | `wiki/entities/place/Mercatura.md` (preferred `kind:city`; expand Arrival / Orientation / Gazetteer / If-nobody-intervenes from existing pressure; preserve Otar / Solange / S1 closed bombs) |
| **Resist invent** | same Mercatura page (do **not** invent plague/siege as canon on Mercatura) |
| **Create fixture** | Saltspire Haven (labeled invention) |
| **Flesh stub** | `wiki/entities/place/calven-and-calveno.md` (`kind:settlement` → upgrade toward `kind:city` / city.md) |
| **Linked canon (flesh)** | Tessarine Concordat, Dravosi Crown, Seven Houses, Warren, Passage, Simone, Lavinia Sordi |

**Eval count:** 4

---

## region-design

| | Path |
| --- | --- |
| **Template** | `wiki/templates/region.md` + `wiki/templates/contracts/region.yml` |
| **Improve** | `wiki/entities/region/aruhe.md` (Linter `hard_fail=false`; still place-kernel shaped) |
| **Linked places** | `wiki/entities/place/river-slack-basin.md`, `cutoff-lip.md`, `print-braid.md` |
| **Resist invent** | Aruhe macro-threat prompt |
| **Create fixture** | Brine Ladder (labeled invention) |
| **Flesh** | `wiki/entities/region/Midchain.md` → region.md shape |
| **Also cited** | `wiki/entities/lore/taking-on-aruhe.md`, razer-grass / ecology on Aruhe |

**Eval count:** 4

---

## lore-design

| | Path |
| --- | --- |
| **Template** | `wiki/templates/lore.md` (+ `contracts/lore.yml` fields) |
| **Improve** | `wiki/entities/lore/taking-on-aruhe.md` (Linter `hard_fail=false`) |
| **Resist invent** | metaphysics / “real answer” prompt on taking rule |
| **Create fixture** | Pier-Debt Custom (labeled invention) |
| **Flesh stub** | `wiki/entities/lore/taken-whole.md` (do not promote rumour to Current Truth; alt: `red-wake.md`) |

**Eval count:** 4

---

## npc-design

| | Path |
| --- | --- |
| **Template** | `wiki/templates/npc.md` (`role` ∈ `rival` \| `patron` \| `contact`) |
| **Improve** | `wiki/entities/npc/varn.md` (preferred; replaces `nona-black-jaw`) |
| **Role fix** | Live frontmatter `role: "Inner lock keeper"` is **wrong** vs template — assert correcting YAML `role` to `contact` (or fitting enum) while keeping craft/job in Nature/body |
| **Resist invent** | Varn Crown-betrayal / rich-biography-as-canon prompt |
| **Create fixture** | Kell Drift (labeled invention) |
| **Flesh stub** | `wiki/entities/npc/mave-sorn.md` (Velvet Noose broker) |
| **Superseded improve** | `wiki/entities/npc/nona-black-jaw.md` (no longer primary) |

**Wiki-template evals:** ids 1–4  
**Craft evals converted to assertions:** ids 5–14 (incidental scale, no lore-dump, persuasion≠mind control, limited ally, redundant clues, no cutscene immunity, rare betrayal, active villain plan, no PC-sheet boss, no predetermined redemption)  
**Dropped vs old suite:** blank-Multiattack-only boss (overlaps PC-sheet reject); standalone want/leverage/need (covered in improve quality)

**Eval count:** 14

---

## place-design

| | Path |
| --- | --- |
| **Template** | `wiki/templates/place.md` (+ `contracts/place.yml`) |
| **Improve** | `wiki/entities/place/high-eyrie.md` (preferred; replaces `print-braid`; Sentinels / Drowned Maw / Crown refusal-without-terms / two-hundred-years hold) |
| **Resist invent** | High Eyrie southern neighbor dungeon-across-gap prompt |
| **Create fixture** | Cinder Ford (labeled invention) |
| **Flesh stub** | `wiki/entities/place/river-slack-basin.md` (preferred alt Linter; basin / cutoff-lip / otter-claim); print-braid no longer primary improve |
| **Cardinal Where** | Eval 14 fixture kept; pattern also applies to high-eyrie / slack-basin |
| **Also cited** | `cutoff-lip.md`, Sentinels roster (`master-kyzil`, apprentices, record-keepers) |

**Wiki-template evals:** ids 1–4  
**Craft evals converted:** ids 5–14 (kernel/promise, topology graph, triple clue vectors, obstacle counterplay, inhabited factions+moves, location moves, high-tier capabilities, enemies-vanished, surreal reliable rule, cardinal Where filing)  
**Dropped vs old suite:** identical corridor-branch fork (covered by topology); mural-opening dump (covered by place.md narration on improve); settlement-vs-dungeon contrast (deferred to city/region skills)

**Eval count:** 14

---

## Judgment calls

1. **Mercatura over Calveno for city improve:** Mercatura is already `kind: city` and the preferred Linter city exemplar; Calveno (`kind:settlement`) moves to **flesh** / settlement→city upgrade.
2. **Varn over Nona:** Linter-preferred improve; assert **role enum correction** (`contact`) while preserving inner-lock craft identity in Nature/body.
3. **High Eyrie over Print Braid for place improve:** Linter-preferred; Print Braid remains a linked Aruhe site but not the vault improve primary. Flesh prefers **river-slack-basin**.
4. **taken-whole over red-wake:** clearer rumour-vs-truth split for the flesh guardrail (unchanged).
5. **Midchain as region flesh:** content-rich but wrong shape; good “restructure to region.md” case (unchanged).
6. **Craft caps:** npc and place held at 14; craft ids left alone unless they hardcoded Nona / print-braid vault improve paths (they did not).
7. **Graders vs lint:** Linter `hard_fail=false` on preferred pages does **not** mean the live page already matches full template fill — score the **output**.

## Post-author / PR note

- **#136** — Lint-clean Phase 2 exemplars (Aruhe and Calven link retargets); main advanced after the original Batch A suites were authored.
- **#137** — merged.
- **This folder** — retarget follow-up only: swap preferred improve/flesh/resist targets to match Wiki Linter clean verdicts above. Skills under `/home/box/agentic-co-dm` untouched.
