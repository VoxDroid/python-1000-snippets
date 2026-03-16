# sample1.py
# Fit an ARIMA(1,0,0) model to synthetic AR data and print AIC.

import numpy as np
from statsmodels.tsa.arima.model import ARIMA


def generate_ar1(length=200, phi=0.7, sigma=1.0, seed=0):
    np.random.seed(seed)
    eps = np.random.normal(scale=sigma, size=length)
    x = np.zeros(length)
    for t in range(1, length):
        x[t] = phi * x[t - 1] + eps[t]
    return x


if __name__ == '__main__':
    data = generate_ar1(length=200, phi=0.7, sigma=0.5)
    model = ARIMA(data, order=(1, 0, 0))
    fit = model.fit(method_kwargs={"warn_convergence": False})
    print("ARIMA(1,0,0) AIC:", fit.aic)

    # `fit.params` is a numpy array. The first parameter is typically the AR coefficient.
    ar_param = float(fit.params[0]) if len(fit.params) > 0 else float('nan')
    print(f"Estimated phi (AR coefficient): {ar_param:.3f}")
