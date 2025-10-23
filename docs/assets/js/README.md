# JavaScript Assets

This directory contains JavaScript files that enhance the functionality of the Microsoft Sovereign Cloud Brain Trek documentation site.

## External Links Handler (`external-links.js`)

### Purpose
Automatically opens external links in a new browser tab or window, improving user experience by keeping the documentation site open while users explore external resources.

### Features
- **Automatic Detection**: Identifies all external links (links pointing to different hostnames)
- **New Tab Opening**: Adds `target="_blank"` attribute to external links
- **Security**: Adds `rel="noopener noreferrer"` to prevent security vulnerabilities
- **CSS Class**: Adds `external-link` class for optional styling

### How It Works
1. Runs when the page DOM is fully loaded
2. Queries all anchor tags with `href` attributes
3. Checks if each link points to an external domain (different hostname)
4. Adds appropriate attributes to external links only
5. Internal links and anchor links remain unmodified

### Internal vs External Links

**External Links** (open in new tab):
- `https://learn.microsoft.com/...`
- `https://techcommunity.microsoft.com/...`
- `https://github.com/Azure/...`
- Any link to a different domain

**Internal Links** (same tab):
- `/microsoft-sovereign-cloud-brain-trek/...`
- `../level-100/...`
- `#anchor-links`
- Any relative path or same-domain link

### Implementation
The script is loaded via `docs/_includes/head_custom.html`, which is automatically included in the `<head>` section by the Just the Docs theme.

### Testing
To verify the feature is working:
1. Open any documentation page
2. Open browser DevTools Console
3. Inspect external links - they should have:
   - `target="_blank"`
   - `rel="noopener noreferrer"`
   - `class="external-link"`

### Maintenance
- No maintenance required for new links added to markdown files
- Works automatically for all pages in the site
- Compatible with Jekyll and Just the Docs theme

### Security Considerations
The `rel="noopener noreferrer"` attribute prevents:
- **noopener**: Prevents new pages from accessing `window.opener` (security risk)
- **noreferrer**: Prevents passing referrer information to external sites

This is a security best practice for all external links that open in new tabs.

---

**Last Updated**: October 2025  
**Compatibility**: Jekyll 3.10+, Just the Docs 0.10+
