# Research: DRY Multi-Harness Spec Kit

## Repair in place

**Decision**: Do not `specify init --force`. Upgrade/install integrations against current manifests.

**Rationale**: `specify integration status --json` is `ok`. Metadata exists (`installed_integrations: [omp]`, schema 1). Spec Kit 1.0.6. Zero missing/modified managed files. FR-007/009.

**Alternatives considered**: Force re-init — forbidden as first step; only if metadata is unusable.

## Default integration and script flavor

**Decision**: Keep OMP as the default integration. Install `codex`, `grok`, and `claude` with Spec Kit's shipped Python implementation (`--script py`). Upgrade OMP to `--script py`. Then `specify integration use omp` last so the default stays `omp`. Do not write project Spec Kit scripts.

**Rationale**: `init-options.json` and `integration.json` already use `default_integration: omp`. Spec FR-011/029. Codex/Grok/Claude are multi-install safe. Python is Spec Kit's own script pack, not a repo-authored replacement. Switching the default to Codex would contradict the chosen scaffolding policy.

**Alternatives considered**: Switch default to Codex — rejected; Oh My Pi remains the stable default. Custom Python wrappers around `specify` — FR-029 forbids. Switching default before other integrations exist — `use` needs them installed.

## Canonical operating contract

**Decision**: Root `AGENTS.md` is the single operating map. Add a short Sources of Truth / Workflow / Validation section that points at constitution, `specs/`, docs, and commands. Do not copy constitution or feature requirements into it. Keep existing wiki/skill routing; that is this repo's operating map, not a second constitution.

**Rationale**: Codex and Grok read root `AGENTS.md`. Constitution IX: do not duplicate. Spec FR-002.

**Alternatives considered**: Move all instruction into `.omp/AGENTS.md` — 005 did that for OMP-first; this spec supersedes it for cross-harness. Empty `AGENTS.md` plus many nested files — loses the map.

## Claude shim

**Decision**: Root `CLAUDE.md` is byte-identical to root `AGENTS.md` (`cmp` exit 0). Delete it after adding `.claude/CLAUDE.md` containing `@../AGENTS.md` plus a Claude-only stub. No second policy body.

**Rationale**: FR-014. Unique intent in `CLAUDE.md` is none.

**Alternatives considered**: Keep root `CLAUDE.md` as import — Claude relative imports resolve from the importing file; playbook requires `.claude/CLAUDE.md` → `../AGENTS.md`.

## OMP context

**Decision**: Keep `.omp/AGENTS.md` as `@../AGENTS.md` only (OMP native file shadows root at the same tree). Remove the duplicate Spec Kit live-context block from `.omp/AGENTS.md`. Point `agent-context` `context_file` at `AGENTS.md`. Preserve `.omp/RULES.md`, `.omp/config.yml` caps, specialists, and `/feature-fast`. Add `disabledExtensions: [context-file:project:CLAUDE.md]` without dropping other keys. Do not set `disabledProviders: [claude]` unless inspection shows duplicate Claude skills/commands. Do not disable `anthropic`.

**Rationale**: OMP discovers Claude project files. Root `CLAUDE.md` would shadow the canonical contract. Array settings replace rather than merge — preserve existing config. 005 baseline stays except default-integration assertion.

**Alternatives considered**: Delete `.omp/AGENTS.md` — OMP would read root `AGENTS.md`, but 005 and current agent-context assume the native file. Disable entire `claude` provider — over-kills Foundry/skills discovery.

## Grok isolation

**Decision**: Install native `.grok/skills/speckit-*`. Document user-level `~/.grok/config.toml` `[compat.claude] agents/skills/rules = false` in `docs/agents/harness-dispatch.md`. Do not pretend a project `.grok/config.toml` `[compat.claude]` governs the harness. Verify with `grok inspect` when the CLI is present; if absent, record as a runtime check in quickstart, not a fake pass.

**Rationale**: Playbook: Claude compat is user-level. Grok also sees `.agents/skills`; keep native Grok adapters anyway.

**Alternatives considered**: Skip Grok integration because Codex skills are visible — FR-010 requires native Grok adapters.

## Codex adapters

**Decision**: `specify integration install codex --script py` → `.agents/skills/speckit-*`. Do not hand-edit those files. There are currently zero `speckit*` skills under `.agents/skills`.

**Rationale**: FR-010/012. Manifest-managed.

## Grok Bot dispatcher

**Decision**: One in-repo procedure: `docs/agents/harness-dispatch.md`. Procedure, pointers, prohibitions, return report. Not a Spec Kit integration. Not copied constitution/specs. Grok Bot loads that file (or a skill whose body is that file). No `.grok-bot/speckit/`.

**Rationale**: FR-020/021. Repo is the owner so Bot-local copies are unnecessary.

**Alternatives considered**: Paste Spec Kit prompts into a Bot skill — forbidden. Bot-only skill outside the repo — not reviewable in git.

## 005 check script

**Decision**: Add `scripts/check-speckit-dry.sh` (same shape as `scripts/check-omp-baseline.sh`: cwd root, exit 0/1, stdout status). Relax `check-omp-baseline.sh` so it no longer requires `integration == omp` or forbids a Claude file that is a thin import. Keep OMP command/specialist/rules checks.

**Rationale**: Two scripts, two seams. The DRY check owns `default_integration == omp`. The 005 script owns OMP adapters, specialists, and caps.

**Alternatives considered**: One combined script — mixes 005 and 014. Pytest — bulk suite, constitution IV.

## CI

**Decision**: Add `.github/workflows/speckit-dry.yml` that runs `specify integration status --json` and `scripts/check-speckit-dry.sh`. Fail on `status != ok`, unexplained missing/modified managed files, or check-script exit 1. Do not byte-compare generated adapters.

**Rationale**: No workflow files exist today (only `.github/copilot-instructions.md`). FR-026.

**Alternatives considered**: Check script only — FR-026 wants automation that fails closed. Compare harness adapters to each other — FR-027 forbids.

## Out of scope this feature

**Decision**: Do not rewrite `.github/copilot-instructions.md` (Copilot is not a target harness). Do not rewrite campaign wiki content. Do not assign phases to named products. Do not edit generated `speckit.*` / `speckit-*` after install.

**Rationale**: Scope lock. Copilot twin is a known leftover for a later pass.
