# sample3.py
# Verify a Merkle proof for a given leaf against a known root.

import hashlib


def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


def verify_proof(leaf: str, proof, root: str) -> bool:
    computed = leaf
    for sibling_hash, is_left in proof:
        if is_left:
            computed = hash_data(sibling_hash + computed)
        else:
            computed = hash_data(computed + sibling_hash)
    return computed == root


def main():
    # Example data
    data = ["tx1", "tx2", "tx3", "tx4"]
    leaf_index = 2

    # Build tree and proof using the same functions as sample2
    from sample2 import MerkleTree

    tree = MerkleTree(data)
    leaf_hash = tree.leaves[leaf_index]
    proof = tree.get_proof(leaf_index)

    print("Merkle root:", tree.root)
    print(f"Verifying leaf index {leaf_index} (hash={leaf_hash})")

    valid = verify_proof(leaf_hash, proof, tree.root)
    print("Proof valid:", valid)

    # Tamper with proof to show verification failure
    if proof:
        bad_proof = proof.copy()
        bad_proof[0] = ("0" * 64, bad_proof[0][1])
        print("Tampered proof valid:", verify_proof(leaf_hash, bad_proof, tree.root))


if __name__ == '__main__':
    main()
