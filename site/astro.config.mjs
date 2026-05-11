// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import mdx from "@astrojs/mdx";
import rehypeMermaid from "rehype-mermaid-lite";
import { buildSidebar } from "./scripts/build-sidebar.mjs";

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
