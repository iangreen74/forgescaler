import os
import re
import json
from pathlib import Path

VARIABLE_REGEX = re.compile(r'variable\s+"(\w+)"')
TFVARS_FILE = Path("infra/terraform.tfvars")
LOG_FILE = ".aiops/memory/logs/var_mismatch.jsonl"

def extract_variables(tf_dir):
    declared = set()
    for tf_file in Path(tf_dir).rglob("*.tf"):
        content = tf_file.read_text()
        declared.update(VARIABLE_REGEX.findall(content))
    return declared

def load_tfvars():
    defined = set()
    if not TFVARS_FILE.exists():
        return defined
    with open(TFVARS_FILE) as f:
        for line in f:
            match = re.match(r"(\w+)\s*=", line.strip())
            if match:
                defined.add(match.group(1))
    return defined

def write_mismatches(missing):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "w") as f:
        for var in missing:
            f.write(json.dumps({
                "type": "missing_tfvar",
                "variable": var,
                "source": "infra/variables.tf",
                "message": f"Required variable '{var}' not found in terraform.tfvars"
            }) + "\n")
    print(f"✅ Wrote {len(missing)} variable mismatch logs to {LOG_FILE}")

if __name__ == "__main__":
    declared_vars = extract_variables("infra")
    defined_vars = load_tfvars()
    missing_vars = declared_vars - defined_vars
    write_mismatches(missing_vars)
