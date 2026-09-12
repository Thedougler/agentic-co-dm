#!/usr/bin/env bash
# Shared loader (SOURCE this, don't execute it): exports CAMPAIGN_ROOT and
# merges repo-local config from .env.local into the environment for shell
# hooks/scripts. Semantics match the Node (vault/campaigns/.claude/skills/npc-voice/scripts/
# lib/env.mjs) and Python (utils/tools/audio/src/shattered_audio/env_local.py)
# loaders: a real environment variable always wins; .env.local only fills what
# isn't already set; an absent .env.local is fine. Parses (never `source`s)
# .env.local so a value can't execute shell and stdin is never read — safe to
# source under `set -euo pipefail` and inside stdin-reading hooks.
#
# CAMPAIGN_ROOT: an explicit value (shell env or .env.local) wins; otherwise
# the repo root auto-detected from this file's own location (utils/scripts/lib
# -> three levels up), so a fresh clone works with an empty/absent .env.local
# and no git dependency.

__env_local_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
__campaign_os_default_root="$(cd "$__env_local_dir/../../.." && pwd)"
__env_local_file="$__campaign_os_default_root/.env.local"

if [ -f "$__env_local_file" ]; then
  while IFS= read -r __line || [ -n "$__line" ]; do
    __line="${__line#"${__line%%[![:space:]]*}"}"
    case "$__line" in ''|'#'*) continue ;; *'='*) ;; *) continue ;; esac
    __key="${__line%%=*}"
    __val="${__line#*=}"
    __key="${__key%"${__key##*[![:space:]]}"}"
    case "$__key" in [!A-Za-z_]*|*[!A-Za-z0-9_]*) continue ;; esac
    case "$__val" in
      \"*\") __val="${__val#\"}"; __val="${__val%\"}" ;;
      \'*\') __val="${__val#\'}"; __val="${__val%\'}" ;;
    esac
    if [ -z "${!__key:-}" ]; then export "$__key=$__val"; fi
  done < "$__env_local_file"
fi

export CAMPAIGN_ROOT="$(cd "${CAMPAIGN_ROOT:-$__campaign_os_default_root}" && pwd)"

unset __env_local_dir __campaign_os_default_root __env_local_file __line __key __val
