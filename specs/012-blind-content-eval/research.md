# Research: Blind Cold Evaluation of D&D Content

## Decision: A new eval skill, not a script suite

**Rationale**: Spec FR-003 — file-shape checking cannot pass the change. This repo's product is creative Work. Constitution IV wants tests at public seams; the seam here is a DM-usable page and speakable look, which a second cold judge can observe. pytest over markdown cannot score appropriate use or TotM quality without becoming a method prescription (Constitution VII).

**Alternatives considered**: Expand `impl-validator` (it checks spec match, not table copy). pytest + golden files (form only; fails FR-003). Human-only review with no skill (no trigger; variance).

## Decision: Author and evaluator are different jobs

**Rationale**: FR-002. The authoring session is contamination. `writing-for-agents` tells the author when they are done (dispatch two cold evals). `blind-content-eval` is what those evals load. Same-session self-review is not this test. Host isolated dispatch (no authoring transcript, no skill diff) is the environment — do not write a runner.

**Alternatives considered**: Same-session "now critique your output" (not blind). New omp agent file plus a skill (two mechanisms). Put the whole rubric in `AGENTS.md` (always-loaded; Constitution IX).

## Decision: Rubrics stay on existing authorities

**Rationale**: 010 already owns DM copy (`copy-writer`), spoken look (`theatre-of-the-mind`), vault form (`obsidian-markdown` + `wiki/AGENTS.md` Layout). The eval skill names axes and fail modes, then loads those. Restating them is sediment.

**Alternatives considered**: A new quality essay in the eval skill (duplication). A numeric rubric 1–5 (false precision; suffocates).

## Decision: Two independent pass/fail judgments, omit inapplicable axes

**Rationale**: Spec FR-010 / FR-009. Pass/fail per applicable axis. Disagreement → not done. A spoken-only handout does not fail mechanical form. Do not invent a weighted score.

**Alternatives considered**: One evaluator (self-review smell). Majority of three (extra tokens; not required). Required all four axes on every sample (fails FR-009).

## Decision: Sample Work is the judged object

**Rationale**: Spec assumption. Changing a skill is the event; the test is content that skill now produces, not the skill file's own prose as DM copy. Author produces one sample from the changed guidance, then evals see only that sample plus the kind it claims.

**Alternatives considered**: Judge the skill diff (not the product). Judge every wiki page (out of scope; FR-011).

## Decision: Quickstart is two cold passes on fixture jobs

**Rationale**: Constitution IV. Observe that scripts-alone cannot pass; that two isolated judges can pass/fail the contract jobs; that omitted axes are omitted. Do not rewrite `legacy/`.

**Alternatives considered**: CI job that shells out to an LLM judge (new automation surface; not asked). Scanner over `wiki/` (SC-007 fail).
