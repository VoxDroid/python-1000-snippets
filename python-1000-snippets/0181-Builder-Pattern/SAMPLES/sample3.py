# sample3.py
# pizza builder with director class

class Pizza:
    def __init__(self):
        self.dough = ''
        self.sauce = ''
        self.toppings = []
    def __str__(self):
        return f"Pizza with {self.dough} dough, {self.sauce} sauce, toppings: {self.toppings}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    def set_dough(self, dough):
        self.pizza.dough = dough
        return self
    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self
    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self
    def build(self):
        return self.pizza

class Director:
    def __init__(self, builder):
        self.builder = builder
    def make_margherita(self):
        return self.builder.set_dough('thin').set_sauce('tomato').add_topping('cheese').build()

if __name__ == '__main__':
    director = Director(PizzaBuilder())
    print(director.make_margherita())
