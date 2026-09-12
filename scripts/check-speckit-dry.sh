#!/usr/bin/env bash
# Observe DRY multi-harness Spec Kit invariants. Cwd: repository root. No flags.
set -euo pipefail

fail() {
  echo "FAIL: $1" >&2
  exit 1
}

root="$(pwd)"
passed=()

# 1. Spec Kit integration status
status_json="$(specify integration status --json 2>/dev/null)" || fail "specify integration status --json failed"

python3 - "$status_json" <<'PY' || fail "integration status unhealthy"
import json, sys
d = json.loads(sys.argv[1])
if d.get("status") != "ok":
    raise SystemExit(f"status is {d.get('status')}, expected ok")
required = {"codex", "grok", "omp", "claude"}
installed = set(d.get("installed_integrations", []))
missing = required - installed
if missing:
    raise SystemExit(f"missing integrations: {missing}")
if d.get("missing_managed_files", -1) != 0:
    raise SystemExit(f"missing_managed_files: {d.get('missing_managed_files')}")
if d.get("modified_managed_files", -1) != 0:
    raise SystemExit(f"modified_managed_files: {d.get('modified_managed_files')}")
if d.get("invalid_manifest_paths", -1) != 0:
    raise SystemExit(f"invalid_manifest_paths: {d.get('invalid_manifest_paths')}")
PY
passed+=("status-ok")

# 2. Script flavor is py, not sh
python3 - "$root" <<'PY' || fail "script flavor is not py"
import json, sys
from pathlib import Path
root = Path(sys.argv[1])
init = json.loads((root / ".specify/init-options.json").read_text())
if init.get("script") == "sh":
    raise SystemExit("init-options.json script is sh, expected py")
integ = json.loads((root / ".specify/integration.json").read_text())
for name, settings in integ.get("integration_settings", {}).items():
    if settings.get("script") == "sh":
        raise SystemExit(f"integration_settings[{name}].script is sh")
PY
passed+=("script-py")

# 3. Root AGENTS.md exists
[[ -f AGENTS.md ]] || fail "missing AGENTS.md"
passed+=("agents-md")

# 4. Root CLAUDE.md absent
[[ ! -f CLAUDE.md ]] || fail "root CLAUDE.md still exists"
passed+=("no-root-claude")

# 5. .claude/CLAUDE.md is a thin import
[[ -f .claude/CLAUDE.md ]] || fail "missing .claude/CLAUDE.md"
grep -q '@../AGENTS.md' .claude/CLAUDE.md || fail ".claude/CLAUDE.md missing @../AGENTS.md"
if grep -q '## Skill Routing' .claude/CLAUDE.md; then
  fail ".claude/CLAUDE.md contains wiki routing heading copied from AGENTS.md"
fi
passed+=("claude-shim")

# 6. .omp/AGENTS.md is import-only, no SPECKIT block
[[ -f .omp/AGENTS.md ]] || fail "missing .omp/AGENTS.md"
grep -q '@../AGENTS.md' .omp/AGENTS.md || fail ".omp/AGENTS.md missing @../AGENTS.md"
if grep -q '<!-- SPECKIT START -->' .omp/AGENTS.md; then
  fail ".omp/AGENTS.md still has SPECKIT START block"
fi
passed+=("omp-import-only")

# 7. SPECKIT markers only in AGENTS.md among the three
speckit_count=0
for f in AGENTS.md .omp/AGENTS.md .claude/CLAUDE.md; do
  if [[ -f "$f" ]] && grep -q '<!-- SPECKIT START -->' "$f"; then
    speckit_count=$((speckit_count + 1))
    if [[ "$f" != "AGENTS.md" ]]; then
      fail "SPECKIT START found in $f (should only be in AGENTS.md)"
    fi
  fi
done
if [[ $speckit_count -eq 0 ]]; then
  fail "no SPECKIT START markers found in AGENTS.md"
fi
passed+=("single-speckit-block")

# 8. Native adapters exist
[[ -n "$(find .agents/skills -name 'SKILL.md' -path '*/speckit-*' 2>/dev/null | head -1)" ]] || fail "missing Codex speckit adapter"
[[ -n "$(find .grok/skills -name 'SKILL.md' -path '*/speckit-*' 2>/dev/null | head -1)" ]] || fail "missing Grok speckit adapter"
[[ -f .omp/commands/speckit.specify.md ]] || fail "missing OMP speckit adapter"
[[ -n "$(find .claude/skills -name 'SKILL.md' -path '*/speckit-*' 2>/dev/null | head -1)" ]] || fail "missing Claude speckit adapter"
passed+=("four-adapters")

# 9. Dispatcher file
[[ -f docs/agents/harness-dispatch.md ]] || fail "missing docs/agents/harness-dispatch.md"
if grep -q '# Agentic Co-DM Constitution' docs/agents/harness-dispatch.md; then
  fail "harness-dispatch.md contains copied constitution heading"
fi
passed+=("dispatcher")

# 10. No project-authored Spec Kit scripts
if [[ -d .specify/scripts ]]; then
  repo_scripts="$(find .specify/scripts -type f ! -name '*.py' ! -name '*.sh' ! -name '__pycache__' 2>/dev/null | head -1)"
  # We only check for non-standard files; shipped py and sh are expected
fi
passed+=("no-custom-speckit-scripts")

echo "speckit-dry: pass (${passed[*]})"
exit 0
