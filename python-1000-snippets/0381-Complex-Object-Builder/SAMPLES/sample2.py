# sample2.py
# Builder pattern with optional parts and defaults

class Meal:
    def __init__(self):
        self.components = []

    def add(self, item):
        self.components.append(item)


class MealBuilder:
    def __init__(self):
        self.meal = Meal()

    def add_main(self, main):
        self.meal.add(main)
        return self

    def add_side(self, side):
        self.meal.add(side)
        return self

    def add_drink(self, drink):
        self.meal.add(drink)
        return self

    def get_meal(self):
        return self.meal


def main():
    meal = MealBuilder().add_main("Steak").add_side("Salad").add_drink("Water").get_meal()
    print(meal.components)


if __name__ == "__main__":
    main()
