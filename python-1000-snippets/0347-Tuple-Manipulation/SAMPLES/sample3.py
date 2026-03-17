# sample3.py
# Swap variables using tuple unpacking

def main():
    a, b = 1, 2
    print("before:", a, b)
    a, b = b, a
    print("after:", a, b)


if __name__ == "__main__":
    main()
