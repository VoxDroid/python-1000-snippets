# sample2.py
# Sorting with a custom key function

def sort_people(people):
    # Sort by last name, then first name
    return sorted(people, key=lambda p: (p["last"].lower(), p["first"].lower()))


def main():
    people = [
        {"first": "John", "last": "Doe"},
        {"first": "Alice", "last": "Smith"},
        {"first": "Bob", "last": "doe"},
    ]
    print("before:", people)
    print("after:", sort_people(people))


if __name__ == "__main__":
    main()
