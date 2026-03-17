"""List files in the current directory and show their sizes."""

from pathlib import Path


def list_files_with_sizes(path: Path):
    return [(p.name, p.stat().st_size) for p in path.iterdir() if p.is_file()]


if __name__ == "__main__":
    root = Path(".")
    files = list_files_with_sizes(root)
    print("Files in current directory (first 5):", files[:5])
