/**
 * External Links Handler
 * Automatically opens external links in a new tab/window
 * Adds security attributes to prevent tabnabbing
 *
 * Built: October 2025
 */

(function() {
  'use strict';

  // Configuration
  const INTERNAL_DOMAINS = [
    'jonathan-vella.github.io',
    window.location.hostname
  ];

  const BASE_PATH = '/sov-cloud-brain-trek';

  /**
   * Check if a URL is external (not within the site)
   */
  function isExternalLink(url, hostname) {
    // Skip empty, anchor-only, or javascript: links
    if (!url || url.startsWith('#') || url.startsWith('javascript:') || url.startsWith('mailto:')) {
      return false;
    }

    // Relative paths are internal
    if (!url.startsWith('http://') && !url.startsWith('https://') && !url.startsWith('//')) {
      return false;
    }

    // Check if link is to an internal domain
    try {
      const linkUrl = new URL(url, window.location.origin);
      return !INTERNAL_DOMAINS.some(domain => linkUrl.hostname === domain || linkUrl.hostname.endsWith('.' + domain));
    } catch (e) {
      // If URL parsing fails, assume it's internal to be safe
      return false;
    }
  }

  /**
   * Process all links on the page
   */
  function processLinks() {
    const links = document.querySelectorAll('a[href]');
    let processedCount = 0;

    links.forEach(link => {
      const href = link.getAttribute('href');
      const hostname = link.hostname;

      // Skip if already has target="_blank"
      if (link.getAttribute('target') === '_blank') {
        return;
      }

      // Check if external
      if (isExternalLink(href, hostname)) {
        // Add target="_blank" to open in new tab
        link.setAttribute('target', '_blank');

        // Add security attributes
        // noopener: prevents the new page from accessing window.opener
        // noreferrer: prevents the browser from sending referrer information
        const currentRel = link.getAttribute('rel') || '';
        const relValues = new Set(currentRel.split(' ').filter(Boolean));
        relValues.add('noopener');
        relValues.add('noreferrer');
        link.setAttribute('rel', Array.from(relValues).join(' '));

        // Add title attribute for accessibility (if not already present)
        if (!link.getAttribute('title')) {
          link.setAttribute('title', 'Opens in a new tab');
        }

        processedCount++;
      }
    });

    // Log results (only in development)
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
      console.log(`External Links: Processed ${processedCount} external links`);
    }
  }

  /**
   * Initialize when DOM is ready
   */
  function init() {
    // Process existing links
    processLinks();

    // Watch for dynamically added links (e.g., from AJAX, search results)
    if (window.MutationObserver) {
      const observer = new MutationObserver(function(mutations) {
        let shouldProcess = false;

        mutations.forEach(function(mutation) {
          if (mutation.addedNodes.length > 0) {
            mutation.addedNodes.forEach(function(node) {
              if (node.nodeType === 1 && (node.tagName === 'A' || node.querySelector('a'))) {
                shouldProcess = true;
              }
            });
          }
        });

        if (shouldProcess) {
          processLinks();
        }
      });

      observer.observe(document.body, {
        childList: true,
        subtree: true
      });
    }
  }

  // Run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    // DOM is already ready
    init();
  }
})();
