# Batch A eval citations

Written under `/workspace/batch-a-evals/` only. Source skills live in
`/home/box/agentic-co-dm/.agents/skills/{city,region,lore,npc,place}-design/`
and were **not** modified.

## Lint / path note

Exemplars are **best-available live pages**. Several are lint-dirty
(double `---` YAML openers, broken links, pre-template shape, e.g.
`river-slack-basin.md`, `cutoff-lip.md`, `calven-and-calveno.md` as
`kind:settlement`). Graders must score **output template conformance**,
not current vault lint-clean status. Wiki Linter / later cleanup may swap
paths; update this file when paths move.

Pattern bar: `.agents/skills/faction-design/evals/evals.json` (typed
`assertions` only; no `expectations` string arrays).

---

## city-design

| | Path |
| --- | --- |
| **Template** | `wiki/templates/city.md` (`type: place`, `kind: city`; no `city.yml`) |
| **Improve** | `wiki/entities/place/calven-and-calveno.md` |
| **Resist invent** | same Calveno page (plague/siege prompt) |
| **Create fixture** | Saltspire Haven (labeled invention) |
| **Flesh stub** | `wiki/entities/place/Mercatura.md` (preserve Otar / Solange / S1 closed bombs) |
| **Linked canon** | Tessarine Concordat, Dravosi Crown, Warren, Passage, Simone, Lavinia Sordi |

**Eval count:** 4

---

## region-design

| | Path |
| --- | --- |
| **Template** | `wiki/templates/region.md` + `wiki/templates/contracts/region.yml` |
| **Improve** | `wiki/entities/region/aruhe.md` |
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
| **Improve** | `wiki/entities/lore/taking-on-aruhe.md` |
| **Resist invent** | metaphysics / “real answer” prompt on taking rule |
| **Create fixture** | Pier-Debt Custom (labeled invention) |
| **Flesh stub** | `wiki/entities/lore/taken-whole.md` (do not promote rumour to Current Truth; alt: `red-wake.md`) |

**Eval count:** 4

---

## npc-design

| | Path |
| --- | --- |
| **Template** | `wiki/templates/npc.md` (`role` ∈ `rival` \| `patron` \| `contact`) |
| **Improve** | `wiki/entities/npc/nona-black-jaw.md` (preferred over `varn.md`) |
| **Resist invent** | Nona Crown-agent / betrayal prompt |
| **Create fixture** | Kell Drift (labeled invention) |
| **Flesh stub** | `wiki/entities/npc/mave-sorn.md` (Velvet Noose broker) |
| **Alt improve** | `wiki/entities/npc/master-kyzil.md` (not used in suite; available swap) |

**Wiki-template evals:** ids 1–4  
**Craft evals converted to assertions:** ids 5–14 (incidental scale, no lore-dump, persuasion≠mind control, limited ally, redundant clues, no cutscene immunity, rare betrayal, active villain plan, no PC-sheet boss, no predetermined redemption)  
**Dropped vs old suite:** blank-Multiattack-only boss (overlaps PC-sheet reject); standalone want/leverage/need (covered in improve quality)

**Eval count:** 14

---

## place-design

| | Path |
| --- | --- |
| **Template** | `wiki/templates/place.md` (+ `contracts/place.yml`) |
| **Improve** | `wiki/entities/place/print-braid.md` (best template-aligned) |
| **Resist invent** | Print Braid east neighbor / secret dungeon prompt |
| **Create fixture** | Cinder Ford (labeled invention) |
| **Flesh stub** | `wiki/entities/place/high-eyrie.md` (Sentinels / Drowned Maw; Where NESW + gaps) |
| **Also cited** | `river-slack-basin.md`, `cutoff-lip.md` (region/place cluster) |

**Wiki-template evals:** ids 1–4  
**Craft evals converted:** ids 5–14 (kernel/promise, topology graph, triple clue vectors, obstacle counterplay, inhabited factions+moves, location moves, high-tier capabilities, enemies-vanished, surreal reliable rule, cardinal Where filing)  
**Dropped vs old suite:** identical corridor-branch fork (covered by topology); mural-opening dump (covered by place.md narration on improve); settlement-vs-dungeon contrast (deferred to city/region skills)

**Eval count:** 14

---

## Judgment calls

1. **Calveno `kind:settlement`:** improve target asserts finished output `kind: city` / city.md structure; live page kind is not the pass bar.
2. **Nona over Varn:** audit steer; Varn remains a thin lock-keeper but Nona is the completeness exemplar.
3. **taken-whole over red-wake:** clearer rumour-vs-truth split for the flesh guardrail.
4. **Midchain as region flesh:** content-rich but wrong shape; good “restructure to region.md” case without inventing a thinner region from scratch.
5. **Craft caps:** npc and place held at 14 by dropping weakest overlaps listed above.
6. **Graders vs lint:** prompts explicitly say do not treat vault lint noise as skill failure.

## Post-author update

Main advanced to `9c60209` (Lint-clean Phase 2 exemplars: Aruhe and Calven link retargets #136) after these suites were authored. Exemplar paths unchanged; link targets may be cleaner. Graders still score output template conformance, not live lint-clean status.
