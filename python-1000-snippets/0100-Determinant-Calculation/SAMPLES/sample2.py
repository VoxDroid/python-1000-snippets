# sample2.py
# Compute determinant of 3x3 and check singularity

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
    m = [[6,1,1],[4,-2,5],[2,8,7]]
    print('det', determinant(m))
    print('singular?', determinant([[1,2],[2,4]]) == 0)
