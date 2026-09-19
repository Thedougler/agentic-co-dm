# Hybrid Spec-Driven Development

This is the detailed operating contract for substantial work. It extends the existing Spec Kit lifecycle; it does not replace the constitution, wiki, campaign lifecycle, reveal/visibility rules, QMD precedence, or content skills.

## 1. Classify before writing

Emit exactly one route decision before creating or changing a substantial artifact:

```text
work_class: engineering | agent-system | campaign-architecture | creative-system
route: full-sdd
reason: <observable system, reusable-rule, campaign-structure, or future-agent behavior change>
```

Use `engineering` for normal software, CLI, automation, storage, retrieval, and test changes. Use `agent-system` for skills, agent instructions, wiki operating behavior, or harness behavior. Use `campaign-architecture` for durable multi-session campaign structures. Use `creative-system` for reusable game systems such as reputation, faction turns, quests, encounters, clues, progression, or beats.

Route routine established NPC, location, item, spell, creature, individual beat, recap, and equivalent campaign content through its existing skill, template, lifecycle, and Work protocol. It has no feature directory. A mixed request records the SDD route for the system-changing slice and the existing skill route for routine content; never force both into one route.

Completion criterion: the artifact or completion evidence contains one `work_class`, `route`, and reason, or explicitly records the routine route and its skill.

## 2. Build the minimum sufficient specification

For full SDD, read only the authoritative context needed for the decision: constitution, current `AGENTS.md`, applicable docs and contracts, owner artifacts, targeted retrieval results, current schemas, and environment-derived facts. Record `context_used` and `context_omitted`; omissions are deliberate and named. Resolve existing titles, aliases, stems, deterministic paths, wikilinks, QMD results, manifests, and duplicate candidates before proposing an owner.

The specification records:

- `work_class`, objective, value, assumptions, dependencies, success evidence, named failures, and explicit scope boundaries;
- authoritative context and canonical owner artifacts;
- independently testable acceptance scenarios;
- for campaign-facing or reusable game-system work: actors, motivations, factions, locations, pressures, clocks, relationships, information states, conditional opportunities, continuity, player-owned decisions, open outcomes, independent world motion, and if-nobody-intervenes consequences;
- for engineering work: ordinary technical requirements, architecture, storage, testing, platform, performance, and constraints without campaign-only requirements;
- canon impact: current truth, affected truth, proposals, contradictions, provenance, reveal, visibility; DM acceptance is not required when constitution X already makes the fact canon.

Describe observable behavior. Leave creative method, prose voice, screenplay order, authored player choices, and fixed endings open when alternatives can satisfy the outcome. Conditional fictional events stay proposals, never accepted truth.

Completion criterion: every applicable specification field has evidence or an explicit not-applicable reason, and each named failure maps to an acceptance check or review.

## 3. Plan real ownership and dependencies

The plan names one canonical owner and one active writer for every artifact. It records the minimum context, deliberate exclusions, dependency edges, serial/parallel waves, agency and continuity constraints, DM usability, verification surfaces, and measured context cost where claimed.

Use an edge only for a real prerequisite. When applicable, preserve this order:

```text
grounding/retrieval → owner/entity resolution → missing owner creation
→ rules/system/world state → relationships/agendas → playable situations
→ DM/session presentation → continuity verification → file what is canon
→ deterministic maintenance/retrieval refresh
```
Parallel work is limited to disjoint canonical write surfaces. Tasks with an actual dependency remain serial even when both are prose. Safe deterministic maintenance (lint, manifest update, retrieval refresh, or link repair) uses its existing unattended path and does not acquire a needless DM gate.

Completion criterion: every task has an owner, artifact, evidence, state, and real predecessors; no parallel wave shares a canonical write surface.

## 4. Preserve canon and agency

Reuse an equivalent existing owner. If identity remains uncertain, report the collision evidence and require an explicit distinction before minting a new owner. Use repository kind and path conventions; never introduce opaque IDs, a parallel canon database, or a second lifecycle or owner model.

Keep accepted current truth, affected truth, proposal/conditional material, and player-owned outcomes distinguishable. Preserve provenance, reveal, and visibility boundaries. Campaign-facing Work is inspectable. User-said canon files immediately. Specification, plan, and tasks still do not invent unsaid events.

Preparation exposes materially different response surfaces: engagement, negotiation, investigation, avoidance, redirection, failure, refusal, and unexpected approaches where the fiction permits them. NPCs, factions, threats, opportunities, clocks, and consequences can move independently according to established motives and circumstances.

Completion criterion: owner resolution, canon state, and reveal/visibility are explicit in the evidence; user-said canon files under constitution X without a separate acceptance wait.

## 5. Verify at the correct boundary

Use deterministic checks for objective class, route, schema, closed vocabulary, filename, link, owner, lifecycle, canon precedence, entity-before-spoken, DM-facing explicitness, reveal/visibility, file-under-constitution-X, dependency, attribution, and compatibility failures. Existing wiki, link, schema, token, QMD, OMP, and Spec Kit checks remain their own authorities.

Use an independent blind paired evaluator with a fixed rubric for playability, specificity, continuity, player agency, and DM usefulness. Do not turn creative judgment or prose preference into deterministic lint. Record semantic review separately from hard-gate results.

Completion evidence exposes:

```text
route
context_used
context_omitted
owners_affected
owners_resolved
dependencies
deterministic_checks
quality_review
work_status: produced | accepted | failed | incomplete
dm_acceptance: not-required
canon_state: unchanged | proposal | accepted-truth
filing
measurement
```

`accepted-truth` follows constitution X, not a chat accept step. Failed or incomplete Work remains reportable and does not become canon.

## 6. Measure and promote safely

Use `scripts/efficiency-trace.py` for redacted local telemetry and `config/efficiency.yaml` for policy. Trace every `prep` and `wrapup` by default across the useful trajectory from request through final Work; exclude idle/unrelated activity. Record tokenizer identity, retrieval attempts and fallbacks, counts, failures, retries, and one exclusive primary source owner per measured token occurrence. A measurement gap is not a complete sample. Normal records remain local, redacted, and retained for 90 days; incompatible schemas quarantine with an observable error without rewriting history.

Compare only the same sitting class and job, with at least 10 paired cases and a 5% median trajectory-token reduction, zero new hard-gate failures, semantic non-inferiority, and no material runtime-failure or DM-revision increase. Low-risk changes need the canary path, moderate-risk changes need shadow replay and canary review, and high-risk changes need human review. Hard or material quality regressions roll back. Until the separate native-tokenizer governance change is accepted, native-tokenizer comparisons and promotion remain blocked and carry an explicit measurement-gap reason.

Completion criterion: report values are labeled `measured`, `estimated`, or `inferred`, include denominators, and promotion evidence names the paired baseline, risk path, quality gates, and rollback result.

## 7. Compatibility guard

Keep `specify`, `clarify`, `plan`, `checklist`, `tasks`, `analyze`, `implement`, and `converge` available with configured git and agent-context extensions. Do not edit generated `.agents/skills/speckit-*`, `.omp/commands/speckit.*`, or managed `.specify/templates/*` as a policy shortcut. Use this contract as progressive disclosure from `AGENTS.md`, and let feature `spec.md`, `plan.md`, and `tasks.md` own their respective behavior and topology.
