
# sample3.py
# Handle errors and cleanup when using shelve.

import os
import shelve
import tempfile

def main() -> None:
    with tempfile.TemporaryDirectory(prefix="shelve_") as tmpdir:
        db_path = tmpdir + "/data"
        try:
            with shelve.open(db_path) as db:
                db["hello"] = "world"
                print("Stored hello=world")
        except Exception as e:  # pragma: no cover
            print("Failed to open shelf:", e)
        finally:
            # Ensure artifacts are removed
            for f in os.listdir(tmpdir):
                os.remove(os.path.join(tmpdir, f))

if __name__ == "__main__":
    main()
