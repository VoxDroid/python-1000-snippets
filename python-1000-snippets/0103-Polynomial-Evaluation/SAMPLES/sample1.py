# sample1.py
# Basic polynomial evaluation using Horner's method

def evaluate_polynomial(coeffs, x):
    result = 0
    for coef in reversed(coeffs):
        result = result * x + coef
    return result

if __name__ == '__main__':
    coeffs = [1,2,3]  # 1 + 2x + 3x^2
    print('P(2)=', evaluate_polynomial(coeffs, 2))
