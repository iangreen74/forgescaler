import boto3
import json
import os
from datetime import datetime

region = os.environ.get("AWS_REGION", "us-east-1")
client = boto3.client("dynamodb", region_name=region)

DYNAMODB_TABLES = [
    "forgescaler-terraform-locks",
    "terraform-locks"
]

TARGET_LOCK_IDS = [
    "forgescaler-terraform-state/infra/terraform.tfstate",
    "forgescaler-terraform-state/landing/terraform.tfstate"
]

def fetch_locks(table_name):
    client = boto3.client("dynamodb")
    try:
        response = client.scan(TableName=table_name)
        items = response.get("Items", [])
        return [{
            "LockID": item["LockID"]["S"],
            "Digest": item.get("Digest", {}).get("S", ""),
            "Timestamp": datetime.utcnow().isoformat(),
            "Table": table_name
        } for item in items if item["LockID"]["S"] in TARGET_LOCK_IDS]
    except Exception as e:
        print(f"Error scanning table {table_name}: {e}")
        return []

def log_locks(locks, path=".aiops/memory/logs/locks.jsonl"):
    with open(path, "a") as f:
        for lock in locks:
            f.write(json.dumps(lock) + "\n")

if __name__ == "__main__":
    all_locks = []
    for table in DYNAMODB_TABLES:
        all_locks.extend(fetch_locks(table))
    if all_locks:
        log_locks(all_locks)
        print(f"🔒 Logged {len(all_locks)} active lock(s) to memory.")
    else:
        print("✅ No active tracked locks found.")
