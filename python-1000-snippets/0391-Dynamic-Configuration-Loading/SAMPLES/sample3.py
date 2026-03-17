
# sample3.py
# Load configuration from a command-line argument.

import argparse
import json
import os

DEFAULT_CONFIG = {"username": "guest", "debug": False}

def load_config(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_CONFIG.copy()

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.json", help="Path to config file")
    args = parser.parse_args()

    config = load_config(args.config)
    print("Config:", config)

if __name__ == "__main__":
    main()
