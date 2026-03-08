# sample1.py
# Manually count occurrences of a character.

def main():
    text = "banana"
    char = "a"
    count = 0
    for c in text:
        if c == char:
            count += 1
    print(f"Character '{char}' appears {count} times.")

if __name__ == '__main__':
    main()

