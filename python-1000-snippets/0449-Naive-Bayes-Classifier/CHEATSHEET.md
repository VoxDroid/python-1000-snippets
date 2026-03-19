# 0449-Naive-Bayes-Classifier Cheatsheet

- **GaussianNB**: for continuous features assuming Gaussian distribution.
- **MultinomialNB**: for count data (e.g., word counts).
- **BernoulliNB**: for binary features (e.g., term presence).

Example:
```python
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, y)
```
