# Architecture

`tools/wiki_ops/scope.py` resolves typed file sets. `identity.py` classifies page identity before repairs. `mutations.py` exposes semantic section, frontmatter, link, index, manifest, and rename operations with hashes. `transactions.py` validates all operations in memory, writes atomically, then finalizes manifest/index/QMD once, retaining committed content when QMD fails.

`scripts/wiki-lint` is diagnostic and plan-producing; `scripts/wiki-bulk-ops` is the mutation boundary. Template contracts in `wiki/templates/contracts/` own status-dependent structure. `tools/creative_lint/vale_adapter.py` maps Vale findings through `rules/registry.yml`, while typed state controls applicability. `docs/agents/policy-owners.yml` records policy ownership so maintenance can report contradictions without mutating canon.
