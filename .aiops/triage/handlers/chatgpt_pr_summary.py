import os
import openai
import json
import subprocess

openai.api_key = os.getenv("OPENAI_API_KEY")

diff = subprocess.check_output(["git", "diff", "origin/main...HEAD"], text=True)
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a helpful AI code reviewer."},
    {"role": "user", "content": f"Please summarize and comment on this PR:
{diff}"}
  ]
)

summary = response.choices[0].message["content"]
print("AI Summary:")
print(summary)

# Write comment to file
with open("ai_review.txt", "w") as f:
    f.write(summary)
