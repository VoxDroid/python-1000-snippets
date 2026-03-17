# sample1.py
# Complex lambda expression with conditional logic in map

def transform(data):
    return list(map(lambda x: x**2 if x > 0 else abs(x) + 1, data))


def main():
    data = [1, -2, 3, -4, 0]
    print("input:", data)
    print("transformed:", transform(data))


if __name__ == "__main__":
    main()
