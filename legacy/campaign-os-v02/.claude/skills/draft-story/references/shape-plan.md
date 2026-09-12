# Shape plan (DS4)

Before drafting, beside the REGISTER line, write one line per planned
section: `<section>: opens <move> / closes <shape>` where shape ∈
{concrete-image, dialogue, action-cut, epigram} and epigram appears at
most once per piece. Tense: register.md's default, or name the override
and reason here. The plan is a commitment — Pass 2 checks the draft
against it, and `node utils/scripts/prose-shape.mjs <file> --profile
vault/refs/stories/style-profile.json` must exit 0 before DS7 (a
drift-only flag blocks only once the profile has dm_signed_off: true).
