# sample1.py
# Generate a list of 5 random integers between 1 and 100.

import random

def main():
    nums = [random.randint(1, 100) for _ in range(5)]
    print("Random integers:", nums)

if __name__ == '__main__':
    main()

