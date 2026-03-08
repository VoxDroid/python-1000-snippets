# sample1.py
# Remove a specific element if present.

def main():
    animals = ["cat", "dog", "bird"]
    item = "dog"
    if item in animals:
        animals.remove(item)
    print("After removal:", animals)

if __name__ == '__main__':
    main()

