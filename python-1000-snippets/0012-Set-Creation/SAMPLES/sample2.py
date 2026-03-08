# sample2.py
# Demonstrate set union, intersection, and difference.

def main():
    a = {1, 2, 3}
    b = {3, 4, 5}
    print("Union:", a.union(b))
    print("Intersection:", a.intersection(b))
    print("Difference a-b:", a.difference(b))

if __name__ == '__main__':
    main()

