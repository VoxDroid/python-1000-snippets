# sample2.py
# Filter words longer than 3 characters using comprehension.

def main():
    words = ["apple", "to", "banana", "go"]
    long = [w for w in words if len(w) > 3]
    print(long)

if __name__ == '__main__':
    main()

