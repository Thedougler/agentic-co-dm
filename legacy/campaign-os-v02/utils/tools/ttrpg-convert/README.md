# ttrpg-convert

Native binary of [ttrpg-convert-cli](https://github.com/ebullient/ttrpg-convert-cli),
which converts 5eTools/Pf2eTools JSON bestiary, item, and rules data into
Obsidian markdown. Vendored here so any agent can regenerate reference
material or check what field names/wording the Fantasy Statblocks plugin
and Initiative Tracker expect, without re-deriving the tool's own schema
from memory or guessing at a 2024-format field name.

## Install

```bash
utils/tools/ttrpg-convert/install.sh
```

Downloads the pinned version's platform binary to `bin/ttrpg-convert`
(gitignored — re-run the script on a new machine or after a version bump
in the script itself).

## Use

Needs 5eTools JSON source data as input (this tool does not bundle
monster/item data, only the conversion templates) — point it at a local
clone of a 5etools data mirror, filtered to sources you're licensed to use
(SRD by default with no config). See `ttrpg-convert --help` and the
upstream README/docs for config file shape and source filtering.

```bash
utils/tools/ttrpg-convert/bin/ttrpg-convert -o /tmp/ttrpg-out /path/to/5etools-data
```

Treat generated output as scratch/reference, not something to commit
as-is — this repo's own creature pages follow `_templates/creature.md`,
not the raw tool output.
