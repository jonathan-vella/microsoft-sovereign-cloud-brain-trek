/**
 * build-sidebar.mjs
 *
 * Reads `site/src/content/docs/<level>/` and produces a Starlight sidebar
 * `items` array. The default `autogenerate` config labels every group with
 * the literal folder name, so `module-01-cloud-computing/` shows up in the
 * sidebar as "module-01-cloud-computing" instead of the nicely-formatted
 * "Module 1 — Cloud Computing Fundamentals" that lives in the folder's
 * `index.md` front matter.
 *
 * This helper walks the level directory, detects subdirectories starting
 * with `module-`, reads their `index.md` to extract the `title`, and emits
 * an explicit group for each. Flat pages and the level overview are still
 * picked up via `autogenerate` of the level root with a sub-directory
 * filter — but Starlight does not have a built-in "autogenerate but skip
 * folders" option, so we list flat pages explicitly as `slug` entries.
 *
 * The function is called at config-load time from `astro.config.mjs`.
 */
import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const CONTENT_ROOT = path.resolve(__dirname, "../src/content/docs");

/**
 * Parse a minimal `title:` value out of the front matter at the top of a
 * Markdown/MDX file. Avoids pulling in a full YAML parser — front matter
 * here is hand-authored and the `title` field is consistently quoted or
 * bare on its own line.
 */
async function readFrontMatterTitle(filePath) {
  let text;
  try {
    text = await fs.readFile(filePath, "utf8");
  } catch {
    return null;
  }
  if (!text.startsWith("---")) return null;
  const end = text.indexOf("\n---", 3);
  if (end === -1) return null;
  const fm = text.slice(3, end);
  const line = fm.split("\n").find((l) => /^title\s*:/.test(l));
  if (!line) return null;
  let value = line.replace(/^title\s*:\s*/, "").trim();
  // Strip surrounding quotes if present.
  if (
    (value.startsWith('"') && value.endsWith('"')) ||
    (value.startsWith("'") && value.endsWith("'"))
  ) {
    value = value.slice(1, -1);
  }
  return value || null;
}

/**
 * Read `sidebar.order` from front matter (used by Starlight to sort items
 * within a group). Returns `null` if not present.
 */
async function readFrontMatterOrder(filePath) {
  let text;
  try {
    text = await fs.readFile(filePath, "utf8");
  } catch {
    return null;
  }
  if (!text.startsWith("---")) return null;
  const end = text.indexOf("\n---", 3);
  if (end === -1) return null;
  const fm = text.slice(3, end);
  // Look for `sidebar:` block followed by `  order: N`
  const m = fm.match(/sidebar\s*:\s*\n(?:[ \t]+[a-z_]+\s*:.*\n?)*?[ \t]+order\s*:\s*(\d+)/);
  return m ? Number(m[1]) : null;
}

/**
 * Build the items array for one level (level-50, level-100, etc.).
 *
 * Layout produced:
 *   [
 *     { slug: 'level-50' },                                  // overview
 *     { label: 'Module 1 — Cloud Computing', autogenerate: { directory: 'level-50/module-01-cloud-computing' }, collapsed: true },
 *     { label: 'Module 2 — …', autogenerate: { … }, collapsed: true },
 *     { slug: 'level-50/comprehensive-knowledge-check' },    // flat page
 *     …
 *   ]
 */
export async function buildLevelItems(level) {
  const levelDir = path.join(CONTENT_ROOT, level);
  const entries = await fs.readdir(levelDir, { withFileTypes: true });

  // Collect the level overview (index.md) — emitted first.
  const items = [{ slug: level }];

  // Two lists so we can sort each independently and then interleave by order.
  const moduleEntries = []; // { name, label, order }
  const flatEntries = []; // { slug, order }

  for (const ent of entries) {
    if (ent.name.startsWith(".")) continue;
    if (ent.isDirectory()) {
      if (!ent.name.startsWith("module-")) continue;
      const indexFile = path.join(levelDir, ent.name, "index.md");
      const title = (await readFrontMatterTitle(indexFile)) || ent.name;
      const order = (await readFrontMatterOrder(indexFile)) ?? 99;
      moduleEntries.push({
        name: ent.name,
        label: title,
        order,
      });
    } else if (ent.isFile()) {
      if (ent.name === "index.md" || ent.name === "index.mdx") continue;
      if (!/\.(md|mdx)$/.test(ent.name)) continue;
      const slug = `${level}/${ent.name.replace(/\.(md|mdx)$/, "")}`;
      const order =
        (await readFrontMatterOrder(path.join(levelDir, ent.name))) ?? 99;
      flatEntries.push({ slug, order });
    }
  }

  // Merge & sort by order. Within the same order, modules come first
  // (matches the visual hierarchy on the level overview pages).
  const merged = [
    ...moduleEntries.map((m) => ({ kind: "module", ...m })),
    ...flatEntries.map((f) => ({ kind: "flat", ...f })),
  ].sort((a, b) => {
    if (a.order !== b.order) return a.order - b.order;
    if (a.kind !== b.kind) return a.kind === "module" ? -1 : 1;
    return (a.label || a.slug).localeCompare(b.label || b.slug);
  });

  for (const item of merged) {
    if (item.kind === "module") {
      items.push({
        label: item.label,
        collapsed: true,
        autogenerate: { directory: `${level}/${item.name}` },
      });
    } else {
      items.push({ slug: item.slug });
    }
  }

  return items;
}

/**
 * Build the full top-level Starlight sidebar configuration.
 *
 * Top-level level groups are `collapsed: true` so the sidebar opens with a
 * clean five-row outline (Level 50 / 100 / 200 / 300 + Resources). Inside
 * each level, module groups are also `collapsed: true` so the nested tree
 * doesn't auto-expand when the user clicks into a single level. Starlight
 * still auto-opens the active path on the page being viewed.
 */
export async function buildSidebar() {
  return [
    {
      label: "Level 50 — Prerequisites",
      badge: { text: "L50", variant: "note" },
      collapsed: true,
      items: await buildLevelItems("level-50"),
    },
    {
      label: "Level 100 — Foundational",
      badge: { text: "L100", variant: "tip" },
      collapsed: true,
      items: await buildLevelItems("level-100"),
    },
    {
      label: "Level 200 — Intermediate",
      badge: { text: "L200", variant: "caution" },
      collapsed: true,
      items: await buildLevelItems("level-200"),
    },
    {
      label: "Level 300 — Advanced",
      badge: { text: "L300", variant: "danger" },
      collapsed: true,
      items: await buildLevelItems("level-300"),
    },
    {
      label: "Resources",
      collapsed: true,
      autogenerate: { directory: "resources" },
    },
  ];
}
