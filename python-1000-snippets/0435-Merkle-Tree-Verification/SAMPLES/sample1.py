# sample1.py
# Demonstrates computing a Merkle tree root for a list of leaves.

import hashlib


def merkle_root(leaves: list[bytes]) -> bytes:
    if not leaves:
        return b""

    nodes = [hashlib.sha256(leaf).digest() for leaf in leaves]

    while len(nodes) > 1:
        if len(nodes) % 2 == 1:
            nodes.append(nodes[-1])
        nodes = [
            hashlib.sha256(nodes[i] + nodes[i + 1]).digest()
            for i in range(0, len(nodes), 2)
        ]

    return nodes[0]


def main() -> None:
    leaves = [b"a", b"b", b"c", b"d"]
    root = merkle_root(leaves)
    print("Merkle root (hex):", root.hex())


if __name__ == "__main__":
    main()
