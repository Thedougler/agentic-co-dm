@../AGENTS.md

# OMP runtime

OMP list settings replace rather than merge. Preserve every existing entry when changing arrays such as `disabledProviders` and `disabledExtensions`.

Read `.omp/config.yml` for model roles, caps, isolation, and discovery settings. Do not copy those values here. Read `specs/<feature>/` for feature requirements and task state.

## Behavioral validation

For skill-creator test subagents, use the configured `task` model. Give cold
context containing the changed excerpt, task, scope, and success criteria; grant
no write permission; reconcile the output before completion.

Prefer flexible, outcome-based guidance over rigid carveouts and unnecessary
step-by-step specificity.

