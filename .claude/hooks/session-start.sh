#!/bin/bash
# SessionStart hook for Claude Code on the web: installs the locked Python
# environment (.venv via uv, incl. Python 3.12+, Vale, ruff, pyright, pytest)
# and the Node lint tools so `./scripts/run-pytest`, `./scripts/wiki lint`,
# and the npm lint scripts work in remote containers.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}"

if ! command -v uv >/dev/null 2>&1; then
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
fi

# pyproject requires Python >=3.12; uv fetches a managed interpreter if needed.
uv sync --frozen

npm install --no-audit --no-fund

# The vale wheel downloads its Go binary on first run with Python's urllib,
# which rejects the remote proxy CA under Python 3.13+ strict X.509 checks.
# Fetch the matching binary with curl instead (idempotent: skipped once real).
vale_bin="$(.venv/bin/python -c 'import vale, pathlib; print(pathlib.Path(vale.__file__).parent / "vale_bin")')"
if [ "$(stat -c %s "$vale_bin")" -lt 1000 ]; then
  vale_version="$(.venv/bin/python -c 'import importlib.metadata as m; print(".".join(m.version("vale").split(".")[:3]))')"
  tmp="$(mktemp -d)"
  curl -fsSL "https://github.com/errata-ai/vale/releases/download/v${vale_version}/vale_${vale_version}_Linux_64-bit.tar.gz" \
    | tar -xz -C "$tmp" vale
  install -m 0755 "$tmp/vale" "$vale_bin"
  rm -rf "$tmp"
fi
.venv/bin/vale --version

# Vale ships its binary in the venv; expose .venv/bin for the session.
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export PATH=\"$PWD/.venv/bin:$PWD/node_modules/.bin:\$PATH\"" >> "$CLAUDE_ENV_FILE"
fi
