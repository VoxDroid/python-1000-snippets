# sample1.py
# Simple builder constructing a product with parts

class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)


class Builder:
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("Part A")
        return self

    def build_part_b(self):
        self.product.add("Part B")
        return self

    def get_product(self):
        return self.product


def main():
    builder = Builder()
    product = builder.build_part_a().build_part_b().get_product()
    print(product.parts)


if __name__ == "__main__":
    main()
