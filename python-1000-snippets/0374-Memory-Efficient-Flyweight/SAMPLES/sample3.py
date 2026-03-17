# sample3.py
# Flyweight factory with cache size reporting

class Flyweight:
    def __init__(self, state):
        self.state = state

    def operation(self, unique):
        return f"{self.state}::{unique}"


class FlyweightFactory:
    def __init__(self):
        self._cache = {}

    def get_flyweight(self, state):
        if state not in self._cache:
            self._cache[state] = Flyweight(state)
        return self._cache[state]

    def cache_size(self):
        return len(self._cache)


def main():
    factory = FlyweightFactory()
    factory.get_flyweight("x").operation("a")
    factory.get_flyweight("x").operation("b")
    factory.get_flyweight("y").operation("c")
    print("cache size:", factory.cache_size())


if __name__ == "__main__":
    main()
