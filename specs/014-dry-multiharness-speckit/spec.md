# Feature Specification: DRY Multi-Harness Spec Kit

**Feature Branch**: `014-dry-multiharness-speckit`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: "Repair this existing repository so Spec Kit and coding-agent configuration is DRY across Codex, Grok Build, Oh My Pi, occasional Claude Code, and Grok Bot as an outer-loop orchestrator. One canonical project-instruction layer, one Spec Kit state, one copy of every feature artifact, native Spec Kit adapters per coding harness, no manually synchronized prompts, no duplicated project policy, no harness-specific copies of feature requirements, deterministic handoff, manifest-aware maintenance, drift protection. Preserve existing unique instructions; do not repair by deleting everything or force-reinitializing first. Generated adapter similarity is not a DRY violation; human-maintained semantics have exactly one owner. Use Spec Kit's default Python implementation (not shell scripts, not custom Spec Kit scripts) so every harness can run maintenance."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - One owner for every project fact (Priority: P1)

A maintainer (or an agent acting for them) can point at any project rule, requirement, decision, or workflow and name exactly one authoritative document. Other places either stay silent or point at that owner. The operating map tells agents where to look; it is not a second copy of principles, feature requirements, or harness runtime settings.

**Why this priority**: Duplicate owners are how agents diverge. Every later story depends on a single compiled truth.

**Independent Test**: Pick a sample of operating rules, feature requirements, and engineering principles from current sessions. For each, exactly one owner document contains the fact; other agent-facing files do not restate it.

**Acceptance Scenarios**:

1. **Given** a project operating rule, **When** a maintainer asks where it lives, **Then** the answer is the canonical repository operating contract, not a harness-specific rewrite.
2. **Given** a non-negotiable engineering principle, **When** it is inspected, **Then** it has one authoritative copy in the project constitution and is not pasted into operating maps, generated adapters, or orchestrator instructions.
3. **Given** a feature requirement, **When** it is inspected, **Then** it lives in that feature's specification (with design and work graph downstream of it), not in harness configuration or prompts.
4. **Given** the same rule appearing in multiple agent files today, **When** repair completes, **Then** one owner remains and the other copies are gone or reduced to a reference.
5. **Given** a coding session in any supported harness, **When** the agent loads project instructions, **Then** it follows the same ownership map rather than a harness-local policy twin.

---

### User Story 2 - Repair preserves unique human intent (Priority: P1)

This repository already exists. Repair starts by preserving current state, classifying each configuration file, and migrating unique human intent to its owner. It does not begin by deleting harness directories or force-reinitializing Spec Kit. Force re-initialization is only the last resort when integration metadata cannot be recovered.

**Why this priority**: Unique instructions lost in a wipe cannot be reconstructed from conversation. Preservation is the difference between repair and vandalism.

**Independent Test**: Start from a snapshot that includes unique notes in both canonical files and generated adapters. After repair, every unique note is in its owner document; generated adapters no longer carry those notes; Spec Kit history and existing feature specifications remain.

**Acceptance Scenarios**:

1. **Given** the existing repository, **When** repair begins, **Then** current configuration is snapshotted or otherwise preserved before mutation.
2. **Given** a configuration file with unique human intent, **When** it is classified, **Then** that intent is migrated to its owner before the file is regenerated or removed.
3. **Given** healthy integration metadata, **When** adapters need refresh, **Then** repair upgrades or installs integrations in place and does not force-reinitialize the project.
4. **Given** unusable or missing integration metadata, **When** no other recovery works, **Then** force re-initialization may run after preservation, and existing feature specifications, constitution, source, and tests still survive.
5. **Given** an existing feature specification, **When** this repair runs, **Then** that specification remains the authority for its feature; repair does not invent a second copy.

---

### User Story 3 - Native disposable adapters, no hand-copied workflows (Priority: P2)

Each supported coding harness invokes Spec Kit through that harness's native generated adapter. Humans do not copy Spec Kit prompts, commands, or feature requirements between harnesses. After unique intent is migrated out, generated adapters can be regenerated without losing project knowledge. Obsolete hand-copied Spec Kit command sets are removed once native adapters work.

**Why this priority**: Hand-copied workflows drift on the next upgrade. Native generated adapters are how four harnesses share one protocol.

**Independent Test**: Inventory Spec Kit entry points. Each of Codex, Grok Build, Oh My Pi, and Claude Code has a native generated adapter; no extra hand-copied Spec Kit command directory remains active; regenerating adapters does not drop any unique project rule.

**Acceptance Scenarios**:

1. **Given** Codex, Grok Build, Oh My Pi, and Claude Code, **When** a maintainer inspects Spec Kit entry points, **Then** each harness has its native generated adapter and uses it when that harness is invoked.
2. **Given** a generated adapter, **When** a human is tempted to add a project rule there, **Then** the rule is instead added to the owner document; the adapter stays disposable.
3. **Given** leftover hand-copied Spec Kit commands or prompts, **When** native adapters are healthy, **Then** the leftovers are removed after any unique intent is migrated.
4. **Given** two harnesses' generated adapters, **When** they contain similar generated wording, **Then** that similarity is accepted; it is not treated as a DRY violation.
5. **Given** Spec Kit extensions or presets, **When** repair finishes, **Then** they are registered for each installed coding harness without copying shared project state into those harnesses.

---

### User Story 4 - Compatibility discovery does not create a second policy (Priority: P2)

Claude Code reads a thin import of the canonical operating contract, not a second policy manual. Grok Build and Oh My Pi must not quietly re-ingest Claude's copy (or each other's copies) as competing instructions. Harness-specific files contain only genuine harness-specific deltas.

**Why this priority**: Even with one owner on disk, compatibility loaders can compile a second brain at runtime.

**Independent Test**: Inspect what each harness actually loads. Claude imports the canonical contract. Grok and Oh My Pi resolve the canonical contract rather than a Claude shadow. No harness-specific file restates project policy.

**Acceptance Scenarios**:

1. **Given** Claude Code, **When** it loads project instructions, **Then** it consumes the canonical operating contract through a thin compatibility import and does not keep a full duplicate policy file at the repository root.
2. **Given** Grok Build, **When** it resolves instructions and skills, **Then** it loads the canonical operating contract and native Grok Spec Kit adapters; it does not take Claude instruction, skill, or rule copies as project policy.
3. **Given** Oh My Pi, **When** it resolves project context, **Then** the canonical operating contract wins; a Claude project instruction file does not shadow it.
4. **Given** a harness-specific configuration file, **When** it is reviewed, **Then** it contains only concerns unique to that harness (runtime, permissions, discovery isolation), not feature requirements or constitution text.
5. **Given** Codex, **When** a new session starts, **Then** it recognizes the canonical operating contract and native Codex Spec Kit adapters.

---

### User Story 5 - Handoff is repository state, not a replayed prompt (Priority: P2)

Work moves between harnesses by pointing at repository artifacts, commits, and evidence. A new harness does not redesign a feature that already has a specification. At any moment, each canonical artifact has one writer. Parallel implementation uses separate workspaces, not shared mutation of one workspace.

**Why this priority**: Re-specifying in each harness creates competing realities. Last-writer-wins on a shared workspace corrupts the protocol.

**Independent Test**: Walk a feature from specification in one harness to planning, tasks, implementation, and independent review in others. There is still one spec, one plan, one task graph, and one implementation owner per workspace.

**Acceptance Scenarios**:

1. **Given** an existing feature specification, **When** a different harness is asked to continue the work, **Then** it reads the specification (and downstream artifacts) instead of reconstructing the feature from the original prompt.
2. **Given** intended behavior that must change, **When** agents update artifacts, **Then** they change the specification first and reconcile design and tasks afterward; they do not silently redefine requirements in the task graph or in code.
3. **Given** a canonical artifact (specification, design, task graph, or a writable workspace), **When** more than one agent is involved, **Then** only one writer mutates that artifact at a time; others may research, review, test, or propose.
4. **Given** parallel implementation slices, **When** they run, **Then** each writable slice has its own workspace; multiple write-capable harnesses are not aimed at one workspace.
5. **Given** a change of harness, **When** handoff occurs, **Then** the receiving agent is given paths, commits, artifacts, expected phase, and constraints not already in the repository — not a pasted copy of canonical documents.

---

### User Story 6 - Outer-loop orchestration without a fifth source of truth (Priority: P3)

Grok Bot coordinates research, intake, harness choice, launch, monitoring, and review requests. It is not a Spec Kit integration and does not keep Bot-local copies of policy or specifications. Its reusable skill is procedure only.

**Why this priority**: An orchestrator that copies the repo becomes the most dangerous duplicate: it looks authoritative and is always stale.

**Independent Test**: Read the Bot skill and a sample dispatch. It points at repository files, names a coding harness and phase, and does not embed constitution text or feature requirements.

**Acceptance Scenarios**:

1. **Given** Grok Bot, **When** it takes a software task, **Then** it reads the canonical operating contract and current Spec Kit artifacts, selects a coding harness, and hands off objective, paths, phase, and extra constraints only.
2. **Given** the Bot skill, **When** it is inspected, **Then** it contains orchestration procedure, canonical-file pointers, prohibitions, and a required return report — not repository policy or specification text.
3. **Given** an existing specification, **When** the Bot launches a harness, **Then** it does not ask that harness to recreate the artifact.
4. **Given** Bot storage, **When** repair completes, **Then** there is no Bot-local Spec Kit command pack and no Bot-local copy of a feature specification.

---

### User Story 7 - Manifest-aware maintenance and drift detection (Priority: P3)

Maintainers verify repair by what each consumer actually loads, not by a tidy file tree. Spec Kit reports a clean multi-install of the four coding harnesses with a stable default. Automated checks fail on real integration errors and on the ownership invariants. Routine upgrades investigate modified generated files instead of blindly overwriting them. This repository uses Spec Kit's shipped Python implementation for maintenance scripts, not a Unix-shell-only variant and not a project-written replacement.

**Why this priority**: Configuration that only looks repaired will drift the first time a harness's compatibility loader or an upgrade rewrites adapters.

**Independent Test**: Run Spec Kit status in the healthy state (clean, four coding harnesses installed, chosen default). Inject an integration error and a forbidden duplicate policy file; automated checks fail. Run status/upgrade from more than one harness using Spec Kit's shipped Python implementation.

**Acceptance Scenarios**:

1. **Given** completed repair, **When** Spec Kit integration status is inspected, **Then** it is healthy, the four coding harnesses are installed, the chosen default is stable, and there are no unexplained missing or modified managed files, invalid manifests, unsafe overlap, or broken shared infrastructure.
2. **Given** each coding harness, **When** runtime inspection runs, **Then** that harness loads the intended context and native Spec Kit adapters.
3. **Given** an actual Spec Kit integration error, **When** the automated check runs, **Then** it fails rather than reporting success.
4. **Given** a generated adapter that a human edited, **When** maintenance runs, **Then** unique intent is migrated first; overwrite happens only as an intentional, inspected act — not as the default upgrade.
5. **Given** Spec Kit status, install, upgrade, or equivalent maintenance, **When** it is run from any supported coding harness, **Then** it uses Spec Kit's shipped Python implementation and does not require a Unix-shell-only variant or any project-authored Spec Kit script.

---

### Edge Cases

- Existing unique instructions live in generated adapters: migrate, then regenerate; do not overwrite first.
- Integration metadata is healthy: upgrade/install in place; do not force-reinitialize.
- Integration metadata is absent or unusable: preserve, then force-reinitialize as fallback only.
- Generated adapters for different harnesses differ in wording: allowed; do not demand identical bytes.
- Claude compatibility import exists: required thin shim, not a second manual; root-level full duplicate is forbidden.
- Grok also discovers Codex skill locations: keep native Grok adapters; verify which skill actually wins rather than assuming.
- Oh My Pi can discover many other harnesses: isolate enough that the canonical operating contract wins; do not disable unrelated model providers merely to isolate Claude discovery.
- User-level Grok compatibility settings cannot be enforced by the repository: document the required isolation; verify with Grok inspection; do not pretend a project file governs user-level discovery if it does not.
- Oh My Pi project isolation lists replace rather than merge with global lists: preserve existing intentional isolation when adding project isolation.
- A feature is already specified: later harnesses consume it; they do not specify it again.
- Trivial work may use a shorter Spec Kit flow; production work uses the full flow. Neither flow is recreated in harness-local prompts.
- Brownfield planning: new feature work inspects existing architecture, dependencies, tests, and implementation and reuses them unless the specification requires change.
- Parallel review can be read-only in a separate workspace; it must not mutate the implementation workspace.
- Harness roles are assigned by capability and availability; phases are not permanently bound to one product. Author and independent reviewer are different agents when review is warranted.
- Current project still has a shell-script Spec Kit setting: repair switches it to Spec Kit's shipped Python implementation; leftover shell-only generated maintenance files are treated as obsolete after that path works. The project MUST NOT add custom Spec Kit scripts to replace Spec Kit's own.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Every human-maintained fact, rule, requirement, decision, or workflow MUST have exactly one authoritative owner. Other locations MUST NOT restate it.
- **FR-002**: Repository operating instructions MUST have a single canonical operating contract that maps agents to deeper owners. That contract MUST NOT be an encyclopedia of principles, feature requirements, or harness runtime settings.
- **FR-003**: Project principles MUST have exactly one authoritative copy in the constitution. Other agent-facing files MUST reference or read it at runtime, not copy it.
- **FR-004**: Feature behavior and requirements MUST live in that feature's specification. Technical design MUST live in that feature's plan. The implementation work graph MUST live in that feature's tasks. Supporting research MUST live in that feature's Spec Kit artifacts.
- **FR-005**: Architecture documentation MUST live in canonical repository docs. Executable truth MUST live in source and tests.
- **FR-006**: Each coding harness's runtime configuration MUST own only that harness's runtime concerns. Spec Kit workflow adapters MUST be generated by Spec Kit and treated as disposable.
- **FR-007**: Repair MUST preserve existing state before mutation and MUST NOT start by deleting harness or Spec Kit directories or by force-reinitializing.
- **FR-008**: Unique human intent in any configuration file MUST be classified and migrated to its owner before that file is regenerated or removed.
- **FR-009**: When integration metadata is healthy, repair MUST refresh adapters by installing missing integrations and upgrading installed ones. Force re-initialization MUST be reserved for unusable or missing metadata after preservation.
- **FR-010**: Codex, Grok Build, Oh My Pi, and Claude Code MUST each have a native Spec Kit integration. Installing an additional safe integration MUST NOT by itself change the default integration.
- **FR-011**: The repository MUST pick one stable default Spec Kit integration as scaffolding policy. The chosen default is Oh My Pi (`omp`). That default MUST NOT be interpreted as a requirement that every task run through that harness.
- **FR-012**: Generated Spec Kit adapters MUST NOT contain unique project policy. After repair they MUST be regenerable without information loss.
- **FR-013**: Hand-copied or legacy Spec Kit command and prompt copies that are not manifest-managed MUST be removed after unique intent is migrated and native adapters work.
- **FR-014**: Claude Code MUST consume the canonical operating contract through a thin compatibility import. A full duplicate policy file MUST NOT remain at the repository root.
- **FR-015**: Grok Build sessions on this repository MUST NOT treat Claude instruction, skill, or rule copies as project policy when native Grok adapters and the canonical operating contract are present.
- **FR-016**: Oh My Pi MUST resolve the canonical operating contract as project context. A Claude project instruction file MUST NOT shadow it. Isolating Claude discovery MUST NOT disable unrelated model inference providers.
- **FR-017**: Changing harness MUST NOT cause a feature to be specified, planned, or tasked again when those artifacts already exist. Handoff MUST pass paths, commits, artifacts, expected phase, and only constraints absent from the repository.
- **FR-018**: At any moment, each canonical artifact (specification, plan, tasks, writable workspace) MUST have at most one writer. Other agents MAY inspect, review, test, or propose, but MUST NOT independently mutate the same artifact.
- **FR-019**: Parallel writable implementation MUST use separate workspaces. Multiple write-capable harnesses MUST NOT share one writable workspace.
- **FR-020**: Grok Bot MUST act as an outer-loop orchestrator only. It MUST NOT be a Spec Kit integration, MUST NOT keep Bot-local copies of policy or specifications, and MUST NOT paste Spec Kit prompts into a Bot skill.
- **FR-021**: The Bot skill MUST contain reusable orchestration procedure, pointers to canonical files, prohibitions, and a required completion report. It MUST NOT copy repository policy or feature requirements.
- **FR-022**: Agents MUST treat the repository as development memory. Conversation history MUST NOT be a competing source of feature requirements.
- **FR-023**: When intended behavior changes, agents MUST change the specification first, then reconcile plan and tasks, then implement. They MUST NOT patch tasks or code to silently redefine requirements.
- **FR-024**: Planning in this brownfield repository MUST inspect existing architecture, dependencies, tests, and relevant implementation, and MUST reuse them unless the specification explicitly requires change.
- **FR-025**: Spec Kit integration status MUST be inspectable in a machine-readable form suitable for agents and CI. After repair it MUST report a healthy multi-install of the four coding harnesses with the chosen default and no unexplained managed-file, manifest, overlap, or infrastructure errors.
- **FR-026**: Automated checks MUST fail on an actual Spec Kit integration error and MUST enforce the ownership invariants (one canonical operating contract, no full duplicate root Claude policy, thin Claude import, no unique human edits left in generated adapters, feature requirements under specifications, constitution not copied into agent files, no active leftover Spec Kit command directories).
- **FR-027**: Automated checks MUST NOT demand that generated adapters for different harnesses be identical.
- **FR-028**: Routine Spec Kit upgrades MUST investigate modified generated files. Blind overwrite MUST NOT be the default maintenance path.
- **FR-029**: This repository MUST use Spec Kit's shipped Python implementation for executable maintenance (status, install, upgrade, and related commands). It MUST NOT keep a Unix-shell-only script setting, and it MUST NOT introduce project-authored Spec Kit scripts as a substitute.
- **FR-030**: Repair is complete only when existing unique instructions are preserved, each completion criterion in this specification is true, runtime inspection confirms each harness receives the intended context, and machine-readable Spec Kit status is clean.
- **FR-031**: Harness-specific files MAY contain similar generated adapter content. They MUST NOT contain duplicated human-maintained semantics.

### Key Entities

- **Canonical operating contract**: Single repository map that points agents at owners; not a second copy of those owners.
- **Constitution**: Single owner of non-negotiable project principles.
- **Feature specification**: Single owner of a feature's behavior and requirements.
- **Feature plan**: Single owner of that feature's technical design.
- **Feature tasks**: Single owner of that feature's implementation work graph.
- **Generated adapter**: Spec Kit-produced, harness-native, disposable workflow entry point.
- **Harness runtime configuration**: Settings that exist only because a specific harness needs them.
- **Orchestrator procedure**: Reusable Bot skill that coordinates coding harnesses without owning repository truth.
- **Integration manifest**: Spec Kit record of installed adapters, hashes, and health.
- **Knowledge owner**: The one document allowed to state a given fact.
- **Workspace**: One writable tree with one implementation owner at a time.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In an audit of at least 20 distinct project facts sampled from operating rules, principles, and feature requirements, 100% have exactly one owner document and 0 are restated as policy in another agent-facing file.
- **SC-002**: Starting from a snapshot that plants unique notes in a generated adapter, repair migrates 100% of those notes to the owner document and leaves the adapter regenerable; 0 unique notes remain only in the generated copy.
- **SC-003**: After repair, 100% of the four coding harnesses expose Spec Kit through a native generated adapter, and 0 extra hand-copied Spec Kit command sets remain active.
- **SC-004**: In cold-start inspection of Claude Code, Grok Build, Oh My Pi, and Codex, 100% resolve the same canonical operating contract; Claude has 0 full duplicate policy manuals; Grok and Oh My Pi treat Claude copies as non-authoritative for this project.
- **SC-005**: On a feature that already has a specification, handing work to a second and third harness produces 0 additional specifications, plans, or task graphs for that feature.
- **SC-006**: When two write-capable agents are given overlapping work, 100% of trials keep a single writer per canonical artifact, and parallel implementation uses separate workspaces in 100% of parallel trials (at least three).
- **SC-007**: The orchestrator skill contains 0 copied constitution clauses and 0 copied feature requirements, and 100% of sampled dispatches (at least three) point at repository artifacts instead of replaying the original feature prompt.
- **SC-008**: A healthy repository passes the automated integration/ownership check; a fixture with a real integration error fails it in 100% of runs; a fixture with a forbidden duplicate policy file fails it in 100% of runs.
- **SC-009**: A maintainer who is not an internals expert can complete the post-repair verification loop (status, one inspection per coding harness, confirm no leftover command copies) in a single sitting without a second operator.
- **SC-010**: A maintainer can complete Spec Kit status and upgrade from each of at least two different supported coding harnesses using Spec Kit's own shipped maintenance scripts, with 0 project-authored replacements for those scripts and 0 remaining dependence on a shell-only Spec Kit script setting.

## Assumptions

- Target coding harnesses are Codex, Grok Build, Oh My Pi, and Claude Code (used occasionally). Grok Bot is an outer-loop orchestrator, not a fifth Spec Kit integration.
- Designated surfaces (product choices, not success metrics): canonical operating contract is the repository-root agent instruction file; Claude's thin import lives in Claude's project instruction file and points at that contract; constitution lives in Spec Kit memory; feature artifacts live under `specs/`; Codex adapters under the Codex skills location; Grok adapters under the Grok skills location; Oh My Pi adapters under the Oh My Pi commands location; Claude adapters under the Claude skills location; Bot orchestration procedure is a reusable Bot skill. Exact paths may follow current Spec Kit layouts.
- Stable default Spec Kit integration is Oh My Pi (`omp`). Other installed integrations remain installed. This is scaffolding policy, not a mandate that Oh My Pi perform every task.
- Spec Kit script mode for this repository is Spec Kit's default/shipped Python implementation (`--script py` or equivalent). That means selecting Spec Kit's own Python scripts, not writing custom Python (or other) scripts for Spec Kit. The current shell-script setting is the brownfield defect this feature removes.
- Generated adapter similarity across harnesses is not a DRY violation. DRY applies only to human-maintained semantics.
- User-level Grok Claude-compatibility isolation may be required for strict runtime isolation and cannot always be stored in the project. The requirement is the observed Grok session behavior; the user-level setting is the documented means when project config cannot govern it.
- Oh My Pi isolation prefers disabling the project Claude instruction file when that file would shadow the canonical contract. Disabling the entire Claude discovery source is only for confirmed duplicate skill/command/hook/MCP inheritance, and must preserve existing intentional isolation lists.
- Existing feature specifications, constitution, source, tests, and git history remain authoritative for their domains. This feature does not rewrite campaign content.
- Prior assumption that cross-harness instruction twins were out of scope is superseded for the harnesses named here. The replacement is one owner plus generated adapters, not parallel policy manuals.
- Force re-initialization is an escape hatch for missing or unusable integration metadata, not the normal repair path.
- Phases are not permanently assigned to a named product. Author and independent reviewer should differ when independent review is warranted.
- Trivial work may skip quality-gate phases; production work uses the full Spec Kit flow. The flow itself is owned by Spec Kit, not recopied into harness prompts.
- Brownfield reuse is required unless a specification explicitly demands architectural change.
- Automated drift checks belong in continuous integration and SHOULD fail the build on real Spec Kit integration errors and on the ownership invariants in FR-026.
- Easy, safe, idempotent formatting or index refresh that already runs unattended is not in scope for this repair.
