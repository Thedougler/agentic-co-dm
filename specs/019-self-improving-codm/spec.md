# Feature Specification: Self-Improving Co-DM

**Feature Branch**: `019-self-improving-codm`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: "agentic-co-dm is a self bootstraping, self reflecting, self improving exercise in agentic and human creativity, communication and collaboration with both aligned towards the goal of producing the best posible dnd campaign for the users players."

## Clarifications

### Session 2026-09-12

- Q: What is a core metric of self-improvement besides serving these players? → A: Token cost of an operation or sitting. More Work completed at the same quality. Wasted context hurts focus and output quality, so cutting it is an improvement only when quality holds.


## User Scenarios & Testing *(mandatory)*

### User Story 1 - Aim at these players (Priority: P1)

The DM names the people at the table and what this campaign is trying to be for them. The Co-DM works from that aim. When the DM and the Co-DM later state the aim independently, they name the same players and the same current intent. Generic "good D&D" is not the aim.

**Why this priority**: Bootstrap, reflection, and improvement have no target without a shared aim. Alignment is the product; the rest of the loop exists to serve it.

**Independent Test**: Name a table of at least three players and a current campaign intent. Ask the DM and the Co-DM separately what the campaign is for. They match on who and on intent. A later prep proposal that could have been written for any table fails this test.

**Acceptance Scenarios**:

1. **Given** a campaign with no recorded table aim, **When** the DM starts prep with the Co-DM, **Then** the Co-DM asks the DM to name the players and the current campaign intent before treating Work as aimed.
2. **Given** a recorded table aim, **When** the DM and the Co-DM each state the aim without seeing the other's wording, **Then** both name the same players and the same current intent.
3. **Given** a recorded table aim, **When** the Co-DM proposes prep Work, **Then** the proposal is specific to those players and that intent, not interchangeable with a proposal for a different table.
4. **Given** the DM changes who is at the table or what the campaign is trying to be, **When** they tell the Co-DM, **Then** later Work uses the updated aim and does not keep the obsolete one.

---

### User Story 2 - Gaps do not stall playable Work (Priority: P2)

Prep or wrapup needs something the wiki or the Co-DM's current practice does not yet cover. The Co-DM still delivers a DM-addressed proposal in that sitting, marks invention where the wiki is silent, and names the gap. It does not wait for a new practice, a new page, or a later session before offering Work. If the gap is in how the Co-DM itself works, that is a separate proposal for the DM to accept or reject — not a silent rewrite of the Co-DM.

**Why this priority**: A self-bootstrapping partner produces the campaign from an incomplete start. Stalling until the toolkit is perfect is the failure.

**Independent Test**: Ask for prep the wiki does not cover, and separately for a job the Co-DM has no standing practice for. In both cases the DM receives a proposal in that sitting, the gap is named, and how the Co-DM works is unchanged.

**Acceptance Scenarios**:

1. **Given** a prep request the wiki does not cover, **When** the DM asks in that sitting, **Then** they receive a proposal marked as invention, grounded in established lore, and the missing wiki coverage is named.
2. **Given** a prep or wrapup job the Co-DM has no standing practice for, **When** the DM asks in that sitting, **Then** they still receive playable Work and a named gap; the Co-DM does not refuse because a practice is missing.
3. **Given** a named gap in how the Co-DM works, **When** the Co-DM offers a fix, **Then** that fix is a proposal for the DM, and how the Co-DM works is unchanged until the DM accepts.
4. **Given** a named gap, **When** the DM rejects the proposed fix, **Then** later sittings still produce Work; the rejected fix is not applied.

---

### User Story 3 - Reflect, then improve only with the DM (Priority: P3)

After wrapup — and after prep when the DM asks — the Co-DM offers a reflection: what served these players, what did not, and one concrete next change if any. The DM accepts, edits, or rejects it. An accepted reflection that calls for a campaign change becomes a canon proposal. An accepted reflection that calls for a change in how the Co-DM works becomes an improvement proposal. Nothing in the wiki and nothing in how the Co-DM works changes until the DM accepts. The Co-DM does not run this during a session.

**Why this priority**: Self-reflection without a gate is silent rewrite. A gate without reflection is a Co-DM that never learns this table. The loop is the feature.

**Independent Test**: Finish wrapup for a session with at least one thing that served the table and one that did not. Confirm a reflection exists, the DM can accept or reject it, an accepted campaign change is proposed rather than filed, and an accepted practice change is proposed rather than applied. Confirm a rejected reflection leaves wiki and Co-DM practice untouched.

**Acceptance Scenarios**:

1. **Given** a finished wrapup, **When** that wrapup is complete, **Then** the DM has a reflection that names at least one observation about these players (what served them, what did not, or both).
2. **Given** a reflection, **When** the DM rejects it, **Then** the wiki is unchanged and how the Co-DM works is unchanged.
3. **Given** a reflection the DM accepts that calls for a campaign fact to change, **When** the Co-DM continues, **Then** it offers a canon proposal and does not edit the wiki until that proposal is accepted.
4. **Given** a reflection the DM accepts that calls for a change in how the Co-DM works, **When** the Co-DM continues, **Then** it offers an improvement proposal and does not apply that change until the DM accepts.
5. **Given** an accepted improvement, **When** a later sitting uses the same kind of job, **Then** the Co-DM follows the accepted change rather than the obsolete practice.
6. **Given** a session in progress, **When** play is happening, **Then** no reflection or improvement is running.
7. **Given** the DM asks for a reflection after prep, **When** that prep sitting is complete, **Then** they receive a reflection they can accept, edit, or reject, with the same gate as wrapup.
8. **Given** a completed sitting that included aim, Work, reflection, a proposal the DM accepted or rejected, and the sitting's token cost, **When** the DM later inspects that sitting, **Then** they can see each of those steps.

---

### User Story 4 - More Work, less waste, quality holds (Priority: P4)

A sitting has a token cost: how much the Co-DM had to read and write to finish its jobs. That cost is a core improvement metric. The DM and Co-DM use it to get more Work done in a sitting without dropping quality. Wasted context (reading or writing that does not change the sitting's outcome) is named so it can be cut. An accepted change that finishes the same jobs with lower token cost at the same quality is an improvement. A change that saves tokens by lowering quality is not. A change that raises token cost for the same jobs, without preventing a named failure, is not.

**Why this priority**: Token waste drowns signal. Less waste improves focus and the quality of Work for these players. Efficiency that trades away quality is not self-improvement.

**Independent Test**: Record token cost and accepted Work for a sitting. Apply an accepted efficiency change. Repeat the same kind of sitting. Token cost is lower, at least as much Work is accepted, and quality still passes. A proposed change that raises token cost with no named failure, or that lowers quality to save tokens, does not count as an improvement.

**Acceptance Scenarios**:

1. **Given** a finished prep or wrapup sitting, **When** that sitting is complete, **Then** its token cost is recorded and inspectable with the rest of the loop.
2. **Given** two sittings of the same kind, **When** the later one follows an accepted efficiency improvement, **Then** it finishes the same jobs at a lower token cost and quality still passes.
3. **Given** a proposed change that lowers token cost by producing worse Work, **When** it is judged as an improvement, **Then** it does not count as one.
4. **Given** a proposed change that raises token cost for the same jobs and does not prevent a named failure, **When** it is judged as an improvement, **Then** it does not count as one.
5. **Given** wasted context in a sitting (read or written material that did not change the outcome), **When** the Co-DM reflects on efficiency, **Then** that waste is named so the DM can accept or reject cutting it.

---

### Edge Cases

- No players named yet: the Co-DM does not claim the Work is aimed; it asks for the table aim first.
- DM names players but no intent: the Co-DM still asks for current campaign intent before treating alignment as done.
- Reflection is only praise or only process talk: it is incomplete until it names a concrete observation about these players.
- Reflection contradicts a wiki page: treat it as Work; do not silently overwrite canon.
- Fun would play better if a wiki fact changed: the Co-DM may propose the change; it does not silently edit canon.
- Gap is a missing campaign fact: invent a proposal (existing Co-DM rules); do not invent a wiki page before accept.
- Gap is missing Co-DM practice: still produce Work; propose the practice separately.
- DM rejects an improvement: keep producing Work with current practice; do not re-offer the same rejected fix unless the DM asks or new evidence from play appears.
- More than one improvement from one reflection: propose them as separate accept-or-reject items; do not bundle a campaign edit with a practice edit as one accept.
- Practice change would also produce D&D wiki content guidance: existing quality evaluation still binds; this loop does not skip it.
- Practice change that redesigns how the Co-DM is instructed: existing rules for who may write that change still bind; this loop does not skip them.
- Players never give direct feedback: the DM is the judge of "best for these players"; the Co-DM does not contact players.
- Two reflections in one wrapup: one reflection per wrapup unless the DM asks for another.
- Empty or uningested campaign: bootstrap still applies; mark invention; do not fake wiki citations.
- First sitting of a kind has no prior token cost: record this sitting's cost; compare starting with the next same-kind sitting.
- Token cost compared across different jobs or different sitting kinds: invalid; compare only same kind of sitting.
- Cutting tokens by omitting a quality evaluation or the DM accept-gate: not an improvement.
- Adding standing context the Co-DM must always read, when that context does not prevent a named failure: wasted context; not an improvement.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The DM MUST be able to record who the players are and the current campaign intent for those players.
- **FR-002**: The Co-DM MUST work from that recorded aim. Work that could be swapped onto a different table without edits MUST NOT count as aimed.
- **FR-003**: When no table aim is recorded, the Co-DM MUST ask for it before treating Work as aimed.
- **FR-004**: When the DM updates the players or the intent, later Work MUST use the updated aim.
- **FR-005**: A missing wiki fact or missing Co-DM practice MUST NOT prevent the Co-DM from offering playable Work in that sitting.
- **FR-006**: When Work is offered despite a gap, the Co-DM MUST name the gap to the DM.
- **FR-007**: A proposed change to how the Co-DM works MUST be a proposal the DM accepts, edits, or rejects. The Co-DM MUST NOT apply that change before accept.
- **FR-008**: After wrapup, the Co-DM MUST offer a reflection that names at least one concrete observation about these players.
- **FR-009**: After prep, the Co-DM MUST offer a reflection when the DM asks, and MUST NOT require the DM to ask in wrapup.
- **FR-010**: A reflection MUST be accept-or-reject Work. It MUST NOT write wiki facts or change how the Co-DM works by itself.
- **FR-011**: An accepted reflection that calls for a campaign fact to change MUST become a canon proposal and MUST still wait for accept before any wiki write.
- **FR-012**: An accepted reflection that calls for a change in how the Co-DM works MUST become an improvement proposal and MUST still wait for accept before that change is applied.
- **FR-013**: After the DM accepts an improvement, later sittings of that kind of job MUST follow the accepted change.
- **FR-014**: The Co-DM MUST NOT run reflection or improvement during a session.
- **FR-015**: Campaign wiki writes, invention marking, and the DM accept-gate from the existing Co-DM product still bind. This loop MUST NOT create a second path around them.
- **FR-016**: Existing quality evaluation for D&D content guidance, and existing rules for who may redesign how the Co-DM is instructed, still bind. This loop MUST NOT skip them.
- **FR-017**: The Co-DM MUST address reflections and improvement proposals to the DM, never to the players.
- **FR-018**: Agent and DM communication in this loop MUST be inspectable after the fact (aim, Work, reflection, proposal, accept or reject, applied change, token cost).
- **FR-019**: Each prep or wrapup sitting MUST record its token cost (how much the Co-DM had to read and write to finish that sitting's jobs).
- **FR-020**: Token cost of an operation or sitting MUST be a core metric of self-improvement, alongside whether Work served these players.
- **FR-021**: A change MUST NOT count as an improvement if it raises token cost for the same jobs without preventing a named failure.
- **FR-022**: A change MUST NOT count as an improvement if it lowers token cost by lowering Work quality.
- **FR-023**: Completing more accepted Work in a sitting at the same quality and at equal or lower token cost MUST count as an efficiency win.
- **FR-024**: Standing context the Co-DM must read or write that does not change the sitting's outcome MUST be nameable as wasted context in an efficiency reflection.

### Key Entities

- **DM**: The human who runs the session. Sole table runtime. Judge of whether the campaign is serving these players.
- **Co-DM**: Agent work in prep and wrapup. Addresses the DM, never the players, and does not run during a session.
- **Players**: The humans at this table. They receive the campaign. They do not operate the wiki or the Co-DM.
- **Table aim**: Who these players are, and what this campaign is currently trying to be for them. Recorded by the DM. The shared target for alignment.
- **Work**: Mutable prep the DM may accept, edit, or reject.
- **Gap**: A missing wiki fact or missing Co-DM practice that would otherwise be used for this sitting's job.
- **Reflection**: Work offered after wrapup (and after prep when asked) that names what served these players and what did not.
- **Canon proposal**: A suggested change to wiki facts. Not applied unless the DM accepts.
- **Improvement proposal**: A suggested change to how the Co-DM works. Not applied unless the DM accepts.
- **Wiki**: Compiled, citable campaign pages. Human prose. Source of truth for canon.
- **Token cost**: How much the Co-DM must read and write to finish one operation or one sitting. Core metric of self-improvement.
- **Wasted context**: Reading or writing that does not change the sitting's outcome. Cutting it is an improvement only when quality holds.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Given a named table of at least three players and a current campaign intent, the DM and the Co-DM independently state the same players and the same intent on 100% of a three-trial check.
- **SC-002**: In a review of at least five accepted prep proposals written after a table aim exists, a second DM who knows a different table marks at least 80% as not reusable for that other table without edits.
- **SC-003**: When a sitting's job has a missing wiki fact or missing Co-DM practice, the DM receives playable Work in that sitting 100% of the time, and the gap is named 100% of the time.
- **SC-004**: In those gap sittings, 0% of Co-DM practice changes are applied before the DM accepts an improvement proposal.
- **SC-005**: After wrapup of a sample of at least three sessions, 100% include a reflection the DM can accept, edit, or reject, and 100% of those reflections name a concrete observation about these players.
- **SC-006**: 0% of rejected reflections produce a wiki write or a Co-DM practice change.
- **SC-007**: Of accepted reflections that name a needed change, 100% produce a follow-up canon proposal or improvement proposal the DM can act on in the same sitting, rather than ending only as chat.
- **SC-008**: In a debrief after at least three sessions, the DM rates Co-DM Work as aimed at these players (not generic D&D) for 80% or more of accepted Work.
- **SC-009**: A DM can review one chain — reflection to accepted proposal to visible change — in under 10 minutes without a second operator.
- **SC-010**: 0% of sampled sessions have reflection or improvement running while play is happening.
- **SC-011**: After an accepted efficiency improvement, a repeat of the same sitting kind finishes the same jobs at a lower token cost in 100% of sampled pairs, and quality still passes the bar that applied before the change.
- **SC-012**: 0% of accepted improvements raise token cost for the same jobs without naming the failure they prevent.
- **SC-013**: 0% of accepted efficiency improvements produce Work that fails the quality bar that applied before the change.
- **SC-014**: In those same-kind pairs, the later sitting yields at least as many accepted Work items as the earlier sitting.

## Assumptions

- Primary user is the human DM. Players receive the campaign; they do not operate this loop.
- "Best possible campaign" is judged by the DM for this table. There is no hidden quality score the Co-DM optimizes without the DM.
- This feature is the improvement loop around the existing Co-DM product. It does not replace ingest, prep proposals, play-surface staging, or wrapup filing.
- v1 remains one campaign, one table, D&D 5e.
- Self-bootstrap means: produce Work from an incomplete start and name the gap. It does not mean the Co-DM rewrites how it works without accept.
- Self-reflection means: after wrapup (and after prep when asked), offer inspectable observations about these players. It does not mean a live agent at the table, and it does not mean contacting players.
- Self-improvement means: accepted reflections become proposals the DM gates. Campaign changes stay canon proposals. Practice changes stay improvement proposals. Token cost of the sitting is a core metric: more Work at the same quality, less wasted context.
- Creativity, communication, and collaboration are already the Co-DM experiment. This feature adds shared aim and a closed improve-with-accept loop. It does not add a second communication path to players.
- Fun may still shape Work. Wiki facts still change only when the DM accepts a canon proposal.
- One reflection per wrapup is enough unless the DM asks for another.
- Token cost is how much the Co-DM must read and write to finish the jobs. Quality is a constraint, not a trade. Fewer tokens that produce worse Work is not improvement. More tokens for the same jobs is not improvement unless they prevent a named failure.
- Out of scope: a Co-DM agent during a session; player accounts or player-operated feedback; autonomous rewrite of Co-DM practice; replacing existing content evaluation or instruction-redesign rules; multi-campaign orchestration; non-5e rules systems; billing; replacing the DM; a hidden quality score the Co-DM optimizes by cutting tokens without the DM.
