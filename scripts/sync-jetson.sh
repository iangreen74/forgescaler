#!/bin/bash
# sync-jetson.sh

STATE_FILE=".aiops/state/jetson.json"
LOG_FILE=".aiops/memory/logs/deployment_reflections.jsonl"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo "Updating sync timestamp..."
jq --arg ts "$TIMESTAMP" '.last_synced = $ts' "$STATE_FILE" > tmp.json && mv tmp.json "$STATE_FILE"

echo "Appending to memory log..."
cat "$STATE_FILE" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

echo "Sync complete."
