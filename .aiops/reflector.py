import os
import json
import boto3
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
AWS_BUCKET = "forgescaler-memory"

def read_log_file(path="terraform.log"):
    with open(path, "r") as file:
        return file.read()

def summarize_log(log_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a DevOps assistant trained to analyze and reflect on infrastructure logs."},
            {"role": "user", "content": f"Please summarize the following terraform log, highlighting any issues, risks, or recommendations:\n\n{log_text}"}
        ],
        temperature=0.3
    )
    return response.choices[0].message["content"].strip()

def upload_to_s3(payload, filename):
    s3 = boto3.client("s3")
    s3.put_object(
        Bucket=AWS_BUCKET,
        Key=f"logs/{filename}",
        Body=json.dumps(payload, indent=2).encode("utf-8"),
        ContentType="application/json"
    )

def main():
    try:
        log = read_log_file()
        summary = summarize_log(log)
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H%M%SZ")
        payload = {
            "timestamp": timestamp,
            "summary": summary
        }
        upload_to_s3(payload, f"{timestamp}.jsonl")
        print("✅ Reflection uploaded to S3.")
    except Exception as e:
        print("❌ Error during reflection:", str(e))

if __name__ == "__main__":
    main()
