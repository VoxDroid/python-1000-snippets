# sample3.py
# Adapter used to make object compatible with expected interface

class LegacyCalculator:
    def add(self, x, y):
        return x + y


class CalculatorClient:
    def compute(self, calculator, x, y):
        # expects calculator to have `compute(x,y)` method
        return calculator.compute(x, y)


class CalculatorAdapter:
    def __init__(self, legacy):
        self.legacy = legacy

    def compute(self, x, y):
        return self.legacy.add(x, y)


def main():
    legacy = LegacyCalculator()
    adapter = CalculatorAdapter(legacy)
    client = CalculatorClient()
    print(client.compute(adapter, 3, 4))


if __name__ == "__main__":
    main()
