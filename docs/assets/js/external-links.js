/**
 * External Links Handler
 * Automatically opens external links in a new tab/window
 * 
 * This script adds target="_blank" and rel="noopener noreferrer" to all links
 * that point to external domains (not part of the current site).
 */

(function() {
  'use strict';

  /**
   * Initialize external link handler when DOM is ready
   */
  function initExternalLinks() {
    // Get the current hostname
    const currentHost = window.location.hostname;
    
    // Get all links on the page
    const links = document.querySelectorAll('a[href]');
    
    links.forEach(function(link) {
      const href = link.getAttribute('href');
      
      // Skip if href is empty, an anchor, or potentially dangerous protocol
      if (!href || href.startsWith('#') || href.startsWith('javascript:') || 
          href.startsWith('data:') || href.startsWith('vbscript:')) {
        return;
      }
      
      // Check if link is external
      // A link is external if it starts with http(s) and points to a different host
      let isExternal = false;
      
      if (href.startsWith('http://') || href.startsWith('https://')) {
        try {
          const linkUrl = new URL(href);
          isExternal = linkUrl.hostname !== currentHost;
        } catch (e) {
          // If URL parsing fails, assume it's not external
          isExternal = false;
        }
      }
      
      if (isExternal) {
        // Add target="_blank" to open in new tab
        link.setAttribute('target', '_blank');
        
        // Add rel="noopener noreferrer" for security
        // noopener: prevents new page from accessing window.opener
        // noreferrer: prevents passing referrer information
        const existingRel = link.getAttribute('rel') || '';
        const relValues = existingRel.split(' ').filter(Boolean);
        
        if (!relValues.includes('noopener')) {
          relValues.push('noopener');
        }
        if (!relValues.includes('noreferrer')) {
          relValues.push('noreferrer');
        }
        
        link.setAttribute('rel', relValues.join(' '));
        
        // Add visual indicator (optional - can be styled with CSS)
        if (!link.querySelector('.external-link-icon')) {
          link.classList.add('external-link');
        }
      }
    });
  }

  // Run when DOM is fully loaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initExternalLinks);
  } else {
    // DOM already loaded
    initExternalLinks();
  }
})();
