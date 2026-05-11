#!/usr/bin/env node
/**
 * emit-legacy-stubs.mjs
 *
 * Phase 5.2 — Legacy `.html` URL preservation.
 *
 * Reads `path-rewrite-map.json` (produced by `migrate.mjs`) and writes a
 * static HTML stub file into `dist/` at every legacy URL. Each stub:
 *
 *   - Returns HTTP 200 (it is a real file served by GitHub Pages)
 *   - Uses `<meta http-equiv="refresh">` to redirect browsers to the new slug
 *   - Carries `<link rel="canonical">` so search engines transfer link equity
 *   - Falls back to a visible `<a>` for clients that ignore meta-refresh
 *
 * Why static stubs rather than 404.astro JS bouncing:
 *   - 200 status preserves SEO ranking signals (no Soft 404)
 *   - No client-side JS dependency on the redirect path
 *   - The redirect resolves before Pagefind, social-share crawlers, or
 *     archive bots try to index the URL
 *
 * The script is idempotent. Re-running it overwrites stubs; deleting an
 * entry from `path-rewrite-map.json` does NOT auto-remove the matching
 * stub (call this script after a fresh `astro build` to get a clean set).
 *
 * Invoked by:
 *   npm --prefix site run emit-legacy-stubs        # one-off
 *   the Astro deploy workflow (post-build step)
 */

import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const SITE_ROOT = path.resolve(__dirname, "..");
const MAP_PATH = path.join(SITE_ROOT, "path-rewrite-map.json");
const DIST_DIR = path.join(SITE_ROOT, "dist");

// These must match `site` + `base` in astro.config.mjs.
const ASTRO_SITE = "https://jonathan-vella.github.io";
const ASTRO_BASE = "/microsoft-sovereign-cloud-brain-trek";

/**
 * Escape a string for safe HTML attribute / text content interpolation.
 * The slug values come from migrate.mjs and should already be safe, but
 * we belt-and-brace it because the output is shipped as-is to the browser.
 */
function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

/**
 * Render a single redirect stub. The format matches the spec in
 * `/memories/session/plan.md` § 5.2.
 */
function renderStub({ legacyHref, newHref, canonicalUrl }) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Redirecting&hellip;</title>
<meta http-equiv="refresh" content="0; url=${escapeHtml(newHref)}">
<link rel="canonical" href="${escapeHtml(canonicalUrl)}">
<meta name="robots" content="noindex, follow">
<style>
  body { font-family: 'Segoe UI', system-ui, sans-serif; max-width: 32rem; margin: 4rem auto; padding: 0 1rem; color: #1f2937; }
  a { color: #0078D4; }
</style>
</head>
<body>
<h1>This page has moved.</h1>
<p>
  The location previously served at
  <code>${escapeHtml(legacyHref)}</code>
  is now available at
  <a href="${escapeHtml(newHref)}">${escapeHtml(newHref)}</a>.
</p>
<p>You will be redirected automatically.</p>
</body>
</html>
`;
}

/**
 * The migration map keys are root-relative paths starting with `/`.
 * Both forms exist in the data:
 *   - "/level-100/foo.html"            → slug "/level-100/foo/"
 *   - "/level-100/README.html"         → slug "/level-100/"
 * We want to skip:
 *   - Keys whose target is identical to the legacy path (no-op)
 *   - Anything that doesn't look like an HTML file
 */
function isStubTarget(legacyKey, target) {
  if (!legacyKey || !target) return false;
  if (!legacyKey.startsWith("/")) return false;
  if (!legacyKey.toLowerCase().endsWith(".html")) return false;
  if (legacyKey === target) return false;
  return true;
}

async function ensureDir(dir) {
  await fs.mkdir(dir, { recursive: true });
}

async function distExists() {
  try {
    const stat = await fs.stat(DIST_DIR);
    return stat.isDirectory();
  } catch {
    return false;
  }
}

async function main() {
  if (!(await distExists())) {
    console.error(
      `emit-legacy-stubs: '${DIST_DIR}' does not exist. Run 'astro build' first.`,
    );
    process.exit(1);
  }

  let rawMap;
  try {
    rawMap = await fs.readFile(MAP_PATH, "utf8");
  } catch (err) {
    console.error(
      `emit-legacy-stubs: cannot read ${MAP_PATH}. Run 'npm run migrate' first.\n${err.message}`,
    );
    process.exit(1);
  }

  const map = JSON.parse(rawMap);
  const entries = Object.entries(map);

  let written = 0;
  let skipped = 0;
  let collisions = 0;

  for (const [legacyKey, target] of entries) {
    if (!isStubTarget(legacyKey, target)) {
      skipped++;
      continue;
    }

    // Strip the leading "/" so we can resolve against dist/.
    const relLegacy = legacyKey.replace(/^\//, "");
    const stubPath = path.join(DIST_DIR, relLegacy);

    // If `astro build` already produced a real HTML file at this path
    // (which shouldn't happen for a `.html` legacy URL given Starlight's
    // clean URLs), refuse to clobber it.
    try {
      const existing = await fs.readFile(stubPath, "utf8");
      // Only treat a file as a collision if it does NOT look like one of
      // our own stubs (so re-runs are idempotent).
      if (!existing.includes("legacy-stub-marker")) {
        collisions++;
        console.warn(
          `emit-legacy-stubs: refusing to overwrite non-stub file at ${stubPath}`,
        );
        continue;
      }
    } catch {
      // ENOENT — fine, we'll write a fresh stub below.
    }

    // The new slug is already root-relative (e.g. "/level-100/foo/"). Pages
    // serves us under ASTRO_BASE, so we prepend it to produce the absolute
    // path the browser should navigate to.
    const newHref = `${ASTRO_BASE}${target}`;
    const canonicalUrl = `${ASTRO_SITE}${newHref}`;

    const html = renderStub({
      legacyHref: `${ASTRO_BASE}${legacyKey}`,
      newHref,
      canonicalUrl,
    }).replace(
      "<head>",
      `<head>\n<!-- legacy-stub-marker: generated by site/scripts/emit-legacy-stubs.mjs -->`,
    );

    await ensureDir(path.dirname(stubPath));
    await fs.writeFile(stubPath, html, "utf8");
    written++;
  }

  console.log(`emit-legacy-stubs — wrote ${written} stub(s)`);
  console.log(`                   skipped ${skipped} non-HTML / no-op entries`);
  if (collisions > 0) {
    console.log(`                   ${collisions} collisions (non-stub files left in place)`);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
