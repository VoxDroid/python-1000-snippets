# sample1.py
# Create and update a student profile dictionary.

def main():
    student = {"name": "Alice", "age": 20, "major": "CS"}
    print("Original:", student)
    student["age"] = 21
    student["gpa"] = 3.8
    print("Updated:", student)

if __name__ == '__main__':
    main()

