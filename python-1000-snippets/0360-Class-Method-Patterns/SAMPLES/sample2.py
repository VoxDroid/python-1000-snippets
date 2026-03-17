# sample2.py
# Class method that uses class-level state

class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
        return cls.count


def main():
    print(Counter.increment())
    print(Counter.increment())


if __name__ == "__main__":
    main()
