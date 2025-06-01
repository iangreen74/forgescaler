# scripts/ai_review.py

import os
import openai
import json
from datetime import datetime

# Load API key and plan file
openai.api_key = os.getenv("OPENAI_API_KEY")

TERRAFORM_PLAN_FILE = "plan_output.txt"
OUTPUT_LOG = ".aiops/memory/logs"

SYSTEM_PROMPT = """
You are a DevOps AI assistant reviewing Terraform infrastructure plans. Your task is to:
- Identify any security risks or bad practices
- Note if IAM, S3, networking, or EKS resources are misconfigured
- Give a confidence score (0–100)
- Suggest improvements if needed

Respond in Markdown with a clear summary.
"""

def load_plan():
    if not os.path.exists(TERRAFORM_PLAN_FILE):
        return "[ERROR] Terraform plan file not found."
    with open(TERRAFORM_PLAN_FILE) as f:
        return f.read()

def analyze_plan(plan_text):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": plan_text[:12000]}  # truncate if too large
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages
    )
    return response.choices[0].message.content.strip()

def save_log(summary):
    os.makedirs(OUTPUT_LOG, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    path = os.path.join(OUTPUT_LOG, f"{timestamp}-ai-review.jsonl")
    data = {
        "timestamp": timestamp,
        "event": "ai_review",
        "summary": summary
    }
    with open(path, "w") as f:
        f.write(json.dumps(data))
    print(f"✅ AI Review log written to {path}")
    return summary

def main():
    plan = load_plan()
    result = analyze_plan(plan)
    summary = save_log(result)
    print("::set-output name=summary::" + summary.replace('\n', ' '))

if __name__ == "__main__":
    main()
