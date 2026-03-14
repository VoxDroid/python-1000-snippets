# sample2.py
# Generate a Merkle proof for a leaf and print the proof steps.

import hashlib


class MerkleTree:
    def __init__(self, leaves):
        self.leaves = [self._hash(item) for item in leaves]
        self.levels = [self.leaves]
        self._build_tree()

    @staticmethod
    def _hash(data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

    def _build_tree(self):
        current = self.leaves
        while len(current) > 1:
            next_level = []
            for i in range(0, len(current), 2):
                left = current[i]
                right = current[i + 1] if i + 1 < len(current) else left
                next_level.append(self._hash(left + right))
            self.levels.append(next_level)
            current = next_level

    @property
    def root(self):
        return self.levels[-1][0] if self.levels else None

    def get_proof(self, index: int):
        proof = []
        for level in self.levels[:-1]:
            sibling_index = index ^ 1
            sibling = level[sibling_index] if sibling_index < len(level) else level[index]
            proof.append((sibling, sibling_index < index))
            index //= 2
        return proof


def main():
    data = ["tx1", "tx2", "tx3", "tx4"]
    tree = MerkleTree(data)

    target_index = 2
    proof = tree.get_proof(target_index)

    print("Merkle root:", tree.root)
    print(f"Proof for leaf index {target_index} (hash={tree.leaves[target_index]}):")
    for idx, (sibling_hash, is_left) in enumerate(proof):
        side = 'left' if is_left else 'right'
        print(f"  Level {idx}: sibling ({side}) = {sibling_hash}")


if __name__ == '__main__':
    main()
