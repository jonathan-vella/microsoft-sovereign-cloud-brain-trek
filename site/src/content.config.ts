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
        // The original Jekyll site used `nav_order` for sidebar position.
        // Starlight uses `sidebar.order` instead — the migration script
        // rewrites `nav_order: N` to `sidebar: { order: N }`. Keeping a
        // permissive optional `nav_order` here would let stragglers slip
        // through silently, so we deliberately do NOT accept it.
      }),
    }),
  }),
};
