# sample3.py
# Builder that validates required parts before returning the product

class House:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)


class HouseBuilder:
    def __init__(self):
        self.house = House()
        self._has_walls = False

    def build_walls(self):
        self.house.add("walls")
        self._has_walls = True
        return self

    def build_roof(self):
        self.house.add("roof")
        return self

    def get_house(self):
        if not self._has_walls:
            raise ValueError("House must have walls")
        return self.house


def main():
    builder = HouseBuilder().build_walls().build_roof()
    house = builder.get_house()
    print(house.parts)


if __name__ == "__main__":
    main()
