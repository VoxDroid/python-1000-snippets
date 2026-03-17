# sample3.py
# Strategy pattern using functions rather than objects

def strategy_add(x):
    return x + 1


def strategy_mul(x):
    return x * 2


def apply_strategy(x, strategy_func):
    return strategy_func(x)


def main():
    print(apply_strategy(5, strategy_add))
    print(apply_strategy(5, strategy_mul))


if __name__ == "__main__":
    main()
