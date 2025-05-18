"""
Planner Agent — From Reflection to Action Plan

This agent takes reflections and user intents, analyzes system context,
and generates high-level plans: infrastructure, code structure, or AI agent deployments.
"""

import os
from datetime import datetime

REFLECTIONS_PATH = "../../memory/bootstrap/reflections.md"
PLANS_PATH = "../../memory/bootstrap/plans/"
os.makedirs(PLANS_PATH, exist_ok=True)

def generate_plan(reflection: str) -> str:
    # Heuristic planner for now — AI-driven planner in future
    if "YAML" in reflection or "chart" in reflection.lower():
        return "Plan: Validate Helm charts using 'helm lint' and add schema enforcement to CI pipeline."
    elif "IAM" in reflection:
        return "Plan: Add missing IAM policies for CloudWatch logs access."
    return "Plan: Unknown pattern, flag for manual review."

def create_plan_file(reflection: str, plan: str):
    filename = os.path.join(PLANS_PATH, f"plan_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.txt")
    with open(filename, "w") as f:
        f.write(f"[REFLECTION]\n{reflection}\n\n[PLAN]\n{plan}\n")
    print(f"[PLAN CREATED] {filename}")

def process_latest_reflection():
    if not os.path.exists(REFLECTIONS_PATH):
        print("No reflections found.")
        return
    with open(REFLECTIONS_PATH, "r") as f:
        lines = f.readlines()
    latest = ''.join(lines[-10:])  # Simple way to grab recent reflection
    plan = generate_plan(latest)
    create_plan_file(latest, plan)

if __name__ == "__main__":
    process_latest_reflection()
