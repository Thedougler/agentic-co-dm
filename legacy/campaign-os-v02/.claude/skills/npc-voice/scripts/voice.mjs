#!/usr/bin/env node
// npc-voice CLI — NPC dialogue audio via ElevenLabs.
// Commands: voices (free) | design ($) | create (free) | say ($).
// Run with no args for usage. API key: ELEVENLABS_API_KEY in repo-root .env.local.
import { mkdir, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { parseArgs } from "node:util";
import { loadApiKey } from "./lib/env.mjs";
import { describeApiError, makeClient } from "./lib/eleven.mjs";
import { writeAudioFile } from "./lib/output.mjs";

const DEFAULT_MODEL = "eleven_multilingual_v2";
const OUTPUT_FORMAT = "mp3_44100_128";

const USAGE = `npc-voice — NPC dialogue audio via ElevenLabs

Usage (from repo root: npm run voice -- <command> ...):
  voices [--search <q>]                          list account voices (free)
  design "<voice description>" [--text "<sample line>"] [--out <dir>]
                                                 generate voice previews ($; previews go to a
                                                 temp dir, NEVER the vault)
  create --name "<Name>" --description "<desc>" --generated-voice-id <id>
                                                 save a picked preview as a permanent voice (free)
  say --voice <voice_id> --text "<line>" --out <path>.mp3
      [--model ${DEFAULT_MODEL}] [--stability <0..1>] [--similarity <0..1>]
      [--dry-run] [--force]                      generate a dialogue clip ($)
`;

function fail(message) {
  console.error(message);
  process.exit(1);
}

async function cmdVoices(rest) {
  const { values } = parseArgs({ args: rest, options: { search: { type: "string" } } });
  const client = await makeClient();
  const res = await client.voices.search({ pageSize: 100, ...(values.search ? { search: values.search } : {}) });
  const voices = res.voices ?? [];
  if (voices.length === 0) {
    console.log("No voices found.");
    return;
  }
  console.log("voice_id\tname\tdescription");
  for (const v of voices) {
    const desc = v.description ?? Object.values(v.labels ?? {}).filter(Boolean).join(", ");
    console.log(`${v.voiceId}\t${v.name}\t${(desc ?? "").slice(0, 90)}`);
  }
}

async function cmdDesign(rest) {
  const { values, positionals } = parseArgs({
    args: rest,
    options: { out: { type: "string" }, text: { type: "string" } },
    allowPositionals: true,
  });
  const description = positionals[0];
  if (!description) fail(`design needs a voice description.\n\n${USAGE}`);
  const outDir = values.out ?? join(tmpdir(), `npc-voice-previews-${Date.now()}`);
  const client = await makeClient();
  const res = await client.textToVoice.design({
    voiceDescription: description,
    outputFormat: OUTPUT_FORMAT,
    ...(values.text ? { text: values.text } : { autoGenerateText: true }),
  });
  await mkdir(outDir, { recursive: true });
  console.log("preview\tgenerated_voice_id\tseconds");
  let i = 0;
  for (const p of res.previews) {
    i += 1;
    const file = join(outDir, `preview-${i}.mp3`);
    await writeFile(file, Buffer.from(p.audioBase64, "base64"));
    console.log(`${file}\t${p.generatedVoiceId}\t${typeof p.durationSecs === "number" ? p.durationSecs.toFixed(1) : "?"}`);
  }
  console.log(`\nSample text: ${res.text}`);
  console.log('Play the previews, pick one, then run: create --name "<Name>" --description "<desc>" --generated-voice-id <id>');
}

async function cmdCreate(rest) {
  const { values } = parseArgs({
    args: rest,
    options: {
      name: { type: "string" },
      description: { type: "string" },
      "generated-voice-id": { type: "string" },
    },
  });
  const { name, description } = values;
  const generatedVoiceId = values["generated-voice-id"];
  if (!name || !description || !generatedVoiceId) {
    fail(`create needs --name, --description and --generated-voice-id.\n\n${USAGE}`);
  }
  const client = await makeClient();
  const voice = await client.textToVoice.create({
    voiceName: name,
    voiceDescription: description,
    generatedVoiceId,
  });
  console.log(`Created voice "${name}" — voice_id: ${voice.voiceId}`);
  console.log("Record it in the NPC page frontmatter: voice_id + voice (description).");
}

async function cmdSay(rest) {
  const { values } = parseArgs({
    args: rest,
    options: {
      voice: { type: "string" },
      text: { type: "string" },
      out: { type: "string" },
      model: { type: "string", default: DEFAULT_MODEL },
      stability: { type: "string" },
      similarity: { type: "string" },
      "dry-run": { type: "boolean", default: false },
      force: { type: "boolean", default: false },
    },
  });
  const { voice, text, out } = values;
  if (!voice || !text || !out) fail(`say needs --voice, --text and --out.\n\n${USAGE}`);
  if (!out.endsWith(".mp3")) fail(`--out must end in .mp3 (got: ${out})`);

  const voiceSettings = {};
  for (const [flag, key] of [["stability", "stability"], ["similarity", "similarityBoost"]]) {
    if (values[flag] !== undefined) {
      const n = Number(values[flag]);
      if (Number.isNaN(n) || n < 0 || n > 1) fail(`--${flag} must be a number between 0 and 1 (got: ${values[flag]})`);
      voiceSettings[key] = n;
    }
  }

  const request = {
    text,
    modelId: values.model,
    outputFormat: OUTPUT_FORMAT,
    ...(Object.keys(voiceSettings).length > 0 ? { voiceSettings } : {}),
  };

  if (values["dry-run"]) {
    loadApiKey();
    console.log("DRY RUN — no API call, nothing written.");
    console.log(`Would call textToSpeech.convert(${JSON.stringify(voice)}, ${JSON.stringify(request)})`);
    console.log(`Would write: ${out}${values.force ? " (overwriting)" : ""}`);
    return;
  }

  const client = await makeClient();
  const audio = await client.textToSpeech.convert(voice, request);
  const bytes = await writeAudioFile(audio, out, { force: values.force });
  console.log(`Wrote ${out} (${bytes} bytes)`);
  console.log(`Embed it in the page: ![[${out.split("/").pop()}]]`);
}

const COMMANDS = { voices: cmdVoices, design: cmdDesign, create: cmdCreate, say: cmdSay };

const [command, ...rest] = process.argv.slice(2);
const handler = COMMANDS[command];
if (!handler) fail(USAGE);

try {
  await handler(rest);
} catch (err) {
  if (err && typeof err === "object" && "statusCode" in err) {
    fail(describeApiError(err));
  }
  fail(err instanceof Error ? err.message : String(err));
}
