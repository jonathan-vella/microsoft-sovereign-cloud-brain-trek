/**
 * Loads `site/redirects.json` (old clean route -> new clean route) for Astro's `redirects` option.
 *
 * Rules:
 * - Entries are never removed. To change a destination, edit the value.
 * - A redirect is active only once its source page is gone, so the file can list planned moves
 *   before the content moves. Moving or deleting the page activates the redirect automatically.
 * - Destinations must be final pages (no chains). `npm run check:urls` enforces this after a build.
 */
import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { withBase } from "./site-constants.mjs";

const SITE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const DOCS = path.join(SITE, "src", "content", "docs");

export function readRedirects() {
  return JSON.parse(readFileSync(path.join(SITE, "redirects.json"), "utf8"));
}

export function pageExists(route) {
  const rel = route.replace(/^\/|\/$/g, "");
  const candidates = rel
    ? [`${rel}.md`, `${rel}.mdx`, `${rel}/index.md`, `${rel}/index.mdx`]
    : ["index.md", "index.mdx"];
  return candidates.some((c) => existsSync(path.join(DOCS, c)));
}

/**
 * Redirects whose source page no longer exists, keyed without the trailing slash as Astro expects.
 * @returns {Record<string, string>}
 */
export function activeRedirects() {
  /** @type {Record<string, string>} */
  const out = {};
  for (const [from, to] of Object.entries(readRedirects())) {
    // Astro does not add `base` to redirect destinations.
    if (!pageExists(from)) out[from.replace(/\/$/, "")] = withBase(to);
  }
  return out;
}

/** Follow redirects.json from a route to its final destination. */
export function resolveRoute(route, redirects = readRedirects()) {
  const seen = new Set();
  let current = route;
  while (redirects[current] && !pageExists(current)) {
    if (seen.has(current)) throw new Error(`Redirect cycle at ${current}`);
    seen.add(current);
    current = redirects[current];
  }
  return current;
}
