# sample3.py
# Demonstrate list comprehensions and slicing.

def main():
    squares = [x*x for x in range(10)]
    print("Squares:", squares)
    odds = [x for x in range(10) if x % 2 == 1]
    print("Odd numbers:", odds)
    print("First three squares:", squares[:3])

if __name__ == '__main__':
    main()

