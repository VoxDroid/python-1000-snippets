# sample2.py
# Read file line-by-line with explicit readline() calls.

def main():
    try:
        with open("example.txt", "r") as f:
            line = f.readline()
            while line:
                print(line.strip())
                line = f.readline()
    except FileNotFoundError:
        print("example.txt not found")

if __name__ == '__main__':
    main()

