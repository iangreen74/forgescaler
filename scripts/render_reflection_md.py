import os
import json
from datetime import datetime

LOGS_DIR = ".aiops/memory/logs"
REFLECT_DIR = ".aiops/memory/reflections"

def summarize_path_audit(path):
    if not os.path.exists(path):
        return "✅ No path mismatches detected."
    lines = open(path).readlines()
    if not lines:
        return "✅ No path mismatches detected."
    summary = ["❌ Path Mismatches:"]
    for line in lines:
        data = json.loads(line)
        summary.append(f"- `{data['referenced_path']}` in `{data['workflow']}`")
    return "\n".join(summary)

def summarize_var_mismatch(path):
    if not os.path.exists(path):
        return "✅ All required Terraform variables defined."
    lines = open(path).readlines()
    if not lines:
        return "✅ All required Terraform variables defined."
    summary = ["⚠️ Missing Terraform Variables:"]
    for line in lines:
        data = json.loads(line)
        summary.append(f"- `{data['variable']}` not found in tfvars.")
    return "\n".join(summary)

def summarize_locks(path):
    if not os.path.exists(path):
        return "✅ No stale Terraform locks found."
    lines = open(path).readlines()
    if not lines:
        return "✅ No stale Terraform locks found."
    summary = ["🔒 Active Lock(s) Detected:"]
    for line in lines:
        data = json.loads(line)
        summary.append(f"- `{data['LockID']}` in table `{data['Table']}`")
    return "\n".join(summary)

def generate_reflection():
    os.makedirs(REFLECT_DIR, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%SZ")
    md_path = os.path.join(REFLECT_DIR, f"summary-{timestamp}.md")

    with open(md_path, "w") as f:
        f.write(f"# 🔁 Reflection Log – {timestamp}\n\n")
        f.write("## 📐 Structure\n")
        f.write(summarize_path_audit(os.path.join(LOGS_DIR, "path_audit.jsonl")) + "\n\n")
        f.write("## 🧾 Terraform Inputs\n")
        f.write(summarize_var_mismatch(os.path.join(LOGS_DIR, "var_mismatch.jsonl")) + "\n\n")
        f.write("## 🔒 Lock State\n")
        f.write(summarize_locks(os.path.join(LOGS_DIR, "locks.jsonl")) + "\n")

    print(f"✅ Reflection log written to {md_path}")

if __name__ == "__main__":
    generate_reflection()
