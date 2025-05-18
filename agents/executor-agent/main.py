"""
Executor Agent — Action Taker

This agent consumes generated plans and applies them, either by executing CLI actions,
opening GitHub pull requests, or updating Kubernetes resources.
"""

import os
from datetime import datetime

PLANS_PATH = "../../memory/bootstrap/plans/"
EXECUTIONS_LOG = "../../memory/bootstrap/executions.jsonl"

def execute_plan(plan_file: str):
    with open(plan_file, "r") as f:
        contents = f.read()

    # Simulate plan execution
    print(f"[EXECUTING] Plan from {plan_file}\n---\n{contents}\n---")
    action_summary = f"Executed simulated actions for: {os.path.basename(plan_file)}"

    log_execution(plan_file, action_summary)

def log_execution(plan_file: str, summary: str):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "plan_file": os.path.basename(plan_file),
        "result": summary
    }
    with open(EXECUTIONS_LOG, "a") as f:
        f.write(str(log_entry) + "\n")
    print(f"[LOGGED] Execution of {plan_file}")

def run_executor():
    if not os.path.exists(PLANS_PATH):
        print("No plans found.")
        return
    plan_files = sorted([os.path.join(PLANS_PATH, f) for f in os.listdir(PLANS_PATH)], reverse=True)
    if not plan_files:
        print("No plan files available.")
        return
    execute_plan(plan_files[0])  # Execute the most recent plan

if __name__ == "__main__":
    run_executor()
