#!/usr/bin/env node
/**
 * Records every public URL into `site/url-baseline.json` so `check:urls` can prove none of them 404.
 * Run after `npm run build && npm run emit-legacy-stubs`. Entries are merged, never removed:
 * once a URL is public it must keep resolving (to a page or a redirect).
 */
import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SITE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const DIST = path.join(SITE, "dist");
const OUT = path.join(SITE, "url-baseline.json");
const SKIP = new Set(["_astro", "pagefind"]);

async function* routes(dir, rel = "") {
  for (const ent of await fs.readdir(dir, { withFileTypes: true })) {
    if (!ent.isDirectory() || SKIP.has(ent.name)) continue;
    const child = `${rel}/${ent.name}`;
    try {
      await fs.stat(path.join(dir, ent.name, "index.html"));
      yield `${child}/`;
    } catch {}
    yield* routes(path.join(dir, ent.name), child);
  }
}

const existing = await fs.readFile(OUT, "utf8").then(JSON.parse).catch(() => ({ routes: [], legacy: [] }));
const found = ["/"];
for await (const r of routes(DIST)) found.push(r);
const legacy = Object.keys(JSON.parse(await fs.readFile(path.join(SITE, "path-rewrite-map.json"), "utf8")));

const merged = {
  routes: [...new Set([...existing.routes, ...found])].sort(),
  legacy: [...new Set([...existing.legacy, ...legacy])].sort(),
};
await fs.writeFile(OUT, JSON.stringify(merged, null, 2) + "\n", "utf8");
console.log(`url-baseline.json: ${merged.routes.length} routes, ${merged.legacy.length} legacy URLs`);
