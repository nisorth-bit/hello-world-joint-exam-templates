#!/usr/bin/env bash
# Cursor afterFileEdit hook: sync edited .md files to Notion
set -euo pipefail

input=$(cat)

# Extract file path from hook payload (Write / StrReplace / EditNotebook tools)
file_path=$(echo "$input" | python3 -c "
import sys, json
data = json.load(sys.stdin)
ti = data.get('tool_input', {})
path = ti.get('path', ti.get('target_notebook', ''))
print(path)
" 2>/dev/null || true)

if [[ -z "$file_path" ]]; then
  echo '{}' ; exit 0
fi

# Only process .md files inside the workspace
if [[ "$file_path" != *.md ]]; then
  echo '{}' ; exit 0
fi

WORKSPACE="/Users/naokinishimura/Desktop/整形外科雑誌/hello-world"
SYNC_SCRIPT="$WORKSPACE/.cursor/sync_to_notion.py"

# Run async so we don't block the agent
python3 "$SYNC_SCRIPT" "$file_path" >> "$WORKSPACE/.cursor/notion-sync.log" 2>&1 &

echo '{}'
