# sample2.py
# Aggregate churn metrics and alert if churn risk high.


def churn_risk(customers):
    risk_count = sum(1 for c in customers if c['status'] == 'churn')
    total = len(customers)
    return risk_count / total if total else 0


if __name__ == '__main__':
    customers = [{'id': 1, 'status': 'retain'}, {'id': 2, 'status': 'churn'}]
    print('Churn risk fraction:', churn_risk(customers))
