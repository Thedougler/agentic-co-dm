// ElevenLabs client construction + API-error normalization.
import { loadApiKey } from "./env.mjs";

export async function makeClient() {
  const apiKey = loadApiKey();
  const { ElevenLabsClient } = await import("@elevenlabs/elevenlabs-js");
  return new ElevenLabsClient({ apiKey });
}

/**
 * Turn an ElevenLabsError (statusCode + body) into an actionable one-liner.
 * @param {{statusCode?: number, body?: unknown, message?: string}} err
 * @returns {string}
 */
export function describeApiError(err) {
  const status = err?.statusCode;
  const detail = typeof err?.body === "string" ? err.body : JSON.stringify(err?.body ?? err?.message ?? "");
  if (status === 401) {
    return "ElevenLabs rejected the API key (401) — check ELEVENLABS_API_KEY in .env.local.";
  }
  if (status === 402 || detail.includes("quota_exceeded")) {
    return "ElevenLabs character quota exhausted — check the account's subscription before retrying.";
  }
  if (status === 422) {
    return `ElevenLabs rejected the request (422) — likely a bad voice id or malformed input; run the "voices" subcommand to list valid ids. Detail: ${detail}`;
  }
  if (status === 429) {
    return "ElevenLabs rate limit hit (429) — wait a moment and retry.";
  }
  return `ElevenLabs API error${status != null ? ` (${status})` : ""}: ${detail}`;
}
