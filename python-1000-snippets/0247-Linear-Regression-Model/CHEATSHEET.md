# 0247 - Linear Regression Model Cheatsheet

- `LinearRegression()` fits `y = w*x + b` with least squares.
- Use `model.coef_` for the slope and `model.intercept_` for the intercept.
- Evaluate with `r2_score(y_true, y_pred)` or `model.score(X, y)`.
- Scale features if magnitudes differ widely.
