# gstack for Gemini CLI

**gstack-geminicli** is a collection of high-performance agentic "skills" designed to make AI-assisted development faster, safer, and more thorough. 

This is a port of the original [gstack](https://github.com/garrytan/gstack) (created by [Garry Tan](https://github.com/garrytan)) specifically optimized for **Google Gemini CLI**.

## Why gstack-geminicli?

By using Gemini 1.5 Pro with gstack-geminicli, you unlock the **2 Million Token context window**. 

While other agents struggle with large repositories, gstack-geminicli allows the agent to:
- **Ingest entire modules and test suites** in a single pass.
- **Maintain deep coherence** during complex, multi-file refactors.
- **Perform exhaustive QA** across hundreds of files without losing context.

## Installation

### 1. Requirements
- [Google Gemini CLI](https://github.com/google/gemini-cli) installed and authenticated.
- [GitHub CLI (gh)](https://cli.github.com/) (recommended for PR and issue workflows).
- **Shell Environment**: A Bash-compatible shell is required (native on macOS/Linux, or Git Bash/WSL on Windows).

### 2. Setup
Clone this repository and link the skills to your Gemini CLI skills directory:

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/gstack-geminicli.git
cd gstack-geminicli
```
# Link skills to Gemini CLI (Unix/macOS Example)
mkdir -p ~/.gemini/skills
ln -s $(pwd)/review ~/.gemini/skills/review
# ... or copy the folders to ~/.gemini/skills/
```

## Platform Support
- **macOS**: Fully supported (tested on zsh/bash).
- **Linux**: Fully supported.
- **Windows**: Supported via **Git Bash**, **PowerShell** (with coreutils), or **WSL**.

## Key Skills Included

| Skill | Command | Description |
|-------|---------|-------------|
| **Review** | `/review` | Deep PR analysis for safety, race conditions, and structural issues. |
| **QA** | `/qa` | Autonomous end-to-end testing and bug discovery. |
| **Ship** | `/ship` | Pre-flight checks and PR creation. |
| **Investigate** | `/investigate` | Root-cause analysis of complex bugs. |
| **Plan** | `/plan-eng` | Architectural design and engineering reviews. |
| **Browse** | `/browse` | Headless browser interaction for UI/UX testing. |

## Credits

Original concept and implementation by **Garry Tan**. 
Original repository: [https://github.com/garrytan/gstack](https://github.com/garrytan)

Ported to Gemini CLI by [Your Name/GitHub Account].

## License

MIT License (See [LICENSE](LICENSE) for details).
