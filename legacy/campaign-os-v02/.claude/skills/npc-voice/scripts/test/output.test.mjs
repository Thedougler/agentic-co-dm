import assert from "node:assert/strict";
import { mkdtempSync, readFileSync, existsSync, readdirSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { Readable } from "node:stream";
import { test } from "node:test";
import { writeAudioFile } from "../lib/output.mjs";

const dir = () => mkdtempSync(join(tmpdir(), "npc-voice-out-"));

test("writes stream to a nested path, creating dialogue/ dirs", async () => {
  const out = join(dir(), "dialogue", "thunk-no-refunds.mp3");
  const bytes = await writeAudioFile(Readable.from([Buffer.from("abc"), Buffer.from("def")]), out);
  assert.equal(bytes, 6);
  assert.equal(readFileSync(out, "utf8"), "abcdef");
});

test("refuses to overwrite without force", async () => {
  const out = join(dir(), "clip.mp3");
  await writeAudioFile(Readable.from([Buffer.from("v1")]), out);
  await assert.rejects(writeAudioFile(Readable.from([Buffer.from("v2")]), out), /--force/);
  assert.equal(readFileSync(out, "utf8"), "v1");
  await writeAudioFile(Readable.from([Buffer.from("v2")]), out, { force: true });
  assert.equal(readFileSync(out, "utf8"), "v2");
});

test("failed stream leaves no partial file and no tmp litter", async () => {
  const d = dir();
  const out = join(d, "clip.mp3");
  const broken = new Readable({
    read() {
      this.destroy(new Error("network died"));
    },
  });
  await assert.rejects(writeAudioFile(broken, out), /network died/);
  assert.equal(existsSync(out), false);
  assert.deepEqual(readdirSync(d), []);
});
