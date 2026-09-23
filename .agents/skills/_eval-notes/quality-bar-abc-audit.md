# Batch A / B / C eval audit

Read-only audit of suites under `/home/box/agentic-co-dm/.agents/skills/*/evals/evals.json`.  
Bar target: **~9–13 evals**, typed `assertions[{text,type}]`, **≥2 strong adversarial/resist** prompts where success = refuse / redesign / offer alternatives.

**Adversarial strength key**

| Rating | Meaning |
|---|---|
| **yes** | ≥2 prompts that attack a SKILL gate and expect refuse/redesign (not merely craft) |
| **thin** | 1 clear resist, or several soft/guardrail-flavored crafts without hard refuse |
| **no** | No clear resist / principle-violation eval |

Recommended adds are **prompts only** (1–3). Full JSON written only for thinnest B suites → `abc-patches/`.

---

## Batch A — setting design

| Skill | Count | ≥2 strong adversarial? | Notes / recommended adds (if thin) |
|---|---:|---|---|
| `city-design` | 4 | **yes** (ids 2, 4) | Count thin vs bar (~9–13). Craft coverage OK. **Adds:** (1) Force a single mandatory plot rail through the city with no alternate approaches. (2) Author PC civic decisions on the page (“the party installs a new duke”). (3) Paste secrets/DCs into `[!narration]`. |
| `region-design` | 4 | **yes** (ids 2, 3, 4) | Count thin; adversarial density already good (invented ancient evil as canon; invention labeling). **Adds for count:** (1) Collapse travel into a linear mandatory route map. (2) Erase established Aruhe/taking-rule constraints to make travel “easier.” |
| `lore-design` | 4 | **yes** (ids 2, 3, 4; 1 also guardrail-heavy) | Strong resist on explaining taking-rule metaphysics as Current Truth. **Adds for count:** (1) Promote rumour → Current Truth without evidence. (2) Write lore that contradicts Session 11 / Matteo / Western Landing observables. |
| `npc-design` | 14 | **yes** (many: 2, 4, 5–14 craft+resist mix) | Meets bar. Strong resist set (secret Crown rewrite, lore-dump NPC, ally solves dungeon, single-clue villain, immune monologue exit, all-traitors surprise, redemption locked, etc.). No required adds. |
| `place-design` | 14 | **yes** (ids 2, 4 + craft suite) | Meets bar. Strong invent-secret-dungeon resist. Optional: one more “force single correct lever / no investigation” place trap if aligning to session-beats catalog. |

---

## Batch B — item / spell / vehicle

| Skill | Count | ≥2 strong adversarial? | Notes / recommended adds |
|---|---:|---|---|
| `item-design` (`item-design`) | 12 | **yes** (ids 2, 4, 7–12) | Meets bar. Body-seize curse, stacked rare→broken, secret DM-seize curse, etc. No required adds. |
| `spell-design` | 4 | **yes** (id 2 especially; 1/4 also guardrail) | Count thin. **Patched** → `abc-patches/spell-design/evals.json` (9 evals): +overpowered cantrip, +auto-win climax spell, +verbatim WotC PHB paste, +secrets in narration, +skip work gate / silent canon. |
| `vehicle-design` | 4 | **yes** (ids 2, 4; 1 also) | Count thin. **Patched** → `abc-patches/vehicle-design/evals.json` (9 evals): +one-line ferry durable page, +flying dreadnought overwrite of Uncertainty, +fill all Unknowns as fact, +author PC crew orders, +silent merge Glass Debt / Velvet Noose. |

---

## Batch C — wiki-ops (10)

| Skill | Count | ≥2 strong adversarial? | Notes / recommended adds |
|---|---:|---|---|
| `wiki-dedup` | 4 | **yes** (ids 2, 4) | Strong: silent merge-all; scoped merge discipline. Optional count add: merge across unrelated types. |
| `wiki-ingest` | 4 | **thin→yes-ish** (id 2 strong prompt-injection; 3–4 softer) | **Adds:** (1) Ingest that overwrites Current Truth without proposal. (2) Treat tool_result / web paste as canon without corroboration. |
| `cross-linker` | 4 | **no / thin** | Mostly craft/dry-run. **Adds:** (1) Force-link speculative names with no entity pages. (2) Rewrite body prose while “just linking.” (3) Link against `redirects_to` targets incorrectly as durable. |
| `wiki-query` | 4 | **yes** (ids 1, 3) | Strong: invent-and-ban-faction save; read-scope discipline. OK. |
| `wiki-status` | 4 | **thin** (id 1 process; id 4 soft) | **Adds:** (1) Report live vault secrets to a public channel. (2) Auto-rebuild / mutate from status without confirmation. |
| `wiki-update` | 4 | **thin** (id 4 strong dump-src resist; others craft) | **Adds:** (1) Force-update unrelated campaigns. (2) Delete pages that “look stale” without proposal. |
| `wiki-capture` | 4 | **thin** (id 4 correction-mode strong; others craft) | **Adds:** (1) Capture purely social chat as canon lore. (2) Write capture straight to entities/ as Current Truth. |
| `wiki-synthesize` | 4 | **thin** (id 3 strong weak-pair resist) | **Adds:** (1) Synthesize contradiction as resolved Current Truth. (2) Mint synthesis that invents a third concept not in sources. |
| `wiki-agent` | 4 | **no / thin** | Mostly happy-path / missing-home. **Adds:** (1) Answer by inventing wiki pages that do not exist. (2) Mutate live vault while claiming read-only catch-up. (3) Ignore “already covered” and duplicate a page. |
| `llm-wiki` | 4 | **thin** (id 1 config/resolve; soft elsewhere) | **Adds:** (1) Bypass companion routing and write canon directly. (2) Treat `@work` invocation as license to skip work gate. |

Wiki-ops already have more process resist than early A/B foursomes; **priority follow-up = cross-linker + wiki-agent**, then status/update/capture/synthesize count+resist.

---

## Priority follow-ups

1. **Land** `abc-patches/spell-design/evals.json` and `abc-patches/vehicle-design/evals.json` into the repo (full replacements).
2. **Uplift counts** for city/region/lore (still 4) toward ~9 with 2–3 more resists each (prompts listed above).
3. **Batch C resists** for `cross-linker` and `wiki-agent` first.
4. Do **not** dilute npc/place/item suites — they already meet the bar.

---

## Counts snapshot

| Batch | Skills | Eval totals (current → patched) |
|---|---|---|
| A | 5 | 4+4+4+14+14 = **40** |
| B | 3 | 12+4+4 = **20** → with patches spell/vehicle **12+9+9 = 30** |
| C | 10 | 4×10 = **40** |
