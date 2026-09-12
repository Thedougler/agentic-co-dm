# Research: Session Beat Skills

## Decision: Keep `session-beats` as the composition skill

**Rationale**: Its description already fires on planning a session, one-shot, adventure arc, or expedition evening (spec US1). 007 already assigned composition and the filed spine to it. Renaming to `composing-beats` would duplicate the Campaign OS skill name and force every caller to move for no behavior change.

**Alternatives considered**: New `composing-beats` beside `session-beats` (two composition skills). Rename `session-beats` (churn; 007 spine owner moves). User-invoked router (type skills could not load each other; SKILL-MECHANICS).

## Decision: Five new type skills named after the type

**Rationale**: Spec FR-004 — Hook, Development, Cliffhanger, Climax, Resolution. Names `hook-beats`, `development-beats`, `cliffhanger-beats`, `climax-beats`, `resolution-beats` use the type as the leading word. They do not collide with Campaign OS `writing-*-beats` if those directories are still discoverable.

**Alternatives considered**: One skill per RTG card (~50 skills; FR-004 forbids; Constitution IX). Reuse `writing-hook-beats` etc. (second system, different domain). Fold cards into `session-beats/references/` only (blob remains; agents still load all cards).

## Decision: Do not port Campaign OS composing/writing-*-beats

**Rationale**: `.claude/skills/composing-beats` and `writing-*-beats` teach Situation/Gravity/Irrigation, not the RTG Beat Chart already adapted in `session-beats`. Spec out of scope: a second pacing system. `writing-beats` under `.agents/skills/` is an article-journey skill (`disable-model-invocation`); leave it.

**Alternatives considered**: Copy those skills into `.agents/skills/` (imports a competing procedure). Merge their card lists into RTG cards (duplicate SoT).

## Decision: All six skills are model-invoked

**Rationale**: The agent must reach composition when planning a session, and a type skill when writing/editing/filling that type. Skills must load each other at named seams. User-invoked skills cannot be fired by other skills (SKILL-MECHANICS). Six always-loaded descriptions is the cost of independent reach; worth it versus one blob.

**Alternatives considered**: Only `session-beats` model-invoked (type skills unreachable at seams). Seventh router skill (Constitution VII/IX; extra trigger).

## Decision: Cards live with their type; chart lives with composition

**Rationale**: FR-006 / SC-007. `beat-types.md` is the blob. Split cards into per-type disclosed reference. Composition keeps agency, skeleton, filed-spine jobs, polarity, budget, threads, recompute. Type skill keeps purpose, completion test, cards, how to fill this beat. Pointers, not copies.

**Alternatives considered**: Keep `beat-types.md` as shared reference both load (agents still open the full catalog). Duplicate card summaries in composition (SoT split).

## Decision: Named seams are the only cross-load

**Rationale**: Spec FR-008. Composition filling a typed slot; typed-beat job that needs chart position/polarity/threads/transition; Play a Cliffhanger as Hook; Play a Development as Hook; handoff that must name the next type. Any other second catalog is a defect.

**Alternatives considered**: Always load composition with every type skill (blob). Type skills inline the full chart (FR-006 fail).

## Decision: `AGENTS.md` holds one routing table

**Rationale**: Same pattern as 010 writing authorities. Sessions that never open `session-beats` still need to pick the right skill. `.omp/AGENTS.md` imports `AGENTS.md` — do not copy the table. `wiki/AGENTS.md` already points spine to `session-beats`; keep that. Description of each type skill carries its write/edit/fill branches.

**Alternatives considered**: Routing only in skill descriptions (misses sessions that do not match). Duplicate table in `.omp/AGENTS.md` (Constitution IX). New `docs/agents/session-beats.md` procedure file (extra hop for a table that fits in `AGENTS.md`).

## Decision: Implementation is design-impact

**Rationale**: Creating five skills and changing `session-beats` trigger/ownership/standing load are the four 016 bullets. Session agent writes a scoped prompt; designated writer lands the skills. Pointer retargets that only swap a skill name without changing who does the step may be `not` — classify per 016. Spec, plan, and this research are out of scope for dispatch.

**Alternatives considered**: Session agent drafts the six skills (016 FR-007 fail). One unbounded rewrite of every pacing skill (scoped-prompt bound fail).

## Decision: Quickstart observes routing, not file internals

**Rationale**: Constitution IV. Classify the contract jobs. A planning job produces a valid chart without type-card catalogs. A typed-beat job does not open the other four catalogs unless a named seam fires. After the split, no skill contains both the full chart and all five catalogs. Do not require rewriting Session 11 to prove it.

**Alternatives considered**: pytest over SKILL.md strings (implementation-coupled). Require a live session to be composed as the only proof (slow; still needed later at implement).
