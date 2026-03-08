# sample1.py
# Basic matrix multiplication implementation

def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    if cols_A != rows_B:
        return None
    C = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == '__main__':
    A = [[1,2],[3,4]]
    B = [[5,6],[7,8]]
    for row in matrix_multiply(A,B):
        print(row)
