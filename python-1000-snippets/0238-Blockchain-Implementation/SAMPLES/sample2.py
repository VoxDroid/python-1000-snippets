# sample2.py
# Demonstrate blockchain validation and tampering detection.

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

    def is_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i - 1]
            if current.previous_hash != prev.hash:
                return False
            if current.hash != current.calculate_hash():
                return False
        return True


def main():
    chain = Blockchain()
    chain.add_block("Transaction A -> B")
    chain.add_block("Transaction C -> D")

    print("Chain valid before tampering:", chain.is_valid())

    # Tamper with a block's data without updating its hash
    chain.chain[1].data = "Transaction A -> X"

    print("Chain valid after tampering:", chain.is_valid())


if __name__ == '__main__':
    main()
