# sample3.py
# Matrix multiplication (naive implementation)

def multiply(a, b):
    if not a or not b:
        return []
    num_rows = len(a)
    num_cols = len(b[0])
    common = len(b)
    result = [[0] * num_cols for _ in range(num_rows)]

    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(common):
                result[i][j] += a[i][k] * b[k][j]

    return result


def main():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    print("A:", a)
    print("B:", b)
    print("A * B:", multiply(a, b))


if __name__ == "__main__":
    main()
