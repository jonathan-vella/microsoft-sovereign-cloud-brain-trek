# GitHub Copilot Coding Agent - Quick Reference Guide

**Project:** Microsoft Sovereign Cloud Skilling Plan  
**Repository:** jonathan-vella/microsoft-sovereign-cloud-brain-trek  
**Last Updated:** October 20, 2025  

---

## 🎯 Mission

Create a comprehensive, 96-page skilling plan for Microsoft Sovereign Cloud, Azure Local, and Edge RAG technologies across three progressive learning levels (100/200/300).

---

## 📊 Current Status (October 20, 2025)

### ✅ Completed (3%)
- **Level 100 Module 1:** Digital Sovereignty Fundamentals (7 files, ~100 pages, 15 quiz questions)
- **Planning Infrastructure:** Master plan, changelog, tracking systems

### 🔄 In Progress (0%)
- None currently active

### 🔴 Pending (97%)
- **Level 100:** 4 modules (Sovereign Cloud Models, Azure Local, Azure Arc, Edge RAG)
- **Level 100 Visuals:** 22 diagrams
- **Level 200:** 6 modules + 34+ diagrams
- **Level 300:** 5 modules + 25-30+ diagrams
- **Review & Polish:** Full content review

---

## 📂 Key Files to Reference

### Planning & Tracking
| File | Purpose | When to Update |
|------|---------|---------------|
| `.github/PROJECT_PLAN.md` | Master roadmap with all modules | Check before starting new module |
| `.github/copilot-instructions.md` | Progress checkboxes | After completing each module |
| `CHANGELOG.md` | Document completed work | After completing each module |
| `docs/assets/images/README.md` | Visual asset tracking | When documenting/creating visuals |

### Content Templates
| File | Use As Template For |
|------|-------------------|
| `docs/level-100/digital-sovereignty.md` | Main module pages |
| `docs/level-100/operational-sovereignty.md` | Sub-pages with technical depth |
| `docs/level-100/knowledge-check.md` | Quiz pages |
| `docs/level-100/README.md` | Level overview pages |

---

## 🔄 Standard Workflow

### For Each Module

1. **📖 Review Plan**
   ```
   Read: .github/PROJECT_PLAN.md → Find your module section
   Note: Module number, estimated time, content structure
   ```

2. **✍️ Create Content**
   - Create main page first (follow template)
   - Create sub-pages one-by-one
   - Create quiz last
   - Follow quality standards (see below)

3. **🔗 Update Navigation**
   - Update parent README.md
   - Add cross-references
   - Link to quiz

4. **📊 Document Visuals**
   - Add required diagrams to `docs/assets/images/README.md`
   - Include specifications and sources

5. **✅ Update Tracking**
   - Mark tasks complete in PROJECT_PLAN.md
   - Update CHANGELOG.md
   - Update copilot-instructions.md progress

6. **🎯 Move to Next**
   - Proceed to next module systematically

---

## ✨ Quality Standards Checklist

Every content file MUST include:

### Technical Requirements
- [x] **YAML Front Matter**
  ```yaml
  ---
  layout: default
  title: [Page Title]
  parent: Level [100/200/300] - [Parent Name]
  nav_order: [Number]
  ---
  ```

- [x] **Table of Contents** (for main pages)
  ```markdown
  ## Table of Contents
  {: .no_toc .text-delta }
  
  1. TOC
  {:toc}
  ```

### Content Requirements
- [x] **Customer Scenarios** - Real-world use cases (3-5 examples)
- [x] **Sales Talking Points** - Value propositions, ROI, benefits
- [x] **Technical Talking Points** - Architecture, capabilities, integration
- [x] **Discovery Questions** - Questions to ask customers
- [x] **Competitive Differentiation** - vs. AWS, GCP (where applicable)
- [x] **Best Practices** - Implementation recommendations
- [x] **Common Pitfalls** - What to avoid
- [x] **Cross-References** - Links to related content
- [x] **Microsoft Learn Links** - Official documentation references

### Quiz Requirements (All Assessments)
- [x] **12-15 questions** per quiz
- [x] **Multiple choice format** (A/B/C/D)
- [x] **Detailed explanations** for each answer
- [x] **Cross-references** to source content
- [x] **Scoring guide** with 80% mastery threshold
- [x] **Study recommendations** based on missed topics
- [x] **Collapsible answers section** (using `<details>` tag)

---

## 📝 Content Standards

### Writing Style
- **Tone:** Professional, educational, accessible
- **Audience:** Sales and technical professionals (dual track)
- **Length:** 
  - Main pages: 20-30 minutes reading time
  - Sub-pages: 15-20 minutes reading time
  - Quizzes: 15-20 minutes completion time

### Structure
```markdown
# [Module Name]
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview / What is [Topic]?

[Introduction and definitions]

---

## [Main Section 1]

### [Subsection 1.1]

**Key Concepts:**
- Bullet points
- Clear and concise

**Example Scenario:**
> Customer story or use case

---

## Customer Scenarios

### Scenario 1: [Industry/Use Case]

**Challenge:** [Problem statement]
**Solution:** [How this technology helps]
**Benefits:** [Outcomes and ROI]

---

## Sales Talking Points

- **Value Prop 1:** [Benefit and differentiation]
- **Value Prop 2:** [Benefit and differentiation]

---

## Technical Implementation

### Prerequisites
- [List requirements]

### Steps
1. [Step-by-step guidance]
2. [Clear and actionable]

---

## Discovery Questions

When engaging customers, ask:
- [Question 1]
- [Question 2]

---

## Competitive Differentiation

| Feature | Microsoft | AWS | GCP |
|---------|-----------|-----|-----|
| [Feature] | [Detail] | [Detail] | [Detail] |

---

## Best Practices

✅ **Do:**
- [Recommendation]

❌ **Don't:**
- [Anti-pattern]

---

## Visual Asset Placeholder

> **📊 Visual Reference Needed**  
> *[Diagram Name]*  
> [Description of what the diagram should show]  
> **Source:** [Microsoft Learn URL]

---

## Next Steps

- **[Link to related content]**
- **[Link to next module]**

---

## Additional Resources

- [Microsoft Learn path]
- [Documentation link]
- [Blog post or video]

---

**Last Updated:** October 2025
```

---

## 🎨 Visual Asset Guidelines

### When Documenting Visuals

Add to `docs/assets/images/README.md`:

```markdown
#### [Number]. [Diagram Name]
**File:** `level-[100/200/300]/[filename].svg`

**Description:** [What the diagram shows]

**Content:**
- [Element 1]
- [Element 2]

**Visual Elements:**
- [Design element 1]
- [Design element 2]

**Recommended Source:**
- Adapt from: [Microsoft Learn URL]
- Reference: [Documentation URL]

**Used In:**
- `docs/level-[100/200/300]/[page].md`

---
```

### Design Standards
- **Format:** SVG (preferred) or PNG (300 DPI minimum)
- **Colors:** Microsoft Blue (#0078D4), Azure Blue (#008AD7)
- **Font:** Segoe UI or Arial
- **Accessibility:** WCAG AA color contrast minimum

---

## 🚨 Common Mistakes to Avoid

### ❌ Don't
- Create files without YAML front matter
- Skip cross-references to related content
- Forget to update navigation in parent README
- Miss quiz explanations
- Use outdated Microsoft Learn URLs
- Create content without customer scenarios
- Forget sales talking points
- Skip competitive differentiation

### ✅ Do
- Follow Digital Sovereignty module as quality benchmark
- Include both sales and technical perspectives
- Add visual asset placeholders with sources
- Update all tracking files after completion
- Cross-reference between related topics
- Include discovery questions for customer conversations
- Add best practices and common pitfalls

---

## 📋 Module Completion Checklist

Before moving to next module, verify:

- [ ] All files created per PROJECT_PLAN.md specification
- [ ] YAML front matter correct on all files
- [ ] Table of contents on main pages
- [ ] Customer scenarios included (3-5)
- [ ] Sales and technical talking points
- [ ] Discovery questions for customers
- [ ] Competitive differentiation (where applicable)
- [ ] Best practices and implementation steps
- [ ] Visual assets documented in images/README.md
- [ ] Quiz created with 12-15 questions
- [ ] Quiz has detailed explanations
- [ ] Navigation updated in parent README.md
- [ ] Cross-references to related content
- [ ] Microsoft Learn links validated
- [ ] PROJECT_PLAN.md tasks marked complete
- [ ] CHANGELOG.md updated
- [ ] copilot-instructions.md progress updated

---

## 🎯 Next Module to Work On

### Level 100 Module 2: Microsoft Sovereign Cloud Models

**Reference:** `.github/PROJECT_PLAN.md` → Phase 1 → Module 2

**Files to Create:**
1. `docs/level-100/sovereign-cloud-models.md` (main page)
2. `docs/level-100/sovereign-public-cloud.md` (sub-page)
3. `docs/level-100/sovereign-private-cloud.md` (sub-page)
4. `docs/level-100/national-partner-clouds.md` (sub-page)
5. `docs/level-100/cloud-models-quiz.md` (quiz)

**Visual Assets to Document:** 3 diagrams
- sovereign-cloud-models-comparison.svg
- model-decision-tree.svg
- partner-clouds-map.svg

**Estimated Time:** 8-10 hours

**Start Command for Agent:**
```
Create Level 100 Module 2: Microsoft Sovereign Cloud Models
- Follow PROJECT_PLAN.md Module 2 specification
- Use digital-sovereignty.md as quality template
- Create 4 content pages + 1 quiz
- Document 3 visual assets
- Update all tracking files
```

---

## 💡 Tips for Success

### For Content Quality
- **Read the template:** Study `digital-sovereignty.md` before starting
- **Stay consistent:** Match tone, structure, and depth of existing content
- **Think dual-track:** Address both sales and technical audiences
- **Be scenario-driven:** Use real customer examples
- **Link everything:** Cross-reference related topics extensively

### For Efficiency
- **Work systematically:** Main page → Sub-pages → Quiz → Visuals
- **Update as you go:** Mark tasks complete immediately
- **Batch similar work:** Do all main pages, then all quizzes, etc.
- **Use templates:** Copy structure from existing files

### For Continuity
- **Check tracking first:** Review PROJECT_PLAN.md before starting
- **Document everything:** Update CHANGELOG.md after each module
- **Leave breadcrumbs:** Note where you stopped in tracking files
- **Stay modular:** Each module should be complete and independent

---

## 📞 Questions?

If you're unsure about:
- **Content depth:** Match Digital Sovereignty module quality
- **Structure:** Follow templates exactly
- **Technical details:** Reference Microsoft Learn documentation
- **Priorities:** Follow PROJECT_PLAN.md order
- **Quality:** Use completion checklist above

---

## 🎉 Success Metrics

You're on track if:
- Each module takes 8-15 hours to complete
- Content length matches existing modules (20-30 min reading)
- All quality checklist items are checked
- Navigation and cross-references work correctly
- Quiz has 12-15 questions with explanations
- Visual assets are documented (even if not created yet)
- Tracking files are updated

---

**Ready to Start?** 🚀

1. Review `.github/PROJECT_PLAN.md` → Module 2
2. Read this guide one more time
3. Study `docs/level-100/digital-sovereignty.md` template
4. Create `sovereign-cloud-models.md` main page
5. Follow the workflow above

**Good luck!** 💪
