# sample1.py
# Generator pipeline to filter and transform

def gen_range(n):
    for i in range(n):
        yield i


def even_numbers(nums):
    for n in nums:
        if n % 2 == 0:
            yield n


def squares(nums):
    for n in nums:
        yield n * n


def main():
    pipeline = squares(even_numbers(gen_range(10)))
    print("even squares:", list(pipeline))


if __name__ == "__main__":
    main()
