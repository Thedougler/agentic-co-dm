# Quickstart: Skill Design Dispatch

Prove the feature by classifying jobs and checking pointers. Do not call the designated writer to prove classification.

## Prerequisites

- Branch `016-skill-design-dispatch`
- Spec [spec.md](./spec.md), contract [contracts/skill-design-dispatch.md](./contracts/skill-design-dispatch.md)
- `AGENTS.md` contains the design-impact gate and who writes
- `docs/agents/skill-design-dispatch.md` exists and is pointed at from that gate
- `.omp/AGENTS.md` and `.claude/CLAUDE.md` still only import `AGENTS.md` (no second copy of the gate)

## 1. Classify the contract jobs (P1, SC-001)

Cover jobs 1–12 in the contract. A second reviewer names class and writer without seeing the first list.

Expected: 100% agreement. Fail if length is used as the gate. Fail if a long reorder is dispatched. Fail if a two-line trigger rewrite is kept by the session agent.

## 2. Non-design stays local (P2, SC-003)

Jobs 1–5: session agent would complete them with no parked issue.

Fail if a parked `Parked skill design:` issue is created for a typo or path fix.

## 3. Design-impact is not written by the session agent (P3, SC-002)

Jobs 6–10: session agent does not modify those targets. A scoped prompt exists, or the job is parked.

Fail if the session agent drafts the new skill or rewrites the trigger.

## 4. Unavailability parks and restores (P4, SC-004, SC-007)

Simulate job 16 (writer unavailable). Targets match pre-attempt content. An issue titled `Parked skill design: …` with `ready-for-agent` contains the scoped prompt. A later session can resume from that issue without the original chat.

Fail if the session agent writes the design. Fail if partial target edits remain.

## 5. Verify, do not rewrite (P5, SC-005)

After a successful dispatch (or a dry run of the verify step): session agent reports in-scope files and outcome. It does not rewrite those files for the same change.

Fail if a “cleanup” edit from the session agent follows.

## 6. Pointers, not copies (FR-008, Constitution IX)

- `AGENTS.md` is the gate.
- `.omp/AGENTS.md` and `.claude/CLAUDE.md` do not restate the four bullets.
- `skill-creator` and `omp-harness` do not instruct the session agent to draft design-impact work; they point at the procedure.
- The procedure does not prescribe how the designated writer designs.

Pass: steps 1–6 hold. Fail any step → routing is not the default yet.
