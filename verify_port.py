import os
import re

def contains_chinese(text):
    return re.search(r'[\u4e00-\u9fff]', text) is not None

def verify_project():
    results = {
        "non_english_files": [],
        "invalid_paths": [],
        "invalid_tools": []
    }
    
    for root, dirs, files in os.walk('.'):
        if '.git' in root: continue
        
        for file in files:
            file_path = os.path.join(root, file)
            
            # Check Markdown files for language and paths
            if file.endswith('.md'):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                    # 1. Check for Chinese characters
                    if contains_chinese(content):
                        results["non_english_files"].append(file_path)
                    
                    # 2. Check for leftover Claude paths
                    if '~/.claude' in content or '.claude/' in content:
                        results["invalid_paths"].append(file_path)
                    
                    # 3. Check for Claude-specific tool names in the YAML header
                    if file == 'SKILL.md':
                        header_match = re.search(r'^---(.*?)---', content, re.DOTALL)
                        if header_match:
                            header_content = header_match.group(1)
                            claude_tools = ['Bash', 'Read', 'Write', 'Edit', 'Grep', 'Glob', 'AskUserQuestion']
                            for t in claude_tools:
                                if re.search(rf'-\s+{t}\b', header_content):
                                    results["invalid_tools"].append(f"{file_path} (contains {t})")

    return results

if __name__ == "__main__":
    report = verify_project()
    print("=== VERIFICATION REPORT ===")
    print(f"Non-English files found: {len(report['non_english_files'])}")
    for f in report['non_english_files']: print(f"  - {f}")
    
    print(f"\nLeftover Claude paths: {len(report['invalid_paths'])}")
    for f in report['invalid_paths']: print(f"  - {f}")
    
    print(f"\nClaude tools detected: {len(report['invalid_tools'])}")
    for f in report['invalid_tools']: print(f"  - {f}")
    
    # Final check: Output a success message if all are clean
    if not any(report.values()):
        print("\nVerification STATUS: PASSED (100% English, Paths and Tools valid)")
    else:
        print("\nVerification STATUS: FAILED")
