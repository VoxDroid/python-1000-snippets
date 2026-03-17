
# sample1.py
# Write multiple log messages to trigger rotation and show rotated files.

import logging
import logging.handlers
import os
import tempfile


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="rotlog_") as tmpdir:
        log_path = os.path.join(tmpdir, "app.log")

        logger = logging.getLogger("rotating_logger")
        logger.setLevel(logging.INFO)
        handler = logging.handlers.RotatingFileHandler(
            log_path, maxBytes=200, backupCount=3
        )
        logger.addHandler(handler)

        for i in range(50):
            logger.info("Log message %d", i)

        # Show what files exist after rotation.
        print("Log files created in:", tmpdir)
        for fname in sorted(os.listdir(tmpdir)):
            fpath = os.path.join(tmpdir, fname)
            size = os.path.getsize(fpath)
            print(f"  {fname} ({size} bytes)")


if __name__ == "__main__":
    main()
