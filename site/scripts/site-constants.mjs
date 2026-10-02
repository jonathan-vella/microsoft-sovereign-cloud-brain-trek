// Shared by astro.config.mjs, the rehype base-path plugin, components, and the build scripts.
export const SITE = "https://jonathan-vella.github.io";
export const BASE = "/microsoft-sovereign-cloud-brain-trek";

/** Prefix BASE to a root-relative URL. Leaves external, protocol-relative, and already-prefixed URLs alone. */
export function withBase(url) {
  if (typeof url !== "string" || !url.startsWith("/") || url.startsWith("//")) return url;
  if (url === BASE || url.startsWith(`${BASE}/`)) return url;
  return `${BASE}${url}`;
}
