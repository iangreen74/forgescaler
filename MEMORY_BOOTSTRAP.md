# MEMORY_BOOTSTRAP.md

This file defines how to quickly sync assistant memory and regenerate repo context when resuming development.

---

## 🧠 What to Run Before Upload

### 1. Current Repo Tree Snapshot
```bash
tree -a -I '__pycache__|.git' -L 3 > vaultscaler_repo_tree_final.txt
```

### 2. Key Memory Files
- `.aiops/state/*.json`
- `.aiops/memory/logs/*.jsonl`
- `README.md`, `README.jetson.md`, `REPO_AUDIT.md`

### 3. Upload Sequence in Chat
- `vaultscaler_repo_tree_final.txt`
- Any current state JSON files
- Mention: “Resume VaultScaler memory using current repo snapshot and last push context”

---

## 🧭 Intent

To allow a clean reset between assistant sessions and retain full context of:

- Repo structure
- Active devices
- Memory logs
- Deployment strategies
