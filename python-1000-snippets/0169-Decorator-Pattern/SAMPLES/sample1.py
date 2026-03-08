# sample1.py
# coffee cost decorator chain (from README)

class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    def cost(self):
        return self._coffee.cost() + 1

if __name__ == '__main__':
    coffee = Coffee()
    coffee_with_milk = MilkDecorator(coffee)
    coffee_with_milk_sugar = SugarDecorator(coffee_with_milk)
    print('Total Cost:', coffee_with_milk_sugar.cost())
