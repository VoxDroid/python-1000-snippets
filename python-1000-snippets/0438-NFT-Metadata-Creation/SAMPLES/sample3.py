# sample3.py
# Demonstrates saving NFT metadata to a JSON file and computing a content hash.

import hashlib
import json
import os


def save_metadata(path: str, metadata: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, separators=(",", ":"), sort_keys=True)


def hash_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    metadata = {
        "name": "Example NFT", 
        "description": "An example NFT metadata entry.",
        "image": "https://example.com/image.png",
        "attributes": [{"trait_type": "Rarity", "value": "Common"}],
    }

    path = os.path.join("temp", "nft_metadata.json")
    save_metadata(path, metadata)

    print("Saved metadata to", path)
    print("SHA-256 hash:", hash_file(path))


if __name__ == "__main__":
    main()
