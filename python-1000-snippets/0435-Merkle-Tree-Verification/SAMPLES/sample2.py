# sample2.py
# Demonstrates generating and verifying a Merkle proof for a specific leaf.

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


def merkle_proof(leaves: list[bytes], index: int) -> list[tuple[bytes, bool]]:
    # Returns a list of (sibling_hash, is_left_sibling) along the path.
    nodes = [hashlib.sha256(leaf).digest() for leaf in leaves]
    proof = []

    while len(nodes) > 1:
        if len(nodes) % 2 == 1:
            nodes.append(nodes[-1])

        sibling_index = index ^ 1
        sibling_hash = nodes[sibling_index]
        is_left = sibling_index < index
        proof.append((sibling_hash, is_left))

        index //= 2
        nodes = [
            hashlib.sha256(nodes[i] + nodes[i + 1]).digest()
            for i in range(0, len(nodes), 2)
        ]

    return proof


def verify_proof(leaf: bytes, proof: list[tuple[bytes, bool]], root: bytes) -> bool:
    computed = hashlib.sha256(leaf).digest()
    for sibling_hash, is_left in proof:
        if is_left:
            computed = hashlib.sha256(sibling_hash + computed).digest()
        else:
            computed = hashlib.sha256(computed + sibling_hash).digest()
    return computed == root


def main() -> None:
    leaves = [b"a", b"b", b"c", b"d"]
    root = merkle_root(leaves)

    index = 2
    proof = merkle_proof(leaves, index)
    print("Merkle root:", root.hex())
    print("Proof for leaf index", index, [p[0].hex() for p in proof])

    valid = verify_proof(leaves[index], proof, root)
    print("Proof valid:", valid)


if __name__ == "__main__":
    main()
