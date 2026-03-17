# sample2.py
# Iterator that produces a fixed number of values

class RangeIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


def main():
    for i in RangeIterator(5):
        print(i)


if __name__ == "__main__":
    main()
