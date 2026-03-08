# sample2.py
# compute compound interest using arithmetic operations

def compound(principal, rate, times, years):
    return principal * ((1 + rate / times) ** (times * years))

if __name__ == '__main__':
    p = 1000
    r = 0.05
    t = 12
    y = 5
    amount = compound(p, r, t, y)
    print(f"After {y} years: {amount:.2f}")

