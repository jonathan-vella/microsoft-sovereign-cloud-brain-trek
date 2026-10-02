/**
 * Course structure derived from the Starlight sidebar (built by scripts/build-sidebar.mjs from the
 * content folders), joined with page front matter. Components use it to render the learning path,
 * module landing pages, and pagination labels, so new levels, modules, and pages show up without a
 * hand-kept list.
 */
import { getCollection, type CollectionEntry } from "astro:content";
import type { StarlightRouteData } from "@astrojs/starlight/route-data";
import { BASE, withBase } from "../../../scripts/site-constants.mjs";
import redirects from "../../../redirects.json";

type SidebarEntry = StarlightRouteData["sidebar"][number];
type SidebarLink = Extract<SidebarEntry, { type: "link" }>;
export type Doc = CollectionEntry<"docs">;

export interface CourseUnit {
  href: string;
  label: string;
  title: string;
  description?: string;
  isCurrent: boolean;
  isKnowledgeCheck: boolean;
}

export interface CourseModule {
  number: number;
  /** Module name without the number, for example "Azure Local overview". */
  name: string;
  /** Landing page, if the module has one yet. */
  overview?: CourseUnit;
  units: CourseUnit[];
  entry?: Doc;
  isCurrent: boolean;
  /** Every page in the module including the landing page, for progress tracking. */
  hrefs: string[];
}

export interface CourseLevel {
  id: string;
  number: number;
  label: string;
  badge?: { text: string; variant: string };
  overview: CourseUnit;
  modules: CourseModule[];
  /** Pages at the level root that are not in a module. */
  extras: CourseUnit[];
  isCurrent: boolean;
  hrefs: string[];
}

const LEVEL_HREF_RE = /\/(level-(\d+))\/$/;
const MODULE_LABEL_RE = /^(\d+)\.\s*(.*)$/;

/** "/microsoft-sovereign-cloud-brain-trek/level-100/x/#y" -> "level-100/x" */
export function idFromHref(href: string): string {
  let path = href.split("#")[0].split("?")[0];
  if (path === BASE || path.startsWith(`${BASE}/`)) path = path.slice(BASE.length);
  return path.replace(/^\/+|\/+$/g, "") || "index";
}

let docsPromise: Promise<Map<string, Doc>> | undefined;
export function getDocs(): Promise<Map<string, Doc>> {
  docsPromise ??= getCollection("docs").then((docs) => new Map(docs.map((d) => [d.id, d])));
  return docsPromise;
}

/** Resolve a root-relative link to the page it points at (following redirects.json), if it exists. */
export async function findDoc(link: string): Promise<Doc | undefined> {
  if (!link.startsWith("/")) return undefined;
  const docs = await getDocs();
  const moves = redirects as Record<string, string>;
  let id = idFromHref(withBase(link));
  for (let hops = 0; !docs.has(id) && moves[`/${id}/`] && hops < 10; hops++) {
    id = idFromHref(withBase(moves[`/${id}/`]));
  }
  return docs.get(id);
}

function toUnit(link: SidebarLink, docs: Map<string, Doc>): CourseUnit {
  const doc = docs.get(idFromHref(link.href));
  return {
    href: link.href,
    label: link.label,
    title: doc?.data.title ?? link.label,
    description: doc?.data.description,
    isCurrent: link.isCurrent,
    isKnowledgeCheck: /knowledge-check/.test(link.href),
  };
}

export async function getCourse(sidebar: SidebarEntry[]): Promise<CourseLevel[]> {
  const docs = await getDocs();
  const levels: CourseLevel[] = [];

  for (const group of sidebar) {
    if (group.type !== "group") continue;
    const first = group.entries.find((e): e is SidebarLink => e.type === "link");
    const match = first?.href.match(LEVEL_HREF_RE);
    if (!first || !match) continue;

    const level: CourseLevel = {
      id: match[1],
      number: Number(match[2]),
      label: docs.get(match[1])?.data.title ?? group.label,
      badge: group.badge ? { text: group.badge.text, variant: group.badge.variant } : undefined,
      overview: toUnit(first, docs),
      modules: [],
      extras: [],
      isCurrent: false,
      hrefs: [first.href],
    };

    for (const entry of group.entries) {
      if (entry === first) continue;
      if (entry.type === "link") {
        level.extras.push(toUnit(entry, docs));
        level.hrefs.push(entry.href);
        continue;
      }
      const links = entry.entries.filter((e): e is SidebarLink => e.type === "link");
      const [, num = "0", name = entry.label] = entry.label.match(MODULE_LABEL_RE) ?? [];
      const overviewLink = links[0]?.label === "Overview" ? links[0] : undefined;
      const mod: CourseModule = {
        number: Number(num),
        name,
        overview: overviewLink && toUnit(overviewLink, docs),
        units: links.filter((l) => l !== overviewLink).map((l) => toUnit(l, docs)),
        entry: overviewLink && docs.get(idFromHref(overviewLink.href)),
        isCurrent: links.some((l) => l.isCurrent),
        hrefs: links.map((l) => l.href),
      };
      level.modules.push(mod);
      level.hrefs.push(...mod.hrefs);
    }
    level.isCurrent =
      first.isCurrent || level.modules.some((m) => m.isCurrent) || level.extras.some((u) => u.isCurrent);
    levels.push(level);
  }
  return levels;
}

export interface NextLink {
  href: string;
  title: string;
  kind: "module" | "level" | "page";
}

/** Where to go after `mod`: the next module in its level, else the next level's overview. */
export function nextAfter(levels: CourseLevel[], mod: CourseModule): NextLink | undefined {
  const li = levels.findIndex((l) => l.modules.includes(mod));
  if (li === -1) return undefined;
  const following = levels[li].modules[levels[li].modules.indexOf(mod) + 1];
  if (following) {
    const target = following.overview ?? following.units[0];
    return target && { href: target.href, title: `Module ${following.number}: ${following.name}`, kind: "module" };
  }
  const nextLevel = levels[li + 1];
  return nextLevel && { href: nextLevel.overview.href, title: nextLevel.overview.title, kind: "level" };
}

/** "2026-10-02" or a Date -> { iso: "2026-10-02", text: "2 October 2026" }. */
export function formatDate(value: string | Date): { iso: string; text: string } {
  const date = typeof value === "string" ? new Date(`${value}T00:00:00Z`) : value;
  return {
    iso: date.toISOString().slice(0, 10),
    text: date.toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric", timeZone: "UTC" }),
  };
}

export function pluralize(count: number, word: string): string {
  return `${count} ${word}${count === 1 ? "" : "s"}`;
}
