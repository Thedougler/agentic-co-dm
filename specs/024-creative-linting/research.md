# Research: Creative Linting

**Branch**: `024-creative-linting` | **Date**: 2026-09-17

## R1: Vale as the Static Evaluation Engine

**Decision**: Use [Vale](https://vale.sh/) (v3.13.0, already installed at `~/.local/bin/vale`) as the static evaluation engine for regex/pattern-based rules. Custom rules defined as Vale YAML styles. Python orchestration layer (`tools/creative_lint/`) handles symbolic evaluators, bundle routing, severity mapping, waivers, shadow mode, and the unified finding schema.

**Rationale**: Vale is purpose-built for prose linting with custom YAML rules. It's already installed, outputs JSON, handles markdown-aware scoping (headings, paragraphs, blockquotes, code fences), and provides extension points (existence, substitution, conditional, occurrence, script/Tengo) that cover the static rule patterns in the spec. Building a custom regex engine when a mature prose linter is on disk violates constitution XVI (Simplest Adequate Tool).

**Alternatives considered**:
- Custom Python regex engine: would duplicate what Vale does, minus markdown-awareness. More code, worse at prose-specific patterns (sentence boundaries, heading scope, code fence exclusion).
- PyYAML + custom framework: adds a dependency for something Vale handles natively.
- Remark/unified.js: wrong language ecosystem (this project is Python).

**Vale extension points for our rules**:
| Extension | Use for |
|---|---|
| `existence` | AGENCY001 (authored PC decisions), AGENCY002 (prescribed actions), KNOW002 (NPC knowledge leak) |
| `conditional` | TEMP001 (temporal marker inconsistency) |
| `occurrence` | SCENE001 (minimum situation markers per section) |
| `script` (Tengo) | Complex pattern matching beyond regex, e.g. cross-reference checks |

**What Vale doesn't cover** (stays in Python):
- Symbolic evaluators: cross-page graph traversal, frontmatter lifecycle cross-reference (CANON001, CANON002)
- Existing structural checks: `tools/lint_wiki.py` HARD keys (broken_links, missing_frontmatter, etc.)
- Bundle routing, severity mapping, waiver matching, shadow telemetry
- LLM/semantic evaluators (Phase 2+)

## R2: Integration Architecture — Three Layers

**Decision**: Compose three evaluation layers, unified at the CLI.

```
scripts/wiki-lint (CLI orchestrator)
├── tools/lint_wiki.py         — existing structural HARD checks (unchanged)
├── vale + styles/CoDM/        — static prose rules (new)
└── tools/creative_lint/       — symbolic evaluators + orchestration (new)
```

**Rationale**: Each layer does what it's best at. `lint_wiki.py` owns structural/frontmatter checks. Vale owns prose-pattern matching with markdown awareness. Python orchestration handles cross-page logic, bundle routing, and the unified finding contract. No layer replaces another.

**Integration points**:
1. `scripts/wiki-lint` gains subcommands (`task`, `rule`, `file`, `corpus`, `changed`). Existing no-subcommand mode calls `lint_wiki.py` unchanged.
2. New subcommands call the Python orchestrator, which invokes Vale (`vale --output=JSON --config=...`) and merges findings with symbolic evaluator results.
3. `scripts/wiki-maintain` (Layer A) is unchanged — A1 still calls `scripts/wiki-lint` with existing flags. Future: A1 can optionally include creative lint findings.
4. Finding schema is unified at the orchestrator layer. Vale JSON output is mapped to the canonical finding schema.

## R3: Vale Configuration Layout

**Decision**: Vale styles live at `styles/CoDM/` with `.vale.ini` at repo root.

```
.vale.ini                     # Vale config (StylesPath, scopes)
styles/
└── CoDM/                    # Custom style package
    ├── AGENCY001.yml         # Each rule = one YAML file
    ├── AGENCY002.yml
    ├── CANON_frontmatter.yml # Static canon checks Vale can handle
    ├── KNOW002.yml
    ├── SCENE001.yml
    ├── TEMP001.yml
    └── meta.json             # Vale package metadata (optional)
```

**Rationale**: Vale's convention is one rule per YAML file in a named style directory. `CoDM` (Co-DM) is the style name. This maps cleanly to the spec's stable-ID requirement — each file's name is the rule ID.

**`.vale.ini` sketch**:
```ini
StylesPath = styles
MinAlertLevel = suggestion

[wiki/*.md]
BasedOnStyles = CoDM
```

**Scope mapping**: Vale's markdown scopes handle content vs frontmatter vs headings. `scope: raw` gives the full file for rules that need frontmatter access. `scope: text` gives body text only (excludes code fences, YAML front matter). `scope: heading` targets headings only.

## R4: Rule Definition Format (Dual)

**Decision**: Two rule definition surfaces.

1. **Vale YAML** (`styles/CoDM/<ID>.yml`): The executable rule for static evaluation. Standard Vale format with extension point, message, level, scope, tokens/pattern.
2. **Rule registry** (`rules/registry.yml`): Metadata for all rules (static + symbolic + semantic). Maps each rule ID to its category, severity in the creative-lint severity model, evaluator type, lifecycle state, repair guidance, bundle memberships, and conflict/dependency declarations. This is the single source of truth for rule metadata (FR-012).

**Rationale**: Vale rules need to be valid Vale YAML (their own format). But the spec requires additional metadata Vale doesn't support (lifecycle, repair guidance, bundle membership, the five-level severity model vs. Vale's three levels). The registry bridges both — it's the canonical rule definition, and the Vale YAML is the executable evaluator for static rules.

**Severity mapping** (Vale → creative lint):
| Vale level | Creative lint severity |
|---|---|
| `error` | BLOCK or REPAIR (determined by registry) |
| `warning` | REVIEW or WARN (determined by registry) |
| `suggestion` | WARN or INFO (determined by registry) |

Vale's three levels are insufficient for the five-level model, so the registry is authoritative for severity. Vale level is set to the closest match to ensure Vale's own filtering doesn't hide findings.

## R5: Finding Output Contract

**Decision**: Single JSON schema for all findings from all evaluator types.

```json
{
  "rule_id": "AGENCY001",
  "result": "fail",
  "severity": "BLOCK",
  "location": {"file": "wiki/path/to/file.md", "line": 42, "col": 5, "text": "You decide..."},
  "evidence": "Matched pattern: 'You decide the risk is worth it'",
  "reason": "Narration authors a player-character decision",
  "repair_target": "Rewrite to describe the situation without prescribing the PC's response"
}
```

**Vale JSON mapping**: Vale's `--output=JSON` produces `{file: [{Line, Message, Check, Severity, Span, ...}]}`. The orchestrator maps: `Check` → `rule_id`, `Line` → `location.line`, `Message` → `evidence`, `Severity` → looked up in registry for creative-lint severity. `reason` and `repair_target` come from the registry.

## R6: Severity Model Implementation

**Decision**: Five levels with clear agent-action semantics.

| Level | Agent action | Correlates with |
|---|---|---|
| BLOCK | Must repair before completion | Truth, safety, agency, schema, deterministic process |
| REPAIR | Auto-repair then re-test | High-confidence defect with clear fix |
| REVIEW | Repair or justify | Probably problematic but contextual |
| WARN | Consider during revision | Creative diagnostic — no mandate |
| INFO | Observation only | Portfolio-level pattern, diversity |

**Status computation**: `repair_required` if any BLOCK or REPAIR. `review_needed` if any REVIEW and no BLOCK/REPAIR. `clean` otherwise.

**Taste guard**: Rules in categories `scene` and `diversity` have a lifecycle ceiling of WARN.

## R7: Initial Rule Set (~15 rules)

**Static (Vale)**:
| ID | Category | Ext. point | Pattern | Severity |
|---|---|---|---|---|
| AGENCY001 | agency | existence | `you (decide\|choose\|feel\|think\|believe\|realize\|know)` in body text | BLOCK |
| AGENCY002 | agency | existence | `you (must\|have to\|need to)` in narration scope | BLOCK |
| AGENCY003 | agency | existence | `you (suddenly\|involuntarily\|can't help but)` | REVIEW |
| KNOW001 | retrieval | existence | `(obviously\|everyone knows\|clearly)` in DM layers without citation | REVIEW |
| KNOW002 | retrieval | existence | NPC using meta-phrases: `(as you may recall\|the player)` | REPAIR |
| TEMP001 | temporal | conditional | Past-tense reference to future session events | REVIEW |
| SCENE001 | scene | occurrence | Min 1 situation/pressure marker per session-prep section | WARN |
| SCENE002 | scene | existence | `(something happens\|stuff occurs\|things go)` vagueness markers | WARN |

**Symbolic (Python)**:
| ID | Category | Check | Severity |
|---|---|---|---|
| CANON001 | canon | NPC with `lifecycle: rejected/dead` referenced as present | REPAIR |
| CANON002 | canon | Entity `updated` >30 days stale referenced in session-prep | REVIEW |
| WIKI001 | wiki | Missing required frontmatter (wraps lint_wiki.py finding) | BLOCK |
| WIKI002 | wiki | Invalid type/lifecycle value (wraps lint_wiki.py finding) | BLOCK |

**INFO-only (corpus-level, Phase 1 stubs)**:
| ID | Category | Check | Severity |
|---|---|---|---|
| DIVERSITY001 | diversity | Vocabulary frequency across sessions | INFO |
| RETRIEVAL001 | retrieval | Broken wikilink in content (wraps lint_wiki.py) | BLOCK |

## R8: Bundle Definitions

**Decision**: Bundles in `rules/bundles.yml`, one entry per task type.

```yaml
session-prep:
  block: [agency, canon, wiki]
  review: [retrieval, temporal]
  diagnostics: [scene, diversity]

wiki-ingest:
  block: [wiki]
  review: [canon]
  diagnostics: [retrieval]

worldbuilding:
  block: [canon, wiki]
  review: [retrieval]
  diagnostics: [scene]

live-codm:
  block: [agency]
  review: []
  diagnostics: [scene]

corpus:
  block: [wiki, canon]
  review: [retrieval, temporal, agency]
  diagnostics: [scene, diversity]
```

**Severity gate logic**: A rule's effective severity in a bundle context is: min(rule's inherent severity, the gate level its category appears at). If a category appears under `diagnostics`, its rules fire at max WARN regardless of their inherent severity.

## R9: Waiver and Shadow Mode Storage

**Decision**: JSON files under `rules/`.

- `rules/waivers.json`: Array of `{rule_id, target, reason, owner, granted, expires}`.
- `rules/shadow/`: Directory of per-rule JSON telemetry files.

Waivers are version-controlled. Shadow telemetry can be gitignored.

## R10: CLI Subcommand Design

**Decision**: Extend `scripts/wiki-lint` with subcommands.

```
wiki-lint                           # Existing (structural HARD checks)
wiki-lint --json                    # Existing (JSON output)
wiki-lint task <bundle>             # Creative lint with task bundle
wiki-lint file <path>               # All rules against a file
wiki-lint corpus                    # Corpus-level rules
wiki-lint changed                   # Changed files since last commit
wiki-lint rule <ID>                 # Describe a rule
wiki-lint --severity block,repair   # Filter by severity
wiki-lint --consolidate <vault>  # Dry-run structural repair plan

```

No-subcommand mode remains unchanged — calls `lint_wiki.py`.
### R10.1: Safe Consolidation Mode

**Decision**: Add `wiki-lint --consolidate [vault] [--json] [--approve]` as a compatibility-preserving structural-repair path. Without `--approve`, the command emits a deterministic dry-run plan and performs no writes. With `--approve`, it re-runs the finding pass, verifies that the plan still matches the current files, and then applies only safe structural repairs.

**Rationale**: The repository skill already defines a consolidation workflow, while the installed CLI currently rejects the flag. Making the behavior explicit in the same agent-shaped CLI closes that contract gap without changing the default report-only mode or granting automatic authority over canon.

**Alternatives considered**:
- Separate `wiki-maintain` command: rejected because users already discover consolidation through `wiki-lint` and a second surface would split the repair contract.
- Interactive-only approval: rejected because agents need a deterministic, non-interactive `--approve` path with preserved exit status.

## R11: Fixture Testing Approach

**Decision**: Fixtures in `tests/fixtures/creative_lint/<RULE_ID>/` as markdown files.

- `fail_*.md` — should trigger the rule
- `pass_*.md` — should not trigger
- `ambiguous_*.md` — recorded, doesn't fail suite

For Vale rules, fixtures can also be validated by running `vale --config=... <fixture>` directly. The pytest harness wraps both Vale and symbolic evaluator fixtures.

## R12: Repository Integration and Dependency Boundaries

**Decision**: Preserve the existing `scripts/wiki-lint` split: no-subcommand mode remains a subprocess facade over `tools/lint_wiki.py`; creative subcommands load the registry, bundles, waivers, and `LintEngine`, which merges Vale and symbolic findings. `scripts/wiki-maintain` keeps its existing A1 path and exposes creative lint only through its optional A7 report.

**Evidence**: `scripts/wiki-lint` defines `structural_main`, `creative_main`, and `_exit_for`; `tools/creative_lint/engine.py` invokes `run_vale` and symbolic evaluators; `scripts/wiki-maintain` calls `scripts/wiki-lint` for A1 and `task corpus` for A7. No `package.json` or npm lockfile currently exists, so FR-019 remains an implementation task rather than an existing capability.

**Decision**: Add PyYAML to Python project metadata because `tools/creative_lint/registry.py` imports `yaml` and registry/bundle loading is required at runtime. Add a private root `package.json` with a pinned `markdownlint-cli2` development dependency and thin scripts that delegate to existing repository commands; commit the generated npm lockfile for reproducibility. Do not add Node wrappers or duplicate lint logic.

**Decision**: Keep `.vale.ini` as the sole Vale package/style authority. The adapter invokes `vale --output=JSON --config=<repo>/.vale.ini`; the configured package set remains `ai-tells`, `proselint`, and `Readability`. The existing `.markdownlint-cli2.jsonc` owns structural rule configuration and excludes `_raw`, `_staging`, `_archive`, and templates.

**Alternatives considered**:
- Treating markdownlint-cli2 as an ad hoc global prerequisite: rejected because it is not reproducible and conflicts with FR-019's discoverable operations.
- Copying Vale's package list into the registry: rejected because it creates a second source of truth and violates the accepted clarification.
- Replacing `tools/lint_wiki.py` with the new engine: rejected because existing structural HARD behavior must remain compatible.

**Risks**: The legacy Markdown scripts contain project-specific checks beyond markdownlint-cli2 built-ins; porting is complete only after equivalent fixtures pass. Existing creative CLI tests do not cover every new subcommand or severity-filter/error path, so those remain explicit implementation/test tasks.

## R13: Markdownlint Version and Node Floor

**Decision**: Pin `markdownlint-cli2` to `0.23.2` in a private root `package.json`, declare `engines.node: ">=22"`, and commit the generated `package-lock.json`. This is the current official package metadata and keeps the structural lint command reproducible through the local npm binary.

**Rationale**: A global-only tool or unpinned `npx` invocation depends on workstation state. A local npm development dependency gives `npm run` direct binary resolution and preserves arguments, streams, and exit status without a wrapper. The Node floor is explicit rather than hidden in a generic “Node.js” prerequisite.

**Alternatives considered**:
- Pin an older markdownlint-cli2 release to retain an unspecified or older Node floor: deferred because the repository has no declared Node compatibility target and the current release is the simplest supported choice.
- Add JavaScript custom rules to reproduce every legacy checker: rejected for this phase because it violates the no-duplicate-implementation constraint and the legacy checks require fixture-backed migration before removal.

**Validation boundary**: markdownlint-cli2 covers configured built-in Markdown structure only. It does not automatically replace project-specific checks for Obsidian links, frontmatter semantics, forbidden trees, image existence, literal backslash-n, or narration callouts. Those legacy scripts remain until equivalent fixtures pass.
