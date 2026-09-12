// Safe audio-stream-to-file: tmp+rename so a failed request never leaves a
// partial mp3, mkdir -p for dialogue/ subfolders, overwrite guard because
// regenerating costs credits.
import { createWriteStream } from "node:fs";
import { mkdir, rename, rm, stat } from "node:fs/promises";
import { dirname } from "node:path";
import { Readable } from "node:stream";
import { pipeline } from "node:stream/promises";

async function fileExists(path) {
  try {
    await stat(path);
    return true;
  } catch {
    return false;
  }
}

/**
 * @param {Readable | ReadableStream<Uint8Array>} audio
 * @param {string} outPath
 * @param {{force?: boolean}} [opts]
 * @returns {Promise<number>} bytes written
 */
export async function writeAudioFile(audio, outPath, { force = false } = {}) {
  if (!force && (await fileExists(outPath))) {
    throw new Error(`${outPath} already exists — pass --force to overwrite (regenerating costs credits).`);
  }
  await mkdir(dirname(outPath), { recursive: true });
  const tmp = `${outPath}.tmp`;
  const stream = audio instanceof Readable ? audio : Readable.fromWeb(audio);
  try {
    await pipeline(stream, createWriteStream(tmp));
    await rename(tmp, outPath);
  } catch (err) {
    await rm(tmp, { force: true });
    throw err;
  }
  return (await stat(outPath)).size;
}
