import os
import json

logs_dir = ".aiops/logs"
output_file = "docs/dashboard.html"

entries = []
for file in os.listdir(logs_dir):
    if file.endswith(".jsonl"):
        with open(os.path.join(logs_dir, file)) as f:
            entries.extend([json.loads(line) for line in f])

html = "<html><head><title>ForgeScaler AI Dashboard</title></head><body><h1>Memory Log Summary</h1><ul>"
for entry in entries[-20:]:  # Show last 20 entries
    html += f"<li>{entry.get('summary', str(entry))}</li>"
html += "</ul></body></html>"

with open(output_file, "w") as f:
    f.write(html)
