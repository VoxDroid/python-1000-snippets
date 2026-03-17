# sample3.py
# frozenset and subset/superset checks

def main():
    fixed = frozenset([1, 2, 3])
    flexible = {1, 2, 3, 4}

    print("fixed (frozenset):", fixed)
    print("flexible:", flexible)
    print("fixed is subset of flexible:", fixed.issubset(flexible))
    print("flexible is superset of fixed:", flexible.issuperset(fixed))


if __name__ == "__main__":
    main()
