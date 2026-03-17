# sample1.py
# Bridge pattern separating abstraction from implementation

class Implementor:
    def action(self):
        raise NotImplementedError


class ConcreteImplementorA(Implementor):
    def action(self):
        return "Action A"


class ConcreteImplementorB(Implementor):
    def action(self):
        return "Action B"


class Abstraction:
    def __init__(self, implementor):
        self.implementor = implementor

    def operation(self):
        return self.implementor.action()


def main():
    bridge_a = Abstraction(ConcreteImplementorA())
    bridge_b = Abstraction(ConcreteImplementorB())
    print(bridge_a.operation())
    print(bridge_b.operation())


if __name__ == "__main__":
    main()
