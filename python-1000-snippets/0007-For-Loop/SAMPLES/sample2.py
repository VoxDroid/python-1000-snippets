# sample2.py
# Sum the first N natural numbers using a for loop.

def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

if __name__ == '__main__':
    print("Sum of 1..10 is", sum_n(10))

