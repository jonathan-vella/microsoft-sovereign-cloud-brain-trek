# Security Policy

## Reporting Security Issues

The Microsoft Sovereign Cloud Brain Trek team takes security seriously. We appreciate your efforts to responsibly disclose your findings.

**Please do NOT report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to the repository maintainer or through GitHub's private vulnerability reporting feature.

## Supported Versions

| Version | Supported |
|---------|-----------|
| Current (main branch) | ✅ |
| Previous releases | ❌ |

## Security Best Practices for This Repository

This repository contains **training documentation only** and does not include:

- Production code or deployable applications
- Secrets, credentials, or API keys
- Customer data or personally identifiable information (PII)

### For Contributors

When contributing to this repository:

1. **Never commit secrets** — Use environment variables or Azure Key Vault references in examples
2. **Sanitize examples** — Ensure all code samples use placeholder values
3. **Review dependencies** — Keep Ruby gems and npm packages updated
4. **Follow Microsoft guidelines** — Adhere to [Microsoft Security Development Lifecycle](https://www.microsoft.com/securityengineering/sdl)

### For Learners

When following the hands-on labs:

1. **Use test environments** — Never use production subscriptions for labs
2. **Clean up resources** — Delete lab resources after completion to avoid costs
3. **Rotate credentials** — If you accidentally expose any credentials, rotate them immediately
4. **Follow least privilege** — Use minimal permissions for lab exercises

## Content Security

The content in this repository references Microsoft's official security documentation:

- [Microsoft Security Best Practices](https://learn.microsoft.com/en-us/security/)
- [Azure Security Documentation](https://learn.microsoft.com/en-us/azure/security/)
- [Zero Trust Architecture](https://learn.microsoft.com/en-us/security/zero-trust/)
- [Microsoft Cloud for Sovereignty](https://learn.microsoft.com/en-us/industry/sovereign-cloud/)

## Dependency Updates

This project uses GitHub Dependabot to monitor and update dependencies. Security updates are prioritized and typically addressed within 48 hours.

## Contact

For security concerns, contact the repository maintainer through GitHub.

---

**Last Updated:** November 2025
