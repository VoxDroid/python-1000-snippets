# sample1.py
# Demonstrate sorting numeric lists in-place and with sorted()

if __name__ == '__main__':
    numbers = [5, 2, 9, 1, 5, 6]
    print("original:", numbers)

    # in-place sort
    numbers.sort()
    print("sorted ascending:", numbers)

    # use sorted to create a new list descending
    numbers = [5, 2, 9, 1, 5, 6]
    desc = sorted(numbers, reverse=True)
    print("sorted descending (new list):", desc)
