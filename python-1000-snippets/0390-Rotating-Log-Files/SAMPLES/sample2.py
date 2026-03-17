
# sample2.py
# Uses a formatter with RotatingFileHandler.

import logging
import logging.handlers
import os
import tempfile


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="rotlog_fmt_") as tmpdir:
        log_path = os.path.join(tmpdir, "app.log")
        handler = logging.handlers.RotatingFileHandler(
            log_path, maxBytes=150, backupCount=2
        )
        handler.setFormatter(
            logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
        )

        logger = logging.getLogger("formatted")
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)

        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")

        print("Wrote logs to:", tmpdir)
        print("Files:")
        for fname in sorted(os.listdir(tmpdir)):
            print(" ", fname)


if __name__ == "__main__":
    main()
