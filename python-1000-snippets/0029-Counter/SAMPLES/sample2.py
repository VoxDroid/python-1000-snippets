# sample2.py
# Use collections.Counter to count word frequencies.

from collections import Counter

def main():
    words = "apple banana apple cherry banana apple".split()
    c = Counter(words)
    print(c)
    print("apple appears", c['apple'], "times")

if __name__ == '__main__':
    main()

