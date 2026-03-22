# sample1.py
# Count item support in transactions.


def support_count(transactions):
    counts = {}
    for t in transactions:
        for item in t:
            counts[item] = counts.get(item, 0) + 1
    return counts


if __name__ == '__main__':
    txns = [['bread','milk'], ['milk','eggs']]
    print('Support:', support_count(txns))
