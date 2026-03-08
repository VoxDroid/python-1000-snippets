# sample1.py
# Write multiple lines to a file.

def main():
    with open("output.txt", "w") as f:
        f.write("Line 1\n")
        f.write("Line 2\n")
    print("Wrote lines to output.txt")

if __name__ == '__main__':
    main()

