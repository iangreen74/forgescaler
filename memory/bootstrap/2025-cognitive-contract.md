# Forgescaler Cognitive Contract (v1.0)

_“This system learns by doing, evolves by reflecting, and grows by remembering.”_

## 1. Lifecycle of Every Action

Each GitHub Action must follow:

### Before Execution

- AI scans memory logs (`.jsonl`, `.md`) from prior runs
- Compares planned actions to past attempts
- Warns of potential duplication, error patterns, or missed opportunities

### During Execution

- Logs plan/apply/deploy actions in `.jsonl`
- Tracks diffs and system changes

### After Execution

- Writes `.jsonl` and optional `.md` reflection
- Syncs memory to `s3://forgescaler-memory`
- Agents ingest memory and adapt behavior for future cycles

## 2. Fractal Reflection Principle

- Reflections are recursive and self-improving
- The system reflects not only on actions, but on how it reflects
- Failures, successes, and adaptations are all encoded

## 3. Persistence and Privacy

- Logs are versioned (Git)
- Synced and archived (S3)
- Never deleted — only learned from

## 4. Human–AI Synergy

- Human and AI co-author reflections
- Memory evolves through conversation, not just code
- Decisions are remembered and built upon

## 5. Implementation Hooks

| Stage        | Tooling                                         |
| ------------ | ----------------------------------------------- |
| Pre-run      | AI reads `forgescaler-memory/logs/*.jsonl`      |
| Post-run     | `.jsonl` + `.md` created by AI or GitHub Action |
| Storage      | `s3://forgescaler-memory`                       |
| Agent Access | Agents read logs from S3 or memory index        |
