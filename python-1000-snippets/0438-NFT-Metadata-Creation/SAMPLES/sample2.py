# sample2.py
# Demonstrates computing a content hash for NFT metadata (e.g., for IPFS/CID).

import hashlib
import json


def metadata_hash(metadata: dict) -> str:
    # Use deterministic JSON serialization for hashing.
    serialized = json.dumps(metadata, separators=(",", ":"), sort_keys=True).encode("utf-8")
    return hashlib.sha256(serialized).hexdigest()


def main() -> None:
    metadata = {
        "name": "Example NFT",
        "description": "An example NFT metadata entry.",
        "image": "https://example.com/image.png",
        "attributes": [{"trait_type": "Rarity", "value": "Common"}],
    }

    print("Metadata hash (SHA-256):", metadata_hash(metadata))


if __name__ == "__main__":
    main()
