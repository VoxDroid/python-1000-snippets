# sample2.py
# Filter even numbers from a list using a loop.

def filter_even(nums):
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
    return evens

if __name__ == '__main__':
    numbers = list(range(1, 11))
    print("Even numbers:", filter_even(numbers))

