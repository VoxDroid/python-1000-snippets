# sample1.py
# Transpose a 2D list

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def main():
    matrix = [[1, 2, 3], [4, 5, 6]]
    print("matrix:", matrix)
    print("transposed:", transpose(matrix))


if __name__ == "__main__":
    main()
