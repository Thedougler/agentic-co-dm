# Context Map

Multi-context layout for Campaign OS. Each context owns a bounded vocabulary and
its own `CONTEXT.md`; this file is the index. Read the root context first, then the
context relevant to the area you're working in.

| Context | File | What it covers |
|---------|------|----------------|
| Campaign OS (system-wide) | [`CONTEXT.md`](CONTEXT.md) | Process vocabulary, at-table design, pipeline stages, session/episode distinction |
| wiki-cli | [`utils/wiki-cli/CONTEXT.md`](utils/wiki-cli/CONTEXT.md) | Linter, VaultIndex, link graph, PageRank, vault organiser |
| dndsim | [`utils/dndsim/CONTEXT.md`](utils/dndsim/CONTEXT.md) | Combat simulation engine, rules packs, primitives, policies |

## ADRs

System-wide decisions live in [`docs/adr/`](docs/adr/). Context-specific decisions
live alongside their context's `CONTEXT.md` when they exist:

- `utils/wiki-cli/docs/adr/` — wiki-cli-specific decisions (not yet present; add as needed)
- `utils/dndsim/docs/adr/` — dndsim-specific decisions (not yet present; add as needed)
