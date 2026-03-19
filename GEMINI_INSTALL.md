# gstack for Gemini CLI Installation Guide

**gstack** is a set of advanced "skills" originally defined by Garry Tan, designed to transform your **Google Gemini CLI** into a virtual development team with CEO, Architect, and QA Engineer capabilities.

---

## 1. Prerequisites

Before installation, ensure your system has the following tools:

*   **Google Gemini CLI**: Properly installed and authenticated.
*   **Bun**: Required for the gstack browser testing tool (`browse`).
    *   Installation: `curl -fsSL https://bun.sh/install | bash`
*   **Git**: For version control and code tracking.

---

## 2. Installation Steps

### Step A: Create Skills Directory
Gemini CLI reads custom skills from `~/.gemini/skills` by default.

```bash
# Create the directory path
mkdir -p ~/.gemini/skills/gstack
```

### Step B: Move Ported Files to Destination
If you have already ported the files locally, copy them to the directory above:

```bash
# Assuming your current directory is the ported gstack_port
cp -r * ~/.gemini/skills/gstack/
```

### Step C: Run Setup Script
gstack needs to compile its internal `browse` binaries and configure the environment.

```bash
cd ~/.gemini/skills/gstack
chmod +x setup
./setup
```

> **Note (Windows Users)**: If you are using Git Bash or WSL, ensure you run this in a Unix-like environment. For native Windows, ensure `bun` is added to your PATH.

---

## 3. Configuring Gemini CLI

To ensure Gemini CLI recognizes these skills, verify the paths. Gemini CLI automatically scans for `SKILL.md` files under `~/.gemini/skills`.

You can check the configuration using:

```bash
# List currently loaded skills (depending on your Gemini CLI version)
gemini skills list
```

---

## 4. How to Use

Once installed, you can invoke the following features in your Gemini CLI session via description or direct command:

| Feature/Command | Role / Purpose | Recommended Usage |
| :--- | :--- | :--- |
| `/plan-ceo-review` | **CEO Mode** | Review product strategy, challenge vision, expand or trim scope. |
| `/plan-eng-review` | **Architect Mode** | Analyze system architecture, draw data flows, check error handling. |
| `/qa` | **QA Mode** | Launch headless browser tests for UI, discover bugs, and auto-fix. |
| `/review` | **Code Review** | Rigorous Staff Engineer-level security and logic audit. |
| `/investigate` | **Deep Investigation** | Root-cause analysis of complex, hard-to-debug issues. |
| `/ship` | **Ship Mode** | Prepare PRs, run final tests, and automate the release process. |

---

## 5. Key Changes (Gemini CLI Version)

Differences from the original `garrytan/gstack` (Claude Code version):

1.  **Path Changes**: All configurations and binaries are now located at `~/.gemini/skills/gstack`.
2.  **Tool Adaptation**: Original `Bash`, `Read`, and `Edit` commands are adapted to Gemini CLI's `run_shell_command`, `read_file`, and `replace`.
3.  **Context Optimization**: Skill instructions are tuned for Gemini's 1M+ Token Context, encouraging the agent to read more project context (e.g., `ARCHITECTURE.md`) for better decision-making.

---

## Troubleshooting

*   **Browser fails to start**: Ensure `~/.gemini/skills/gstack/browse/dist/browse` has execution permissions.
*   **Skills not found**: Ensure `SKILL.md` is in the root of `~/.gemini/skills/gstack/`.
*   **Path Conflicts**: If you have Claude Code installed, note that these now use independent configuration paths and do not interfere with each other.
