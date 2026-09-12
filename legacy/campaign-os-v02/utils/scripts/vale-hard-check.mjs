#!/usr/bin/env node
// vale-hard-check — the blocking `.vale-hard.ini` pass, routed through
// runValeScoped (lib/prose-scope.mjs) instead of invoking `vale` directly.
//
// A raw `vale --config .vale-hard.ini <file>` call skips
// withFrontmatterGuard's pre-scan neutralization entirely: Vale's
// `lintMetadata` code path for YAML frontmatter runs BEFORE
// TokenIgnores/BlockIgnores apply, so a frontmatter value DESIGNED to hold
// a vale-hard-flagged token (e.g. `owner_skill:` legitimately containing
// "SKILL.md" per ADR-0044) trips CampaignOS.ProcessLeak even though the
// same file passes `npm run lint` clean. runValeScoped's own doc comment
// already names this script as the intended caller: "wiki-cli's Vale
// producers' direct invocations route through
// this single entry point."
//
// CLI: node vale-hard-check.mjs <file...>   (paths relative to cwd or absolute)
// Prints one line per alert: "<file>:<line>:<col> <severity> <message> [<Check>]".
// Exit code mirrors `vale`'s own single-invocation contract: 0 clean, 1
// alerts found, 2 a `vale` execution error (batch driver failure, unparseable
// output, or a missing-file abort that survived every retry).
import path from 'node:path';
import { REPO_ROOT, runValeScoped } from './lib/prose-scope.mjs';

function main() {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.error('usage: vale-hard-check.mjs <file...>');
    process.exit(2);
  }

  const targets = args.map((a) => path.relative(REPO_ROOT, path.resolve(a)));
  const { byFile, status, batchErrors } = runValeScoped(targets, {
    configPath: path.join(REPO_ROOT, '.vale-hard.ini'),
  });

  if (batchErrors.length > 0) {
    for (const err of batchErrors) console.error(`vale-hard-check: ${err}`);
    process.exit(2);
  }

  let alertCount = 0;
  for (const [file, alerts] of byFile) {
    for (const alert of alerts) {
      alertCount += 1;
      const line = alert.Line ?? 1;
      const col = alert.Span?.[0] ?? 1;
      console.log(`${file}:${line}:${col} ${alert.Severity} ${alert.Message} [${alert.Check}]`);
    }
  }

  if (alertCount > 0) process.exit(1);
  process.exit(status > 1 ? 2 : 0);
}

main();
