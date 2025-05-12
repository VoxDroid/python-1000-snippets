# NFT Metadata Creation

## Description
This snippet demonstrates creating NFT metadata in JSON format.

## Code
```python
import json
nft_metadata = {
    "name": "My NFT",
    "description": "A unique digital asset",
    "image": "http://example.com/image.png"
}
print("Metadata:", json.dumps(nft_metadata))
```

## Output
```
Metadata: {"name": "My NFT", "description": "A unique digital asset", "image": "http://example.com/image.png"}
```

## Explanation
- **NFT Metadata Creation**: Generates metadata for an NFT.
- **Logic**: Creates a JSON dictionary with NFT attributes.
- **Complexity**: O(1) for creation.
- **Use Case**: Used for NFT minting on blockchain platforms.
- **Best Practice**: Follow standards (e.g., ERC-721); validate URLs; ensure uniqueness.