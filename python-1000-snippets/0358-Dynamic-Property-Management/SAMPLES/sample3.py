# sample3.py
# Dynamic attributes using __getattr__

class LazyObject:
    def __init__(self):
        self._cache = {}

    def __getattr__(self, name):
        if name.startswith("computed_"):
            value = len(name)
            self._cache[name] = value
            return value
        raise AttributeError(f"{type(self).__name__} has no attribute {name!r}")


def main():
    obj = LazyObject()
    print(obj.computed_value)  # computed on demand
    print(obj._cache)
    try:
        print(obj.missing)
    except AttributeError as e:
        print("error:", e)


if __name__ == "__main__":
    main()
