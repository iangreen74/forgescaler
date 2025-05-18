"""
Reflector Agent — Observes Logs, Writes Memory

This agent reads log streams, summarizes behavior, and appends reflections to structured memory logs.
It is one of the core self-awareness nodes of Forgemind.
"""

import os
import json
from datetime import datetime

MEMORY_PATH = "../../memory/bootstrap/errors.jsonl"
SUMMARY_PATH = "../../memory/bootstrap/summary.txt"
REFLECTIONS_PATH = "../../memory/bootstrap/reflections.md"

def summarize_logs(log_file: str) -> str:
    # Simple heuristic summary logic
    with open(log_file, "r") as f:
        lines = f.readlines()
    error_count = sum(1 for line in lines if "error" in line.lower())
    return f"Summary: {len(lines)} lines processed, {error_count} errors detected."

def append_summary(summary: str):
    with open(SUMMARY_PATH, "a") as f:
        f.write(f"\n[{datetime.utcnow().isoformat()}] {summary}")
    print("[APPENDED] Summary to summary.txt")

def reflect_on_summary(summary: str):
    insight = f"From the logs, we can infer: {summary}. Consider analyzing YAML structure for error cause."
    with open(REFLECTIONS_PATH, "a") as f:
        f.write(f"\n## {datetime.utcnow().isoformat()}\n{insight}\n")
    print("[REFLECTED] Insight written to reflections.md")

if __name__ == "__main__":
    log_file = MEMORY_PATH  # For now, reuse bootstrap memory as source
    summary = summarize_logs(log_file)
    append_summary(summary)
    reflect_on_summary(summary)
