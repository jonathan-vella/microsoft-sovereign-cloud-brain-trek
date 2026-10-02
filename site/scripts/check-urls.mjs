#!/usr/bin/env node
/**
 * Post-build URL guard. Run after `npm run build && npm run emit-legacy-stubs`.
 *
 * Fails when:
 * - a URL in url-baseline.json no longer resolves (no page, no redirect)
 * - a redirect points outside the base path, at a missing page, or at another redirect (chain/cycle)
 * - a link or image in any built page points at a missing file, or is root-relative without the base path
 *
 * Warns (with --verbose, lists them) when a page links to an old URL that only resolves through a redirect.
 */
import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { BASE } from "./site-constants.mjs";

const SITE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const DIST = path.join(SITE, "dist");
const verbose = process.argv.includes("--verbose");
const errors = [];
const warnings = [];

const fileFor = (p) =>
  p.endsWith("/") ? path.join(DIST, p, "index.html") : path.extname(p) ? path.join(DIST, p) : path.join(DIST, p, "index.html");

const read = (f) => fs.readFile(f, "utf8").catch(() => null);

function refreshTarget(html) {
  const m =
    html.match(/<meta[^>]+http-equiv=["']?refresh["']?[^>]+content=["']\s*\d+\s*;\s*url=([^"']+)["']/i) ??
    html.match(/<meta[^>]+content=["']\s*\d+\s*;\s*url=([^"']+)["'][^>]+http-equiv=["']?refresh/i);
  return m ? m[1].trim() : null;
}

const cache = new Map();
/** Follow meta-refresh redirects from a base-less path. Returns { ok, hops, final, reason }. */
async function resolve(p) {
  if (cache.has(p)) return cache.get(p);
  const seen = new Set();
  let current = p;
  let hops = 0;
  let result;
  for (;;) {
    const html = await read(fileFor(current));
    if (html === null) {
      result = { ok: false, hops, reason: hops ? `redirect target ${current} does not exist` : "not found" };
      break;
    }
    const target = path.extname(current) && !current.endsWith(".html") ? null : refreshTarget(html);
    if (!target) {
      result = { ok: true, hops, final: current };
      break;
    }
    if (!target.startsWith(`${BASE}/`)) {
      result = { ok: false, hops, reason: `redirect to ${target} is missing the base path` };
      break;
    }
    seen.add(current);
    current = decodeURI(target.slice(BASE.length).split(/[?#]/)[0]);
    hops++;
    if (seen.has(current)) {
      result = { ok: false, hops, reason: `redirect cycle at ${current}` };
      break;
    }
  }
  cache.set(p, result);
  return result;
}

// 1. Every baseline URL resolves to a real page in at most one redirect.
const baseline = JSON.parse(await fs.readFile(path.join(SITE, "url-baseline.json"), "utf8"));
for (const url of [...baseline.routes, ...baseline.legacy]) {
  const r = await resolve(url);
  if (!r.ok) errors.push(`baseline ${url}: ${r.reason}`);
  else if (r.hops > 1) errors.push(`baseline ${url}: redirect chain (${r.hops} hops) ending at ${r.final}`);
}

// 2. Every internal link and image in built pages resolves.
async function* htmlFiles(dir) {
  for (const ent of await fs.readdir(dir, { withFileTypes: true })) {
    const full = path.join(dir, ent.name);
    if (ent.isDirectory()) {
      if (ent.name !== "_astro" && ent.name !== "pagefind") yield* htmlFiles(full);
    } else if (ent.name.endsWith(".html")) yield full;
  }
}

const SKIP = /^(https?:|mailto:|tel:|data:|javascript:|#|\/\/)/i;
let pages = 0;
let links = 0;
for await (const file of htmlFiles(DIST)) {
  const html = await read(file);
  if (refreshTarget(html)) continue;
  pages++;
  const rel = "/" + path.relative(DIST, file).split(path.sep).join("/");
  const pageUrl = BASE + rel.replace(/index\.html$/, "");
  const page = rel.replace(/index\.html$/, "");
  for (const m of html.matchAll(/\s(?:href|src)=["']([^"']+)["']/g)) {
    const raw = m[1];
    if (SKIP.test(raw)) continue;
    links++;
    const pathname = decodeURI(new URL(raw, `https://x${pageUrl}`).pathname);
    if (pathname !== BASE && !pathname.startsWith(`${BASE}/`)) {
      errors.push(`${page}: link "${raw}" is missing the base path`);
      continue;
    }
    const target = pathname.slice(BASE.length) || "/";
    const r = await resolve(target);
    if (!r.ok) errors.push(`${page}: broken link "${raw}" (${r.reason})`);
    else if (r.hops > 0) warnings.push(`${page}: links to old URL ${target} (redirects to ${r.final})`);
  }
}

const uniq = (a) => [...new Set(a)];
const errs = uniq(errors);
const warns = uniq(warnings);
console.log(`check-urls: ${baseline.routes.length + baseline.legacy.length} baseline URLs, ${pages} pages, ${links} links`);
if (warns.length) {
  console.log(`  ${warns.length} warning(s): links to redirected URLs${verbose ? "" : " (use --verbose to list)"}`);
  if (verbose) warns.forEach((w) => console.log(`  warn  ${w}`));
}
if (errs.length) {
  errs.slice(0, verbose ? errs.length : 100).forEach((e) => console.log(`  error ${e}`));
  if (!verbose && errs.length > 100) console.log(`  ... and ${errs.length - 100} more (use --verbose)`);
  console.log(`check-urls: FAILED with ${errs.length} error(s)`);
  process.exit(1);
}
console.log("check-urls: OK");
