# sample2.py
# Custom sort using lambda as a key function

def sort_students(students):
    # Sort by score descending, then name ascending
    return sorted(students, key=lambda s: (-s["score"], s["name"]))


def main():
    students = [
        {"name": "Alice", "score": 88},
        {"name": "Bob", "score": 95},
        {"name": "Clara", "score": 95},
        {"name": "Dave", "score": 70},
    ]

    print("before:", students)
    print("after:", sort_students(students))


if __name__ == "__main__":
    main()
