/**
 * Starlight route middleware (wired in astro.config.mjs as `routeMiddleware`).
 *
 * - Hero action links: Starlight emits them as written, without the site base path. Front matter
 *   uses root-relative links (`/level-50/`) like page bodies do; the base is added here.
 * - Pagination: prev/next use the sidebar label, which is "Overview" for every landing page.
 *   Show the target page's title instead, so "Next" reads "Module 4: Azure Arc introduction".
 * - "On this page": list the sections the landing page templates add.
 */
import { defineRouteMiddleware, type StarlightRouteData } from "@astrojs/starlight/route-data";
import { getDocs, idFromHref } from "./components/course/course";
import { withBase } from "../scripts/site-constants.mjs";

export const onRequest = defineRouteMiddleware(async (context) => {
  const route = context.locals.starlightRoute;

  for (const action of route.entry.data.hero?.actions ?? []) {
    action.link = withBase(action.link);
  }

  // The pagination links are the sidebar's own objects; replace them rather than mutate.
  const docs = await getDocs();
  const relabel = <T extends { href: string; label: string }>(link: T | undefined): T | undefined => {
    const title = link && docs.get(idFromHref(link.href))?.data.title;
    return link && title ? { ...link, label: title } : link;
  };
  route.pagination = { prev: relabel(route.pagination.prev), next: relabel(route.pagination.next) };

  // Add the sections that the landing page templates (overrides/MarkdownContent.astro) render
  // to "On this page". Index 0 is Starlight's "Overview" link to the page title.
  const items = route.toc?.items;
  if (!items) return;
  const entry = (slug: string, text: string) => ({ depth: 2, slug, text, children: [] });
  if (/^level-\d+$/.test(route.id)) {
    items.splice(1, 0, entry("modules-in-this-level", "Modules in this level"));
  } else if (/^level-\d+\/module-[^/]+$/.test(route.id)) {
    const meta = route.entry.data.module;
    const before = [];
    if (meta?.objectives?.length) before.push(entry("learning-objectives", "Learning objectives"));
    if (meta?.prerequisites?.length) before.push(entry("prerequisites", "Prerequisites"));
    items.splice(1, 0, ...before);
    if ((findCurrentGroup(route.sidebar)?.entries.length ?? 0) > 1) {
      items.push(entry("in-this-module", "In this module"));
    }
  }
});

type SidebarEntry = StarlightRouteData["sidebar"][number];
type SidebarGroup = Extract<SidebarEntry, { type: "group" }>;

/** The sidebar group whose direct links include the current page. */
function findCurrentGroup(entries: SidebarEntry[]): SidebarGroup | undefined {
  for (const e of entries) {
    if (e.type !== "group") continue;
    if (e.entries.some((c) => c.type === "link" && c.isCurrent)) return e;
    const found = findCurrentGroup(e.entries);
    if (found) return found;
  }
  return undefined;
}
