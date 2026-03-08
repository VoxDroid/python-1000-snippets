# sample1.py
# Demonstrate declaring variables of different types and printing them.

def main():
    name = "Alice"
    age = 30
    height = 5.7
    is_student = False
    print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

    # modify variables
    age += 1
    print("Next year age will be", age)

if __name__ == '__main__':
    main()

