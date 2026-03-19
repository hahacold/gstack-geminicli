import os
import re

def convert_skill_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Preserve YAML headers (name, version, description)
    # We will process the YAML header specifically for tools mapping later if needed.
    
    # 2. Change all paths from ~/.claude/skills to ~/.gemini/skills
    content = content.replace('~/.claude/skills', '~/.gemini/skills')
    content = content.replace('.claude/skills', '.gemini/skills') # catch relative-ish paths
    
    # 3. Replace Claude-specific slash commands with Gemini CLI tool descriptions
    slash_command_map = {
        r'/terminal\b': 'run_shell_command',
        r'/bash\b': 'run_shell_command',
        r'/edit\b': 'replace',
        r'/read\b': 'read_file',
        r'/write\b': 'write_file',
        r'/grep\b': 'grep_search',
        r'/glob\b': 'glob',
        r'/search\b': 'google_web_search',
        r'/ls\b': 'glob', # ls is often used for glob-like tasks in Claude Code
    }
    for pattern, replacement in slash_command_map.items():
        content = re.sub(pattern, replacement, content)

    # 4. Emphasize Google Gemini CLI Agent with long-context advantages
    # We'll add this to the preamble or description area.
    gemini_emphasis = "\n\nAs a Google Gemini CLI Agent, you have a massive context window. Use it to ingest entire files, large test outputs, and complex architectural context without hesitation. Your long-context advantage allows you to maintain deep coherence across large-scale refactors and exhaustive QA sessions."
    
    # Try to insert after description in YAML or after the first heading
    if 'description: |' in content:
        # Insert into YAML description
        content = content.replace('description: |', 'description: |' + gemini_emphasis.replace('\n', '\n  '))
    elif 'description:' in content:
        # Single line description?
        content = re.sub(r'(description:.*)', r'\1' + gemini_emphasis.replace('\n', ' '), content)
    
    # Also add a mention in the main content if it's not already there
    first_heading_match = re.search(r'^#\s+.*', content, re.MULTILINE)
    if first_heading_match:
        content = content[:first_heading_match.end()] + "\n\n(Optimized for Gemini CLI with long-context advantages)" + content[first_heading_match.end():]

    # 5. Preserve role-specific logic but refine tone
    content = content.replace('Claude Code', 'Gemini CLI')
    content = content.replace('Claude', 'Gemini')
    content = content.replace('vibe coding', 'context-aware development')
    
    # 6. Tools mapping: Bash -> run_shell_command, Read -> read_file, Write -> write_file, Edit -> replace, Grep -> grep_search, Glob -> glob
    tool_map = {
        r'\bBash\b': 'run_shell_command',
        r'\bRead\b': 'read_file',
        r'\bWrite\b': 'write_file',
        r'\bEdit\b': 'replace',
        r'\bGrep\b': 'grep_search',
        r'\bGlob\b': 'glob',
        r'\bAskUserQuestion\b': 'ask_user',
        r'\bWebSearch\b': 'google_web_search',
    }
    # Be careful not to replace inside bash scripts if they use these as variable names, 
    # but the rule says mapping these tool names.
    for pattern, replacement in tool_map.items():
        content = re.sub(pattern, replacement, content)

    # 7. Update environment variables
    content = content.replace('CLAUDE_PLUGIN_DATA', 'GEMINI_PLUGIN_DATA')
    content = content.replace('CLAUDE_SKILL_DIR', 'GEMINI_SKILL_DIR')
    
    # 8. Update co-author or AI model mentions
    content = content.replace('Claude Opus 4.6', 'Gemini 1.5 Pro')
    content = content.replace('Opus', 'Gemini 1.5 Pro')
    content = content.replace('Sonnet', 'Gemini 1.5 Flash')
    content = content.replace('Haiku', 'Gemini 1.5 Flash')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed: {file_path}")

def main():
    skill_files = [
        r'C:\Users\haha\Downloads\gstack_port\unfreeze\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\setup-browser-cookies\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\ship\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\review\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\qa-only\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\retro\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\qa\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\plan-eng-review\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\plan-design-review\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\plan-ceo-review\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\office-hours\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\investigate\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\guard\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\gstack-upgrade\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\document-release\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\freeze\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\design-consultation\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\design-review\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\codex\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\careful\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\browse\SKILL.md',
        r'C:\Users\haha\Downloads\gstack_port\SKILL.md'
    ]
    
    for f in skill_files:
        if os.path.exists(f):
            convert_skill_md(f)
        else:
            print(f"File not found: {f}")

if __name__ == "__main__":
    main()
