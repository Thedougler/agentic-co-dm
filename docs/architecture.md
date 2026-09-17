# Architecture

`tools/wiki_ops/scope.py` resolves typed file sets. `identity.py` classifies page identity before repairs. `mutations.py` exposes semantic section, frontmatter, link, index, and rename operations with hashes. `transactions.py` validates all operations in memory, writes atomically, then finalizes manifest/index/QMD once.

`wiki-lint` is diagnostic and plan-producing; `wiki-bulk-ops` is the mutation boundary. Template contracts in `wiki/templates/contracts/` own lifecycle-dependent structure. `docs/agents/policy-owners.yml` records policy ownership so maintenance can report contradictions without mutating canon.
