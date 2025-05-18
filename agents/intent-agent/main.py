"""
Intent Agent — From Idea to Structure

This agent parses natural language user input and converts it into structured intent
objects for downstream planning and execution.
"""

import os
import json
from datetime import datetime

INTENT_INPUT_PATH = "../../memory/bootstrap/intents/"
STRUCTURED_INTENT_PATH = "../../memory/bootstrap/structured_intents/"
os.makedirs(STRUCTURED_INTENT_PATH, exist_ok=True)

def parse_user_input(prompt: str) -> dict:
    # Heuristic intent parser — AI model will replace this later
    intent = {
        "raw_prompt": prompt,
        "parsed": {
            "type": "web_app",
            "features": ["user auth", "file upload", "dashboard"],
            "tech_stack": ["React", "FastAPI", "S3", "EKS"]
        },
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    return intent

def save_structured_intent(intent: dict):
    filename = os.path.join(STRUCTURED_INTENT_PATH, f"intent_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.json")
    with open(filename, "w") as f:
        json.dump(intent, f, indent=2)
    print(f"[INTENT SAVED] {filename}")

def capture_and_process(prompt: str):
    intent = parse_user_input(prompt)
    save_structured_intent(intent)

if __name__ == "__main__":
    user_prompt = "Build a SaaS for vinyl album drops with user login and upload."
    capture_and_process(user_prompt)
