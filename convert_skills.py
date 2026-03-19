import os
import re

def convert_skill_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Paths: ~/.claude -> ~/.gemini
    content = content.replace('~/.claude', '~/.gemini')
    content = content.replace('.claude/', '.gemini/')
    
    # 2. Branding
    content = content.replace('Claude Code', 'Gemini CLI')
    content = content.replace('Claude', 'Gemini')
    content = content.replace('CC+gstack', 'Gemini+gstack')
    content = content.replace('CC ', 'Gemini CLI ')
    content = content.replace(' CC', ' Gemini CLI')
    
    # 3. Specific Tool Replacements (Targeted)
    # Only replace AskUserQuestion everywhere as it's a specific term
    content = content.replace('AskUserQuestion', 'ask_user')
    
    # 4. YAML Tools Mapping (Only in the YAML header)
    yaml_match = re.search(r'^---(.*?)---', content, re.DOTALL)
    if yaml_match:
        yaml_content = yaml_match.group(1)
        tool_map = {
            r'\bBash\b': 'run_shell_command',
            r'\bRead\b': 'read_file',
            r'\bWrite\b': 'write_file',
            r'\bEdit\b': 'replace',
            r'\bGrep\b': 'grep_search',
            r'\bGlob\b': 'glob',
            r'\bWebSearch\b': 'google_web_search',
        }
        new_yaml = yaml_content
        for pattern, replacement in tool_map.items():
            new_yaml = re.sub(pattern, replacement, new_yaml)
        content = content.replace(yaml_content, new_yaml)

    # 5. Gemini Emphasis
    gemini_emphasis = "\n\n(Optimized for Gemini CLI with long-context advantages. Use your massive context window to ingest entire files and maintain deep coherence.)"
    if 'description: |' in content and gemini_emphasis not in content:
        content = content.replace('description: |', 'description: |' + gemini_emphasis.replace('\n', '\n  '))

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Walk through all directories and find SKILL.md
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file == 'SKILL.md':
                convert_skill_md(os.path.join(root, file))

if __name__ == "__main__":
    main()
