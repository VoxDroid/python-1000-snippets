# sample1.py
# Basic strategy selection using objects

class Strategy:
    def execute(self, x):
        raise NotImplementedError


class Add(Strategy):
    def execute(self, x):
        return x + 1


class Multiply(Strategy):
    def execute(self, x):
        return x * 2


def main():
    strategies = {"add": Add(), "multiply": Multiply()}
    result = strategies["add"].execute(5)
    print("add result:", result)
    result = strategies["multiply"].execute(5)
    print("multiply result:", result)


if __name__ == "__main__":
    main()
