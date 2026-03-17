
# sample1.py
# Store and retrieve a value using shelve.

import shelve
import tempfile

def main() -> None:
    with tempfile.TemporaryDirectory(prefix="shelve_") as tmpdir:
        db_path = tmpdir + "/data"
        with shelve.open(db_path) as db:
            db["key"] = "value"
            print("Stored:", db["key"])

if __name__ == "__main__":
    main()
