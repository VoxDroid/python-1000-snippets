# sample1.py
# Simple linear demand forecast via slope/intercept.


def linear_forecast(history, future_t):
    n=len(history)
    x=list(range(1,n+1))
    y=history
    x_mean=sum(x)/n
    y_mean=sum(y)/n
    num=sum((xi-x_mean)*(yi-y_mean) for xi,yi in zip(x,y))
    den=sum((xi-x_mean)**2 for xi in x)
    slope=num/den if den else 0
    intercept=y_mean-slope*x_mean
    return int(intercept+slope*future_t)

if __name__=='__main__':
    history=[10,12,14]
    print('Forecasted demand for 4:', linear_forecast(history,4))
