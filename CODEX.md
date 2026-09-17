# Codex Companion

Codex-specific guidance for this repository. Load `AGENTS.md` first; use this file only for native Codex behavior, verified Codex gaps, and Codex UI affordances. Shared policy stays in `AGENTS.md`, the constitution, specs, skills, and docs named there.

## Start

1. Confirm `AGENTS.md` is the active operating map before applying this file.
   Done when shared routing, sources of truth, Spec Kit workflow, and wiki/campaign gates come from `AGENTS.md` rather than being reconstructed here.
2. Classify the request against the shared routing in `AGENTS.md`, then add only Codex-specific handling from this companion.
   Done when the chosen skill, spec route, or workflow owner is named or clearly applied, and no shared rule has been duplicated as Codex policy.
3. Use native Codex app features when they are the shortest reliable path: task/thread coordination for Codex tasks, sidebar tools for task organization, inline code comments for review feedback, image generation for generated or edited images, and automations for scheduled follow-up.
   Done when Codex-only state is handled through the Codex surface that owns it, while durable repository state still lands in files, commits, specs, or wiki owners.
4. Verify at the boundary the user asked for.
   Done when file changes are checked in the repo, generated media has a confirmed returned asset path before it is filed or linked, Codex task actions name the affected task, and any unverified Codex capability is reported as a gap.

## Codex Task Surfaces

- Use Codex tasks for user-requested task management: create, fork, inspect, continue, hand off, archive, rename, pin, or wait on tasks through the Codex task tools.
- Use heartbeat automations for recurring follow-up in the current thread unless the user explicitly asks for standalone project work or a new task per run.
- Keep notification preferences in automation settings, not in the durable prompt.
- When opening files, reviews, terminals, browser tabs, or generated artifacts for the user, use Codex panels when that helps inspection; repository truth remains the file content and verification output.

## Subagents And Delegation

The root Codex agent remains lead and accountable for repository changes. When delegation is useful, follow the active Codex multi-agent routing loaded for the workspace: pass scoped context, set the required model and effort explicitly, and review the result before changing files or reporting completion.

## Inline Review

Use Codex inline comments for actionable code review findings that belong on exact lines. Keep each comment tied to the smallest useful range, with the priority and file path set. Put broad summaries, tradeoffs, and non-line-specific notes in the chat response.

## Images And Attachments

- Preserve Codex-provided attachment references exactly until the host returns a concrete file path or displayed image.
- For new or edited images, use the native Codex image tool and confirm the returned asset before adding a wiki embed, session file link, token crop, or owner-page reference.
- The repository has no verified Codex CLI image-generation contract. Treat CLI image invocation as unavailable until a Codex-focused session records a tested command, inputs, outputs, and asset location.
- Do not substitute OMP's `xd://generate_image` request shape for Codex. The OMP `openai-codex` provider is backend selection evidence, not a Codex harness contract.

## Spec Kit In Codex

Invoke Codex Spec Kit phases through the generated `.agents/skills/speckit-*` adapters when the user asks for a Spec Kit phase. Treat adapter edits as out of scope for ordinary Codex companion work.

## Gaps

If a Codex-native behavior is uncertain, mark the capability as unverified and keep the work on a verified path. Record durable fixes in the authoritative repository surface when the gap affects future agents; report one-off runtime limitations in the final response.
