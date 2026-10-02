#!/usr/bin/env node
/**
 * Lints content under src/content/docs.
 *
 * Errors (always fail):
 *   - hard-coded base path in a page body (write `/images/...` or `/level-100/...`; the build adds the base)
 *   - `lastVerified` present but not YYYY-MM-DD
 * Metadata checks (fail with --strict, which `npm run lint:content` and CI use; warn without it):
 *   - missing `lastVerified`
 *   - missing `## Sources` section
 *   - Sources links outside the allowed Microsoft domains
 * Writing checks from the unslop skill (warn only, never fail):
 *   - em dashes, emoji in headings or bullets, banned words
 *
 * Usage: node scripts/lint-content.mjs [--strict] [--verbose]
 */
import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { BASE } from "./site-constants.mjs";

const SITE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const DOCS = path.join(SITE, "src", "content", "docs");
const strict = process.argv.includes("--strict");
const verbose = process.argv.includes("--verbose");

const ALLOWED_SOURCE_HOSTS = [
  "learn.microsoft.com",
  "azure.microsoft.com",
  "blogs.microsoft.com",
  "news.microsoft.com",
  "techcommunity.microsoft.com",
  "www.microsoft.com",
  "microsoft.com",
  "servicetrust.microsoft.com",
  "aka.ms",
  "github.com", // only github.com/Azure and github.com/microsoft, checked below
];
const ALLOWED_GITHUB_ORGS = ["azure", "microsoft"];

const BANNED = [
  "delve", "crucial", "pivotal", "tapestry", "testament", "underscores?", "vibrant", "showcas(?:e|es|ing)",
  "seamless(?:ly)?", "leverag(?:e|es|ed|ing)", "utiliz(?:e|es|ed|ing)", "robust", "cutting-edge", "game-changer",
  "realm", "embark", "foster(?:s|ing)?", "garner", "intricate", "interplay", "paradigm", "synergy", "holistic",
  "in order to", "it is important to note",
];
const BANNED_RE = new RegExp(`\\b(${BANNED.join("|")})\\b`, "gi");
const EMOJI_RE = /\p{Extended_Pictographic}/u;

async function* walk(dir) {
  for (const ent of await fs.readdir(dir, { withFileTypes: true })) {
    const full = path.join(dir, ent.name);
    if (ent.isDirectory()) yield* walk(full);
    else if (/\.mdx?$/.test(ent.name)) yield full;
  }
}

function split(text) {
  if (!text.startsWith("---")) return { fm: "", body: text };
  const end = text.indexOf("\n---", 3);
  return end === -1 ? { fm: "", body: text } : { fm: text.slice(3, end), body: text.slice(end + 4) };
}

const errors = [];
const meta = { lastVerified: [], sources: [], domains: [] };
const style = { emDash: 0, emoji: 0, banned: 0, files: new Set(), detail: [] };
let files = 0;

for await (const file of walk(DOCS)) {
  files++;
  const rel = path.relative(DOCS, file).split(path.sep).join("/");
  const { fm, body } = split(await fs.readFile(file, "utf8"));

  if (new RegExp(`(^|[\\s("'=])${BASE}/`).test(body)) errors.push(`${rel}: hard-coded base path "${BASE}/" in page body`);

  const lv = fm.match(/^lastVerified:\s*["']?([^"'\s]+)["']?\s*$/m);
  if (!lv) meta.lastVerified.push(rel);
  else if (!/^\d{4}-\d{2}-\d{2}$/.test(lv[1])) errors.push(`${rel}: lastVerified "${lv[1]}" is not YYYY-MM-DD`);

  const src = body.match(/^##\s+Sources\s*$([\s\S]*?)(?=^##\s|(?![\s\S]))/m);
  if (!src) meta.sources.push(rel);
  else {
    for (const [url] of src[1].matchAll(/https?:\/\/[^\s)>\]"']+/g)) {
      const u = new URL(url);
      const host = u.hostname.toLowerCase();
      const okHost = ALLOWED_SOURCE_HOSTS.includes(host);
      const okGithub = host !== "github.com" || ALLOWED_GITHUB_ORGS.includes(u.pathname.split("/")[1]?.toLowerCase());
      if (!okHost || !okGithub) meta.domains.push(`${rel}: ${url}`);
    }
  }

  const prose = body.replace(/^(```|~~~)[\s\S]*?^\1/gm, "");
  const before = style.emDash + style.emoji + style.banned;
  for (const line of prose.split("\n")) {
    const dashes = (line.match(/—/g) || []).length;
    style.emDash += dashes;
    if (/^\s*(#{1,6}\s|[-*+]\s|\d+\.\s)/.test(line) && EMOJI_RE.test(line)) style.emoji++;
    const hits = line.match(BANNED_RE) || [];
    style.banned += hits.length;
    if (verbose && (dashes || hits.length)) style.detail.push(`${rel}: ${[dashes ? `${dashes} em dash` : "", ...hits].filter(Boolean).join(", ")}`);
  }
  if (style.emDash + style.emoji + style.banned > before) style.files.add(rel);
}

const report = (label, list) => {
  if (!list.length) return;
  console.log(`  ${strict ? "error" : "warn "} ${list.length} ${label}`);
  if (verbose || strict) list.forEach((x) => console.log(`        ${x}`));
};

console.log(`lint-content: ${files} files${strict ? " (strict)" : ""}`);
errors.forEach((e) => console.log(`  error ${e}`));
report("page(s) without lastVerified", meta.lastVerified);
report("page(s) without a ## Sources section", meta.sources);
report("Sources link(s) outside allowed Microsoft domains", meta.domains);
console.log(
  `  style (unslop, warn only): ${style.emDash} em dashes, ${style.emoji} emoji headings/bullets, ` +
    `${style.banned} banned words across ${style.files.size} file(s)`,
);
if (verbose) style.detail.forEach((d) => console.log(`        ${d}`));

const metaCount = meta.lastVerified.length + meta.sources.length + meta.domains.length;
if (errors.length || (strict && metaCount)) {
  console.log(`lint-content: FAILED`);
  process.exit(1);
}
console.log("lint-content: OK");
