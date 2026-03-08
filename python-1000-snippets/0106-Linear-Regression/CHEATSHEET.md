# 0106-Linear-Regression Cheatsheet

- For data points `(xi, yi)` compute:
  - `m = (n Σ xi yi - Σ xi Σ yi) / (n Σ xi² - (Σ xi)²)`
  - `b = (Σ yi - m Σ xi) / n`
- Predictions: `y_pred = m*x + b`.
- Can compute using vectors with NumPy: `m,b = np.polyfit(x,y,1)`.
- To evaluate fit quality compute R² coefficient:
  ```python
  ss_res = sum((yi - (m*xi+b))**2 for xi, yi in zip(x,y))
  ss_tot = sum((yi - mean(y))**2 for yi in y)
  r2 = 1 - ss_res/ss_tot
  ```
- Use least squares for simple models; extend to multiple regression with matrices.
