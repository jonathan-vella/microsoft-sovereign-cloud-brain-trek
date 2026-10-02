import { defineCollection, z } from "astro:content";
import { docsLoader } from "@astrojs/starlight/loaders";
import { docsSchema } from "@astrojs/starlight/schema";

export const collections = {
  docs: defineCollection({
    loader: docsLoader(),
    schema: docsSchema({
      // Extend the Starlight base schema with project-specific metadata.
      // Description is required so every page provides good SEO and search
      // result text. Max length is set to 220 to fit the longest existing
      // description in the source content (currently 207 chars). Tighten
      // this once the migration is complete.
      extend: z.object({
        description: z
          .string()
          .min(20)
          .max(220)
          .describe("SEO and navigation description, 20–220 chars."),
        // Date the page's facts were last checked against Microsoft sources (YYYY-MM-DD).
        // Optional during the content rebuild; becomes required once every page has it.
        lastVerified: z
          .union([z.string().regex(/^\d{4}-\d{2}-\d{2}$/), z.date()])
          .optional()
          .describe("Date the page's facts were last verified, YYYY-MM-DD."),
        // Module landing pages (`level-NN/module-NN-*/index.md[x]`) only. Every key is optional;
        // the landing template (src/components/ModuleOverview.astro) skips what is missing.
        module: z
          .object({
            // Reading time for the whole module, for example "30-45 minutes".
            duration: z.string().optional(),
            // What the learner can do after the module. One plain sentence each.
            objectives: z.array(z.string()).optional(),
            // Plain text, or a root-relative page link such as "/level-50/" (shown with its title).
            prerequisites: z.array(z.string()).optional(),
            // Override the computed next module with a root-relative link.
            next: z.string().optional(),
          })
          .optional()
          .describe("Module landing page metadata rendered by the module template."),
        // The original Jekyll site used `nav_order` for sidebar position.
        // Starlight uses `sidebar.order` instead — the migration script
        // rewrites `nav_order: N` to `sidebar: { order: N }`. Keeping a
        // permissive optional `nav_order` here would let stragglers slip
        // through silently, so we deliberately do NOT accept it.
      }),
    }),
  }),
};
