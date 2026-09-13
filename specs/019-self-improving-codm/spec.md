# Feature Specification: Self-Improving Co-DM

**Feature Branch**: `019-self-improving-codm`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: "agentic-co-dm is a self bootstraping, self reflecting, self improving exercise in agentic and human creativity, communication and collaboration with both aligned towards the goal of producing the best posible dnd campaign for the users players."

## Clarifications

### Session 2026-09-12

- Q: What is a core metric of self-improvement besides serving these players? → A: Token cost of an operation or sitting. More Work completed at the same quality. Wasted context hurts focus and output quality, so cutting it is an improvement only when quality holds.
- Q: Who manages token cost? → A: Agents. They decrease it objectively. The DM does not manage, review, or gate token cost.
- Q: How should agents pursue lower token cost? → A: Proactively create and maintain reusable, flexible, agent-shaped helper scripts. Do not wait for the DM. Use an existing command when it already does the job.
- Q: Does this spec govern `errors.md`? → A: Yes. Agents fill it at runtime when an operation fails. They drain an entry when a wiki improvement (or other accepted fix) actually removes the cause. Do not drain without a fix. Do not leave a fixed error in the ledger.
- Q: Should the system organize its own files and folders? → A: Yes. Agents self-organize file and folder layout as the system grows, including the wiki (llm-wiki), optimizing for agent lookup and token cost. The DM does not manage layout. Changing wiki facts still uses the accept-gate.


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

Prep or wrapup needs something the wiki or the Co-DM's current practice does not yet cover. The Co-DM still delivers a DM-addressed proposal in that sitting, marks invention where the wiki is silent, and names the gap. It does not wait for a new practice, a new page, or a later session before offering Work. If the gap is in how the Co-DM itself works **and it changes campaign Work or what the DM sees**, that is a separate proposal for the DM to accept or reject. A gap that is only wasted context is User Story 4: agents close it without the DM.

**Why this priority**: A self-bootstrapping partner produces the campaign from an incomplete start. Stalling until the toolkit is perfect is the failure.

**Independent Test**: Ask for prep the wiki does not cover, and separately for a job the Co-DM has no standing practice for. In both cases the DM receives a proposal in that sitting, the gap is named, and how the Co-DM works is unchanged.

**Acceptance Scenarios**:

1. **Given** a prep request the wiki does not cover, **When** the DM asks in that sitting, **Then** they receive a proposal marked as invention, grounded in established lore, and the missing wiki coverage is named.
2. **Given** a prep or wrapup job the Co-DM has no standing practice for, **When** the DM asks in that sitting, **Then** they still receive playable Work and a named gap; the Co-DM does not refuse because a practice is missing.
3. **Given** a named gap in how the Co-DM works that would change campaign Work or what the DM sees, **When** the Co-DM offers a fix, **Then** that fix is a proposal for the DM, and how the Co-DM works is unchanged until the DM accepts.
4. **Given** a named gap of that kind, **When** the DM rejects the proposed fix, **Then** later sittings still produce Work; the rejected fix is not applied.
5. **Given** a gap that is only wasted context, **When** agents can cut it without changing Work quality, **Then** they cut it without a DM proposal.

---

### User Story 3 - Reflect, then improve only with the DM (Priority: P3)

After wrapup — and after prep when the DM asks — the Co-DM offers a reflection: what served these players, what did not, and one concrete next change if any. The DM accepts, edits, or rejects it. An accepted reflection that calls for a campaign change becomes a canon proposal. An accepted reflection that calls for a campaign-facing change in how the Co-DM works becomes an improvement proposal. Nothing in the wiki changes until the DM accepts. Token-cost-only cuts are not this gate; agents own those (User Story 4). The Co-DM does not run this during a session.

**Why this priority**: Self-reflection without a gate is silent rewrite. A gate without reflection is a Co-DM that never learns this table. The loop is the feature.

**Independent Test**: Finish wrapup for a session with at least one thing that served the table and one that did not. Confirm a reflection exists, the DM can accept or reject it, an accepted campaign change is proposed rather than filed, and an accepted campaign-facing practice change is proposed rather than applied. Confirm a rejected reflection leaves wiki and campaign-facing practice untouched.

**Acceptance Scenarios**:

1. **Given** a finished wrapup, **When** that wrapup is complete, **Then** the DM has a reflection that names at least one observation about these players (what served them, what did not, or both).
2. **Given** a reflection, **When** the DM rejects it, **Then** the wiki is unchanged and campaign-facing Co-DM practice is unchanged.
3. **Given** a reflection the DM accepts that calls for a campaign fact to change, **When** the Co-DM continues, **Then** it offers a canon proposal and does not edit the wiki until that proposal is accepted.
4. **Given** a reflection the DM accepts that calls for a campaign-facing change in how the Co-DM works, **When** the Co-DM continues, **Then** it offers an improvement proposal and does not apply that change until the DM accepts.
5. **Given** an accepted improvement, **When** a later sitting uses the same kind of job, **Then** the Co-DM follows the accepted change rather than the obsolete practice.
6. **Given** a session in progress, **When** play is happening, **Then** no reflection or improvement is running.
7. **Given** the DM asks for a reflection after prep, **When** that prep sitting is complete, **Then** they receive a reflection they can accept, edit, or reject, with the same gate as wrapup.
8. **Given** a completed sitting that included aim, Work, reflection, and a proposal the DM accepted or rejected, **When** the DM later inspects that sitting, **Then** they can see each of those steps.

---

### User Story 4 - Agents cut waste, quality holds (Priority: P4)

A sitting has a token cost: how much the Co-DM had to read and write to finish its jobs. That cost is a core improvement metric, and **agents own it**. They record it, compare same-kind sittings, and objectively decrease it. They proactively create and maintain reusable, flexible, agent-shaped helpers so a later sitting runs a command instead of re-deriving the procedure in context. The DM does not manage token cost, does not review it, and does not accept or reject efficiency changes. Wasted context (reading or writing that does not change the sitting's outcome) is cut by agents without waiting on the DM. A change that finishes the same jobs with lower token cost at the same quality is an improvement. A change that saves tokens by lowering quality is not. A change that raises token cost for the same jobs, without preventing a named failure, is not.

**Why this priority**: Token waste drowns signal. Less waste improves focus and the quality of Work for these players. The DM's job is the campaign; the agents' job is to spend fewer tokens on the same quality of Work.

**Independent Test**: Record token cost and accepted Work for a sitting. Agents apply an efficiency change without a DM accept step, including a helper when the job will repeat. Repeat the same kind of sitting. Token cost is lower, at least as much Work is accepted, quality still passes, and the later sitting uses the helper rather than re-teaching the procedure. The DM was not asked to manage any of this.

**Acceptance Scenarios**:

1. **Given** a finished prep or wrapup sitting, **When** that sitting is complete, **Then** agents have recorded its token cost. The DM was not asked to record, review, or accept that cost.
2. **Given** two sittings of the same kind, **When** agents have applied an efficiency change between them, **Then** the later sitting finishes the same jobs at a lower token cost, quality still passes, and the DM did not gate that change.
3. **Given** a proposed change that lowers token cost by producing worse Work, **When** it is judged as an improvement, **Then** it does not count as one.
4. **Given** a proposed change that raises token cost for the same jobs and does not prevent a named failure, **When** it is judged as an improvement, **Then** it does not count as one.
5. **Given** wasted context in a sitting (read or written material that did not change the outcome), **When** agents can cut it without changing the sitting's outcome or Work quality, **Then** they cut it without a DM accept step.
6. **Given** a job that will repeat or has repeated, **When** a reusable helper would lower token cost of the next sitting, **Then** agents create that helper without waiting for the DM and without being asked.
7. **Given** such a helper exists, **When** a later same-kind sitting runs, **Then** agents use it instead of re-deriving the procedure in context, and they keep it current as the job changes.
8. **Given** a command already completes the same job, **When** agents would add a helper, **Then** they run that command instead of wrapping it.
---

### User Story 5 - Fill the error ledger, drain it when the wiki improves (Priority: P5)

When a Co-DM operation fails at runtime, agents write that failure to the error ledger (`errors.md`). They do not wait for the DM. When later work improves the wiki — or otherwise actually removes the cause — agents drain the matching entries. A drained entry is gone because the cause is fixed, not because someone cleared the file. Leftover entries for already-fixed causes are wasted context. Filling and draining the ledger is agent-owned. A wiki write that is the fix still waits on the DM accept-gate; the drain happens after that write lands.

**Why this priority**: An undrained ledger is a second brain of unfixed failure. Filling without draining is noise. Draining without a fix hides the failure. The improvement loop has to do both.

**Independent Test**: Cause a runtime failure. Confirm an entry exists. Land a wiki improvement that removes the cause. Confirm that entry is gone and that no other entry disappeared without its cause being fixed. The DM was not asked to edit the ledger.

**Acceptance Scenarios**:

1. **Given** a Co-DM operation that fails at runtime, **When** that sitting ends, **Then** the error ledger contains an entry for that failure. The DM was not asked to write it.
2. **Given** an error ledger entry whose cause a wiki improvement has actually removed, **When** that wiki improvement has landed, **Then** agents have drained that entry.
3. **Given** an error ledger entry whose cause is not yet fixed, **When** agents improve the wiki for other reasons, **Then** that entry remains.
4. **Given** a wiki write that would fix a recorded error, **When** the DM has not accepted that write, **Then** the wiki is unchanged and the entry is not drained.
5. **Given** a drained entry, **When** inspected, **Then** the cause was fixed; the entry was not removed as cleanup without a fix.
---

### User Story 6 - Layout grows into agent-shaped structure (Priority: P6)

As helpers, ledgers, skills, **and wiki pages** accumulate, agents reorganize files and folders so a later sitting can find the one file it needs without loading unrelated trees. That includes the wiki (llm-wiki). Layout is optimized for agent use: names and locations match the job or page kind, mixed dumps are split, and unused paths are not standing load. Agents do this as the system grows. They do not wait for the DM. A layout change that makes lookup slower or loads more unrelated material is not an improvement. Moving or regrouping a wiki page without changing its facts is layout, not a canon write. Changing wiki facts still waits on accept. When a page moves, agents keep it findable (links and names still resolve).

**Why this priority**: Growth without organization is wasted context. Agents already own token cost and helpers; layout is the same job at folder scale, including the wiki they retrieve from.

**Independent Test**: Start from a mixed dump of unrelated agent files **and** mixed wiki pages of different kinds. After growth-triggered organization, a later sitting for one named job or one page kind opens only the files for that job or kind. The DM was not asked for the layout change. A reorg that scatters the needed file or forces a wider load does not count. Wiki facts were not rewritten. Links still resolve.

**Acceptance Scenarios**:

1. **Given** agent-facing files for different jobs mixed in one place, **When** that mix has grown past a single sitting's job, **Then** agents split or move them so each job has a findable location, without asking the DM.
2. **Given** wiki pages of different kinds mixed so lookup loads unrelated trees, **When** that mix has grown, **Then** agents regroup them for agent lookup without asking the DM, and without changing page facts.
3. **Given** that organization, **When** a later sitting runs one named job or retrieves one page kind, **Then** agents find those files without loading unrelated trees, at equal or lower token cost.
4. **Given** a layout change that increases hops or unrelated load for the same job or page kind, **When** it is judged as an improvement, **Then** it does not count as one.
5. **Given** a wiki layout move, **When** it lands, **Then** page facts are unchanged, links still resolve, and the DM was not asked to accept the move.
6. **Given** a change to wiki facts, **When** agents would file it, **Then** that change still waits on the DM accept-gate. Layout is not a path around canon.
7. **Given** a one-off file that is not growing a mixed dump, **When** agents consider reorganizing, **Then** they leave it; growth, not tidiness, is the trigger.

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
- Cutting tokens by omitting a quality evaluation or the DM accept-gate for campaign Work: not an improvement.
- Adding standing context the Co-DM must always read, when that context does not prevent a named failure: wasted context; agents cut it; the DM is not asked.
- Token-cost changes that would also change campaign wiki facts or player-visible Work: those campaign effects still need the DM accept-gate; the token-cost part does not wait on the DM.
- Asking the DM to review or accept a token-cost number: out of scope; agents own that metric.
- One-off job that will not repeat: do not create a helper.
- Helper goes stale: agents update or remove it. A stale helper agents still load is wasted context.
- Helper that only a human can operate: not agent-shaped; does not count.
- Helper that changes campaign wiki facts or player-visible Work: those campaign effects still need the DM accept-gate.
- Asking the DM to request, review, or accept a helper: out of scope; agents own that work.
- Runtime failure with no ledger entry: incomplete sitting; fill the ledger.
- Draining the whole ledger because some entries were fixed: invalid; drain only matching fixed causes.
- Filling the ledger with process talk or token-cost numbers the DM must review: out of scope; the ledger is agent-owned.
- Error whose fix is not a wiki change (a helper, wasted-context cut): drain when that fix lands; still no DM gate unless the fix is campaign-facing.
- Reorganizing agent-facing or wiki layout on a one-off file: skip; wait until mixed growth makes lookup costly.
- Layout change that hides the file an agent needs or requires a wider tree load: not an improvement.
- Moving or regrouping a wiki page without changing facts: layout; agents do it; the DM is not asked.
- Changing wiki facts under the cover of a layout move: invalid; that is a canon write and still needs accept.
- Asking the DM to approve folder names for helpers, ledgers, scripts, or wiki grouping: out of scope; agents own layout.
- Wiki layout move that leaves broken links: incomplete; agents keep the page findable in the same change.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The DM MUST be able to record who the players are and the current campaign intent for those players.
- **FR-002**: The Co-DM MUST work from that recorded aim. Work that could be swapped onto a different table without edits MUST NOT count as aimed.
- **FR-003**: When no table aim is recorded, the Co-DM MUST ask for it before treating Work as aimed.
- **FR-004**: When the DM updates the players or the intent, later Work MUST use the updated aim.
- **FR-005**: A missing wiki fact or missing Co-DM practice MUST NOT prevent the Co-DM from offering playable Work in that sitting.
- **FR-006**: When Work is offered despite a gap, the Co-DM MUST name the gap to the DM.
- **FR-007**: A proposed change to how the Co-DM works that would change campaign Work or what the DM sees MUST be a proposal the DM accepts, edits, or rejects. The Co-DM MUST NOT apply that campaign-facing change before accept. Token-cost-only changes, helper work, error-ledger fill/drain, and layout changes (agent-facing **or** wiki file/folder layout) that do not change Work quality or wiki facts MUST follow FR-019 through FR-046 instead, with no DM accept step.
- **FR-008**: After wrapup, the Co-DM MUST offer a reflection that names at least one concrete observation about these players.
- **FR-009**: After prep, the Co-DM MUST offer a reflection when the DM asks, and MUST NOT require the DM to ask in wrapup.
- **FR-010**: A reflection MUST be accept-or-reject Work. It MUST NOT write wiki facts by itself. It MUST NOT apply a campaign-facing practice change by itself.
- **FR-011**: An accepted reflection that calls for a campaign fact to change MUST become a canon proposal and MUST still wait for accept before any wiki write.
- **FR-012**: An accepted reflection that calls for a campaign-facing change in how the Co-DM works MUST become an improvement proposal and MUST still wait for accept before that change is applied.
- **FR-013**: After the DM accepts an improvement, later sittings of that kind of job MUST follow the accepted change.
- **FR-014**: The Co-DM MUST NOT run reflection or improvement during a session.
- **FR-015**: Campaign wiki **fact** writes, invention marking, and the DM accept-gate from the existing Co-DM product still bind. This loop MUST NOT create a second path around canon. Wiki **layout** (where pages live, how they are grouped) is FR-039 through FR-046, not a canon write.
- **FR-016**: Existing quality evaluation for D&D content guidance, and existing rules for who may redesign how the Co-DM is instructed, still bind. This loop MUST NOT skip them.
- **FR-017**: The Co-DM MUST address reflections and improvement proposals to the DM, never to the players.
- **FR-018**: Agent and DM communication in this loop MUST be inspectable after the fact (aim, Work, reflection, proposal, accept or reject, applied change). Token cost is inspectable to agents. The DM MUST NOT be required to review it.
- **FR-019**: Each prep or wrapup sitting MUST record its token cost (how much the Co-DM had to read and write to finish that sitting's jobs). Agents MUST record it. The DM MUST NOT be asked to record or accept it.
- **FR-020**: Token cost of an operation or sitting MUST be a core metric of self-improvement, alongside whether Work served these players. Agents MUST own that metric. The DM MUST NOT manage, review, or gate it.
- **FR-021**: A change MUST NOT count as an improvement if it raises token cost for the same jobs without preventing a named failure.
- **FR-022**: A change MUST NOT count as an improvement if it lowers token cost by lowering Work quality.
- **FR-023**: Completing more accepted Work in a sitting at the same quality and at equal or lower token cost MUST count as an efficiency win. Agents MUST pursue that win without a DM accept step.
- **FR-024**: Standing context the Co-DM must read or write that does not change the sitting's outcome MUST be treated as wasted context. Agents MUST cut it when they can do so without lowering quality. They MUST NOT wait for the DM.
- **FR-025**: Agents MUST objectively decrease token cost of same-kind sittings over time when quality holds. "Objectively" means same jobs, measured token cost, quality still passing — not DM opinion.
- **FR-026**: Agents MUST proactively create reusable, flexible, agent-shaped helpers when that would lower token cost of a repeating job. They MUST NOT wait for the DM or for a request.
- **FR-027**: Agents MUST maintain those helpers as the job changes. A stale helper that agents still load MUST be treated as wasted context: update it or remove it.
- **FR-028**: A helper MUST be agent-shaped: invocable without a GUI, arguments in, text or structured output out, and an exit that distinguishes done from failed. A human-only wrapper MUST NOT count.
- **FR-029**: A helper MUST be reusable and flexible enough for the next same-kind sitting's inputs. A one-shot hardcode that cannot take the next sitting's inputs MUST NOT count.
- **FR-030**: Agents MUST NOT wrap a command that already completes the same job. They MUST run that command.
- **FR-031**: A helper that does not lower token cost of a later same-kind sitting, or that lowers Work quality, MUST NOT count as an efficiency win.
- **FR-032**: This spec MUST govern the error ledger (`errors.md`): runtime fill and drain-on-fix.
- **FR-033**: When a Co-DM operation fails at runtime, agents MUST append an entry to the error ledger before the sitting is complete. They MUST NOT wait for the DM.
- **FR-034**: When a wiki improvement or other landed fix actually removes the cause of an error ledger entry, agents MUST drain that entry.
- **FR-035**: Agents MUST NOT drain an entry whose cause is not yet fixed.
- **FR-036**: After a wiki improvement lands, leftover ledger entries for causes that improvement fixed MUST be treated as wasted context and drained in the same sitting.
- **FR-037**: The DM MUST NOT be required to fill, review, or drain the error ledger. A wiki write that is the fix still waits on the DM accept-gate; drain MUST wait until that write has landed.
- **FR-038**: An undrained ledger of already-fixed errors MUST count as wasted context, not as an improvement record.
- **FR-039**: Agents MUST self-organize agent-facing files and folders **and** the wiki (llm-wiki) as the system grows, so a later sitting can find the file for a named job or page kind without loading unrelated trees.
- **FR-040**: Layout MUST be optimized for agent use: names and locations match the job or page kind; mixed dumps of unrelated jobs or kinds MUST be split; unused paths MUST NOT stay in standing load.
- **FR-041**: Agents MUST NOT wait for the DM to request, review, or accept layout changes (agent-facing or wiki grouping).
- **FR-042**: A layout change that increases lookup cost or unrelated load for the same job or page kind MUST NOT count as an improvement.
- **FR-043**: A wiki layout move or regroup MUST NOT change page facts. Changing wiki facts MUST still wait on the DM accept-gate.
- **FR-044**: One-off files MUST NOT be reorganized solely for tidiness. Growth that makes lookup costly is the trigger.
- **FR-045**: When a wiki page moves or is regrouped, agents MUST keep it findable in the same change (links and names still resolve).
- **FR-046**: Layout MUST NOT be used as a path around the canon accept-gate.

### Key Entities

- **DM**: The human who runs the session. Sole table runtime. Judge of whether the campaign is serving these players.
- **Co-DM**: Agent work in prep and wrapup. Addresses the DM, never the players, and does not run during a session.
- **Players**: The humans at this table. They receive the campaign. They do not operate the wiki or the Co-DM.
- **Table aim**: Who these players are, and what this campaign is currently trying to be for them. Recorded by the DM. The shared target for alignment.
- **Work**: Mutable prep the DM may accept, edit, or reject.
- **Gap**: A missing wiki fact or missing Co-DM practice that would otherwise be used for this sitting's job.
- **Reflection**: Work offered after wrapup (and after prep when asked) that names what served these players and what did not.
- **Canon proposal**: A suggested change to wiki facts. Not applied unless the DM accepts.
- **Improvement proposal**: A suggested campaign-facing change to how the Co-DM works. Not applied unless the DM accepts. Does not include token-cost-only cuts.
- **Wiki**: Compiled, citable campaign pages. Human prose. Source of truth for canon.
- **Token cost**: How much the Co-DM must read and write to finish one operation or one sitting. Core metric of self-improvement. Owned by agents, not the DM.
- **Wasted context**: Reading or writing that does not change the sitting's outcome. Agents cut it when quality holds. The DM does not gate that cut.
- **Agent-shaped helper**: A reusable command agents create and maintain so a later sitting spends fewer tokens on the same job. Arguments in, result out, done vs failed. Owned by agents, not the DM.
- **Error ledger** (`errors.md`): Agent-owned list of runtime failures. Filled when operations fail. Drained when the cause is actually fixed, including when improving the wiki.
- **Agent-facing layout**: How helpers, ledgers, skills, and other agent files are named and grouped. Owned by agents.
- **Wiki layout**: How wiki (llm-wiki) pages are named and grouped. Owned by agents. Optimized for findability and token cost as the system grows. Not a change to page facts.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Given a named table of at least three players and a current campaign intent, the DM and the Co-DM independently state the same players and the same intent on 100% of a three-trial check.
- **SC-002**: In a review of at least five accepted prep proposals written after a table aim exists, a second DM who knows a different table marks at least 80% as not reusable for that other table without edits.
- **SC-003**: When a sitting's job has a missing wiki fact or missing Co-DM practice, the DM receives playable Work in that sitting 100% of the time, and the gap is named 100% of the time.
- **SC-004**: In those gap sittings, 0% of campaign-facing Co-DM practice changes are applied before the DM accepts an improvement proposal. Token-cost-only cuts are excluded from this count.
- **SC-005**: After wrapup of a sample of at least three sessions, 100% include a reflection the DM can accept, edit, or reject, and 100% of those reflections name a concrete observation about these players.
- **SC-006**: 0% of rejected reflections produce a wiki write or a campaign-facing Co-DM practice change.
- **SC-007**: Of accepted reflections that name a needed campaign or campaign-facing change, 100% produce a follow-up canon proposal or improvement proposal the DM can act on in the same sitting, rather than ending only as chat.
- **SC-008**: In a debrief after at least three sessions, the DM rates Co-DM Work as aimed at these players (not generic D&D) for 80% or more of accepted Work.
- **SC-009**: A DM can review one chain — reflection to accepted proposal to visible campaign change — in under 10 minutes without a second operator.
- **SC-010**: 0% of sampled sessions have reflection or improvement running while play is happening.
- **SC-011**: After agents apply an efficiency change with no DM accept step, a repeat of the same sitting kind finishes the same jobs at a lower token cost in 100% of sampled pairs, and quality still passes the bar that applied before the change.
- **SC-012**: 0% of agent-applied efficiency changes raise token cost for the same jobs without naming the failure they prevent.
- **SC-013**: 0% of agent-applied efficiency changes produce Work that fails the quality bar that applied before the change.
- **SC-014**: In those same-kind pairs, the later sitting yields at least as many accepted Work items as the earlier sitting.
- **SC-015**: In a sample of at least five token-cost records and efficiency cuts, 0% required the DM to record, review, or accept the token cost.
- **SC-016**: In a sample of at least three repeating same-kind sittings where a helper would lower token cost, 100% of later sittings use an existing helper rather than re-deriving the procedure in context.
- **SC-017**: 0% of those helpers were requested, reviewed, or accepted by the DM.
- **SC-018**: 100% of those helpers are invocable as a command (arguments in, text or structured result out, done vs failed).
- **SC-019**: 0% of those helpers wrap a command that already completed the same job.
- **SC-020**: After the repeating job changes, 100% of sampled helpers are updated or removed before the next sitting; 0% remain stale and still loaded.
- **SC-021**: In a sample of at least five runtime Co-DM failures, 100% produce an error ledger entry before the sitting ends, with 0% requiring the DM to write it.
- **SC-022**: After a wiki improvement that removes the cause of recorded errors, 100% of matching entries are drained in that sitting.
- **SC-023**: 0% of drained entries in that sample were removed without the cause being fixed.
- **SC-024**: In a sample of at least five fill or drain actions, 0% required the DM to edit the error ledger.
- **SC-025**: After a mixed dump of unrelated agent-facing files **or** mixed wiki kinds is organized, a later sitting for one named job or one page kind loads files for that job or kind only, in 100% of sampled jobs, at equal or lower token cost.
- **SC-026**: 0% of those layout changes (agent-facing or wiki grouping) required the DM to request, review, or accept them.
- **SC-027**: 0% of sampled layout changes that increased hops or unrelated load for the same job or page kind are counted as improvements.
- **SC-028**: In that sample, 0% of wiki layout moves change page facts, and 100% keep links resolving.
- **SC-029**: 0% of sampled wiki fact changes are filed as layout moves without the DM accept-gate.

## Assumptions

- Primary user is the human DM. Players receive the campaign; they do not operate this loop.
- "Best possible campaign" is judged by the DM for this table. There is no hidden quality score the Co-DM optimizes without the DM.
- This feature is the improvement loop around the existing Co-DM product. It does not replace ingest, prep proposals, play-surface staging, or wrapup filing.
- v1 remains one campaign, one table, D&D 5e.
- Self-bootstrap means: produce Work from an incomplete start and name the gap. It does not mean the Co-DM rewrites campaign-facing practice without accept.
- Self-reflection means: after wrapup (and after prep when asked), offer inspectable observations about these players. It does not mean a live agent at the table, and it does not mean contacting players.
- Self-improvement means: accepted reflections become proposals the DM gates when they change the campaign or what the DM sees. Token cost of the sitting is a core metric owned by agents: more Work at the same quality, less wasted context, proactive agent-shaped helpers, self-organized agent-facing **and wiki** layout, no DM review of layout.
- Creativity, communication, and collaboration are already the Co-DM experiment. This feature adds shared aim and a closed improve-with-accept loop for campaign Work. It does not add a second communication path to players. It does not make the DM an efficiency or folder reviewer.
- Fun may still shape Work. Wiki facts still change only when the DM accepts a canon proposal. Wiki file and folder layout is not a fact change.
- One reflection per wrapup is enough unless the DM asks for another.
- Token cost is how much the Co-DM must read and write to finish the jobs. Agents manage it and decrease it objectively, including by creating and maintaining reusable agent-shaped helpers and by organizing files and folders — including the wiki (llm-wiki) — for agent lookup as the system grows. Quality is a constraint, not a trade. Fewer tokens that produce worse Work is not improvement. More tokens for the same jobs is not improvement unless they prevent a named failure. The DM is not asked to accept token-cost numbers, efficiency-only cuts, helpers, or layout.
- The error ledger (`errors.md`) is agent-owned. Runtime failures fill it. Wiki improvements and other landed fixes drain matching entries. Drain without a fix is a defect. Leaving fixed errors in the ledger is wasted context.
- Out of scope: a Co-DM agent during a session; player accounts or player-operated feedback; autonomous rewrite of campaign **canon facts**; replacing existing content evaluation or instruction-redesign rules for D&D content guidance; multi-campaign orchestration; non-5e rules systems; billing; replacing the DM; a hidden quality score; the DM managing or gating token cost, helpers, the error ledger, or layout; human-only wrappers; wrapping a command that already does the job; reorganizing one-off files for tidiness.
