# scripts/render_dashboard.py

import os
import json
from datetime import datetime
from pathlib import Path
from jinja2 import Template

MEMORY_DIR = Path(".aiops/memory/logs")
OUTPUT_FILE = Path("dashboard.html")

TEMPLATE = Template("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>ForgeScaler Memory Dashboard</title>
    <style>
        body { font-family: sans-serif; background: #f4f4f4; padding: 2rem; }
        h1 { color: #333; }
        .entry { background: white; padding: 1rem; margin-bottom: 1rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .timestamp { font-size: 0.9rem; color: gray; }
    </style>
</head>
<body>
    <h1>ForgeScaler Memory Dashboard</h1>
    {% for log in logs %}
    <div class="entry">
        <div class="timestamp">{{ log.timestamp }}</div>
        <div><strong>Event:</strong> {{ log.event }}</div>
        <div><strong>Summary:</strong> {{ log.summary }}</div>
    </div>
    {% endfor %}
</body>
</html>
""")

def load_logs():
    logs = []
    if not MEMORY_DIR.exists():
        return logs

    for file in sorted(MEMORY_DIR.glob("*.jsonl")):
        with open(file) as f:
            try:
                data = json.loads(f.read())
                logs.append(data)
            except json.JSONDecodeError:
                continue
    return logs

def render():
    logs = load_logs()
    html = TEMPLATE.render(logs=logs)
    OUTPUT_FILE.write_text(html)
    print(f"✅ Dashboard rendered to {OUTPUT_FILE}")

if __name__ == "__main__":
    render()
