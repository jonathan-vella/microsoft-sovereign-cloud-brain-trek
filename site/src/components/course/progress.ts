/**
 * Marks pages the reader has opened, using the list kept in localStorage by the inline script in
 * astro.config.mjs (`VISITED_KEY`). Nothing leaves the browser. Elements opt in with:
 *   data-progress-pages="href href ..."  container; gets --progress (0-1) and data-progress-state
 *   data-progress-text                    child of a container; filled with "2 of 6 pages visited"
 *   data-progress-page="href"             single page row; gets data-visited="true|false"
 */
export const VISITED_KEY = "brain-trek:visited";

function readVisited(): Set<string> {
  try {
    return new Set(JSON.parse(localStorage.getItem(VISITED_KEY) ?? "[]"));
  } catch {
    return new Set();
  }
}

function apply() {
  const visited = readVisited();
  for (const el of document.querySelectorAll<HTMLElement>("[data-progress-pages]")) {
    const pages = (el.dataset.progressPages ?? "").split(" ").filter(Boolean);
    const done = pages.filter((p) => visited.has(p)).length;
    el.style.setProperty("--progress", String(pages.length ? done / pages.length : 0));
    el.dataset.progressState = done === 0 ? "none" : done === pages.length ? "done" : "started";
    const text = [...el.querySelectorAll<HTMLElement>("[data-progress-text]")].find(
      (t) => t.closest("[data-progress-pages]") === el,
    );
    if (text) {
      text.textContent = done ? `${done} of ${pages.length} pages visited` : "Not started";
      text.hidden = false;
    }
  }
  for (const el of document.querySelectorAll<HTMLElement>("[data-progress-page]")) {
    const isVisited = visited.has(el.dataset.progressPage ?? "");
    el.dataset.visited = String(isVisited);
    const label = el.querySelector<HTMLElement>("[data-progress-label]");
    if (label) label.textContent = isVisited ? "Visited" : "";
  }
}

apply();
// Back/forward cache restores the old DOM; refresh the marks.
window.addEventListener("pageshow", (e) => e.persisted && apply());
