# Contributing to Microsoft Sovereign Cloud Skilling Plan

Thank you for your interest in contributing to this project! We welcome contributions from the community to help improve and expand this skilling plan.

## How to Contribute

### Reporting Issues

If you find errors, outdated information, or have suggestions for improvements:

1. Check if the issue already exists in the [GitHub Issues](https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Specific location (file and section)
   - Suggested correction or improvement
   - Any relevant links or references

### Submitting Changes

1. **Fork the repository**

   ```bash
   git clone https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek.git
   cd microsoft-sovereign-cloud-brain-trek
   ```

2. **Create a feature branch**

   ```bash
   git checkout -b feature/your-improvement
   ```

3. **Make your changes**
   - Edit files in the `/docs` folder
   - Follow the existing structure and formatting
   - Test your markdown locally if possible

4. **Commit your changes**

   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

5. **Push to your fork**

   ```bash
   git push origin feature/your-improvement
   ```

6. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Describe your changes clearly
   - Reference any related issues

## Content Guidelines

### Markdown Formatting

- Use proper heading hierarchy (H1 → H2 → H3)
- Include blank lines before and after headings
- Use code blocks with language specifications
- Add alt text for images

### Content Standards

- **Accuracy:** All technical content should reference official Microsoft documentation
- **Currency:** Include "Last Updated" dates and link to latest Microsoft Learn resources
- **Clarity:** Write for both sales and technical audiences
- **Consistency:** Follow existing terminology and naming conventions

### File Organization

```text
docs/
├── index.md                    # Home page
├── introduction.md             # Overview
├── level-100/                  # Foundational content
│   ├── README.md
│   ├── prerequisites.md
│   └── ...
├── level-200/                  # Intermediate content
├── level-300/                  # Advanced content
├── resources/                  # Additional resources
└── assets/
    └── images/                 # Diagrams and screenshots
```

### Microsoft Learn References

When adding Microsoft Learn resources:

- Use official Microsoft Learn URLs
- Include the full module/article title
- Add a brief description of the content
- Specify estimated time to complete (if available)

Example:

```markdown
- **[Get started with Microsoft Cloud for Sovereignty](https://learn.microsoft.com/en-us/training/paths/get-started-sovereignty/)** - 4 modules covering sovereignty fundamentals (3 hours)
```

### Images and Diagrams

- Store images in `/docs/assets/images/`
- Use descriptive filenames (e.g., `azure-local-architecture.png`)
- Always include alt text
- Prefer diagrams from official Microsoft documentation
- If creating custom diagrams, follow Microsoft's visual style

## Types of Contributions Welcomed

### Content Updates

- Corrections to technical inaccuracies
- Updates to reflect new Azure features
- Additional real-world examples
- Clarifications and improvements

### New Content

- Additional lab exercises
- Case studies and success stories
- Best practices and tips
- FAQ sections
- Quiz questions for knowledge checks

### Documentation Improvements

- Better explanations of complex concepts
- Additional diagrams and visual aids
- Cross-references between related topics
- Improved navigation and structure

### Translations

- Translations to other languages (future)
- Ensure technical accuracy in translations

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome diverse perspectives
- Focus on constructive feedback
- Assume good intentions

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks
- Trolling or inflammatory comments
- Publishing others' private information

## Review Process

1. **Initial Review:** Maintainers will review your PR within 5 business days
2. **Feedback:** You may receive requests for changes or clarifications
3. **Approval:** Once approved, your contribution will be merged
4. **Recognition:** Contributors will be acknowledged in release notes

## Questions?

If you have questions about contributing:

- Open a GitHub Discussion
- Review existing Issues and PRs
- Contact the maintainers

## Contributors

We thank the following people for their contributions to this project:

- **[@jonathan-vella](https://github.com/jonathan-vella)** - Project Lead and Primary Author
- **[@OliCSADoerr](https://github.com/OliCSADoerr)** - Content Contributor (Documentation)

## License

By contributing to this project, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

Thank you for helping improve this skilling plan! Your contributions help sales and technical professionals worldwide master Microsoft Sovereign Cloud technologies.
