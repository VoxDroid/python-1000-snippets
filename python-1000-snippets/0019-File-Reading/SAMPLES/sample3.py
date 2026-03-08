# sample3.py
# Count total words in a file.

def main():
    try:
        with open("example.txt", "r") as f:
            text = f.read()
        words = text.split()
        print("Word count:", len(words))
    except FileNotFoundError:
        print("example.txt not found")

if __name__ == '__main__':
    main()

