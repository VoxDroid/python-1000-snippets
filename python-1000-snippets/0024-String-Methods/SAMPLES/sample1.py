# sample1.py
# Demonstrate various string methods on one text.

def main():
    text = "  Hello, Python Developers!  "
    print("Original:", repr(text))
    print("Upper:", text.upper())
    print("Lower:", text.lower())
    print("Stripped:", text.strip())
    print("Replaced:", text.replace("Python", "World"))
    print("Starts with '  He'?:", text.startswith("  He"))
    print("Count 'o':", text.count("o"))

if __name__ == '__main__':
    main()

