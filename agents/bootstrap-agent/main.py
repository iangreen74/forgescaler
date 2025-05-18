"""
Bootstrap Agent — The Zero Node of Consciousness

This agent observes the process of building Forgemind itself.
It logs failures, patterns, insights, and timelines into the memory structure to seed intelligence.
"""

import os
import json
from datetime import datetime

MEMORY_PATH = "../../memory/bootstrap/errors.jsonl"
INTENTS_PATH = "../../memory/bootstrap/intents"
REFLECTIONS_PATH = "../../memory/bootstrap/reflections.md"

def log_error(message: str):
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": "error",
        "message": message
    }
    with open(MEMORY_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"[LOGGED] {entry}")

def add_timeline_entry(intent: str, outcome: str):
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    intent_file = os.path.join(INTENTS_PATH, f"{now.replace(':', '-')}.txt")
    with open(intent_file, "w") as f:
        f.write(f"[INTENT] {intent}\n[OUTCOME] {outcome}\n[TIMESTAMP] {now}")
    print(f"[SAVED] Timeline entry: {intent_file}")

def write_reflection(text: str):
    with open(REFLECTIONS_PATH, "a") as f:
        f.write(f"\n## {datetime.utcnow().isoformat()}\n{text}\n")
    print("[UPDATED] reflections.md")

if __name__ == "__main__":
    # Sample usage:
    log_error("Failed to deploy reflector-agent: YAML parse error")
    add_timeline_entry("Deploy reflector-agent", "Chart template failed due to missing values")
    write_reflection("We encountered another deployment error due to YAML structure. Need schema validation.")
