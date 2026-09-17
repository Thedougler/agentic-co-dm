# Feature Specification: Hybrid Spec-Driven Development

**Feature Branch**: `021-hybrid-sdd-adaptation`

**Created**: 2026-09-16

**Status**: Draft

**Input**: User description: Adapt the repository-owned Spec Kit layer into a hybrid Spec-Driven Development system for engineering, agent-system, campaign-architecture, and creative-system work while preserving existing wiki, canon, agency, Work, and engineering workflows.

## Clarifications

### Session 2026-09-16

- Q: What should one sitting’s measured trajectory include? → A: Whole useful trajectory: request, loaded context, retrieval, tools, failures, retries, model input/output, and final Work; exclude idle and unrelated activity.
- Q: Which token count should be authoritative when local and provider-reported counts differ? → A: Use each model family’s native tokenizer as authoritative; compare token measurements only within the same model/tokenizer family.
- Q: Where should normal sitting traces be stored and how long should they be retained? → A: Local gitignored JSONL with redacted metadata and token counts only, retained for 90 days; sanitized evaluation fixtures and pinned baselines may be committed.
- Q: Which Co-DM quality requirements must be executable hard gates rather than semantic judgments? → A: Hard-gate canon precedence, entity-before-spoken, DM-facing explicitness, reveal/visibility boundaries, accept-before-write, and objective mechanics/schema checks; use blind semantic evaluation for playability, specificity, continuity, agency, and usefulness.
- Q: What evidence should be required before an optimization is promoted or rolled back? → A: Require pinned paired replay, zero new hard-gate failures, semantic non-inferiority, and material savings; low-risk changes may auto-promote after at least 10 same-kind pairs and a 10% canary, moderate-risk changes require shadow replay and canary review, high-risk changes require human review, and any hard failure or material quality regression triggers rollback.
- Q: When should a fetched page count as materially useful retrieval? → A: Count it as useful when accepted Work explicitly cites or links it, or an independent evaluator confirms that it supplied a required fact, rule, or safety constraint; fetched-but-unused pages count as unnecessary retrieval.
- Q: What minimum metric vector must every efficiency report expose? → A: Total trajectory, input/output, source components, retrieval counts/tokens, retries, hard failures, acceptance, revisions, runtime failures, and labeled derived metrics.
- Q: How should token attribution handle content that belongs to multiple source categories? → A: Assign each measured token occurrence one primary source owner; retain secondary provenance as metadata only and never count the same occurrence twice.
- Q: Which sitting task classes should the initial efficiency system compare? → A: Compare `prep` and `wrapup`; keep audit and replay as metadata rather than separate comparison classes.
- Q: Who should own the efficiency policy and its safety thresholds? → A: Maintainers own the versioned `config/efficiency.yaml`; agents may read and propose changes but may not silently weaken thresholds, gates, or autonomy boundaries.
- Q: How should QMD fallback behavior be recorded when a higher-precedence collection is silent or fails? → A: Log every attempted collection and fallback, preserve wiki → shattered-sea → legacy precedence, and never let fallback material override current accepted canon.
- Q: How should the trace schema evolve without breaking historical reports? → A: Version every trace, support additive evolution, and quarantine incompatible records rather than guessing or rewriting history.
- Q: Should trajectory telemetry be always-on or sampled for normal `prep` and `wrapup` sittings? → A: Collect redacted telemetry for every `prep` and `wrapup` sitting; explicit disablement records a measurement gap.
- Q: What should count as successful Work when efficiency metrics use a denominator? → A: Track produced, accepted, failed, and incomplete separately; exclude failed or incomplete sittings from accepted-Work denominators while retaining their traces and failure reasons.
- Q: Which changes may be autonomous, and which require shadow evaluation or human review? → A: Auto-promote only deterministic low-risk cleanup; require shadow replay and canaries for retrieval, routing, budgets, and tool exposure; require human review for semantic compression, model changes, canon changes, schema changes, instruction redesign, and policy or threshold changes.
- Q: Which request should the minimum seven-case classification run use as Scenario G? → A: A mixed request combining routine campaign content with an agent-system or reusable-system change.
- Q: What evidence should establish semantic non-inferiority when comparing an optimization with its pinned baseline? → A: A blind paired evaluator using a fixed semantic-quality rubric, with no meaningful aggregate quality loss alongside the existing hard gates.
- Q: What should happen before the separate native-tokenizer governance change is accepted? → A: Collect and report redacted telemetry, but block native-tokenizer comparisons and promotion; affected records carry an explicit measurement-gap reason and are excluded from complete comparison samples.


















## User Scenarios & Testing *(mandatory)*

### User Story 1 - Classify work before governing it (Priority: P1)

A DM, maintainer, or capable agent brings a substantial request to the repository. The Spec Kit layer identifies whether the request needs full SDD, assigns one work class, and routes routine campaign content through its existing skill and template process. The classification is understandable without manually teaching the repository.

**Why this priority**: Applying full software ceremony to routine campaign content wastes context and constrains creative work; skipping SDD for system changes makes future agent behavior drift.

**Independent Test**: Run the classification against representative requests for an agent-system change, campaign architecture, a creative game system, a routine NPC, and a normal software feature. Each request receives the expected route and rationale without creating fictional canon.

**Acceptance Scenarios**:

1. **Given** a significant change to an agent-facing skill or LLM-wiki behavior, **When** the request is classified, **Then** it is `agent-system`, full SDD is selected, and the reason identifies its effect on future agent behavior.
2. **Given** a durable regional conflict or other multi-session campaign structure, **When** the request is classified, **Then** it is `campaign-architecture`, full SDD is selected, and player-owned outcomes remain open.
3. **Given** a reusable reputation, faction-turn, quest, encounter, clue, progression, or beat system, **When** the request is classified, **Then** it is `creative-system`, full SDD is selected, and the request is expressed as observable play behavior.
4. **Given** one ordinary NPC requested using an established campaign skill and template, **When** the request is classified, **Then** it is routine campaign content, full SDD is not required, and the existing campaign-content route is selected.
5. **Given** a normal CLI, Python tooling, automation, storage, retrieval, or test request, **When** the request is classified, **Then** it is `engineering` and normal engineering SDD semantics remain in force.

---

### User Story 2 - Specify playable outcomes without closing play (Priority: P1)

For campaign-facing and reusable game-system work, the DM receives a specification that describes value, actors, pressures, state, constraints, and observable behavior without prescribing a screenplay, authored player decisions, fixed scene sequence, or required ending. The world can act independently while player choices remain consequential and unresolved possibilities remain open.

**Why this priority**: Player agency is a system invariant. A specification that silently authors the future produces unusable campaign prep even if it is internally coherent.

**Independent Test**: Inspect specifications for a five-to-ten-session regional conflict and a faction reputation system. Verify that each names independent actors, motivations, pressures, conditional consequences, player decision surfaces, and an if-nobody-intervenes outcome while omitting required player choices and fixed endings.

**Acceptance Scenarios**:

1. **Given** a regional conflict intended to support roughly five to ten sessions, **When** its specification is reviewed, **Then** it describes actors, factions, locations, pressures, clocks, relationships, information states, continuity constraints, and conditional opportunities without naming which faction players join, a mandatory scene order, or how the conflict ends.
2. **Given** a reputation system, **When** a player action changes a faction relationship or information access, **Then** the specification defines observable state and behavior changes without selecting the action or future narrative outcome for the players.
3. **Given** a world pressure with no player intervention, **When** the relevant condition persists, **Then** the specification states an independent-world consequence that can change the situation without declaring it the only route to success.
4. **Given** a player refusal, avoidance, negotiation, investigation, failure, or unexpected approach, **When** it is applied to a specified situation, **Then** the specification leaves a materially playable response surface rather than treating a predetermined route as required.
5. **Given** multiple plausible future events, **When** they are recorded in the specification, **Then** they are distinguishable as fixed world anchors, current truths, likely or conditional possibilities, or player-owned outcomes.

---

### User Story 3 - Preserve truth ownership and the canon boundary (Priority: P1)

An agent planning the work can identify authoritative repository and campaign context, resolve existing owner entities, distinguish accepted facts from proposals, and identify the DM acceptance boundary. Specification, plan, and task completion never silently turn fictional proposals into campaign truth.

**Why this priority**: The repository already has a mature wiki, provenance, reveal, visibility, lifecycle, owner-page, and Work model. A second truth system or an unreviewed canon write would corrupt it.

**Independent Test**: Present a request that names an existing faction under an alias and proposes future campaign events. Verify that the existing owner is reused, provenance and visibility are retained, contradictions are surfaced, and no wiki fact changes before DM acceptance.

**Acceptance Scenarios**:

1. **Given** an apparent new faction, place, NPC, item, creature, vehicle, spell, quest, or other entity whose title or alias already resolves to an owner page, **When** the work is grounded, **Then** the existing owner is reused and no duplicate canonical entity is proposed.
2. **Given** an entity with no matching owner after targeted identity resolution, **When** a new owner is genuinely required, **Then** the specification identifies the required artifact, its existing repository kind and path convention, and its provenance obligations without introducing opaque IDs.
3. **Given** existing canon that may be affected, **When** the specification is written, **Then** it separates facts that must remain true, facts that may be affected, proposed truths, relevant owner pages, contradictions, and reveal or visibility implications.
4. **Given** a plan, task list, or completed implementation containing conditional fictional events, **When** the artifact is approved or completed, **Then** those events remain proposals or conditional possibilities until the existing Work and DM acceptance rules make them true.
5. **Given** a campaign-facing proposal, **When** it is ready for the DM, **Then** it is inspectable Work addressed to the DM, and only accepted Work can change campaign truth or be promoted into accepted wiki state.
6. **Given** a safe deterministic maintenance action such as lint, manifest update, retrieval refresh, or link repair, **When** it does not change campaign facts, **Then** it is not blocked by a needless human approval gate.

---

### User Story 4 - Plan and task real artifact dependencies (Priority: P2)

An agent can derive a plan and task graph appropriate to the work class. Engineering work retains technical planning. Creative and agentic work plans minimum sufficient context, retrieval exclusions, owner artifacts, continuity, agency constraints, DM usability, verification, and token cost. Tasks express real dependencies and bounded parallelism rather than a flat list of writing steps.

**Why this priority**: Correct sequencing prevents duplicate entities, owner-page omissions, contradictory state, context waste, and concurrent writes to one canonical artifact.

**Independent Test**: Review plans and task lists for an agent-system change, a campaign architecture feature, a creative system, and a normal software feature. Verify that each uses the appropriate planning vocabulary, lists affected owners, and gives a dependency-resolvable graph with only genuinely independent parallel work.

**Acceptance Scenarios**:

1. **Given** creative or agentic work, **When** a plan is generated, **Then** it identifies minimum sufficient context, targeted retrieval, deliberately excluded context, affected canonical artifacts, artifact ownership, continuity constraints, player-agency constraints, named creative constraints, DM-facing usability, verification, and context/token cost.
2. **Given** engineering work, **When** a plan is generated, **Then** it retains normal technical context, architecture, storage, testing, platform, performance, constraints, and source-structure planning without requiring campaign concepts that do not apply.
3. **Given** creative or campaign-system artifacts with dependencies, **When** tasks are generated, **Then** the graph can represent grounding and retrieval → owner/entity resolution → genuinely missing owners → rules, systems, or world state → relationships and agendas → playable situations → DM/session presentation → continuity verification → Work proposal → required DM acceptance → filing or promotion → deterministic maintenance and retrieval refresh.
4. **Given** two tasks touching independent artifacts and a third task touching a shared canonical artifact, **When** an execution wave is formed, **Then** only the independent pair is eligible for parallel work and the shared artifact has one active writer.
5. **Given** two tasks with an actual dependency, **When** task order is derived, **Then** the dependent task cannot be presented as parallel merely because both are prose or both have the same user-story label.
6. **Given** a task graph with no meaningful dependency or ownership conflict, **When** tasks are generated, **Then** the system does not add ceremony solely to display a DAG.

---

### User Story 5 - Verify the right things and keep both SDD paths compatible (Priority: P2)

A reviewer or implementing agent can verify deterministic repository constraints separately from creative judgment, use existing checks and retrieval machinery, and complete the normal Spec Kit lifecycle without changing the engineering path. The adapted layer remains compatible with specify, clarify, plan, checklist, tasks, analyze, implement, converge, git, and agent-context integrations.

**Why this priority**: The hybrid system succeeds only if creative and agentic semantics are added without degrading reliable software delivery or pretending subjective craft is machine-verifiable.

**Independent Test**: Run a matrix containing representative requests from all four SDD classes plus routine content. Verify route-specific acceptance evidence, deterministic checks, preserved hooks and integrations, and no subjective quality gate disguised as a lint failure.

**Acceptance Scenarios**:

1. **Given** an invalid campaign type, lifecycle, relationship, filename, schema field, beat kind, required owner, or closed vocabulary value, **When** verification runs, **Then** an objective check reports the violation using the repository's existing vocabulary and checker surfaces.
2. **Given** a question about whether a conflict is interesting, dialogue is dramatic, prose has a desired voice, or a creative process was ideal, **When** verification runs, **Then** it remains a reasoning or DM judgment and is not made a deterministic pass/fail lint rule.
3. **Given** an existing Spec Kit git or agent-context extension, **When** the adapted workflow runs, **Then** its configured lifecycle and capabilities remain available and are not silently replaced by a second integration.
4. **Given** an engineering feature, **When** it progresses through normal Spec Kit phases, **Then** it can use ordinary requirements, technical plans, tests, implementation, and convergence without campaign-specific concepts worsening its artifacts.
5. **Given** a creative or agentic feature, **When** it reaches completion, **Then** evidence identifies deterministic checks, continuity and agency review, owner resolution, Work status, DM acceptance status where required, filing or promotion status, and measured context cost without claiming that lint proves creative quality.

---

### Representative Validation Scenarios

These scenarios are the minimum cross-class acceptance set for the adapted system:

- **Scenario A — Agent-system change**: A significant skill or LLM-wiki behavior change classifies as `agent-system`, retrieves only relevant authoritative context, uses existing vocabulary and ownership, specifies observable outcomes, and names deterministic and judgment-based verification separately.
- **Scenario B — Campaign architecture**: A regional conflict for roughly five to ten sessions specifies a living situation with independent actors, pressures, world state, continuity, and agency guarantees; it does not choose the players' allegiance, scene order, or ending.
- **Scenario C — Creative game system**: A reputation system specifies persistent reputation state, faction behavior changes, and information access changes while leaving player decisions and resulting story outcomes open.
- **Scenario D — Routine NPC**: One ordinary NPC routes to the existing NPC skill/template process without generating a full SDD feature directory or engineering task graph.
- **Scenario E — Existing entity collision**: An apparent new entity that matches an existing title, alias, stem, path, wikilink, qmd result, manifest entry, or duplicate candidate reuses the owner page.
- **Scenario F — Proposed canon**: Future events remain proposals or conditional possibilities through specification, plan, task completion, and review until the existing DM acceptance rules authorize a fact change.
- **Scenario G — Mixed request**: A request combining routine campaign content with an agent-system or reusable-system change separates the SDD-worthy slice from the routine content and routes each through its existing process.

### Edge Cases
- Normal traces MUST NOT retain raw prompt, wiki, campaign, or model content merely for token telemetry; only redacted metadata, provenance identifiers, and measured counts are retained.

- The separate native-tokenizer governance change is not yet accepted: redacted trace collection and reporting MAY proceed, but native-tokenizer comparisons and promotion MUST be blocked; affected records carry a measurement-gap reason and are not complete comparison samples.

- A request mixes routine campaign content with an agent-system or reusable system change: classify the system-changing slice for SDD and route ordinary content through its existing owner skill; do not force unrelated content into one feature.
- A request names both a campaign architecture and an individual session beat: the architecture is SDD work; the beat remains with its typed beat skill unless the feature changes the beat system itself.
- The repository is silent about a campaign fact: mark invention and proposal status; retrieve relevant rules and owner pages; never fabricate a citation or silently file a fact.
- Targeted retrieval finds conflicting accepted, proposed, legacy, or external material: current accepted repository knowledge outranks lower-authority material; unresolved conflict remains visible for DM or owner resolution.
- A new entity name resembles an existing alias but describes a distinct entity: report the collision evidence and require an explicit distinction before minting a new owner.
- A specification repeats a closed vocabulary with different members: identify the authoritative owner and report drift; do not create a second enum to make the spec internally consistent.
- A fetched page is materially useful only when accepted Work explicitly cites or links it, or an independent evaluator confirms that it supplied a required fact, rule, or safety constraint; fetched-but-unused pages are unnecessary retrieval.

- DM acceptance is required for a campaign fact but not for a deterministic index, manifest, lint, or retrieval refresh: keep the safety gate only on the fact-changing surface.
- A creative task has no player-dependent outcome: it may state a fixed world anchor or current truth, but must still identify independent-world motion and visibility where relevant.
- A normal engineering task mentions a domain term that is also used in campaign work: use the repository's authoritative domain owner and do not invent a competing definition.

## Requirements *(mandatory)

### Work Classification and Routing

- **FR-001**: The Spec Kit layer MUST classify substantial work as exactly one of `engineering`, `agent-system`, `campaign-architecture`, or `creative-system`.
- **FR-002**: The classification MUST state why full SDD applies and MUST identify routine campaign content as intentionally outside full SDD when no repository or reusable-system change is involved.
- **FR-003**: Routine NPC, location, item, spell, creature, individual session beat, recap, and equivalent established campaign-content requests MUST route through their existing skills, templates, lifecycle, and Work protocol.
- **FR-004**: Mixed requests MUST separate the SDD-worthy system change from routine content rather than applying one route indiscriminately.

### Hybrid Specification Contract

- **FR-005**: An applicable specification MUST state its work class, objective, and why the outcome matters to the DM, players, campaign, or agents.
- **FR-006**: An applicable specification MUST identify the existing repository, campaign, world, schema, vocabulary, ADR, owner pages, and behavior that remain authoritative unless explicitly changed.
- **FR-007**: A campaign-facing or reusable game-system specification MUST state the agency surface: player-owned decisions, outcomes that remain open, independent NPC/faction/world action, persistent pressures, player-caused changes, unresolved possibilities, and if-nobody-intervenes motion.
- **FR-008**: A campaign-facing or reusable game-system specification MUST prefer actors, motivations, factions, locations, pressures, clocks, relationships, opportunities, consequences, information states, and conditional possibilities over predetermined scene sequences or endings.
- **FR-009**: An applicable specification MUST define independently testable acceptance scenarios without prescribing a particular creative method, prose voice, story structure, implementation architecture, or agent reasoning approach where alternatives satisfy the outcome.
- **FR-010**: An applicable specification MUST name its success evidence, assumptions, dependencies, and explicit out-of-scope boundaries.

### Canon, Provenance, and Entity Ownership

- **FR-011**: The adapted system MUST preserve the existing lifecycle, provenance, reveal, visibility, owner-page, and Work acceptance systems as the sole campaign-canon authority.
- **FR-012**: Specifications, plans, and task completion MUST NOT canonize fictional facts or conditional future events.
- **FR-013**: Campaign-facing changes MUST remain inspectable Work addressed to the DM until accepted; only accepted Work may change campaign truth or be promoted into accepted wiki state.
- **FR-014**: Before proposing a new canonical entity, the process MUST resolve existing titles, aliases, stems, deterministic paths, wikilinks, qmd/search results, manifests, and duplicate candidates using existing repository identity mechanisms.
- **FR-015**: The process MUST reuse an existing owner when identity resolution establishes equivalence and MUST report collision evidence when equivalence is uncertain.
- **FR-016**: The process MUST NOT introduce opaque entity IDs, a parallel canon database, a second lifecycle, or a second owner model unless a separately demonstrated failure cannot be solved by existing identity and ownership mechanisms.
- **FR-017**: Proposed, conditional, unrevealed, and player-owned material MUST remain distinguishable from accepted current truth and must preserve applicable visibility and reveal boundaries.

### Planning and Task Topology

- **FR-018**: Downstream planning MUST retain normal technical planning capability for `engineering` work.
- **FR-019**: Downstream planning for `agent-system`, `campaign-architecture`, and `creative-system` work MUST reason about minimum sufficient context, targeted retrieval, deliberate retrieval exclusions, canonical artifacts, artifact ownership, dependencies, independent versus serial work, agency, continuity, canon impact, named creative constraints, verification, DM usability, and context/token cost.
- **FR-020**: Downstream task generation MUST represent real dependency topology and MUST NOT reduce creative or campaign-system work to a flat sequence of prose-writing tasks.
- **FR-021**: Where applicable, creative and campaign-system task topology MUST be able to express grounding and retrieval, owner/entity resolution, genuinely missing owner creation, underlying rules/system/world state, relationships and active agendas, playable situations, DM/session presentation, continuity verification, Work proposal, required DM acceptance, filing or promotion, and deterministic maintenance/retrieval refresh.
- **FR-022**: Parallel work MUST be limited to genuinely independent artifacts with disjoint write ownership; each canonical artifact MUST have at most one active writer.
- **FR-023**: Dependency notation or DAG ceremony MUST be added only when it clarifies a real dependency, concurrency boundary, or ownership constraint.

### Vocabulary, Verification, and Efficiency

- **FR-024**: Established closed vocabularies, including campaign types, lifecycle values, relationship names, beat kinds, and other enumerated schema values, MUST remain single-source authorities.
- **FR-025**: The adapted system MUST detect or surface contradictory closed-vocabulary declarations and MUST prefer deterministic validation where the violation is objective.
- **FR-026**: Deterministic checks MUST cover applicable objective failures such as invalid type, lifecycle, relationship, filename, schema field, beat kind, required owner, broken link, duplicate identity, or vocabulary drift using existing or appropriately extended repository tooling.
- **FR-027**: Verification MUST use executable hard gates for canon precedence, entity-before-spoken behavior, DM-facing explicitness, reveal and visibility boundaries, accept-before-write semantics, and objective mechanics or schema checks. Playability, specificity, continuity, player agency, and DM usefulness MUST use a blind paired evaluator with a fixed semantic-quality rubric, independent of the optimization under evaluation, and MUST NOT become deterministic lint failures.

- **FR-028**: Context strategy MUST prefer minimum sufficient authoritative retrieval, owner-page retrieval, targeted relationships, current state, invoked rules, progressive disclosure, machine-readable discovery, and environment-derived truth. A fetched page MUST count as materially useful only when accepted Work explicitly cites or links it, or an independent evaluator confirms that it supplied a required fact, rule, or safety constraint; fetched-but-unused pages MUST count as unnecessary retrieval. QMD MUST record every attempted collection and fallback while preserving wiki → shattered-sea → legacy precedence; fallback material MUST NOT override current accepted canon.



- **FR-030**: Any claimed token or context improvement MUST be measured with the selected model family’s native tokenizer as authoritative across the whole useful trajectory from the user request through final Work, including loaded instructions and context, retrieval, tool calls, failed calls, retries, and model input/output; idle time and unrelated activity MUST be excluded. Comparisons MUST remain within the same model/tokenizer family unless a separately specified normalization method exists. Comparisons MUST preserve narrative craft, mechanics, specificity, canon fidelity, playability, agency, and DM usefulness. Normal sitting traces MUST use local gitignored JSONL containing redacted metadata and token counts only, with 90-day retention; sanitized evaluation fixtures and pinned baselines MAY be committed.




### Compatibility and Completion

- **FR-031**: The adapted Spec Kit layer MUST preserve the normal substantial-feature lifecycle: specify, clarify, plan, checklist, tasks, analyze, implement, and converge.
- **FR-032**: Existing Spec Kit git and agent-context extensions MUST remain configured and operational unless a concrete incompatibility is named and resolved.

- **FR-033**: Existing wiki schema, entity directories, lifecycle, reveal, visibility, Work acceptance, campaign skills, templates, retrieval primitives, linter, staged writes, designated-writer policy, domain vocabulary, and unattended deterministic maintenance MUST remain compatible.
- **FR-034**: Completion evidence MUST identify the route taken, authoritative context used and intentionally omitted, affected and resolved owner artifacts, dependency topology, deterministic checks run, creative/agency/continuity review, Work and DM acceptance state where applicable, filing or promotion state, and measured context cost where claimed.
- **FR-035**: The system MUST distinguish specification approval, plan approval, task completion, creative Work production, DM acceptance or modification, and accepted campaign truth as separate states.
- **FR-036**: Every optimization candidate MUST be evaluated against a pinned baseline with equivalent inputs and recorded revisions. Promotion MUST require at least 10 same-kind paired cases, at least a 5% median trajectory-token reduction, zero new hard-gate failures, semantic non-inferiority established by the blind paired evaluator and fixed rubric in FR-027, and no material increase in runtime failures or DM revision rate. Low-risk changes MAY auto-promote only after a 10% canary; moderate-risk changes MUST complete shadow replay and canary review; high-risk changes MUST receive human review. Any hard-gate failure or material quality regression MUST trigger rollback.

- **FR-037**: Every efficiency report MUST expose total trajectory tokens, input tokens, output tokens, tokens by source component, retrieval query and fetch counts, retrieval tokens, retry amplification, hard-gate failure rate, DM acceptance rate, DM revision rate, runtime or tool failure rate, and derived metrics with explicit denominators. Each value MUST be labeled measured, estimated, or inferred. Every measured token occurrence MUST have one exclusive primary source owner; secondary provenance MAY be retained as metadata but MUST NOT be counted twice.
- **FR-038**: Each sitting MUST be classified as `prep` or `wrapup` for initial efficiency comparisons. Audit and replay MAY be recorded as metadata but MUST NOT become separate comparison classes. Efficiency comparisons MUST use the same sitting class and same jobs.
- **FR-039**: Efficiency policy MUST be owned by maintainers in a versioned `config/efficiency.yaml`. The policy MUST define measurement rules, sample requirements, non-inferiority requirements, autonomy classes, canary rules, and rollback thresholds. Agents MAY read and propose policy changes but MUST NOT silently weaken thresholds, quality gates, or autonomy boundaries.
- **FR-040**: Every trace record MUST carry an explicit schema version. Readers MUST support additive schema evolution and MUST quarantine incompatible records with an observable error; they MUST NOT guess missing meanings or rewrite historical records.
- **FR-041**: Redacted trajectory telemetry MUST be collected for every `prep` and `wrapup` sitting by default. An explicit configuration MAY disable collection, but the resulting sitting MUST record an observable measurement gap and MUST NOT be treated as a complete comparison sample. Before the separate native-tokenizer governance change is accepted, collection and redacted reporting MAY proceed, but native-tokenizer comparisons and promotion MUST be blocked; affected records MUST carry an explicit measurement-gap reason and MUST NOT count as complete comparison samples.
- **FR-042**: Sittings MUST distinguish produced, accepted, failed, and incomplete Work. Failed and incomplete sittings MUST retain traces and failure reasons but MUST be excluded from accepted-Work efficiency denominators. Accepted Work MUST require explicit DM acceptance.
- **FR-043**: Autonomy classes MUST map as follows: deterministic low-risk cleanup MAY auto-promote after the required replay and canary; retrieval, routing, context budgets, and tool exposure MUST require shadow replay and canary review; semantic compression, model changes, canon or schema changes, instruction redesign, and policy or threshold changes MUST require human review. No candidate MAY alter its own evaluation criteria or safety thresholds.








### Named Failure Modes and Scope Boundary

The following constraints are included because each prevents a named failure:

- **NF-001 — Wrong route**: full SDD applied to routine content or omitted for system-changing work; prevented by FR-001–FR-004.
- **NF-002 — Predetermined play**: player decisions or endings authored as requirements; prevented by FR-007–FR-009.
- **NF-003 — Silent canonization**: specification, plan, tasks, or completion treated as accepted campaign truth; prevented by FR-011–FR-013 and FR-035.
- **NF-004 — Duplicate entity**: an equivalent owner recreated under an alias or alternate path; prevented by FR-014–FR-016.
- **NF-005 — Provenance or visibility loss**: facts become uncited, unrevealed material becomes exposed, or proposals appear current; prevented by FR-006, FR-011, FR-017, and FR-034.
- **NF-006 — Contradictory world or vocabulary state**: closed sets, lifecycle values, or current facts diverge between artifacts; prevented by FR-024–FR-026.
- **NF-007 — Wrong owner or concurrent clobber**: work is filed on the wrong artifact or multiple agents write one canonical artifact; prevented by FR-014, FR-021–FR-022.
- **NF-008 — Context waste**: agents load entire unrelated trees or duplicate standing instructions; prevented by FR-019 and FR-028–FR-030.
- **NF-009 — Software regression**: creative semantics degrade conventional Spec Kit engineering; prevented by FR-018 and FR-031–FR-033.
- **NF-010 — Process theater**: ceremony, approval, or subjective lint is added without a named objective failure; prevented by FR-023 and FR-027.

**Out of scope**:

- Rewriting the LLM-wiki, migrating campaign content, or replacing existing skills and templates.
- Requiring Spec Kit for ordinary NPCs, items, locations, spells, creatures, session beats, recaps, and equivalent routine content.
- Creating a parallel campaign-canon database, alternate lifecycle vocabulary, opaque entity-ID layer, story bible, character database, or timeline database.
- Encoding one correct novel, screenplay, branching-video-game, scene, act, page-count, or ending structure.
- Predetermining player actions, beliefs, decisions, routes, or campaign outcomes.
- Making subjective creative quality a deterministic lint failure.
- Copying entire third-party presets or making the repository depend on multiple third-party presets to borrow individual patterns.
- Replacing the existing Work acceptance, reveal, visibility, provenance, designated-writer, token-measurement, or safe-maintenance policies.
- Adding human approval gates to safe deterministic work.
- Changing the constitution unless a separate tracked governance change establishes that its principles must be amended.

### Key Entities

- **SDD work class**: One of `engineering`, `agent-system`, `campaign-architecture`, or `creative-system`, plus the explicit non-SDD routine-content route.
- **Hybrid specification**: The feature artifact containing class, objective, value, ground truth, agency surface where applicable, canon impact, testable scenarios, named failures, scope, assumptions, and success evidence.
- **Ground truth source**: Existing repository or campaign authority such as the constitution, AGENTS, skills, schemas, ADRs, owner pages, current wiki state, retrieval results, or environment configuration.
- **Canonical artifact**: The existing owner page, skill, template, contract, script, configuration, or Spec Kit artifact that owns a fact or behavior; ownership is not duplicated by this feature.
- **Agency surface**: The explicit boundary between player-owned decisions, autonomous world motion, pressures, conditional possibilities, and fixed anchors.
- **Canon impact record**: The distinction between unchanged current truth, affected truth, proposed truth, owner pages, contradictions, provenance, and reveal/visibility consequences, using existing repository semantics.
- **Work proposal**: DM-addressed, inspectable campaign output that remains mutable until accepted and is distinct from specification, plan, task completion, and canon.
- **Dependency graph**: The real prerequisite and single-writer relationships among context, owners, systems, situations, presentation, verification, acceptance, filing, and maintenance tasks.
- **Verification evidence**: Deterministic check results plus explicit agency, continuity, owner, Work, acceptance, and creative-judgment review evidence; lint does not stand in for craft judgment.
- **Context cost**: Measured context and token use across the whole useful trajectory of comparable work, using the selected model family’s native tokenizer as authoritative, from user request through final Work, including loaded context, retrieval, tools, failures, retries, and model input/output, while excluding idle and unrelated activity. Measurements from different model/tokenizer families are not directly comparable. Normal traces are local, gitignored, redacted, and retained for 90 days; committed fixtures and baselines contain no raw sensitive content.



## Success Criteria *(mandatory)

### Measurable Outcomes

- **SC-001**: In a seven-case classification run covering Scenarios A–G, 7/7 requests receive the expected SDD or routine-content route, and each rationale identifies the relevant scope boundary.

- **SC-002**: In a review of at least three specifications for each applicable creative/agentic class, 100% contain objective, user/table value, ground truth, named failure modes, out-of-scope boundaries, and independently testable acceptance scenarios.
- **SC-003**: In a review of at least three campaign-facing specifications, 100% explicitly state player-owned decisions, independent world motion, an if-nobody-intervenes consequence, and at least one unresolved or conditional possibility; 0% require a player allegiance, scene sequence, or authored ending.
- **SC-004**: In a proposed-canon test with at least five fictional future events, 0/5 become accepted wiki facts through specification, plan, task completion, or review without the existing DM acceptance path.
- **SC-005**: In an entity-collision test set of at least ten aliases or equivalent existing entities, 100% resolve to the existing owner or surface an explicit ambiguity before a new owner is proposed; 0 duplicates are created.
- **SC-006**: In a task-topology review containing at least ten creative or campaign-system tasks, 100% have an identifiable dependency/ownership rationale, and no task marked parallel shares a canonical write surface with another task in its wave.
- **SC-007**: In a deliberate vocabulary-drift fixture, the verification surface reports the conflicting closed-set declarations while preserving the authoritative owner; no new competing vocabulary is added.
- **SC-008**: In a normal engineering feature smoke run, all supported Spec Kit lifecycle phases remain invocable and at least one conventional technical acceptance scenario completes without campaign-specific requirements being imposed.
- **SC-009**: Across a compatibility audit of the configured git and agent-context extensions, 100% of existing hooks and lifecycle capabilities remain available, and no second integration or authority surface is introduced.
- **SC-010**: In a deterministic-check fixture containing invalid type, lifecycle, relationship, filename, link, owner, schema, canon-precedence, entity-before-spoken, DM-explicitness, reveal, visibility, or accept-before-write violations, every objective violation is reported; in a paired subjective-quality fixture, 0 subjective judgments are reported as deterministic failures.
- **SC-011**: Across at least three comparable workflow pairs, targeted retrieval loads no unrelated mandatory artifact set and measured context cost is equal to or lower than the current baseline without reducing required grounding or acceptance evidence.
- **SC-012**: In a completion-evidence audit of at least five feature runs across the four SDD classes, 100% identify route, authoritative context, affected owners, dependencies, verification evidence, and acceptance/canon state; creative runs also identify agency and continuity review.
- **SC-013**: In a routine-NPC smoke run, 0 full SDD feature directories, plans, or engineering task graphs are generated, and the existing NPC skill/template route remains usable.
- **SC-014**: In a review of at least five completed creative or agentic workflows, 100% distinguish specification approval, plan approval, task completion, Work production, DM acceptance, and accepted campaign truth as separate states.
- **SC-015**: In a promotion fixture with low-, moderate-, and high-risk candidates, 100% use pinned paired replay and a blind paired evaluator with the fixed semantic-quality rubric; low-risk promotion requires at least 10 same-kind pairs and a 10% canary, moderate-risk promotion requires shadow replay and canary review, high-risk promotion requires human review, and every hard-gate failure or material quality regression causes rollback.
- **SC-016**: In a retrieval fixture with cited, evaluator-confirmed, and fetched-but-unused pages, 100% of cited or evaluator-confirmed pages are classified as materially useful and 100% of fetched-but-unused pages are classified as unnecessary retrieval.
- **SC-017**: In a report fixture containing successful, failed, retried, and retrieved work, 100% expose the required metric vector and label every value as measured, estimated, or inferred with its derived-metric denominator.
- **SC-018**: In an attribution fixture containing overlapping standing instructions, skill, user, wiki, retrieval, helper, tool, retry, and output content, 100% of measured token occurrences have exactly one primary source owner and component totals do not double-count occurrences.
- **SC-019**: In a mixed sitting fixture containing prep, wrapup, audit, and replay activity, 100% of prep and wrapup records use those comparison classes, audit and replay remain metadata, and no cross-class efficiency comparison is reported.
- **SC-020**: In a policy-ownership fixture, 100% of efficiency runs load the versioned maintainer-owned policy, and agent proposals that weaken thresholds, quality gates, or autonomy boundaries are rejected without changing the policy.
- **SC-021**: In a QMD fallback fixture with silent and failed higher-precedence collections, 100% record every attempted collection and fallback, preserve wiki → shattered-sea → legacy precedence, and prevent fallback material from overriding accepted canon.
- **SC-022**: In a trace-schema fixture containing additive and incompatible revisions, 100% of additive records remain readable, incompatible records are quarantined with an observable error, and no historical record is rewritten.
- **SC-023**: In a telemetry-coverage fixture containing enabled, explicitly disabled, and pre-governance sittings, 100% of enabled prep and wrapup sittings produce traces; every disabled sitting records a measurement gap; and every pre-governance sitting may report redacted telemetry but has native-tokenizer comparison and promotion blocked, carries a measurement-gap reason, and is excluded from complete comparison samples.
- **SC-024**: In a sitting fixture containing produced, accepted, failed, and incomplete Work, 100% classify each state correctly; failed and incomplete traces remain reportable with failure reasons and are excluded from accepted-Work denominators.
- **SC-025**: In an autonomy-classification fixture containing low-, moderate-, and high-risk candidates, 100% receive the required promotion path; no candidate changes its own evaluation criteria or safety thresholds.

## Assumptions

- The current constitution, AGENTS files, wiki schemas, skills, templates, Work protocol, retrieval primitives, linter, staged-write behavior, and configured environment are authoritative and are loaded progressively rather than copied into this feature.
- The repository's existing campaign lifecycle, provenance, reveal, visibility, owner-page, and DM acceptance mechanisms are sufficient; this feature adapts Spec Kit to them rather than adding a canon model.
- `engineering` retains ordinary Spec Kit technical semantics; the other three classes add only the contract needed to prevent their named failures.
- A request that changes a skill, instruction, retrieval rule, workflow, prompt surface, or LLM-wiki operating behavior is substantial even when its output is prose, because it changes how future agents operate.
- A request that creates or revises a reusable game or campaign system is substantial; an instance of an established content kind is not substantial unless it changes that system.
- Existing identity resolution uses deterministic paths, canonical titles, aliases, wikilinks, globally unique stems, qmd/search, manifests, and duplicate detection; opaque IDs are unnecessary by default.
- The installed Spec Kit CLI and current catalog are discovery sources only. The named community presets/extensions are reference designs, not dependencies or authorities.
- Reference patterns adopted selectively are: agency and conditional state from game-narrative work; motivations, relationships, chronology, and continuity from long-form fiction work; scene purpose and readable change from screenwriting; classify-before-write from inventory alignment; drift visibility from canon work; single-owner vocabulary checks; traceable intake and sequencing; provider-neutral roles; lean command composition; explicit dependencies; and command-density techniques.
- Those references do not authorize Twine, Ink, novel, screenplay, fixed-ending, live-ID, alternate-canon, alternate-lifecycle, second-routing, or redundant-intake assumptions.
- Safe deterministic maintenance may run unattended. Human judgment remains at the existing DM and creative-quality boundaries.
- Context/token comparisons use the selected model family’s native tokenizer as the authoritative method and compare same-kind work within that model/tokenizer family; lower cost is not a success when quality or completeness falls.
- Because this clarification changes the current repository-wide tiktoken authority, implementation MUST first land a separate tracked governance change updating the applicable AGENTS and token-measurement policy. Until that change is accepted, the feature MAY collect and report redacted telemetry but MUST gate native-tokenizer comparisons and promotion and mark affected records with an explicit measurement-gap reason; it MUST NOT silently override the current policy.
- The feature is complete when the adapted Spec Kit artifacts and downstream behavior can govern both SDD paths without requiring migration of existing campaign content.
