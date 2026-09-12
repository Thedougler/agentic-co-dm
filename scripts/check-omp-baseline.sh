#!/usr/bin/env bash
# Observe the OMP + Spec Kit baseline. Cwd: repository root. No flags.
set -euo pipefail

fail() {
  echo "$1" >&2
  exit 1
}

root="$(pwd)"
passed=()

python3 - "$root" <<'PY' || fail "integration is not omp in .specify/init-options.json"
import json, sys
from pathlib import Path
p = Path(sys.argv[1]) / ".specify/init-options.json"
data = json.loads(p.read_text())
if data.get("integration") != "omp":
    raise SystemExit(1)
PY
passed+=("integration-omp")

[[ -f .omp/commands/speckit.specify.md ]] || fail "missing .omp/commands/speckit.specify.md"
[[ -f .omp/commands/speckit.converge.md ]] || fail "missing .omp/commands/speckit.converge.md"
passed+=("speckit-commands")

[[ -f .omp/AGENTS.md ]] || fail "missing .omp/AGENTS.md"
grep -q '@../AGENTS.md' .omp/AGENTS.md || fail ".omp/AGENTS.md missing @../AGENTS.md"
grep -q '<!-- SPECKIT START -->' .omp/AGENTS.md || fail ".omp/AGENTS.md missing SPECKIT START"
grep -q '<!-- SPECKIT END -->' .omp/AGENTS.md || fail ".omp/AGENTS.md missing SPECKIT END"
passed+=("live-context")

[[ -f .omp/RULES.md ]] || fail "missing .omp/RULES.md"
grep -qi 'verification' .omp/RULES.md || fail ".omp/RULES.md missing verification"
grep -qi 'generated' .omp/RULES.md || fail ".omp/RULES.md missing generated-files rule"
grep -qi 'push' .omp/RULES.md || fail ".omp/RULES.md missing push rule"
grep -qi 'deploy' .omp/RULES.md || fail ".omp/RULES.md missing deploy rule"
grep -q 'tasks.md' .omp/RULES.md || fail ".omp/RULES.md missing map-to-tasks"
passed+=("sticky-rules")

[[ -f .omp/config.yml ]] || fail "missing .omp/config.yml"
grep -q 'maxConcurrency: 4' .omp/config.yml || fail ".omp/config.yml maxConcurrency is not 4"
grep -q 'maxRecursionDepth: 1' .omp/config.yml || fail ".omp/config.yml maxRecursionDepth is not 1"
grep -A1 '^advisor:' .omp/config.yml | grep -q 'enabled: false' || fail ".omp/config.yml advisor not disabled"
grep -A1 '^memory:' .omp/config.yml | grep -q 'backend: off' || fail ".omp/config.yml memory not off"
grep -A1 '^autolearn:' .omp/config.yml | grep -q 'enabled: false' || fail ".omp/config.yml autolearn not off"
passed+=("config-caps")

for name in spec-auditor implementer verifier; do
  f=".omp/agents/${name}.md"
  [[ -f "$f" ]] || fail "missing $f"
  grep -Fq 'spawns: []' "$f" || fail "$f missing spawns: []"
done
passed+=("specialists")

for phase in specify clarify plan checklist tasks analyze implement converge; do
  if [[ -f ".omp/agents/${phase}.md" ]]; then
    fail "phase-named agent under .omp/agents/"
  fi
done
passed+=("no-phase-agents")

[[ -f .omp/commands/feature-fast.md ]] || fail "missing .omp/commands/feature-fast.md"
passed+=("feature-fast")

if [[ -f CLAUDE.md ]] && grep -q '<!-- SPECKIT START -->' CLAUDE.md; then
  fail "CLAUDE.md has a Spec Kit twin block"
fi
passed+=("no-client-twin")

echo "omp-speckit-baseline: pass (${passed[*]})"
exit 0
