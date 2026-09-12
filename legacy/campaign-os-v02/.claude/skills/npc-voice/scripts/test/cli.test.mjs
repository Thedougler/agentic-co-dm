import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { existsSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { test } from "node:test";

const CLI = join(import.meta.dirname, "..", "voice.mjs");

function run(args, env = {}) {
  try {
    const stdout = execFileSync(process.execPath, [CLI, ...args], {
      encoding: "utf8",
      env: { ...process.env, ...env },
    });
    return { code: 0, stdout, stderr: "" };
  } catch (err) {
    return { code: err.status, stdout: err.stdout ?? "", stderr: err.stderr ?? "" };
  }
}

test("no args → usage on stderr, exit 1", () => {
  const res = run([]);
  assert.equal(res.code, 1);
  assert.match(res.stderr, /Usage/);
});

test("unknown command → usage, exit 1", () => {
  const res = run(["shout"]);
  assert.equal(res.code, 1);
  assert.match(res.stderr, /Usage/);
});

test("say without required flags → exit 1 naming them", () => {
  const res = run(["say", "--text", "hi"], { ELEVENLABS_API_KEY: "fake" });
  assert.equal(res.code, 1);
  assert.match(res.stderr, /--voice, --text and --out/);
});

test("say rejects non-mp3 output", () => {
  const res = run(["say", "--voice", "v1", "--text", "hi", "--out", "clip.wav"], { ELEVENLABS_API_KEY: "fake" });
  assert.equal(res.code, 1);
  assert.match(res.stderr, /must end in \.mp3/);
});

test("say rejects out-of-range stability", () => {
  const res = run(["say", "--voice", "v1", "--text", "hi", "--out", "c.mp3", "--stability", "2"], {
    ELEVENLABS_API_KEY: "fake",
  });
  assert.equal(res.code, 1);
  assert.match(res.stderr, /--stability must be a number between 0 and 1/);
});

test("say --dry-run prints the planned call and writes nothing", () => {
  const out = join(mkdtempSync(join(tmpdir(), "npc-voice-cli-")), "dialogue", "thunk-test.mp3");
  const res = run(
    ["say", "--voice", "v1", "--text", "No refunds.", "--out", out, "--stability", "0.4", "--dry-run"],
    { ELEVENLABS_API_KEY: "fake" },
  );
  assert.equal(res.code, 0);
  assert.match(res.stdout, /DRY RUN/);
  assert.match(res.stdout, /textToSpeech\.convert\("v1"/);
  assert.match(res.stdout, /"stability":0\.4/);
  assert.equal(existsSync(out), false);
});

test("design without a description → exit 1", () => {
  const res = run(["design"], { ELEVENLABS_API_KEY: "fake" });
  assert.equal(res.code, 1);
  assert.match(res.stderr, /voice description/);
});

test("create without flags → exit 1 naming them", () => {
  const res = run(["create", "--name", "X"], { ELEVENLABS_API_KEY: "fake" });
  assert.equal(res.code, 1);
  assert.match(res.stderr, /--name, --description and --generated-voice-id/);
});
