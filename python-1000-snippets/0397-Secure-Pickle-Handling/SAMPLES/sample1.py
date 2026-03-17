
# sample1.py
# Basic pickle round-trip serialization.

import pickle

def main() -> None:
    data = {"key": "value", "count": 42}
    blob = pickle.dumps(data)
    restored = pickle.loads(blob)
    print("Restored:", restored)

if __name__ == "__main__":
    main()
