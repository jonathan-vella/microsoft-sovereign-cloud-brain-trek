// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import mdx from "@astrojs/mdx";
import rehypeMermaid from "rehype-mermaid-lite";

// Mermaid init script with the Azure color palette used across the docs.
// The Mermaid module is loaded from a CDN to keep the build self-contained.
const mermaidInitScript = `import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
mermaid.initialize({
  startOnLoad: true,
  theme: "base",
  themeVariables: {
    primaryColor: "#0078D4",
    primaryTextColor: "#ffffff",
    primaryBorderColor: "#004578",
    lineColor: "#505050",
    secondaryColor: "#107C10",
    tertiaryColor: "#FF8C00",
    fontFamily: "Segoe UI, system-ui, sans-serif"
  }
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
      social: {
        github:
          "https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek",
      },
      sidebar: [
        {
          label: "Level 50 — Prerequisites",
          badge: { text: "L50", variant: "note" },
          autogenerate: { directory: "level-50" },
        },
        {
          label: "Level 100 — Foundational",
          badge: { text: "L100", variant: "tip" },
          autogenerate: { directory: "level-100" },
        },
        {
          label: "Level 200 — Intermediate",
          badge: { text: "L200", variant: "caution" },
          autogenerate: { directory: "level-200" },
        },
        {
          label: "Level 300 — Advanced",
          badge: { text: "L300", variant: "danger" },
          autogenerate: { directory: "level-300" },
        },
        {
          label: "Resources",
          autogenerate: { directory: "resources" },
        },
      ],
      components: {
        // Theme components (light/dark switcher) ported from dc2fabric.
        // These will be added in Phase 1.3 alongside KnowledgeCheck and DiagramContainer.
        // ThemeProvider: "./src/components/ThemeProvider.astro",
        // ThemeSelect: "./src/components/ThemeSelect.astro",
      },
    }),
    mdx(),
  ],
});
