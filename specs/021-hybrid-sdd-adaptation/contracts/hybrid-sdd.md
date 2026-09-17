# Contract: Hybrid SDD Routing and Completion Evidence

Agent-facing contract. It extends the existing Spec Kit phases; it does not replace the constitution, wiki schema, Work acceptance, reveal/visibility rules, campaign lifecycle, or existing content skills.

## Route decision

Before writing a substantial repository or reusable-system change, emit one classification:

```text
work_class: engineering | agent-system | campaign-architecture | creative-system
route: full-sdd
reason: <why this changes the system, reusable rules, or future agent behavior>
```

An established NPC, location, item, spell, creature, individual beat, recap, or equivalent routine content uses its existing skill/template route and does not create a feature directory. A mixed request splits the system-changing slice from routine content and records both routes.

## Required specification surface

Every full-SDD specification states:

- `work_class`, objective, value, authoritative context, dependencies, assumptions, success evidence, named failures, and out-of-scope boundaries;
- independently testable acceptance scenarios;
- the canonical owner and identity evidence for each existing artifact it touches;
- for campaign-facing or reusable game-system work: player-owned decisions, open outcomes, independent world motion, pressures, conditional possibilities, continuity, and reveal/visibility consequences;
- for engineering work: ordinary technical requirements remain sufficient without campaign-only concepts.

No specification, plan, task list, or implementation completion may turn conditional fictional material into accepted campaign truth.

## Required plan surface

The plan identifies:

- minimum sufficient authoritative context and deliberately omitted context;
- canonical artifacts, owner, single-writer boundary, and real dependency edges;
- serial and parallel waves, with parallel work limited to disjoint canonical write surfaces;
- continuity, agency, canon, DM usability, deterministic checks, blind semantic review, and measured context cost where applicable;
- compatibility with the existing Spec Kit phases and extensions.

## Required task surface

Tasks preserve real prerequisites. When applicable, the topology can express:

```text
grounding/retrieval
  → owner/entity resolution
  → missing owner creation
  → rules/system/world state
  → relationships/agendas
  → playable situations
  → DM/session presentation
  → continuity verification
  → Work proposal
  → DM acceptance
  → filing/promotion
  → deterministic maintenance/retrieval refresh
```

The graph may omit nodes that do not apply, but it may not flatten a real dependency or add a wave solely to display a DAG.

## Completion evidence

The final report or saved completion record exposes these keys or clearly labeled equivalents:

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
dm_acceptance: not-required | pending | accepted | modified | rejected
canon_state: unchanged | proposal | accepted-truth
filing
measurement
```

`accepted-truth` is valid only when the existing DM acceptance path has completed. A rejected or incomplete Work result remains reportable and does not silently become canon.

## Verification boundary

Executable hard gates cover canon precedence, entity-before-spoken, DM-facing explicitness, reveal/visibility, accept-before-write, and objective mechanics/schema checks. Playability, specificity, continuity, agency, and DM usefulness use blind paired semantic evaluation with a fixed rubric and are never emitted as deterministic lint failures.

## Ownership and compatibility

- `AGENTS.md` owns the compact route pointer.
- `docs/agents/hybrid-sdd.md` owns the detailed operating procedure.
- `specs/<feature>/spec.md` owns behavior and acceptance.
- `specs/<feature>/plan.md` owns technical design.
- `specs/<feature>/tasks.md` owns implementation topology.
- Existing `docs/agents/work.md`, campaign skills, wiki schemas, QMD precedence, and constitution remain owners of their current facts.
- Generated Spec Kit adapters and managed templates remain disposable integration outputs and are not policy owners.
