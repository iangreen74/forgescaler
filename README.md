# ForgeScaler

**ForgeScaler** is an AI-native operating system that powers the deployment, memory, and orchestration of sovereign AI infrastructure — starting with the [VaultScaler One](https://vaultscaler.com) security appliance.

Built for edge-first autonomy, ForgeScaler enables modular, reflective, fully offline systems capable of local inference, AI memory, and secure operational intelligence.

---

## 🏠 Powered Product: VaultScaler One

VaultScaler One is a plug-and-play AI security guard in a box:

- Runs facial recognition and threat detection **entirely offline**
- Logs memory and system state to `.aiops/memory/`
- Deploys using `bootstrap_jetson.sh` on **Jetson Orin NX**
- Ships with pre-configured ONNX models and sync logic

---

## 🧠 Core Concepts

### 🔁 Reflective Memory System

- All system actions and observations are recorded in `.jsonl` memory logs
- `.aiops/state/*.json` tracks per-device configuration
- Actions reflect into structured memory for analysis and reproducibility

### 🧩 Modular AI Agents

- `inference-agent`, `reflector-agent`, `intent-agent`, etc.
- Each unit of logic is containerized and version-controlled
- Helm-based charts for each service layer

---

## 🛠️ Repo Structure

- `build/inference-agent/` — FastAPI + ONNX runtime for vision models
- `charts/` — Helm charts for agents, inference, memory
- `scripts/` — Bootstrap, sync, layout validation, memory reflectors
- `.aiops/` — Memory logs, state files, triage handlers
- `README.jetson.md` — Hardware-specific Jetson One setup

---

## ⚙️ Features

- Runs on:
  - Raspberry Pi
  - Jetson Orin NX
  - Cloud-native EKS (for multi-node prototypes)
- Supports GitHub Actions for:
  - Plan validation
  - Reflective memory updates
  - Deployment lifecycle

---

## 🧭 Roadmap

- [x] Jetson Orin support
- [x] AIOps memory log system
- [x] VaultScaler One MVP live
- [ ] VaultStore plugin manager
- [ ] Live dashboard from `.jsonl` logs
- [ ] Multi-device orchestration (VaultMesh)

---

## 🔗 Related Projects

- 🔒 [VaultScaler One](https://vaultscaler.com) — Consumer-facing product powered by ForgeScaler
- 🌐 [iangreen.io](https://iangreen.io) — Creator site and system architecture journal

---

## 🧑‍💻 Author

Built by [Ian Green](https://iangreen.io)  
Las Vegas, NV · DevOps Engineer · Systems Architect
