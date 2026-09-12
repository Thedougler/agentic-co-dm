# wiki-cli

The lint engine of record ([ADR-0042](../../docs/adr/0042-wiki-cli-engine-of-record.md),
[ADR-0045](../../docs/adr/0045-wiki-cli-cutover-complete.md)). A Python CLI
(`wiki`) replacing the retired JS lint pipeline. Invoked via npm wrappers
(`npm run lint -- <path>`, `npm run lint:sweep`, `npm run lint:drain`) which
delegate to `uv run --directory utils/wiki-cli wiki <command>`. The command
surface is [ADR-0064](../../docs/adr/0064-lint-output-is-an-instruction-list.md).

`uv sync` installs dependencies; `uv run pytest` runs the tests; `pyright`
from the repo root type-checks (config lives in the root
`pyrightconfig.json`).
