# sample2.py
# Use properties to control access to a private attribute

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value


def main():
    acct = BankAccount(100)
    print("balance:", acct.balance)
    acct.balance = 200
    print("balance after deposit:", acct.balance)
    try:
        acct.balance = -50
    except ValueError as e:
        print("error:", e)


if __name__ == "__main__":
    main()
