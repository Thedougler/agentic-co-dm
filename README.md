# Agentic Co-DM

Agentic Co-DM is a skill-based toolkit for preparing and wrapping up tabletop RPG sessions. It provides agent instructions, writing and visual skills, an Obsidian campaign wiki, Spec Kit feature workflows, and QMD search indexing.

## Requirements

- Python 3.12 or newer
- Node.js and npm
- `uv` (used to install Spec Kit and manage Python tooling)
- An Obsidian vault for campaign knowledge

The Python project has no application dependencies beyond the tools listed below; its scripts use the Python standard library.

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

   `PyYAML` is required by `.specify/extensions/agent-context`; the repository's own Python scripts otherwise use only the standard library.

7. Install QMD:

   ```bash
   npm install --global @tobilu/qmd
   qmd --version
   ```

8. Initialize and update the project search index:

   ```bash
   ./scripts/qmd-maintain.sh
   ```

   QMD indexes this repository's `wiki/` collection first. The maintenance script also expects the configured legacy campaign collections to exist; update those collection paths in `scripts/qmd-maintain.sh` if they are not available on your workstation.

## Verify the checkout

Run these checks from the repository root:

```bash
python tools/check_wiki_pages.py
specify --version
qmd status
```

If QMD is not initialized or its collections are stale, run `./scripts/qmd-maintain.sh` before `qmd status`.

## Working with the project

- Read `AGENTS.md` before making changes; it contains repository conventions and skill routing.
- Use `.agents/skills/*/SKILL.md` for the available agent skills.
- Treat `wiki/` as the compiled campaign knowledge source.
- Run `./scripts/qmd-maintain.sh` after wiki changes when QMD search is enabled.
- Read feature plans and quickstarts under `specs/` for feature-specific verification.
- Use the Spec Kit commands exposed by the configured agent integration for specification, planning, task generation, and implementation workflows.

## Repository layout

```text
.agents/skills/   Agent skills and procedures
.specify/         Spec Kit configuration and extensions
.omp/             OMP integration commands and agents
scripts/          Maintenance and ingest scripts
specs/            Feature specifications and quickstarts
tools/             Repository validation tools
wiki/             Obsidian campaign wiki
CONTEXT.md        Project vocabulary and domain boundaries
AGENTS.md         Repository instructions
```
