# Agentic Co-DM

Agentic Co-DM is a skill-based toolkit for preparing and wrapping up tabletop RPG sessions. It provides agent instructions, writing and visual skills, an Obsidian campaign wiki, Spec Kit feature workflows, and QMD search indexing.

## Requirements

- Python 3.12 or newer
- Node.js and npm
- `uv` (used to install Spec Kit and manage Python tooling)
- An Obsidian vault for campaign knowledge

Most repository scripts use the Python standard library. Spec Kit’s agent-context extension needs `PyYAML`. Objective token counts use `tiktoken` via `scripts/token-count.py` (pinned in `pyproject.toml`) — see `docs/agents/token-measurement.md`.

## Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd agentic-co-dm
   ```

2. Install `uv` if it is not already available:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   Restart the shell or add `~/.local/bin` to `PATH` if the installer requests it.

3. Install Spec Kit. This repository is already initialized for the `omp` integration; do not run `specify init` over the checkout.

   ```bash
   uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
   specify --version
   ```

4. Create the local environment file:

   ```bash
   cp .env.example .env
   ```

5. Set `OBSIDIAN_VAULT_PATH` in `.env` to the path of your Obsidian vault. Keep the QMD defaults from `.env.example` unless you use a different index configuration.

6. Create the Python environment and install the Python tooling used by the Spec Kit agent-context extension:

   ```bash
   uv venv --python 3.12
   source .venv/bin/activate
   python -m pip install pyyaml
   ```

7. Install QMD:

   ```bash
   npm install --global @tobilu/qmd
   qmd --version
   ```

8. Initialize and update the project search index:

   ```bash
   ./scripts/qmd-maintain.sh
   ```

   QMD indexes this repository’s `wiki/` collection first. The maintenance script also expects the configured legacy campaign collections to exist; update those collection paths in `scripts/qmd-maintain.sh` if they are not available on your workstation.

## Verify the checkout

Run these checks from the repository root:

```bash
python tools/check_wiki_pages.py
specify --version
qmd status
./scripts/wiki-maintain --report --summary-only
```

If QMD is not initialized or its collections are stale, run `./scripts/qmd-maintain.sh` before `qmd status`.

`wiki-maintain` Layer A includes objective token totals via `scripts/token-count.py`. A noisy vault (HARD lint) is expected during migration — quiet keep-ahead only when Layer A is clean.

## Working with the project

- Read `AGENTS.md` before making changes; it is the source of truth for conventions and skill routing.
- Use `.agents/skills/*/SKILL.md` for agent skills.
- Treat `wiki/` as the **compiled** campaign knowledge layer. `wiki/_raw/` is an ingest inbox only — file then archive; never leave sources parked there; never overwrite `_raw/` as live canon.
- Prefer thin CLIs over dumping whole files into agent context (`scripts/manifest.py`, Retrieval Primitives in `llm-wiki`).
- Run `./scripts/qmd-maintain.sh` after wiki changes when QMD search is enabled.
- Keep feature work on branches; sync local `main` with `./scripts/git-sync-main` (ff-only to `origin/main`).
- Spec Kit workflows live under `specs/` and the configured agent integration.

## Wiki health (operators)

Design lock: `docs/agents/wiki-maintenance-loop.md` (issue #90).

| Task | Command / pointer |
| --- | --- |
| Layer A report (lint + waste leads + `_raw/` + plans) | `./scripts/wiki-maintain --report` |
| HARD wiki lint only | `./scripts/wiki-lint --json` |
| Context-waste leads | `python3 scripts/context-waste-scan.py` |
| Objective tokens | `python3 scripts/token-count.py --sum wiki` / `--footprint` — default `cl100k_base`; **not** `bytes/4` |
| Filename remorph plan | `./scripts/remorph-page-filename-kebab --dry-run` — **`--apply` gated** until greenlit |

**Do not automate without an explicit greenlight:** lore invent, mass kebab rename apply, dedup merge, link demotions during migration freeze, craft/narrative/mechanics thinning for token scores, or collapsing conflicting rumors into one “truth.” Scripts do not grade prose — Creative Director does.

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
