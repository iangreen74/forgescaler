import json
import os

MEMORY_DIR = ".aiops/memory/logs"

def read_recent_events(n=5):
    events = []
    for fname in sorted(os.listdir(MEMORY_DIR), reverse=True):
        if fname.endswith(".jsonl"):
            with open(os.path.join(MEMORY_DIR, fname)) as f:
                for line in f:
                    try:
                        events.append(json.loads(line.strip()))
                    except:
                        continue
            if len(events) >= n:
                break
    return events[:n]

if __name__ == "__main__":
    recent = read_recent_events()
    print("🧠 Last Memory Events:")
    for event in recent:
        print(f"- [{event['timestamp']}] {event['event']}: {event.get('notes', '')}")
