# sample1.py
# Merge two dictionaries with unpacking

def main():
    defaults = {"host": "localhost", "port": 8000}
    override = {"port": 8080, "debug": True}
    merged = {**defaults, **override}
    print("defaults:", defaults)
    print("override:", override)
    print("merged:", merged)


if __name__ == "__main__":
    main()
