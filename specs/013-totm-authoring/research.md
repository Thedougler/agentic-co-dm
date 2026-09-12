# Research: Theatre of the Mind Authoring

## Decision: `theatre-of-the-mind` owns the outcomes

**Rationale**: 010 already routes player-facing text here. A seventh skill would be a second trigger for the same mouth surface (Constitution VII). A row on the 010 `AGENTS.md` table would spend always-loaded tokens on Beat/layering rules that are not every turn (Constitution IX). Put the testable outcomes on the skill that already fires.

**Alternatives considered**: New `totm-authoring` skill (router-skill smell; steals 010). `AGENTS.md` table (wrong layer; always-loaded). Duplicate the standard into `run-guide` and `session-beats` (sediment; 010 already deleted that pattern). New `docs/agents/totm.md` (extra hop; easy to skip).

## Decision: Outcomes and named failures, not the 18-section method

**Rationale**: Spec FR-031, Constitution VII, 011 Q2. Experts (*Scripting the Game*, Sly Flourish, AbyssalBrews, The Nerdd) already supplied the outcomes in the spec. Requiring dominant-impression → relationships → sensory → features as the only architecture, or word-count floors, or a parallel scene markdown template, is itself a fail. Named failures stay: scripting players; secrets/DCs/unearned names in spoken look; decorative Beat-useless prose; state-dependent openings; Layer 2/3 dumped into the opening; hidden-grid coordinates; turn-by-turn combat scripts; portraits that stage an encounter; traps with no clue in the fiction.

**Alternatives considered**: Paste the user standard as required SKILL.md steps (suffocates; SKILL.md already 34KB). Quote-dump expert articles beside the skill (second competing procedure). Keep per-entity sentence formulas and length floors (pins method; Constitution IV/VII).

## Decision: Prune SKILL.md; do not grow it

**Rationale**: Constitution IX. The current body mixes load-bearing gates (work gate, situated vs standalone, access/hidden truth, no PC scripting) with sediment (sentence-count floors, Strong-echo architecture bans, per-type formula, “you see” on surfaces). Implementation replaces method sediment with 013 outcomes so net tokens fall or stay flat. Specialist refs (`voice.md`, `examples.md`, `places.md`, …) stay examples unless they contradict a named failure. `examples.md` already teaches moves, not sentence order — leave it.

**Alternatives considered**: Append 013 as a new section on top of the hard gates (token spike; two competing procedures). Rewrite every reference file (scope spike; most are examples). Delete standalone/situated (loses the wiki-portrait vs scene split the spec names).

## Decision: Wiki portrait is the existing standalone portrait

**Rationale**: Spec US6 is the cold owner-page first impression. The skill already gates that mode when no table state is supplied. Do not invent a third mode. Coverage dimensions (identity, recognizable whole, sensory signature) stay unordered. Length floors as pass/fail go away; telegram that cannot picture the subject remains a fail.

**Alternatives considered**: Separate “wiki portrait” skill branch (duplicate mode gate). Require Beat type on portraits (spec says portraits are not scene scripts).

## Decision: Session 11 slots already hold FR-032 facts

**Rationale**: FR-033. Beat/job, spoken look, Now, zones, clock/zone Narration cells, Be ready for already exist. TotM fills `[!narration]` and Narration cells. It does not emit a parallel scene card. When the job is not a beat card (owner portrait, chat sample), include only the facts that apply and omit empty sections.

**Alternatives considered**: Require the spec §17 markdown template on every prepared scene (second cockpit; SC-010 fail). Move tactical reference into TotM (steals 007 DM-facing zones).

## Decision: `run-guide` pass 3 is Layer 1, not a scene-stock dump

**Rationale**: Current pass-3 / Initial Narration completion demands every currently perceivable subject in the opening. That collides with FR-013. Zone rows, clock ticks, and other stubs are already the reveal surface. Change that completion line only. Keep four-pass order and empty stubs on passes 1–2. `session-beats` keeps the chart.

**Alternatives considered**: Redesign the cockpit to add Reveal Blocks headings (second template). Leave the dump rule (spec fail). Teach layering only in TotM and leave run-guide contradicting it (two procedures).

## Decision: Relational bands in player-facing look; feet stay on DM zones

**Rationale**: Spec FR-020 vs 007 assumption. Spoken look uses Melee / Near / Far (surfaces.md already has near/far/block). Beat-card Zones may keep feet and compass for DM scan. Exact distance in spoken look only when the fiction makes it perceptible and decision-constraining. Combat opening is TotM; turn-by-turn and top-of-round scripts stay forbidden (run-guide already has no Round script).

**Alternatives considered**: Convert Zones to bands only (breaks 007 scan grammar). Put coordinates in spoken look “for clarity” (hidden grid). Prewrite combat updates (FR-002 fail).

## Decision: Quickstart is the behavioral test; method-pinning evals drop

**Rationale**: Constitution IV. Observe agency, Beat job, state-independence, layering, combat facts, portraits, traps. Do not pytest YAML. Existing `evals.json` rows that pin sentence architecture, length floors, or Strong-echo structure are in-scope to delete or retarget at named failures. Do not add a bulk suite. Do not rewrite `legacy/`.

**Alternatives considered**: Keep architecture-pinning evals (locks the method 013 forbids). Scanner over wiki `[!narration]` (SC-009 fail).
