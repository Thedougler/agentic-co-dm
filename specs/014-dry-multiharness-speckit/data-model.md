# Data Model: DRY Multi-Harness Spec Kit

## KnowledgeOwner

A human-maintained fact has exactly one owner document.

| Owner | Owns | Must not own |
|---|---|---|
| `AGENTS.md` | Operating map, pointers, rules needed on nearly every task | Constitution text, feature requirements, generated adapter bodies |
| `.specify/memory/constitution.md` | Non-negotiable principles | Feature requirements, harness runtime |
| `specs/<feature>/spec.md` | Feature behavior | Implementation task graph |
| `specs/<feature>/plan.md` | Technical design | Feature requirements |
| `specs/<feature>/tasks.md` | Implementation work graph | Silent requirement changes |
| Canonical docs (`docs/`, `CONTEXT.md` when present) | Architecture / domain | Harness adapter text |
| Source + tests | Executable truth | Policy copies |
| Harness runtime files | Permissions, discovery isolation, model roles | Project policy, specs |
| `docs/agents/harness-dispatch.md` | Orchestration procedure | Policy, specs, Spec Kit prompts |
| Spec Kit generated adapters | Harness invocation of Spec Kit phases | Unique project rules |

**Validation**: A fact restated as policy in a non-owner file is a defect. A reference/pointer is allowed.

## GeneratedAdapter

Spec Kit-managed, disposable, harness-native entry point.

| Field | Rule |
|---|---|
| Location | Codex `.agents/skills/speckit-*`; Grok `.grok/skills/speckit-*`; OMP `.omp/commands/speckit.*`; Claude `.claude/skills/speckit-*` |
| Manifest | Tracked in `.specify/integrations/*.manifest.json` |
| Hash | Spec Kit owned; modified = investigate, migrate unique text, regenerate |
| Similarity across harnesses | Allowed |
| Human edits | Forbidden after unique intent is migrated |

**State**: `missing` | `unmodified` | `modified` | `legacy-unmanaged`

Legacy unmanaged copies that are not in the manifest are removed after migration.

## IntegrationRecord

From `.specify/integration.json` + `specify integration status --json`.

| Field | Healthy value after repair |
|---|---|
| `status` | `ok` |
| `default_integration` | `codex` |
| `installed_integrations` | `codex`, `grok`, `omp`, `claude` (order irrelevant) |
| script flavor | Spec Kit shipped Python (`py`) for each installed integration |
| `missing_managed_files` | `0` unexplained |
| `modified_managed_files` | `0` unexplained |
| `invalid_manifest_paths` | `0` |
| `findings` | empty or only explained items |

**Transitions**:

```text
omp-only + script sh
  → install missing (codex, grok, claude) --script py
  → upgrade omp --script py
  → register extensions per integration
  → use codex (default)
  → status ok
```

Force-init is not a transition unless the record is unusable.

## InstructionShim

Thin file that imports the canonical contract.

| Shim | Content |
|---|---|
| `.claude/CLAUDE.md` | `@../AGENTS.md` plus Claude-only stub |
| `.omp/AGENTS.md` | `@../AGENTS.md` only |

**Validation**: Shim body does not restate wiki routing, constitution, or feature requirements. Root `CLAUDE.md` does not exist.

## LiveContextBlock

Spec Kit `agent-context` injection between `<!-- SPECKIT START -->` and `<!-- SPECKIT END -->`.

| Field | Rule |
|---|---|
| File | `AGENTS.md` only (`context_file: AGENTS.md`) |
| Content | Pointer to current feature plan; not a spec copy |
| Duplicates | Must not also appear in `.omp/AGENTS.md` or Claude shim |

## DispatcherProcedure

`docs/agents/harness-dispatch.md`

Required sections: purpose, procedure (read AGENTS.md, git state, Spec Kit artifacts, phase, pick harness, hand off paths/phase/extra constraints), canonical file list, prohibitions, return report.

**Validation**: Zero constitution clauses copied. Zero feature requirements copied. No Spec Kit prompt bodies.

## DriftCheck

`scripts/check-speckit-dry.sh` + CI.

Observes IntegrationRecord + InstructionShim + KnowledgeOwner invariants. Exit 1 on failure. Does not compare generated adapter bytes.
