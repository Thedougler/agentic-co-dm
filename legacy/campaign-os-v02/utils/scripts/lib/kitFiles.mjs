// Kit files (docs/guardrails/_FORMAT.md F15) — never autofix-eligible.
// F15 requires a deliberate edit with a version bump and a MIGRATION-LOG
// entry, which no unattended pass can produce.
//
// Every CLAUDE.md at any depth counts, not only the root one: a subtree
// CLAUDE.md is agent instruction prose under the same edit-deliberately
// discipline.
//
// Two consumers share this definition — auto-drain.mjs (never selects a kit
// file for a wave) and any autofix pass (skipped for kit files,
// keeps the advisory report).
export function isKitFile(rel) {
  return /(^|\/)CLAUDE\.md$/.test(rel) || /^docs\/guardrails\/.*\.md$/.test(rel);
}
