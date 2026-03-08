# sample3.py
# Sort list of tuples by the second element with itemgetter

from operator import itemgetter

if __name__ == '__main__':
    pairs = [("a", 2), ("b", 1), ("c", 3)]
    print("original:", pairs)

    pairs.sort(key=itemgetter(1))
    print("sorted by second element:", pairs)

    pairs = [("a", 2), ("b", 1), ("c", 3)]
    sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
    print("sorted descending by second element:", sorted_pairs)
