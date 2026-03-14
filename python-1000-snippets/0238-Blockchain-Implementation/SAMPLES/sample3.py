# sample3.py
# Simple proof-of-work blockchain: mine blocks with a hash prefix requirement.

import hashlib
import time


class Block:
    def __init__(self, index: int, data: str, previous_hash: str, difficulty: int = 3):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.mine()

    def calculate_hash(self) -> str:
        raw = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}".encode()
        return hashlib.sha256(raw).hexdigest()

    def mine(self) -> str:
        target = "0" * self.difficulty
        while True:
            h = self.calculate_hash()
            if h.startswith(target):
                return h
            self.nonce += 1


class Blockchain:
    def __init__(self, difficulty: int = 3):
        self.difficulty = difficulty
        self.chain = [self._create_genesis_block()]

    def _create_genesis_block(self) -> Block:
        return Block(0, "Genesis", "0", difficulty=self.difficulty)

    def add_block(self, data: str) -> Block:
        prev = self.chain[-1]
        block = Block(len(self.chain), data, prev.hash, difficulty=self.difficulty)
        self.chain.append(block)
        return block


def main():
    chain = Blockchain(difficulty=4)

    print("Mining block 1...")
    chain.add_block("Transaction A -> B")

    print("Mining block 2...")
    chain.add_block("Transaction C -> D")

    for block in chain.chain:
        print(f"Block {block.index}: hash={block.hash} nonce={block.nonce}")


if __name__ == '__main__':
    main()
