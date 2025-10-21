<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Project: Microsoft Sovereign Cloud Brain Trek

## Project Overview
- **Official Name:** Microsoft Sovereign Cloud Brain Trek
- **Tagline:** Master Sovereign Cloud, Azure Local, and Edge AI Technologies
- **Subtitle:** A comprehensive learning journey for architects and solutions professionals
- **Type:** Static website / Documentation site for comprehensive skilling program
- **Target Audience:** Sales professionals, architects, and technical experts learning Microsoft Sovereign Cloud, Azure Local, and Edge AI technologies
- **Delivery:** Markdown-based content in /docs folder, ready for Jekyll/GitHub Pages
- **Structure:** Modular pages organized by learning levels (100/200/300)

## Progress Tracking

- [x] Verify that the copilot-instructions.md file in the .github directory is created.

- [x] Clarify Project Requirements
	**Summary:** Project is a skilling plan documentation site with modular markdown content, Microsoft branding, collaborative editing support, and future GitHub Pages deployment.

- [x] Scaffold the Project
	**Summary:** Created project structure with /docs folder, level-based organization (100/200/300), README, LICENSE, CONTRIBUTING guidelines, and initial documentation pages.

- [x] Customize the Project
	**Summary:** 
	- ✅ Level 100 Module 1: Digital Sovereignty Fundamentals (COMPLETE)
	  - Main page enhanced with scenarios, misconceptions, decision framework
	  - 5 sub-pages created (european-commitments, regulatory-overview, data-residency-concepts, operational-sovereignty, knowledge-check)
	  - Navigation updated with cross-references
	  - Visual assets documented (7 diagrams)
	- ✅ Level 100 Module 2: Microsoft Sovereign Cloud Models (COMPLETE)
	  - Main page with three models overview, comparison matrix, decision framework
	  - 3 sub-pages created (sovereign-public-cloud, sovereign-private-cloud, national-partner-clouds)
	  - Quiz with 15 questions and detailed explanations
	  - Navigation updated with complete module structure
	  - Visual assets documented (3 diagrams)
	- ✅ Master project plan created (.github/PROJECT_PLAN.md)
	- ✅ Comprehensive 275-345 hour roadmap documented
	- ✅ Module-by-module breakdown for all three levels
	- ✅ Visual asset tracking and guidelines established
	- 🔄 Level 100 Modules 3-5 pending (Azure Local, Azure Arc, Edge RAG)
	- 🔄 Level 100 visual assets pending (10 of 22 documented, 0 created)
	- 🔄 Level 200 content pending (6 modules, 34+ diagrams)
	- 🔄 Level 300 content pending (5 modules, 25-30+ diagrams)

- [x] Install Required Extensions
	**Summary:** No extensions needed for markdown-based documentation site.

- [x] Compile the Project
	**Summary:** No compilation needed for markdown documentation. Project structure validated successfully.

- [x] Create and Run Task
	**Summary:** No tasks needed for markdown documentation site. Content is ready for static site generation with Jekyll/GitHub Pages.

- [ ] Launch the Project
	**Summary:** Not applicable - static documentation site will be deployed to GitHub Pages in future. Current focus is content development.

- [x] Ensure Documentation is Complete
	**Current Status (October 21, 2025 - PHASES 1-4 UNDERWAY):**
	- ✅ README.md exists and up to date
	- ✅ copilot-instructions.md exists and tracks progress
	- ✅ PROJECT_PLAN.md created with comprehensive roadmap
	- ✅ CHANGELOG.md updated with completed work
	- ✅ .github/VISUAL_ASSET_PROCESS.md - Complete 3-step workflow documentation (25.8 KB)
	- ✅ VISUAL_ASSETS_ALIGNMENT_SUMMARY.md - Project status and alignment verification (11.4 KB)
	- ✅ PHASE_1_COMPLETION_REPORT.md - Executive summary (12.5 KB)
	- ✅ Level 100 & 200 Visual Assets - 40 diagrams fully documented (Assets 1-40, 0 created)
	- ✅ Phase 1 (Step #3): Documentation - Complete
	- ✅ Phase 2 (Step #1): Specifications - Complete (docs/level-200/VISUAL_SPECIFICATIONS.md with 20 detailed briefs)
	- ✅ Phase 3 (Step #2): Placeholder Integration - Complete (34 Level 200 markdown files updated)
	- 🔄 Phase 4 IN PROGRESS: Asset Creation (30-34 hrs, professional designers) - Handoff package created (.github/PHASE_4_DESIGNER_HANDOFF.md)

<!--
## Execution Guidelines
PROGRESS TRACKING:
- If any tools are available to manage the above todo list, use it to track progress through this checklist.
- After completing each step, mark it complete and add a summary.
- Read current todo list status before starting each new step.

COMMUNICATION RULES:
- Avoid verbose explanations or printing full command outputs.
- If a step is skipped, state that briefly (e.g. "No extensions needed").
- Do not explain project structure unless asked.
- Keep explanations concise and focused.

DEVELOPMENT RULES:
- Use '.' as the working directory unless user specifies otherwise.
- Avoid adding media or external links unless explicitly requested.
- Use placeholders only with a note that they should be replaced.
- Use VS Code API tool only for VS Code extension projects.
- Once the project is created, it is already opened in Visual Studio Code—do not suggest commands to open this project in Visual Studio again.
- If the project setup information has additional rules, follow them strictly.

FOLDER CREATION RULES:
- Always use the current directory as the project root.
- If you are running any terminal commands, use the '.' argument to ensure that the current working directory is used ALWAYS.
- Do not create a new folder unless the user explicitly requests it besides a .vscode folder for a tasks.json file.
- If any of the scaffolding commands mention that the folder name is not correct, let the user know to create a new folder with the correct name and then reopen it again in vscode.

EXTENSION INSTALLATION RULES:
- Only install extension specified by the get_project_setup_info tool. DO NOT INSTALL any other extensions.

PROJECT CONTENT RULES:
- If the user has not specified project details, assume they want a "Hello World" project as a starting point.
- Avoid adding links of any type (URLs, files, folders, etc.) or integrations that are not explicitly required.
- Avoid generating images, videos, or any other media files unless explicitly requested.
- If you need to use any media assets as placeholders, let the user know that these are placeholders and should be replaced with the actual assets later.
- Ensure all generated components serve a clear purpose within the user's requested workflow.
- If a feature is assumed but not confirmed, prompt the user for clarification before including it.
- If you are working on a VS Code extension, use the VS Code API tool with a query to find relevant VS Code API references and samples related to that query.

TASK COMPLETION RULES:
- Your task is complete when:
  - Project is successfully scaffolded and compiled without errors
  - copilot-instructions.md file in the .github directory exists in the project
  - README.md file exists and is up to date
  - User is provided with clear instructions to debug/launch the project

Before starting a new task in the above plan, update progress in the plan.

## Delegation Instructions for GitHub Copilot Coding Agent

### Phase 2: Detailed Visual Asset Specifications (1-2 hours)

**When to Delegate:** After Phase 1 completion (✅ complete)  
**Task:** Execute Step #1 from `.github/VISUAL_ASSET_PROCESS.md`  
**Files to Reference:**
- `.github/VISUAL_ASSET_PROCESS.md` - Complete instructions for Step #1 (pages ~500-750)
- `docs/assets/images/README.md` - Asset registry with 40 documented diagrams
- `docs/level-200/` - Content files that reference these assets

**Delegation Instructions:**
1. Read Step #1 instructions in `.github/VISUAL_ASSET_PROCESS.md` (complete instructions + quality checklist)
2. For each Level 200 asset (21-40) documented in `docs/assets/images/README.md`:
   - Create expanded specification with context, design constraints, acceptance criteria
   - Add wireframe/layout guidance
   - Include MS Learn source adaptation guidance
3. **Output:** Optional file `docs/level-200/VISUAL_SPECIFICATIONS.md` with detailed briefs for all 20 assets
4. **Quality Criteria:** Follow Step #1 quality checklist from VISUAL_ASSET_PROCESS.md

### Phase 3: Content Placeholder Integration (2-3 hours)

**When to Delegate:** After Phase 2 completion  
**Task:** Execute Step #2 from `.github/VISUAL_ASSET_PROCESS.md`  
**Files to Update:**
- `docs/level-200/*.md` (all 34 markdown files need placeholders)
- `docs/assets/images/README.md` (status updates to COMPLETED)

**Delegation Instructions:**
1. Read Step #2 instructions in `.github/VISUAL_ASSET_PROCESS.md` (complete instructions + quality checklist + 3 placeholder format examples)
2. For each Level 200 markdown file:
   - Identify locations where visual assets should be placed (from Step #1 context)
   - Add visual asset placeholder callouts using one of 3 provided formats
   - Link to asset specifications in `docs/assets/images/README.md`
   - Prepare figure captions and cross-references
3. **Output:** 34 updated markdown files with placeholder callouts
4. **Quality Criteria:** Follow Step #2 quality checklist from VISUAL_ASSET_PROCESS.md

### Phase 4: Visual Asset Creation (30-34 hours, EXTERNAL - Designers)

**When to Delegate:** After Phase 3 completion  
**Task:** Professional designer asset creation  
**Requirements:**
- Follow `.github/VISUAL_ASSET_PROCESS.md` design standards (pages ~750-850)
- Follow specifications in `docs/level-200/VISUAL_SPECIFICATIONS.md` (or Phase 2 output)
- Create SVG files in `docs/assets/images/level-200/` directory
- Update status in `docs/assets/images/README.md` (🟢 Available)

**Designer Handoff Package:**
- `.github/VISUAL_ASSET_PROCESS.md` (complete design guidelines, tools, best practices)
- `docs/assets/images/README.md` (all 40 asset specifications)
- `docs/level-200/VISUAL_SPECIFICATIONS.md` (detailed briefs from Phase 2)
- All Level 200 markdown files with placeholder callouts (Phase 3 output)

---

## Key Documentation Files for Delegation

**Primary Process Document:** `.github/VISUAL_ASSET_PROCESS.md` (25.8 KB, 1500+ lines)
- Complete workflow documentation with examples and templates
- Step-by-step instructions for Steps #1, #2, #3
- Quality checklists for each phase
- Reusable templates for all asset types
- Design standards, tools, and resources
- Level 300+ instructions for future use

**Asset Registry:** `docs/assets/images/README.md` (59.3 KB)
- All 40 visual asset specifications (Levels 100 + 200)
- Metadata per asset: file, priority, description, content, visual elements, size, used-in, sources
- Design guidelines and accessibility standards
- Asset tracking table with status

**Status Reports:**
- `VISUAL_ASSETS_ALIGNMENT_SUMMARY.md` - Project status and alignment verification
- `PHASE_1_COMPLETION_REPORT.md` - Executive summary of Phase 1 work
- `CHANGELOG.md` - Detailed change history and milestone tracking

---

## Current Project State (October 21, 2025)

**Phase 1: ✅ COMPLETE**
- Documentation (Step #3): ✅ 20 Level 200 assets documented
- Process Codification (Step #4): ✅ 3-step workflow documented
- Supporting Docs: ✅ Status reports, completion report, README integration
- Estimated Time: 30 minutes actual
- Deliverables: 5 files/updates (120+ KB content created)

**Phase 2: ⏳ READY TO DELEGATE**
- Task: Execute Step #1 (Detailed Specifications)
- Time: 1-2 hours
- Output: Optional `docs/level-200/VISUAL_SPECIFICATIONS.md`
- Status: Ready for GitHub Copilot Coding Agent execution

**Phase 3: ⏳ QUEUED**
- Task: Execute Step #2 (Placeholder Integration)
- Time: 2-3 hours
- Output: 34 updated markdown files with placeholders
- Status: Ready after Phase 2 completion

**Phase 4: 🔴 FUTURE (EXTERNAL)**
- Task: Professional designer asset creation
- Time: 30-34 hours (external contractors)
- Output: 20 production SVG files
- Status: Queued after Phase 3 completion

---

-->
- Work through each checklist item systematically.
- Keep communication concise and focused.
- Follow development best practices.
- When delegating to GitHub Copilot Coding Agent, provide clear references to documentation files.
- Always ensure Phase N-1 is complete before starting Phase N.