# sample3.py
# Count occurrences of items in a list using Counter.

from collections import Counter

def main():
    nums = [1,2,2,3,3,3]
    c = Counter(nums)
    print(c)

if __name__ == '__main__':
    main()

