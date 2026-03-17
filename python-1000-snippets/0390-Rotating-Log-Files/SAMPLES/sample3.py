
# sample3.py
# Demonstrates time-based rotation and manual rollover.

import logging
import logging.handlers
import os
import tempfile


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="timedrot_") as tmpdir:
        log_path = os.path.join(tmpdir, "app.log")
        handler = logging.handlers.TimedRotatingFileHandler(
            log_path, when="s", interval=1, backupCount=3
        )
        logger = logging.getLogger("timed")
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)

        # Write a few messages and force a rollover.
        logger.info("Before rollover")
        handler.doRollover()
        logger.info("After rollover")

        print("Generated logs in:", tmpdir)
        for fname in sorted(os.listdir(tmpdir)):
            print(" ", fname)


if __name__ == "__main__":
    main()
