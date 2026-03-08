# sample2.py
# Sort strings by length using key and reverse options

if __name__ == '__main__':
    words = ["banana", "pie", "Washington", "book"]
    print("original:", words)

    words.sort(key=len)
    print("sorted by length:", words)

    words = ["banana", "pie", "Washington", "book"]
    longest_first = sorted(words, key=len, reverse=True)
    print("longest first:", longest_first)
