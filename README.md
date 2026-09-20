# Agentic Co-DM

Agentic Co-DM is a skill-based toolkit for preparing and wrapping up tabletop RPG sessions. It provides agent instructions, writing and visual skills, an Obsidian campaign wiki, Spec Kit feature workflows, and QMD search indexing.

## Requirements

- Python 3.12 or newer
- Node.js 22 or newer and npm
- `uv` (used to install Python dependencies and Spec Kit)
- An Obsidian vault for campaign knowledge

Python dependencies are declared in `pyproject.toml`; Node development tools are declared in `package.json`. QMD is installed globally because the maintenance scripts invoke its `qmd` executable.

## First-time installation and setup

Run these steps once from a fresh checkout. On later sessions, start at [Verify the checkout](#verify-the-checkout).

1. Install the host prerequisites:

   - Python 3.12 or newer
   - Node.js 22 or newer and npm

   Use your operating system's package manager or the official installers. Confirm the versions:

   ```bash
   python3 --version
   node --version
   npm --version
   ```

2. Clone the repository:

   ```bash
   git clone <repository-url>
   cd agentic-co-dm
   ```

3. Install `uv` if it is not already available:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   Restart the shell or add `~/.local/bin` to `PATH` if the installer requests it, then re-run `uv --version`.

4. Install the locked Python dependencies and development tools:

   ```bash
   uv sync
   source .venv/bin/activate
   .venv/bin/python -m pytest --version
   .venv/bin/ruff --version
   .venv/bin/pyright --version
   ```

   `uv sync` creates `.venv` with the runtime and development dependencies. If a tool is missing, run `uv sync` again.

5. Install the Node development tools:

   ```bash
   npm install
   ```

6. Install Spec Kit. This repository is already initialized for the `omp` integration; do not run `specify init` over the checkout.

   ```bash
   uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
   specify --version
   ```

7. Create the local environment file:

   ```bash
   cp .env.example .env
   ```

   Set the path to your Obsidian vault:

   ```dotenv
   OBSIDIAN_VAULT_PATH=/absolute/path/to/your/vault
   ```

   Keep the QMD defaults from `.env.example` unless you use a different index configuration. `.env` is ignored by Git.

8. Install QMD:

   ```bash
   npm install --global @tobilu/qmd
   qmd --version
   ```

9. Initialize and update the project search index:

   ```bash
   ./scripts/qmd-maintain.sh
   ```

   QMD indexes this repository's `wiki/` collection first. The maintenance script also expects the configured legacy campaign collections to exist; update those collection paths in `scripts/qmd-maintain.sh` if they are not available on your workstation.

## Verify the checkout

Run these checks from the repository root after activating `.venv`:

```bash
python3 tools/check_wiki_pages.py
specify --version
qmd status
npm run check:python
npm test
npm run lint:markdown -- --no-globs README.md
./scripts/wiki-maintain --report --summary-only
```

If QMD is not initialized or its collections are stale, run `./scripts/qmd-maintain.sh` before `qmd status`.

`wiki-maintain` A3 runs `scripts/token-count.py` when present (it is on main); soft-skips only if the CLI is absent. A noisy vault (HARD lint) is expected during migration — quiet keep-ahead only when Layer A is clean.

## Working with the project

- Read `AGENTS.md` before making changes; it is the source of truth for conventions and skill routing.
- Use `.agents/skills/*/SKILL.md` for agent skills.
- Treat `wiki/` as the **compiled** campaign knowledge layer. `wiki/_raw/` is an ingest inbox only — file then archive; never leave sources parked there; never overwrite `_raw/` as live canon.
- Prefer thin CLIs over dumping whole files into agent context (`scripts/manifest.py`, Retrieval Primitives in `llm-wiki`).
- Run `./scripts/qmd-maintain.sh` after wiki changes when QMD search is enabled.
- Wiki canon commits on `main`. Agent-instruction work uses a feature branch; sync local `main` with `./scripts/git-sync-main` before work. For a direct `main` push, fetch `origin/main`, rebase local commits onto it, then push; if push is rejected as non-fast-forward, repeat fetch → rebase → push up to three times and stop on conflict.
- Spec Kit workflows live under `specs/` and the configured agent integration.

## Wiki health (operators)

Design lock: `docs/agents/wiki-maintenance-loop.md` (issue #90).

| Task | Command / pointer |
| --- | --- |
| Layer A report (lint + waste leads + `_raw/` + plans) | `./scripts/wiki-maintain --report` |
| HARD wiki lint only | `./scripts/wiki-lint --json` |
| Context-waste leads | `python3 scripts/context-waste-scan.py` |
| Objective tokens | `python3 scripts/token-count.py --sum wiki` / `--footprint` — default `cl100k_base`; **not** `bytes/4` |
| Filename remorph plan | `./scripts/remorph-page-filename-kebab --dry-run` then `--apply` (greenlit 2026-09-14 for kebab / Aruhe / 00 strips; prefer PR diffs) |

**Do not automate without an explicit greenlight:** lore invent, dedup merge, link demotions during migration freeze, craft/narrative/mechanics thinning for token scores, or collapsing conflicting rumors into one “truth.” Mass kebab remorph `--apply` unlocked 2026-09-14 (Nick); still dry-run first. Scripts do not grade prose — Creative Director does.

Related methods: `docs/agents/context-waste-method.md`, `docs/agents/token-measurement.md`.

## Repository layout

```text
.agents/skills/   Agent skills and procedures
.specify/         Spec Kit configuration and extensions
.omp/             OMP integration commands and agents
docs/agents/      Operator/agent method locks (maintenance, tokens, waste, …)
scripts/          Maintenance, lint, remorph, and ingest CLIs
specs/            Feature specifications and quickstarts
tools/            Repository validation tools (e.g. wiki lint)
wiki/             Obsidian campaign wiki (compiled knowledge)
CONTEXT.md        Project vocabulary and domain boundaries
AGENTS.md         Repository instructions (conventions + routing)
```
