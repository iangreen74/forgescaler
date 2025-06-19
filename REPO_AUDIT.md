# REPO_AUDIT.md

## 🔍 Purpose

This repository powers **VaultScaler One**, an AI-powered, offline-first security appliance. It also includes the ForgeScaler operating system that governs deployment, memory logging, and AIOps-based orchestration.

---

## ✅ What's In This Repo

### Core
- `build/inference-agent/`: FastAPI + ONNX inference runtime
- `charts/inference-agent/`: Helm chart to deploy above as container
- `scripts/`: Bootstrap and sync tools for Jetson and Pi
- `models/`: Lightweight ONNX models (e.g. SqueezeNet)

### AI Memory + State
- `.aiops/state/*.json`: Live device memory snapshots
- `.aiops/memory/logs/*.jsonl`: Reflective memory over time
- `memory.schema.json`: Standard for memory structure

### GitHub Automation
- `.github/workflows/`: Reflect, apply, validate Terraform/Helm memory states

### AIOps Agents
- `agents/`: Modular logic agents (reflector, planner, etc.)

---

## 🗑️ Candidates for Removal
- `infra/`: EKS/cloud infra, currently unused
- `k8s/`: Cloud-native K8s YAMLs, may be deprecated
- `.mlops/`: Placeholder for retraining pipelines, not needed for MVP

---

## 🛠️ Future Considerations
- `vaultstore/`: Modular plug-in directory for adding AI capabilities
- `releases/`: Tag production-ready builds and QR data
- `dashboard/`: Web dashboard rendering device fleet from `.jsonl`

