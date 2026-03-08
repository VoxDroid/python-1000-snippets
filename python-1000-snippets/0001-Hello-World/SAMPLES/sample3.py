# sample3.py
# Read greeting from a configuration file and print it.

import os

def load_greeting(filepath: str) -> str:
    with open(filepath) as f:
        return f.read().strip()

if __name__ == "__main__":
    base = os.path.dirname(__file__)
    greeting_file = os.path.join(base, "greeting.txt")
    greeting = load_greeting(greeting_file)
    print(greeting)
