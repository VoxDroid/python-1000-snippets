# sample2.py
# Use yield from to delegate to subgenerators

def group_by_size(strings):
    for s in strings:
        yield len(s), s


def main():
    words = ["apple", "banana", "cherry"]
    for size, word in group_by_size(words):
        print(f"{word} has length {size}")


if __name__ == "__main__":
    main()
