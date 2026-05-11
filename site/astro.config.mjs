// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import mdx from "@astrojs/mdx";
import rehypeMermaid from "rehype-mermaid-lite";
import { buildSidebar } from "./scripts/build-sidebar.mjs";

// Mermaid init script with the Fluent 2 / Azure color palette. The
// previous palette set primary fill to #0078D4 with white text, which
// produced low-contrast nodes on Microsoft Learn-style diagrams. The
// new palette uses a light tint fill with a dark border + dark text,
// matching how Microsoft Learn renders inline architecture diagrams.
const mermaidInitScript = `import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
mermaid.initialize({
  startOnLoad: true,
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
});`;

export default defineConfig({
  site: "https://jonathan-vella.github.io",
  base: "/microsoft-sovereign-cloud-brain-trek",
  trailingSlash: "always",
  markdown: {
    rehypePlugins: [rehypeMermaid],
  },
  integrations: [
    starlight({
      title: "Microsoft Sovereign Cloud Brain Trek",
      description:
        "Master Sovereign Cloud, Azure Local, and Edge AI Technologies — a comprehensive learning journey for architects and solutions professionals.",
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
      components: {
        // Lock the site to light theme: ThemeSelect is empty (hides the
        // header dropdown) and ThemeProvider forces `data-theme="light"`
        // on every page load. See site/src/components/ for both overrides.
        ThemeSelect: "./src/components/ThemeSelect.astro",
        ThemeProvider: "./src/components/ThemeProvider.astro",
      },
    }),
    mdx(),
  ],
});
