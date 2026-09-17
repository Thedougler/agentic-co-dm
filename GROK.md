# Grok Repository Addendum

Temporary Grok Build-only image-generation notes. Grok Build is the primary Grok path; Grok Bot is out of scope. Shared policy remains in `AGENTS.md`; this file records only native Grok Build behavior.

## Native image handling

- On Grok Build, render the visual prompt inventory into natural prose through `imagine`; do not send the inventory template as if it were the host command syntax.
- User-attached chat images are referenced by host tokens such as `[Image #1]`; they have no vault path. Preserve the token as the image input rather than inventing an attachment filename.
- The OMP `xd://generate_image` path/data/mime contract does not apply to Grok Build. Use the image-input mechanism exposed by the active Grok session.
- Keep identity anchors and expressive scene direction separate in the brief. Confirm the generated result and its returned asset reference before filing or linking it.
