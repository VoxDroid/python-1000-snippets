# sample1.py
# Basic blockchain implementation: create blocks and display the chain.

import hashlib
import time


class Block:
    def __init__(self, index: int, data: str, previous_hash: str):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        raw = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}".encode()
        return hashlib.sha256(raw).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self._create_genesis_block()]

    def _create_genesis_block(self) -> Block:
        return Block(0, "Genesis Block", "0")

    def add_block(self, data: str) -> Block:
        prev = self.chain[-1]
        block = Block(len(self.chain), data, prev.hash)
        self.chain.append(block)
        return block

    def print_chain(self):
        for block in self.chain:
            print(f"Block {block.index}: {block.hash} (prev {block.previous_hash})")


def main():
    chain = Blockchain()
    chain.add_block("Transaction A -> B")
    chain.add_block("Transaction C -> D")

    chain.print_chain()


if __name__ == '__main__':
    main()
