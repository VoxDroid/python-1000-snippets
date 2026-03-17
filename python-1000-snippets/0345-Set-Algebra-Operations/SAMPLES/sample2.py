# sample2.py
# Set comprehensions for algebra operations

def main():
    a = {x for x in range(1, 6)}
    b = {x for x in range(4, 9)}

    print("A:", a)
    print("B:", b)
    print("A ∩ B:", {x for x in a if x in b})
    print("A ∪ B:", {x for x in a} | {x for x in b})


if __name__ == "__main__":
    main()
