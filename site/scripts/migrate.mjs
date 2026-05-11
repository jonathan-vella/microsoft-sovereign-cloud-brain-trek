#!/usr/bin/env node
/**
 * migrate.mjs — Jekyll → Astro Starlight content conversion script.
 *
 * Reads `docs/` (Jekyll source) and writes `site/src/content/docs/`
 * (Starlight content collection). Idempotent and re-runnable.
 *
 * Usage:
 *   node site/scripts/migrate.mjs               # full migration (all levels)
 *   node site/scripts/migrate.mjs --level 50    # one level only
 *   node site/scripts/migrate.mjs --no-reshape  # skip module folder reshape
 *   node site/scripts/migrate.mjs --dry-run     # don't write files
 *
 * Outputs:
 *   site/src/content/docs/**            converted .md / .mdx files
 *   site/public/images/**               copied SVG/PNG assets
 *   site/path-rewrite-map.json          old slug → new slug map
 *   site/migration-report.json          stats + warnings + quarantine list
 *   site/needs-manual-fix/**            files whose MDX failed parse
 *
 * Transform stages (in order):
 *   1. Discovery: walk docs/, parse all front matter, build module index
 *   2. Path planning: compute new path for each file (reshape if requested)
 *   3. Body transform: strip kramdown, convert callouts/KCs/diagrams, rewrite links
 *   4. Front-matter rewrite: drop layout/nav_order, emit Starlight schema
 *   5. Extension decision: .md vs .mdx based on component usage
 *   6. MDX safety pass: escape JSX gotchas, validate parse, quarantine on fail
 *   7. Asset copy: sync docs/assets/images/ → site/public/images/
 *   8. Report emission: write rewrite map and migration report
 */

import fs from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import matter from "gray-matter";
import { compile as compileMdx } from "@mdx-js/mdx";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const REPO_ROOT = path.resolve(__dirname, "..", "..");
const SRC_DIR = path.join(REPO_ROOT, "docs");
const DEST_DIR = path.join(REPO_ROOT, "site", "src", "content", "docs");
const PUBLIC_IMAGES_DIR = path.join(REPO_ROOT, "site", "public", "images");
const QUARANTINE_DIR = path.join(REPO_ROOT, "site", "needs-manual-fix");
const REPORT_PATH = path.join(REPO_ROOT, "site", "migration-report.json");
const PATH_MAP_PATH = path.join(REPO_ROOT, "site", "path-rewrite-map.json");

const LEVELS = ["level-50", "level-100", "level-200", "level-300", "resources"];

// ------------------------------------------------------------------- args ---

function parseArgs(argv) {
  const args = { level: null, reshape: true, dryRun: false };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--level") args.level = `level-${argv[++i]}`;
    else if (a === "--no-reshape") args.reshape = false;
    else if (a === "--dry-run") args.dryRun = true;
    else if (a === "--help" || a === "-h") {
      printHelp();
      process.exit(0);
    } else {
      console.error(`Unknown flag: ${a}`);
      process.exit(2);
    }
  }
  return args;
}

function printHelp() {
  console.log(`migrate.mjs — Jekyll → Astro Starlight conversion

Flags:
  --level NN        Migrate only one level (e.g. --level 50)
  --no-reshape      Skip module-folder reshape; keep flat layout
  --dry-run         Run all transforms but don't write any files
  --help            Show this message
`);
}

// -------------------------------------------------------------- utilities ---

function slugify(s) {
  // Match GitHub / rehype-slug behavior used by Starlight.
  return s
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9\s-]/g, "")
    .trim()
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-");
}

async function walk(dir, results = []) {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  for (const e of entries) {
    const full = path.join(dir, e.name);
    if (e.isDirectory()) await walk(full, results);
    else if (e.isFile() && full.endsWith(".md")) results.push(full);
  }
  return results;
}

async function ensureDir(p) {
  await fs.mkdir(p, { recursive: true });
}

// ----------------------------------------------------- discovery (pass 1) ---

/**
 * Walk docs/ and build:
 *   files: [{ srcPath, levelDir, baseName, frontMatter, body }]
 *   moduleIndex: Map<title, srcPath>   for parent-resolution
 */
async function discover(args) {
  const allMd = await walk(SRC_DIR);
  const files = [];
  const moduleIndex = new Map();
  const skipped = [];

  for (const srcPath of allMd) {
    const rel = path.relative(SRC_DIR, srcPath);
    const segments = rel.split(path.sep);
    const levelDir = segments[0];

    // Top-level pages need per-file handling:
    //   docs/index.md         — Jekyll home; we keep the Phase-1.1 Starlight
    //                           splash instead, but record a link map so
    //                           refs to ../index.md resolve to "/".
    //   docs/introduction.md  — real content page; migrate it.
    //   docs/404.md           — Starlight emits its own 404; skip.
    //   docs/README.md        — project status doc; not user content; skip.
    if (segments.length === 1) {
      if (rel === "introduction.md") {
        // Fall through into the normal pipeline; processed below.
      } else {
        skipped.push({ srcPath: rel, reason: "top-level-page" });
        continue;
      }
    } else if (!LEVELS.includes(levelDir)) {
      skipped.push({ srcPath: rel, reason: `not-a-known-level: ${levelDir}` });
      continue;
    }
    if (args.level && segments.length > 1 && levelDir !== args.level) continue;

    let parsed;
    try {
      const raw = await fs.readFile(srcPath, "utf8");
      parsed = matter(raw);
    } catch (err) {
      skipped.push({ srcPath: rel, reason: `parse-failed: ${err.message}` });
      continue;
    }

    const baseName = path.basename(srcPath, ".md");
    const fm = parsed.data || {};
    const file = {
      srcPath,
      relPath: rel,
      levelDir,
      baseName,
      frontMatter: fm,
      body: parsed.content,
    };
    files.push(file);

    if (fm.has_children === true && typeof fm.title === "string") {
      moduleIndex.set(fm.title, file);
    }
  }

  return { files, moduleIndex, skipped };
}

// ---------------------------------------------- path planning (pass 2) -----

/**
 * Decide each file's destination slug and on-disk path. Builds two maps:
 *   pathMap: srcPath → { destPath, slug, isModuleIndex }
 *   slugByOldSlug: oldSlug → newSlug   (for legacy .html stub generation)
 *
 * Reshape rules (when args.reshape):
 *   - module-NN-name.md with has_children: true →
 *       level-X/module-NN-name/index.md
 *   - sub-page with parent: matching that module's title →
 *       level-X/module-NN-name/sub-page-slug.md
 *   - everything else stays at level-X/sub-page-slug.md (flat)
 *
 * Without reshape: every file is level-X/baseName.md (flat).
 */
function planPaths(files, moduleIndex, args) {
  const pathMap = new Map();
  const slugByOldSlug = new Map();

  // Hardcoded slug entries for top-level pages that exist in the source
  // but are intentionally not migrated 1:1. Lets the link rewriter
  // resolve ../index.md and similar refs without warnings.
  const SYNTHETIC_TOP_LEVEL = {
    "index.md": "/",
    "404.md": "/404",
  };

  for (const file of files) {
    const fm = file.frontMatter;
    const isModuleIndex = fm.has_children === true;

    // Top-level introduction.md routes to a flat root page.
    if (file.relPath === "introduction.md") {
      const destRel = "introduction.md";
      const destPath = path.join(DEST_DIR, destRel);
      const slug = "/introduction/";
      pathMap.set(file.srcPath, {
        destPath,
        destRel,
        slug,
        isModuleIndex: false,
      });
      slugByOldSlug.set("/introduction.html", slug);
      continue;
    }

    let folder = file.levelDir;
    let leaf = file.baseName;

    if (args.reshape) {
      if (isModuleIndex && file.baseName.startsWith("module-")) {
        folder = path.join(file.levelDir, file.baseName);
        leaf = "index";
      } else if (typeof fm.parent === "string" && moduleIndex.has(fm.parent)) {
        const parent = moduleIndex.get(fm.parent);
        if (parent.baseName.startsWith("module-")) {
          folder = path.join(parent.levelDir, parent.baseName);
        }
      }
    }

    // Each level's README.md becomes the level landing index. This
    // overwrites the Phase 1.1 placeholder index.md and gives the level
    // sidebar entry a real content page. Same treatment for any
    // level-X/<module>/README.md if one ever exists.
    if (file.baseName === "README") {
      leaf = "index";
    }

    const destRel = path.join(folder, `${leaf}.md`); // extension finalized later
    const destPath = path.join(DEST_DIR, destRel);

    // Starlight slug is the path without /index and without the .md ext.
    const slug =
      "/" +
      (leaf === "index"
        ? folder.split(path.sep).join("/")
        : `${folder.split(path.sep).join("/")}/${leaf}`) +
      "/";

    const oldSlug = `/${file.levelDir}/${file.baseName}.html`;

    pathMap.set(file.srcPath, { destPath, destRel, slug, isModuleIndex });
    slugByOldSlug.set(oldSlug, slug);
  }

  return { pathMap, slugByOldSlug };
}

// --------------------------------------- body transforms (pass 3) ----------

/** Strip kramdown directives that do not survive Starlight. */
function stripKramdownDirectives(body) {
  // {: .no_toc } / {: .text-delta } / {: .no_toc .text-delta } on its own line
  body = body.replace(/^\{:\s*\.[\w\s.-]+\s*\}\s*$/gm, "");
  // {:toc} placeholder line (may follow a "1. TOC" line — strip that pair)
  body = body.replace(/^\s*1\.\s*TOC\s*\n\s*\{:toc\}\s*$/gm, "");
  body = body.replace(/^\s*\{:toc\}\s*$/gm, "");
  return body;
}

/**
 * Drop the entire "## Table of Contents" section that Jekyll/kramdown used
 * to inject the right-sidebar TOC. Starlight auto-generates this.
 *
 * Pattern observed in the survey:
 *   ## Table of Contents
 *   {: .no_toc .text-delta }
 *
 *   1. TOC
 *   {:toc}
 *
 * We delete from the H2 line through the next blank line after {:toc}, or
 * if {:toc} was already stripped, just kill the leftover heading + bullet.
 */
function stripTocSection(body) {
  // Greedy block: the H2 line + any directive/blank lines + an optional
  // "1. TOC" line + an optional {:toc} line + trailing blank line.
  return body.replace(
    /^##\s+Table of Contents\s*\n(?:\{:[^}]+\}\s*\n)?\s*\n?(?:1\.\s*TOC\s*\n)?(?:\{:toc\}\s*\n)?\s*\n?/gim,
    "",
  );
}

/** Drop the leading H1 — Starlight renders it from front-matter `title`. */
function stripLeadingH1(body) {
  // Trim leading blanks, then if the first non-blank line is `# something`,
  // remove that line (and an immediately following `{: .no_toc }` if any).
  const lines = body.split("\n");
  let i = 0;
  while (i < lines.length && lines[i].trim() === "") i++;
  if (i < lines.length && /^#\s+\S/.test(lines[i])) {
    lines.splice(i, 1);
    if (i < lines.length && /^\{:\s*\.no_toc\s*\}\s*$/.test(lines[i])) {
      lines.splice(i, 1);
    }
  }
  return lines.join("\n");
}

/**
 * Convert kramdown callouts to Starlight asides.
 *
 * Source pattern:
 *   {: .CLASS }
 *   > **Optional Title**
 *   > body line 1
 *   > body line 2
 *
 * Mapping:
 *   .note      → :::note
 *   .warning   → :::caution
 *   .important → :::tip       (closest neutral "this matters" feel)
 *   .tip       → :::tip
 *   anything else → :::note    (preserve content; warn in report)
 */
function convertCallouts(body, warnings, fileLabel) {
  const ASIDE = {
    note: "note",
    warning: "caution",
    important: "tip",
    tip: "tip",
    caution: "caution",
    danger: "danger",
  };

  const lines = body.split("\n");
  const out = [];
  let i = 0;

  while (i < lines.length) {
    const directive = lines[i].match(/^\{:\s*\.([\w-]+)\s*\}\s*$/);
    if (directive && i + 1 < lines.length && lines[i + 1].startsWith(">")) {
      const cls = directive[1];
      const variant = ASIDE[cls];
      if (!variant) {
        warnings.push({
          file: fileLabel,
          kind: "unknown-callout-class",
          detail: `{: .${cls} } — defaulting to :::note`,
        });
      }
      const asideKind = variant || "note";

      // Collect contiguous "> " quoted lines.
      i++;
      const quoted = [];
      while (i < lines.length && lines[i].startsWith(">")) {
        quoted.push(lines[i].replace(/^>\s?/, ""));
        i++;
      }

      // First line might be `**Title**` — pull it into the aside title.
      let title = null;
      if (quoted.length && /^\*\*([^*]+)\*\*\s*$/.test(quoted[0])) {
        title = quoted[0].match(/^\*\*([^*]+)\*\*\s*$/)[1].trim();
        quoted.shift();
      } else if (
        quoted.length &&
        /^\*\*([^*]+)\*\*[:\s]/.test(quoted[0])
      ) {
        // "**Note:** body on same line"
        const m = quoted[0].match(/^\*\*([^*]+)\*\*[:\s]+(.*)$/);
        title = m[1].trim().replace(/[:\s]+$/, "");
        quoted[0] = m[2];
      }

      const open = title ? `:::${asideKind}[${title}]` : `:::${asideKind}`;
      out.push(open);
      while (quoted.length && quoted[0].trim() === "") quoted.shift();
      while (quoted.length && quoted[quoted.length - 1].trim() === "")
        quoted.pop();
      out.push(...quoted);
      // MD032 (blanks-around-lists): if the aside body ends with a list item,
      // we must insert a blank line before the closing `:::` so the list
      // terminates cleanly.
      if (
        quoted.length &&
        /^\s*([-*+]|\d+\.)\s+/.test(quoted[quoted.length - 1])
      ) {
        out.push("");
      }
      out.push(":::");
      out.push("");
      continue;
    }
    out.push(lines[i]);
    i++;
  }

  return out.join("\n");
}

/**
 * Convert knowledge-check `<details markdown="1">` blocks to
 * `<KnowledgeCheck answer="X" reference="Y">…children…</KnowledgeCheck>`.
 *
 * Source pattern:
 *   <details markdown="1">
 *   <summary>Click to reveal answer</summary>
 *
 *   **Correct Answer: B**
 *
 *   **Explanation:** ...prose...
 *
 *   **Reference:** [Topic](path.md)
 *
 *   </details>
 *
 * After conversion:
 *   - Removes the `<summary>` row (component renders its own).
 *   - Strips the "Correct Answer: X" line and surfaces it as the `answer`
 *     prop. The remaining body becomes children.
 *   - Strips the "Reference: [text](url)" line and surfaces the URL as
 *     the `reference` prop (best-effort link rewrite happens later).
 *   - Returns { body, anyConverted } so caller can flag .md → .mdx.
 */
function convertKnowledgeChecks(body, warnings, fileLabel) {
  const re =
    /<details\s+markdown="1"\s*>\s*<summary>([^<]+)<\/summary>\s*([\s\S]*?)<\/details>/g;
  let anyConverted = false;
  body = body.replace(re, (_match, _summary, inner) => {
    anyConverted = true;
    // Two source variants exist:
    //   **Correct Answer: B**       — closing ** wraps the answer letter
    //   **Correct Answer:** B       — colon-close, answer in plain text
    const answerMatch =
      inner.match(/\*\*Correct Answer:\s*([^*\n]+?)\s*\*\*\s*\n?/) ||
      inner.match(/\*\*Correct Answer:\*\*\s*([^\n]+?)\s*\n?/);
    const refMatch = inner.match(
      /\*\*Reference:\*\*\s*\[[^\]]+\]\(([^)]+)\)\s*\n?/,
    );
    const answer = answerMatch ? answerMatch[1].trim() : "?";
    const reference = refMatch ? refMatch[1].trim() : null;

    if (answer === "?") {
      warnings.push({
        file: fileLabel,
        kind: "knowledge-check-no-answer",
        detail: "Could not extract answer letter from <details> block",
      });
    }

    let children = inner;
    if (answerMatch) children = children.replace(answerMatch[0], "");
    if (refMatch) children = children.replace(refMatch[0], "");
    children = children.trim();

    const propsAttr = reference
      ? `answer="${escapeAttr(answer)}" reference="${escapeAttr(reference)}"`
      : `answer="${escapeAttr(answer)}"`;
    return `<KnowledgeCheck ${propsAttr}>\n\n${children}\n\n</KnowledgeCheck>`;
  });
  return { body, anyConverted };
}

/**
 * Convert diagram-container `<details>` blocks to <DiagramContainer>.
 *
 * Source pattern:
 *   <details class="diagram-container"[ open]>
 *   <summary>View Diagram: Title</summary>
 *   <div class="diagram-content" markdown="1">
 *
 *   ![alt](image.svg)
 *   _Figure caption_
 *
 *   </div>
 *   </details>
 *
 * Converted:
 *   <DiagramContainer title="Title" defaultOpen>
 *
 *   ![alt](image.svg)
 *   _Figure caption_
 *
 *   </DiagramContainer>
 */
function convertDiagramContainers(body) {
  const re =
    /<details\s+class="diagram-container"(\s+open)?\s*>\s*<summary>([^<]*)<\/summary>\s*<div\s+class="diagram-content"\s+markdown="1"\s*>\s*([\s\S]*?)<\/div>\s*<\/details>/g;
  let anyConverted = false;
  body = body.replace(re, (_match, openAttr, summary, inner) => {
    anyConverted = true;
    const title = summary.replace(/^View Diagram:\s*/i, "").trim();
    const propsParts = [`title="${escapeAttr(title)}"`];
    if (openAttr) propsParts.push("defaultOpen");
    return `<DiagramContainer ${propsParts.join(" ")}>\n\n${inner.trim()}\n\n</DiagramContainer>`;
  });
  return { body, anyConverted };
}

function escapeAttr(s) {
  return String(s).replace(/"/g, "&quot;");
}

// -------------------------------------------------- link rewriting ---------

/**
 * Rewrite all internal links in the body:
 *   [text]({% link path %})           Jekyll tag form
 *   [text](relative.md)               relative same-folder
 *   [text](../level-X/foo.md)         cross-level
 *   [text](foo.md#anchor)             with anchor
 *   <a href="foo.md">                 inline HTML
 *
 * External links (http*, mailto:, tel:) are left alone.
 *
 * Resolution: source `.md` is mapped through `srcLookup` (relPath under
 * docs/ → slug from pathMap). A link to a deleted file is left unchanged
 * and a warning is emitted.
 */
function rewriteLinks(body, file, srcLookup, warnings) {
  const fileLabel = file.relPath;

  // {% link path/to/file.md %} — root-relative to docs/
  body = body.replace(
    /\{%\s*link\s+([^\s%]+)\s*%\}/g,
    (_full, target) =>
      resolveLink(target, file, srcLookup, warnings, fileLabel, {
        rootRelative: true,
      }),
  );

  // [text](target.md[#anchor]) — only matches relative .md or .md#frag
  body = body.replace(
    /\]\(([^)]+\.md(?:#[^)]+)?)\)/g,
    (_full, target) => {
      // Skip absolute URLs and anchor-only references.
      if (/^https?:|^mailto:|^tel:|^#/i.test(target)) return `](${target})`;
      const resolved = resolveLink(
        target,
        file,
        srcLookup,
        warnings,
        fileLabel,
      );
      return `](${resolved})`;
    },
  );

  // <a href="target.md[#anchor]"> — best-effort
  body = body.replace(
    /<a\s+href="([^"]+\.md(?:#[^"]+)?)"/g,
    (_full, target) => {
      if (/^https?:/i.test(target)) return `<a href="${target}"`;
      const resolved = resolveLink(
        target,
        file,
        srcLookup,
        warnings,
        fileLabel,
      );
      return `<a href="${resolved}"`;
    },
  );

  // Component reference="..." attribute carrying a .md path. Emitted by
  // convertKnowledgeChecks before this rewrite runs. The path is the raw
  // string from the original Markdown link, so apply the same rules as a
  // normal Markdown link.
  body = body.replace(
    /(\sreference=")([^"]+\.md(?:#[^"]+)?)(")/g,
    (_full, lead, target, tail) => {
      if (/^https?:/i.test(target)) return `${lead}${target}${tail}`;
      const resolved = resolveLink(
        target,
        file,
        srcLookup,
        warnings,
        fileLabel,
      );
      return `${lead}${resolved}${tail}`;
    },
  );

  // Image references: ../../assets/images/level-X/foo.svg →
  // /microsoft-sovereign-cloud-brain-trek/images/level-X/foo.svg
  body = body.replace(
    /(!\[[^\]]*\]\()((?:\.\.\/)+assets\/images\/[^)]+)(\))/g,
    (_full, lead, p, tail) => {
      const stripped = p.replace(/^(\.\.\/)+assets\//, "");
      return `${lead}/microsoft-sovereign-cloud-brain-trek/${stripped}${tail}`;
    },
  );
  // Same for inline HTML <img src="../../assets/images/...">
  body = body.replace(
    /(<img\s[^>]*\bsrc=")((?:\.\.\/)+assets\/images\/[^"]+)(")/g,
    (_full, lead, p, tail) => {
      const stripped = p.replace(/^(\.\.\/)+assets\//, "");
      return `${lead}/microsoft-sovereign-cloud-brain-trek/${stripped}${tail}`;
    },
  );

  return body;
}

function resolveLink(
  target,
  sourceFile,
  srcLookup,
  warnings,
  fileLabel,
  opts = {},
) {
  // Split off optional #anchor
  const [pathPart, anchor] = target.split("#");

  // Resolve to a path under docs/. Three cases:
  //   1. Site-absolute Jekyll path (leading "/")  → strip leading slash
  //   2. Jekyll {% link %} tag (rootRelative)     → already root-relative
  //   3. Markdown relative path                   → join with source dir
  let lookupKey;
  if (pathPart.startsWith("/")) {
    lookupKey = pathPart.replace(/^\//, "");
  } else if (opts.rootRelative) {
    lookupKey = path.normalize(pathPart);
  } else if (pathPart.startsWith("..") || pathPart.includes("/")) {
    const sourceDir = path.dirname(sourceFile.relPath);
    lookupKey = path.normalize(path.join(sourceDir, pathPart));
  } else {
    lookupKey = path.join(path.dirname(sourceFile.relPath), pathPart);
  }

  const entry = srcLookup.get(lookupKey);
  if (!entry) {
    warnings.push({
      file: fileLabel,
      kind: "broken-internal-link",
      detail: `Could not resolve "${target}" → looked up "${lookupKey}"`,
    });
    return target; // leave as-is so reviewer can fix
  }

  return anchor ? `${entry.slug}#${anchor}` : entry.slug;
}

// -------------------------------------- front matter rewrite (pass 4) ------

/**
 * Convert Jekyll/just-the-docs front matter to the Starlight schema.
 * Drops Jekyll-only fields, maps nav_order → sidebar.order, etc.
 */
function rewriteFrontMatter(file, planEntry) {
  const fm = file.frontMatter;
  const out = {
    title: fm.title,
    description: fm.description,
  };
  if (typeof fm.nav_order === "number" || typeof fm.nav_order === "string") {
    out.sidebar = { order: Number(fm.nav_order) };
  }
  if (fm.nav_exclude === true) {
    out.sidebar = { ...(out.sidebar || {}), hidden: true };
  }
  // Module overview pages (now folder index) get a stable visual marker:
  // Starlight will pick them up automatically as the folder root.
  if (planEntry.isModuleIndex) {
    out.sidebar = out.sidebar || {};
    if (out.sidebar.order === undefined) out.sidebar.order = 0;
  }
  return out;
}

// ----------------------------- extension decision (pass 5) -----------------

function pickExtension({ usedKnowledgeCheck, usedDiagramContainer, body }) {
  if (usedKnowledgeCheck || usedDiagramContainer) return ".mdx";
  // Look for any other JSX-like usage that demands MDX.
  if (/<[A-Z][A-Za-z0-9]*[\s/>]/.test(body)) return ".mdx";
  return ".md";
}

// ------------------------------ MDX safety pass (pass 6) -------------------

/**
 * Light pre-processing for known MDX gotchas. The full parser is the source
 * of truth — anything still failing goes to quarantine.
 *
 * Heuristics applied:
 *   - Self-close stray <br> and <hr> if not already closed.
 *   - Escape "<" followed by a digit in prose (e.g. "<5 minutes" → "&lt;5 minutes").
 *   - Leave fenced code blocks untouched.
 */
function mdxSafetyPass(body) {
  // Tokenize fenced code blocks so we don't touch their contents.
  const segments = tokenizeFenced(body);
  for (let i = 0; i < segments.length; i++) {
    if (segments[i].type !== "prose") continue;
    let s = segments[i].text;
    s = s.replace(/<br\s*>/g, "<br />");
    s = s.replace(/<hr\s*>/g, "<hr />");
    s = s.replace(/<(\d)/g, "&lt;$1");
    // Escape bare braces in prose that would otherwise be parsed as JSX
    // expressions by MDX. We only protect ones that are not already
    // escaped and not part of a JSX attribute / component (which appear
    // immediately after a tag name and the parser handles natively).
    s = escapeBareBraces(s);
    segments[i].text = s;
  }
  return segments.map((s) => s.text).join("");
}

/**
 * Walk the prose segment line by line. Skip lines that look like part
 * of a JSX tag block (start with `<` or `</` or are inside one). On
 * every other line, escape `{` and `}` to `\{` and `\}` so MDX does
 * not try to parse them as expressions. Common offenders in the Jekyll
 * source: pseudo-config code samples that escaped their fence, kramdown
 * inline attribute lists (we already strip the most common ones, but
 * this catches stragglers), and prose that contains literal JSON.
 */
function escapeBareBraces(text) {
  const lines = text.split("\n");
  let insideJsxBlock = false;
  for (let i = 0; i < lines.length; i++) {
    const trimmed = lines[i].trim();
    // Heuristic: a line starting with `<` and not `</` opens a JSX block
    // and we let MDX handle its attributes. A line that's purely a JSX
    // close (or self-close) ends the block.
    if (/^<\/?[A-Za-z]/.test(trimmed)) {
      insideJsxBlock = !/\/>\s*$/.test(trimmed) && !/^<\//.test(trimmed)
        ? true
        : false;
      continue;
    }
    if (insideJsxBlock) {
      // Heuristic: blank line ends the JSX block we were in for the
      // purposes of this scanner; child prose is on subsequent lines.
      if (trimmed === "") insideJsxBlock = false;
      continue;
    }
    // Don't escape an already-escaped brace.
    lines[i] = lines[i]
      .replace(/(?<!\\)\{/g, "\\{")
      .replace(/(?<!\\)\}/g, "\\}");
  }
  return lines.join("\n");
}

function tokenizeFenced(body) {
  const out = [];
  const re = /```[\s\S]*?```/g;
  let lastIndex = 0;
  let m;
  while ((m = re.exec(body))) {
    if (m.index > lastIndex)
      out.push({ type: "prose", text: body.slice(lastIndex, m.index) });
    out.push({ type: "code", text: m[0] });
    lastIndex = m.index + m[0].length;
  }
  if (lastIndex < body.length)
    out.push({ type: "prose", text: body.slice(lastIndex) });
  return out;
}

async function validateMdx(content) {
  try {
    await compileMdx(content, { jsx: true });
    return { ok: true };
  } catch (err) {
    return { ok: false, error: err.message };
  }
}

// ----------------------------- assemble & write (pass 7) -------------------

function assembleOutput({ frontMatter, body, ext, importsHeader }) {
  const fmYaml = serializeYaml(frontMatter);
  const head = ext === ".mdx" && importsHeader ? `\n${importsHeader}\n` : "";
  return `---\n${fmYaml}---\n${head}\n${body.trim()}\n`;
}

/** Tiny stable YAML serializer for the small set of keys we emit. */
function serializeYaml(obj) {
  const lines = [];
  for (const [k, v] of Object.entries(obj)) {
    if (v === undefined || v === null) continue;
    if (typeof v === "string") {
      lines.push(`${k}: ${quoteIfNeeded(v)}`);
    } else if (typeof v === "number" || typeof v === "boolean") {
      lines.push(`${k}: ${v}`);
    } else if (typeof v === "object") {
      lines.push(`${k}:`);
      for (const [k2, v2] of Object.entries(v)) {
        if (v2 === undefined || v2 === null) continue;
        if (typeof v2 === "string")
          lines.push(`  ${k2}: ${quoteIfNeeded(v2)}`);
        else lines.push(`  ${k2}: ${v2}`);
      }
    }
  }
  return lines.join("\n") + "\n";
}

function quoteIfNeeded(s) {
  if (/^[\w./-]+$/.test(s) && !/^(true|false|null|yes|no)$/i.test(s)) return s;
  return `"${s.replace(/\\/g, "\\\\").replace(/"/g, '\\"')}"`;
}

// ------------------------------------ asset copy (pass 8) ------------------

async function copyImages(dryRun) {
  const SRC = path.join(SRC_DIR, "assets", "images");
  if (!existsSync(SRC)) return { copied: 0 };
  await ensureDir(PUBLIC_IMAGES_DIR);
  // Only copy actual web image assets — skip Python diagram generators
  // (.py), READMEs, asset registries, and other source-of-truth files
  // that live alongside the rendered SVGs.
  const ALLOWED = new Set([".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp"]);
  let copied = 0;
  async function copyDir(srcDir, destDir) {
    const entries = await fs.readdir(srcDir, { withFileTypes: true });
    for (const e of entries) {
      const srcP = path.join(srcDir, e.name);
      const destP = path.join(destDir, e.name);
      if (e.isDirectory()) {
        if (!dryRun) await ensureDir(destP);
        await copyDir(srcP, destP);
      } else if (e.isFile()) {
        const ext = path.extname(e.name).toLowerCase();
        if (!ALLOWED.has(ext)) continue;
        if (!dryRun) await fs.copyFile(srcP, destP);
        copied++;
      }
    }
  }
  await copyDir(SRC, PUBLIC_IMAGES_DIR);
  return { copied };
}

// --------------------------------------- main orchestration ---------------

async function main() {
  const args = parseArgs(process.argv);
  console.log(
    `migrate.mjs — level=${args.level || "all"} reshape=${args.reshape} dryRun=${args.dryRun}`,
  );

  const { files, moduleIndex, skipped } = await discover(args);
  console.log(
    `Discovered ${files.length} content file(s); ${skipped.length} skipped (top-level / unknown)`,
  );

  const { pathMap, slugByOldSlug } = planPaths(files, moduleIndex, args);

  // srcLookup: key = relative path under docs/ (no leading docs/), value = plan entry
  const srcLookup = new Map();
  for (const f of files) srcLookup.set(f.relPath, pathMap.get(f.srcPath));

  // Register synthetic entries for top-level pages that exist in the
  // source but are intentionally not converted 1:1 (the Starlight
  // splash replaces docs/index.md; Starlight emits its own 404). Allows
  // internal links like `../index.md` to resolve without warnings.
  srcLookup.set("index.md", { slug: "/" });
  srcLookup.set("404.md", { slug: "/404" });

  const warnings = [];
  const promotedToMdx = [];
  const stayedAsMd = [];
  const quarantined = [];

  // Reset destination if not dry-run? No — we want idempotency, not destroy.
  // We do clean the quarantine dir each run so its state always reflects
  // the current source.
  if (!args.dryRun && existsSync(QUARANTINE_DIR)) {
    await fs.rm(QUARANTINE_DIR, { recursive: true, force: true });
  }

  for (const file of files) {
    const plan = pathMap.get(file.srcPath);
    let body = file.body;

    body = stripTocSection(body);
    body = stripLeadingH1(body);
    body = convertCallouts(body, warnings, file.relPath);
    // Strip remaining kramdown directives AFTER convertCallouts so that
    // `{: .note }`, `{: .warning }`, etc. survive long enough to be recognized
    // as callout markers. Anything still present at this point is layout
    // metadata (`.no_toc`, `.text-delta`) that Starlight does not consume.
    body = stripKramdownDirectives(body);

    const kc = convertKnowledgeChecks(body, warnings, file.relPath);
    body = kc.body;
    const dc = convertDiagramContainers(body);
    body = dc.body;

    body = rewriteLinks(body, file, srcLookup, warnings);

    const ext = pickExtension({
      usedKnowledgeCheck: kc.anyConverted,
      usedDiagramContainer: dc.anyConverted,
      body,
    });

    const importsHeader =
      ext === ".mdx"
        ? [
            kc.anyConverted
              ? `import KnowledgeCheck from "~/components/KnowledgeCheck.astro";`
              : null,
            dc.anyConverted
              ? `import DiagramContainer from "~/components/DiagramContainer.astro";`
              : null,
          ]
            .filter(Boolean)
            .join("\n")
        : null;

    if (ext === ".mdx") body = mdxSafetyPass(body);

    const frontMatter = rewriteFrontMatter(file, plan);
    const output = assembleOutput({ frontMatter, body, ext, importsHeader });

    // Validate MDX before writing — quarantine on failure.
    if (ext === ".mdx") {
      const result = await validateMdx(output);
      if (!result.ok) {
        quarantined.push({ file: file.relPath, error: result.error });
        if (!args.dryRun) {
          const qPath = path.join(QUARANTINE_DIR, file.relPath);
          await ensureDir(path.dirname(qPath));
          await fs.writeFile(qPath, output, "utf8");
          await fs.writeFile(`${qPath}.error.txt`, result.error, "utf8");
        }
        continue;
      }
      promotedToMdx.push(file.relPath);
    } else {
      stayedAsMd.push(file.relPath);
    }

    const finalDestPath = plan.destPath.replace(/\.md$/, ext);
    if (!args.dryRun) {
      await ensureDir(path.dirname(finalDestPath));
      await fs.writeFile(finalDestPath, output, "utf8");
    }
  }

  const assetReport = await copyImages(args.dryRun);

  const report = {
    generatedAt: new Date().toISOString(),
    args,
    counts: {
      discovered: files.length,
      promotedToMdx: promotedToMdx.length,
      stayedAsMd: stayedAsMd.length,
      quarantined: quarantined.length,
      warnings: warnings.length,
      imagesCopied: assetReport.copied,
    },
    warnings,
    quarantined,
    skipped,
    promotedToMdx,
    stayedAsMd,
  };

  if (!args.dryRun) {
    await fs.writeFile(REPORT_PATH, JSON.stringify(report, null, 2), "utf8");
    const mapObj = Object.fromEntries(slugByOldSlug);
    await fs.writeFile(PATH_MAP_PATH, JSON.stringify(mapObj, null, 2), "utf8");
  }

  console.log(`
=== Migration Summary ===
Discovered:      ${files.length}
Promoted to MDX: ${promotedToMdx.length}
Stayed as MD:    ${stayedAsMd.length}
Quarantined:     ${quarantined.length}
Warnings:        ${warnings.length}
Images copied:   ${assetReport.copied}
Path-rewrite map entries: ${slugByOldSlug.size}

Report:    ${path.relative(REPO_ROOT, REPORT_PATH)}
Map:       ${path.relative(REPO_ROOT, PATH_MAP_PATH)}
${quarantined.length ? `Quarantine: ${path.relative(REPO_ROOT, QUARANTINE_DIR)}/\n` : ""}`);

  if (quarantined.length > 0) process.exit(1);
}

main().catch((err) => {
  console.error("FATAL:", err);
  process.exit(2);
});
