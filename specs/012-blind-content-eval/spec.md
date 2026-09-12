# Feature Specification: Blind Cold Evaluation of D&D Content

**Feature Branch**: `012-blind-content-eval`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: simple script-based validation of output is not suitable for this repo. This is an agentic creativity project. Changes to skills, instructions, and similar that produce D&D content must be tested and validated objectively using blind cold evaluation by separate evaluators. Not only must the form of content be correct (layout, format, shape, mechanics) but it must be used appropriately. Copy text must be of the highest quality, ideal for a DM reference. Player-facing text (narration) must be the highest quality theatre of the mind text possible.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Blind cold evaluation is the test (Priority: P1)

Someone has changed a skill, standing instruction, or procedure that produces D&D wiki content. Before that change is treated as done, sample content those instructions produce is given to evaluators who did not author it and who do not see the authoring session. Script scoring of the output is not the acceptance test. The change is incomplete until those evaluators pass it on the axes below.

**Why this priority**: Scripts can check punctuation and miss a useless DM page or unspeakable narration. Blind cold evaluation is the only test that matches a creativity product.

**Independent Test**: Produce sample content from the changed guidance. Give it to a second evaluator with no authoring transcript. They can pass or fail it on form, appropriate use, DM copy, and spoken look (when those bands exist) without asking the author what was intended.

**Acceptance Scenarios**:

1. **Given** a change to guidance that produces D&D wiki content, **When** it is treated as done, **Then** sample content from that guidance has been passed by evaluators who did not produce it and did not see the authoring session.
2. **Given** only a script or checklist over the output file, **When** the change is reviewed, **Then** that is not sufficient to treat the change as done.
3. **Given** a change to guidance that does not produce D&D wiki content, **When** it is reviewed, **Then** this evaluation is not required.

---

### User Story 2 - Form is correct and used appropriately (Priority: P2)

Evaluators judge layout, format, shape, and mechanics. Correct form that is used for the wrong job fails (a mechanic as decoration, a layout that hides the choice, a shape that does not match the kind). The page must be usable as the kind of Work it claims to be.

**Why this priority**: Pretty wrong is still wrong. Form without appropriate use is how a DM gets a page they cannot run.

**Independent Test**: Give an evaluator a sample page and the kind it claims to be. They can say whether layout, format, shape, and mechanics match that kind and are used for the jobs those treatments mean — without being told the author's intent.

**Acceptance Scenarios**:

1. **Given** sample D&D content, **When** evaluated cold, **Then** layout, format, shape, and mechanics match the kind of Work it claims to be.
2. **Given** a mechanic, layout treatment, or shape used for a job it does not mean, **When** evaluated, **Then** the sample fails even if the file is well-formed.
3. **Given** a sample with no mechanical band (spoken-only handout), **When** evaluated, **Then** mechanical form is not required.

---

### User Story 3 - DM copy is a table-ready reference (Priority: P3)

DM-facing bands are copy a human DM can run: complete-sentence prose, signal-dense, a recipe not a story and not telegram. Agent-speak, slash-stacks, and filler fail. This is ordinary human reference quality, not a novel.

**Why this priority**: The wiki exists so a DM can run a session. Bad DM copy is unusable at the table even when the shape is correct.

**Independent Test**: Give an evaluator only the DM-facing bands. They can use them as a reference in a mock run without decoding agent shorthand, and they would not score the text as a finished story or as telegram stubs.

**Acceptance Scenarios**:

1. **Given** DM-facing bands, **When** evaluated cold, **Then** they are complete-sentence human prose a DM can use as a table reference.
2. **Given** telegram stubs, slash-stacks, or agent-speak in those bands, **When** evaluated, **Then** the sample fails.
3. **Given** a sample with no DM-facing band (player-only handout), **When** evaluated, **Then** DM-copy quality is not required.

---

### User Story 4 - Spoken look is theatre of the mind (Priority: P4)

Player-facing narration is spoken look: a drawable picture a second person can read aloud. Secrets, difficulty classes, unearned names, and process notes stay out. Padding and telegram both fail.

**Why this priority**: Players hear only what the DM presents. Weak or leaky narration is the mouth-surface failure.

**Independent Test**: Give a second person only the player-facing passages. They can read them aloud without a secret, DC, unearned name, or process note, and the picture is drawable.

**Acceptance Scenarios**:

1. **Given** player-facing narration, **When** evaluated cold, **Then** it is theatre of the mind: drawable, speakable, free of secrets, difficulty classes, unearned names, and process notes.
2. **Given** telegram stubs or verbose padding in those passages, **When** evaluated, **Then** the sample fails.
3. **Given** a sample with no player-facing band, **When** evaluated, **Then** theatre of the mind quality is not required.

---

### Edge Cases

- Evaluators did not produce the sample and do not see the authoring transcript, the skill diff, or the author's notes. Seeing those makes the evaluation not cold.
- Two independent evaluators. One author self-review is not this test.
- Axes that do not apply (no spoken band, no mechanics) are omitted, not failed.
- Script or format checkers may still run as chores. They cannot pass the change by themselves.
- Ordinary wiki content jobs that are not changing D&D content guidance are outside this feature's required eval (they still follow 010 writing authorities and the DM accept-gate).
- Non-D&D-content skills (search, ingest plumbing, contributor docs) are outside this eval.
- The DM accept-gate still binds. Blind eval does not write silent canon.
- Spoken look stays theatre of the mind; DM procedure stays out of it. 010 authorities still apply.
- Legacy wiki pages are not rewritten solely to prove this eval.
- A sample that matches a template heading-for-heading but is unusable or unspeakable fails (form without appropriate use or quality).
- Disagreement between the two evaluators: the change is not done until they agree on pass, or the sample is revised and re-evaluated.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: A change to a skill, standing instruction, or procedure that produces D&D wiki content MUST NOT be treated as done until sample content from that guidance has passed blind cold evaluation.
- **FR-002**: Evaluators MUST be people or agents who did not produce the sample and MUST NOT see the authoring session, skill diff, or author notes while judging.
- **FR-003**: Script scoring, file-shape checkers, and similar automatic checks MUST NOT be sufficient to pass the change.
- **FR-004**: Evaluation MUST cover every axis that applies to the sample: form (layout, format, shape, mechanics), appropriate use of that form, DM-copy quality, and theatre of the mind quality.
- **FR-005**: Form MUST match the kind of Work the sample claims to be.
- **FR-006**: Form MUST be used for the jobs those treatments mean. Decorative or swapped use of a mechanic, layout, or shape MUST fail.
- **FR-007**: DM-facing bands MUST be complete-sentence human prose a DM can use as a table reference. Telegram stubs, slash-stacks, and agent-speak MUST fail.
- **FR-008**: Player-facing narration MUST be theatre of the mind: drawable, speakable, with no secret, difficulty class, unearned name, or process note. Telegram stubs and verbose padding MUST fail.
- **FR-009**: Axes with no corresponding band MUST be omitted, not failed.
- **FR-010**: At least two independent evaluators MUST judge the sample. The change is incomplete while they disagree on pass/fail.
- **FR-011**: Guidance that does not produce D&D wiki content MUST NOT be required to use this evaluation.
- **FR-012**: Existing Work rules still bind: chat proposal first; wiki write after DM accept, except named ingest stubs. Evaluation MUST NOT write silent canon.
- **FR-013**: Writing and visual authorities still apply (agent, DM, players, vault, visual-references, visual-aids). This evaluation MUST NOT reassign them.
- **FR-014**: Legacy wiki pages MUST NOT be rewritten solely to satisfy this feature.

### Key Entities

- **Guidance change**: An edit to a skill, standing instruction, or procedure that produces D&D wiki content.
- **Sample content**: Work produced from that changed guidance for evaluation. Not the skill file itself as the judged object.
- **Blind cold evaluation**: Judgment by evaluators who did not produce the sample and do not see the authoring session.
- **Evaluator**: An independent judge. Not the author.
- **Form**: Layout, format, shape, and mechanics of the sample.
- **Appropriate use**: Those treatments mean the jobs they are supposed to mean for that kind of Work.
- **DM copy**: DM-facing bands. Table reference, not a novel, not telegram.
- **Spoken look**: Player-facing narration. Theatre of the mind.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: After this rule is in force, 100% of changes to D&D content-producing guidance that are treated as done have a sample that passed blind cold evaluation by at least two independent evaluators.
- **SC-002**: In a review of those evaluations, 0% were passed by script scoring alone.
- **SC-003**: Two independent cold evaluators agree on pass/fail for 100% of a set of at least 8 samples covering form, appropriate use, DM copy, spoken look, a no-spoken-band sample, and a no-mechanic sample.
- **SC-004**: In a review of passed DM-facing bands, 0% are telegram, slash-stacks, or agent-speak; 100% are usable as a table reference in complete sentences.
- **SC-005**: In a read-aloud test of passed player-facing passages, 100% can be presented without a secret, difficulty class, unearned name, or process note, and a second person judges the picture drawable.
- **SC-006**: In a review of passed samples that claim a kind, 100% use layout, format, shape, and mechanics for the jobs of that kind — not as decoration.
- **SC-007**: After this rule is in force, 0% of legacy wiki pages are rewritten solely to match it.

## Assumptions

- The object under test is sample content produced from the changed guidance, not the skill file's own prose as DM copy.
- "Blind" and "cold" mean the evaluator did not author the sample and does not see the authoring transcript, skill diff, or author notes while judging.
- Two evaluators is the default. More is allowed. One is not this test.
- "Highest quality" for DM copy means table-ready reference as defined in the copy-writer outcome (complete sentences, signal-dense recipe). It does not mean a published novel.
- "Highest quality" for narration means theatre of the mind as defined in 010: drawable, speakable, leak-free, neither telegram nor padding.
- Script and format chores may still run unattended. They are not the acceptance test.
- This eval is required when D&D content-producing guidance changes. It is not required on every ordinary wiki write.
- The DM remains the accept-gate for canon. Evaluators do not publish to players.
- Out of scope: replacing 010 writing authorities; rewriting legacy pages to prove eval; using this eval on search/ingest plumbing; treating a heading-order matcher as pass.
