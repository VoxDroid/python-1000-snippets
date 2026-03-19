# 0438-NFT-Metadata-Creation Cheatsheet

- NFT metadata is typically JSON containing `name`, `description`, `image`, and `attributes`.
- For consistency, serialize JSON with sorted keys and stable separators before hashing.

## Hash metadata
```py
import hashlib, json
serialized = json.dumps(metadata, sort_keys=True, separators=(",", ":")).encode()
hash = hashlib.sha256(serialized).hexdigest()
```

## Notes
- IPFS and other content-addressed storage systems use these hashes to reference metadata.
- Ensure deterministic serialization to avoid hash mismatches.
