# sample1.py
# Simple threshold-based churn prediction rule.


def predict_churn(features):
    # features: dict with usage_hours and tickets
    score = features['usage_hours'] < 3 or features['tickets'] > 5
    return 'churn' if score else 'retain'


if __name__ == '__main__':
    profile = {'usage_hours': 2.5, 'tickets': 2}
    print('Prediction:', predict_churn(profile))
