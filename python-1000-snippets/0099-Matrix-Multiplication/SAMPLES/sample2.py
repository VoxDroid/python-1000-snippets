# sample2.py
# Handle incompatible dimensions gracefully

def safe_multiply(A, B):
    if not A or not B:
        return None
    if len(A[0]) != len(B):
        print('incompatible dimensions')
        return None
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6]]
    B = [[7,8],[9,10]]  # compatible
    print('result', safe_multiply(A,B))
    C = [[1,2],[3,4]]
    # incompatible with A
    print('result', safe_multiply(A,C))
