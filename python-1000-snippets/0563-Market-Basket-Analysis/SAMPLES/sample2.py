# sample2.py
# Identify frequent itemsets by minimum support.


def frequent_itemsets(transactions, min_support=0.5):
    n = len(transactions)
    counts = support_count(transactions)
    freq = [item for item, c in counts.items() if c / n >= min_support]
    return freq


def support_count(transactions):
    counts = {}
    for t in transactions:
        for item in t:
            counts[item] = counts.get(item, 0) + 1
    return counts


if __name__ == '__main__':
    txns = [['bread','milk'], ['milk','eggs'], ['bread','eggs']]
    print('Frequent items:', frequent_itemsets(txns, 0.5))
