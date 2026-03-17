"""Walk a directory tree and count files by extension."""

from pathlib import Path
from collections import Counter


def count_by_extension(root: Path):
    counter = Counter()
    for path in root.rglob("*"):
        if path.is_file():
            counter[path.suffix.lower()] += 1
    return counter


if __name__ == "__main__":
    root = Path(".")
    counts = count_by_extension(root)
    print("File counts by extension (top 10):", counts.most_common(10))
