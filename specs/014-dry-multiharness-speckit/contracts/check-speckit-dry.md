# Contract: `scripts/check-speckit-dry.sh`

Agent-shaped. Cwd: repository root. No flags.

## Input

None.

## Output

- stdout: one line `speckit-dry: pass (...)` or failures on stderr
- exit `0` pass, `1` fail

## Observes

1. `specify integration status --json` per [specify-status.md](./specify-status.md)
2. `.specify/init-options.json` / integration settings use Spec Kit script `py`, not `sh`
3. Root `AGENTS.md` exists
4. Root `CLAUDE.md` is absent
5. `.claude/CLAUDE.md` contains `@../AGENTS.md` and does not contain the wiki routing heading copied from `AGENTS.md`
6. `.omp/AGENTS.md` contains `@../AGENTS.md` and does not contain `<!-- SPECKIT START -->`
7. `AGENTS.md` is the only project file with `<!-- SPECKIT START -->` among `{AGENTS.md,.omp/AGENTS.md,.claude/CLAUDE.md}`
8. Native adapters exist: at least one `.agents/skills/speckit-*/SKILL.md`, `.grok/skills/speckit-*/SKILL.md`, `.omp/commands/speckit.specify.md`, `.claude/skills/speckit-*/SKILL.md`
9. `docs/agents/harness-dispatch.md` exists and does not contain a copied constitution heading (`# Agentic Co-DM Constitution`)
10. No project file under `.specify/scripts/` that is not Spec Kit-shipped (do not add repo-authored Spec Kit scripts)

## Does not observe

- Adapter body equality
- User-level `~/.grok/config.toml` (document in quickstart; missing CLI is skip with a note, not a silent pass of Grok session isolation)

## 005 coexistence

`scripts/check-omp-baseline.sh` must not require `default_integration == omp` after this feature. It may still require `.omp/commands/speckit.specify.md` and OMP specialists.
