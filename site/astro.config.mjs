// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import mdx from "@astrojs/mdx";
import rehypeMermaid from "rehype-mermaid-lite";
import { buildSidebar } from "./scripts/build-sidebar.mjs";
import { activeRedirects } from "./scripts/redirects.mjs";
import { SITE, BASE } from "./scripts/site-constants.mjs";
import rehypeBasePath from "./src/plugins/rehype-base-path.mjs";

// Mermaid init script with the Fluent 2 / Azure color palette. The
// previous palette set primary fill to #0078D4 with white text, which
// produced low-contrast nodes on Microsoft Learn-style diagrams. The
// new palette uses a light tint fill with a dark border + dark text,
// matching how Microsoft Learn renders inline architecture diagrams.
const mermaidInitScript = `import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
mermaid.initialize({
  startOnLoad: false,
  theme: "base",
  themeVariables: {
    primaryColor: "#DEECF9",
    primaryTextColor: "#0C3B5E",
    primaryBorderColor: "#0F6CBD",
    secondaryColor: "#E8F5E8",
    secondaryBorderColor: "#107C10",
    secondaryTextColor: "#0B6A0B",
    tertiaryColor: "#FFF4CE",
    tertiaryBorderColor: "#B89500",
    tertiaryTextColor: "#5C4400",
    lineColor: "#605E5C",
    textColor: "#242424",
    mainBkg: "#DEECF9",
    nodeBorder: "#0F6CBD",
    clusterBkg: "#F7FAFD",
    clusterBorder: "#CFE3F6",
    fontFamily: "Inter Variable, Segoe UI, system-ui, sans-serif",
    fontSize: "15px"
  },
  flowchart: { curve: "basis", padding: 14 },
  sequence: { useMaxWidth: true },
  themeCSS: ".edgeLabel { background-color: #F7FAFD; }"
});
// Mermaid measures text while drawing, so a diagram inside a closed <details> (DiagramContainer)
// comes out squashed. Draw visible diagrams now and the rest when their container opens.
const draw = (root) => {
  const nodes = [...root.querySelectorAll("pre.mermaid:not([data-processed])")].filter((n) => !n.closest("details:not([open])"));
  if (nodes.length) mermaid.run({ nodes });
};
draw(document);
document.addEventListener("toggle", (e) => e.target.open && draw(e.target), true);`;

// Records each page the reader opens, for the progress marks on the learning path and module
// pages (src/components/course/progress.ts reads the same key). Stays in the browser.
const recordVisitScript = `try {
  const key = "brain-trek:visited";
  const seen = JSON.parse(localStorage.getItem(key) || "[]");
  const page = location.pathname.replace(/\\/?$/, "/");
  if (!seen.includes(page)) localStorage.setItem(key, JSON.stringify(seen.concat(page).slice(-1000)));
} catch {}`;

export default defineConfig({
  site: SITE,
  base: BASE,
  trailingSlash: "always",
  // Old URLs of moved or deleted pages. Source of truth: site/redirects.json.
  redirects: activeRedirects(),
  markdown: {
    rehypePlugins: [rehypeMermaid, rehypeBasePath],
  },
  integrations: [
    starlight({
      title: "Microsoft Sovereign Cloud Brain Trek",
      description:
        "Training for architects and solutions professionals on Microsoft Sovereign Cloud, Azure Local, Azure Arc, Foundry Local, and Zero Trust.",
      logo: {
        src: "./src/assets/brand/logo.svg",
        replacesTitle: false,
      },
      favicon: "/favicon.svg",
      customCss: ["./src/styles/custom.css"],
      head: [
        {
          tag: "script",
          attrs: { type: "module" },
          content: mermaidInitScript,
        },
        { tag: "script", content: recordVisitScript },
      ],
      editLink: {
        baseUrl:
          "https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek/edit/main/site/",
      },
      lastUpdated: true,
      pagination: true,
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
      social: [
        {
          icon: "github",
          label: "GitHub",
          href: "https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek",
        },
      ],
      sidebar: await buildSidebar(),
      // Hero link base path and title-based prev/next labels. See src/route-data.ts.
      routeMiddleware: "./src/route-data.ts",
      components: {
        // Lock the site to light theme: ThemeSelect is empty (hides the
        // header dropdown) and ThemeProvider forces `data-theme="light"`
        // on every page load. See site/src/components/ for both overrides.
        ThemeSelect: "./src/components/ThemeSelect.astro",
        ThemeProvider: "./src/components/ThemeProvider.astro",
        // Level and module landing page templates (learning path, module summary and pages).
        MarkdownContent: "./src/components/overrides/MarkdownContent.astro",
        // "Last verified" from front matter next to "Last updated".
        LastUpdated: "./src/components/overrides/LastUpdated.astro",
      },
    }),
    mdx(),
  ],
});
