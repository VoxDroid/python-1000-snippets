# sample1.py
# Simple anomaly detection for fraud via z-score threshold.

import statistics


def detect_anomaly(txns, threshold=2):
    values = [t['amount'] for t in txns]
    mean = statistics.mean(values)
    stdev = statistics.pstdev(values)
    flags = []
    for t in txns:
        if stdev > 0 and abs(t['amount'] - mean) / stdev > threshold:
            flags.append((t['id'], True))
        else:
            flags.append((t['id'], False))
    return flags


if __name__ == '__main__':
    data = [{'id': 1, 'amount': 10}, {'id': 2, 'amount': 12}, {'id': 3, 'amount': 50}]
    print('Anomaly flags:', detect_anomaly(data))
