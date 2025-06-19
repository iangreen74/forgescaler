#!/bin/bash

PI_USER="iangreen"
PI_HOST="vaultpi.local"
STATE_FILE=".aiops/state/raspberry-pi.json"
REFLECTION_LOG=".aiops/memory/logs/deployment_reflections.jsonl"

echo "[*] Connecting to ${PI_USER}@${PI_HOST}..."

JSON=$(ssh "${PI_USER}@${PI_HOST}" << 'EOF'
hostname=$(hostname)
ip=$(hostname -I | awk '{print $1}')
status=$(sudo k3s kubectl get nodes -o json | jq -r '.items[0].status.conditions[] | select(.type=="Ready") | .status')
images=$(sudo k3s ctr images ls -q | jq -R . | jq -s .)
pods=$(sudo k3s kubectl get pods -o json | jq '[.items[] | {name: .metadata.name, status: .status.phase}]')

jq -n --arg hostname "$hostname" \
      --arg ip "$ip" \
      --arg status "$status" \
      --argjson images "$images" \
      --argjson pods "$pods" \
      --arg time "$(date -Iseconds)" \
      '{
        type: "hardware_sync",
        target: "raspberry-pi",
        timestamp: $time,
        hostname: $hostname,
        ip: $ip,
        k3s_ready: ($status == "True"),
        images: $images,
        pods: $pods
      }'
EOF
)

echo "$JSON" > "$STATE_FILE"
echo "$JSON" >> "$REFLECTION_LOG"

echo "[✓] Pi state written to:"
echo "  - $STATE_FILE"
echo "  - $REFLECTION_LOG"
