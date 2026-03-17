# sample3.py
# Use cmp_to_key to sort by multiple criteria

from functools import cmp_to_key


def compare_scores(a, b):
    # Sort by score descending, then name ascending
    if a["score"] != b["score"]:
        return b["score"] - a["score"]
    return (a["name"] > b["name"]) - (a["name"] < b["name"])


def main():
    items = [
        {"name": "Alice", "score": 88},
        {"name": "Bob", "score": 95},
        {"name": "Clara", "score": 95},
    ]
    sorted_items = sorted(items, key=cmp_to_key(compare_scores))
    print("sorted:", sorted_items)


if __name__ == "__main__":
    main()
