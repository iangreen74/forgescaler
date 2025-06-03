import os
import json
import yaml

LAYOUT_FILE = "project-layout.json"
WORKFLOWS_DIR = ".github/workflows"
LOG_FILE = ".aiops/memory/logs/path_audit.jsonl"

def load_layout():
    with open(LAYOUT_FILE) as f:
        layout = json.load(f)

    valid_paths = set()
    for base, content in layout.items():
        valid_paths.add(base)
        for f in content.get("files", []):
            valid_paths.add(os.path.join(base, f))
        for d in content.get("dirs", []):
            valid_paths.add(os.path.join(base, d))
    return valid_paths

def scan_workflows(valid_paths):
    logs = []
    for root, _, files in os.walk(WORKFLOWS_DIR):
        for file in files:
            if not file.endswith(".yml"):
                continue
            path = os.path.join(root, file)
            with open(path) as f:
                try:
                    data = yaml.safe_load(f)
                except Exception as e:
                    logs.append({
                        "type": "parse_error",
                        "file": path,
                        "error": str(e)
                    })
                    continue

            # Scan for `run:` lines with path references
            steps = data.get("jobs", {}).get("reflect", {}).get("steps", [])
            for step in steps:
                run_cmd = step.get("run")
                if not run_cmd:
                    continue
                for word in run_cmd.split():
                    if "/" in word and not word.startswith("http"):
                        cleaned = word.strip(' "\'')
                        if cleaned not in valid_paths:
                            logs.append({
                                "type": "path_mismatch",
                                "workflow": path,
                                "referenced_path": cleaned,
                                "message": "Path not found in project-layout.json"
                            })
    return logs

def write_logs(logs):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "w") as f:
        for entry in logs:
            f.write(json.dumps(entry) + "\n")
    print(f"✅ Wrote {len(logs)} path audit results to {LOG_FILE}")

if __name__ == "__main__":
    valid_paths = load_layout()
    logs = scan_workflows(valid_paths)
    write_logs(logs)
