# sample2.py
# Select strategy with a configuration dictionary

class DiscountStrategy:
    def apply(self, amount):
        raise NotImplementedError


class NoDiscount(DiscountStrategy):
    def apply(self, amount):
        return amount


class TenPercent(DiscountStrategy):
    def apply(self, amount):
        return amount * 0.9


def get_strategy(config):
    mapping = {
        "none": NoDiscount,
        "10%": TenPercent,
    }
    return mapping.get(config, NoDiscount)()


def main():
    config = "10%"
    strategy = get_strategy(config)
    print("final:", strategy.apply(100))


if __name__ == "__main__":
    main()
