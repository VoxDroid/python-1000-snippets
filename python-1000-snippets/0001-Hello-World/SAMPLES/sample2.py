# sample2.py
# Greet a user by name, demonstrating input and function usage

def greet(name: str):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    import sys
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    greet(name)
