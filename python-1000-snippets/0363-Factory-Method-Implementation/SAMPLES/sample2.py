# sample2.py
# Factory with type registration to support extensibility

class Product:
    def use(self):
        raise NotImplementedError


class ConcreteA(Product):
    def use(self):
        return "Using A"


class ConcreteB(Product):
    def use(self):
        return "Using B"


class ProductFactory:
    _registry = {}

    @classmethod
    def register(cls, key, product_cls):
        cls._registry[key] = product_cls

    @classmethod
    def create(cls, key):
        if key not in cls._registry:
            raise ValueError(f"Unknown product: {key}")
        return cls._registry[key]()


ProductFactory.register("A", ConcreteA)
ProductFactory.register("B", ConcreteB)


def main():
    print(ProductFactory.create("A").use())
    print(ProductFactory.create("B").use())


if __name__ == "__main__":
    main()
