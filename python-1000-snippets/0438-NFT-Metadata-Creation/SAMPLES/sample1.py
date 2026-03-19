# sample1.py
# Demonstrates creating basic NFT metadata in JSON format.

import json


def create_nft_metadata(name: str, description: str, image_url: str) -> dict:
    return {
        "name": name,
        "description": description,
        "image": image_url,
        "attributes": [
            {"trait_type": "Rarity", "value": "Common"},
        ],
    }


def main() -> None:
    metadata = create_nft_metadata(
        "Example NFT",
        "An example NFT metadata entry.",
        "https://example.com/image.png",
    )

    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
