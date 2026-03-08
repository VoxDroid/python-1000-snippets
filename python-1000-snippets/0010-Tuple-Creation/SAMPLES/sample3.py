# sample3.py
# Demonstrate tuple packing and immutability.

def main():
    t = 1, 2, 3
    print("Packed tuple:", t)
    try:
        t[0] = 10
    except TypeError as e:
        print("Cannot modify tuple:", e)
    t = t + (4,)
    print("After concatenation:", t)

if __name__ == '__main__':
    main()

