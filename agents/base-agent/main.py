"""Base Agent — Common utilities for ForgeScaler agents."""

import logging
from datetime import datetime

class BaseAgent:
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(name)
        logging.basicConfig(level=logging.INFO)

    def log(self, message: str):
        timestamp = datetime.utcnow().isoformat()
        self.logger.info(f"[{timestamp}] {message}")

if __name__ == "__main__":
    agent = BaseAgent("base-agent")
    agent.log("Agent initialized")
