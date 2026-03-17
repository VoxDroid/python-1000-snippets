
# sample1.py
# Serialize a custom object using a helper method.

import json

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def to_json(self) -> dict:
        return {"name": self.name, "age": self.age}

def main() -> None:
    p = Person("Alice", 30)
    print(json.dumps(p.to_json()))

if __name__ == "__main__":
    main()
