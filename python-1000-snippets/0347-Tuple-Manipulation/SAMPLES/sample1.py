# sample1.py
# Tuple unpacking with starred expression

def main():
    data = (1, 2, 3, 4, 5)
    first, *middle, last = data
    print("data:", data)
    print("first:", first)
    print("middle:", middle)
    print("last:", last)


if __name__ == "__main__":
    main()
