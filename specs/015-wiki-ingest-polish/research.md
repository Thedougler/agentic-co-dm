# Research: Wiki Ingest Polish

## Decision: Keep `wiki-ingest` as the single workflow owner

**Rationale**: The existing skill already classifies append, full, raw, preserve, and combatant-drop modes; requires sequential file closure; and defines the trust boundary. Adding another workflow would duplicate routing and tracking rules.

**Alternatives considered**: A separate polish skill or a new ingest compiler. Rejected because they would split ownership and create competing completion rules.

## Decision: Treat inputs as evidence and compile into existing pages

**Rationale**: `llm-wiki` defines raw sources as immutable and the Wiki as the compiled, interconnected layer. `wiki-ingest` already requires distillation, deduplication, provenance, and manifest page destinations.

**Alternatives considered**: Copying source files into category pages. Rejected because it produces unfinished duplicates and weakens the Wiki as source of truth.

## Decision: Reuse craft-skill authorities for quality

**Rationale**: `copy-writer` owns DM-facing prose and signal density; `obsidian-markdown` owns frontmatter, links, callouts, and scan grammar; `theatre-of-the-mind` owns player-safe spoken language; `dnd5e-mechanics` owns uncertain tests, DCs, and consequences. Ingestion should invoke these authorities according to the destination surface rather than restate them.

**Alternatives considered**: A single ingest-specific style checklist containing all rules. Rejected because duplicated guidance drifts and violates token-efficiency principles.

## Decision: Preserve ambiguity and canon authority explicitly

**Rationale**: Existing guidance marks synthesized claims `^[inferred]`, unclear or conflicting claims `^[ambiguous]`, and requires canon proposals and DM acceptance. Ingestion must polish wording without silently converting uncertainty into fact.

**Alternatives considered**: Prefer the newest source automatically. Rejected because source recency does not establish campaign canon.

## Decision: Retain sequential processing and existing tracking

**Rationale**: The current workflow closes one file before opening the next, updates the manifest only after completion, and maintains index/log/hot surfaces. This prevents cross-file attribution errors and duplicate processing.

**Alternatives considered**: Parallel file ingestion for speed. Rejected because pages may overlap and the current workflow explicitly protects ordering and attribution.

## Decision: Validate with observable fixtures, not text snapshots

**Rationale**: Constitution IV requires tests at public seams. Fixtures can verify destination routing, preservation, conflict handling, audience separation, metadata, and tracking without pinning a particular creative outline.

**Alternatives considered**: Grep-based checks for prescribed phrases. Rejected because they test implementation wording rather than user-visible outcomes.
