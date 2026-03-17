# sample1.py
# Basic flyweight factory sharing intrinsic state

class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state):
        return f"{self.shared_state} + {unique_state}"


class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self._flyweights:
            self._flyweights[shared_state] = Flyweight(shared_state)
        return self._flyweights[shared_state]


def main():
    factory = FlyweightFactory()
    fw1 = factory.get_flyweight("shared")
    print(fw1.operation("unique1"))
    fw2 = factory.get_flyweight("shared")
    print("same instance:", fw1 is fw2)


if __name__ == "__main__":
    main()
