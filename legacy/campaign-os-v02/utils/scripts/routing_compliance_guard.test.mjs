// REFACTOR-PLAN.md P1.1 — pipes stdin payloads into the real PreToolUse hook
// (routing_compliance_guard.sh) against fixture transcripts, same pattern as
// a runGate helper (CAMPAIGN_ROOT override, real
// script invocation, no reimplementation of the hook's own logic here).
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { basename, dirname, join } from 'node:path';
import { mkdtempSync, mkdirSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';

const repoRoot = dirname(fileURLToPath(import.meta.url));
const hookScript = join(repoRoot, 'routing_compliance_guard.sh');

function writeTranscript(lines) {
  const dir = mkdtempSync(join(tmpdir(), 'routing-guard-test-'));
  const file = join(dir, 'transcript.jsonl');
  writeFileSync(file, lines.map((l) => JSON.stringify(l)).join('\n') + '\n');
  return file;
}

function runHook({ filePath, transcriptPath, agentId, tmpRoot }) {
  const payload = JSON.stringify({
    tool_input: { file_path: filePath },
    transcript_path: transcriptPath,
    ...(agentId ? { agent_id: agentId, agent_type: 'general-purpose' } : {}),
  });
  const stdout = execFileSync('bash', [hookScript], {
    input: payload,
    cwd: repoRoot,
    encoding: 'utf8',
    env: {
      ...process.env,
      CAMPAIGN_ROOT: join(repoRoot, '..', '..'),
      ...(tmpRoot ? { TMPDIR: tmpRoot } : {}),
    },
  });
  return stdout;
}

/** Lays out the harness's subagent-transcript path under a controlled TMPDIR:
 * <tmp>/claude-<uid>/<project-slug>/<session>/tasks/<agent-id>.output, where
 * slug and session are derived from the PARENT transcript's own path — the
 * same derivation the hook performs. */
function writeSubagentTranscript(parentTranscript, agentId, lines) {
  const tmpRoot = mkdtempSync(join(tmpdir(), 'routing-guard-sub-'));
  const slug = basename(dirname(parentTranscript));
  const session = basename(parentTranscript, '.jsonl');
  const dir = join(tmpRoot, `claude-${process.getuid()}`, slug, session, 'tasks');
  mkdirSync(dir, { recursive: true });
  writeFileSync(join(dir, `${agentId}.output`), lines.map((l) => JSON.stringify(l)).join('\n') + '\n');
  return tmpRoot;
}

const readToolUse = (absPath) => ({
  type: 'assistant',
  message: { role: 'assistant', content: [{ type: 'tool_use', name: 'Read', input: { file_path: absPath } }] },
});

const repoRootAbs = join(repoRoot, '..', '..');
const wikiDoc = join(repoRootAbs, 'docs/guardrails/WIKI.md');
const codeDoc = join(repoRootAbs, 'docs/guardrails/CODE.md');

test('routing guard: denies a vault/ edit with no prior WIKI.md Read', () => {
  const transcript = writeTranscript([{ type: 'assistant', message: { role: 'assistant', content: [{ type: 'tool_use', name: 'Bash', input: { command: 'ls' } }] } }]);
  const out = runHook({ filePath: join(repoRootAbs, 'vault/campaigns/shattered-sea/npcs/test.md'), transcriptPath: transcript });
  assert.match(out, /"permissionDecision":\s*"deny"/);
  assert.match(out, /Read docs\/guardrails\/WIKI\.md first/);
  rmSync(dirname(transcript), { recursive: true, force: true });
});

test('routing guard: permits a vault/ edit after a prior WIKI.md Read', () => {
  const transcript = writeTranscript([readToolUse(wikiDoc)]);
  const out = runHook({ filePath: join(repoRootAbs, 'vault/campaigns/shattered-sea/npcs/test.md'), transcriptPath: transcript });
  assert.equal(out, '');
  rmSync(dirname(transcript), { recursive: true, force: true });
});

test('routing guard: denies a .mjs edit with no prior CODE.md Read', () => {
  const transcript = writeTranscript([{ type: 'assistant', message: { role: 'assistant', content: [{ type: 'tool_use', name: 'Bash', input: { command: 'ls' } }] } }]);
  const out = runHook({ filePath: join(repoRootAbs, 'utils/scripts/some-new-script.mjs'), transcriptPath: transcript });
  assert.match(out, /"permissionDecision":\s*"deny"/);
  assert.match(out, /Read docs\/guardrails\/CODE\.md first/);
  rmSync(dirname(transcript), { recursive: true, force: true });
});

test('routing guard: permits a .mjs edit after a prior CODE.md Read', () => {
  const transcript = writeTranscript([readToolUse(codeDoc)]);
  const out = runHook({ filePath: join(repoRootAbs, 'utils/scripts/some-new-script.mjs'), transcriptPath: transcript });
  assert.equal(out, '');
  rmSync(dirname(transcript), { recursive: true, force: true });
});

test('routing guard: permits an unrouted path (no WIKI/CODE row matches) regardless of transcript', () => {
  const transcript = writeTranscript([{ type: 'assistant', message: { role: 'assistant', content: [{ type: 'tool_use', name: 'Bash', input: { command: 'ls' } }] } }]);
  const out = runHook({ filePath: join(repoRootAbs, 'README.md'), transcriptPath: transcript });
  assert.equal(out, '');
  rmSync(dirname(transcript), { recursive: true, force: true });
});

// Subagent scoping (REFACTOR-PLAN.md P6.1). A hook payload from a subagent
// carries the PARENT's transcript_path and session_id — measured, not assumed.
// Checking the parent's transcript would hand every subagent the
// orchestrator's own WIKI.md read, which is the exact free pass this hook
// exists to close: an uncoached subagent is the population MIGRATION-LOG
// measured at 0/3 routing compliance.
test('routing guard: denies a subagent vault/ edit when the SUBAGENT never read WIKI.md, even though the parent did', () => {
  const parent = writeTranscript([readToolUse(wikiDoc)]);
  const tmpRoot = writeSubagentTranscript(parent, 'agent-noread', [
    { type: 'assistant', message: { role: 'assistant', content: [{ type: 'tool_use', name: 'Bash', input: { command: 'ls' } }] } },
  ]);
  const out = runHook({
    filePath: join(repoRootAbs, 'vault/campaigns/shattered-sea/npcs/test.md'),
    transcriptPath: parent,
    agentId: 'agent-noread',
    tmpRoot,
  });
  assert.match(out, /"permissionDecision":\s*"deny"/, 'the parent\'s read must not satisfy the subagent');
  rmSync(dirname(parent), { recursive: true, force: true });
  rmSync(tmpRoot, { recursive: true, force: true });
});

test('routing guard: permits a subagent vault/ edit when the SUBAGENT itself read WIKI.md', () => {
  const parent = writeTranscript([
    { type: 'assistant', message: { role: 'assistant', content: [{ type: 'tool_use', name: 'Bash', input: { command: 'ls' } }] } },
  ]);
  const tmpRoot = writeSubagentTranscript(parent, 'agent-didread', [readToolUse(wikiDoc)]);
  const out = runHook({
    filePath: join(repoRootAbs, 'vault/campaigns/shattered-sea/npcs/test.md'),
    transcriptPath: parent,
    agentId: 'agent-didread',
    tmpRoot,
  });
  assert.equal(out, '', 'a compliant subagent must not be blocked');
  rmSync(dirname(parent), { recursive: true, force: true });
  rmSync(tmpRoot, { recursive: true, force: true });
});

test('routing guard: fails open when a subagent transcript cannot be resolved', () => {
  // Deliberate relaxation: denying on an unresolvable path would block every
  // subagent edit the moment the harness renames a directory.
  const parent = writeTranscript([
    { type: 'assistant', message: { role: 'assistant', content: [{ type: 'tool_use', name: 'Bash', input: { command: 'ls' } }] } },
  ]);
  const tmpRoot = mkdtempSync(join(tmpdir(), 'routing-guard-empty-'));
  const out = runHook({
    filePath: join(repoRootAbs, 'vault/campaigns/shattered-sea/npcs/test.md'),
    transcriptPath: parent,
    agentId: 'agent-missing',
    tmpRoot,
  });
  assert.equal(out, '');
  rmSync(dirname(parent), { recursive: true, force: true });
  rmSync(tmpRoot, { recursive: true, force: true });
});

test('routing guard: a Read of WIKI.md earlier for a different edit still satisfies a later vault/ edit in the same session', () => {
  const transcript = writeTranscript([
    readToolUse(wikiDoc),
    { type: 'assistant', message: { role: 'assistant', content: [{ type: 'tool_use', name: 'Edit', input: { file_path: join(repoRootAbs, 'vault/campaigns/shattered-sea/npcs/first.md') } }] } },
  ]);
  const out = runHook({ filePath: join(repoRootAbs, 'vault/campaigns/shattered-sea/npcs/second.md'), transcriptPath: transcript });
  assert.equal(out, '');
  rmSync(dirname(transcript), { recursive: true, force: true });
});
