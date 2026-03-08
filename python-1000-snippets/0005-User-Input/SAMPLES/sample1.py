# sample1.py
# Prompt for name and age, then echo back with conversion and trimming.

def main():
    name = input("Enter your name: ").strip()
    try:
        age = int(input("Enter your age: ").strip())
    except ValueError:
        print("Invalid age; must be a number.")
        return
    print(f"Hello, {name}! You are {age} years old.")

if __name__ == '__main__':
    main()

