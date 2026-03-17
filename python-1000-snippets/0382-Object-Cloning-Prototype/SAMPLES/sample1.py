# sample1.py
# Prototype pattern with deep cloning

import copy


class Prototype:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)


def main():
    original = Prototype({"a": 1})
    cloned = original.clone()
    cloned.value["a"] = 2
    print("original:", original.value)
    print("cloned:", cloned.value)


if __name__ == "__main__":
    main()
