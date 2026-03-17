# sample3.py
# Iterator that returns successive tuples (similar to enumerate)

class Enumerate:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self.iterable)
        result = (self.index, value)
        self.index += 1
        return result


def main():
    for idx, value in Enumerate(["a", "b", "c"]):
        print(idx, value)


if __name__ == "__main__":
    main()
