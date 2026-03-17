# sample3.py
# Polymorphism with composition: strategy pattern

class Greeter:
    def __init__(self, strategy):
        self.strategy = strategy

    def greet(self, name):
        return self.strategy.greet(name)


class FormalGreeting:
    def greet(self, name):
        return f"Good day, {name}."


class CasualGreeting:
    def greet(self, name):
        return f"Hey {name}!"


def main():
    formal = Greeter(FormalGreeting())
    casual = Greeter(CasualGreeting())
    print(formal.greet("Alice"))
    print(casual.greet("Bob"))


if __name__ == "__main__":
    main()
