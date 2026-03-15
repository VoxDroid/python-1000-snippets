# sample3.py
# Fit an ARIMA model and inspect residuals.

import numpy as np
from statsmodels.tsa.arima.model import ARIMA


def generate_ar1(length=200, phi=0.7, sigma=0.5, seed=2):
    rng = np.random.default_rng(seed)
    eps = rng.normal(scale=sigma, size=length)
    x = np.zeros(length)
    for t in range(1, length):
        x[t] = phi * x[t - 1] + eps[t]
    return x


if __name__ == '__main__':
    data = generate_ar1()
    model = ARIMA(data, order=(1, 0, 0))
    fit = model.fit(method_kwargs={"warn_convergence": False})

    resid = fit.resid
    print("Residual mean:", np.mean(resid))
    print("Residual std:", np.std(resid))
    print("Residual first 5:", np.round(resid[:5], 4))
