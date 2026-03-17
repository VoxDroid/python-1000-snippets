
# sample2.py
# Serialize using json.dumps with a default function.

import json

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def default_serializer(obj):
    return getattr(obj, "__dict__", str(obj))

def main() -> None:
    p = Person("Bob", 25)
    print(json.dumps(p, default=default_serializer))

if __name__ == "__main__":
    main()
