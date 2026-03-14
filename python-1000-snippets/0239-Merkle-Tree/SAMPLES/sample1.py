# sample1.py
# Build a Merkle tree from a list of items and print the root hash.

import hashlib


class MerkleTree:
    def __init__(self, leaves):
        self.leaves = [self._hash(item) for item in leaves]
        self.root = self._build_tree(self.leaves)

    @staticmethod
    def _hash(data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

    def _build_tree(self, nodes):
        if len(nodes) == 1:
            return nodes[0]
        parents = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i + 1] if i + 1 < len(nodes) else left
            parents.append(self._hash(left + right))
        return self._build_tree(parents)


def main():
    transactions = ["tx1", "tx2", "tx3", "tx4"]
    tree = MerkleTree(transactions)
    print("Merkle Root:", tree.root)


if __name__ == '__main__':
    main()
