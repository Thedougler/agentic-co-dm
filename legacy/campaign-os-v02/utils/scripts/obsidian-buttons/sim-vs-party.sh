#!/usr/bin/env bash
# Obsidian button target: run the combat simulator — full party vs the
# monster page the button lives on. Called by the Shell Commands plugin
# with the active note's absolute path. Writes a dated report under
# vault/campaigns/shattered-sea/dm-intel/sim-runs/ and opens it in Obsidian.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../../.." && pwd)"
# shellcheck source=lib/dm-console.sh
source "$HERE/lib/dm-console.sh"

monster="${1:-}"
if [[ ! -f "$monster" ]]; then
  echo "Monster file not found: '$monster'" >&2
  exit 1
fi
if ! grep -q '^```statblock' "$monster"; then
  echo "No \`\`\`statblock fence in $(basename "$monster") — the sim can only read Fantasy Statblocks pages." >&2
  exit 1
fi

slug="$(basename "$monster" .md)"
out_dir="$REPO/vault/campaigns/shattered-sea/dm-intel/sim-runs"
out="$out_dir/$slug-vs-party-$(date +%Y%m%d-%H%M).md"
mkdir -p "$out_dir"

cd "$REPO"
sheets=(vault/campaigns/shattered-sea/dm-intel/*-sheet.md)
loadout_args=()
for f in vault/campaigns/shattered-sea/dm-intel/loadouts/*.loadouts.yaml; do
  [[ "$f" == *s06-encounters* ]] && continue  # session-specific scenarios, not party baseline
  loadout_args+=(--loadouts "$f")
done

sim_log="${TMPDIR:-/tmp}/campaign-os-sim.log"
: >"$sim_log"
dm_console_watch sim "⚔ Sim vs Party" "$sim_log"
if ! pnpm --silent sim "${sheets[@]}" "$monster" "${loadout_args[@]}" \
    --seed 42 --out "$out" >"$sim_log" 2>&1; then
  echo "Sim failed — $(tail -3 "$sim_log" | tr '\n' ' ')" >&2
  exit 1
fi

# Pull the headline number for the notification.
winline="$(grep -im1 'win' "$out" | sed 's/[|*#]//g' | tr -s ' ' || true)"
echo "⚔ Party vs $slug: ${winline:-report written} → ${out#"$REPO"/}"

# Open the report in Obsidian (best-effort; the report exists either way).
encoded="$(python3 -c 'import sys,urllib.parse; print(urllib.parse.quote(sys.argv[1]))' "$out")"
open "obsidian://open?path=$encoded" 2>/dev/null || true
