# Encapsulation

## Description
This snippet demonstrates encapsulation by using private attributes and public methods to access them.

## Code
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)
print("Balance:", account.get_balance())
```

## Output
```
Balance: 1500
```

## Explanation
- **Encapsulation**: Hides `__balance` (private) and provides access via public methods (`deposit`, `get_balance`).
- **Logic**: Ensures `balance` is modified safely (e.g., positive deposits).
- **Complexity**: O(1) for operations.
- **Use Case**: Used to protect data integrity and hide implementation details.
- **Best Practice**: Use `__` for private attributes; validate inputs in setters.