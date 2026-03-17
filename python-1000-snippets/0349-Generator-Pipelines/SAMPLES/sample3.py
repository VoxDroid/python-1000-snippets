# sample3.py
# Generator chain using yield from

def gen_numbers(n):
    for i in range(n):
        yield i


def gen_doubled(numbers):
    for x in numbers:
        yield x * 2


def gen_filtered(numbers):
    for x in numbers:
        if x % 3 == 0:
            yield x


def main():
    pipeline = gen_filtered(gen_doubled(gen_numbers(10)))
    print("filtered results:", list(pipeline))


if __name__ == "__main__":
    main()
