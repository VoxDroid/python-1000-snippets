
# sample1.py
# Load a JSON configuration file with defaults.

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
        # Create a config file to demonstrate loading.
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump({"username": "alice", "debug": True}, f)

        config = load_config(config_path)
        print("Loaded config:", config)

if __name__ == "__main__":
    main()
