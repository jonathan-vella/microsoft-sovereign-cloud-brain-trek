// Astro does not add `base` to root-relative links and images written in Markdown,
// so `[x](/level-100/...)` and `![x](/images/...)` would 404 on GitHub Pages.
// This plugin prefixes the base path to root-relative `href` and `src` values.
import { withBase } from "../../scripts/site-constants.mjs";

export default function rehypeBasePath() {
  const visit = (node) => {
    if (node.type === "element" && node.properties) {
      for (const attr of ["href", "src"]) {
        if (typeof node.properties[attr] === "string") {
          node.properties[attr] = withBase(node.properties[attr]);
        }
      }
    }
    if (node.children) node.children.forEach(visit);
  };
  return (tree) => visit(tree);
}
