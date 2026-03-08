# sample2.py
# Create a simple formatted table using width specifiers.

def main():
    data = [("Alice", 29), ("Bob", 34), ("Carol", 23)]
    for name, age in data:
        print(f"{name:<10} | {age:>3}")

if __name__ == '__main__':
    main()

