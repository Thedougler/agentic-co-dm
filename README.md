# Agentic Co-DM

Agentic Co-DM is a skill-based toolkit for preparing and wrapping up tabletop RPG sessions. It combines agent instructions, writing and visual skills, an Obsidian campaign wiki, Spec Kit feature workflows, and QMD search indexing.

## Start here

| You are... | Start with... |
| --- | --- |
| A human exploring the project | [Browse the wiki](#browse-the-wiki), then read [`CONTEXT.md`](CONTEXT.md) |
| An agent working in the repository | [`AGENTS.md`](AGENTS.md), then the relevant [skill](.agents/skills/) |
| Maintaining the wiki | [`wiki/AGENTS.md`](wiki/AGENTS.md) and [`wiki/index.md`](wiki/index.md) |
| Working on a feature | [`specs/`](specs/) and its `spec.md`, `plan.md`, and `tasks.md` |

## Browse the wiki

The links below use ordinary Markdown paths, so GitHub opens them as files and directory listings. The [wiki index](wiki/index.md) is the generated Obsidian map; its `[[wikilinks]]` are most useful inside Obsidian.

### Campaign overview

- [Wiki index](wiki/index.md)
- [Players](wiki/synthesis/Players.md)
- [Story so far](wiki/synthesis/story-so-far.md)
- [Party combat profile](wiki/synthesis/party-combat-profile.md)
- [DM voice notes](wiki/synthesis/dm-voice-notes.md)
- [Session materials](wiki/journal/sessions/shattered-sea/)

### Player characters

- [Jean-Claude Tabarnack](wiki/entities/pc/jean-claude-tabarnack.md)
- [Perrin Black Jaw](wiki/entities/pc/perrin-black-jaw.md)
- [Catarina Davirelli](wiki/entities/pc/catarina-davirelli.md)
- [Crissdalynn Khinriss](wiki/entities/pc/crissdalynn-khinriss.md)
- [Delmar Fisk](wiki/entities/pc/delmar-fisk.md)
- [All player characters](wiki/entities/pc/)

### Entity collections

| Collection | Contents |
| --- | --- |
| [NPCs](wiki/entities/npc/) | People and recurring characters |
| [Places](wiki/entities/place/) | Sites and settlements |
| [Regions](wiki/entities/region/) | Route-scale areas and territories |
| [Factions](wiki/entities/faction/) | Organizations and powers |
| [Creatures](wiki/entities/creature/) | Monsters and other creatures |
| [Items](wiki/entities/item/) | Equipment, treasures, and objects |
| [Vehicles](wiki/entities/vehicle/) | Ships and other named vehicles |
| [Quests](wiki/entities/quest/) | Campaign situations and objectives |
| [Lore](wiki/entities/lore/) | Durable world truths and beliefs |
| [Templates](wiki/templates/) | Page scaffolds for new wiki entries |

`wiki/` is the compiled campaign knowledge layer. `_raw/` is an ingest inbox, `_staging/` is the review queue when staged writes are enabled, and `_archive/` contains historical evidence; those folders are not current canon.

## What is in the repository?

```text
.agents/skills/   Agent skills and procedures
.specify/         Spec Kit configuration and extensions
.omp/              OMP integration commands and agents
docs/agents/       Operator and agent method locks
scripts/           Maintenance, lint, remorph, and ingest CLIs
specs/             Feature specifications and quickstarts
tools/             Repository validation tools
wiki/              Obsidian campaign wiki
CONTEXT.md         Project vocabulary and domain boundaries
AGENTS.md          Repository instructions and skill routing
```

## Working with agents

- Read [`AGENTS.md`](AGENTS.md) before making changes; it defines conventions and routing.
- Use one of the procedures in [`.agents/skills/`](.agents/skills/) instead of inventing a parallel workflow.
- Treat the wiki as compiled, citable knowledge. The search index is derived; the wiki remains the source of truth.
- Before writing a wiki page, read [`wiki/AGENTS.md`](wiki/AGENTS.md), use the matching template, and keep related pages linked.
- Run `./scripts/qmd-maintain.sh` after wiki changes when QMD search is enabled.
- Wiki canon commits on `main`. Agent-instruction work uses a feature branch.
- Spec Kit workflows live under [`specs/`](specs/) and the configured agent integration.

## Requirements

- Python 3.12 or newer
- Node.js and npm
- `uv` (used to install Spec Kit and manage Python tooling)
- An Obsidian vault for campaign knowledge

Most repository scripts use the Python standard library. Spec Kit’s agent-context extension needs `PyYAML`. Objective token counts use `tiktoken` via `scripts/token-count.py` (pinned in `pyproject.toml`) — see [`docs/agents/token-measurement.md`](docs/agents/token-measurement.md).

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

`wiki-maintain` A3 runs `scripts/token-count.py` when present (it is on main); soft-skips only if the CLI is absent. A noisy vault (HARD lint) is expected during migration — quiet keep-ahead only when Layer A is clean.

## Wiki health (operators)

Design lock: [`docs/agents/wiki-maintenance-loop.md`](docs/agents/wiki-maintenance-loop.md).

| Task | Command / pointer |
| --- | --- |
| Layer A report (lint + waste leads + `_raw/` + plans) | `./scripts/wiki-maintain --report` |
| HARD wiki lint only | `./scripts/wiki-lint --json` |
| Context-waste leads | `python3 scripts/context-waste-scan.py` |
| Objective tokens | `python3 scripts/token-count.py --sum wiki` / `--footprint` — default `cl100k_base`; **not** `bytes/4` |
| Filename remorph plan | `./scripts/remorph-page-filename-kebab --dry-run` then `--apply` |

**Do not automate without an explicit greenlight:** lore invent, dedup merge, link demotions during migration freeze, craft/narrative/mechanics thinning for token scores, or collapsing conflicting rumors into one “truth.” Mass kebab remorph `--apply` is unlocked; still dry-run first.

Related methods: [`docs/agents/context-waste-method.md`](docs/agents/context-waste-method.md) and [`docs/agents/token-measurement.md`](docs/agents/token-measurement.md).
