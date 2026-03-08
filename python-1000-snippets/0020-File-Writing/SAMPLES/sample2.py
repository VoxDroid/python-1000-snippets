# sample2.py
# Append a new line to the same file.

def main():
    with open("output.txt", "a") as f:
        f.write("Appended line\n")
    print("Appended to output.txt")

if __name__ == '__main__':
    main()

