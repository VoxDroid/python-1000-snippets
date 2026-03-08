# sample1.py
# BankAccount example (matching README)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def get_balance(self):
        return self.__balance

if __name__ == '__main__':
    account = BankAccount('Alice', 1000)
    account.deposit(500)
    print('Balance:', account.get_balance())
