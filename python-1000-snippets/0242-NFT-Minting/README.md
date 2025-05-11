# NFT Minting

## Description
This snippet demonstrates a simplified NFT minting simulation.

## Code
```python
import hashlib

class NFT:
    def __init__(self, owner, metadata):
        self.owner = owner
        self.metadata = metadata
        self.token_id = hashlib.sha256(f"{owner}{metadata}".encode()).hexdigest()
    def transfer(self, new_owner):
        self.owner = new_owner
        return self.token_id

nft = NFT("Alice", "Artwork#1")
print("Token ID:", nft.token_id)
print("New Owner:", nft.transfer("Bob"))
```

## Output
```
Token ID: <64-character SHA256 hash>
New Owner: <64-character SHA256 hash>
```

## Explanation
- **NFT Minting**: Simulates creating an NFT with a unique token ID and transferring ownership.
- **Logic**: Hashes owner and metadata to create a token ID; updates owner on transfer.
- **Complexity**: O(1) for minting and transfer.
- **Use Case**: Models NFT creation for blockchain platforms like Ethereum.
- **Best Practice**: Use blockchain for persistence; validate metadata; ensure uniqueness.