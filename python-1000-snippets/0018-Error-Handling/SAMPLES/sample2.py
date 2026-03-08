# sample2.py
# Attempt to open a file that may not exist.

try:
    with open("nonexistent.txt") as f:
        print(f.read())
except FileNotFoundError as e:
    print("Caught error:", e)

