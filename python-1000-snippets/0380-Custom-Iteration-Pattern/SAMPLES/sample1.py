# sample1.py
# Custom iterator generating even numbers

class EvenNumbers:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_num:
            raise StopIteration
        result = self.current
        self.current += 2
        return result


def main():
    print(list(EvenNumbers(6)))


if __name__ == "__main__":
    main()
