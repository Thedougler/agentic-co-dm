// Repo-root resolution + API-key loading for the npc-voice CLI.
import { join } from "node:path";

// scripts/lib → scripts → npc-voice → skills → .claude → repo root
export const repoRoot = join(import.meta.dirname, "..", "..", "..", "..", "..");

/**
 * Load ELEVENLABS_API_KEY — shell env wins, else .env.local at the repo root.
 * @param {{envFile?: string}} [opts]
 * @returns {string}
 */
export function loadApiKey({ envFile = join(repoRoot, ".env.local") } = {}) {
  if (!process.env.ELEVENLABS_API_KEY) {
    try {
      process.loadEnvFile(envFile);
    } catch {
      // absent file is fine — the key may come from the shell
    }
  }
  const key = process.env.ELEVENLABS_API_KEY;
  if (!key) {
    throw new Error(
      "ELEVENLABS_API_KEY is not set — add it to .env.local at the repo root (see .env.example).",
    );
  }
  return key;
}
