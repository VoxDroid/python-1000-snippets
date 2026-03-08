# sample1.py
# Recursive determinant calculation

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for j in range(n):
        minor = [[matrix[i][k] for k in range(n) if k != j] for i in range(1, n)]
        det += ((-1)**j) * matrix[0][j] * determinant(minor)
    return det

if __name__ == '__main__':
    print(determinant([[1,2],[3,4]]))
