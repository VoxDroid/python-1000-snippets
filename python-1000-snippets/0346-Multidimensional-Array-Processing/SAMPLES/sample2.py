# sample2.py
# Flatten a nested list

def flatten(matrix):
    return [item for row in matrix for item in row]


def main():
    matrix = [[1, 2], [3, 4], [5, 6]]
    print("matrix:", matrix)
    print("flattened:", flatten(matrix))


if __name__ == "__main__":
    main()
