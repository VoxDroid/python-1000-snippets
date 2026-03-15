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
    param_names = list(fit.model.param_names)
    params = fit.params
    if "ar.L1" in param_names:
        phi = params[param_names.index("ar.L1")]
    else:
        phi = float('nan')
    print(f"Estimated phi: {phi:.3f}")
