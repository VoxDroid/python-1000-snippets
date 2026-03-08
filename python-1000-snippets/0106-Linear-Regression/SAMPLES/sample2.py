# sample2.py
# Compute R-squared to measure goodness of fit

def linear_regression(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_xx = sum(xi * xi for xi in x)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
    b = (sum_y - m * sum_x) / n
    return m, b

def r_squared(x, y, m, b):
    mean_y = sum(y)/len(y)
    ss_res = sum((yi - (m*xi + b))**2 for xi, yi in zip(x,y))
    ss_tot = sum((yi - mean_y)**2 for yi in y)
    return 1 - ss_res/ss_tot

if __name__ == '__main__':
    x=[1,2,3,4]; y=[2,4,5,4]
    m,b = linear_regression(x,y)
    print('r2', r_squared(x,y,m,b))
