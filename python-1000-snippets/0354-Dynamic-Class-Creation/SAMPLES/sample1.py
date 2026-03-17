# sample1.py
# Create a class dynamically with type

def greet(self):
    return f"Hello, {self.name}!"


DynamicPerson = type("DynamicPerson", (), {"name": "World", "greet": greet})


def main():
    p = DynamicPerson()
    print(p.greet())


if __name__ == "__main__":
    main()
