# gstack for Gemini CLI Usage Manual

Congratulations! You have successfully installed **gstack**. This toolset transforms your Gemini CLI into an AI team spanning the entire development lifecycle. This manual will guide you on how to efficiently use these new skills.

---

## 🚀 Quick Start: Core Command Table

You can enter the following commands in your conversation at any time (or simply describe your needs):

| Command | Role / Scenario | When to Use |
| :--- | :--- | :--- |
| `/office-hours` | **Startup Mentor** | When you have a new idea but haven't started coding yet. |
| `/plan-ceo-review` | **CEO Review** | Review feature scope, decide to "go big" or "lean MVP." |
| `/plan-eng-review` | **Architect Review** | Before coding, confirm architecture, data flow, and edge cases. |
| `/investigate` | **Detective Mode** | Deep-dive root-cause analysis for hard-to-debug issues. |
| `/qa` | **QA Engineer** | Automate browser tests and fix bugs after development. |
| `/review` | **Code Review** | Before merging, check security and logic. |
| `/design-review` | **Designer Mode** | Check UI alignment, spacing, and visual aesthetics. |
| `/ship` | **Release Manager** | Automate Changelog updates, versioning, and PR creation. |

---

## 🛠 Advanced Usage Guide

### 1. Automated QA and Repair (`/qa`)
One of gstack's most powerful features. It launches a headless browser to simulate real user actions.
*   **Command:** `/qa`
*   **Workflow:** Scan page -> Discover issue -> **Auto-modify source code** -> Re-test -> Commit code.
*   **Tip:** If your site requires login, run `/setup-browser-cookies` first to import cookies from Chrome/Edge.

### 2. Systematic Debugging (`/investigate`)
When you say "there's a bug here," Gemini might normally guess a fix. `/investigate` enforces this workflow:
1.  **Investigate**: Read logs and relevant code.
2.  **Analyze**: Identify error patterns.
3.  **Hypothesize**: Propose potential root causes.
4.  **Experiment**: Implement a fix only after verifying the hypothesis.

### 3. Security Guard (`/guard`)
If you are operating in a production environment or on critical source code:
*   Enter `/guard` to activate both **Careful Mode** (dangerous command warnings) and **Freeze Mode** (restricting modifications to specific directories).
*   Enter `/unfreeze` to unlock directories.

---

## 💻 Environment Notes

*   **Path Handling**: This installation uses standard Unix-style paths. In Gemini CLI, paths appear as `~/.gemini/skills/gstack/...`.
*   **Browser Engine**: The `browse` tool uses built-in Playwright Chromium. If you encounter network issues, ensure your firewall allows `browse` binary access.
*   **Permissions**: Ensure `setup` has been run to set the correct execution permissions for binaries.

---

## 🔄 Upgrades and Maintenance

gstack is continuously updated to adapt to the latest Gemini models.
*   Enter `/gstack-upgrade` to check and update to the latest version.

---

## 💡 Pro-Tips
gstack is **proactive**. When it detects you have completed a stage (e.g., just finished coding), it might suggest: "It looks like you're done. Should I run `/review` for you?"

You can adjust proactiveness via:
*   `gstack-config set proactive false` (Disable suggestions)
*   `gstack-config set proactive true` (Enable suggestions)
