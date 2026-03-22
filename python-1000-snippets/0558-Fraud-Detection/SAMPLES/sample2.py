# sample2.py
# Score transactions by risk rules and return suspicious entries.


def risk_score(txn):
    score = 0
    if txn['amount'] > 1000:
        score += 1
    if txn['location'] != 'home':
        score += 1
    return score


def suspicious(txns):
    return [t for t in txns if risk_score(t) >= 1]


if __name__ == '__main__':
    txns = [{'id':1,'amount':200,'location':'home'},{'id':2,'amount':1500,'location':'foreign'}]
    print('Suspicious:', suspicious(txns))
