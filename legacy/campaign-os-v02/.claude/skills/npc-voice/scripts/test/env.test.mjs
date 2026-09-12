import assert from "node:assert/strict";
import { readFileSync, mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { test, beforeEach, afterEach } from "node:test";
import { loadApiKey, repoRoot } from "../lib/env.mjs";

let savedKey;
beforeEach(() => {
  savedKey = process.env.ELEVENLABS_API_KEY;
  delete process.env.ELEVENLABS_API_KEY;
});
afterEach(() => {
  if (savedKey === undefined) delete process.env.ELEVENLABS_API_KEY;
  else process.env.ELEVENLABS_API_KEY = savedKey;
});

test("repoRoot resolves to the campaign-os repo root", () => {
  const pkg = JSON.parse(readFileSync(join(repoRoot, "package.json"), "utf8"));
  assert.equal(pkg.name, "campaign-os-tooling");
});

test("throws an actionable error when the key is nowhere", () => {
  assert.throws(
    () => loadApiKey({ envFile: join(tmpdir(), "npc-voice-no-such-file.env") }),
    /ELEVENLABS_API_KEY is not set.*\.env\.local/,
  );
});

test("reads the key from the env file", () => {
  const dir = mkdtempSync(join(tmpdir(), "npc-voice-env-"));
  const envFile = join(dir, ".env.local");
  writeFileSync(envFile, "ELEVENLABS_API_KEY=test-key-123\n");
  try {
    assert.equal(loadApiKey({ envFile }), "test-key-123");
  } finally {
    delete process.env.ELEVENLABS_API_KEY;
    rmSync(dir, { recursive: true, force: true });
  }
});

test("an already-set shell env var wins over the file", () => {
  process.env.ELEVENLABS_API_KEY = "from-shell";
  assert.equal(loadApiKey({ envFile: join(tmpdir(), "npc-voice-no-such-file.env") }), "from-shell");
});
