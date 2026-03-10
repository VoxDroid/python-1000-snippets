# sample1.py
# house builder example from README

class House:
    def __init__(self):
        self.walls = None
        self.roof = None
    def __str__(self):
        return f"House with {self.walls} walls and {self.roof} roof"

class HouseBuilder:
    def __init__(self):
        self.house = House()
    def set_walls(self, walls):
        self.house.walls = walls
        return self
    def set_roof(self, roof):
        self.house.roof = roof
        return self
    def build(self):
        return self.house

if __name__ == '__main__':
    builder = HouseBuilder()
    house = builder.set_walls(4).set_roof("tile").build()
    print(house)    
