# Smart Contract

## Description
This snippet demonstrates a simple smart contract simulation in Python.

## Code
```python
class SmartContract:
    def __init__(self):
        self.balances = {}
    def deposit(self, user, amount):
        if amount > 0:
            self.balances[user] = self.balances.get(user, 0) + amount
            return True
        return False
    def transfer(self, from_user, to_user, amount):
        if self.balances.get(from_user, 0) >= amount:
            self.balances[from_user] -= amount
            self.balances[to_user] = self.balances.get(to_user, 0) + amount
            return True
        return False

contract = SmartContract()
contract.deposit("Alice", 100)
contract.transfer("Alice", "Bob", 50)
print("Balances:", contract.balances)
```

## Output
```
Balances: {'Alice': 50, 'Bob': 50}
```

## Explanation
- **Smart Contract**: Simulates a contract managing user balances with deposit and transfer functions.
- **Logic**: Enforces rules like positive deposits and sufficient balance for transfers.
- **Complexity**: O(1) for operations.
- **Use Case**: Used as a simplified model for Ethereum smart contracts.
- **Best Practice**: Add validation; simulate gas costs; ensure atomicity.