# sample1.py
# Basic set algebra operations

def main():
    a = {1, 2, 3}
    b = {3, 4, 5}

    print("A:", a)
    print("B:", b)
    print("union:", a | b)
    print("intersection:", a & b)
    print("difference A-B:", a - b)
    print("symmetric difference:", a ^ b)


if __name__ == "__main__":
    main()
