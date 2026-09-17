# Grok Repository Addendum

Grok Build-specific guidance for this repository. Grok Build is the primary Grok path; Grok Bot is out of scope. Project context remains in `AGENTS.md`; shared agent behavior remains in the constitution; this file records only native Grok Build behavior.

## Behavioral test subject

For agent-facing surface changes, Luna is not available in Grok. Use the closest independent Grok Build equivalent as the behavioral test subject and name that substitution in completion evidence. Give it cold context, no write permission in the prompt, the relevant task or task slice to perform, and explicit scope and success criteria. Reconcile its output as behavioral evidence before declaring completion. The harness substitution is not a gap; inability to run independent validation is the blocker.

## Native image handling

- On Grok Build, render the visual prompt inventory into natural prose through `imagine`; do not send the inventory template as if it were the host command syntax.
- User-attached chat images are referenced by host tokens such as `[Image #1]`; they have no vault path. Preserve the token as the image input rather than inventing an attachment filename.
- The OMP `xd://generate_image` path/data/mime contract does not apply to Grok Build. Use the image-input mechanism exposed by the active Grok session.
- Keep identity anchors and expressive scene direction separate in the brief. Confirm the generated result and its returned asset reference before filing or linking it.
