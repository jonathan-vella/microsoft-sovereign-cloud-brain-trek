/**
 * build-sidebar.mjs
 *
 * Builds the Starlight sidebar from the folders under `src/content/docs/`, so new levels, modules,
 * and pages appear without editing config. Called once at config-load time from `astro.config.mjs`.
 *
 * Structure produced:
 *   Introduction
 *   Level NN group (level-NN/index title without "Level NN:", badge LNN)
 *     Overview (the level landing page)
 *     "N. Module title" group per module-NN-* folder (label from its index.md or index.mdx title)
 *       Overview (the module landing page), content pages, knowledge checks last
 *     Pages left at the level root (for example the Level 50 comprehensive knowledge check)
 *   Resources group (resources/ pages, then each level's visual specifications page)
 *
 * Ordering rules:
 *   - Levels and modules sort by the number in the folder name (`level-100`, `module-03-...`).
 *   - Inside a module: landing page first, then `sidebar.order`, then title. Pages whose file name
 *     contains `knowledge-check` always go last.
 *   - Pages with `sidebar.hidden: true` or `draft: true` are skipped.
 *
 * During the content rebuild some pages still sit at a level root while `redirects.json` already
 * records the module folder they will move to. Those pages are listed under that module now
 * (matched by module number), so navigation and prev/next follow the final outline before and
 * after the move. Once a page moves, its redirect activates and it is picked up from its folder.
 */
import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readRedirects } from "./redirects.mjs";

const CONTENT_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../src/content/docs");

const LEVEL_RE = /^level-(\d+)$/;
const MODULE_RE = /^module-(\d+)(?:-|$)/;
const PAGE_RE = /\.mdx?$/;
const KNOWLEDGE_CHECK_RE = /knowledge-check/;

/** Starlight badge variant per level. Unknown levels fall back to "default". */
const LEVEL_BADGE_VARIANTS = { 50: "note", 100: "tip", 200: "caution", 300: "danger" };

/** Proper nouns kept capitalized when a label has to be derived from a folder name. */
const PROPER_NOUNS = [
  "Microsoft 365 Local", "Sovereign Private Cloud", "Sovereign Public Cloud", "Sovereign Landing Zone",
  "Azure Local", "Azure Arc", "Foundry Local", "Zero Trust", "Azure", "Arc",
];

/** Read the keys the sidebar needs from a page's front matter. Returns null if the file is missing. */
async function readMeta(filePath) {
  let text;
  try {
    text = await fs.readFile(filePath, "utf8");
  } catch {
    return null;
  }
  const fm = text.startsWith("---") ? text.slice(3, Math.max(3, text.indexOf("\n---", 3))) : "";
  const top = (key) => fm.match(new RegExp(`^${key}\\s*:\\s*(.+?)\\s*$`, "m"))?.[1];
  const sidebar = fm.match(/^sidebar\s*:\s*\n((?:[ \t]+.*\n?)*)/m)?.[1] ?? "";
  const nested = (key) => sidebar.match(new RegExp(`^[ \\t]+${key}\\s*:\\s*(.+?)\\s*$`, "m"))?.[1];
  const unquote = (v) => v?.replace(/^(["'])(.*)\1$/, "$2");
  const order = nested("order");
  return {
    title: unquote(top("title")) ?? null,
    order: order !== undefined && /^-?\d+$/.test(order) ? Number(order) : null,
    hidden: nested("hidden") === "true" || top("draft") === "true",
  };
}

async function readDir(dir) {
  try {
    return await fs.readdir(dir, { withFileTypes: true });
  } catch {
    return [];
  }
}

/** Landing page of a folder: index.md or index.mdx. */
async function readIndex(dir) {
  for (const name of ["index.md", "index.mdx"]) {
    const meta = await readMeta(path.join(dir, name));
    if (meta) return meta;
  }
  return null;
}

/** Content pages (not the landing page) directly inside `dir`, as `{ slug, file, title, order }`. */
async function readPages(dir, slugPrefix) {
  const pages = [];
  for (const ent of await readDir(dir)) {
    if (!ent.isFile() || !PAGE_RE.test(ent.name) || /^index\.mdx?$/.test(ent.name)) continue;
    const meta = await readMeta(path.join(dir, ent.name));
    if (!meta || meta.hidden) continue;
    const name = ent.name.replace(PAGE_RE, "");
    pages.push({ slug: `${slugPrefix}/${name}`, name, title: meta.title ?? name, order: meta.order });
  }
  return pages;
}

function byPageOrder(a, b) {
  const kc = Number(KNOWLEDGE_CHECK_RE.test(a.name)) - Number(KNOWLEDGE_CHECK_RE.test(b.name));
  if (kc) return kc;
  const order = (a.order ?? Infinity) - (b.order ?? Infinity);
  if (order && !Number.isNaN(order)) return order;
  return a.title.localeCompare(b.title);
}

/** "module-02-sovereign-landing-zone" -> "Sovereign Landing Zone". Used only when no landing page exists yet. */
function labelFromFolder(folder) {
  let label = folder.replace(MODULE_RE, "").replace(/-/g, " ").trim();
  label = label.charAt(0).toUpperCase() + label.slice(1);
  for (const noun of PROPER_NOUNS) label = label.replace(new RegExp(`\\b${noun}\\b`, "i"), noun);
  return label;
}

/** "Module 3: Azure Local overview" (or "Module 3 - ...") -> "3. Azure Local overview". */
function moduleLabel(title, number, folder) {
  const name = title ? title.replace(/^module\s*\d+\s*[-:–—]\s*/i, "").trim() : labelFromFolder(folder);
  return `${number}. ${name}`;
}

/**
 * Read one level folder: its modules (with interim pages merged in), the pages left at its root,
 * and its visual specifications page.
 */
async function readLevel(levelDir, level, redirects) {
  const modules = new Map(); // module number -> { number, folder, title, hasIndex, overview, pages }

  for (const ent of await readDir(levelDir)) {
    const m = ent.isDirectory() && ent.name.match(MODULE_RE);
    if (!m) continue;
    const index = await readIndex(path.join(levelDir, ent.name));
    modules.set(Number(m[1]), {
      number: Number(m[1]),
      folder: ent.name,
      title: index?.title ?? null,
      overview: index && !index.hidden ? `${level}/${ent.name}` : null,
      pages: await readPages(path.join(levelDir, ent.name), `${level}/${ent.name}`),
    });
  }

  const rootPages = [];
  let visualSpecs = null;
  for (const page of await readPages(levelDir, level)) {
    if (page.name === "visual-specifications") {
      visualSpecs = page.slug;
      continue;
    }
    // Interim placement: follow the planned move recorded in redirects.json.
    const target = redirects[`/${page.slug}/`]?.match(new RegExp(`^/${level}/(module-(\\d+)[^/]*)/([^/]*)/?$`));
    if (!target) {
      rootPages.push(page);
      continue;
    }
    const [, folder, num, child] = target;
    const number = Number(num);
    if (!modules.has(number)) {
      modules.set(number, { number, folder, title: null, overview: null, pages: [] });
    }
    const mod = modules.get(number);
    if (!child && !mod.overview) {
      mod.overview = page.slug;
      mod.title = page.title;
    } else {
      mod.pages.push(page);
    }
  }

  return {
    modules: [...modules.values()].sort((a, b) => a.number - b.number),
    rootPages: rootPages.sort(byPageOrder),
    visualSpecs,
  };
}

function moduleItem(mod) {
  const items = [];
  if (mod.overview) items.push({ slug: mod.overview, label: "Overview" });
  for (const page of mod.pages.sort(byPageOrder)) items.push({ slug: page.slug });
  return { label: moduleLabel(mod.title, mod.number, mod.folder), collapsed: true, items };
}

/**
 * Build the full top-level Starlight sidebar configuration.
 *
 * @returns {Promise<any[]>}
 */
export async function buildSidebar() {
  const redirects = readRedirects();
  const levels = (await readDir(CONTENT_ROOT))
    .filter((ent) => ent.isDirectory() && LEVEL_RE.test(ent.name))
    .map((ent) => ({ name: ent.name, number: Number(ent.name.match(LEVEL_RE)[1]) }))
    .sort((a, b) => a.number - b.number);

  /** @type {any[]} */
  const sidebar = [];
  if (await readMeta(path.join(CONTENT_ROOT, "introduction.md"))) sidebar.push({ slug: "introduction" });

  const visualSpecs = [];
  for (const { name, number } of levels) {
    const levelDir = path.join(CONTENT_ROOT, name);
    const index = await readIndex(levelDir);
    const { modules, rootPages, visualSpecs: specs } = await readLevel(levelDir, name, redirects);
    const items = [];
    if (index && !index.hidden) items.push({ slug: name, label: "Overview" });
    for (const mod of modules) items.push(moduleItem(mod));
    for (const page of rootPages) items.push({ slug: page.slug });
    if (specs) visualSpecs.push({ slug: specs, label: `Level ${number} visual specifications` });

    sidebar.push({
      // The badge carries the level, so "Level 100: Foundation" shows as "Foundation [L100]".
      label: index?.title?.replace(/^level\s*\d+\s*[-:–—]\s*/i, "").trim() || `Level ${number}`,
      badge: { text: `L${number}`, variant: LEVEL_BADGE_VARIANTS[number] ?? "default" },
      collapsed: true,
      items,
    });
  }

  const resourcesDir = path.join(CONTENT_ROOT, "resources");
  const resourcesIndex = await readIndex(resourcesDir);
  const resources = [];
  if (resourcesIndex && !resourcesIndex.hidden) resources.push({ slug: "resources", label: "Overview" });
  for (const page of (await readPages(resourcesDir, "resources")).sort(byPageOrder)) resources.push({ slug: page.slug });
  resources.push(...visualSpecs);
  if (resources.length) sidebar.push({ label: "Resources", collapsed: true, items: resources });

  return sidebar;
}
