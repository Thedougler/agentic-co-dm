# Feature Specification: Agent-Safe Wiki Operations

**Feature Branch**: `025-agent-safe-wiki-ops`

**Created**: 2026-09-17

**Status**: Draft

**Input**: User description: "Make Lint, Repair, and Consolidation Agent-Safe — eliminate systemic causes in errors.md so agents can lint, repair, and consolidate wiki content without guessing identity, authority, scope, structure, mutation syntax, or maintenance order."

## Clarifications

### Session 2026-09-17

- Q: Should errors e-24 through e-38 (Khlysty lint session) be included in SC-007's regression scope? → A: Fold novel Khlysty sub-patterns into existing stories; update SC-007 ID list to include e-24–e-38. No new user stories for patterns that are instances of existing ones.
- Q: When scoped lint finds a link to a page outside the scope, should it silently skip, report info notices, or emit a summary? → A: Silent skip. Cross-scope links produce no output during scoped runs.
- Q: Should template contracts flag deprecated patterns in the template source, in downstream pages, or both? → A: Both — template/skill source flagged as critical error (root cause), downstream pages containing inherited deprecated output flagged as error (symptom).
- Q: When a merge creates a redirect stub, what triggers its removal? → A: No redirect stubs. Merges update the canonical page or do not write. Zero redirect files in the vault.
- Q: Should identity resolution use quantitative content overlap (embeddings/cosine) or only discrete signals? → A: Full content similarity via QMD alongside discrete signals. QMD is already installed and used elsewhere — not a new dependency.
- (User correction) Broken image/embed links (e.g., `![[fisks-fleet-banner]]` referencing a nonexistent asset) and pre-existing redirect stubs (e.g., `fisks-captains.md` with `redirects_to` frontmatter) are live vault errors the linter must detect so agents can fix them.

## User Scenarios & Testing

### User Story 1 - Scoped Faction Lint and Consolidation (Priority: P1)

An agent receives "Lint and consolidate this faction, applying the safe fixes." The repository's tooling resolves entity identity (detecting duplicates like fisks-captains.md vs fisks-fleet.md), scopes the lint to that faction's pages only, produces a compact machine-readable report grouped by file, and offers deterministic repair actions the agent can preview and apply atomically — without composing line-number patches, regex-editing the index, or refreshing QMD after each write.

**Why this priority**: This is the acceptance test stated in the intent. Every open error (e-12 through e-23) was recorded during exactly this workflow. Solving it end-to-end proves the four-layer architecture works.

**Independent Test**: Run the scoped lint-and-consolidate workflow against a faction with a known duplicate page. Verify identity resolution surfaces the ambiguity, deterministic repairs apply atomically, the index and manifest update via typed operations, and QMD refreshes once at the end.

**Acceptance Scenarios**:

1. **Given** two wiki pages cover the same faction entity with different titles, **When** identity resolution runs, **Then** it returns `ambiguous` with both candidates and blocks automatic mutation until the user designates the canonical page.
2. **Given** a scoped lint targets one faction directory, **When** the lint runs, **Then** it inspects only files matching that scope and returns compact counts plus page-grouped findings — not 726-page full-vault output.
3. **Given** a lint finding has a deterministic repair action, **When** the agent requests a dry-run plan, **Then** the system returns typed mutation operations (not prose instructions) that the agent can preview and then apply atomically.
4. **Given** a scoped lint targets one faction, **When** a wikilink points to a page outside that scope, **Then** the link is assumed valid and produces no finding — cross-scope links are not validated during scoped runs.
5. **Given** a consolidation merges two faction pages, **When** the merge completes, **Then** the canonical page, index entry, manifest identity, and backlinks update in one logical operation — the obsolete page is removed, no redirect stub is created, no manual regex editing.
6. **Given** a multi-file repair transaction completes, **When** finalization runs, **Then** QMD, index, and manifest refresh exactly once (not after each intermediate write).
7. **Given** a page contains an embed link (`![[name]]`) referencing a nonexistent asset, **When** scoped lint runs, **Then** it produces an error finding for the broken embed.

---

### User Story 2 - Template Conformance Without False Mandates (Priority: P1)

An agent lints a faction page against the faction template. The system distinguishes required sections from optional sections using explicit machine-readable semantics — not incidental template comments. A dormant faction is not flagged for missing active-faction structures. A page that omits an optional section produces no finding.

**Why this priority**: e-13 and e-14 are the highest-volume error class (579 scaffold-drift findings across 31 pages from treating optional headings as mandatory). Fixing this is prerequisite to any useful lint output.

**Independent Test**: Lint a faction page that omits optional sections and has a non-active lifecycle. Verify zero false-mandatory findings and that only genuinely missing required sections produce errors.

**Acceptance Scenarios**:

1. **Given** a faction template marks a section as optional, **When** a page omits that section, **Then** no finding is produced.
2. **Given** a faction page has `lifecycle: dormant`, **When** template conformance runs, **Then** active-only sections (e.g., Active Agenda, Current Operations) are not required.
3. **Given** a template contract specifies allowed callout types for factions, **When** a page uses a disallowed callout, **Then** exactly one finding is produced citing the contract violation.
4. **Given** a template or skill teaches a deprecated pattern (e.g., faction clocks), **When** template conformance runs, **Then** a critical-error finding flags the deprecated guidance at its authoritative source (template or skill), and an error-level finding flags each downstream page that already contains the inherited deprecated output.
5. **Given** a page has `redirects_to` frontmatter (legacy redirect stub), **When** lint runs, **Then** it produces an error finding — the vault policy is zero redirect stubs, and the finding includes a deterministic repair action to delete the stub file and rewrite any inbound links to the canonical target. The `redirects_to` frontmatter key is deprecated and MUST NOT be used by new tooling.

---

### User Story 3 - Creative Lint With Applicability Awareness (Priority: P2)

Creative heuristic rules (like SCENE001 for scene pressure) evaluate only applicable document surfaces — playable narrative sections of entity types where scene pressure is meaningful. Redirects, metadata blocks, template scaffold, tables, labels, and historical summaries are structurally excluded. Rules with uncertain precision remain in SHADOW or WARN severity.

**Why this priority**: e-15 demonstrated false positives on redirect stubs and on pages with explicit pressure. Without applicability, creative lint noise drowns actionable findings.

**Independent Test**: Run SCENE001 against a redirect stub and against a faction page with explicit pressure in its narrative sections. Verify the redirect produces no finding and the pressured page produces no finding.

**Acceptance Scenarios**:

1. **Given** a redirect stub page, **When** SCENE001 evaluates it, **Then** no finding is produced (structural exemption).
2. **Given** a faction page with clear pressure, agenda, and player openings in narrative sections, **When** SCENE001 evaluates it, **Then** no false-positive finding is produced.
3. **Given** a creative rule has no positive fixture demonstrating acceptable precision, **When** the rule is loaded, **Then** it runs at SHADOW or WARN severity, not ERROR.
4. **Given** a page in a transient state (e.g., mid-transaction before finalization), **When** deterministic structural lint runs, **Then** it does not classify the transient page as an orphan or index omission.

---

### User Story 4 - Typed Mutation Operations (Priority: P1)

An agent applies a wiki repair using typed semantic operations (replace_section, set_frontmatter, rename_or_merge_page, etc.) instead of composing line-number patches, CUT/hunk grammar, or regex substitutions. The mutation layer reads the current file, verifies preconditions, resolves all operations, and writes atomically — or fails cleanly with the original untouched.

**Why this priority**: e-21 and e-23 are direct consequences of agents composing low-level patch grammar. This is the most reusable layer — every other story depends on it.

**Independent Test**: Issue a replace_section mutation targeting a heading path with an expected content hash. Verify the section replaces atomically. Then issue the same mutation with a stale hash and verify it fails without writing.

**Acceptance Scenarios**:

1. **Given** a mutation targets a section by heading path, **When** the section exists and the content hash matches, **Then** the replacement applies atomically and the diff is emitted.
2. **Given** a mutation targets a section by heading path, **When** the content hash does not match (stale), **Then** the mutation is rejected, the file is untouched, and the error names the mismatch.
3. **Given** two mutations in the same transaction target overlapping ranges, **When** the transaction is resolved, **Then** it is rejected before any write occurs.
4. **Given** a rename_or_merge_page mutation, **When** it executes, **Then** the canonical page, index entry, manifest identity, and deterministic backlinks all update in one atomic operation — the obsolete page is removed, no redirect stub is created.

---

### User Story 5 - Index and Manifest as Structured State (Priority: P2)

Agents update wiki/index.md and .manifest.json through dedicated typed operations (replace_index_entry, update_manifest_identity) rather than regex-editing a 107KB single-line document or manually substituting canonical paths in provenance records.

**Why this priority**: e-16 and e-17 showed that manual index/manifest editing is error-prone and causes partial corruption. The mutation layer (Story 4) must include these structured-state operations.

**Independent Test**: Merge two pages using the rename_or_merge_page operation. Verify the index entry updates to the canonical path and the manifest records a merged_into identity transition — without the agent parsing index.md directly.

**Acceptance Scenarios**:

1. **Given** a page merge, **When** the index update operation runs, **Then** the old entry is replaced with the canonical entry atomically — no regex on the raw 107KB file.
2. **Given** a page merge, **When** the manifest update operation runs, **Then** a page-level identity transition (merged_into or equivalent) is recorded independently of source-ingest provenance.

---

### User Story 6 - Batched Finalization at Transaction Boundaries (Priority: P2)

A multi-file repair transaction defers QMD refresh, index rebuild, and other derived maintenance until the entire mutation set completes and validates. No intermediate refreshes occur unless a subsequent mutation requires the refreshed state.

**Why this priority**: e-19 showed repeated three-collection QMD reindex passes during one merge. Batched finalization is a direct efficiency requirement.

**Independent Test**: Execute a three-file consolidation. Count QMD refresh invocations. Verify exactly one refresh at the end, not three.

**Acceptance Scenarios**:

1. **Given** a transaction mutates three files, **When** finalization runs, **Then** QMD refresh, index update, and manifest update each execute once after the mutation set completes.
2. **Given** finalization completes, **When** the agent reads the summary, **Then** the output is compact: files changed, findings resolved, embedding backlog count — not verbose reindex logs.

---

### User Story 7 - Identity Resolution Before Work Ordering (Priority: P1)

Before any repair or consolidation queue orders work by filename or file size, a reusable identity-resolution step runs. It uses canonical path, title, aliases, wikilinks, manifest provenance, type/kind, merge history, and QMD-backed content similarity to classify each candidate as `resolved`, `ambiguous`, or `distinct`. Ambiguous results block automatic mutation and report candidates for human decision.

**Why this priority**: e-12 is the root cause of the Fisk's Fleet incident — the agent selected the wrong page because it ordered by file size before resolving identity. This must precede all other operations.

**Independent Test**: Present two files with different titles but overlapping content about the same entity. Verify identity resolution returns `ambiguous` with both candidates.

**Acceptance Scenarios**:

1. **Given** two pages with different filenames but the same canonical entity, **When** identity resolution runs, **Then** it returns `ambiguous` with both candidates listed.
2. **Given** an unambiguous page with no duplicates, **When** identity resolution runs, **Then** it returns `resolved` with the canonical path.
3. **Given** an ambiguous result, **When** the agent attempts to queue a repair, **Then** the queue rejects the item until identity is resolved.

---

### User Story 8 - Policy Single-Ownership (Priority: P2)

Policy rules (like acceptance semantics, callout vocabulary, template optionality) have exactly one authoritative owner. Lower-level skills reference the owner rather than restating the rule. When a policy conflict is detected, the system surfaces it rather than silently applying the wrong authority.

**Why this priority**: e-20 showed contradictory acceptance semantics between docs/agents/work.md and faction-design. Duplicate policy causes agent confusion at the point of action.

**Independent Test**: Introduce a test policy statement in a lower-level skill that contradicts its higher-level owner. Verify a policy-conflict check surfaces the contradiction.

**Acceptance Scenarios**:

1. **Given** faction-design references docs/agents/work.md for acceptance semantics, **When** an agent checks whether an explicit user repair instruction satisfies the acceptance gate, **Then** the answer is unambiguous from the single authority.
2. **Given** a lower-level skill restates a higher-level policy with a semantic difference, **When** a policy-conflict test runs, **Then** it reports the conflict with both locations.

---

### Edge Cases

- What happens when a page has no frontmatter at all (e.g., a raw drop in _raw/)? Identity resolution should classify it as `distinct` (unprocessed source), not error.
- What happens when a merge target page is currently being written by another process? The mutation layer's snapshot precondition fails and the operation is rejected cleanly.
- What happens when a template contract changes between lint runs? Template conformance uses the current contract version; stale findings from an old contract are not carried forward.
- What happens when a creative rule has zero fixtures? It must remain in SHADOW severity and cannot produce ERROR or WARN findings.
- What happens when the index file is malformed? The index mutation API should detect and report the malformation rather than silently appending.

## Requirements

### Functional Requirements

- **FR-001**: System MUST provide an identity-resolution layer that classifies wiki pages as `resolved`, `ambiguous`, or `distinct` using canonical path, title, aliases, manifest provenance, type/kind, merge history, and QMD-backed content similarity.
- **FR-002**: System MUST block automatic mutation on `ambiguous` identity results and report candidates.
- **FR-003**: System MUST accept a first-class scope object (files, directory, entity type, resolved identity set, changed files, task bundle) for lint, repair, plan, and verification operations.
- **FR-004**: Scoped operations MUST inspect only in-scope files and return compact machine output: scope, files checked, counts by severity/rule, findings grouped by file.
- **FR-005**: Template contracts MUST represent section semantics explicitly (required, optional, repeatable, conditional) with machine-readable schema — not derived solely from template comments.
- **FR-006**: Template conformance MUST respect lifecycle-based applicability: non-active entities MUST NOT be flagged for missing active-only sections.
- **FR-007**: Creative lint rules MUST declare document applicability, structural scope, and explicit exemptions. Rules without positive fixtures MUST remain at SHADOW or WARN severity.
- **FR-008**: System MUST provide typed semantic mutation operations (replace_section, delete_section, insert_section, set_frontmatter, remove_frontmatter, rename_or_merge_page, replace_index_entry, update_manifest_identity, rewrite_links) using semantic anchors (heading path, field name, canonical identity, content hash).
- **FR-009**: Mutation operations MUST read current state, verify preconditions, resolve all operations before writing, reject overlapping or conflicting operations, build the complete result, validate invariants, and write atomically — failing cleanly with the original untouched on any error.
- **FR-010**: rename_or_merge_page MUST atomically update canonical page, index entry, manifest identity transition (merged_into), and deterministic backlinks. No redirect stub is created — the obsolete page is removed and all inbound links rewrite to the canonical path.
- **FR-011**: Lint findings MUST declare their repair class: diagnostic-only, human-repair, or deterministic-repair-with-typed-action. Deterministic repairs MUST produce typed mutation actions, not prose instructions.
- **FR-012**: A dry-run plan MUST be constructable from deterministic repair actions before any mutation is applied.
- **FR-013**: Multi-file transactions MUST defer derived maintenance (QMD refresh, index rebuild, manifest update) until the complete mutation set validates. Intermediate refreshes occur only when a subsequent mutation requires the refreshed state.
- **FR-014**: Finalization output MUST be compact: files changed, findings resolved, embedding backlog count.
- **FR-015**: Policy rules MUST have exactly one authoritative owner. Lower-level skills MUST reference the owner, not restate the rule.
- **FR-018**: Lint MUST detect broken embed and image links (`![[name]]` referencing a nonexistent asset) as errors, not only broken wikilinks.
- **FR-019**: Lint MUST detect pre-existing redirect stubs (pages with the legacy `redirects_to` frontmatter key) as errors requiring deletion. The `redirects_to` key is deprecated — new tooling MUST NOT create pages using it or recognize it as a valid routing mechanism.
- **FR-016**: Repeated agent operations MUST have one canonical command surface with consistent arguments, --help, JSON mode, explicit exit meanings, and actionable error messages. Commands MUST self-discover repository and vault paths from the environment (config resolution, git root, vault AGENTS.md) rather than requiring the agent to supply infrastructure paths.
- **FR-017**: Template conformance findings MUST distinguish root-cause severity (deprecated pattern in the template/skill source = critical error) from symptom severity (inherited deprecated output in a downstream page = error).

### Key Entities

- **Page Identity**: Canonical path, title, aliases, merge history, type/kind — the resolved identity of a wiki page.
- **Scope Object**: A typed specification of which files/directories/entity types a lint or repair operation targets.
- **Template Contract**: Machine-readable schema defining required/optional/conditional sections, allowed callouts, frontmatter requirements, and lifecycle-based applicability for a wiki page type.
- **Mutation Operation**: A typed semantic edit (replace_section, set_frontmatter, rename_or_merge_page, etc.) with precondition, selector, and atomic application semantics.
- **Lint Finding**: A diagnostic result declaring its rule, severity, repair class, and (for deterministic repairs) a typed action factory.
- **Repair Plan**: An ordered set of typed mutation operations constructed from deterministic lint findings, previewable as a dry run before application.
- **Transaction**: A bounded set of mutations that apply atomically, deferring derived maintenance to a single finalization pass.

## Success Criteria

### Measurable Outcomes

- **SC-001**: An agent given "Lint and consolidate this faction, applying the safe fixes" completes the operation using only repository-provided commands and typed operations — no line-number patches, CUT/hunk grammar, regex index edits, or manual manifest rewrites.
- **SC-002**: Scoped faction lint returns findings for in-scope files only, with compact machine output that an agent can parse in under 1000 tokens of context.
- **SC-003**: Template conformance produces zero false-mandatory findings on pages that omit optional sections or have non-active lifecycle states.
- **SC-004**: Creative lint rules with positive/negative fixtures produce zero false positives on their fixture set.
- **SC-005**: A two-page faction merge (canonical + removal of obsolete page + index + manifest + backlinks) completes as one logical operation without intermediate QMD refreshes and without creating a redirect stub.
- **SC-006**: Two agents starting from the same repository state produce the same deterministic repair plan for the same scoped lint (before any judgment-only decisions).
- **SC-007**: Every open error in errors.md (e-10, e-12 through e-38) has a causal regression test that fails before the fix and passes after. Errors e-24 through e-38 fold into existing stories as instances of already-identified systemic patterns.

## Assumptions

- The existing wiki-lint infrastructure (Python scripts, finding schema) is extended rather than replaced. The new layers compose around existing tools.
- The mutation layer is implemented as Python CLI commands consistent with the existing scripts/ directory pattern (agent-shaped: args in, JSON/text out, exit status).
- Template contracts are expressed as YAML or JSON schema files co-located with templates, not as changes to the markdown templates themselves.
- Identity resolution uses signals already present in the repository (frontmatter, filenames, manifest, wikilinks) plus QMD content similarity for overlap detection. QMD is an existing dependency, not a new addition. No redirect stubs exist in the vault; merge history is tracked in the manifest.
- QMD refresh is the most expensive derived-maintenance step and is the primary target for batched finalization.
- The mutation layer does not need to handle concurrent writers across different processes — bounded concurrency (Constitution XIV) means at most one writer per artifact.
