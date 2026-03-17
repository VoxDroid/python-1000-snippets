"""Wrap third-party exceptions in a custom domain exception."""

from pathlib import Path


class FileProcessingError(Exception):
    pass


def read_config(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        raise FileProcessingError("Failed to read config file") from e


if __name__ == "__main__":
    path = Path("nonexistent_config.txt")
    try:
        read_config(path)
    except FileProcessingError as e:
        print("Caught custom file error:", str(e))
