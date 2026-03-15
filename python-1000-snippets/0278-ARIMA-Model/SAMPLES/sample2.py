# sample2.py
# Fit an ARIMA model and forecast future values.

import numpy as np
from statsmodels.tsa.arima.model import ARIMA


def generate_ar1(length=150, phi=0.6, sigma=0.5, seed=1):
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

    steps = 10
    forecast = fit.get_forecast(steps=steps)
    pred = forecast.predicted_mean
    conf_int = forecast.conf_int(alpha=0.05)

    print(f"Forecasting next {steps} values:")
    for i in range(steps):
        lo, hi = conf_int[i]
        print(f"  step {i+1}: {pred[i]:.3f} (95% CI: [{lo:.3f}, {hi:.3f}])")
