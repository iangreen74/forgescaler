"""
Memory Reflector Agent

This agent reads reflective memory logs and produces summarized insights
for long-term intelligence and historical awareness.
"""

import os
from datetime import datetime

MEMORY_DIR = "../../memory/bootstrap"
SUMMARY_PATH = "../../memory/bootstrap/summary.txt"

def summarize_reflections():
    reflections = []
    for fname in sorted(os.listdir(MEMORY_DIR)):
        if fname.endswith(".md"):
            with open(os.path.join(MEMORY_DIR, fname), "r") as f:
                reflections.append(f.read())

    summary = f"# Summary ({datetime.utcnow().isoformat()})\n\n"
    for r in reflections:
        lines = r.splitlines()
        title = next((l for l in lines if l.startswith("## ")), "Untitled")
        insight = next((l for l in lines if l.startswith("### Insight:")), "No insight found")
        summary += f"{title}\n{insight}\n\n"

    with open(SUMMARY_PATH, "a") as f:
        f.write(summary)
    print("[SUMMARY WRITTEN]")

if __name__ == "__main__":
    summarize_reflections()
