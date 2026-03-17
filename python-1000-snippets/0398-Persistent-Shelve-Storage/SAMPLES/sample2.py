
# sample2.py
# Demonstrate writeback behavior with mutable values.

import shelve
import tempfile

def main() -> None:
    with tempfile.TemporaryDirectory(prefix="shelve_") as tmpdir:
        db_path = tmpdir + "/data"
        with shelve.open(db_path, writeback=True) as db:
            db.setdefault("items", []).append("a")
            db.setdefault("items", []).append("b")
            db.sync()
            print("Items:", db["items"])

if __name__ == "__main__":
    main()
