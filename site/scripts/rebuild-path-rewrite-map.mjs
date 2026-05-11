#!/usr/bin/env node
/**
 * rebuild-path-rewrite-map.mjs
 *
 * Phase 6 cutover side-effect — the original migrate.mjs would emit
 * `site/path-rewrite-map.json` (legacy `.html` URL → new Starlight slug)
 * by walking the source tree under `docs/`. Phase 6 deleted `docs/`, so
 * the map is no longer regenerable from source.
 *
 * This script regenerates an equivalent map by walking the built
 * `dist/` tree and computing each canonical route's flat legacy URL —
 * which is `<level>/<leaf-basename>.html`, mirroring the original
 * Jekyll layout where every page lived directly under its `level-XX/`
 * directory (no module-NN subfolders).
 *
 * Run this whenever you add or remove pages so `emit-legacy-stubs.mjs`
 * keeps the legacy URLs covered. The output is checked in so the build
 * does not need `docs/` to recreate it.
 */

import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const SITE = path.resolve(__dirname, "..");
const DIST = path.join(SITE, "dist");
const OUT = path.join(SITE, "path-rewrite-map.json");

/**
 * Walk dist/, collect every directory that contains an `index.html`.
 * Each one is a canonical Starlight route.
 */
async function* canonicalRoutes(dir, base = "") {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  for (const ent of entries) {
    if (!ent.isDirectory()) continue;
    // Skip Starlight infrastructure folders.
    if (ent.name === "_astro" || ent.name === "pagefind") continue;
    const full = path.join(dir, ent.name);
    const route = base ? `${base}/${ent.name}` : ent.name;
    const indexFile = path.join(full, "index.html");
    try {
      await fs.stat(indexFile);
      yield route;
    } catch {
      // Directory without an index.html; recurse — it's a route container.
    }
    yield* canonicalRoutes(full, route);
  }
}

/**
 * Compute the flat Jekyll-style legacy URL for a canonical route.
 *   - top-level "index" route → "/" (no stub; the splash already lives at /)
 *   - "level-100"               → "/level-100/README.html"
 *   - "level-100/module-04-azure-arc"
 *                               → "/level-100/module-04-azure-arc.html"  (was a module overview page)
 *   - "level-100/module-04-azure-arc/azure-arc-intro"
 *                               → "/level-100/azure-arc-intro.html"      (flat under its level)
 *   - "introduction"            → "/introduction.html"
 *   - "level-50/comprehensive-knowledge-check"
 *                               → "/level-50/comprehensive-knowledge-check.html"
 */
function legacyUrlForRoute(route) {
  const parts = route.split("/");
  // top-level: introduction
  if (parts.length === 1 && parts[0] === "") return null;
  if (parts.length === 1) {
    return `/${parts[0]}.html`;
  }
  // level only: /level-100/README.html
  if (parts.length === 1 || parts.length === 0) return null;
  const level = parts[0];
  if (parts.length === 2 && parts[1].startsWith("module-")) {
    return `/${level}/${parts[1]}.html`;
  }
  if (parts.length === 1) return `/${level}/README.html`;
  // bare-leaf under a level (no module folder)
  if (parts.length === 2) {
    return `/${level}/${parts[1]}.html`;
  }
  // module-nested: drop the module segment
  // /level-100/module-04-azure-arc/azure-arc-intro → /level-100/azure-arc-intro.html
  const leaf = parts[parts.length - 1];
  return `/${level}/${leaf}.html`;
}

async function main() {
  const map = {};
  // Special-case top-level paths.
  map["/introduction.html"] = "/introduction/";
  for (const lvl of ["level-50", "level-100", "level-200", "level-300", "resources"]) {
    map[`/${lvl}/README.html`] = `/${lvl}/`;
  }
  // Original Jekyll uppercase URLs that the new Starlight build emits as
  // lowercase kebab-case slugs. Without these aliases the legacy bookmarks
  // would 404. The Jekyll site shipped these files at uppercase + underscore
  // paths (mirroring the source filename `VISUAL_SPECIFICATIONS.md`); the
  // Astro build slugifies them to lowercase kebab-case.
  const aliases = {
    "/level-100/VISUAL_SPECIFICATIONS.html": "/level-100/visual-specifications/",
    "/level-200/VISUAL_SPECIFICATIONS.html": "/level-200/visual-specifications/",
    "/level-300/VISUAL_SPECIFICATIONS.html": "/level-300/visual-specifications/",
  };
  Object.assign(map, aliases);

  for await (const route of canonicalRoutes(DIST)) {
    if (route === "" || route === "/") continue;
    // Skip top-level non-level routes that already got special cases above
    // (e.g., "introduction").
    if (route === "introduction") continue;
    // level-XX top-level alone is handled by the README mapping above.
    const parts = route.split("/");
    if (parts.length === 1) continue;
    const legacy = legacyUrlForRoute(route);
    if (!legacy) continue;
    const target = `/${route}/`;
    // First entry wins (so a flat /level-100/foo.html doesn't clobber a more
    // specific module page). In practice every leaf basename was unique under
    // its level in the original Jekyll tree, so collisions only happen for
    // legitimate aliases; keep the first.
    if (!(legacy in map)) {
      map[legacy] = target;
    }
  }

  const sorted = Object.fromEntries(
    Object.entries(map).sort(([a], [b]) => a.localeCompare(b)),
  );
  await fs.writeFile(OUT, JSON.stringify(sorted, null, 2) + "\n", "utf8");
  console.log(`Wrote ${Object.keys(sorted).length} entries to ${OUT}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
