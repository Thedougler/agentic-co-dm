# Feature Specification: Skill Design Dispatch

**Feature Branch**: `016-skill-design-dispatch`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: "When agents must perform large modifications to skill files, or other agent facing text, small changes or modifications may be done by the main agent (changing a value, a sentence, a path, a single word or a couple words) however beyond that, agents should delegate the skill modification or creation to a reserved high-expertise writer which will complete the task. In the event usage limits cause it to stop or refuse or otherwise error, it will be resumed later and the task left incomplete. Due to these limits the reserved writer is only used for these large changes where expertise in skill design is necessary, and its task will be appropriately scoped and prompted. Small changes to skill files that dont impact the overall design can be handled by the main agent." Later direction: only skill files and big changes to standing agent-facing instructions; used for high-level agentic design with far-reaching scope and implications. Grill settlements: the gate is design-impact not size; closed in-scope set; unavailability leaves files untouched.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Classify design-impact before writing (Priority: P1)

A session agent is about to change an in-scope instruction file. Before any of that file changes, the agent classifies the change as **design-impact** or **not**.

Design-impact means the change would alter any of:

- when a skill triggers (its description / trigger)
- workflow ownership (which skill or agent does a step)
- standing load (what is always in context)
- creating a new skill or subagent

Anything else on an in-scope file — a typo, a path, a named value, a clarifying sentence that does not change who does what — is not design-impact. Length does not decide. A long mechanical reorder is not design-impact. A two-line trigger rewrite is.

The session agent applies this checklist itself. Borderline of those four bullets is design-impact. The owner is not asked to classify.

**Why this priority**: Dispatch without a checkable gate either never fires or fires on every edit. Classification is the product.

**Independent Test**: Give two reviewers the same set of at least twelve proposed edits covering all four bullets plus typos, paths, values, clarifying sentences, and a long mechanical reorder. They name design-impact or not without seeing each other. They agree with the checklist on every item.

**Acceptance Scenarios**:

1. **Given** a proposed edit to an in-scope file, **When** the session agent is about to write, **Then** it has classified the edit as design-impact or not before the file changes.
2. **Given** an edit that would change a skill trigger, ownership, standing load, or would create a skill or subagent, **When** classified, **Then** it is design-impact.
3. **Given** a typo, path, value, or clarifying sentence that does not change who does what, **When** classified, **Then** it is not design-impact even if the diff is long.
4. **Given** a long mechanical reorder with no behavior change, **When** classified, **Then** it is not design-impact.
5. **Given** a two-line rewrite of a skill trigger, **When** classified, **Then** it is design-impact.

---

### User Story 2 - Non-design edits stay with the session agent (Priority: P2)

When the classification is not design-impact, the session agent makes the change. It does not dispatch, does not park work, and does not wait for the designated writer.

**Why this priority**: The reserved writer is scarce. Spending it on typos and path fixes is the failure the owner named.

**Independent Test**: Give a session agent an in-scope typo or path fix. The file is corrected in that session. No parked dispatch exists for it.

**Acceptance Scenarios**:

1. **Given** a non-design-impact edit to an in-scope file, **When** the session agent works, **Then** that agent completes the edit in the same session.
2. **Given** that edit, **When** the session ends, **Then** there is no parked dispatch for it.
3. **Given** a mixed request (one non-design fix and one design-impact change), **When** the session agent works, **Then** it completes the non-design fix itself and does not use that as license to also write the design-impact change.

---

### User Story 3 - Design-impact work is dispatched (Priority: P3)

When the classification is design-impact, the session agent does not write the target files. It writes a scoped prompt that states the outcome, the in-scope files, and the bounds (what must not change), then hands the work to the designated writer. The designated writer is the only writer of that change.

This routing applies in every coding session that would edit those files, including sessions that never loaded a skill-authoring playbook.

**Why this priority**: Far-reaching instruction design is the scarce expertise. The session agent drafting it is the defect.

**Independent Test**: Give a session agent a job that would change a skill trigger or create a skill. The target files are unchanged by that agent. A scoped prompt exists. The designated writer is the one that changes the files, or the job is parked per User Story 4.

**Acceptance Scenarios**:

1. **Given** a design-impact job, **When** the session agent acts, **Then** it does not modify the target instruction files.
2. **Given** that job, **When** the session agent hands it off, **Then** the handoff includes a scoped prompt naming the outcome, the in-scope files, and the bounds.
3. **Given** a successful designated-writer run, **When** the change lands, **Then** the designated writer is the sole writer of that change.
4. **Given** a session that did not load a skill-authoring playbook, **When** it would make a design-impact edit, **Then** it still classifies and dispatches.

---

### User Story 4 - Unavailability parks work and leaves files untouched (Priority: P4)

If the designated writer cannot start, stops, refuses, or errors (including usage limits), the design-impact job is incomplete. In-scope target files match their content from before the attempt. The scoped prompt is tracked work a later session can find without the original chat. The session agent does not finish the design itself.

**Why this priority**: A half-written skill is worse than a delayed one. Falling back to the session agent guts the policy the first time the reserved writer is unavailable, which is expected.

**Independent Test**: Simulate a design-impact job whose designated writer is unavailable. Target files are unchanged. Tracked work contains the scoped prompt. A later session can resume from that work without the original conversation.

**Acceptance Scenarios**:

1. **Given** a design-impact job whose designated writer cannot run, **When** the session agent stops, **Then** every target file is unchanged from before the attempt.
2. **Given** that stop, **When** a later session looks for incomplete design-impact work, **Then** it finds tracked work that contains the scoped prompt.
3. **Given** that stop, **When** the session agent is still capable of editing files, **Then** it still does not write the design-impact change.
4. **Given** a designated writer that dies after changing some but not all target files, **When** the job is marked incomplete, **Then** those files are restored to their pre-attempt content before the session reports incomplete.

---

### User Story 5 - Session agent verifies, it does not rewrite (Priority: P5)

After a successful designated-writer run, the session agent checks that the files touched are inside the in-scope set and that the prompt's outcome is met, then reports. It does not rewrite the files to "clean them up."

The owner may overrule and tell the session agent to write anyway. Absent that overrule, dispatch stands.

**Why this priority**: Rewriting after the specialist lands is paying for expertise and then throwing it away.

**Independent Test**: After a successful dispatch, inspect the session agent's subsequent edits. None of the dispatched files were rewritten by that agent for the same change. A scope check was reported.

**Acceptance Scenarios**:

1. **Given** a successful designated-writer change, **When** the session agent continues, **Then** it reports whether touched files were in-scope and whether the prompt outcome was met.
2. **Given** that success, **When** the session agent would "improve" the same files, **Then** it does not rewrite them for that change.
3. **Given** the owner explicitly overrules dispatch, **When** the session agent writes the design-impact change, **Then** that overrule is the only license to do so.

---

### Edge Cases

- A mixed request (typo plus trigger rewrite): complete the typo; dispatch the trigger. Completing the typo does not authorize writing the trigger.
- New skill or new subagent: always design-impact.
- Out-of-scope surfaces (constitution, feature specs, generated command adapters, campaign wiki): this routing does not apply. Those surfaces keep their existing authoring loops.
- The designated writer changing `writing-for-agents` itself: allowed. That document is in-scope when the change is design-impact.
- Owner overrule: the session agent may write design-impact changes only when the owner explicitly says to skip dispatch.
- Designated writer unavailable after a scoped prompt already exists: do not create a second tracker item for the same job; resume the existing one.
- Session agent "just fixing wording" that actually changes a trigger or ownership: that is design-impact, not a clarifying sentence.
- Multiple in-scope files in one design-impact job: one scoped prompt, one dispatch (or one parked item), not a prompt per file unless the outcomes are independent jobs.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Before an in-scope instruction file changes, the session agent MUST classify the change as design-impact or not.
- **FR-002**: Design-impact MUST mean a change that would alter skill triggering, workflow ownership, standing load, or that would create a skill or subagent. Length MUST NOT be the gate.
- **FR-003**: The session agent MUST apply that checklist itself. Borderline of those four bullets MUST be treated as design-impact. The owner MUST NOT be required to classify.
- **FR-004**: Non-design-impact edits to in-scope files MUST be completed by the session agent in the same session without dispatch.
- **FR-005**: On a design-impact job, the session agent MUST NOT modify the target instruction files.
- **FR-006**: On a design-impact job, the session agent MUST produce a scoped prompt that names the outcome, the in-scope files, and the bounds.
- **FR-007**: The designated writer MUST be the sole writer of a design-impact change that lands.
- **FR-008**: This routing MUST apply in every coding session that would edit in-scope files, including sessions that did not load a skill-authoring playbook.
- **FR-009**: If the designated writer cannot start, stops, refuses, or errors, the job MUST be left incomplete: target files MUST match their pre-attempt content, and the scoped prompt MUST be tracked work a later session can find without the original chat.
- **FR-010**: Unavailability of the designated writer MUST NOT authorize the session agent to write the design-impact change.
- **FR-011**: After a successful designated-writer run, the session agent MUST verify in-scope files and prompt outcome, and MUST NOT rewrite those files for the same change.
- **FR-012**: The owner MAY overrule dispatch. Absent an explicit overrule, FR-005 through FR-011 still bind.
- **FR-013**: In-scope instruction files are source skills (not generated adapters), standing project instructions and sticky rules, subagent definitions, and the agent-writing authority. Constitution, feature specs, generated command adapters, and campaign wiki MUST NOT be brought into this routing.
- **FR-014**: A mixed request MUST be split: non-design work by the session agent, design-impact work dispatched or parked.
- **FR-015**: Creating a new skill or subagent MUST be classified as design-impact.
- **FR-016**: Parked work for a job that already has a scoped prompt MUST be resumed rather than duplicated.

### Key Entities

- **Session agent**: The agent currently doing the owner's task in any coding harness.
- **Designated writer**: The reserved high-expertise specialist for far-reaching agent-instruction design. Not the session agent.
- **In-scope instruction file**: A source skill, standing project instruction or sticky rule, subagent definition, or the agent-writing authority.
- **Design-impact**: A change that would alter skill triggering, workflow ownership, standing load, or that would create a skill or subagent.
- **Scoped prompt**: The handoff artifact naming outcome, in-scope files, and bounds.
- **Parked dispatch**: Tracked incomplete design-impact work containing the scoped prompt, with target files untouched.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Two independent reviewers classify a set of at least 12 proposed in-scope edits covering all four design-impact bullets plus typo, path, value, clarifying sentence, and long mechanical reorder, and agree with the checklist on 100% of those items.
- **SC-002**: In a review of design-impact jobs after this rule is in force, 0% of the target instruction files were written by the session agent, except where the owner explicitly overruled.
- **SC-003**: 100% of non-design-impact in-scope edits in that review were completed by the session agent with no parked dispatch.
- **SC-004**: When the designated writer is unavailable, 100% of target files match their pre-attempt content, and 100% of those jobs have findable tracked work containing the scoped prompt.
- **SC-005**: After successful dispatch, 0% of those files are rewritten by the session agent for the same change.
- **SC-006**: In a sample of sessions that edit in-scope files without loading a skill-authoring playbook, 100% still classify and dispatch (or park) correctly.
- **SC-007**: A later session can resume a parked dispatch from tracked work alone, without the original chat, in 100% of sampled parked jobs.

## Assumptions

- The designated writer is the owner's reserved high-expertise skill-design specialist. Substituting the session agent when that specialist is unavailable is the failure this feature prevents. Which product hosts that specialist is a planning choice, not a classification choice.
- Every coding harness that can edit in-scope files is bound. A harness-local optional playbook is not sufficient.
- Parked dispatch is tracked on the project's existing issue tracker (issues are already the work surface). Chat-only parking is out.
- The session agent self-classifies; the owner is not a classification step.
- After success, the session agent's job is verify-and-report, not a second draft.
- "Appropriately scoped and prompted" means the scoped prompt is small enough that the designated writer is doing one design job, not an unbounded rewrite of all instructions.
- Out of scope: how the designated writer designs (craft stays with writing-for-agents); constitution amendment; Spec Kit specify/plan/tasks loops; generated Spec Kit adapters; campaign wiki writes; spending the designated writer on non-design edits.
- Owner overrule is explicit in the request that the session agent should write the design-impact change itself. Silence is not overrule.
