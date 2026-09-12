import assert from "node:assert/strict";
import { test } from "node:test";
import { describeApiError } from "../lib/eleven.mjs";

test("401 → bad key message naming .env.local", () => {
  assert.match(describeApiError({ statusCode: 401 }), /API key.*\.env\.local/);
});

test("402 → quota message", () => {
  assert.match(describeApiError({ statusCode: 402 }), /quota/);
});

test("quota_exceeded in body → quota message regardless of status", () => {
  assert.match(describeApiError({ statusCode: 400, body: { detail: { status: "quota_exceeded" } } }), /quota/);
});

test("422 → suggests the voices subcommand", () => {
  assert.match(describeApiError({ statusCode: 422, body: "bad voice" }), /voices.*subcommand|"voices"/);
});

test("429 → rate limit message", () => {
  assert.match(describeApiError({ statusCode: 429 }), /rate limit/i);
});

test("unknown error carries status and detail through", () => {
  assert.match(describeApiError({ statusCode: 500, body: "boom" }), /500.*boom/);
});
