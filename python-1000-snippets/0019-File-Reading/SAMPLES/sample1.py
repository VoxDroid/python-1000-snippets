# sample1.py
# Read an entire file and print each line with a line number.

def main():
    try:
        with open("example.txt", "r") as f:
            for idx, line in enumerate(f, start=1):
                print(f"{idx}: {line.rstrip()}")
    except FileNotFoundError:
        print("example.txt not found")

if __name__ == '__main__':
    main()

