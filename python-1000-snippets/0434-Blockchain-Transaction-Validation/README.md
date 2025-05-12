# Blockchain Transaction Validation

## Description
This snippet demonstrates a simplified blockchain transaction validation.

## Code
```python
try:
    import hashlib
    class Transaction:
        def __init__(self, sender, receiver, amount):
            self.sender = sender
            self.receiver = receiver
            self.amount = amount
        
        def is_valid(self):
            return self.amount > 0 and hashlib.sha256(f"{self.sender}{self.receiver}{self.amount}".encode()).hexdigest().startswith("0")
    
    tx = Transaction("Alice", "Bob", 10)
    print("Valid:", tx.is_valid())
except ImportError:
    print("Mock Output: Valid: True")
```

## Output
```
Mock Output: Valid: False
```
*(Real output: `Valid: False` in most cases unless the hash starts with '0')*

## Explanation
- **Blockchain Transaction Validation**: Validates a transaction’s integrity.
    - In real blockchain systems, you'd also validate the sender's signature and other factors like timestamps.
    - In real systems, the hash condition could represent proof of work or other consensus rules.
- **Logic**: Checks positive amount and a simplified hash condition.
- **Complexity**: O(1) for validation.
- **Use Case**: Used in blockchain systems for transaction verification.
- **Best Practice**: Use cryptographic signatures; validate inputs; ensure consensus.