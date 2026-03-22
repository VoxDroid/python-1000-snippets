# sample2.py
# Classify risk levels from computed score.


def risk_level(score):
    if score > 2:
        return 'high'
    elif score > 1:
        return 'medium'
    return 'low'


if __name__ == '__main__':
    print('Risk level:', risk_level(1.7))
