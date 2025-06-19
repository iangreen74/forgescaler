#!/bin/bash
# bootstrap_jetson.sh

echo "Updating system and installing dependencies..."
sudo apt-get update
sudo apt-get install -y python3-pip curl

echo "Installing Python packages..."
pip3 install fastapi uvicorn onnxruntime opencv-python

echo "Launching inference agent..."
cd ~/vaultscaler/build/inference-agent
python3 app.py
