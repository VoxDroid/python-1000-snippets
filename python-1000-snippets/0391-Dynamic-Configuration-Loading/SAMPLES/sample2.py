
# sample2.py
# Load config from a path specified by the CONFIG_PATH environment variable.

import json
import os
import tempfile

DEFAULT_CONFIG = {"username": "guest", "debug": False}

def load_config(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return DEFAULT_CONFIG.copy()

def main() -> None:
    with tempfile.TemporaryDirectory(prefix="config_") as tmpdir:
        config_path = os.path.join(tmpdir, "config.json")
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump({"username": "bob", "debug": False}, f)

        os.environ.setdefault("CONFIG_PATH", config_path)
        path = os.environ.get("CONFIG_PATH", config_path)
        config = load_config(path)
        print("Using config path:", path)
        print("Loaded config:", config)

if __name__ == "__main__":
    main()
