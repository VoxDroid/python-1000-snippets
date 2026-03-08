# sample2.py
# bank account with Overdrawn and Normal states

class State:
    def deposit(self, acct, amount):
        pass
    def withdraw(self, acct, amount):
        pass

class NormalState(State):
    def deposit(self, acct, amount):
        acct.balance += amount
        if acct.balance < 0:
            acct.state = OverdrawnState()
    def withdraw(self, acct, amount):
        acct.balance -= amount
        if acct.balance < 0:
            acct.state = OverdrawnState()

class OverdrawnState(State):
    def deposit(self, acct, amount):
        acct.balance += amount
        if acct.balance >= 0:
            acct.state = NormalState()
    def withdraw(self, acct, amount):
        print('cannot withdraw, account overdrawn')

class Account:
    def __init__(self, balance=0):
        self.balance = balance
        self.state = NormalState()
    def deposit(self, amount):
        self.state.deposit(self, amount)
    def withdraw(self, amount):
        self.state.withdraw(self, amount)

if __name__ == '__main__':
    a = Account(50)
    a.withdraw(100)
    print('balance', a.balance, 'state', type(a.state).__name__)
    a.deposit(100)
    print('balance', a.balance, 'state', type(a.state).__name__)

