# sample2.py
# Mean absolute error evaluation for demand forecast.


def mae(history, predicted):
    n=len(history)
    return sum(abs(h-p) for h,p in zip(history,predicted))/n

if __name__=='__main__':
    history=[10,12,14]
    predicted=[11,11,15]
    print('MAE:', mae(history,predicted))
