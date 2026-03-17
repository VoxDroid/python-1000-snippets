
# sample2.py
# Write an INI file programmatically.

import configparser
import os
import tempfile

def main() -> None:
    config = configparser.ConfigParser()
    config["database"] = {
        "host": "127.0.0.1",
        "port": "5432",
        "user": "dbuser",
    }

    with tempfile.TemporaryDirectory(prefix="ini_") as tmpdir:
        ini_path = os.path.join(tmpdir, "db.ini")
        with open(ini_path, "w", encoding="utf-8") as f:
            config.write(f)

        print("Wrote INI file to:", ini_path)
        print("Contents:")
        with open(ini_path, "r", encoding="utf-8") as f:
            print(f.read())

if __name__ == "__main__":
    main()
