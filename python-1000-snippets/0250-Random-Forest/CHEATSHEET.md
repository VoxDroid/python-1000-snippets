# 0250 - Random Forest Cheatsheet

- `RandomForestClassifier(n_estimators=..., oob_score=True)` trains ensemble trees.
- `model.feature_importances_` reveals which inputs matter most.
- OOB score is calculated using held-out samples from each tree.
- Use `max_depth`, `min_samples_leaf` to reduce overfitting.
