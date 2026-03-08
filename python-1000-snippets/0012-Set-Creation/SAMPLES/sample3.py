# sample3.py
# Check membership and modify a set.

def main():
    fruits = {"apple", "banana"}
    print("Has apple?", "apple" in fruits)
    fruits.add("cherry")
    fruits.discard("banana")
    print("After changes:", fruits)

if __name__ == '__main__':
    main()

