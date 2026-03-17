
# sample3.py
# Safer alternative using JSON.

import json

def main() -> None:
    data = {"key": "value", "count": 42}
    blob = json.dumps(data)
    restored = json.loads(blob)
    print("JSON restored:", restored)

if __name__ == "__main__":
    main()
