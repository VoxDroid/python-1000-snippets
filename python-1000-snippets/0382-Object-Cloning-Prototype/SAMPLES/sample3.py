# sample3.py
# Prototype registry for reusing template objects

import copy


class PrototypeRegistry:
    def __init__(self):
        self._prototypes = {}

    def register(self, key, prototype):
        self._prototypes[key] = prototype

    def clone(self, key):
        return copy.deepcopy(self._prototypes[key])


class Widget:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Widget({self.name})"


def main():
    registry = PrototypeRegistry()
    registry.register("button", Widget("Button"))
    registry.register("label", Widget("Label"))

    w1 = registry.clone("button")
    w2 = registry.clone("label")
    print(w1, w2)


if __name__ == "__main__":
    main()
