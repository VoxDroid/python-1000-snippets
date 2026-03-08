# sample1.py
# Compute slope and intercept for simple data set

def linear_regression(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_xx = sum(xi * xi for xi in x)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
    b = (sum_y - m * sum_x) / n
    return m, b

if __name__ == '__main__':
    x = [1,2,3,4]
    y = [2,4,5,4]
    m,b = linear_regression(x,y)
    print('line', m, b)
