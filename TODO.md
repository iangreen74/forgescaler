# TODO.md – Next Push

### 🧹 Repo Cleanup
- [ ] Remove or archive `infra/` (Terraform for EKS)
- [ ] Remove or archive `k8s/`
- [ ] Consider pruning `.mlops/` unless needed soon

### 🧠 Memory
- [ ] Validate `.aiops/memory/logs/` schema matches `.schema.json`
- [ ] Add device inventory entry to `.jsonl` for Jetson unit

### 📊 Dashboard
- [ ] Create `dashboard/index.html` to visualize all known devices
- [ ] Deploy via S3 + CloudFront (like vaultscaler.com)
- [ ] Pull from `.jsonl` or `.json` in public S3 bucket

### 🧪 GitHub Actions
- [ ] Add `log-device-shipment.yml` (manual trigger)
- [ ] Consider `tag-release.yml` for creating signed device builds

