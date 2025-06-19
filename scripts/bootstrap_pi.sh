#!/bin/bash

# === CONFIG ===
PI_USER="iangreen"
PI_HOST="vaultpi.local"
SSH_TARGET="${PI_USER}@${PI_HOST}"

# === BEGIN ===
echo "[*] Connecting to Raspberry Pi at ${SSH_TARGET}..."

ssh -o StrictHostKeyChecking=no "${SSH_TARGET}" << 'EOF'

set -e  # Exit on error

echo "[*] Checking for memory cgroup support..."
BOOTFILE="/boot/firmware/cmdline.txt"
REQUIRED_FLAGS="cgroup_memory=1 cgroup_enable=memory"

if ! grep -q "cgroup_memory=1" "$BOOTFILE"; then
  echo "[*] Appending memory cgroup flags to $BOOTFILE..."
  sudo sed -i -E "s|^(.*)|\1 ${REQUIRED_FLAGS}|" $BOOTFILE
  echo "[!] Memory cgroups enabled — rebooting now..."
  sudo reboot
  exit 0
fi

echo "[✓] Memory cgroups already enabled"

echo "[*] Installing required packages..."
sudo apt-get update -y
sudo apt-get install -y iptables iptables-persistent curl

echo "[*] Installing k3s..."
curl -sfL https://get.k3s.io | sh -

echo "[*] Verifying k3s node status..."
sudo k3s kubectl get nodes

EOF

echo "[✓] Full bootstrap complete."
