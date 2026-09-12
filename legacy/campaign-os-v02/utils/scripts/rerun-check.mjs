#!/usr/bin/env node
// rerun-check — REFACTOR-PLAN.md P1.2. A single command an orchestrator runs
// to independently re-verify a dispatch wave, instead of a judgment call
// each time ("does this look right?"). Never trust a subagent's self-report
// (orchestrator contract item 2) — this is the mechanical re-run that
// contract requires before a wave closes (vault/refs/runbook-dispatch-wave.md
// step 4).
//
// CLI:
//   node rerun-check.mjs lint <file...>   npm run lint's own report against
//                                          exactly these files (no autofix —
//                                          a re-verification checks, it
//                                          doesn't mutate; --fail-on any so
//                                          ANY remaining finding fails the
//                                          wave, not just error-severity)
//   node rerun-check.mjs test [file...]   npm test, or node --test against
//                                          exactly these test files if given
//   node rerun-check.mjs --cmd "<command>" [file...]
//                                          an arbitrary shell command,
//                                          each file appended as an argv
//                                          entry (quote the whole command)
//
// Always prints exactly one line: `VERDICT: PASS` or `VERDICT: FAIL (see
// output above)`, and exits 0 on PASS, 1 on FAIL — so a caller can grep the
// one line instead of re-deriving pass/fail from raw tool output.
import { spawnSync } from 'node:child_process';
import { REPO_ROOT } from './lib/prose-scope.mjs';

function run(cmd, args) {
  const result = spawnSync(cmd, args, { cwd: REPO_ROOT, stdio: 'inherit', shell: false });
  return result.status ?? 1;
}

function main() {
  const argv = process.argv.slice(2);
  if (argv.length === 0) {
    console.error('usage: rerun-check.mjs <lint|test|--cmd "<command>"> [file...]');
    process.exit(1);
  }

  let status;
  if (argv[0] === 'lint') {
    const files = argv.slice(1);
    if (files.length === 0) {
      console.error('rerun-check lint: no files given — pass the wave\'s exact touched-path list');
      process.exit(1);
    }
    status = run('uv', ['run', '--directory', 'utils/wiki-cli', 'wiki', 'lint', ...files]);
  } else if (argv[0] === 'test') {
    const files = argv.slice(1);
    status = files.length > 0
      ? run('node', ['--test', ...files])
      : run('npm', ['test']);
  } else if (argv[0] === '--cmd') {
    const command = argv[1];
    const files = argv.slice(2);
    if (!command) {
      console.error('rerun-check --cmd: no command string given');
      process.exit(1);
    }
    status = run('bash', ['-c', `${command} "$@"`, 'bash', ...files]);
  } else {
    console.error(`rerun-check: unknown check '${argv[0]}' — expected lint, test, or --cmd`);
    process.exit(1);
  }

  console.log(status === 0 ? 'VERDICT: PASS' : 'VERDICT: FAIL (see output above)');
  process.exit(status === 0 ? 0 : 1);
}

main();
