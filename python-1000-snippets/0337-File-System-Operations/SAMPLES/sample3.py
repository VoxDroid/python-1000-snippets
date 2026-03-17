"""Create and remove a temporary file under /temp."""

from pathlib import Path
import uuid


def create_temp_file(base_dir: Path, content: str) -> Path:
    base_dir.mkdir(parents=True, exist_ok=True)
    path = base_dir / f"tmp_{uuid.uuid4().hex}.txt"
    path.write_text(content, encoding="utf-8")
    return path


def cleanup(path: Path) -> None:
    if path.exists():
        path.unlink()


if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parents[1]
    temp_dir = repo_root / "temp"
    temp_file = create_temp_file(temp_dir, "temporary content")
    print("Created temporary file:", temp_file)
    cleanup(temp_file)
    print("Deleted temporary file:", temp_file)
