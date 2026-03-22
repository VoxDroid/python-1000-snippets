# sample1.py
# Simple linear credit score model via coefficient features.


def credit_score(features, coeffs, base=300):
    score = base + sum(features[k] * coeffs.get(k, 0) for k in features)
    return int(score)


if __name__ == '__main__':
    features = {'income': 1, 'payment_history': 2}
    coeffs = {'income': 50, 'payment_history': 75}
    print('Credit score:', credit_score(features, coeffs))
