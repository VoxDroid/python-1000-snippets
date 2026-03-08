# sample3.py
# Write CSV-like data by joining values.

def main():
    rows = [["name", "age"], ["Alice", "30"], ["Bob", "25"]]
    with open("output.txt", "w") as f:
        for row in rows:
            f.write(",".join(row) + "\n")
    print("Wrote CSV data to output.txt")

if __name__ == '__main__':
    main()

