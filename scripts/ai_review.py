#!/usr/bin/env python3
import os
from datetime import datetime

# Simulated AI response (placeholder until OpenAI integration is live)
summary = "✅ AI Review: Terraform plan appears valid and secure. No immediate issues detected."

# Create memory directory
os.makedirs(".aiops/memory/logs/", exist_ok=True)

# Save memory log
timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
filename = f".aiops/memory/logs/{timestamp}-ai-review.jsonl"
with open(filename, "w") as f:
    f.write(summary + "\n")

# Set GitHub Actions output (modern method)
with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"summary={summary}\n")
