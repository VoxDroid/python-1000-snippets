# sample2.py
# Convert credit score to rating category.


def credit_category(score):
    if score >= 750:
        return 'excellent'
    elif score >= 650:
        return 'good'
    elif score >= 550:
        return 'fair'
    return 'poor'


if __name__ == '__main__':
    score = 750
    print('Category:', credit_category(score))
