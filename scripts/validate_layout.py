import os
import json
import sys

def load_layout():
    with open("project-layout.json") as f:
        return json.load(f)

def validate_dir(path, expected_dirs, expected_files):
    actual_dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    actual_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    errors = []

    for f in expected_files:
        if f not in actual_files:
            errors.append(f"Missing file: {os.path.join(path, f)}")

    for d in expected_dirs:
        parts = d.split("/")
        base = parts[0]
        sub = "/".join(parts[1:])
        if base not in actual_dirs:
            errors.append(f"Missing directory: {os.path.join(path, base)}")
        elif sub:
            sub_path = os.path.join(path, base)
            sub_dirs = [os.path.relpath(os.path.join(dp, d), path) for dp, dn, fn in os.walk(sub_path) for d in dn]
            if not any(sub in s for s in sub_dirs):
                errors.append(f"Missing nested directory: {os.path.join(path, d)}")

    return errors

def main():
    layout = load_layout()
    errors = []

    for dir_path, contents in layout.items():
        if not os.path.exists(dir_path):
            errors.append(f"Missing top-level directory: {dir_path}")
            continue

        expected_dirs = contents.get("dirs", [])
        expected_files = contents.get("files", [])
        errors.extend(validate_dir(dir_path, expected_dirs, expected_files))

    if errors:
        print("❌ Project layout validation failed:")
        for err in errors:
            print(" -", err)
        sys.exit(1)
    else:
        print("✅ Project layout is valid.")

if __name__ == "__main__":
    main()
