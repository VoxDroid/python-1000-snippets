# sample1.py
# Risk scoring based on weighted features without numpy.


def weighted_risk(features, weights):
    score = sum(features[k] * weights.get(k, 0) for k in features)
    return round(score, 2)


if __name__ == '__main__':
    features = {'debt':1, 'credit_history':2, 'income':3}
    weights = {'debt':0.5, 'credit_history':0.3, 'income':0.2}
    print('Risk score:', weighted_risk(features, weights))
