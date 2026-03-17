# sample1.py
# Custom iterator generating even numbers

class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        result = self.current
        self.current += 2
        return result


def main():
    evens = EvenNumbers(10)
    print("even numbers:", list(evens))


if __name__ == "__main__":
    main()
