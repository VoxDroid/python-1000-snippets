# sample2.py
# Evaluate derivative as well

def evaluate_polynomial(coeffs, x):
    result = 0
    for coef in reversed(coeffs):
        result = result * x + coef
    return result

def derivative(coeffs):
    return [i * coeffs[i] for i in range(1, len(coeffs))]

if __name__ == '__main__':
    coeffs = [1, -4, 3]  # 1 -4x +3x^2
    print('P(5)=', evaluate_polynomial(coeffs, 5))
    print('P prime coeffs', derivative(coeffs))
    print("P' (5)=", evaluate_polynomial(derivative(coeffs), 5))
