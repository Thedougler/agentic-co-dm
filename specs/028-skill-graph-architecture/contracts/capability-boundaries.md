# Contract: Capability Boundaries and Composition

## Authority chain

1. `AGENTS.md` selects the existing owner directly from user intent and artifact kind.
2. The receiving capability owns its procedure, specialized craft, completion guard, and local handoffs.
3. `docs/agents/hybrid-sdd.md` governs substantial system-changing work and cross-capability planning.
4. `wiki/AGENTS.md` governs wiki semantics and output constraints for wiki writes.
5. Templates/contracts and validation rules govern artifact shape and validity.
6. `specs/027-wiki-agent-cli/contracts/wiki-cli.md` governs query, lint, and health observation results.

Later layers do not duplicate earlier procedures. Strong pointers keep required safeguards available at their load boundary.

## Boundary contract

Every in-scope wiki-facing capability exposes these concepts as headings or clear equivalents:

### Input

State the intents, targets, evidence, and constraints the capability accepts. A receiving capability does not reclassify the whole request when its owned slice is already explicit.

### Work

State only the owner-specific procedure and safeguards. Load the minimum context projection. Use focused retrieval when evidence is insufficient, then resume the same capability.

### Done

State observable completion evidence. Prose existence is never sufficient. A writer reaches applicable validation; a read answer includes grounded evidence; maintenance reaches a clean affected scope or reports a specific owner-level blocker.

### Capability Handoff

State when ownership changes, which existing owner receives the bounded slice, what evidence returns, and where the parent resumes. Trivial local decisions do not become handoffs.

## Parent/child contract

- The parent operation retains the original objective.
- A child owns only its named artifact or operation.
- Required child output contracts pass before the parent resumes.
- The parent rejoins all required children before dependent work.
- Independent children may run concurrently only when no prerequisite edge exists and canonical write surfaces are disjoint.
- One active writer owns a shared canonical surface.

## Read contract

- Read requests answer without canonical wiki mutation.
- Retrieval progresses from compact search evidence to focused page evidence and stops when sufficient.
- A possible useful edit does not authorize mutation.
- Derived cache and timing side effects remain limited to those specified by the wiki CLI contract.
- Durable insight reports, logs, page edits, manifest edits, and index edits are write workflows.

## Write contract

- Resolve the artifact owner before mutation.
- Retrieve current canon and governing output contract.
- Satisfy real dependencies in order.
- Use the existing mutation/finalization path for that owner.
- Run applicable scoped validation.
- Clean closes; deterministic findings go to registered deterministic repair; semantic findings go to the artifact owner; affected scope returns to validation.

## Ingest contract

- Preserve source evidence and resolve destination ownership.
- Child owner capabilities write their artifact; ingest retains source-level completion responsibility.
- Tracking surfaces update once through their existing owner.
- Every written page reaches scoped validation.
- Retrieval refresh uses the existing finalization path once.

## Maintenance contract

- `wiki health` is the observation surface for ordered action selection.
- `wiki lint` exposes the complete configured findings for the selected scope.
- Agents consume `context.act`, `next`, `focus`, and finding fields; they do not construct a second priority planner.
- Deterministic repair uses only registered safe fixers.
- Semantic repair routes to the artifact owner.
- The repaired scope is rerun until clean or a specific blocker remains.

## Context contract

Required projection:
- receiving owner instructions;
- target artifact/source;
- relevant current canon;
- applicable template/contract and validation evidence;
- explicit dependencies and deliberate omissions.

Forbidden inheritance:
- unrelated artifact groups read by a prior capability;
- a whole-vault crawl where a focused observation suffices;
- duplicated child procedures pasted into the parent prompt.

## Synchronization contract

- Guidance-only route/handoff changes: owner skill, root/docs authority, and cold behavioral eval.
- Artifact-shape/lifecycle changes: governing template/contract, consuming skill, validation, and public-seam tests.
- Validation changes: canonical rule source, validation implementation/docs, and observable tests.
- Generated Vale vocabulary is refreshed through its owner; it is not hand-edited.

## Evaluation contract

Cold, focused subjects use the weakest sufficient executor model. Assertions cover:

1. direct owner selection;
2. subtype handoff without generic indirection;
3. child return to parent;
4. dependency order and safe concurrency;
5. bounded context projection;
6. read-only canonical state;
7. validation and retrieval feedback cycles;
8. preservation of specialized output contracts;
9. absence of forbidden orchestration machinery;
10. every named failure in `spec.md` mapped to at least one scenario.

Static heading checks may support legibility but cannot replace behavioral execution evidence.
